"""Exact tests for geometry-independent oscillator SU(2) generators.

Mass-normalized coordinates x have kinetic energy sum(p^2)/2. The functions
f and g absorb the manuscript's positive metric weights. No spacetime-spin
or full reduced-worldline Hamiltonian claim is made.
"""
import argparse,json,platform
from pathlib import Path
import sympy as s
parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path,default=Path(__file__).with_name('full_symmetry_results.json'))
args=parser.parse_args()
x=s.symbols('O A S W',real=True);p=s.symbols('pO pA pS pW',real=True)
O,A,S,W=x;pO,pA,pS,pW=p
omega=s.symbols('omega',positive=True)
K,T=s.symbols('K T',real=True)
f=s.Function('f');g=s.Function('g')
def pb(a,b):return s.expand(sum(s.diff(a,xx)*s.diff(b,pp)-s.diff(a,pp)*s.diff(b,xx) for xx,pp in zip(x,p)))
def assertzero(a):assert s.simplify(a)==0,a
def generators(i,j,ci=0,cj=0):
    u=x[i]-ci;v=x[j]-cj;r=p[i];t=p[j]
    return [(omega*u*v+r*t/omega)/2,(u*t-r*v)/2,
            (omega*u*u+r*r/omega-omega*v*v-t*t/omega)/4]
H0=sum(pp*pp+omega**2*xx*xx for xx,pp in zip(x,p))/2
U=K*f(A)*S+T*g(A)*W
H=H0+U
J=generators(0,1)
D=K*s.diff(f(A),A)*S+T*s.diff(g(A),A)*W
rates=[s.factor(pb(j,H)) for j in J]
expected=[-pO*D/(2*omega),-O*D/2,pA*D/(2*omega)]
for a,b in zip(rates,expected):assertzero(a-b)
for a,b,c in [(0,1,2),(1,2,0),(2,0,1)]:assertzero(pb(J[a],J[b])-J[c])

# General natural-Hamiltonian necessity from Jz, without assuming quadratic V.
V=s.Function('V')(*x)
Hv=sum(pp*pp for pp in p)/2+V
for i,j in [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]:
    gz=generators(i,j)[2]
    formula=(p[i]*(omega**2*x[i]-s.diff(V,x[i]))-p[j]*(omega**2*x[j]-s.diff(V,x[j])))/(2*omega)
    assertzero(pb(gz,Hv)-formula)

c1,c2=s.symbols('c1 c2',real=True)
# Conditions sufficient for arbitrary independent geometry jets K,T.
joint_cases={
 'OA':(0,1,c1,c2),
 'OS':(0,2,s.Integer(0),g(A)),
 'OW':(0,3,f(A),s.Integer(0)),
 'AS':(1,2,s.Integer(0),c2),
 'AW':(1,3,c1,s.Integer(0)),
 'SW':(2,3,s.Integer(0),s.Integer(0))}
joint_results={}
for label,(i,j,ff,gg) in joint_cases.items():
    hh=H0+K*ff*S+T*gg*W
    rr=[s.factor(pb(jj,hh)) for jj in generators(i,j)]
    assert all(z==0 for z in rr),(label,rr)
    joint_results[label]=[str(z) for z in rr]

# Constant prescribed nonzero geometry permits fixed affine forcing shifts.
fixed_cases={
 'OA':(0,1,c1,c2), 'OS':(0,2,c1,g(A)),
 'OW':(0,3,f(A),c2), 'AS':(1,2,c1,c2),
 'AW':(1,3,c1,c2),'SW':(2,3,c1,c2)}
fixed_results={}
for label,(i,j,ff,gg) in fixed_cases.items():
    hh=H0+K*ff*S+T*gg*W
    centers=[0,0,-K*c1/omega**2,-T*c2/omega**2]
    rr=[s.factor(pb(jj,hh)) for jj in generators(i,j,centers[i],centers[j])]
    assert all(z==0 for z in rr),(label,rr)
    fixed_results[label]=[str(z) for z in rr]

# Merely inserting an instantaneous equilibrium is not conservation.
Kd,Td=s.symbols('K_dot T_dot',real=True)
moving=generators(0,2,0,-K*c1/omega**2)
forceH=H0+K*c1*S+T*(A+A**3)*W
moving_rates=[s.simplify(pb(jj,forceH)+s.diff(jj,K)*Kd+s.diff(jj,T)*Td) for jj in moving]
assert any(z!=0 for z in moving_rates)
assert all(s.simplify(z.subs(Kd,0))==0 for z in moving_rates)

