"""Exact algebra and a separate discretized conjugation check; no particle identification."""
from pathlib import Path
import sympy as sp
import numpy as np
import json
import argparse,platform

x,y,h,a=sp.symbols('x y h a', real=True)
lam=sp.symbols('lambda',positive=True)
v=sp.sqrt(3/lam)
rho=x*x+y*y;eta=(v+h)**2+a*a
V=rho**2/4+rho/2+2*rho*eta+lam*(eta-3/lam)**2/4
C={y:-y,a:-a}
assert sp.simplify(V.xreplace(C)-V)==0
H=sp.simplify(sp.hessian(V,(x,y,h,a)).subs({x:0,y:0,h:0,a:0}))
assert (H-sp.diag(1+12/lam,1+12/lam,6,0)).applyfunc(sp.simplify)==sp.zeros(4)
px,py,ph,pa=sp.symbols('px py ph pa',real=True)
qp=x*py-y*px
qs=(v+h)*pa-a*ph
transform={y:-y,a:-a,py:-py,pa:-pa}
assert sp.expand(qp.xreplace(transform)+qp)==0
assert sp.expand(qs.xreplace(transform)+qs)==0
g0,g1,g2,g3=sp.symbols('g0:4',real=True)
cross=px*g0+py*g1+ph*g2+pa*g3
assert sp.expand(cross.xreplace({py:-py,pa:-pa,g1:-g1,g3:-g3})-cross)==0

# Planar real representation has 2*pi identity; it is not a spinor representation.
theta=sp.symbols('theta',real=True)
R=sp.Matrix([[sp.cos(theta),-sp.sin(theta)],[sp.sin(theta),sp.cos(theta)]])
assert R.subs(theta,2*sp.pi)==sp.eye(2)

# Independent sampled field/momentum check, using a periodic spatial grid.
# This is a consistency check, not a localized solution or a vacuum stability run.
rng=np.random.default_rng(20261108)
N=1024; L=16.; z=np.arange(N)*L/N; dz=L/N
fields=[]
for k in range(4):
    c=rng.normal(size=(6,2))
    f=sum(c[n-1,0]*np.sin(2*np.pi*n*z/L)+c[n-1,1]*np.cos(2*np.pi*n*z/L) for n in range(1,7))*.015
    fields.append(f)
phi=fields[0]+1j*fields[1]
sigma=np.sqrt(3/12)+fields[2]+1j*fields[3]
pi_phi=rng.normal(size=N)*.01+1j*rng.normal(size=N)*.01
pi_sigma=rng.normal(size=N)*.01+1j*rng.normal(size=N)*.01
def dx(f):return (np.roll(f,-1)-np.roll(f,1))/(2*dz)
def observables(f,s,p,t):
    r=np.abs(f)**2;e=np.abs(s)**2
    pot=r*r/4+r/2+2*r*e+12/4*(e-3/12)**2
    energy=dz*np.sum((np.abs(p)**2+np.abs(t)**2+np.abs(dx(f))**2+np.abs(dx(s))**2)/2+pot)
    return np.array([energy,dz*np.sum(np.imag(np.conj(f)*p)),dz*np.sum(np.imag(np.conj(s)*t)),dz*np.sum(np.real(np.conj(p)*dx(f)+np.conj(t)*dx(s)))])
o=observables(phi,sigma,pi_phi,pi_sigma)
c=observables(phi.conj(),sigma.conj(),pi_phi.conj(),pi_sigma.conj())
error=np.abs(c-o*np.array([1,-1,-1,1]))
assert np.max(error)<1e-12

# At lambda=12, the stationary tail uses omega below sqrt(2).
w=sp.symbols('omega',real=True)
f,s=sp.symbols('f s',real=True)
Vs=f**4/4+f*f/2+2*f*f*s*s+lam*(s*s-3/lam)**2/4
W=Vs-w*w*f*f/2
assert sp.simplify(W.xreplace({w:-w})-W)==0
# Charge-even fixed-Q stationary energy term and integer winding relation.
Q,I,n=sp.symbols('Q I n',real=True,nonzero=True)
assert (Q**2/(2*I)).subs(Q,-Q)==Q**2/(2*I)
# Angular momentum density uses real product, not imaginary part.
J=sp.re(sp.conjugate(sp.I*w*f)*(sp.I*n*f))
assert sp.simplify(J-n*w*f*f)==0

result={
 'date':'2026-11-08','scope':'Exact identities for the existing canonical two-complex-scalar action; no independent novelty or physical-particle claim',
 'symbolic_checks':{
  'potential_conjugation_invariant':True,'phase_charges_reverse':True,
  'momentum_density_conjugation_invariant':True,
  'vacuum_hessian':str(H),'stationary_equations_even_in_omega':True,
  'fixed_charge_energy_even_in_Q':True,'scalar_rotation_2pi_identity':True,
  'single_winding_Jz_equals_nQ':True},
 'sampled_check':{'lambda':12,'periodic_1D_points':N,'length':L,'seed':20261108,
   'observables_E_Qphi_Qsigma_P':o.tolist(),'conjugates':c.tolist(),'absolute_errors':error.tolist(),
   'not_a_stationary_profile_or_particle_simulation':True},
 'vacuum_at_lambda_12':{'phi_mass_squared':2,'sigma_radial_mass_squared':6,'sigma_phase_mass_squared':0},
 'versions':{'python':platform.python_version(),'sympy':sp.__version__,'numpy':np.__version__}}
parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path,default=Path(__file__).with_name('charge_conjugation_results.json'))
out=parser.parse_args().output
out.write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
