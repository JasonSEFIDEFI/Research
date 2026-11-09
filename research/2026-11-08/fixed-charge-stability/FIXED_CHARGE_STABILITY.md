# Step 6: fixed-charge continuation and constrained energy tests

**Exploratory / Not Promoted. AI-assisted derivation, code and prose. Dimensionless scalar-Maxwell extension only; no independent review or electron identification.**

## Result and scope

Holding the continuous charge number N=1250.1753361265248 fixed reverses the misleading impression one could get from comparing the preceding fixed-frequency rows: adding electric coupling raises the total energy. The branch loses its energetic advantage over dispersed free charged scalars near q=0.00601012. Nevertheless, the static radial real-amplitude Hessian tested here has no negative eigenvalue at q=0 or .01. These statements are compatible: an energetically disfavored localized state can have a local energy barrier.

This is progress within step 6, not completion of full three-dimensional dynamical stability. The tests below examine explicitly defined energy restrictions. They do not compute physical growth rates or the full coupled gauge/scalar evolution spectrum.

## 1. Fixed charge boundary-value problem

Keep the preceding half-normalized scalar-Maxwell action, lambda=12, Phi=exp(-i omega t)f, Sigma=s real, A0=a and Omega=omega-qa. The radial equations remain

\[
f''+2f'/r=(1+f^2+4s^2-\Omega^2)f,\quad
s''+2s'/r=(4f^2+12s^2-3)s,
\]
\[
a''+2a'/r=-q\Omega f^2.
\]

Add c'=4 pi r^2 Omega f^2, c(0)=0, c(R)=N, and solve for omega as an additional unknown. Regular origin conditions and outer f(R)=0, s(R)=.5, a'(R)+a(R)/R=0 are retained. Include the exterior Coulomb energy. This holds Qem=qN fixed during any perturbation at a specified q. Between rows q changes, so it is N, not the numerical electric charge, that is held equal. N is a continuous classical integral, not a derived integer particle count or the internal identity-oscillator occupation.

| q | omega | E | mPhi N - E |
|---:|---:|---:|---:|
| 0 | 1.4012230845 | 1767.6973305 | +0.3175852 |
| .0025 | 1.4013130340 | 1767.7523605 | +0.2625552 |
| .005 | 1.4015829129 | 1767.9172524 | +0.0976633 |
| .01 | 1.4026630631 | 1768.5737539 | -0.5588381 |
| .015 | 1.4044673541 | 1769.6562002 | -1.6412845 |
| .02 | 1.4070123697 | 1771.1432101 | -3.1282943 |

Here mPhi=sqrt(2). All six rows are nontrivial nodeless accepted solutions. At q=.03 the solver exceeds its mesh limit, has order-one equation residual, a radial node, and fails both charge and flux checks; it is rejected. Subsequent planned .04 and .05 points are not attempted. This failure is not a maximum-coupling theorem. In particular, the accepted fixed-N q=.02 solution demonstrates why the previous fixed-frequency q=.02 vacuum solve was not evidence of universal nonexistence.

The q=.01 replication at R=160 and tolerance 2e-8 changes E by 5.44e-11 relative and omega by 3.71e-11 relative. These are observed changes between numerical solves, not rigorous error bounds. The initial scan uses R=120 and tolerance 1e-7. All attempts, including the failed .03 row, remain in `fixed_charge_results.json`.

An adaptive follow-up to the observed binding-margin sign change locates the root at q=0.00601011855. At R=160/tolerance 2e-8 its residual energy margin is approximately 2.46e-8. This is an equality with the free-scalar dispersion threshold, not a dynamical stability boundary, charge quantization, or a prediction for the observed elementary charge. At fixed total charge the electric energy of a sufficiently spread distribution tends to zero; thus the free threshold is a relevant dispersal comparison. Being above it does not prove a linear growing mode or a decay timescale.

## 2. Eliminate Gauss' law before testing the energy

For a fixed real amplitude f define

