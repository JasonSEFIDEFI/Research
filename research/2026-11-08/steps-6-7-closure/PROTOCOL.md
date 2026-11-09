# Steps 6–7 closure audit protocol

Exploratory / Not Promoted. AI-assisted. Written before this checkpoint's numerical runs.

Use the bound scalar-Maxwell candidate q=.0025, lambda=12, N=1250.1753361265248, with the preceding action unchanged. Recompute its constrained real-amplitude Hessian at ell=0,1,2,3 on R=80,h=.2,.1,.05, and R=120,h=.1. Inspect eigenpair residuals below 1e-6, grid convergence, translation zero modes, and the finite-grid high-ell potential bound. These tests must be on the same background used for the observables.

Derive the complete radial charged Cartesian-amplitude/phase Hamiltonian linearization in Coulomb gauge, eliminate the electric constraint using the Coulomb Green function, and reduce the global fixed-charge/gauge pair symplectically. Include the coupled neutral real amplitude; treat the neutral imaginary mode separately. Check canonical-charge conservation, symmetry of the energy matrix, its constrained smallest eigenvalues and eigenpair residuals. Compute the complete finite-grid Hamiltonian spectrum on R=60,h=.4,.2, with projected constraint and gauge pair removed. A finite real part above 1e-6 is a failure to investigate, not automatically a physical instability. Repeat energy tests on R=80,h=.1. No finite-box test certifies nonlinear infinite-volume stability.

Repeat observables on R=120,tol=1e-7 and R=160,tol=2e-8; require relative radius and energy changes below 1e-5, normalized F(0) within 1e-10, and form-factor changes below 1e-5 absolute for sampled k. Quantify conditional mass/charge calibration and spin/current mismatch using primary physical references; do not fit a physical length independently after choosing mass units.

Record steps 6 and 7 as passed only if their actual requirements have been met. If dynamical/global stability or the physical spin/current map remains unproved, retain that requirement as open. Prepare a review dossier with explicit failed requirements rather than declaring completion by renaming the requirements. No independent reviewer is contacted or represented as having reviewed the work.
