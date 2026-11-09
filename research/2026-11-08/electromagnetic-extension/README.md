# Electromagnetic extension checkpoint

Exploratory / Not Promoted. AI-assisted. Read `ELECTROMAGNETIC_EXTENSION.md` for equations, current conventions, results and limitations, and `PROTOCOL.md` for the declared scan.

Run with Python and the versions in `requirements.txt`:

```
python check_gauge_algebra.py
python check_gauged_profiles.py
```

Five nontrivial scalar-Maxwell profiles were accepted in a fixed-frequency scan. The q=.02 attempt is recorded and rejected as the vacuum. The q=.01 profile passed the enlarged-domain/tighter-tolerance replication. This does not establish dynamical stability, a maximum charge, an electron, or a scalar-to-Dirac map.

`seed_profile.csv` is a lossless decimal export of the three arrays r,f,s in the existing public seed archive; export/import was checked for exact floating-point equality. Public source archive and local archive were verified byte for byte. No student, credential or email material is included. The archive hash is recorded in `source_manifest.json`.

Next: hold the charge number fixed while solving for omega, then constrained perturbation analysis. Full three-dimensional stability and the quantum matter bridge remain open.
