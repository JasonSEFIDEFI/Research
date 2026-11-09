"""Adaptive follow-up: locate the fixed-N free-particle energy crossing."""
from pathlib import Path
import json
from scipy.optimize import brentq
from fixed_charge import solve,TARGET
HERE=Path(__file__).resolve().parent
attempts=[]
base,pair=solve(0.)
def gap(q):
    row,_=solve(float(q),pair)
    attempts.append(row)
    if not row['accepted']:raise RuntimeError('Rejected root-search profile')
    return row['binding_margin']
root=brentq(gap,.005,.01,xtol=1e-9)
row,_=solve(root,pair,radius=160.,tol=2e-8)
result=dict(status='Exploratory / Not Promoted',purpose='Adaptive follow-up to the observed sign change, not part of the initial scan',
    q_crossing=root,target_number=TARGET,attempts=attempts,replication=row,
    limit='Energetic equality with dispersed free charged scalars; not a dynamical stability boundary or elementary charge prediction')
(HERE/'threshold_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'q_crossing':root,'replication_binding_margin':row['binding_margin'],'accepted':row['accepted']}))
assert row['accepted'] and abs(row['binding_margin'])<1e-5
