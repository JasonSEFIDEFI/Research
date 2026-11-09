"""Exact checks for the explicitly added scalar U(1) extension."""
from pathlib import Path
import json
import sympy as s
x=s.symbols('x',real=True);q,w,lam=s.symbols('q omega lambda',real=True)
f=s.Function('f')(x);theta=s.Function('theta')(x);a=s.Function('a')(x);chi=s.Function('chi')(x)
phi=f*s.exp(s.I*theta)
D=lambda z,A:s.diff(z,x)+s.I*q*A*z
checks={}
checks['covariant_derivative']=s.simplify(D(s.exp(-s.I*q*chi)*phi,a+s.diff(chi,x))-s.exp(-s.I*q*chi)*D(phi,a))==0
# Half-normalized scalar: dL/dA=q Im(phi* D phi); Maxwell j=-dL/dA.
A,t,f0,om=s.symbols('A t f0 om',real=True)
kin=s.Rational(1,2)*f0**2*(-w+q*A)**2
checks['scalar_current_sign_and_half_normalization']=s.simplify(-s.diff(kin,A)-q*(w-q*A)*f0**2)==0
rho,eta=s.symbols('rho eta',real=True)
V=rho**2/4+rho/2+2*rho*eta+lam*(eta-3/lam)**2/4
checks['phi_potential_force']=s.expand(2*s.diff(V,rho)-(rho+1+4*eta))==0
checks['sigma_potential_force']=s.expand(2*s.diff(V,eta)-(4*rho+lam*eta-3))==0
# Charge conjugation (w,a)->(-w,-a): source changes sign, squares unchanged.
checks['charge_conjugation_source']=s.expand(q*(-w+q*A)*f0**2+q*(w-q*A)*f0**2)==0
checks['charge_conjugation_energy']=s.expand((-w+q*A)**2-(w-q*A)**2)==0
qs,v=s.symbols('q_sigma v',real=True)
checks['charged_condensate_photon_mass_squared']=s.diff(s.Rational(1,2)*qs**2*v**2*A**2,A,2)==qs**2*v**2
checks['radial_gauss_divergence']=s.simplify(s.diff(x*x*s.diff(a,x),x)/x**2-s.diff(a,x,2)-2*s.diff(a,x)/x)==0
result={'status':'Exploratory / Not Promoted','sympy':s.__version__,'checks':checks,'all_passed':all(checks.values()),
 'limits':'These finite algebra checks do not prove dynamical stability or derive the charge coupling.'}
Path(__file__).with_name('gauge_algebra_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2));assert result['all_passed']
