# SEFI / DEFI / GWFM: manuscript and experimental-consistency review

Prepared October 22, 2026. This is a first technical audit, not peer review, experimental validation, or an exhaustive assessment of all physics.

## Finding

The files examined do **not establish that SEFI fits all known experiments perfectly**. Some results of the specified classical oscillator model are mathematically supported and independently reproducible. Several broader physical claims remain unspecified, and some intermediate mathematical claims have explicit counterexamples. An incomplete prediction cannot be scored as either experimental agreement or experimental disagreement.

The phase-dynamics manuscript is particularly useful because it already identifies many of the earlier papers' limitations. Its careful restrictions should be carried into the companion papers. A verified oscillator calculation supports that calculation; it does not independently verify a single-entity ontology, electron-field emergence, quantum error correction, or molecular stabilization.

## Material and scope

I read the mathematical source text of versions corresponding to the eight titles in your submission list, including warp, and the SEFI Space manuscript. I also inspected the double-slit simulation engine and its display component and extracted the written double-slit and superposition explanations. Figures, videos, all archived drafts, all supplementary datasets, and the entire software collection have not been audited. Source text is not a guarantee of identity with the files actually submitted to a journal. No acceptance or publication status was inferred from filenames or tracking numbers.

The exact source files and SHA-256 hashes are in `SEFI_review_source_manifest.json`. Principal sources:

| Manuscript | Source version examined |
|---|---|
| Geometric Worldline Foundations of the Electron Field | `V:\V Drive and GitHub Content\Journal Submissions\GWFM\GWFM_Full_Manuscript_Dutton.tex` |
| SEFI: Formal Mathematical Construction | `V:\V Drive and GitHub Content\Journal Submissions\SEFI\SEFI_Formal_Mathematical_Construction.tex` |
| Unified Geometric Field Theory | `V:\THINKING DEEPLY\JMP\ADV SUBS\JMP26-AR-02666.tex` |
| Displacement-Engineered Warp Fields | `V:\V Drive and GitHub Content\Journal Submissions\The New Warp\warp.tex` |
| DNA as a Golden-Ratio Helical Worldline | `V:\V Drive and GitHub Content\Journal Submissions\DNA\manuscript.tex` |
| Dynamic Entity Field Integration | `V:\V Drive and GitHub Content\Journal Submissions\DEFI\DEFI_Formal_Construction.tex` |
| Geometric Photonic Quantum Error Correction | `V:\V Drive and GitHub Content\Journal Submissions\FULL SUBMISSION\manuscript.tex` |
| Phase Dynamics, Recurrence, and Relational Temporal Ordering | `V:\V Drive and GitHub Content\Journal Submissions\Time\Jason_D_Dutton_Phase_Dynamics_Temporal_Ordering.tex` |

Numerical checks below were implemented independently rather than obtained by executing the author's verification script. Detailed numerical results are in `SEFI_independent_checks.json`. They are computations on model equations, not laboratory experiments or fits to experimental data.

## 1. What checks out in the phase-dynamics reduction

**Origin energy.** For the stated decoupled equation `I_O'' + I_O = 0`, differentiating `Q_O = alpha (I_O'^2 + I_O^2)/2` gives zero. This is a genuine conserved subsystem energy. It does not identify a unique state or guarantee boundedness of the other coordinates.

**Linear stability threshold.** For the constant-geometry, linear-coupling reduction, the normalized stiffness matrix is

```
B = [[1, a, b], [a, 1, 0], [b, 0, 1]],  r = sqrt(a^2+b^2).
```

Its eigenvalues are `1-r, 1, 1+r`. Independent numerical diagonalization of 1,000 random matrices agreed to a maximum absolute error of about `1.11e-15`. All reduced solutions are bounded for `r<1`; `r=1` permits linear drift; `r>1` admits growing solutions. For `r=1.2`, a growing mode has exponent `sqrt(0.2) ≈ 0.447214`. These are properties of the reduced model, not measured material constants.

**Driven counterexample.** I independently integrated

```
eta'' + [0.5 - 0.1 cos(sqrt(2) tau)] eta = 0
```

over one drive period. At 2,048 Runge-Kutta steps, the response matrix has trace `-2.024666915415934`, determinant `0.9999999999999981`, multipliers approximately `-1.169874022627` and `-0.854792892789`, and envelope growth rate `0.0353140229504`. Step refinement supports numerical convergence. These reproduce the manuscript's quoted values. The `Omega=2.2` comparison also reproduces its bounded-case multipliers. Positive instantaneous stiffness does not imply bounded motion under periodic driving.

