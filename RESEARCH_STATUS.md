# Research status

Updated 24 October 2026. This repository was renamed from PhD to Research at the author's request. Repository history and existing manuscript status are retained.

## First correction and working manuscript — 25 October 2026

[Critical-limit correction record](https://github.com/JasonSEFIDEFI/SEFI-PY/blob/18a5275df36d32af1b67d514c0c337637ff2c210/research/2026-10-25/critical-correction/README.md) derives first-order charge coefficients from the reduced stationary equations without fitting full-model charge data. At two declared new couplings, corrected errors against the computed full-model charges are 0.37–1.70 ppm, roughly 1,200–2,400 times smaller than the leading prediction errors. Checks include symbolic expansion, action comparisons, an independent sensitivity equation and domain/tolerance refinements. An explicit conditional maximum-principle bound controls one transverse-amplitude elimination step at prescribed f; it does not establish the full coupled expansion.

The [working manuscript](https://github.com/JasonSEFIDEFI/SEFI-PY/blob/18a5275df36d32af1b67d514c0c337637ff2c210/research/2026-10-25/critical-correction/MANUSCRIPT_DRAFT.md), [derivation](https://github.com/JasonSEFIDEFI/SEFI-PY/blob/18a5275df36d32af1b67d514c0c337637ff2c210/research/2026-10-25/critical-correction/DERIVATION.md), [conditional bound](https://github.com/JasonSEFIDEFI/SEFI-PY/blob/18a5275df36d32af1b67d514c0c337637ff2c210/research/2026-10-25/critical-correction/AMPLITUDE_BOUND.md) and [prior-work comparison](https://github.com/JasonSEFIDEFI/SEFI-PY/blob/18a5275df36d32af1b67d514c0c337637ff2c210/research/2026-10-25/critical-correction/LITERATURE_COMPARISON.md) are versioned at SEFI-PY commit `18a5275df36d32af1b67d514c0c337637ff2c210` in [draft PR #6](https://github.com/JasonSEFIDEFI/SEFI-PY/pull/6). **Exploratory / Not Promoted.** No journal submission, established novelty or uniform coupled-limit theorem is claimed. Author verification, independent technical review, broader novelty assessment and explicit approval before promotion remain required.

## Frequency continuation and critical coupling — 25 October 2026

[Stationary-branch and formal critical-limit record](https://github.com/JasonSEFIDEFI/SEFI-PY/blob/446e6177ec30b840a0fcd336ff72dd96a1c2df4e/research/2026-10-25/localized-frequency/README.md) resolves a numerical charge minimum near Q=953.31 at lambda=12, distinct from the free-threshold binding crossing near Q=1225.43. Two Q=1000 stationary profiles have different computed radial constrained-energy character. Coupling continuation reaches lambda=15.9; a formally derived reduced variational problem predicts delta^(-3/2) charge growth, with about 0.41% discrepancy in the scaled minimum at that coupling. A model-specific virial obstruction for the stated stationary class at lambda>=16 is documented with its assumptions.

The package contains all initial and recovery attempts, raw profiles, grid/domain/tolerance comparisons, symbolic checks, a derivation and a [publication-readiness assessment](https://github.com/JasonSEFIDEFI/SEFI-PY/blob/446e6177ec30b840a0fcd336ff72dd96a1c2df4e/research/2026-10-25/localized-frequency/PUBLICATION_READINESS.md). It is pushed at SEFI-PY commit `446e6177ec30b840a0fcd336ff72dd96a1c2df4e` on the existing [draft PR #6](https://github.com/JasonSEFIDEFI/SEFI-PY/pull/6), not merged into main. **Exploratory / Not Promoted**: no general nonlinear stability, proved singular-limit convergence, established novelty or physical-particle claim. Next work is a controlled critical-limit correction and independent technical/literature review. No journal submission or promotion approval is recorded.

## Exploratory numerical update — 25 October 2026

[Localized vacuum branch continuation and publication assessment](https://github.com/JasonSEFIDEFI/SEFI-PY/blob/d3fa758cb9404ddcfd58d6f2e5bb6c46a6dead19/research/2026-10-25/localized-branch/README.md) extends the lambda=12 two-complex-scalar study across thirteen charges on three grids, compares 26 sampled two-daughter energies, and cross-checks a free-threshold binding crossing near Q=1225.43 with continuum collocation. Stationary localized states above threshold, unresolved low-charge runs and an extended finite-box state are retained separately. The record includes raw profiles, variational checks and a conditional phase-sector derivation.

[Draft SEFI-PY pull request #6](https://github.com/JasonSEFIDEFI/SEFI-PY/pull/6) contains the new research package; it is published on a research branch and has not been merged into SEFI-PY main. **Exploratory / Not Promoted.** There is no observed-particle, global minimization, general nonlinear stability or established novelty claim, and no journal submission. Next work is frequency/fold continuation, coupling dependence and a detailed comparison with existing multi-field soliton literature. This update follows the existing localized-field priority and preserves the [SEFI-INV-001 approval gate](research/checkpoints/SEFI-INV-001.md).

## Current research priority

[Research review and priorities](research/2026-10-24/research-priorities/REVIEW.md): concentrate on the existing two-field localized-vacuum branch, derive an effective collective-coordinate/identity correspondence, and then study interactions. Preserve the moving-ring branch and use Lieb–Liniger as a bounded exact correlation benchmark. Application tracks remain separate until they supply their missing constitutive or experimental inputs.

The review follows the author's instruction to follow the mathematics from his models. It ranks the major documented research tracks, identifies the next decisive calculations, and records the limits of its source review.

## Latest technical checkpoint

[SEFI Hamiltonian audit](research/2026-10-24/sefi-hamiltonian-audit/REPORT.md): explicit coordinate-time reduction of the newer foundations action, handling its reparametrization constraints. The unrestricted nonzero-curvature-coupled realization admits regular timelike histories with energy unbounded below. This is a mathematical obstruction to a globally positive-energy reading of that realization, not a disproof of every possible single-entity interpretation.

The folder includes the complete derivation, pinned source manifest, reproducible Python/SymPy checks and numerical results. Exact symbolic claims, numerical implementation evidence, and unconstructed physical hypotheses are separated.

## Prior checkpoint

[Exact two-body finite-jump correlation transport and finite-N endpoint benchmarks](https://github.com/JasonSEFIDEFI/Research/tree/6e77ff32c13e3a7bf8b7a22b317dd3f708713851/10_DISSERTATION/cyclic_transport_2026_10_24) remains published on the `research/lieb-liniger-response-2026-10-21` branch. It includes bound-state leakage and cutoff errors, and static repulsive Bethe results through N=24. Lieb–Liniger assumes geometry, particles and interaction; it does not derive SEFI ontology.

## Physical interpretation and ongoing work

The inspected SEFI formulations do not yet select a full physical state space, constitutive functions and admissible-state constraints, quantization and normalized observation law with calibrated predictions. These remain research tasks. The energy obstruction informs the worldline/effective-action work; it is not a verdict on every realization or a reason to stop defined field calculations. Mathematical outcomes, including changes of shape, failures and equivalences to existing models, guide the next step.

The research policy is to push completed, checked results, including failures and limitations. Public commits are research records, not claims of peer review, journal acceptance, novelty, or experimental verification.
