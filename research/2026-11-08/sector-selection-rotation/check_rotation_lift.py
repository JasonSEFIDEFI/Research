"""Kinematic comparison of original and diagonal rotation actions.

No claim that the diagonal action is selected or extends to the Lorentz group.
"""
from pathlib import Path
import argparse,json,platform
import sympy as s
parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path,default=Path(__file__).with_name('rotation_lift_results.json'))
args=parser.parse_args()
plus=s.Matrix([[0,0,0],[s.sqrt(2),0,0],[0,s.sqrt(2),0]])
minus=plus.T
L=[(plus+minus)/2,(plus-minus)/(2*s.I),s.diag(-1,0,1)]
S=[s.Matrix([[0,1],[1,0]])/2,s.Matrix([[0,-s.I],[s.I,0]])/2,s.diag(1,-1)/2]
LL=[s.kronecker_product(a,s.eye(2)) for a in L]
SS=[s.kronecker_product(s.eye(3),a) for a in S]
def comm(a,b):return (a*b-b*a).applyfunc(s.simplify)
for a in LL:
    for b in SS:assert comm(a,b)==s.zeros(6)
diag=[a+b for a,b in zip(LL,SS)]
for gens in [LL,diag]:
    for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]:assert comm(gens[i],gens[j])==s.I*gens[k]
c=s.symbols('c',real=True)
mixed=[a+c*b for a,b in zip(LL,SS)]
defect=comm(mixed[0],mixed[1])-s.I*mixed[2]
assert (defect-s.I*(c*c-c)*SS[2]).applyfunc(s.simplify)==s.zeros(6)
assert s.solve(c*c-c,c)==[0,1]
orbital2pi=s.diag(*[s.simplify(s.exp(-2*s.pi*s.I*LL[2][k,k])) for k in range(6)])
diagonal2pi=s.diag(*[s.simplify(s.exp(-2*s.pi*s.I*diag[2][k,k])) for k in range(6)])
assert orbital2pi==s.eye(6) and diagonal2pi==-s.eye(6)
casimir=sum((g*g for g in diag),s.zeros(6)).applyfunc(s.simplify)
assert casimir.eigenvals()=={s.Rational(3,4):2,s.Rational(15,4):4}
# The stated original boosts, which act trivially on internal labels, have
# [K_i,K_j]=-i eps_ijk L_k; using the new J leaves an i eps S mismatch.
boost_mismatch=s.I*SS[2]
assert boost_mismatch!=s.zeros(6)
result=dict(date='2026-11-08',status='all exact rotation-comparison checks passed',
 assumptions=['orbital l=1 representation','chosen internal N=1 doublet','commuting orbital and internal algebras'],
 homogeneous_generator_mixtures_closing_su2=['c=0','c=1'],
 original_spatial_2pi='identity',chosen_diagonal_2pi='minus identity',
 diagonal_total_casimir={'3/4':2,'15/4':4},
 original_boosts_fail_for_new_rotation_generator=True,
 spatial_rotation_assignment_selected_by_action=False,
 scope='Kinematic representation comparison; not a constructed relativistic SEFI theory or electron',
 versions=dict(python=platform.python_version(),sympy=s.__version__))
args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
