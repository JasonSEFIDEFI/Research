# Step 8 technical audit protocol — 9 November 2026

Exploratory / Not Promoted. AI self-audit, not an independent external review.

Review pinned parent 9e3bdeca7c48ed14922e7aee77f1b75b27945d53. Preserve all earlier claims and results as historical records; corrections must be explicit. No reviewer is contacted or claimed.

1. Verify the downloaded package's normalized manifests, regenerate the Schur check, and inspect code/derivations for current, constraint, normalization and boundary inconsistencies.
2. Independently differentiate a small finite-dimensional Cartesian canonical Hamiltonian and compare its Hessian against the assembled Coulomb-gauge matrix. Require maximum absolute matrix difference <1e-10.
3. Investigate the nonzero discrete gauge-mode defects. Solve the stationary fixed-N equations on the SAME variational finite-difference grid as the linearized Hamiltonian rather than interpolating an unrelated continuum BVP background. Use q=.0025, N=1250.1753361265248, lambda=12, R60/h=.4,.2 and R80/h=.1. Newton convergence requires field residual <1e-10 and relative charge residual <1e-10; stop/report failure if 20 damped iterations do not converge. No model/action change is allowed.
4. Reassemble the full radial Hamiltonian on those discrete critical points. Require symmetry <1e-10, gauge/null and charge-conservation defects <1e-9, and low-eigenpair residuals <1e-7. Compute full physical quotient spectra for the two R60 grids; investigate any real growth >1e-6. Test R80/h=.1 constrained energy. Compare energies, frequencies and charge-shape radius with previous results; report discretization changes rather than demanding equality of different discretizations.
5. Check finite-generator Hessian corrections against the numerical static Schur identity and map conclusions to actual tested domains. An exact gauge identity fixes a technical review issue; it does not prove nonlinear continuum stability.
6. Issue an objection/response register and bounded verdict. Internal reproducibility or algebra checks may pass while independent review and the physical-matter claim remain unpassed. Do not turn numerical non-growth into an observation or add spin/current structure to force a pass.
