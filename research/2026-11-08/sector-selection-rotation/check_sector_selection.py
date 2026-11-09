"""Analytic variational bounds plus independent oscillator-basis calculations."""
from pathlib import Path
import argparse,json,platform,csv
import numpy as np
import scipy
from scipy.special import eval_genlaguerre,gammaln,roots_hermite,eval_hermite
from scipy.sparse import csr_matrix,kron,diags
from scipy.sparse.linalg import eigsh
import sympy as s

parser=argparse.ArgumentParser()
parser.add_argument('--output-dir',type=Path,default=Path(__file__).parent)
args=parser.parse_args();out=args.output_dir;out.mkdir(parents=True,exist_ok=True)
R=s.sqrt(13)/6
couple_a=s.sqrt(26)*s.exp(-s.Rational(1,8))/24
couple_b=s.sqrt(13)*s.exp(-s.Rational(1,8))/12
c=s.Rational(3,16);d=s.Rational(3,32)
norm=1+c*c+d*d
trial=(s.Rational(5,2)+s.Rational(7,2)*c*c+s.Rational(11,2)*d*d-2*c*couple_a-2*d*couple_b)/norm
closed=(5471-32*s.exp(-s.Rational(1,8))*(s.sqrt(26)+s.sqrt(13)))/2138
assert s.simplify(trial-closed)==0
lower=s.Rational(1,2)+s.sqrt(131)/12
upper_r=s.Rational(26151,10690)
lower_r=s.Rational(29,20)
gap_r=s.factor(upper_r-lower_r)
# exp(-1/8)>7/8, sqrt(26)>5, sqrt(13)>18/5, sqrt(131)>57/5.
assert s.Rational(1,8)>0
assert 26>5**2 and 13>s.Rational(18,5)**2 and 131>s.Rational(57,5)**2
assert s.simplify((5471-28*(5+s.Rational(18,5)))/2138-upper_r)==0
assert s.Rational(1,2)+s.Rational(57,5)/12==lower_r
assert upper_r>s.Rational(3,2) and gap_r<1

def sin_matrix(n):
    eta=.5;mat=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            lo=min(i,j);hi=max(i,j);k=hi-lo
            mat[i,j]=np.imag((1j*eta)**k)*np.exp(-eta*eta/2+.5*(gammaln(lo+1)-gammaln(hi+1)))*eval_genlaguerre(lo,k,eta*eta)
    return mat
small=sin_matrix(8)
gx,gw=roots_hermite(128)
normal=np.array([eval_hermite(i,gx)/np.sqrt(2.**i*np.exp(gammaln(i+1))) for i in range(8)])
quad=(normal*(gw*np.sin(gx/np.sqrt(2.)))[None,:])@normal.T/np.sqrt(np.pi)
# A oscillator frequency is 2, so A=x/sqrt(2) in Hermite quadrature.
quaderror=float(np.max(np.abs(small-quad)))
assert quaderror<2e-12,quaderror
assert abs(small[0,1]-.5*np.exp(-.125))<1e-14

records=[]
for n in [8,12,18,26,36,48]:
    sm=csr_matrix(sin_matrix(n))
    bx=diags([np.sqrt(np.arange(1,n)/2),np.sqrt(np.arange(1,n)/2)],[-1,1],shape=(n,n))
    bare=(2*(np.arange(n)+.5)[:,None]+(np.arange(n)+.5)[None,:]).ravel()
    H=diags(bare)+float(R)*kron(sm,bx,format='csr')
    assert (H-H.T).nnz==0
    v0=np.cos(np.arange(n*n)*np.sqrt(2.))+.3
    vals,vecs=eigsh(H,k=6,which='SA',tol=2e-13,v0=v0,maxiter=30000)
    ix=np.argsort(vals);vals=vals[ix];vecs=vecs[:,ix]
    residuals=np.linalg.norm(H@vecs-vecs*vals,axis=0)
    assert np.max(residuals)<1e-9
    parity=(-1.)**(np.arange(n)[:,None]+np.arange(n)[None,:]).ravel()
    signs=np.sum(vecs*vecs*parity[:,None],axis=0)
    assert np.max(np.abs(np.abs(signs)-1))<1e-9
    records.append(dict(basis_per_coordinate=n,dimension=n*n,eigenvalues=vals.tolist(),
      matrix_eigenpair_residuals=residuals.tolist(),joint_parities=signs.tolist()))
last=np.array(records[-1]['eigenvalues']);before=np.array(records[-2]['eigenvalues'])
change=float(np.max(np.abs(last-before)))
assert change<1e-8,change
# Nested Galerkin upper bounds should not rise outside roundoff.
for a,b in zip(records,records[1:]):
    assert np.max(np.array(b['eigenvalues'])-np.array(a['eigenvalues']))<1e-10
assert last[0]>=float(lower)-1e-10
assert last[1]<=float(trial)+1e-10
result=dict(date='2026-11-08',status='all symbolic bounds and numerical checks passed',
 scope='Quantized internal fixed-geometry example, not observed matter or a new quantization derivation',
 analytic=dict(E0_lower_exact=str(lower),E1_upper_trial_exact=str(trial),
   E0_lower_value=float(lower),E1_upper_trial_value=float(trial),
   trial_gap_upper_value=float(trial-lower),
   certified_E1_upper_rational=str(upper_r),certified_E0_lower_rational=str(lower_r),
   certified_gap_upper_rational=str(gap_r),certified_gap_upper_value=float(gap_r),
   certified_gap_upper_strictly_below_dark_gap_one=True),
 matrix_validation=dict(max_quadrature_difference=quaderror,points=128,threshold=2e-12),
 convergence=dict(max_last_two_change=change,threshold=1e-8),
 numerical_gap_estimate=float(last[1]-last[0]),dark_gap=1,
 N1_invariant_but_not_selected=True,lower_competing_rest_excitation_proved_for_this_example=True,
 basis_records=records,
 versions=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,sympy=s.__version__))
(out/'sector_selection_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
with (out/'basis_convergence.csv').open('w',newline='',encoding='utf-8') as f:
    writer=csv.writer(f);writer.writerow(['basis_size','dimension']+['E'+str(i) for i in range(6)]+['maximum_matrix_residual'])
    for r in records:writer.writerow([r['basis_per_coordinate'],r['dimension']]+r['eigenvalues']+[max(r['matrix_eigenpair_residuals'])])
print(json.dumps({k:result[k] for k in ['status','analytic','matrix_validation','convergence','numerical_gap_estimate']},indent=2))
