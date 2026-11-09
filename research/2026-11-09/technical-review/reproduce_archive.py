"""Verify and rerun selected checks from the preceding downloadable archive."""
from pathlib import Path
import argparse,zipfile,json,subprocess,sys,hashlib
parser=argparse.ArgumentParser()
parser.add_argument('archive',type=Path)
parser.add_argument('--directory',type=Path,required=True)
args=parser.parse_args();root=args.directory.resolve();root.mkdir(parents=True,exist_ok=True)
checks=[]
with zipfile.ZipFile(args.archive) as z:
    for folder in ['fixed-charge-stability','steps-6-7-closure']:
        m=json.loads(z.read(folder+'/manifest.json'))
        assert all(hashlib.sha256(z.read(folder+'/'+k)).hexdigest()==v for k,v in m['files'].items())
        checks.append(dict(folder=folder,checked=len(m['files']),passed=True))
    for member in z.namelist():assert (root/member).resolve().is_relative_to(root)
    z.extractall(root)
closure=root/'steps-6-7-closure';before=json.loads((closure/'observational_check_results.json').read_text())
for script in ['check_schur.py','observational_check.py']:
    run=subprocess.run([sys.executable,str(closure/script)],capture_output=True,text=True,check=True)
    (root/(script+'.log')).write_text(run.stdout+run.stderr,encoding='utf-8')
after=json.loads((closure/'observational_check_results.json').read_text())
diffs={k:abs(before['mass_only_calibration'][k]-after['mass_only_calibration'][k]) for k in ['scale_MeV','radius_m','absolute_charge_over_elementary_charge','energy_radius']}
assert max(diffs.values())<1e-8
result=dict(status='Exploratory / Not Promoted',kind='Same-agent isolated-directory rerun from saved archive; not external replication',
    archive_sha256=hashlib.sha256(args.archive.read_bytes()).hexdigest(),manifests=checks,
    rerun_scripts=['check_schur.py','observational_check.py'],mass_calibration_absolute_differences=diffs,passed=True)
Path(__file__).with_name('reproduction_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
