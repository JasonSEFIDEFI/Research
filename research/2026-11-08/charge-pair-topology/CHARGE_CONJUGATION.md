# SEFI charge conjugation and the electron positron question

Jason Duran Dutton research checkpoint  
November 8, 2026  
Exploratory mathematical analysis with Codex assistance

## Result

The existing canonical two-complex-scalar model has an exact equal-energy, opposite-global-charge pairing. This holds for its full classical equations and for any stationary localized solution within the stated ansatz. The numerical branch previously computed therefore has a conjugate branch without changing its couplings or fitting a new profile.

This pairing is not sufficient to identify the branches as electrons and positrons. The present spherical solutions have zero classical angular momentum; linearized elementary excitations are scalar modes; the action has a global phase symmetry but no electromagnetic gauge field. No emergent spin-half quantization or fermionic exchange law has been constructed.

These identities are standard consequences of this action. Their application here clarifies the model; it is not a claim of novelty, completed physical-matter derivation or experimental validation.

## Starting action and scope

Use the previously specified canonical normalization, metric signature (+---), dimensionless fields and spacetime coordinates:

\[
\mathcal L=\frac12\partial_\mu\Phi^*\partial^\mu\Phi
+\frac12\partial_\mu\Sigma^*\partial^\mu\Sigma-V,
\]

\[
V=\frac{\rho^2}{4}+\frac\rho2+2\rho\eta
+\frac\lambda4\left(\eta-\frac3\lambda\right)^2,
\qquad \rho=|\Phi|^2,\quad\eta=|\Sigma|^2,\quad\lambda>0.
\]

This is the canonical localized-field model already studied in the stationary branch records. It is not the unrestricted higher-derivative worldline action addressed by the earlier Hamiltonian audit. Minkowski geometry, field content and couplings are inputs here.

The equations are

\[
\Box\Phi+(1+|\Phi|^2+4|\Sigma|^2)\Phi=0,
\]
\[
\Box\Sigma+(4|\Phi|^2+\lambda|\Sigma|^2-3)\Sigma=0.
\]

The potential is nonnegative in its original variables. With the prescribed vacuum and finite-energy boundary conditions, canonical energy is nonnegative. This does not by itself prove a localized minimum or nonlinear stability.

## Exact opposite charge pairing

The transformation C maps both fields and their momenta to their complex conjugates:

\[
C:(\Phi,\Sigma,\dot\Phi,\dot\Sigma)
\longmapsto(\Phi^*,\Sigma^*,\dot\Phi^*,\dot\Sigma^*).
\]

Every coefficient in the field equations is real and depends only on moduli. Conjugating either equation therefore yields the corresponding equation for the transformed field. For a fixed real asymptotic Sigma phase, C preserves the boundary condition. Other constant vacuum phases are related by the model's global symmetry.

Define the two independent global phase currents by

\[
j_\Phi^\mu=\operatorname{Im}(\Phi^*\partial^\mu\Phi),
\qquad j_\Sigma^\mu=\operatorname{Im}(\Sigma^*\partial^\mu\Sigma).
\]

Their integrals reverse under C. Canonical energy and stress energy are invariant:

\[
(E,Q_\Phi,Q_\Sigma,P)\longmapsto
(E,-Q_\Phi,-Q_\Sigma,P).
\]

For the real-profile stationary class,

\[
\Phi=e^{i\omega t}f(r),\qquad \Sigma=s(r),
\]

\[
Q_\Phi=\omega I,\qquad
I=4\pi\int_0^\infty r^2 f(r)^2\,dr.
\]

The profile equations depend on omega squared. Replacing omega by minus omega preserves the same f and s and the same energy, while reversing Q. Equivalently, the fixed-charge kinetic contribution is Q squared divided by 2I and is charge-even. For any existing stationary profile, this supplies an exact conjugate partner. It does not require another numerical branch solve and does not prove the existence of profiles beyond those already established.

In the selected numerical lambda=12 branch, the previously reported minimum near |Q|=953.31 and free-threshold binding crossing near |Q|=1225.43 therefore occur symmetrically at both signs. Those values remain dimensionless numerical results with the original branch and stability qualifications. They are not multiples of measured electron charge without an additional physical normalization.

## Vacuum spectrum calculated from the same potential

Choose a vacuum representative

\[
\Phi=0,\qquad \Sigma=v=\sqrt{3/\lambda}.
\]

