"""Adaptive follow-up: sampled nonradial static amplitude sectors, not dynamics."""
from pathlib import Path
import json
from radial_hessian import evaluate
HERE=Path(__file__).resolve().parent
data=json.loads((HERE/'fixed_charge_results.json').read_text());rows=[]
for q,path in [(0.,'profile_q0.csv'),(.01,'profile_q001.csv')]:
    w=next(x['omega'] for x in data['continuation'] if x['q']==q)
    for ell in [1,2,3]:
        for h in [.2,.1,.05]:
            row=evaluate(q,w,path,80.,h,ell,False);rows.append(row)
            print(json.dumps({k:row[k] for k in ['q','ell','h','lowest_eigenvalues','sampled_high_ell_bound']}),flush=True)
(HERE/'angular_hessian_results.json').write_text(json.dumps(dict(status='Exploratory / Not Promoted',
    scope='Adaptive extension after the radial test: static real-amplitude harmonics, no dynamical modes',results=rows),indent=2)+'\n')
assert all(max(x['eigenpair_residuals'])<1e-6 for x in rows)
