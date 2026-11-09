# Electromagnetic coupling and a self-consistent charged branch

**Exploratory / Not Promoted. AI-assisted derivation and computation, 2026-11-08. All numerical quantities are dimensionless.**

## What this step establishes

An explicit Maxwell extension of the existing canonical scalar model supports numerical, stationary, localized, electrically charged profiles at several small couplings. The scalar fields and electric potential are solved together. Gauge covariance, the current normalization and Gauss' law agree. This is a concrete extension of the action, not a derivation of electromagnetism or of the elementary charge from the original SEFI action. The scalar solution and the previous conditional Dirac construction are different models; no identification between them has been derived.

## 1. Specify the action before identifying charge

Use metric (+---), natural units, and

\[
\mathcal L=\tfrac12(D_\mu\Phi)^*D^\mu\Phi
+\tfrac12\partial_\mu\Sigma^*\partial^\mu\Sigma
-V(|\Phi|^2,|\Sigma|^2)-\tfrac14F_{\mu\nu}F^{\mu\nu},
\quad D_\mu=\partial_\mu+iqA_\mu,
\]
\[
V(\rho,\eta)=\rho^2/4+\rho/2+2\rho\eta
+\tfrac\lambda4(\eta-3/\lambda)^2.
\]

Phi is charged and Sigma is neutral. The Maxwell field, its normalization and the parameter q are additional inputs. Under

\[
\Phi\mapsto e^{-iq\chi}\Phi,\quad A_\mu\mapsto A_\mu+\partial_\mu\chi,
\]

D Phi transforms by the same phase and F is invariant. Sigma's global phase symmetry remains separate. It is not the photon.

The half normalization of each complex scalar matters. Varying A gives

\[
\partial_\nu F^{\nu\mu}=j^\mu,
\qquad j^\mu=-q\operatorname{Im}(\Phi^*D^\mu\Phi).
\]

Indeed, the matter variation is +q Im(Phi* D Phi) delta A, and Maxwell's variation is +(partial F) delta A. The Phi equation and its conjugate imply partial_mu j^mu=0. There is no extra factor of two. With the earlier global-current convention Im(Phi* partial Phi), electric charge is minus q times that charge at A=0. Below the negative time-phase convention makes the electric density positive for positive q and omega.

A0 has no time derivative in the action: its canonical momentum vanishes. Its Euler equation is the Gauss constraint div E=j0, rather than a new propagating scalar polarization. The Maxwell constraint structure is the usual local U(1) one.

## 2. The vacuum restricts the gauge embedding

At Phi=0 and |Sigma|=v=sqrt(3/lambda), the chosen gauge U(1) is unbroken. There is no photon mass term at tree level. If instead Sigma carried charge qSigma under this same single Maxwell field, its kinetic term would contain

\[
\tfrac12q_\Sigma^2v^2 A_\mu A^\mu,\qquad m_\gamma^2=q_\Sigma^2v^2.
\]

Thus the proposed one-photon embedding keeps the nonzero condensate neutral. More elaborate gauge groups would require their own mass-matrix analysis. Neither this choice nor charge quantization follows from the original scalar action.

## 3. Radial scalar-Maxwell equations

Choose

\[
\Phi=e^{-i\omega t}f(r),\quad\Sigma=s(r),\quad A_0=a(r),\quad A_i=0,
\quad \Omega(r)=\omega-qa(r).
\]

Fix a(infinity)=0, so omega is the asymptotic frequency. The field equations are

\[
f''+\frac2r f'=[1+f^2+4s^2-\Omega^2]f,
\]
\[
s''+\frac2r s'=[4f^2+\lambda s^2-3]s,
\]
\[
a''+\frac2r a'=-q\Omega f^2.
\]

Regularity requires f'(0)=s'(0)=a'(0)=0. At infinity, f=0, s=sqrt(3/lambda), and a=0. The Coulomb tail is a=Qem/(4 pi r). Define the continuous classical charge number N and electric charge by

\[
N=4\pi\int_0^\infty r^2\Omega f^2dr,
\quad Q_{\rm em}=qN=-4\pi\lim_{r\to\infty}r^2a'.
\]

N here is a classical integral, not a demonstrated integer occupation number. It is not the internal oscillator N used in the earlier sector-selection calculation.

The energy is