**Phase and recurrence.** The stated harmonic phase lift, the obstruction to a globally increasing instantaneous reading on a periodic orbit, and the need for commensurate excited frequencies for exact full-state recurrence are supported under the paper's assumptions. The relational evolution equation is an invertible clock change when phase speed is positive and the history is available. It does not remove the parameter from the original action. The paper says this explicitly.

**Nonlinear potential.** Completing the squares produces the stated effective potential. Its coercivity is a sufficient confinement condition for the autonomous identity reduction with positive kinetic energy and the stated regularity. It is not a proof of stability for unrestricted geometry or arbitrary coupling functions.

These are substantive mathematical results within a defined model. Their novelty relative to existing dynamical-systems work has not been established by this audit.

## 2. GWFM and the double-slit claim

The GWFM manuscript states that its construction preserves all QM and QFT predictions, but it does not supply the equivalence proof. Its derivations appendix is a list of topics rather than the promised derivations.

The formulas `T=T_A union T_B` and `I(x)=measure(T_A intersection T_B)` do not by themselves produce quantum interference. Two contributions can have identical support and opposite amplitudes: `A=1`, `B=-1`, giving zero total intensity despite complete overlap. A phase-weighted amplitude construction can handle cancellation; GWFM also writes a schematic phase-weighted path integral, so this is a limitation of the set-intersection formula, not a proof that every worldline formulation fails.

What is missing is a specified measure, boundary conditions, normalization, detector model, and a derivation of the observable probabilities. The positive trajectory-occupation distribution `phi(x)=integral delta(x-y(tau)) d tau` is not automatically a complex spinor-valued electron field.

