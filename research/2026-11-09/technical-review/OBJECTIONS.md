# Objection and response register — 9 November 2026

Exploratory / Not Promoted. All objections below were raised in AI self-audit; none is attributed to an outside reviewer.

| Issue | Severity | Evidence/response | Disposition |
|---|---|---|---|
| Interpolated profile is not stationary on the stability grid; projecting out an approximate gauge vector changes the finite system | Major numerical construction | New variational-grid Newton solve; defects fall to 1.81e-13 or less; spectra and energy recomputed | Corrected for declared radial grids |
| Assembled phase/Coulomb Hamiltonian might have a sign or factor error | Major if present | Original canonical energy differentiated independently in 18 variables; max difference 8.89e-16 | No error found in checked identity |
| Archive and observables might not reproduce | Major if present | Both manifests pass; isolated-directory Schur and observable reruns reproduce the selected outputs exactly | Passed on same runtime only |
| Positive energy and imaginary spectrum might be counted as independent validations | Interpretation | They are linked by a finite-dimensional Hamiltonian theorem; retain as implementation checks | Scope clarified |
| Finite radial spectra and sampled angular sectors are insufficient for nonlinear infinite-volume 3D stability | Major open proof obligation | Corrected discrete evidence does not prove coercivity, well-posedness, massless-channel control or fragmentation bounds | Open; broad step 6 not passed |
| Static spherical scalar current cannot match electron magnetic response | Major physical obstruction | Current/dipole vanish for this ansatz; measured moment is nonzero; fitting scales cannot change zero | Direct identification fails; quantum bridge open |
| Established gauged two-field Q-ball literature may already explain the mechanism | Novelty obligation | Primary FLS/gauged-FLS comparison added; action differences explicit; no novelty asserted | No novelty pass; exhaustive comparison open |
| Self-audit is not independent review | Step 8 process requirement | Same AI authored calculations and this audit; separate code is not a separate reviewer | Independent review still required |

Closing a numerical issue does not close an unrelated physical or review requirement. This register must accompany any review request or later claim of completion.
