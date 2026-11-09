# Constrained radial Hamiltonian and the remaining continuum gap

**Exploratory / Not Promoted. AI-assisted.** This extends the preceding static assessment to charged amplitude and phase dynamics on the same bound q=.0025 background. It supplies an explicit operator for independent checking, not a nonlinear three-dimensional stability theorem.

## Variables and charge

Work in radial Coulomb gauge with no transverse radial Maxwell degree of freedom. Write the charged field in its rotating frame as Phi=exp(-i omega t)(f+u+i v). Its rotated canonical momenta have background (0,-Omega f), where Omega=omega-qa. Let (p_u,p_v) denote momentum perturbations and z,p_z the neutral real-amplitude pair. The positive charge number density is n=y p_x-x p_y, so

\[
\delta n=f(\Omega u-p_v),\qquad
\delta N=\int f(\Omega u-p_v)d^3x.
\]

Eliminate the electric constraint with G=(-Delta)^(-1) on regular radial sources, including the exterior Coulomb tail. The quadratic rotating Hamiltonian K=H-omega N is

\[
K_2=\tfrac12\int[p_u^2+p_v^2+p_z^2
+u A u+v B v+z C z+16fsuz
+2\Omega u p_v-2\Omega v p_u]d^3x
+\tfrac{q^2}{2}\langle\delta n,G\delta n\rangle,
\]
\[
A=-\Delta+1+3f^2+4s^2,\quad
B=-\Delta+1+f^2+4s^2,\quad
C=-\Delta-3+4f^2+36s^2.
\]

The cross term 16fsuz inside the one-half integral is equivalent to Hessian block 8fs. G here is the **unscreened** Coulomb inverse, since the canonical charge density is an independent phase-space variable. Minimizing over that momentum recovers the screened operator from the earlier static calculation. Substituting a screened G directly into this Hamiltonian would double-count the response.

With Z=(u,v,z,p_u,p_v,p_z), let L be the symmetric Hessian of K2 and J the canonical symplectic matrix. The complete charged radial/neutral-real linearization is Zdot=JLZ. No amplitude eigenvalue is relabeled as a squared dynamical frequency.

The radial code uses U=r u, V=r v, Zr=r z and equally transformed momenta. The constant factor 4 pi in the symplectic form cancels that in the energy. It retains the finite-grid Coulomb boundary condition on r delta a and reports the background's discrete gauge-mode defect rather than claiming exact stationarity of an interpolated continuum profile on every grid.

## Remove the constraint and its gauge orbit together

Let c be the Euclidean gradient of delta N after radial discretization and g=Jc. Normalize c and g; they are orthogonal. The tangent constraint is c^T Z=0 and g is its global gauge direction. The projector P=I-cc^T-gg^T commutes with J, hence its range is symplectic. Using an orthonormal basis Q for this range gives

\[
L_{\rm red}=Q^T L Q,\quad J_{\rm red}=Q^T J Q,\quad
\dot z=J_{\rm red}L_{\rm red}z.
\]

This removes both the charge-changing direction and the unphysical global phase zero mode. It does not freeze local phases. The code checks Jred^2=-I, symmetry, eigenpair residuals, and the complete eigenvalue spectrum on the two declared coarse grids. A direct symmetric solve replaces an interrupted slow unshifted iterative attempt; no partial iterative spectrum is used.

For any finite matrix with Lred positive definite, Jred Lred is similar to the antisymmetric matrix Lred^(1/2) Jred Lred^(1/2). Its eigenvalues are purely imaginary and its quadratic energy is conserved. This establishes a finite-dimensional sufficient test; it does not by itself prove continuum coercivity or nonlinear stability. The reference JSON records the observed finite-grid positivity and spectrum rather than asserting the theorem's continuum hypotheses.