\[
L_f=-\nabla^2+q^2f^2,\qquad
u=1-q^2L_f^{-1}f^2,\qquad u(\infty)=1,
\quad C[f]=\int f^2u\,d^3x.
\]

Then a=(omega/q)(1-u), interpreted continuously at q=0, Omega=omega u and N=omega C. The electric field and charged phase momentum minimize their positive quadratic energy subject to Gauss' law and total N. One can derive this by minimizing integral (n^2/f^2+|E|^2)/2 with div E=qn and integral n=N: its Euler equations give n=f^2(omega-qa) and E=-grad a. Their energy equals omega N/2, including the exterior field. The reduced static functional is therefore

\[
\mathcal E_N[f,s]=\tfrac12\int(|\nabla f|^2+|\nabla s|^2)d^3x
+\int V(f^2,s^2)d^3x+\frac{N^2}{2C[f]}.
\]

This is a constrained static energy reduction in the real, zero-spatial-current class, not a replacement for all dynamical perturbation equations. The boundary condition on L inverse is decay of 1-u. It is not a finite-box Dirichlet zero potential.

For a real amplitude variation h, self-adjointness gives

\[
\delta C=2\int f u^2h,\quad
\delta^2 C=2\int u^2h^2-8q^2\langle fuh,L_f^{-1}fuh\rangle.
\]

Consequently

\[
\delta^2\frac{N^2}{2C}
=\frac{\omega^2}{C}(\delta C)^2-\frac{\omega^2}{2}\delta^2C.
\]

Freezing a, or using only a local negative Omega^2 contribution, omits necessary terms. The code checks the first and second C variations and the reduced electric/time energy second variation against independent finite differences. The best second-variation relative agreement is better than 3e-8 for the tested smooth direction on every declared radial grid. This is a directional implementation check, not a proof for all variations.

## 3. The real-amplitude Hessian

With inner product integral over d^3x, write h=delta f, k=delta s. The Hessian has blocks

\[
H_{ff}=-\nabla^2+1+3f^2+4s^2-\Omega^2
+4q^2 M_{f\Omega}L_f^{-1}M_{f\Omega}
+\frac{4\omega^2}{C}|fu^2\rangle\langle fu^2|,
\]
\[
H_{ss}=-\nabla^2-3+4f^2+36s^2,\qquad H_{fs}=H_{sf}=8fs.
\]

The rank-one term enforces fixed N and is positive; the electrostatic response term is also positive. In spherical harmonics ell>0 the first charge variation integrates to zero, so the rank-one term vanishes, while L inverse is taken in that same angular sector. The local Laplacian gains ell(ell+1)/r^2.

For ell=0, set xi=r h and zeta=r k, with zero perturbations at 0 and R. A centered second-order radial matrix is used with the exterior Coulomb response retained. The tabulated values are eigenvalues of this static Hessian in the L2 amplitude norm, **not squared dynamical frequencies**.

| q | R | h | lowest restricted radial eigenvalue |
|---:|---:|---:|---:|
| 0 | 80 | .2 | .0380356570 |
| 0 | 80 | .1 | .0380373373 |
| 0 | 80 | .05 | .0380377559 |
| 0 | 120 | .1 | .0372223219 |
| .01 | 80 | .2 | .0347132729 |
| .01 | 80 | .1 | .0347148112 |
| .01 | 80 | .05 | .0347151944 |
| .01 | 120 | .1 | .0337003742 |

The first four eigenpairs are retained; their Euclidean matrix residuals are below 8e-12. Mesh refinement is consistent with a second-order scheme. Domain changes move the low finite-box modes, so no infinite-volume eigenvalue with all the displayed digits is claimed. The asymptotic charged-amplitude threshold is 2-omega^2, about .03657 at q=0 and .03254 at q=.01, consistent with low box modes approaching continuum. The sampled positive minima supply evidence against a negative direction in this restricted radial test, not a certified continuum spectral bound.

