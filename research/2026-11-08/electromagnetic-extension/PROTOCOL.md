# Electromagnetic extension: preregistered scope

Exploratory / Not Promoted. AI-assisted calculations, 2026-11-08.

Derive a minimal U(1) extension of the previously specified canonical two-complex-scalar model. Keep Sigma neutral, Phi charged; introduce Maxwell kinetic energy. This is an added action, not an emergence proof. Separately record minimal coupling of the conditional Dirac reference; do not identify its spinor with either scalar.

Use metric (+---), D=partial+iqA, Phi=exp(-i omega t)f(r), A0=a(r), Sigma=s(r). Fix a(infinity)=0. Check local gauge covariance, current normalization, charge conjugation, the photon mass if Sigma were charged, and Gauss' law.

Numerics: lambda=12, omega=1.401223084350689, seed from the existing public ungauged Q1250 calculation. Continue q=0, .0025, .005, .01, .015, .02 at fixed omega, stopping if the boundary-value solver fails or the branch becomes trivial. No claim of maximum charge or stability from this scan. Use r in [0,120], tolerance 1e-7, 801 initial points, max 30000 nodes. Repeat q=.01 at R=160 and tolerance 2e-8. Require positive nodeless nontrivial f, converged solver, residual below tolerance, Gauss charge/flux agreement below 1e-5 relative, and replication agreement below 1e-4 relative in charge number and total energy. Include analytic exterior Coulomb energy. If continuation fails report it rather than changing the protocol invisibly.

At fixed omega both charge number and energy may move; this is not a fixed-charge binding comparison. No time-dependent stability, quantum spin/statistics, physical units, elementary charge magnitude, or electron mass is inferred.