The complete computed radial spectra contain 892 and 1792 physical phase-space eigenvalues at R=60,h=.4 and .2. Neither has a growing eigenvalue above 1e-6; the largest absolute real parts are 3.84e-15 and 1.80e-14. Their smallest nonzero frequencies are .0141275420 and .0141292384. The reduced energy minima are .0131181893 and .0131220066. At R=80,h=.1 the reduced energy minimum is .0126866426, with eigenpair residuals below 3.9e-13. The positive neutral-phase squared-frequency minima decrease from about .002763 at R=60 to .001547 at R=80, consistent with a gapless infinite-volume channel.

The unreduced discrete gauge-mode residual is 1.68e-4 on R60,h=.4, 1.12e-4 on R60,h=.2 and 1.22e-5 on R80,h=.1. Boundary and interpolation errors affect this diagnostic, so it is not claimed to scale purely with h squared between different domains. The symplectic constraint reduction is exact for the finite projected matrices; its interpretation as the continuum quotient still requires the stated convergence assumptions. Raw spectra are generated as CSV files with normalized text hashes, supplied in the downloadable packet, and reproducible from the code.

On this same q=.0025 background the smallest static radial amplitude values are .0378291661, .0378308361 and .0378312521 at R80,h=.2,.1,.05. Ell=1 shifts are -5.8212e-5,-1.4541e-5,-3.6364e-6, approaching the translation zero at the expected second-order rate. The h=.05 ell=2 and ell=3 values are .0415358882 and .0439839888. The finite-grid local angular bound is below 7.504, while ell(ell+1)>=12 for ell>=3; this excludes higher-ell negative amplitude directions for those discrete quadratic forms. It is not a certified bound between grid points. The independent Coulomb/static Schur identity agrees to 2.00e-15 absolute in its reference test.

## Independent cross-check against the previous static Hessian

In transformed radial variables define D=q^2 M_f G M_f, Pmom=I+D and Bmom=M_Omega(I-D). Eliminating p_v subject to d^T p_v=e^T U, with d=r f and e=r f Omega, gives the amplitude Schur complement

\[
H_{UU}-B_{\rm mom}P_{\rm mom}^{-1}B_{\rm mom}^T
+\frac{|e+B_{\rm mom}P_{\rm mom}^{-1}d\rangle
\langle e+B_{\rm mom}P_{\rm mom}^{-1}d|}{d^T P_{\rm mom}^{-1}d}.
\]

Using (I+D)^(-1) and the resolvent identity yields exactly

\[
-\Delta+V_{ff}-\Omega^2
+4q^2M_{f\Omega}(-\Delta+q^2f^2)^{-1}M_{f\Omega}
+\frac{4\omega^2}{C[f]}|fu^2\rangle\langle fu^2|,
\]

where u in this last formula is the previously defined screening function, not the Cartesian amplitude perturbation. The notation overlap is confined to this comparison; the code calls the screening function `u` only in its independent Schur test. `check_schur.py` evaluates both reductions independently on a finite radial matrix with a nontrivial test profile.

## Other sectors and what the tests cannot establish

The neutral imaginary field eta decouples linearly and obeys eta_tt=-(-Delta+4f^2+12s^2-3)eta. Since the positive background s solves this operator's zero equation, its continuum quadratic form equals integral s^2 |grad(eta/s)|^2 for compactly supported eta. This excludes a negative direction in that stated class; the infinite-volume vacuum spectrum is gapless. Its finite-box low eigenvalues are reported separately.

For general three-dimensional perturbations, the exact fixed-N energy can be minimized over charge density and the longitudinal electric field at given amplitudes. The remaining spatial phase, magnetic and transverse kinetic terms are nonnegative. Consequently positivity of the complete reduced amplitude Hessian, modulo translations and gauge, would supply an energy-based sufficient linear stability route. The angular matrices on the actual bound candidate test the low harmonics and the discrete high-ell bound; they are not a certified continuum bound. The ell=1 translation shifts are retained and studied under refinement.

A nonlinear infinite-volume conclusion still requires an admissible function space, well-posed constrained evolution, coercivity modulo symmetries, and control of the massless channel. No simulation of finite duration would establish all of that. Global fragmentation requires comparison with all allowed daughter states and diffuse radiation. Those proofs/comparisons have not been supplied; the checkpoint must leave them unresolved.
