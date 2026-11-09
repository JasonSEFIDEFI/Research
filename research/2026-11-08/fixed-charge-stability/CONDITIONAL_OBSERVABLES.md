# Step 7 entry: conditional observables and an electron-identification obstruction

**Exploratory / Not Promoted. AI-assisted. These are predictions within the added classical scalar-Maxwell model, not validated electron predictions. Full step 6 dynamical stability is pending.**

Use the nodeless fixed-N solution at q=.0025, lambda=12, N=1250.1753361265248. A separate R=160, tolerance 2e-8 solve gives omega=1.401313034 approximately, E=1767.75236051585 and Qem=3.1254383403. Its free-scalar binding margin is positive, .2625551820. This does not transfer the other backgrounds' Hessian checks to this one or prove stability against fragmentation.

## Charge shape

The model's electric density is rho_em=q(omega-qa)f^2. Normalize its spatial Fourier transform:

\[
F(k)=\frac{4\pi}{N}\int_0^\infty r^2(\omega-qa)f^2\frac{\sin kr}{kr}\,dr,
\qquad F(0)=1.
\]

This is a classical static charge-density form factor in the chosen rest frame. Identifying it with a relativistic quantum scattering form factor requires a derived collective-coordinate quantization and current matrix element; that identification is not supplied here.

\[
\langle r^2\rangle=\frac{4\pi}{N}\int r^4(\omega-qa)f^2dr,
\quad F(k)=1-k^2\langle r^2\rangle/6+O(k^4).
\]

The charge RMS radius is **7.21181331** in the current length unit. Direct integration and the small-k slope agree in radius squared to 5.33e-8 relative for k=.0001.

| k | F(k) |
|---:|---:|
| 0 | 1 |
| .01 | .9991336564 |
| .025 | .9946015051 |
| .05 | .9786338775 |
| .1 | .9180094163 |
| .2 | .7185409135 |
| .5 | .1626820350 |
| 1 | -.0051545463 |

The nonconstant result distinguishes this extended classical charge profile from a point charge. At large separation d compared with the profile radius, its leading electrostatic interaction with another localized charge is Q1 Q2/(4 pi d) in these rationalized units. Equal charges repel and conjugate charges attract at that leading order; internal deformation, scalar exchange and radiation require additional calculations.

## One scale cannot independently fit mass and radius

Under the optional canonical unit map x_dimless=mu x_phys, Phi_phys=mu Phi_dimless and Sigma_phys=mu Sigma_dimless in natural units, energy scales as Ephys=mu E and radius as rphys=r/mu. This assumes the present canonical action is the physical one; it is not a derived SEFI measurement map. The dimensionless product is then invariant:

\[
E_{\rm phys}r_{\rm rms,phys}=E r_{\rm rms}=12748.7000.
\]

If its rest energy were calibrated to a target particle mass M, its radius would be 12748.7 times that mass's reduced Compton length hbar/(Mc). Choosing mu cannot change this ratio. Likewise, the numerical electric charge qN does not change under this unit scaling. Charge normalization must be supplied separately. No physical size fit or experimental exclusion limit is asserted without that measurement map and a suitable current comparison.

## Spin and magnetic response remain decisive

For this static spherical scalar ansatz, spatial momentum density and spatial electric current vanish. Hence its classical angular momentum and magnetic dipole moment are both zero. Charge conjugation reverses its charge but does not generate spin. These statements concern this background, not a theorem excluding all quantizations of every scalar soliton.

The earlier conditional Dirac construction has a stipulated physical spin-half doublet. No map from this scalar profile or its perturbation modes to that doublet has been derived. Assigning a Dirac magnetic moment to the profile would assume the missing result. Thus the current candidate cannot yet be called an electron or positron, even if dynamical stability were later demonstrated.

## Decision and next executable question

Step 7 has now begun with reproducible conditional observables and a scale-invariant diagnostic. It has not reached a calibrated measured prediction. The next decisive mathematical task is to derive, or rule out for the specified action, a physical spin-half collective state and its electromagnetic current. The original topology/sector-selection obstructions remain in force. In parallel, the constrained dynamical stability calculation is still required before calling any candidate stable matter. Proceeding with conditional observables does not mark those requirements complete.
