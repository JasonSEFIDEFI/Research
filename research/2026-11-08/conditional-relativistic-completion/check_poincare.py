"""Exact first-order momentum differential-operator algebra for a conditional
massive spin-half representation. All new physical inputs are recorded.
"""
from pathlib import Path
import argparse,json,platform,itertools
import sympy as s

parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path,default=Path(__file__).with_name('poincare_results.json'))
args=parser.parse_args()
p=s.symbols('p1:4',real=True);E,m=s.symbols('E m',positive=True)
I=s.eye(2);Z=s.zeros(2)
S=[s.Matrix([[0,1],[1,0]])/2,s.Matrix([[0,-s.I],[s.I,0]])/2,s.diag(1,-1)/2]
shell=E**2-m**2-sum(x*x for x in p)
def dp(f,j):return s.diff(f,p[j])+p[j]/E*s.diff(f,E)
def reduced(expr):
    num,den=s.fraction(s.cancel(expr))
    return s.rem(s.Poly(s.expand(num),E),s.Poly(shell,E)).as_expr()
def zero(expr):return reduced(expr)==0
def mz(mat):return all(zero(x) for x in mat)
def cross(a,b):return [sum((s.LeviCivita(i,j,k)*a[j]*b[k] for j in range(3) for k in range(3)),s.zeros(2)) for i in range(3)]

# A differential operator is scalar derivative coefficients plus a 2x2 matrix.
def add(a,b):return ([x+y for x,y in zip(a[0],b[0])],a[1]+b[1])
def scale(c,a):return ([c*x for x in a[0]],c*a[1])
def bracket(a,b):
    aa,ab=a;ba,bb=b
    deriv=[sum(aa[j]*dp(ba[k],j)-ba[j]*dp(aa[k],j) for j in range(3)) for k in range(3)]
    mul=ab*bb-bb*ab
    for j in range(3):mul+=aa[j]*bb.applyfunc(lambda x:dp(x,j))-ba[j]*ab.applyfunc(lambda x:dp(x,j))
    return deriv,mul
def equal(a,b):return all(zero(x-y) for x,y in zip(a[0],b[0])) and mz(a[1]-b[1])
zeroop=([0,0,0],s.zeros(2))
H=([0,0,0],E*I)
P=[([0,0,0],p[i]*I) for i in range(3)]
J=[];K=[];oldK=[]
sx=cross(S,p)
for i in range(3):
    jder=[-s.I*sum(s.LeviCivita(i,j,k)*p[j] for j in range(3)) for k in range(3)]
    J.append((jder,S[i]))
    kd=[s.I*E if k==i else s.Integer(0) for k in range(3)]
    scalar=s.I*p[i]/(2*E)*I
    oldK.append((kd,scalar))
    K.append((kd,scalar-sx[i]/(E+m)))

checks=[]
def check(name,a,b,expect):
    actual=bracket(a,b)
    assert equal(actual,expect),name
    checks.append(name)
for i,j in itertools.combinations(range(3),2):
    c=sum((scale(s.I*s.LeviCivita(i,j,k),J[k])[1] for k in range(3)),s.zeros(2))
    expected=zeroop
    for k in range(3):expected=add(expected,scale(s.I*s.LeviCivita(i,j,k),J[k]))
    check(f'JJ_{i}{j}',J[i],J[j],expected)
    check(f'KK_{i}{j}',K[i],K[j],scale(-1,expected))
    check(f'PP_{i}{j}',P[i],P[j],zeroop)
for i in range(3):
    check(f'JH_{i}',J[i],H,zeroop)
    check(f'KH_{i}',K[i],H,scale(s.I,P[i]))
    check(f'PH_{i}',P[i],H,zeroop)
    for j in range(3):
        ep=zeroop;ek=zeroop
        for k in range(3):
            ep=add(ep,scale(s.I*s.LeviCivita(i,j,k),P[k]))
            ek=add(ek,scale(s.I*s.LeviCivita(i,j,k),K[k]))
        check(f'JP_{i}{j}',J[i],P[j],ep)
        check(f'JK_{i}{j}',J[i],K[j],ek)
        check(f'KP_{i}{j}',K[i],P[j],scale(s.I if i==j else 0,H))
assert len(checks)==45,len(checks)
# Omitting the spin correction is retained as a failed candidate.
old_defect=bracket(oldK[0],oldK[1])
expected=scale(-s.I,J[2])
assert not equal(old_defect,expected)
defect=old_defect[1]-expected[1]
assert mz(defect-s.I*S[2])

# Formal adjoint for flat dp: (A partial)^dagger=-A* partial-partial A*.
for i in range(3):
    A,B=K[i]
    assert all(zero(a+s.conjugate(a)) for a in A)
    div=sum(dp(s.conjugate(A[j]),j) for j in range(3))
    assert mz(B.H-div*I-B)

# W0=p.S and W=E J+p cross K, all derivative terms cancel.
W0=sum((p[j]*S[j] for j in range(3)),s.zeros(2))
W=[]
for i in range(3):
    ww=scale(E,J[i])
    for j in range(3):
        for k in range(3):ww=add(ww,scale(s.LeviCivita(i,j,k)*p[j],K[k]))
    assert all(zero(a) for a in ww[0])
    target=m*S[i]+p[i]*W0/(E+m)
    assert mz(ww[1]-target)
    W.append(target)
assert mz(E*W0-sum((p[i]*W[i] for i in range(3)),s.zeros(2)))
Wsq=W0*W0-sum((ww*ww for ww in W),s.zeros(2))
assert mz(Wsq+s.Rational(3,4)*m*m*I)

# Regular minimal spin coefficient in a collinear-momentum boost bracket.
f=s.symbols('f',real=True)
condition=(E*E-m*m)*f*f+2*E*f+1
assert zero(condition.subs(f,-1/(E+m)))
assert zero(condition.subs(f,-1/(E-m)))
assert s.limit(-1/(E+m),E,m)==-1/(2*m)
assert s.limit(-1/(E-m),E,m,dir='+')==-s.oo

result=dict(date='2026-11-08',status='all exact one-particle checks passed',
 assumptions=['chosen internal doublet treated as physical canonical spin','assigned positive mass m',
 'free dispersion E=sqrt(p^2+m^2)','canonical quantum Hilbert space L2(d^3p) tensor C^2',
 'not derived from the prior higher-derivative worldline action'],
 verified_independent_commutators=len(checks),commutators=checks,
 boost_spin_coefficient='-1/(E+m)',flat_measure_correction='i p_i/(2E)',
 mass_casimir='m^2',pauli_lubanski_casimir='-3 m^2/4',
 W_orthogonal_to_P=True,formal_hermiticity=True,
 self_adjointness_not_proved_by_symbolic_checks=True,
 uncorrected_boost_failure_retained=True,
 scope='Conventional conditional free massive spin-half representation; not a SEFI electron derivation',
 versions=dict(python=platform.python_version(),sympy=s.__version__))
args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
