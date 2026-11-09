"""Independent finite-matrix checks of canonical boosts and Wigner rotations."""
from pathlib import Path
import argparse,json,platform
import numpy as np
parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path,default=Path(__file__).with_name('wigner_results.json'))
args=parser.parse_args()
pauli=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],dtype=complex)
I=np.eye(2,dtype=complex)
def dot_sigma(p):return np.einsum('i,ijk->jk',p,pauli)
def canonical(p,m):
    E=np.sqrt(m*m+p@p)
    return ((E+m)*I+dot_sigma(p))/np.sqrt(2*m*(E+m))
def boost(n,eta):
    n=np.asarray(n,float);n=n/np.linalg.norm(n)
    A=np.cosh(eta/2)*I+np.sinh(eta/2)*dot_sigma(n)
    L=np.eye(4);L[0,0]=np.cosh(eta);L[0,1:]=np.sinh(eta)*n
    L[1:,0]=np.sinh(eta)*n;L[1:,1:]+=(np.cosh(eta)-1)*np.outer(n,n)
    return A,L
def wigner(A,L,p,m):
    inp=np.r_[np.sqrt(m*m+p@p),p];out=L@inp
    W=np.linalg.solve(canonical(out[1:],m),A@canonical(p,m))
    return W,out
rng=np.random.default_rng(20261108)
errors={k:0. for k in ['mass_shell','spinor_lorentz_map','wigner_unitarity','wigner_determinant','cocycle','infinitesimal_spin']}
cases=0
for m in [.3,1.,5.]:
    for _ in range(6):
        p=rng.normal(size=3)*m;n1=rng.normal(size=3);n2=rng.normal(size=3)
        eta1=rng.uniform(-1.2,1.2);eta2=rng.uniform(-1.2,1.2)
        A1,L1=boost(n1,eta1);A2,L2=boost(n2,eta2)
        W1,p1=wigner(A1,L1,p,m);W2,p2=wigner(A2,L2,p1[1:],m)
        W21,out=wigner(A2@A1,L2@L1,p,m)
        errors['mass_shell']=max(errors['mass_shell'],abs(out[0]**2-out[1:]@out[1:]-m*m)/(1+m*m+out[0]**2))
        inp=np.sqrt(m*m+p@p)*I+dot_sigma(p)
        target=p1[0]*I+dot_sigma(p1[1:])
        errors['spinor_lorentz_map']=max(errors['spinor_lorentz_map'],float(np.max(np.abs(A1@inp@A1.conj().T-target)))/(1+float(np.max(np.abs(target)))))
        errors['wigner_unitarity']=max(errors['wigner_unitarity'],float(np.max(np.abs(W21.conj().T@W21-I))))
        errors['wigner_determinant']=max(errors['wigner_determinant'],float(abs(np.linalg.det(W21)-1)))
        errors['cocycle']=max(errors['cocycle'],float(np.max(np.abs(W21-W2@W1))))
        E=np.sqrt(m*m+p@p);h=1e-6
        for i in range(3):
            n=np.eye(3)[i];ap,lp=boost(n,h);am,lm=boost(n,-h)
            wp,_=wigner(ap,lp,p,m);wm,_=wigner(am,lm,p,m)
            derivative=(wp-wm)/(2*h)
            scross=sum((np.cross(np.eye(3)[j],p)[i]*pauli[j]/2 for j in range(3)),np.zeros((2,2),complex))
            expected=-1j*scross/(E+m)
            errors['infinitesimal_spin']=max(errors['infinitesimal_spin'],float(np.max(np.abs(derivative-expected))))
        cases+=1
assert all(v<2e-12 for k,v in errors.items() if k!='infinitesimal_spin'),errors
assert errors['infinitesimal_spin']<1e-8,errors
result=dict(date='2026-11-08',status='all finite Wigner checks passed',cases=cases,seed=20261108,masses=[.3,1.,5.],
 errors=errors,tolerances=dict(algebra=2e-12,infinitesimal_spin=1e-8,finite_difference_step=1e-6),
 scope='Finite implementation tests of conventional induced representations, not a particle prediction or a proof from sampling',
 versions=dict(python=platform.python_version(),numpy=np.__version__))
args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