## 4. Interpretation and unresolved stability tasks

The static angular follow-up is recorded separately in `angular_hessian_results.json`. It is an adaptive extension of the preregistered radial calculation. Translation symmetry predicts an ell=1 zero direction in infinite volume; small discretization shifts in that channel must be checked under refinement before calling them physical negative modes.

At R=80 the lowest ell=1 eigenvalues for q=.01 are -5.5781e-5, -1.3934e-5 and -3.4846e-6 on h=.2,.1,.05. They decrease in magnitude by approximately four with each halving, consistent with the expected translation zero mode. The q=0 sequence behaves the same way. The next three computed eigenvalues in this channel remain positive; the raw results retain all four. No finite negative continuum eigenvalue is identified by this sequence, and no rigorous exclusion follows solely from extrapolation.

The lowest ell=2 values at h=.05 are .0417522392 for q=0 and .0382839839 for q=.01; ell=3 gives .0442030552 and .0406929964. The pointwise lower-bound mechanism for higher harmonics is explicit: if Vmin(r) is the smaller eigenvalue of the local 2-by-2 amplitude potential matrix, then ell(ell+1)>sup_r r^2 max(0,-Vmin(r)) makes the local-plus-angular part nonnegative, and both the radial derivative form and electrostatic nonlocal term are nonnegative. The sampled suprema are about 7.508 and 7.424, below 12 for ell>=3. This supplies a useful high-angular-momentum diagnostic; the sampled supremum has not been converted into a certified continuum bound. The actual ell=3 matrix test is also positive. No large angular instability appears in these sampled static sectors.

One omitted direction admits an analytic partial check. Since the accepted neutral amplitude s is positive and solves (-Delta+4f^2+12s^2-3)s=0, the neutral imaginary-field quadratic form for smooth compactly supported eta factorizes as integral s^2 |grad(eta/s)|^2 >=0. It is therefore nonnegative on this class. Its vacuum spectrum is still gapless, and the factorization does not establish nonlinear asymptotic stability. Charged phase gradients and magnetic fields contribute nonnegative spatial energy around the zero-current background; their constrained time evolution has not been numerically solved here.

The neutral Sigma phase remains massless in the vacuum. It is not covered by a gapped real-amplitude spectrum. Neither are the coupled charged phase, temporal evolution, and transverse electromagnetic perturbations tested by these real-amplitude eigenvalues. Fixed charge and Gauss' law must also be enforced in the time-dependent problem. Fragmentation into separated nonlinear daughter solutions is another comparison beyond the free threshold.

The familiar ungauged slope criterion must not be imported as a sufficient gauged stability test. [Panin and Smolyakov, Problem with classical stability of U(1) gauged Q-balls](https://arxiv.org/abs/1612.00737) explains the obstruction to transferring ordinary Q-ball methods directly. Angular instabilities are independently relevant; see [Rajaraman, Instabilities of Gauged Q-Balls](https://arxiv.org/abs/2406.02817), and the numerical three-dimensional study [Kinach and Choptuik, Dynamics of U(1) gauged Q-balls in three spatial dimensions](https://arxiv.org/abs/2408.07561). These are context, not validation of this branch or an assertion that their model-specific stability boundaries apply here.

Next work is the full constrained linearized radial evolution problem, with phase variables and electrostatic constraints included, followed by nonspherical dynamical modes or converged three-dimensional evolution. Static energy checks narrow that task; they do not complete it. The missing scalar-to-spinor map, physical charge normalization, internal sector selection and measured predictions remain separate unresolved requirements for an electron/positron interpretation.

**Checkpoint decision:** the fixed-charge and static stability assessment is complete at the declared scope. Full step 6 is **not established**: conditional static evidence is not a proof of three-dimensional dynamical stability. Step 7 may proceed as a conditional observable calculation, with this prerequisite explicitly open. The bound q=.0025 background used there is not silently assigned the Hessian results calculated at q=0 and .01.
