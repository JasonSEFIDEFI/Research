# One quantum sector test protocol

November 8, 2026. Record written before the computations in this directory.

Use the exact fixed-geometry sine-coupling example already recorded in the preceding checkpoint. In its dimensionless canonical units and with hbar=1:

- Dark pair O,D: frequency 1, H_OD=N+1, degeneracy N+1.
- Remaining A,B: H_AB=(p_A^2+p_B^2)/2+2 A^2+B^2/2+(sqrt(13)/6) sin(A) B.
- No new parameter is fitted or optimized in this test.

Questions: does conservation of N select N=1; is the dark doublet the lowest nonvacuum excitation; what changes if N=1 is imposed as an additional constraint?

First derive an operator lower bound on E0_AB by completing the B oscillator square and using sin(A)^2<=A^2. Bound E1_AB above with a two-dimensional Rayleigh–Ritz space consisting of |0,0> and a fixed trial vector proportional to |0,1>-(3/16)|1,0>-(3/32)|1,2>. The trial coefficients are fixed here, before spectral evaluation. Compare the resulting excitation-gap upper bound with dark gap 1. Check any strict comparison with explicit rational inequalities rather than floating-point eigenvalues alone.

Separately compute the lowest six Ritz values in nested product oscillator bases of sizes 8,12,18,26,36,48 per coordinate. Use the exact infinite-basis matrix elements of sin(A), not the sine of a truncated position matrix. Validate low-order matrix entries against independent 128-point Gauss–Hermite quadrature, tolerance 2e-12. Verify symmetry and finite-matrix eigenpair residuals; target residual below 1e-9. Require the last two basis sizes to agree within 1e-8 for the six reported values before describing them as numerically converged. Differences of Ritz upper bounds are numerical gap estimates, not rigorous gap bounds.

No experimental data, physical electron units, thermal state, spin lift or electromagnetic field is introduced. Canonical bosonic quantization is an explicit assumption. Retain negative results. If the prescribed trial bound is inconclusive, report that before any revised calculation. No particle or novelty claim follows from this protocol.