The displayed GWFM action has a free Grassmann kinetic term and electromagnetic coupling through `q integral y_dot A`. It does not display the spin-field coupling and constraints needed to establish the spinor-QED equivalence. Merely including Grassmann variables does not derive the electron magnetic moment or exchange statistics. Compare the actual worldline-QFT machinery and amplitude calculations in [Schubert's review](https://arxiv.org/abs/hep-th/0101036).

The inspected simulator is at `V:\THINKING DEEPLY\Microsoft\Double Slit Simul;ator\SEFI_DoubleSlitEngine.js`. It calculates two radial sine waves, adds them, divides by two, and squares the result. It then adds a chosen local intensity contribution around the displayed electron and applies a user-defined collapse threshold. The `slitWidth` argument is read but does not enter the engine's field calculation; in the inspected display component it changes the drawn slit rectangles. Thus this version cannot test the physical effect of changing slit width on the diffraction envelope.

That code illustrates interference encoded in its input formula. It does not derive that formula from the SEFI identity dynamics or compare predicted counts with measured counts. The separate four-page double-slit explanation is interpretive prose; it does not supply that missing quantitative derivation. The extracted superposition PDF likewise contains schematic formulas and placeholder derivation sections. Other versions may contain additional work and would need separate inspection.

## 3. SEFI and SEFI Space

Layer names and functions are defined, but explicit observable maps for Origin, Authorship, Sovereignty, and Warp remain missing. Invariance under an allowed transformation is not automatically conservation along a dynamical history.

The initial acceleration bound is written with coordinate-time derivatives and an ordinary norm. To make a universal relativistic statement, its frame dependence and physical units must be specified or replaced with an appropriately covariant formulation. A bounded identity oscillator does not independently impose this bound on the spacetime trajectory.

SEFI Space adds a positive diagonal metric and a possible internal action. Its own future-work section defers explicit layer functions. There is also a distinction to resolve between preserving the entire identity vector and changing its Warp coordinate: either the vector is unchanged, or only a specified invariant/equivalence class is preserved. The intended interpretation must be defined consistently.

## 4. DEFI: a valid subsystem calculation, but an invalid equivalence claim

The Origin conservation calculation is valid with the stated metric convention. The later phase paper explicitly clarifies index lowering and dimensionless time, resolving an ambiguity that would otherwise affect interpretation of the kinetic expression.

However, vanishing identity acceleration at an instant does **not** imply

```
D/dtau (kappa, torsion, I_dot, I_ddot) = 0.
```

The latter also requires constant geometric invariants and vanishing derivatives of the identity accelerations. A harmonic coordinate can have zero acceleration at a zero crossing and nonzero third derivative there. Equilibrium of the Sovereignty/Warp/Authorship coordinates does not force the independent Origin oscillator to stop. A fixed point in the full dynamical state requires conditions on velocities as well as positions.

Likewise, freezing nonzero identity coordinates does not generally remove `mu_1 kappa^2 I_S + mu_2 torsion^2 I_W`. It remains geometry-dependent and can still affect the geometric variation. Removing the coupling requires additional conditions, such as vanishing coupling functions or relevant coordinates.

The geometric variation has not been explicitly carried out. Curvature and torsion introduce higher trajectory derivatives; parameter constraints and boundary conditions matter. Conservative dynamics does not generally relax to an attracting equilibrium without an additional mechanism. The phase paper correctly acknowledges these issues. The companion DEFI paper's stronger claims should be reconciled with it.

## 5. DNA: explicit numerical and logical issues

The cylindrical-helix formulas are valid as spatial geometry. With the manuscript's input values:

```
kappa/torsion = 21 pi / 34 = 1.940395462511...
pi/phi                     = 1.941611038725...
```

Their relative difference is about `-0.06261%`. Proximity of rounded input values is not exact golden-ratio locking. This small mismatch alone does not reject an approximate empirical model; it rejects the claim that exact equality was proved from those values.

The stated phase-offset equation `(2 pi/10) phi` evaluates to approximately `58.2492 degrees`, not `144 degrees`. This is an arithmetic inconsistency independent of molecular interpretation.

The action explicitly inserts the desired target into `lambda (kappa/torsion - pi/phi)^2 ||I||^2`. Minimizing that penalty favors the target by construction when its coefficient is positive and the identity norm is nonzero. It does not derive why nature selects that target. At zero identity norm the penalty vanishes for any admissible ratio; competing terms also prevent inferring a global minimum of the full action from this term alone.

A constant curvature/torsion ratio is not thereby a topological invariant. A static spatial backbone curve is not automatically a material particle's timelike trajectory. Establishing biological protection against decoherence requires a defined physical state, environment, coupling, and measured coherence observable. These are not supplied.

The full identity-norm penalty also changes the Origin equation away from exact matching, so the original Origin energy is not generally conserved. The later phase paper correctly derives this modification. DNA structural variation must also be confronted; [the experimental sequence-dependence literature](https://doi.org/10.1038/292375a0) makes a universal rigid helix assumption inappropriate without explicit restrictions.

## 6. Photonic QEC: a geometric demonstration, not a verified quantum recovery

The saddle example uses `Sigma: z=alpha x^2-beta y^2` and maps a point vertically onto its graph. This is a retraction, but generally not the Euclidean nearest-point projection asserted in the surrounding discussion.

Counterexample with `alpha=beta=1`: from `(1,0,2)`, the stated map returns `(1,0,1)` at distance `1`. The surface point `(1.1,0,1.21)` is closer, at distance approximately `0.796304`.

For the specific example, resetting the perturbed z coordinate restores the reference exactly because x and y were kept exact. That is an algebraically correct construction, but its exact recovery is built into the chosen perturbation. It does not establish correction of general unknown errors. Projection onto a surface alone also does not fix a curve's curvature and torsion: many distinct curves lie on the same surface.

At `t=0`, the reference `(t,sin(t),alpha t^2-beta sin(t)^2)` has tangent `(1,1,0)` and acceleration `(0,0,2(alpha-beta))`. In the allowed case `alpha=beta`, curvature vanishes and the ordinary Frenet normal/binormal are undefined. Even when `alpha!=beta`, `(0,0,cos(t))` is not generally a binormal displacement; the label requires a calculation or a different frame.

For quantum error correction, a classical trajectory and geometric projection are insufficient. Specify an encoded quantum subspace, noise channel, physically implementable recovery, and logical/entanglement fidelity. Exact correction can be tested through the [Knill-Laflamme framework](https://arxiv.org/abs/quant-ph/9604034). Approximate correction needs an explicit error criterion. The phase manuscript already recognizes this requirement.

The premise that established QEC lacks geometry also needs narrowing: [GKP's original work](https://arxiv.org/abs/quant-ph/0008040) explicitly uses noncommutative phase-space geometry.

## 7. Unified operator and warp construction

The unified manuscript appropriately labels particle assignments and cosmological claims as hypotheses. An eigenvalue equation alone does not derive observed masses, charges, spin, or interactions.

The Lorentzian spacetime operator remains hyperbolic regardless of a positive internal metric. A nearest-point minimization based on a positive Riemannian distance cannot simply be imported to Lorentzian spacetime. A chosen spatial slice, auxiliary positive metric, or another well-defined prescription is necessary. Derivative-dependent worldline invariants used as field potentials also need an explicit correspondence to functions/operators on the stated Hilbert space.

The internal term is written with `+Delta_I` and a positive quadratic potential. On a positive Euclidean internal space, that is not the usual confining harmonic-oscillator operator `-Delta_I + V`. Rapidly oscillating compactly supported functions can drive its kinetic quadratic form negatively without bound. A stable particle-spectrum interpretation therefore needs a sign/convention analysis and a defined spectral problem; it does not follow from the displayed formula. This is not a claim that every such differential operator lacks self-adjoint realizations.

For warp, the source leaves the functions `D`, `C`, and `f` schematic. It describes grids, integration, and numerical results without providing their complete numerical specification in the main text. The located folder contains source, figures, a video, and a readme, but I did not locate or audit a complete supplementary implementation there. No inference about unavailable supplements is warranted.

The condition `C=0` defines a level set; it does not prove invariance or attraction under the flow. The phase paper supplies the missing invariance test, `partial_tau C + grad(C).f = 0` on the constraint. A 3D curl also requires a specified spatial restriction if the proposed field is a four-vector. No spacetime metric solution, stress-energy budget, or laboratory propulsion measurement is established by the geometric flow construction.

## 8. Selected experimental benchmarks

This is a finite benchmark map, not a claim to have executed experiments or exhaustively reviewed experimental physics. “Not derived” is not synonymous with “ruled out.”

| Benchmark | Required comparison | Status in the examined material |
|---|---|---|
| Single-electron interference buildup | Position probabilities and count statistics with apparatus geometry | Qualitative explanation and fringe visualization; no fitted experimental comparison. [Experimental reference](https://doi.org/10.1119/1.16104). |
| Slit-width and separation dependence | Fringe spacing, diffraction envelope, visibility | Separation and wavelength enter the inspected engine; width does not enter its field computation. |
| Which-path detection / decoherence | Detector coupling, reduced state, visibility versus distinguishability | Qualitative stabilization language; a quantitative measurement model is missing. |
| Aharonov-Bohm phase | Phase shift versus enclosed flux | Gauge-coupling term is structurally relevant; derivation and data comparison are not supplied. [Experimental reference](https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevA.34.815/fulltext). |
| Bell/CHSH correlations | Joint probabilities versus settings, with locality and measurement assumptions explicit | No complete SEFI joint-probability derivation. “One geometry” alone is insufficient; the framework is not thereby ruled out. [Hensen et al.](https://arxiv.org/abs/1508.05949). |
| Electron spin and magnetic moment | Spinor dynamics and magnetic response, including radiative corrections | Not calculated from the displayed GWFM construction. [Precision measurement](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.130.071801). |
| Fermionic exchange / exclusion | Antisymmetry or equivalent observable amplitudes for multiple fermions | Not derived by the occupation-density formula or entity postulate. |
| Atomic spectra and scattering | Calibrated energy levels, amplitudes, cross sections, uncertainties | No completed predictive calculation identified in the examined eight papers. |
| Quantum recovery | Encoded-state and entanglement preservation under a specified noise channel | Classical surface restoration shown; quantum recovery not established. |
| DNA structure and fluctuations | Structural distributions and environmental/sequence dependence | Approximate geometric input fit; exact locking and decoherence protection not demonstrated. |
| Relativistic clocks | Proper-time calibration and measured rate comparisons | Phase paper states a compatible calibration assumption; no independent derivation or measurement. |
| Cosmological expansion | Stress-energy dynamics and observational likelihoods | Phenomenological scaling statements; no completed observational comparison. |

If the intended theory is exactly empirically equivalent to established QM/QFT, that can be a legitimate interpretive objective. It requires an equivalence construction, and those same experiments would not uniquely select its ontology. A new physical prediction is necessary to distinguish it experimentally from an empirically equivalent alternative.

## 9. A concrete route toward a lab test

Start with the best-specified sector: the coupled-oscillator reduction. Define three measured coordinates, independently calibrate their inertial coefficients and couplings, and predict mode splitting before collecting the response data. Test the threshold and periodically driven growth against conventional oscillator equations. This can validate an effective implementation; ordinary coupled oscillators can reproduce these results too.

To test SEFI specifically, derive an independently calibrated relation from physical curvature/torsion to those couplings and identify a predicted departure from the conventional apparatus model. Specify the predicted magnitude, uncertainties, and the outcome that would reject the relation. Do not fit all couplings retrospectively and call the fit an independent prediction.

For the photonic route, replace the geometric analogy with one explicit encoded state, one error channel, and one realizable recovery operation. Compare logical and entanglement fidelity with and without correction, accounting for rejected events and resource costs. Geometric filtering of accepted events alone is not proof of unconditional quantum recovery.

Before either test, reconcile companion manuscripts with the phase paper's corrections: restrict stability claims, fix the DNA arithmetic and exactness claims, distinguish retraction from nearest-point projection, and supply the omitted quantum and geometric derivations. The files support developing a testable research program; they do not currently support a claim that every known experiment has been matched.