# Broken and exact examples use the same selected OA oscillator generators.
nonlinear=[s.factor(pb(jj,H0+K*A*A*S+T*c2*W)) for jj in J]
linear=[s.factor(pb(jj,H0+K*(c1+A)*S+T*c2*W)) for jj in J]
assert any(z!=0 for z in nonlinear) and any(z!=0 for z in linear)

# A rotated nonlinear dark mode was not covered by the coordinate-pair table.
B,DD,pB,pD=s.symbols('B D pB pD',real=True)
u,v=s.symbols('u v',real=True)
rad=s.sqrt(u*u+v*v)
alpha=s.symbols('OmegaA_squared',positive=True)
F=s.Function('F')
rot={S:(u*B-v*DD)/rad,W:(v*B+u*DD)/rad,
     pS:(u*pB-v*pD)/rad,pW:(v*pB+u*pD)/rad}
original=(pO*pO+pA*pA+pS*pS+pW*pW)/2+omega**2*(O*O+S*S+W*W)/2+alpha*A*A/2+(u*S+v*W)*F(A)
transformed=s.simplify(original.subs(rot,simultaneous=True))
expected_dark=(pO*pO+pA*pA+pB*pB+pD*pD)/2+omega**2*(O*O+B*B+DD*DD)/2+alpha*A*A/2+rad*F(A)*B
assertzero(transformed-expected_dark)
xx=[O,A,B,DD];pp=[pO,pA,pB,pD]
def darkpb(a,b):return s.simplify(sum(s.diff(a,q)*s.diff(b,p)-s.diff(a,p)*s.diff(b,q) for q,p in zip(xx,pp)))
darkJ=[(omega*O*DD+pO*pD/omega)/2,(O*pD-pO*DD)/2,
       (omega*O*O+pO*pO/omega-omega*DD*DD-pD*pD/omega)/4]
dark_rates=[darkpb(j,transformed) for j in darkJ]
assert all(z==0 for z in dark_rates)
for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]:assertzero(darkpb(darkJ[i],darkJ[j])-darkJ[k])
darkN=(omega*(O*O+DD*DD)+(pO*pO+pD*pD)/omega)/2
assertzero(darkpb(darkN,transformed))
R=s.symbols('R',positive=True)
Vp=omega**2*(O*O+B*B+DD*DD)/2+alpha*A*A/2+R*F(A)*B
completion=omega**2*(O*O+DD*DD+(B+R*F(A)/omega**2)**2)/2+alpha*A*A/2-R**2*F(A)**2/(2*omega**2)
assertzero(Vp-completion)
example_hess=s.hessian(Vp.subs({omega:1,alpha:4,R:s.sqrt(13)/6,F(A):s.sin(A)}),(O,A,B,DD)).subs({O:0,A:0,B:0,DD:0})
assert all(example_hess[:n,:n].det()>0 for n in range(1,5))
theta_dot=s.symbols('theta_dot',real=True)
moving_coupling=-theta_dot*(B*pD-DD*pB)
moving_dark=[s.factor(darkpb(j,moving_coupling)) for j in darkJ]
assert any(z!=0 for z in moving_dark)

result=dict(date='2026-11-08',status='all exact symmetry checks passed',
 scope='Fixed oscillator SU(2): six coordinate-aligned cases and one exact nonlinear rotated dark-mode family; not every nonlinear or geometry-dependent symmetry',
 assumptions=['positive constant kinetic weights absorbed by canonical mass normalization',
 'geometry jets K and T can vary independently for joint-action classification',
 'selected pair bare frequencies equal reference omega',
 'constant affine centers for fixed-geometry cases'],
 general_Jz_necessity_checked_for_six_pairs=True,
 OA_exact_generator_rates=[str(z) for z in rates],
 arbitrary_geometry_sufficient_case_checks=joint_results,
 fixed_geometry_shifted_case_checks=fixed_results,
 moving_equilibrium_generator_rates=[str(z) for z in moving_rates],
 nonconstant_authorship_counterexamples=dict(linear=[str(z) for z in linear],quadratic=[str(z) for z in nonlinear]),
 nonlinear_dark_mode=dict(assumptions=['OmegaO=OmegaS=OmegaW','fixed coupling direction (u,v) nonzero','common arbitrary smooth F(A)'],
  transformed_Hamiltonian=str(expected_dark),generator_rates=[str(z) for z in dark_rates],
  oscillator_number_conserved=True,square_completion_verified=True,
  bounded_sine_example_positive_hessian=True,example_hessian=str(example_hess),
  moving_frame_generator_rates=[str(z) for z in moving_dark],
  general_independent_geometry_motion_not_classified=True),
 spatial_spin_or_electron_identification=False,
 versions=dict(python=platform.python_version(),sympy=s.__version__))
args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