Write Phi=x+iy and Sigma=v+h+ia. Canonical real-component kinetic normalization gives the exact potential Hessian at the vacuum:

\[
\operatorname{Hess}V\big|_{\rm vac}
=\operatorname{diag}\left(1+\frac{12}{\lambda},
1+\frac{12}{\lambda},6,0\right).
\]

Thus at lambda=12 the two real Phi components have mass squared 2, the Sigma radial mode has mass squared 6, and its phase mode is massless. This is a small-fluctuation calculation, not a proof of soliton stability. The massless mode is a scalar phase excitation, not a photon derived from the action.

Ordinary perturbative quantization of complex scalar modes supplies particle and antiparticle excitations with spin zero. A nonperturbative fermionic soliton is a separate possibility in suitable theories, but it requires a demonstrated configuration-space and quantization mechanism; it does not follow from naming two real components or two charge signs. No such construction is supplied by the current spherical branch.

## Angular momentum and phase quantization

The spherical real-profile ansatz has no angular dependence. Its classical angular momentum is zero.

For comparison, consider a scalar winding ansatz Phi=f(r,theta) exp[i(omega t+n phi)] with static, real Sigma. Single-valued scalar fields require integer n. With angular generator convention

\[
J_z=\int\operatorname{Re}(\dot\Phi^*\partial_\varphi\Phi)\,d^3x,
\]

one obtains J_z=n Q_Phi. Reversing the rotation convention reverses the overall sign, not the integer-winding restriction. This relation is not itself a derivation of quantum spin: orbital angular momentum and intrinsic spin must be distinguished.

A restricted global-phase collective coordinate alpha has kinetic term I dot(alpha) squared divided by 2 at fixed profiles and conjugate momentum p_alpha=I dot(alpha)=Q. If one additionally quantizes an ordinary periodic rotor with single-valued wavefunctions, its momentum is k hbar with integer k. This is an added quantum prescription, not a derived electromagnetic charge unit. It also does not produce a spinor sector: the scalar fields return to themselves under a 2 pi spatial rotation, and the n=0 spherical configuration is rotation-invariant.

The current branch therefore supplies neither a half-integer rotational representation nor a fermionic exchange law. This is a limit of this construction, not a theorem forbidding emergent fermions in every scalar or topological theory.

## Electromagnetic coupling cannot be assumed from global charge

There is no A_mu or Maxwell term in the starting action. Its Noether charge is consequently not already an observed electric charge, and a Coulomb field has not been derived.

A possible extension would introduce a Maxwell term and covariant derivatives. This changes the model and would need a separate justification and new stationary solutions satisfying Gauss law.

One immediate consistency condition can be derived before performing that extension. Suppose a single proposed U(1) acts on Sigma with charge q_Sigma and coupling g. Around Sigma=v, its kinetic term contains

\[
\frac12g^2q_\Sigma^2v^2 A_\mu A^\mu.
\]

The vector mass squared would be g squared q_Sigma squared v squared. A single massless electromagnetic gauge field therefore requires q_Sigma=0 in this vacuum, unless additional fields or gauge generators provide a different unbroken combination. Gauging the diagonal phase symmetry with charged Sigma would instead give a massive vector. Gauging only Phi avoids this particular vacuum mass, but leaves the Sigma phase mode and introduces an electric coupling by assumption.

This gives a concrete constraint on any electromagnetic bridge. It does not select a unique bridge or derive the coupling, electron mass, spin or statistics. An electrostatic field also adds energy and back-reaction, so the ungauged soliton profiles cannot simply be relabeled as gauged solutions.

## Rotation loop test in an explicitly stated configuration space

There is a further analytic test available without modifying the action. Fix the vacuum phase and consider the regular finite-energy class

\[
\mathcal X=\{(\Phi,\Sigma):\Phi\in H^1(\mathbb R^3;\mathbb C),\ \Sigma-v\in H^1(\mathbb R^3;\mathbb C)\}.
\]

The localized stationary profiles with their decaying tails belong to this class. It is an affine Hilbert space. The polynomial potential has degree at most four in Phi and Sigma-v, with no nonzero vacuum constant or linear term. Sobolev embedding into L^p for 2<=p<=6 and Holder inequalities make its quadratic, cubic and quartic terms integrable. Thus every configuration in this class has finite static energy.

For any continuous spatial rotation loop R_t with R_0=R_1 equal to the identity, write u_t=(Phi_t,Sigma_t-v), with u_0=u_1=u_base. The explicit based homotopy

