"""Variational-grid critical point and radial Hamiltonian review.
No projected repair of a nonstationary background is used as evidence.
"""
from pathlib import Path
import json,hashlib
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.sparse import diags,bmat,csc_matrix
from scipy.sparse.linalg import spsolve
from scipy.linalg import eigh,eigvals,qr
HERE=Path(__file__).resolve().parent
SOURCE=next(p for p in [HERE.parent/'fixed-charge-stability',HERE.parent.parent/'2026-11-08'/'fixed-charge-stability',HERE.parent/'fixed-charge-git'] if p.exists())
TARGET=1250.1753361265248;Q=.0025

def background(R,h):
    r=np.arange(1,int(round(R/h)))*h;n=len(r);weight=4*np.pi*h
    D=diags([-np.ones(n-1),2*np.ones(n),-np.ones(n-1)],[-1,0,1],format='csc')/h**2
    De=D.copy();De[-1,-1]-=1/h**2
    data=np.loadtxt(SOURCE/'profile_q00025.csv',delimiter=',',skiprows=1)
    f,s,a=CubicSpline(data[:,0],data[:,1:],axis=0)(r).T
    w=json.loads((SOURCE/'conditional_observables_results.json').read_text())['background']['omega']
    x=np.r_[r*f,r*(s-.5),r*a,w]
    def residual(x,jac=False):
        F,S,A=np.split(x[:-1],3);w=x[-1];f=F/r;s=.5+S/r;Om=w-Q*A/r
        out=np.r_[D@F+(1+f*f+4*s*s-Om*Om)*F,
            D@S+(4*f*f+12*s*s-3)*(S+.5*r),De@A-Q*Om*F*F/r,
            (weight*np.dot(Om,F*F)-TARGET)/TARGET]
        if not jac:return out
        col=lambda z:csc_matrix(z[:,None]);row=lambda z:csc_matrix(z[None,:]);diag=lambda z:diags(z,format='csc')
        matrix=bmat([[D+diag(1+3*f*f+4*s*s-Om*Om),diag(8*f*s),diag(2*Q*Om*f),col(-2*Om*F)],
                     [diag(8*f*s),D+diag(4*f*f+36*s*s-3),None,col(np.zeros(n))],
                     [diag(-2*Q*Om*f),None,De+diag(Q*Q*f*f),col(-Q*F*F/r)],
                     [row(2*weight*Om*F/TARGET),row(np.zeros(n)),row(-weight*Q*F*F/r/TARGET),csc_matrix([[weight*np.dot(F,F)/TARGET]])]],format='csc')
        return out,matrix
    history=[]
    for iteration in range(20):
        res,J=residual(x,True);norm=float(max(abs(res)));history.append(norm)
        if norm<1e-10:break
        dx=spsolve(J,-res);step=1.
        while step>=1/1024 and max(abs(residual(x+step*dx)))>=norm:step/=2
        if step<1/1024:raise RuntimeError('Newton line search rejected')
        x+=step*dx
    else:raise RuntimeError('Newton failed declared iteration limit')
    F,S,A=np.split(x[:-1],3);w=float(x[-1]);f=F/r;s=.5+S/r;a=A/r;Om=w-Q*a
    N=weight*np.dot(Om,F*F)
    energy=weight*(.5*(np.dot(F,D@F)+np.dot(S,D@S)+np.dot(A,De@A))+np.sum(r*r*(f**4/4+f*f/2+2*f*f*s*s+3*(s*s-.25)**2)+.5*Om*Om*F*F))
    radius=float(np.sqrt(weight*np.sum(r*r*Om*F*F)/N))
    significant=f[abs(f)>max(1e-8,max(abs(f))*1e-5)]
    radial_nodes=int(np.count_nonzero(np.diff(np.sign(significant))))
    flux=4*np.pi*A[-1]
    assert f[0]>.001 and radial_nodes==0 and 0<w<np.sqrt(2)
    return dict(r=r,D=D,De=De,f=f,s=s,a=a,Om=Om,w=w,record=dict(radius=R,h=h,omega=w,energy=float(energy),charge_number=float(N),
        first_interior_f=float(f[0]),first_interior_s=float(s[0]),radial_nodes=radial_nodes,gauss_flux=float(flux),
        gauss_relative_error=abs(flux-Q*N)/(Q*N),binding_margin=float(np.sqrt(2)*N-energy),
        charge_relative_error=abs(N-TARGET)/TARGET,charge_rms_radius=radius,newton_residual_history=history,stationary_maximum_residual=history[-1]))

