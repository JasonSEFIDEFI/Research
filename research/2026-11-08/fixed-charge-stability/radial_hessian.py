"""Real-amplitude, fixed-N radial energy Hessian, with Gauss eliminated."""
from pathlib import Path
import json
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.sparse import diags
from scipy.sparse.linalg import splu
from scipy.linalg import eigh
HERE=Path(__file__).resolve().parent

def evaluate(q,w,path,R,h,ell=0,variation_checks=True):
    data=np.loadtxt(HERE/path,delimiter=',',skiprows=1)
    r=np.arange(1,int(round(R/h)))*h;n=len(r)
    f,s,a=CubicSpline(data[:,0],data[:,1:],axis=0)(r).T
    weight=4*np.pi*h
    lap=diags([-np.ones(n-1),2*np.ones(n),-np.ones(n-1)],[-1,0,1],format='csc')/h**2
    # r*delta a is constant in the source-free exterior: Neumann endpoint.
    centrifugal=ell*(ell+1)/r**2
    lap=lap+diags(centrifugal,format='csc')
    lap_e=lap.copy();lap_e[-1,-1]-=(r[-1]/R)**ell/h**2
    def capacitance(field):
        factor=splu(lap_e+diags(q*q*field*field,format='csc'))
        u=1-q*q*factor.solve(r*field*field)/r
        C=weight*np.sum(r*r*field*field*u)
        return C,u,factor
    # The background capacitance is always monopolar; only its variation has ell.
    if ell:
        background_lap=diags([-np.ones(n-1),2*np.ones(n),-np.ones(n-1)],[-1,0,1],format='csc')/h**2
        background_lap[-1,-1]-=1/h**2
        background_lu=splu(background_lap+diags(q*q*f*f,format='csc'))
        u=1-q*q*background_lu.solve(r*f*f)/r
        C=weight*np.sum(r*r*f*f*u)
        lu=splu(lap_e+diags(q*q*f*f,format='csc'))
    else:C,u,lu=capacitance(f)
    omega=w;Om=omega*u
    ff=lap+diags(1+3*f*f+4*s*s-Om*Om,format='csc')
    ss=lap+diags(-3+4*f*f+36*s*s,format='csc');cross=8*f*s
    b=r*f*u*u;source=f*Om
    def matvec(z,constrained=True):
        x,y=z[:n],z[n:]
        out=ff@x+cross*y+4*q*q*source*lu.solve(source*x)
        if constrained and ell==0:out+=(4*omega*omega/C)*weight*b*np.dot(b,x)
        return np.r_[out,ss@y+cross*x]
    # Direct symmetric solve avoids slow unshifted iteration near the continuum.
    block=ff.toarray()
    if ell==0:block+=(4*omega*omega/C)*weight*np.outer(b,b)
    if q: block+=4*q*q*source[:,None]*lu.solve(np.diag(source))
    matrix=np.block([[block,np.diag(cross)],[np.diag(cross),ss.toarray()]])
    assert np.max(abs(matrix-matrix.T))<1e-10
    vals,vecs=eigh(matrix,subset_by_index=[0,3],driver='evr')
    order=np.argsort(vals);vals=vals[order];vecs=vecs[:,order]
    residuals=[float(np.linalg.norm(matvec(vecs[:,i])-vals[i]*vecs[:,i])) for i in range(4)]
    # Independent directional finite difference of C, using a smooth radial test.
    xi=r*np.exp(-(r/8)**2);df=xi/r
    dc=2*weight*np.sum(r*f*u*u*xi)
    d2c=2*weight*np.sum(u*u*xi*xi)-8*q*q*weight*np.dot(f*u*xi,lu.solve(f*u*xi))
    differences=[]
    for eps in ([1e-3,3e-4,1e-4] if variation_checks else []):
        plus=capacitance(f+eps*df)[0];minus=capacitance(f-eps*df)[0]
        differences.append(dict(epsilon=eps,first_relative=abs((plus-minus)/(2*eps)-dc)/max(1,abs(dc)),
            second_relative=abs((plus-2*C+minus)/eps**2-d2c)/max(1,abs(d2c))))
    # Check the electrostatic contribution to the Hessian against direct energy.
    N=omega*C;analytic_T=omega**2/C*dc**2-omega**2*d2c/2
    energy_differences=[]
    for eps in ([1e-3,3e-4,1e-4] if variation_checks else []):
        cp=capacitance(f+eps*df)[0];cm=capacitance(f-eps*df)[0]
        observed=(N*N/(2*cp)-N*N/C+N*N/(2*cm))/eps**2
        energy_differences.append(dict(epsilon=eps,relative_error=abs(observed-analytic_T)/max(1,abs(analytic_T))))
    local_min=(1+3*f*f+4*s*s-Om*Om+(-3+4*f*f+36*s*s))/2-np.sqrt(((1+3*f*f+4*s*s-Om*Om-(-3+4*f*f+36*s*s))/2)**2+cross**2)
    angular_bound=float(max(r*r*np.maximum(0,-local_min)))
    return dict(q=q,omega=w,radius=R,h=h,ell=ell,capacitance=C,discrete_charge_number=N,
        sampled_high_ell_bound=angular_bound,
        lowest_eigenvalues=vals.tolist(),eigenpair_residuals=residuals,
        capacitance_variation_checks=differences,electrostatic_energy_second_variation_checks=energy_differences,
        sign='positive in this discretized restricted subspace' if vals[0]>0 else 'negative direction in this discretized restricted subspace')

if __name__=='__main__':
    data=json.loads((HERE/'fixed_charge_results.json').read_text());rows=[]
    for q,path in [(0.,'profile_q0.csv'),(.01,'profile_q001.csv')]:
        w=next(row['omega'] for row in data['continuation'] if row['q']==q)
        for R,h in [(80.,.2),(80.,.1),(80.,.05),(120.,.1)]:
            row=evaluate(q,w,path,R,h);rows.append(row)
            print(json.dumps({k:row[k] for k in ['q','radius','h','lowest_eigenvalues','eigenpair_residuals']}),flush=True)
    result=dict(status='Exploratory / Not Promoted',restriction='static real scalar amplitudes; fixed charge; electrostatic response included; not the full dynamical spectrum',results=rows)
    (HERE/'radial_hessian_results.json').write_text(json.dumps(result,indent=2)+'\n')
    assert all(max(x['eigenpair_residuals'])<1e-6 for x in rows)
    assert all(min(x['second_relative'] for x in row['capacitance_variation_checks'])<1e-5 for row in rows)
    assert all(min(x['relative_error'] for x in row['electrostatic_energy_second_variation_checks'])<1e-5 for row in rows)
