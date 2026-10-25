# Research status

Updated 24 October 2026. This repository was renamed from PhD to Research at the author's request. Repository history and existing manuscript status are retained.

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
