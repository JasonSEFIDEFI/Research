"""Exact checks of identity-variable packings and conditional oscillator SU(2).

This is a conventional oscillator construction, not a derivation of spatial spin.
"""
from pathlib import Path
import argparse,json,platform
import sympy as s

parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path,default=Path(__file__).with_name('identity_algebra_results.json'))
args=parser.parse_args()
q1,q2,q3,q4,p1,p2,p3,p4=s.symbols('q1 q2 q3 q4 p1 p2 p3 p4',real=True)
qs=[q1,q2,q3,q4];ps=[p1,p2,p3,p4]
def pb(f,g):return s.simplify(sum(s.diff(f,q)*s.diff(g,p)-s.diff(f,p)*s.diff(g,q) for q,p in zip(qs,ps)))
def zero(x):return s.simplify(s.expand_complex(x))==0

# Coordinate-only C^2 packing: correct Hopf identity, zero canonical brackets.
w1=q1+s.I*q2;w2=q3+s.I*q4
R2=sum(q*q for q in qs)
b=s.Matrix([2*s.re(s.conjugate(w1)*w2),2*s.im(s.conjugate(w1)*w2),s.Abs(w1)**2-s.Abs(w2)**2])
assert zero(b.dot(b)-R2**2)
assert all(pb(b[i],b[j])==0 for i in range(3) for j in range(3))
assert pb(w1,s.conjugate(w1))==0

# Canonical pairing uses positions and momenta of two modes, not four positions.
z1=(q1+s.I*p1)/s.sqrt(2);z2=(q2+s.I*p2)/s.sqrt(2)
assert zero(pb(z1,s.conjugate(z1))+s.I)
N1=(q1*q1+p1*p1)/2;N2=(q2*q2+p2*p2)/2;N=N1+N2
J=s.Matrix([(q1*q2+p1*p2)/2,(q1*p2-p1*q2)/2,(N1-N2)/2])
assert zero(pb(J[0],J[1])-J[2])
assert zero(pb(J[1],J[2])-J[0])
assert zero(pb(J[2],J[0])-J[1])
assert all(pb(N,j)==0 for j in J)
assert zero(J.dot(J)-N*N/4)
om1,om2=s.symbols('omega1 omega2',positive=True)
H=om1*N1+om2*N2
split=[s.factor(pb(j,H)) for j in J]
assert zero(split[0]+(om1-om2)*J[1])
assert zero(split[1]-(om1-om2)*J[0])
assert all(s.simplify(x.subs(om2,om1))==0 for x in split)
assert split[0]!=0 and split[1]!=0 and split[2]==0

# Norm of positions does not equal conserved oscillator phase-space radius.
H4=sum(q*q+p*p for q,p in zip(qs,ps))/2
normrate=pb(R2,H4)
assert normrate==2*sum(q*p for q,p in zip(qs,ps))
t=s.symbols('t',real=True)
assert s.simplify((s.cos(t)**2+s.sin(t)**2)/2-s.Rational(1,2))==0
assert s.cos(t).subs(t,s.pi/2)==0

# An anisotropic coordinate potential is not invariant under arbitrary mixing.
k1,k2,theta=s.symbols('k1 k2 theta',real=True)
deltaV=s.expand((k1*q2*q2+k2*q1*q1-k1*q1*q1-k2*q2*q2)/2)
assert s.simplify(deltaV+(k1-k2)*(q1-q2)*(q1+q2)/2)==0

# Fixed-N quantum matrices built directly, so there is no cutoff commutator artifact.
sectors=[]
for n in range(7):
    dim=n+1;plus=s.zeros(dim)
    for k in range(n):plus[k+1,k]=s.sqrt((k+1)*(n-k))
    minus=plus.T
    jx=(plus+minus)/2;jy=(plus-minus)/(2*s.I)
    jz=s.diag(*[s.Rational(2*k-n,2) for k in range(dim)])
    def comm(a,b):return (a*b-b*a).applyfunc(s.simplify)
    assert comm(jx,jy)==s.I*jz
    assert comm(jy,jz)==s.I*jx
    assert comm(jz,jx)==s.I*jy
    casimir=(jx*jx+jy*jy+jz*jz).applyfunc(s.simplify)
    assert casimir==s.Rational(n*(n+2),4)*s.eye(dim)
    U=s.diag(*[s.simplify(s.exp(-2*s.pi*s.I*jz[k,k])) for k in range(dim)])
    assert U==(-1)**n*s.eye(dim)
    sectors.append(dict(N=n,dimension=dim,j=str(s.Rational(n,2)),casimir=str(s.Rational(n*(n+2),4)),central_2pi_sign=(-1)**n))

# Internal N=1 SU(2) rotation differs from inherited spatial action on scalar labels.
assert sectors[1]['central_2pi_sign']==-1
scalar_spatial=s.eye(2);internal=-s.eye(2)
assert scalar_spatial!=internal

# Full linearized foundations model: a symmetric arrowhead ASW block.
aa,bb,cc,dd,ee,r=s.symbols('a b c d e r',real=True)
M=s.Matrix([[aa,bb,cc],[bb,dd,0],[cc,0,ee]])
minor=(M-r*s.eye(3)).extract([0,1],[0,2]).det()
assert minor==-bb*cc
char=s.factor((M-r*s.eye(3)).det())
assert s.simplify(char-((aa-r)*(dd-r)*(ee-r)-bb**2*(ee-r)-cc**2*(dd-r)))==0
example=s.Matrix([[4,1,1],[1,2,0],[1,0,2]])
assert example.eigenvals()=={2:1,3-s.sqrt(3):1,3+s.sqrt(3):1}
assert (example-2*s.eye(3)).det()==0
result=dict(date='2026-11-08',status='all exact symbolic and fixed-sector checks passed',
 assumptions=['prescribed constant geometry','constant couplings, shifted oscillator equilibria',
 'canonical normalization of the selected two modes','equal frequencies for conserved SU(2)',
 'canonical bosonic quantization for the quantum matrix comparison'],
 coordinate_packing=dict(hopf_polynomial_identity=True,canonical_brackets='zero',
 norm_derivative=str(normrate),norm_can_cross_zero_at_nonzero_energy=True),
 canonical_packing=dict(poisson_su2=True,classical_casimir='N**2/4',
 generator_rates_for_split_frequencies=[str(x) for x in split],degenerate_conservation=True),
 quantum_sectors=sectors,
 full_linearized_model=dict(arrowhead_characteristic=str(char),repeated_eigenvalue_necessary_minor=str(minor),
  both_nonzero_offdiagonal_couplings_imply_simple_ASW_spectrum=True,
  example_ASW_squared_frequencies=['2','3-sqrt(3)','3+sqrt(3)'],
  origin_pair_possible_if_origin_squared_frequency_is_2=True,degeneracy_not_generically_enforced=True),
 spatial_spin_identification=False,
 scope='Standard internal oscillator algebra; no electron, electromagnetic charge, exchange-statistics or Lorentz-spin derivation',
 versions=dict(python=platform.python_version(),sympy=s.__version__))
args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