\[
H(s,t)=u_{\rm base}+(1-s)(u_t-u_{\rm base}),\qquad 0\leq s,t\leq1,
\]

stays in H^1, preserves the fixed asymptotic vacuum and has finite static energy throughout. It contracts the loop to the constant configuration while keeping its basepoint fixed. The same affine contraction applies to every loop in this class. Consequently pi_1(X)=0: a nontrivial rotation-loop sign cannot be obtained by the usual nontrivial-cover construction on this particular full configuration space.

This is a statement about the specified bosonic configuration space. It is not a classification of every finite-energy infrared tail, gauge quotient, separately constrained fixed-charge phase space, adiabatically restricted moduli space, or possible SEFI extension. A contraction can pass through field zeros and configurations outside the stationary family; the original action permits those configurations. Excluding them would require a justified physical or mathematical restriction. A winding seen in one ansatz is not sufficient to remove the contraction in the full space.

This narrows the next step: the current canonical H^1 field space supplies neither a spinor transformation law nor the nontrivial rotation-loop topology needed for that particular route to fermionic soliton quantization. Any alternative mechanism must be exhibited explicitly.

## Checks performed for this checkpoint

The accompanying Python script checks the potential symmetry, charge reversal, momentum-density invariance, vacuum Hessian, omega-even stationary functional, charge-even fixed-Q energy, scalar 2 pi rotation and winding identity with exact SymPy expressions.

A separate 1024-point periodic one-dimensional sample checks energy, two phase charges and momentum before and after conjugation. All four transformation errors were zero at the recorded floating-point precision. This is an independent sampled consistency check, not a localized particle solution, a PDE evolution or a stability test.

Environment: Python 3.14, SymPy 1.14.0, NumPy 2.5.2. The JSON records the numerical package versions and sampling seed; the reproduction instructions specify Python. Substantive derivation, coding and drafting assistance was provided by Codex; author verification and independent technical review remain outstanding.

## Next decisive work

A continuation in [FIXED_CHARGE_TOPOLOGY.md](FIXED_CHARGE_TOPOLOGY.md) separately treats a stated regular fixed-charge phase space and its global phase quotient.

The immediate structural gap is the spin and statistics construction. More precision on a scalar radial profile cannot by itself resolve it. The explicit H^1 rotation-loop calculation above closes one simple proposed route. The next question is whether a different, physically justified configuration space or quantization mechanism follows from the underlying SEFI formulation. That needs its own boundary conditions, rotation and exchange analysis, and a justified quantization rule. A proposed spinor extension would have to be labeled an added assumption rather than a derived result.

In parallel, any electromagnetic interpretation needs an explicit unbroken gauge generator, field equations, Gauss constraint, coupling normalization and self-consistent finite-energy charged solutions. Matching observed electron properties would then require spin-half fermionic behavior, opposite equal charges, common mass and quantitative interaction predictions. Neither introducing a Dirac field by assumption nor choosing scales to fit electron mass would establish that these properties emerged from SEFI.

The justified description at this checkpoint is **an equal-energy opposite-global-charge pairing in the existing scalar model**. “Electron positron duality field” remains a proposed interpretation to test, not a result established here.

## Sources

1. [Existing canonical action and stationary branch draft](https://github.com/JasonSEFIDEFI/SEFI-PY/blob/18a5275df36d32af1b67d514c0c337637ff2c210/research/2026-10-25/critical-correction/MANUSCRIPT_DRAFT.md), section 2.
2. [Physical vacuum and potential audit](https://github.com/JasonSEFIDEFI/SEFI-PY/blob/847a071351ed2b1c54e240fd9a520a1cce238178/research/2026-10-19/vortex-extended/PHYSICAL_BACKGROUND.md).
3. [Frequency continuation and charge thresholds](https://github.com/JasonSEFIDEFI/SEFI-PY/blob/446e6177ec30b840a0fcd336ff72dd96a1c2df4e/research/2026-10-25/localized-frequency/README.md).
4. David Tong, [Free fields](https://www.damtp.cam.ac.uk/user/tong/qft/qfthtml/S2.html), complex scalar quantization; [Quantizing the Dirac field](https://www.damtp.cam.ac.uk/user/tong/qft/qfthtml/S5.html), spin and particle antiparticle structure. Search excerpts were accessible during this review; direct page/PDF fetches timed out. These support the standard QFT comparison, not a new SEFI derivation.
