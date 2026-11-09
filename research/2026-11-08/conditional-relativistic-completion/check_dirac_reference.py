"""Conventional Dirac projector, CAR and positive free Fock Hamiltonian checks.
These structures are reference inputs, not SEFI outputs.
"""
from pathlib import Path
import argparse,json,platform
import sympy as s
parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path,default=Path(__file__).with_name('dirac_reference_results.json'))
args=parser.parse_args()
p=s.symbols('p1:4',real=True);E,m=s.symbols('E m',positive=True)
shell=E**2-m**2-sum(x*x for x in p)
def red(x):
    a,b=s.fraction(s.cancel(x))
    return s.rem(s.Poly(s.expand(a),E),s.Poly(shell,E)).as_expr()
def mz(a):return all(red(x)==0 for x in a)
I2=s.eye(2);I4=s.eye(4);Z2=s.zeros(2)
sigma=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
beta=s.diag(1,1,-1,-1)
alpha=[s.BlockMatrix([[Z2,a],[a,Z2]]).as_explicit() for a in sigma]
gamma=[beta]+[beta*a for a in alpha]
for i in range(4):
    for j in range(4):
        target=2*(1 if i==0 else -1)*I4 if i==j else s.zeros(4)
        assert gamma[i]*gamma[j]+gamma[j]*gamma[i]==target
HD=m*beta+sum((p[i]*alpha[i] for i in range(3)),s.zeros(4))
assert mz(HD*HD-E*E*I4)
Pplus=(I4+HD/E)/2;Pminus=(I4-HD/E)/2
assert mz(Pplus*Pplus-Pplus) and mz(Pminus*Pminus-Pminus)
assert mz(Pplus*Pminus) and Pplus+Pminus==I4
assert s.trace(Pplus)==2 and s.trace(Pminus)==2
assert mz(HD*Pplus-E*Pplus) and mz(HD*Pminus+E*Pminus)
sp=sum((p[i]*sigma[i] for i in range(3)),s.zeros(2))
# Remove the common normalization sqrt((E+m)/(2E)) to keep rational checks.
uraw=I2.col_join(sp/(E+m))
wraw=(-sp/(E+m)).col_join(I2)
norm2=(E+m)/(2*E)
assert mz(norm2*uraw.H*uraw-I2)
assert mz(norm2*wraw.H*wraw-I2)
assert mz(uraw.H*wraw)
assert mz(norm2*uraw*uraw.H-Pplus)
assert mz(norm2*wraw*wraw.H-Pminus)
assert mz(HD*uraw-E*uraw) and mz(HD*wraw+E*wraw)
# Field antiparticle v(p) is the negative-energy spectral basis at -p.
vraw=(sp/(E+m)).col_join(I2)
assert mz(norm2*uraw*uraw.H*beta-(E*gamma[0]-sum((p[i]*gamma[i+1] for i in range(3)),s.zeros(4))+m*I4)/(2*E))
assert mz(norm2*vraw*vraw.H*beta-(E*gamma[0]-sum((p[i]*gamma[i+1] for i in range(3)),s.zeros(4))-m*I4)/(2*E))
C=s.I*gamma[2]*gamma[0]
assert all(C*g.T*C.inv()==-g for g in gamma)

# A finite one-momentum CAR reference: electron up/down, antiparticle up/down.
Z=s.diag(1,-1);a=s.Matrix([[0,1],[0,0]])
def tensor(items):
    r=s.Matrix([[1]])
    for item in items:r=s.kronecker_product(r,item)
    return r
ops=[tensor([Z]*i+[a]+[I2]*(3-i)) for i in range(4)]
ident=s.eye(16)
for i in range(4):
    for j in range(4):
        assert ops[i]*ops[j]+ops[j]*ops[i]==s.zeros(16)
        assert ops[i]*ops[j].H+ops[j].H*ops[i]==(ident if i==j else s.zeros(16))
numbers=[a.H*a for a in ops]
total=sum(numbers,s.zeros(16))
Hf=E*total
q=s.symbols('q',real=True)
Q=q*(numbers[0]+numbers[1]-numbers[2]-numbers[3])
assert Hf*Q-Q*Hf==s.zeros(16)
assert all(x>=0 for x in total.diagonal())
assert all(n*n==n for n in numbers)
# Under a chosen one-particle mode permutation, construct its fermionic lift.
perm=[2,3,0,1];UC=s.zeros(16)
for column in range(16):
    bits=[(column>>(3-i))&1 for i in range(4)]
    mapped=[perm[i] for i,b in enumerate(bits) if b]
    inv=sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))
    outbits=[0]*4
    for i in mapped:outbits[i]=1
    row=sum(b<<(3-i) for i,b in enumerate(outbits))
    UC[row,column]=(-1)**inv
assert UC.H*UC==ident
assert UC*Hf*UC.H==Hf and UC*Q*UC.H==-Q

# Both permutation parities are allowed by a two-copy representation alone.
swap=s.zeros(4)
for i in range(2):
    for j in range(2):swap[j*2+i,i*2+j]=1
sym=(s.eye(4)+swap)/2;anti=(s.eye(4)-swap)/2
for gen in [ss/2 for ss in sigma]:
    totalgen=s.kronecker_product(gen,I2)+s.kronecker_product(I2,gen)
    assert swap*totalgen-totalgen*swap==s.zeros(4)
assert sym*sym==sym and anti*anti==anti
assert s.trace(sym)==3 and s.trace(anti)==1

result=dict(date='2026-11-08',status='all exact Dirac-reference and CAR checks passed',
 assumptions=['conventional Clifford matrices','assigned positive mass','CAR and normal ordering for the field reference',
 'two independent electron and antiparticle spin labels in one momentum mode'],
 clifford_and_projector_identities=True,positive_energy_isometry_and_completeness=True,
 charge_conjugation_clifford_identity=True,
 finite_CAR_modes=4,finite_Fock_dimension=16,free_normal_ordered_energy_nonnegative=True,
 opposite_charge_equal_energy_reference=True,
 two_copy_symmetry_alone_allows_both_exchange_parities=True,
 reference_Fock_spectrum_multiplicities={str(k):s.binomial(4,k).__int__() for k in range(5)},
 full_microcausality_not_tested_by_finite_mode_matrix=True,
 scope='Standard free Dirac reference under imposed quantum/local-field structure; no SEFI matter derivation',
 versions=dict(python=platform.python_version(),sympy=s.__version__))
args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
