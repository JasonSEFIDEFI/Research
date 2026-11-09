# Constrained radial stability of a charged two-field scalar model

**Exploratory research note for author review — 9 November 2026**

**Status:** Exploratory / Not Promoted. AI-assisted derivation, computation and drafting. No independent review, journal submission, established novelty or derivation of observed matter is claimed.

## Abstract

A canonical two-complex-scalar model with an explicitly added Maxwell field was investigated for localized charged solutions and constrained radial stability. At a selected fixed classical charge number, stationary profiles were computed together with their electrostatic response. A technical audit identified an inconsistency between interpolated continuum profiles and the finite-difference Hamiltonian used for stability analysis. Solving the stationary equations directly on the same variational grid reduced normalized gauge/charge defects to approximately 10^-13 or smaller. The corrected constrained energy matrices were positive on the declared radial tests, and complete spectra on two finite grids contained no growing mode above the specified numerical threshold. These findings support a bounded finite-grid result. They do not establish nonlinear three-dimensional continuum stability, and the present spherical classical current does not provide the spin or magnetic response required for an electron identification.

## 1. Model and question

The calculation uses metric (+---) and the action density

\[
\mathcal L=\frac12|D_\mu\Phi|^2+\frac12|\partial_\mu\Sigma|^2
-V(|\Phi|^2,|\Sigma|^2)-\frac14F_{\mu\nu}F^{\mu\nu},
\qquad D_\mu=\partial_\mu+iqA_\mu,
\]
\[
V(\rho,\eta)=\frac{\rho^2}{4}+\frac\rho2+2\rho\eta
+\frac\lambda4\left(\eta-\frac3\lambda\right)^2.
\]

Phi is electrically charged; Sigma is neutral and has a nonzero vacuum amplitude. The Maxwell sector and coupling q are additional inputs to the earlier ungauged scalar model. Spatial dimension, locality, kinetic normalization and the potential are specified rather than emergent outputs.

The stationary ansatz is Phi=exp(-i omega t)f(r), Sigma=s(r), A0=a(r), Ai=0, with Omega=omega-qa and a(infinity)=0. The electric current follows from the half-normalized scalar kinetic term:

\[
j^\mu=-q\,\operatorname{Im}(\Phi^*D^\mu\Phi),\qquad
N=4\pi\int_0^\infty r^2\Omega f^2dr,\qquad Q_{\rm em}=qN.
\]

N is a continuous classical charge integral, not a derived integer occupation number. The audited candidate uses lambda=12, q=.0025 and N=1250.1753361265248; all numerical quantities before an explicitly stated unit calibration are dimensionless.

The question is whether the selected localized background has a constrained growing radial perturbation in the specified discretizations. It is narrower than proving that this configuration is an elementary particle.

## 2. Numerical consistency before stability

An interpolated solution of one numerical problem need not be a critical point of a different discrete Hamiltonian. The first implementation had nonzero discrete gauge-mode defects of order 10^-4 to 10^-5. Projecting out a charge/gauge pair did not make that interpolated background exactly stationary.

The corrective calculation solves the stationary field equations, Gauss constraint and fixed N directly on the variational radial grid. It uses F=r f, S=r(s-.5), A=r a and treats omega as an unknown. The electric boundary condition retains the exterior Coulomb field. Damped Newton iterations use an analytic sparse Jacobian; all reported backgrounds satisfy the declared residual, nontriviality, charge and nodelessness checks.

The full charged radial Cartesian amplitude/phase Hamiltonian is then linearized about these discrete critical points. The canonical charge density is n=y p_x-x p_y. Gauss elimination uses the unscreened Coulomb inverse in phase space; screened response appears only after constrained momentum minimization. The fixed-charge tangent and its global gauge orbit are removed together by symplectic reduction.

## 3. Corrected results

| Outer radius R | Grid spacing h | Stationary maximum residual | Normalized gauge/charge defect | Lowest constrained radial energy eigenvalue |
|---:|---:|---:|---:|---:|
| 60 | .4 | 2.38e-14 | 8.04e-16 | .0131610422 |
| 60 | .2 | 1.81e-12 | 1.81e-13 | .0131327405 |
| 80 | .1 | 1.49e-13 | 1.65e-14 | .0126890137 |

Complete physical quotient spectra were computed for the first two grids, with dimensions 892 and 1792. No eigenvalue had a positive real part exceeding 10^-6. The largest absolute real parts were 4.83e-15 and 2.61e-14, respectively. The largest grid was tested through its constrained energy eigenvalues rather than a complete spectral recomputation.

An independent implementation of the energy differentiation, performed by the same AI, compared an 18-variable symbolic canonical Hessian with the assembled blocks. Their maximum absolute difference was 8.89e-16. Prior package manifests verified, and the selected observable and Schur calculations reproduced exactly in an isolated directory on the same runtime. These are implementation and reproducibility checks, not independent peer review.

Positive constrained energy and a purely imaginary spectrum are related by finite-dimensional Hamiltonian structure. Their agreement should not be counted as two independent physical validations. Finite-volume, interpolation, grid and modeling errors also cannot be inferred from eigensolver residuals alone.

## 4. Interpretation and limits

The defensible result is a reproducible localized charged branch with corrected finite-grid constrained radial stability evidence. Earlier angular tests provide additional bounded evidence, but no certified continuum coercivity estimate, nonlinear infinite-volume stability theorem or complete fragmentation analysis has been supplied.

The mechanism belongs to established gauged Q-ball research. Two-field gauged models and spinning configurations already exist in the literature; this parameterized action and its neutral complex field must be compared explicitly before any novelty claim. [Loiko and Shnir, 2019](https://arxiv.org/abs/1906.01943v2).

Ordinary ungauged slope criteria cannot simply be imported as sufficient gauged stability criteria. This study instead makes the charge constraint and electric response explicit. [Panin and Smolyakov, 2017](https://arxiv.org/abs/1612.00737v3).

The static spherical ansatz has zero spatial current, classical angular momentum and magnetic dipole. The earlier conditional Dirac construction has not been derived from this scalar background. Fitting a mass scale or the gauge coupling supplies inputs; it does not create physical spin-half, a quantum current matrix element or a new calibrated prediction. Consequently, neither the electron/positron identification nor the proposed electron-positron duality-field interpretation is established by this result.

## 5. Research disposition and reproducibility

The internal technical milestone is complete at its declared scope: the numerical background inconsistency is corrected, the bounded tests pass, and the record is available for independent assessment. Step 8 as independent scientific review remains incomplete. Review of the bounded calculation may accept a useful numerical or negative result without accepting a derivation of matter.

The exact audited calculation is pinned at [Research commit 6bf404a86f7d6390174615590338f00f9035b521](https://github.com/JasonSEFIDEFI/Research/tree/6bf404a86f7d6390174615590338f00f9035b521/research/2026-11-09/technical-review). It includes protocols, source pins, scripts, numerical results, generated-spectrum hashes, the correction report, unresolved objections and a prepared reviewer brief. Python 3.14.7, NumPy 2.5.2, SciPy 1.18.1 and SymPy 1.14.0 were used. No reviewer has been contacted, and no endorsement, merge, formal promotion or journal submission is recorded.
