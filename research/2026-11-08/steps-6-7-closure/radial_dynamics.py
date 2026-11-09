"""Full charged Cartesian radial Hamiltonian linearization; electric Gauss eliminated.

Coordinates U=r delta Re Phi, V=r delta Im Phi, Z=r delta Re Sigma;
canonical momenta transformed in the same way. Rotating Hamiltonian H-omega*N.
Global charge constraint and gauge orbit are removed symplectically.
"""
from pathlib import Path
import json,sys,hashlib
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.sparse import diags
from scipy.sparse.linalg import splu,LinearOperator,eigsh
from scipy.linalg import qr,eigvals,eigh
HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'fixed-charge-stability'
if not SOURCE.exists():SOURCE=HERE.parent/'fixed-charge-git'

def run(R,h,spectrum):
    q=.0025
    meta=json.loads((SOURCE/'conditional_observables_results.json').read_text());w=meta['background']['omega']
    data=np.loadtxt(SOURCE/'profile_q00025.csv',delimiter=',',skiprows=1)
    r=np.arange(1,int(round(R/h)))*h;n=len(r)
    f,s,a=CubicSpline(data[:,0],data[:,1:],axis=0)(r).T;Om=w-q*a
    D=diags([-np.ones(n-1),2*np.ones(n),-np.ones(n-1)],[-1,0,1],format='csc')/h**2
    DG=D.copy();DG[-1,-1]-=1/h**2;lu=splu(DG)
    A=D+diags(1+3*f*f+4*s*s);B=D+diags(1+f*f+4*s*s);C=D+diags(-3+4*f*f+36*s*s)
    cross=8*f*s
    def J(z):return np.r_[z[3*n:],-z[:3*n]]
    charge=np.r_[r*f*Om,np.zeros(3*n),-r*f,np.zeros(n)]
    charge/=np.linalg.norm(charge);gauge=J(charge)
    def P(z):return z-charge*np.dot(charge,z)-gauge*np.dot(gauge,z)
    def L(z):
        U,V,Z,Pu,Pv,Pz=np.split(z,6)
        delta_n=f*(Om*U-Pv)
        response=q*q*lu.solve(delta_n)
        return np.r_[A@U+cross*Z+Om*Pv+Om*f*response,
                     B@V-Om*Pu,C@Z+cross*U,Pu-Om*V,Pv+Om*U-f*response,Pz]
    def reduced(z):
        return P(L(P(z)))+charge*np.dot(charge,z)+gauge*np.dot(gauge,z)
    rng=np.random.default_rng(20261109);x=rng.normal(size=6*n);y=rng.normal(size=6*n)
    symmetry=abs(np.dot(x,L(y))-np.dot(L(x),y))/max(1,abs(np.dot(x,L(y))))
    symmetry_reduced=abs(np.dot(x,reduced(y))-np.dot(reduced(x),y))/max(1,abs(np.dot(x,reduced(y))))
    # L*Jc=0 in the exact stationary continuum background. FD residue is retained.
    gauge_residual=float(np.linalg.norm(L(gauge)))
    # Direct solve: unshifted iterative minimization was too slow near small modes.
    ident=np.eye(n);zero=np.zeros((n,n));od=np.diag(Om)
    coul=q*q*f[:,None]*lu.solve(ident)*f[None,:]
    cv=od-Om[:,None]*coul
    matrix=np.block([[A.toarray()+Om[:,None]*coul*Om[None,:],zero,np.diag(cross),zero,cv,zero],
                     [zero,B.toarray(),zero,-od,zero,zero],
                     [np.diag(cross),zero,C.toarray(),zero,zero,zero],
                     [zero,-od,zero,ident,zero,zero],
                     [cv.T,zero,zero,zero,ident+coul,zero],
                     [zero,zero,zero,zero,zero,ident]])
    modes=np.column_stack([charge,gauge]);Lm=matrix@modes
    projected=matrix-modes@Lm.T-Lm@modes.T+modes@(modes.T@Lm)@modes.T+modes@modes.T
    vals,vecs=eigh(projected,subset_by_index=[0,3],driver='evr')
    del projected
    residuals=[float(np.linalg.norm(reduced(vecs[:,i])-vals[i]*vecs[:,i])) for i in range(4)]
    record=dict(radius=R,h=h,radial_nodes=n,energy_symmetry_error=symmetry,reduced_symmetry_error=symmetry_reduced,
        unreduced_gauge_mode_residual=gauge_residual,smallest_reduced_energy_eigenvalues=vals.tolist(),eigenpair_residuals=residuals,
        phase_space_dimension=6*n-2)
    if spectrum:
        # Orthonormal complement of {c,Jc}; its subspace is J invariant.
        Q,_=qr(np.column_stack([charge,gauge]),mode='full');basis=Q[:,2:]
        LB=np.column_stack([L(basis[:,i]) for i in range(basis.shape[1])])
        Hred=basis.T@LB
        JB=np.vstack([basis[3*n:],-basis[:3*n]])
        Jred=basis.T@JB
        generator=Jred@Hred
        eig=eigvals(generator)
        record.update(maximum_absolute_real_part=float(max(abs(eig.real))),
            maximum_frequency=float(max(abs(eig.imag))),
            smallest_nonzero_frequency=float(min(abs(eig.imag[abs(eig.imag)>1e-7]))),
            positive_growth_count=int(np.count_nonzero(eig.real>1e-6)),
            symplectic_square_error=float(np.max(abs(Jred@Jred+np.eye(len(Jred))))),
            reduced_energy_minimum_direct=float(eigh(Hred,subset_by_index=[0,0])[0][0]))
        filename=f'radial_spectrum_R{R:g}_h{h:g}.csv'
        np.savetxt(HERE/filename,np.column_stack([eig.real,eig.imag]),delimiter=',',header='real,imag',comments='',fmt='%.17e')
        record['generated_spectrum_file']=filename
        record['spectrum_sha256_LF_UTF8']=hashlib.sha256((HERE/filename).read_text(encoding='utf-8').encode('utf-8')).hexdigest()
    # Neutral imaginary Sigma decouples: eta_tt=-(D+4f^2+12s^2-3)eta.
    neutral=D+diags(4*f*f+12*s*s-3)
    ne=eigh(neutral.toarray(),subset_by_index=[0,2])[0]
    record['neutral_phase_lowest_squared_frequencies']=ne.tolist()
    return record

if __name__=='__main__':
    rows=[]
    for R,h,spectrum in [(60.,.4,True),(60.,.2,True),(80.,.1,False)]:
        row=run(R,h,spectrum);rows.append(row)
        print(json.dumps({k:v for k,v in row.items() if k!='all_eigenvalues'}),flush=True)
    result=dict(status='Exploratory / Not Promoted',scope='Finite-box complete radial charged phase/amplitude plus neutral real mode; neutral imaginary mode separately; not a nonlinear 3D proof',results=rows)
    (HERE/'radial_dynamics_results.json').write_text(json.dumps(result,indent=2)+'\n')
    assert all(max(row['eigenpair_residuals'])<1e-6 and row['energy_symmetry_error']<1e-10 for row in rows)
    assert all(row.get('positive_growth_count',0)==0 for row in rows)
