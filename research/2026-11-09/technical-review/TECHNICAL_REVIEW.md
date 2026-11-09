# Step 8 technical review, correction and verdict

**9 November 2026 — Exploratory / Not Promoted.**

This is an AI self-audit of the pinned research record at `9e3bdeca7c48ed14922e7aee77f1b75b27945d53`, using fresh numerical critical points and a separately implemented symbolic Hessian. It is not independent external peer review. No reviewer has been contacted, and no reviewer approval is represented.

## Verdict

The declared internal algebra, reproducibility and corrected finite-grid radial tests pass. A substantive numerical construction issue was identified and corrected: the old interpolated background was not an exact critical point of the discrete Hamiltonian being analyzed. The corrected same-grid calculation preserves charge/gauge identities and retains positive constrained energy and absence of a computed growing radial mode.

**Step 8 as independent scientific review is not complete or passed.** Full continuum nonlinear three-dimensional stability, global fragmentation resistance and the physical spin/current bridge remain unestablished; direct classical electron identification remains failed. The bounded numerical research record can be reviewed on its own merits, including negative findings, without asserting those physical goals succeeded.

## 1. Major finding and correction: the background must match the operator

The earlier radial code interpolated a continuum boundary-value solution onto a finite-difference grid, then projected out a charge/gauge pair. The interpolated profile's discrete gauge-null residual ranged from about 1.7e-4 to 1.2e-5. The record exposed those values, but projection of an approximately stationary matrix is not exactly the linearization about a discrete critical point. Symplectic projection alone does not repair a nonstationary background.

The corrected code solves the stationary equations and fixed charge on the exact variational grid used by the Hamiltonian. Define interior radial variables F=r f, S=r(s-.5), A=r a. Let D be the centered Dirichlet radial operator for F and S, and De its Coulomb/Neumann counterpart for A. With Omega=omega-qA/r, solve

\[
DF+(1+f^2+4s^2-\Omega^2)F=0,
\]
\[
DS+(4f^2+12s^2-3)(S+r/2)=0,
\]
\[
D_e A-q\Omega F^2/r=0,
\qquad 4\pi h\sum_i\Omega_i F_i^2=N.
\]

The Coulomb boundary condition makes A constant in the source-free exterior. The neutral deviation S and charged F vanish at the outer endpoint. An analytic sparse Jacobian and damped Newton steps solve for F,S,A and omega together. The action, potential, q=.0025 and N=1250.1753361265248 have not changed.

For this variational radial representation the total energy, including the exterior electric tail, is

\[
E_h=4\pi h\left\{\tfrac12(F^TDF+S^TDS+A^TD_eA)
+\sum_i[r_i^2V(f_i^2,s_i^2)+\tfrac12\Omega_i^2F_i^2]\right\}.
\]

The electric boundary term from changing a to A cancels its exterior tail, yielding the displayed De quadratic form. Discrete integrated charge equals Coulomb flux 4 pi A_last to the reported residual.

| R | h | stationary max residual | normalized gauge/charge defect | smallest physical constrained-energy eigenvalue | maximum absolute real part, complete radial spectrum |
|---:|---:|---:|---:|---:|---:|
| 60 | .4 | 2.38e-14 | 8.04e-16 | .0131610422 | 4.83e-15 |
| 60 | .2 | 1.81e-12 | 1.81e-13 | .0131327405 | 2.61e-14 |
| 80 | .1 | 1.49e-13 | 1.65e-14 | .0126890137 | not recomputed: energy test only |

The complete spectra contain 892 and 1792 physical phase-space eigenvalues. Neither has real growth above 1e-6. Energy eigenpair residuals are below 4.3e-13, and the matrices' maximum symmetry error is below 1e-20. All profiles are nontrivial and nodeless under the stated cutoff. Gauss flux errors are below 2.6e-13 relative. The two radial frequencies at the bottom of the nonzero spectrum are .0141666623 and .0141390288; their shifts explicitly show finite-grid effects.

The finest new energy is 1767.7501381947 versus continuum-BVP reference 1767.7523605159; their difference is .00222232. The new charge RMS radius is 7.2111937539 versus 7.2118133097. These differences are not errors in the continuum BVP merely because its own solver tolerance is small: they are errors of a separate second-order discretization. Energy differences from the BVP reference decrease approximately by four when h halves, with the last comparison also enlarging R. No rigorous continuum error bound follows from that observation.

This corrects and supersedes the earlier **interpolated-background spectral evidence** for the finite-grid radial claim. Earlier files and numbers remain available as the historical record. It does not alter the existing explicit limits on continuum or physical interpretation.

## 2. Separate Hamiltonian differentiation check

