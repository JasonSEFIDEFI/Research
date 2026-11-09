"""Self-consistent spherical scalar-Maxwell continuation. Dimensionless; exploratory."""
from pathlib import Path
import json, hashlib, platform
import numpy as np
import scipy
from scipy.integrate import solve_bvp, simpson
HERE=Path(__file__).resolve().parent
W=1.401223084350689

def solve(q, previous=None, radius=120., tol=1e-7):
    r=np.linspace(0,radius,801)
    if previous is None:
        data=np.loadtxt(HERE/'seed_profile.csv',delimiter=',',skiprows=1)
        f=np.interp(r,data[:,0],data[:,1],right=0.)
        s=np.interp(r,data[:,0],data[:,2],right=.5)
        y=np.array([f,np.gradient(f,r),s,np.gradient(s,r),r*0,r*0])
    else:
        sol,old_radius=previous
        y=sol.sol(np.minimum(r,old_radius))
        outside=r>old_radius
        y[0,outside]=0; y[1,outside]=0; y[2,outside]=.5; y[3,outside]=0
        y[4,outside]=sol.y[4,-1]*old_radius/r[outside]
        y[5,outside]=-sol.y[4,-1]*old_radius/r[outside]**2
    y[[1,3,5],0]=0
    def fun(r,y):
        f,fp,s,sp,a,ap=y; om=W-q*a
        return np.array([fp,(1+f*f+4*s*s-om*om)*f,sp,(4*f*f+12*s*s-3)*s,ap,-q*om*f*f])
    def bc(a,b):
        return np.array([a[1],a[3],a[5],b[0],b[2]-.5,b[5]+b[4]/radius])
    singular=np.diag([0.,-2,0,-2,0,-2])
    sol=solve_bvp(fun,bc,r,y,S=singular,tol=tol,bc_tol=1e-11,max_nodes=30000)
    r=np.linspace(0,radius,24001)
    f,fp,s,sp,a,ap=sol.sol(r); om=W-q*a
    integrate=lambda z:float(simpson(4*np.pi*r*r*z,x=r))
    number=integrate(om*f*f); charge=q*number; flux=-4*np.pi*radius**2*ap[-1]
    potential=f**4/4+f*f/2+2*f*f*s*s+3*(s*s-.25)**2
    kinetic=integrate((fp*fp+sp*sp)/2)
    time=integrate(om*om*f*f/2); U=integrate(potential)
    electric_inside=integrate(ap*ap/2); electric_tail=2*np.pi*radius*a[-1]**2
    energy=kinetic+time+U+electric_inside+electric_tail
    nodes=int(np.count_nonzero(np.diff(np.sign(f[abs(f)>max(1e-8,max(abs(f))*1e-5)]))))
    flux_error=abs(flux-charge)/max(abs(charge),1e-20)
    record=dict(q=q,omega=W,lambda_sigma=12,radius=radius,tolerance=tol,status=int(sol.status),
        nodes=len(sol.x),max_rms_residual=float(max(sol.rms_residuals)),boundary_residual=float(max(abs(bc(sol.y[:,0],sol.y[:,-1])))),
        central_f=float(f[0]),central_s=float(s[0]),central_a=float(a[0]),central_frequency=float(om[0]),
        radial_nodes=nodes,charge_number=number,electric_charge=charge,gauss_flux=float(flux),gauss_relative_error=flux_error,
        energy=energy,energy_per_number=energy/number,free_scalar_mass=float(np.sqrt(2)),
        scalar_gradient_energy=kinetic,scalar_time_energy=time,potential_energy=U,
        electric_energy_inside=electric_inside,electric_energy_tail=electric_tail,
        gauss_energy_identity_relative=abs(time+electric_inside+electric_tail-W*number/2)/energy,
        scalar_outer_f=float(abs(f[-2])),
        accepted=bool(sol.status==0 and f[0]>.001 and nodes==0 and number>1 and flux_error<1e-5 and max(sol.rms_residuals)<tol))
    return record,(sol,radius)

if __name__=='__main__':
    rows=[];previous=None; replicate_seed=None
    for q in [0.,.0025,.005,.01,.015,.02]:
        row,previous=solve(q,previous);rows.append(row)
        print(json.dumps(row),flush=True)
        if not row['accepted']:break
        if q==.01:replicate_seed=previous
    replication=None
    if replicate_seed:
        row,_=solve(.01,replicate_seed,160.,2e-8)
        base=next(x for x in rows if x['q']==.01)
        errors={key:abs(row[key]-base[key])/abs(row[key]) for key in ['charge_number','energy']}
        replication=dict(result=row,relative_differences=errors,passed=bool(row['accepted'] and max(errors.values())<1e-4))
    result=dict(status='Exploratory / Not Promoted',stop_reason='last attempted profile rejected as trivial' if not rows[-1]['accepted'] else 'requested scan completed',python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,
        seed_csv_sha256=hashlib.sha256((HERE/'seed_profile.csv').read_bytes()).hexdigest(),continuation=rows,replication=replication)
    (HERE/'gauged_profile_results.json').write_text(json.dumps(result,indent=2)+'\n')
    # A rejected solve is a recorded continuation limit, never a soliton result.
    assert all(x['accepted'] for x in rows[:-1]) and replication['passed']
