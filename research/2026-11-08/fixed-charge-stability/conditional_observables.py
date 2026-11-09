"""Step 7 entry: conditional classical charge form factors, not electron predictions."""
from pathlib import Path
import json
import numpy as np
from scipy.integrate import simpson
from fixed_charge import solve,profile
HERE=Path(__file__).resolve().parent
base,pair=solve(0.)
bound,pair=solve(.0025,pair,radius=160.,tol=2e-8)
assert bound['accepted'] and bound['binding_margin']>0
profile('profile_q00025.csv',pair)
sol,R=pair;r=np.linspace(0,R,32001);f,fp,s,sp,a,ap,c=sol.sol(r)
omega=bound['omega'];density=(omega-.0025*a)*f*f
N=float(simpson(4*np.pi*r*r*density,x=r))
radius2=float(simpson(4*np.pi*r**4*density,x=r)/N)
radius4=float(simpson(4*np.pi*r**6*density,x=r)/N)
ks=[0.,.01,.025,.05,.1,.2,.5,1.]
form=[dict(wavenumber=k,normalized_charge_form_factor=float(simpson(4*np.pi*r*r*density*np.sinc(k*r/np.pi),x=r)/N)) for k in ks]
k=.0001
F=float(simpson(4*np.pi*r*r*density*np.sinc(k*r/np.pi),x=r)/N)
radius_from_slope=6*(1-F)/k**2
result=dict(status='Exploratory / Not Promoted',scope='Step 7 conditional observables of a bound classical scalar-Maxwell background; full dynamical stability pending',
    background=bound,charge_rms_radius=float(np.sqrt(radius2)),charge_fourth_moment=radius4,
    energy_times_charge_rms_radius=float(bound['energy']*np.sqrt(radius2)),
    form_factors=form,small_k_slope_radius_squared=radius_from_slope,
    radius_slope_relative_error=abs(radius_from_slope-radius2)/radius2,
    classical_angular_momentum=0.,magnetic_dipole_moment=0.,
    limitation='No physical mass or length calibration, spin-half identification or measured comparison is derived.')
(HERE/'conditional_observables_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2));assert result['radius_slope_relative_error']<1e-5
