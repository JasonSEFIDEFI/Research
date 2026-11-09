"""Fixed classical charge-number scalar-Maxwell continuation; dimensionless."""
from pathlib import Path
import json, platform, hashlib
import numpy as np
import scipy
from scipy.integrate import solve_bvp, simpson, cumulative_simpson
HERE=Path(__file__).resolve().parent
TARGET=1250.1753361265248
W0=1.401223084350689

def solve(q,previous=None,radius=120.,tol=1e-7):
    r=np.linspace(0,radius,801)
    if previous is None:
        data=np.loadtxt(HERE/'seed_profile.csv',delimiter=',',skiprows=1)
        f=np.interp(r,data[:,0],data[:,1],right=0);s=np.interp(r,data[:,0],data[:,2],right=.5)
        number=cumulative_simpson(4*np.pi*r*r*W0*f*f,x=r,initial=0)
        y=np.array([f,np.gradient(f,r),s,np.gradient(s,r),r*0,r*0,number]);guess=W0
    else:
        old,R=previous;guess=float(old.p[0]);y=old.sol(np.minimum(r,R))
        out=r>R;y[0,out]=0;y[1,out]=0;y[2,out]=.5;y[3,out]=0
        y[4,out]=old.y[4,-1]*R/r[out];y[5,out]=-old.y[4,-1]*R/r[out]**2;y[6,out]=TARGET
    y[[1,3,5],0]=0;y[6,0]=0
    def fun(r,y,p):
        f,fp,s,sp,a,ap,c=y;om=p[0]-q*a
        return np.array([fp,(1+f*f+4*s*s-om*om)*f,sp,(4*f*f+12*s*s-3)*s,ap,-q*om*f*f,4*np.pi*r*r*om*f*f])
    def bc(a,b,p):return np.array([a[1],a[3],a[5],a[6],b[0],b[2]-.5,b[5]+b[4]/radius,b[6]-TARGET])
    singular=np.diag([0.,-2,0,-2,0,-2,0])
    sol=solve_bvp(fun,bc,r,y,p=[guess],S=singular,tol=tol,bc_tol=1e-10,max_nodes=30000)
    rr=np.linspace(0,radius,24001);f,fp,s,sp,a,ap,c=sol.sol(rr);w=float(sol.p[0]);om=w-q*a
    integ=lambda z:float(simpson(4*np.pi*rr*rr*z,x=rr))
    number=integ(om*f*f);flux=-4*np.pi*radius**2*ap[-1];charge=q*number
    G=integ((fp*fp+sp*sp)/2);T=integ(om*om*f*f/2)
    U=integ(f**4/4+f*f/2+2*f*f*s*s+3*(s*s-.25)**2)
    electric=integ(ap*ap/2)+2*np.pi*radius*a[-1]**2;energy=G+T+U+electric
    nodes=int(np.count_nonzero(np.diff(np.sign(f[abs(f)>max(1e-8,max(abs(f))*1e-5)]))))
    charge_error=abs(number-TARGET)/TARGET;gauss_error=abs(flux-charge)/max(abs(charge),1e-20)
    accepted=sol.status==0 and f[0]>.001 and nodes==0 and charge_error<1e-5 and gauss_error<1e-5 and 0<w<np.sqrt(2)
    record=dict(q=q,target_number=TARGET,omega=w,radius=radius,tolerance=tol,status=int(sol.status),message=sol.message,
        nodes=len(sol.x),max_rms_residual=float(max(sol.rms_residuals)),boundary_residual=float(max(abs(bc(sol.y[:,0],sol.y[:,-1],sol.p)))),
        central_f=float(f[0]),central_s=float(s[0]),central_a=float(a[0]),central_frequency=float(om[0]),radial_nodes=nodes,
        charge_number=number,electric_charge=charge,gauss_flux=float(flux),charge_relative_error=charge_error,gauss_relative_error=gauss_error,
        energy=energy,energy_per_number=energy/number,binding_margin=float(np.sqrt(2)*number-energy),
        gradient_energy=G,time_energy=T,potential_energy=U,electric_energy=electric,
        gauss_energy_identity_relative=abs(T+electric-w*number/2)/energy,accepted=bool(accepted))
    return record,(sol,radius)

def profile(name,pair):
    sol,R=pair;r=np.linspace(0,R,int(R/.1)+1);y=sol.sol(r)
    np.savetxt(HERE/name,np.column_stack([r,y[0],y[2],y[4]]),delimiter=',',header='r,f,s,a',comments='',fmt='%.17e')

if __name__=='__main__':
    rows=[];previous=None;rep_seed=None
    for q in [0.,.0025,.005,.01,.015,.02,.03,.04,.05]:
        row,pair=solve(q,previous);rows.append(row);print(json.dumps(row),flush=True)
        if not row['accepted']:break
        previous=pair
        if q==0:profile('profile_q0.csv',pair)
        if q==.01:profile('profile_q001.csv',pair);rep_seed=pair
    replication=None
    if rep_seed:
        row,pair=solve(.01,rep_seed,160.,2e-8);profile('profile_q001_replication.csv',pair)
        base=next(x for x in rows if x['q']==.01)
        diffs={key:abs(row[key]-base[key])/abs(row[key]) for key in ['energy','omega']}
        replication=dict(result=row,relative_differences=diffs,passed=bool(row['accepted'] and max(diffs.values())<1e-5))
    result=dict(status='Exploratory / Not Promoted',python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,
        seed_csv_sha256=hashlib.sha256((HERE/'seed_profile.csv').read_text(encoding='utf-8').encode('utf-8')).hexdigest(),hash_convention='UTF-8 text with LF newlines',continuation=rows,replication=replication)
    (HERE/'fixed_charge_results.json').write_text(json.dumps(result,indent=2)+'\n')
    assert rows[0]['accepted'] and all(x['accepted'] for x in rows[:-1]) and replication and replication['passed']
