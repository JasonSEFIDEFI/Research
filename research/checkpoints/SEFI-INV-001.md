# SEFI-INV-001 — Geometric Inverse Reconstruction — Research Handoff Gate

- **Checkpoint ID:** SEFI-INV-001
- **Created:** 2026-10-25
- **Status:** Exploratory / Not Promoted
- **Approval authority:** Jason Duran Dutton
- **Scope:** Public methodological research gate; no new mathematical or physical result is asserted.
- **Durable reference:** The full Git commit SHA that first introduces this file, recorded in the checkpoint tracking issue. Use that immutable revision when citing this gate; later revisions must retain its history.

## Central mathematical research question

> Can the internal geometry of a physical system be reconstructed from its observable dynamical response without prescribing that geometry in advance?

The guiding programme question remains:

> Can a minimally constrained mathematical structure produce geometry, distinguishable physical entities, and their interactions as emergent properties, rather than requiring those structures to be specified beforehand?

## Scientific motivation and programme relationship

The investigation asks what information measured responses actually contain about a system's internal structure, which geometrical features are identifiable, and which depend on assumptions. Recovering parameters within a prescribed geometric family must be distinguished from deriving geometry itself.

This is a bounded methodological investigation within the GWFM–SEFI–DEFI research programme. The [research portfolio](../../README.md), [research directions](../../Research-Directions.md), and [research status](../../RESEARCH_STATUS.md) provide existing public context. [SEFI-PY](https://github.com/JasonSEFIDEFI/SEFI-PY) is the computational implementation repository; [SEFI-Manuscripts](https://github.com/JasonSEFIDEFI/SEFI-Manuscripts) holds manuscript sources. Programme terminology is research terminology, not evidence of established physical laws. No framework advantage or physical interpretation is assumed.

This gate adds an investigation route without replacing existing priorities, manuscripts, numerical records, negative results, or repository history.

## Proposed mathematical investigation

Specify a forward map F from an admissible system description, probe protocol and nuisance parameters to observables: y = F(g, theta; u) + epsilon. Here g denotes candidate geometric information, theta denotes other dynamical or measurement parameters, u denotes controlled inputs, and epsilon denotes measurement error. This is a proposed formulation, not a derived law.

Before calculation:

1. Define observables, units, governing equations, domain, boundary and initial conditions, measurement operators, noise assumptions, and admissible parameter/state spaces.
2. Inventory every imposed structure: dimension, topology, coordinates, metric family, locality, symmetry, smoothness, embedding and boundary assumptions. Justify each necessary assumption and vary it where possible. Do not impose unnecessary geometric constraints a priori.
3. Define the reconstruction target and its equivalence relation, including coordinate/gauge freedoms and unobservable transformations. Separate intrinsic geometry, embedding geometry, effective propagation geometry and latent representations.
4. Establish or bound uniqueness, nonuniqueness, observability and stability under the actual probe protocol. Construct indistinguishable candidate systems where possible. Account for tradeoffs between geometry, constitutive parameters and measurement calibration.
5. State what could be inferred without a geometric ansatz and what is only recoverable conditional on one. Quantify dependence on priors and regularization.
6. Predeclare error metrics, tolerances, held-out probes and failure conditions before interpreting results. Distinguish local sensitivity from global identifiability.

## Stage 1 — Conventional Baseline

Develop mathematical and computational reference models using established physics, with explicit assumptions and domains of validity.

- Select a bounded, analytically tractable response problem and document its conventional equations and source references.
- Establish direct-solver accuracy and conventional inverse-method performance before adding framework-specific constructions.
- Include known-truth synthetic cases, ambiguous cases, null cases and deliberately misspecified models.
- Compare methods using identical observations, noise realizations, parameter information, tuning budgets and computational accounting.
- Measure recovery error modulo allowed equivalences, predictive error, uncertainty calibration and conditioning.
- Record whether baseline geometry was imposed. Synthetic geometry recovery alone does not demonstrate geometry emergence or physical validation.

**Exit evidence:** defined forward/inverse problem, checked baseline, identifiability analysis and a reproducible evaluation protocol. Exit does not imply research promotion.

## Stage 2 — Geometric Inverse Reconstruction

Investigate whether observable dynamical responses permit reconstruction of underlying geometry.

- Fit only training observations; test predictions on held-out excitations, sensors or response channels.
- Vary probe coverage, noise, resolution, boundaries, parameterization and regularization.
- Return uncertainty or an equivalence class when data do not identify a unique geometry; explicitly report failure to reconstruct.
- Test whether qualitatively different geometries or nongeometric dynamical alternatives explain the same data. A useful representation is not automatically physical geometry.
- Report identifiability limits and counterexamples alongside successes.

**Exit evidence:** bounded reconstruction claim with assumptions, uncertainty, robustness checks and retained negative outcomes.

## Stage 3 — Framework Comparison

Determine whether GWFM, SEFI or DEFI supplies a mathematically justified method, result or prediction beyond conventional approaches.

Derive the proposed mapping from explicit equations; identify all added assumptions and parameters. Test equivalence to established methods, ablate framework-specific terms, and compare on the same baseline protocol. A relabeling, visualization, fitted geometry or passing software test is insufficient to establish novelty or physical advantage. Report equivalence, inferiority and absence of measurable advantage when observed.

**Exit evidence:** justified comparison identifying any incremental result, or a documented null result, with its scope and limitations.

## Stage 4 — Scientific Handoff Review

Assess mathematical validity, reproducibility, consistency with observations, novelty, limitations and falsifiability. Prepare a review package containing definitions, derivations, assumption inventory, source versions, runnable code, data provenance, uncertainty analysis, baseline comparisons, failed cases and unresolved objections. Seek independent checking where feasible and record reviewer concerns and responses.

**Exit evidence:** completed review dossier and a specific promotion recommendation. This stage does not automatically authorize promotion.

## Numerical reproducibility requirements

- Pin source commit SHAs, dependencies, runtime versions, seeds, hardware/precision and complete configurations.
- Supply licensed or otherwise authorized input data, provenance, preprocessing and exact commands from a clean environment to results.
- Save machine-readable outputs, residuals, convergence histories and diagnostics; regenerate figures from those outputs.
- Verify analytic limits, conservation laws where applicable, solver accuracy, discretization/time-step/domain convergence and uncertainty sensitivity.
- Prevent truth-label leakage from synthetic generators into reconstruction. Use independent implementations or analytic checks where practicable.
- Record failed runs, negative results, excluded cases and exclusion reasons. Preserve prior versions.
- Define numerical acceptance thresholds before final comparison. No computations or thresholds are claimed completed by this checkpoint.

## Observational validation requirements

Physical interpretation requires a specified measurement connection: units, calibration, observation law, accessible observables and stated validity regime. Use independent or held-out observational data with documented provenance, uncertainties and selection effects. Separate fitting from prospective or held-out prediction, and compare against conventional alternatives and measurement-system explanations.

Synthetic benchmarks establish only performance within their generator assumptions. Until suitable physical data and an adequate observation model exist, observational validation remains pending; unvalidated SEFI predictions must not be described as established facts.

## Falsification and stopping criteria

For each proposed claim, predeclare a quantitative rejection rule and its applicable regime. At minimum:

- Reject a uniqueness claim if inequivalent admissible geometries produce indistinguishable measured responses within the declared uncertainty.
- Reject a claimed stable reconstruction if perturbations within measurement uncertainty cause errors beyond the declared tolerance.
- Reject predictive adequacy if held-out responses fail the prespecified error or calibration criteria.
- Reject a claimed framework advantage if matched conventional baselines explain the result equally well or better, or the claimed distinction disappears under ablation.
- Reject a claimed geometry derivation if the recovered property was imposed by the ansatz or prior without independent evidential support.
- Withhold physical interpretation when units, governing dynamics, measurement coupling or observational consistency are unresolved.
- Stop promotion when derivations are inconsistent, results are not reproducible, convergence is absent, or contradictions with observations remain unresolved.

A failed bounded claim is a negative result to retain, not a blanket disproof of every framework realization.

## Research promotion criteria and explicit approval

Promotion requires a bounded statement of contribution; checked derivations; justified minimal assumptions; identifiability and nonuniqueness limits; reproducible numerical evidence; fair conventional comparisons; observational support for any physical claim; novelty assessment; explicit limitations and falsification tests; and a completed Stage 4 review dossier.

Label every claim as an established result (with supporting source/proof), a model-dependent finding, or a hypothesis. Do not invent findings or substitute interpretation for evidence.

**Jason Duran Dutton's explicit approval is required before any exploratory result covered by this gate is promoted into formal research.** Record the approval date, exact reviewed commit, approved claims and authorized scope in a versioned promotion record. Approval to publish this methodological checkpoint is not approval to promote results. Passing stages, committing code, closing the tracking issue or completing review does not grant approval.

**Current decision:** Exploratory / Not Promoted. No result is approved for promotion by this document.

## First proposed baseline experiment

Use a conventional linear mass–spring system with response H(omega) = C (K - omega^2 M + i omega D)^(-1) B under explicitly stated mechanical assumptions. Begin with known M, D, B and C; compare full and partial response access, then relax knowledge of nuisance parameters. Investigate which stiffness/connectivity information is identifiable, up to stated equivalences, and construct ambiguous cases. Declare the admissible matrix class and tolerances before simulation.

This is an experimental design proposal only. Mechanical connectivity is a restricted structural surrogate, not a derivation of spatial geometry or spacetime. Numerical execution and all outcomes remain pending.
