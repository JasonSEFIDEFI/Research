# Step 7: calibration, observable convergence and a failed direct electron identification

**Exploratory / Not Promoted. AI-assisted.** The observable implementation is now tested under the same domain/tolerance change used for the bound scalar-Maxwell candidate. This closes a numerical comparison; it does not close the missing quantum measurement map.

## What is stable numerically

For q=.0025, N=1250.1753361265248 and lambda=12, changing R=120,tol=1e-7 to R=160,tol=2e-8 changes energy by 2.37e-11 relative, charge RMS radius by 1.04e-9 relative, and the eight sampled normalized charge form factors by less than 3.95e-10 absolute. F(0)=1 is checked. The charge RMS radius remains 7.21181331 in the model's units.

These are classical rest-frame current-density observables. No derived relativistic quantum current matrix element connects them to scattering form factors. The small numerical changes do not supply that map or quantify modeling error.

## Conditional comparison with measured inputs

The primary reference is the [NIST 2022 CODATA complete constants table](https://physics.nist.gov/cuu/Constants/Table/allascii.txt). Inputs used here are electron rest energy .51099895069 MeV, alpha=.0072973525643, hbar c=197.3269804 MeV fm, and the nonzero electron magnetic moment -9.2847646917e-24 J/T. NIST also lists electron g=-2.00231930436092. These are supplied observations, not quantities predicted by the scalar calculation.

Under the explicitly assumed canonical unit map x_dimless=mu x_phys, Phi_phys=mu Phi_dimless, and the same scaling for Sigma and A, the overall mass/energy scale mu is the only dimensional scale. Maxwell normalization remains fixed. Fitting the bound q=.0025 profile's mass to the electron gives

| Quantity | Conditional outcome |
|---|---|
| Fitted mass scale mu | .000289067044742 MeV |
| Model electric-charge magnitude / e | 10.3210370907 |
| Classical charge RMS radius | 4.92302865e-9 m |
| Classical magnetic dipole moment | 0 |

The profile's charge is qN in rationalized natural units, while e=sqrt(4 pi alpha). Changing mu cannot turn 10.321e into e. The negative-charge conjugate changes only the sign, not this magnitude or the zero dipole.

One can **fit** the coupling too: q=e/N=.000242223720160. Because that changes the field equations, the script solves a new background. Fitting its mass scale as well gives charge magnitude/e=1 to numerical tolerance and a charge radius approximately 4.91884431e-9 m. Its stability has not been tested here and is not inherited from q=.0025. Two fitted observations are not two predictions. Its magnetic dipole remains zero.

No electron-size exclusion threshold or quantum scattering chi-squared is asserted from the classical radius alone. The map to a quantum form factor is absent. The calibration already demonstrates what is free to fit and what is not explained.

## Exact obstruction for the specified ansatz

For a static spherically symmetric scalar profile, the spatial current vanishes, B=0 and the momentum density has no angular component. Therefore

\[
\boldsymbol\mu=\tfrac12\int\mathbf r\times\mathbf j\,d^3x=0,
\qquad\mathbf J=0.
\]

Every spatial rotation leaves the background unchanged. Its rotational collective orbit is a point; there is no orientation coordinate whose quantization produces a rigid-rotor spin-half doublet. This is a statement about this ansatz and its conventional spatial rotation action. It is not a theorem about every quantum state of every scalar theory.

If this classical current is identified directly with the electron's magnetic response, it contradicts the measured nonzero moment. With J=0 it is also incorrect to quote a predicted g=0: the usual spin gyromagnetic ratio is undefined for this background. No unit change makes zero dipole nonzero. Adding an internal spin operator or assigning the previous conditional Dirac magnetic moment would supply new structure whose coupling and physical rotation map still require derivation.

## Step 7 decision

The numerical charge-shape calculation and its convergence assessment are complete within the specified classical model. Direct electron identification using that model's present background/current **fails** the magnetic-response test. An alternative quantum identification remains **unestablished**, because no spin-half state, normalized current matrix element, mass/charge selection or calibrated new prediction is derived. The candidate's stability cannot resolve this kinematic/current obstruction.

Step 8 can review these conclusions and the missing bridge. It cannot honestly review this package as a completed derivation of matter or as a successful electron model. No parameter has been silently changed to turn this failed requirement into a pass.
