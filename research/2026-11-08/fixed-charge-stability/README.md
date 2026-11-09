# Fixed-charge stability assessment and conditional observables

**Exploratory / Not Promoted. AI-assisted, no independent review claimed.**

Read `FIXED_CHARGE_STABILITY.md` for the fixed-charge branch, binding threshold and static radial/angular Hessian. Read `CONDITIONAL_OBSERVABLES.md` for the step 7 charge shape, invariant mass-radius product and missing spin interpretation. Step 6 is not established as full dynamical stability. Conditional step 7 calculations preserve that open prerequisite.

From this directory, with the dependencies in `requirements.txt`:

```
python fixed_charge.py
python threshold.py
python radial_hessian.py
python angular_hessian.py
python conditional_observables.py
```

For predictable runtime, set OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1 before starting Python for dense Hessian solves. The initial iterative eigenvalue attempt was interrupted for slow convergence and replaced by a direct symmetric eigenvalue solve of the same operator. No partial iterative spectrum is used.

`PROTOCOL.md` precedes the initial numerical execution. The threshold search, angular extension and conditional observable calculation are adaptive follow-ups labeled as such. Failed q=.03 continuation is retained; planned higher points are unattempted after the declared stop. The commands generate the CSV background profiles needed for the Hessian and observable calculations; their reference hashes are retained in `generated_profile_hashes.json`. The seed is included as a lossless export of an already public archive, with provenance in `source_manifest.json`.

The static spectra are finite-grid energy diagnostics, not time-evolution frequencies. Ell=1 shifts converge toward translation zero; positive restricted eigenvalues do not certify all dynamical modes. No electron mass, elementary charge, physical spin or observational agreement is derived.

Package text-file and generated-profile hashes use UTF-8 text with LF newlines, so Windows newline translation does not change them. The original NPZ archive hash in the source manifest is a raw-byte archive hash.
