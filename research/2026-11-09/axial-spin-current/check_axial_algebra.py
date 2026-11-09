"""Exact algebra for the specified axial scalar-Maxwell ansatz and weak-probe bound."""
from pathlib import Path
import json
import sympy as s
R,z=s.symbols('R z',positive=True,real=True)
q,w,n,t=s.symbols('q omega n t',real=True,nonzero=True)
f=s.Function('f')(R,z);h=s.Function('s')(R,z);a=s.Function('a')(R,z);b=s.Function('b')(R,z)
Om=w-q*a;k=n+q*b
V=f**4/4+f*f/2+2*f*f*h*h+t*t*(h*h-3/t**2)**2/4
integrand=R*((s.diff(f,R)**2+s.diff(f,z)**2+s.diff(h,R)**2+s.diff(h,z)**2)/2+V+k*k*f*f/(2*R**2)-Om*Om*f*f/2
    -(s.diff(a,R)**2+s.diff(a,z)**2)/2+(s.diff(b,R)**2+s.diff(b,z)**2)/(2*R**2))
EL=lambda x:s.simplify((s.diff(integrand,x)-s.diff(s.diff(integrand,s.diff(x,R)),R)-s.diff(s.diff(integrand,s.diff(x,z)),z))/R)
lap=lambda x:s.diff(x,R,2)+s.diff(x,R)/R+s.diff(x,z,2)
checks={}
checks['charged_amplitude_EL']=s.simplify(EL(f)-(-lap(f)+(1+f*f+4*h*h+k*k/R**2-Om*Om)*f))==0
checks['neutral_amplitude_EL']=s.simplify(EL(h)-(-lap(h)+(4*f*f+t*t*h*h-3)*h))==0
checks['Gauss_EL']=s.simplify(EL(a)-(lap(a)+q*Om*f*f))==0
checks['azimuthal_Maxwell_EL']=s.simplify(R**2*EL(b)-(-s.diff(b,R,2)+s.diff(b,R)/R-s.diff(b,z,2)+q*k*f*f))==0
# Local angular-momentum identity including the cylindrical divergence term.
div=lambda u,v:s.diff(R*u,R)/R+s.diff(v,z)
Jdensity=Om*k*f*f-s.diff(a,R)*s.diff(b,R)-s.diff(a,z)*s.diff(b,z)
checks['angular_momentum_boundary_identity']=s.simplify(Jdensity-n*Om*f*f+div(b*s.diff(a,R),b*s.diff(a,z))-b*(lap(a)+q*Om*f*f))==0
rho,eta=s.symbols('rho eta',nonnegative=True)
potential=rho*rho/4+rho/2+2*rho*eta+t*t*(eta-3/t**2)**2/4
c=1+3/t
checks['potential_sum_of_squares']=s.expand(2*potential-c*rho-(rho+t*eta-3/t)**2/2-(4-t)*rho*eta)==0
checks['screened_b_transformation']=s.simplify((s.diff(R**2*b,R,2)-s.diff(R**2*b,R)/R+s.diff(R**2*b,z,2))/R**2-(s.diff(b,R,2)+3*s.diff(b,R)/R+s.diff(b,z,2)))==0
K,T,U=s.symbols('K T U',real=True)
checks['virial_energy_identity']=s.simplify((K+T+U).subs(U,T-K/3)-(2*T+2*K/3))==0
bound=s.sqrt(2/(1+s.sqrt(3)/2))
result=dict(status='Exploratory / Not Promoted',sympy=s.__version__,checks=checks,all_passed=all(checks.values()),
    lambda_12_weak_probe_g_upper_exact=str(bound),lambda_12_weak_probe_g_upper=float(bound),
    lambda_threshold_for_upper_less_than_2=str(12-8*s.sqrt(2)),
    scope='Exact identities and conditional bound; no existence, novelty, independent review or half-spin derivation')
Path(__file__).with_name('axial_algebra_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2));assert result['all_passed']