\[
E=4\pi\int_0^\infty r^2\left[
\tfrac12(f'^2+s'^2+a'^2)+\tfrac12\Omega^2f^2+V(f^2,s^2)\right]dr.
\]

Charge conjugation Phi -> Phi*, A -> -A, omega -> -omega reverses Qem while preserving the energy. This supplies conjugate classical charged configurations, not electron/positron spin or statistics.

For a fixed scalar profile, the electric equation is

\[
(-\nabla^2+q^2 f^2)a=q\omega f^2.
\]

The decaying solution is unique in the finite-electric-energy class: subtract two solutions, multiply by their difference and integrate to obtain integral (|grad delta a|^2+q^2 f^2 delta a^2)=0. The boundary value at infinity removes the constant freedom. For omega,q>0, the maximum principle gives 0<=qa<=omega. The following calculation also allows f and s to respond.

## 4. Self-consistent numerical continuation

The protocol was written before running the scan. We use lambda=12, omega=1.401223084350689, and the previously saved Q1250 ungauged seed. The continuum solve at q=0 yields N=1250.175336, not exactly 1250; the historical filename labels the seed, not an imposed charge constraint.

The adaptive boundary-value solver treats all three fields simultaneously. At outer radius R the conditions are f(R)=0, s(R)=0.5 and a'(R)+a(R)/R=0. The last condition retains the Coulomb tail rather than artificially setting the finite-radius potential to zero. The exterior electric energy Qflux^2/(8 pi R) is included. Neglected scalar tails are tested by domain enlargement. Numerical profiles are approximations, not an analytic existence proof.

| q | N | Qem | E, including exterior electric energy | E/N | Status |
|---:|---:|---:|---:|---:|---|
| 0 | 1250.175336 | 0 | 1767.697330 | 1.413959530 | accepted |
| 0.0025 | 1257.364140 | 3.143410 | 1777.825801 | 1.413930734 | accepted |
| 0.005 | 1279.806989 | 6.399035 | 1809.443091 | 1.413840608 | accepted |
| 0.01 | 1385.547786 | 13.855478 | 1958.354378 | 1.413415256 | accepted |
| 0.015 | 1658.095954 | 24.871439 | 2341.832093 | 1.412362226 | accepted |
| 0.02 | approximately 0 | approximately 0 | approximately 0 | not meaningful | rejected: vacuum |

All accepted profiles are positive and nodeless under the declared amplitude cutoff, with residuals below 1e-7. For nonzero accepted q, integrated charge and asymptotic electric flux agree to better than 5e-10 relative in the R=120 scan. Replication of q=.01 at R=160 and tolerance 2e-8 changes N by 1.468e-8 relative and E by 1.455e-8 relative; its Gauss error is 1.235e-9. At that point a(0)=.2201253604 and Omega(0)=1.3990218307, demonstrating the self-consistent electric shift.

The q=.02 solver reports convergence but finds the vacuum. The nontriviality and Gauss checks reject it. This continuation attempt establishes neither a maximum coupling nor absence of another branch. The original test assertion expected every requested point to survive; after observing this rejection, the script's final assertion was corrected to accept an explicitly recorded stop while still requiring preceding profiles and the independent replication to pass. No rejected point is relabeled as a soliton.

Multiplying Gauss' law by a and integrating, including its exterior tail, supplies a useful consistency identity:

\[
\tfrac12\int \Omega^2f^2d^3x+\tfrac12\int |\nabla a|^2d^3x
=\tfrac12\omega N.
\]

The code records its relative energy residual separately. This identity also guards against omitting the exterior electric field energy.

## 5. Why decreasing E/N here is not electric attraction

This scan holds omega fixed. N changes substantially, so its rows cannot establish the effect of electric repulsion at fixed charge number. At fixed N and fixed scalar shapes, the small-q expansion instead has a positive leading Coulomb cost:

\[
E_q=E_0+\tfrac{q^2}{2}\int d^3x\,d^3y\,
\frac{n_0(x)n_0(y)}{4\pi|x-y|}+O(q^4),
\quad n_0=\frac{N f^2}{\int f^2d^3x}.
\]

This follows by solving -Delta a=q n0+O(q^3), adjusting omega to keep N fixed, and expanding the scalar time and electric energies. The O(q^2) correction to scalar time energy cancels at fixed N and shape. Profile relaxation must still be solved; the displayed formula alone does not prove a globally minimized branch.

The table's E/N values lie below mPhi=sqrt(2), the free Phi mass, in these dimensionless parameters. That is an energetic comparison with dispersed free Phi quanta if that interpretation is supplied. It does not establish stability against nonspherical disturbances, fragmentation, radiation, or the neutral massless phase channel. No observed electron charge, mass or radius is fitted or predicted.

## 6. Coupling the previous conditional Dirac reference

Separately, if the massive spin-half Dirac field is supplied as in the preceding checkpoint, the standard extension is

\[
\mathcal L_D=\bar\psi(i\gamma^\mu D_\mu-m)\psi-\tfrac14F^2,
\quad j_D^\mu=q\bar\psi\gamma^\mu\psi.
\]

With the same D=partial+iqA convention and psi -> exp(-iq chi)psi, the interaction is -q A_mu bar psi gamma^mu psi. Its current sign follows the first-order Dirac kinetic term; copying the half-normalized scalar current would be an error. Opposite particle and antiparticle charges then follow from the stipulated Dirac field and its CAR quantization. Their charge magnitude q is still an input. The tree-level identity k_mu(q gamma^mu)=q[(slash p+slash k-m)-(slash p-m)] checks this minimal vertex, not an all-orders derivation or a proof of electron structure.

This conventional gauge extension is described in [Tong's QED notes](https://www.damtp.cam.ac.uk/user/tong/qft/qfthtml/S6.html). Gauged Q-balls are an established class, distinct from elementary spin-half particles; see [Heeck et al., Mapping Gauged Q-Balls](https://arxiv.org/abs/2103.06905). These sources provide context, not validation of the particular numerical SEFI branch.

## 7. Remaining bridge and next calculation

There are now two consistent conditional constructions: a charged localized scalar-Maxwell profile, and a minimally coupled Dirac reference. No supplied map turns the former into the latter. Charge quantization, selection of the internal doublet, its physical rotation action and its relation to a localized scalar configuration remain open.

The next executable step is a fixed-N gauged continuation with omega solved as an unknown, followed by constrained perturbation analysis. Start near N=1250.175336, q=0 and track small q; compare energies at the same N, check flux and domain convergence, then analyze radial perturbations with Gauss' constraint enforced. Nonspherical modes and the neutral phase must be included before a full stability claim. This may locate a failure of the model as readily as a viable branch. Calling the field an electron-positron duality field remains a research proposal, not a result established here.