def review(R,h,spectrum):
    b=background(R,h);r,D,De,f,s,a,Om,w=[b[k] for k in ['r','D','De','f','s','a','Om','w']];n=len(r)
    I=np.eye(n);zero=np.zeros((n,n));od=np.diag(Om)
    G=np.linalg.solve(De.toarray(),I);K=Q*Q*f[:,None]*G*f[None,:]
    mixed=od-Om[:,None]*K
    L=np.block([[D.toarray()+np.diag(1+3*f*f+4*s*s)+Om[:,None]*K*Om[None,:],zero,np.diag(8*f*s),zero,mixed,zero],
                [zero,D.toarray()+np.diag(1+f*f+4*s*s),zero,-od,zero,zero],
                [np.diag(8*f*s),zero,D.toarray()+np.diag(-3+4*f*f+36*s*s),zero,zero,zero],
                [zero,-od,zero,I,zero,zero],[mixed.T,zero,zero,zero,I+K,zero],[zero,zero,zero,zero,zero,I]])
    J=lambda z:np.r_[z[3*n:],-z[:3*n]]
    c=np.r_[r*f*Om,np.zeros(3*n),-r*f,np.zeros(n)];c/=np.linalg.norm(c);g=J(c)
    gauge_defect=float(np.linalg.norm(L@g));modes=np.column_stack([c,g]);Lm=L@modes
    red=L-modes@Lm.T-Lm@modes.T+modes@(modes.T@Lm)@modes.T+modes@modes.T
    val,vec=eigh(red,subset_by_index=[0,3],driver='evr')
    result=b['record'];result.update(physical_dimension=6*n-2,energy_symmetry_error=float(max(abs(L-L.T).ravel())),
        gauge_mode_defect=gauge_defect,unreduced_linear_charge_conservation_defect=gauge_defect,
        reduced_energy_eigenvalues=val.tolist(),eigenpair_residuals=[float(np.linalg.norm(red@vec[:,i]-val[i]*vec[:,i])) for i in range(4)])
    del red
    if spectrum:
        basis=qr(modes,mode='full')[0][:,2:]
        Hr=basis.T@L@basis;Jr=basis.T@np.vstack([basis[3*n:],-basis[:3*n]])
        eig=eigvals(Jr@Hr)
        name=f'review_spectrum_R{R:g}_h{h:g}.csv'
        np.savetxt(HERE/name,np.c_[eig.real,eig.imag],delimiter=',',header='real,imag',comments='',fmt='%.17e')
        result.update(maximum_absolute_real_part=float(max(abs(eig.real))),positive_growth_count=int(np.count_nonzero(eig.real>1e-6)),
            smallest_frequency=float(min(abs(eig.imag[abs(eig.imag)>1e-7]))),spectrum_file=name,
            spectrum_sha256_LF_UTF8=hashlib.sha256((HERE/name).read_text().encode()).hexdigest(),
            reduced_symplectic_square_error=float(max(abs(Jr@Jr+np.eye(len(Jr))).ravel())))
    return result

if __name__=='__main__':
    rows=[]
    for R,h,spectrum in [(60.,.4,True),(60.,.2,True),(80.,.1,False)]:
        row=review(R,h,spectrum);rows.append(row);print(json.dumps(row),flush=True)
    result=dict(status='Exploratory / Not Promoted',review_kind='AI self-audit with a separately solved variational-grid background',q=Q,results=rows)
    (HERE/'discrete_review_results.json').write_text(json.dumps(result,indent=2)+'\n')
    assert all(r['stationary_maximum_residual']<1e-10 and r['gauge_mode_defect']<1e-9 and max(r['eigenpair_residuals'])<1e-7 for r in rows)
    assert all(r.get('positive_growth_count',0)==0 and min(r['reduced_energy_eigenvalues'])>0 for r in rows)