`independent_hessian.py` starts from the Cartesian canonical energy instead of copying the assembled stability blocks. It includes the quartic potential, canonical kinetic/gradient terms, charge density n=y p_x-x p_y, its Coulomb energy and the rotating term -omega N. SymPy differentiates the resulting 18-variable, three-node Hamiltonian twice; the test background satisfies the discrete electric constraint but need not solve the scalar equations for this Hessian identity.

The differentiated and assembled Hessians differ by at most **8.89e-16** absolute, passing the 1e-10 criterion. This checks current sign, cross blocks and Coulomb terms by a separate implementation. It is not independence of reviewer or of physical assumptions. The prior independently formulated static Schur identity also regenerates successfully.

## 3. Reproducibility and evidence accounting

Both normalized archive manifests verify: 18 files in the fixed-charge package and 15 in the closure package. The archive is extracted to a fresh directory with path containment checked. The Schur and observable scripts are rerun from that saved package. Mass-scale, radius, charge-ratio and energy-radius outputs reproduce exactly on the same runtime. This is isolated-directory same-environment reproducibility, not cross-platform replication or outside validation.

The complete new spectrum CSVs, source/results manifests and exact commands are preserved in the downloadable review packet. The public scripts regenerate those CSVs, with normalized text hashes recorded in JSON. No partial results from interrupted iterative solvers are used.

Purely imaginary eigenvalues and a positive Hamiltonian Hessian are **not two independent physical validations**: positivity implies that spectral property in a finite Hamiltonian system. Their agreement checks implementation consistency. It is evidence about the specified finite matrices, not evidence that nature realizes this action.

## 4. Literature and novelty check

The charged-soliton mechanism belongs to established non-topological soliton research. [Friedberg, Lee and Sirlin (1976)](https://doi.org/10.1103/PhysRevD.13.2739) studied scalar solitons with a conserved charge and a neutral scalar. [Loiko and Shnir (2019)](https://arxiv.org/html/1906.01943v2), equations 1–2, study a gauged charged complex scalar coupled to a neutral real scalar with a symmetry-breaking potential; they also construct spinning solutions. Our model has additional charged self-interaction and bare quadratic terms, and a neutral **complex** field with a massless phase. These differences prevent calling the actions identical without a mapping; they do not establish novelty or an advantage.

Nonzero classical magnetic moments are possible in other, spinning scalar-soliton ansatzes. Thus zero dipole is an obstruction for the present static spherical configuration/current, not a general no-go theorem for every scalar soliton. The cited spinning model uses integer azimuthal winding and reports J=nQ in its conventions. It does not supply the missing physical spin-half map for this model.

[Panin and Smolyakov (2017)](https://arxiv.org/abs/1612.00737v3) explain why the ordinary ungauged slope criterion does not apply generally to gauged Q-balls. [Kinach and Choptuik (2024/2025)](https://arxiv.org/abs/2408.07561v2) provide fully three-dimensional simulations in other potentials. Neither result establishes stability of our action. An exhaustive novelty search and matched conventional-model comparison remain pending.

## 5. Physical interpretation audit

The [NIST 2022 CODATA table](https://physics.nist.gov/cuu/Constants/Table/allascii.txt) continues to support the measured constants used in the preceding conditional comparison. The physical mass scale and optional q fit remain inputs, not predictions. The static spherical model has zero spatial current, magnetic dipole and classical angular momentum. A direct identification of that current with the electron's nonzero magnetic response fails. The review does not transfer a Dirac moment from the separate conditional spinor construction.

No quantum current matrix element, physical spin-half selection, fermionic state space or new calibrated prediction has been derived. Those are missing theory, not numerical tolerances a finer grid can fix. The prior worldline energy and internal-sector obstructions also remain separate and unresolved.

## 6. Review disposition

**Closed internally:** package integrity; canonical Hessian algebra; same-environment observable reproduction; same-grid radial stationarity, gauge identity, fixed-charge reduction and bounded finite-grid non-growth evidence. The numerical background issue is corrected, and the corrected radial evidence passes its predeclared tolerances.

**Open scientific obligations:** continuum coercivity and nonlinear 3D/fragmentation analysis; a physical spin/current construction; calibrated predictions and adequate observation mapping; exhaustive novelty/baseline assessment.

**Open review obligation:** independent technical assessment by a reviewer who did not generate this record. A second implementation run by the same AI cannot satisfy that requirement. The supplied reviewer brief makes that assessment concrete, but no external endorsement or formal promotion is claimed.

The appropriate claim ready for independent review is: *a reproducible exploratory scalar-Maxwell branch and constrained finite-grid stability calculation, with a correction to the background construction and an explicit failure of direct electron identification*. The claim *SEFI has derived stable electron/positron matter* is not supported.
