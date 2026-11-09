"""Apply the earlier static tests to the actual bound observable background."""
from pathlib import Path
import json,sys
HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'fixed-charge-stability'
if not SOURCE.exists():SOURCE=HERE.parent/'fixed-charge-git'
sys.path.insert(0,str(SOURCE))
from radial_hessian import evaluate
data=json.loads((SOURCE/'conditional_observables_results.json').read_text())
w=data['background']['omega'];rows=[]
for ell in [0,1,2,3]:
    for R,h in [(80.,.2),(80.,.1),(80.,.05),(120.,.1)]:
        row=evaluate(.0025,w,str(SOURCE/'profile_q00025.csv'),R,h,ell,ell==0)
        rows.append(row);print(json.dumps({k:row[k] for k in ['ell','radius','h','lowest_eigenvalues','sampled_high_ell_bound']}),flush=True)
(HERE/'candidate_static_results.json').write_text(json.dumps(dict(status='Exploratory / Not Promoted',q=.0025,results=rows),indent=2)+'\n')
assert all(max(x['eigenpair_residuals'])<1e-6 for x in rows)
