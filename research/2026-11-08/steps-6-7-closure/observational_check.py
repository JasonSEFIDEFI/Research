"""Convergence and conditional calibration; measured inputs are not predictions."""
from pathlib import Path
import json,sys
import numpy as np
from scipy.integrate import simpson
HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'fixed-charge-stability'
if not SOURCE.exists():SOURCE=HERE.parent/'fixed-charge-git'
sys.path.insert(0,str(SOURCE))
from fixed_charge import solve,TARGET
ME_MEV=.51099895069
ALPHA=.0072973525643
HBARC_MEV_FM=197.3269804
E_NATURAL=float(np.sqrt(4*np.pi*ALPHA))
KS=[0.,.01,.025,.05,.1,.2,.5,1.]

def observable(q,pair):
    sol,R=pair;r=np.linspace(0,R,32001);f,fp,s,sp,a,ap,c=sol.sol(r)
    density=(sol.p[0]-q*a)*f*f
    N=float(simpson(4*np.pi*r*r*density,x=r))
    radius=float(np.sqrt(simpson(4*np.pi*r**4*density,x=r)/N))
    ff=[float(simpson(4*np.pi*r*r*density*np.sinc(k*r/np.pi),x=r)/N) for k in KS]
    return dict(charge_number=N,rms_radius=radius,wavenumbers=KS,form_factors=ff)

base,seed=solve(0.)
rows=[]
for R,tol in [(120.,1e-7),(160.,2e-8)]:
    row,pair=solve(.0025,seed,R,tol);assert row['accepted']
    obs=observable(.0025,pair);rows.append(dict(background=row,observables=obs))
changes=dict(energy_relative=abs(rows[0]['background']['energy']/rows[1]['background']['energy']-1),
    radius_relative=abs(rows[0]['observables']['rms_radius']/rows[1]['observables']['rms_radius']-1),
    form_factor_max_absolute=float(max(abs(np.array(rows[0]['observables']['form_factors'])-np.array(rows[1]['observables']['form_factors'])))))
bound=rows[1];energy=bound['background']['energy'];radius=bound['observables']['rms_radius']
scale=ME_MEV/energy
# Optional second fit changes q, hence solve a new background; do not reuse its spectrum.
qfit=E_NATURAL/TARGET
fit,pair=solve(qfit,seed,160.,2e-8);assert fit['accepted']
fitobs=observable(qfit,pair);fitscale=ME_MEV/fit['energy']
result=dict(status='Exploratory / Not Promoted',nist_source='https://physics.nist.gov/cuu/Constants/Table/allascii.txt',
    codata_adjustment=2022,measured_inputs=dict(electron_rest_energy_MeV=ME_MEV,alpha=ALPHA,hbar_c_MeV_fm=HBARC_MEV_FM,
        electron_magnetic_moment_J_per_T=-9.2847646917e-24,electron_g_factor=-2.00231930436092),
    convergence=changes,backgrounds=rows,
    mass_only_calibration=dict(scale_MeV=scale,radius_m=radius/scale*HBARC_MEV_FM*1e-15,
        absolute_charge_over_elementary_charge=bound['background']['electric_charge']/E_NATURAL,
        energy_radius=energy*radius,magnetic_dipole=0.),
    optional_mass_and_charge_fit=dict(q_fitted=qfit,background=fit,observables=fitobs,scale_MeV=fitscale,
        radius_m=fitobs['rms_radius']/fitscale*HBARC_MEV_FM*1e-15,
        absolute_charge_over_elementary_charge=fit['electric_charge']/E_NATURAL,
        magnetic_dipole=0.,stability='Not tested on this separately fitted background'),
    assessment='Direct identification of either static spherical classical configuration with the electron fails its nonzero magnetic response. Mass and charge fits do not derive them; no quantum-current map is supplied.')
(HERE/'observational_check_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['convergence','mass_only_calibration','assessment']},indent=2))
assert max(changes.values())<1e-5 and abs(rows[1]['observables']['form_factors'][0]-1)<1e-10
