# Conditional relativistic spin half target

November 8, 2026. **Exploratory / Not Promoted.**

[Derivation, assumptions and limitations](RELATIVISTIC_COMPLETION.md).

Step 4 now has a consistent conventional free reference: with a selected physical spin-half doublet, assigned positive mass and free relativistic dispersion, a spin-dependent boost correction closes the Poincare algebra. All 45 independent differential-operator commutators and both Casimirs passed exact checks. A finite induced unitary representation supplies the positive-energy realization.

The mass, quantization, sector selection and physical spin assignment have not been derived from SEFI. The original higher-derivative worldline action is unchanged and its energy obstruction remains. This checkpoint does not declare the electron derived by adjoining a known representation.

A conventional local free Dirac-field reference is included with its extra CAR and local-field assumptions. It has positive normal-ordered Fock energy and opposite assigned particle/antiparticle charges. One-particle symmetry alone permits both exchange parities; Fermi statistics is not inferred from the internal doublet alone. The continuum spacelike-support argument is given in the note; finite-mode CAR checks are not a microcausality test.

## Reproduce

Original environment: Python 3.14.7, SymPy 1.14.0, NumPy 2.5.2.

```sh
python -m pip install -r requirements.txt
python check_poincare.py --output fresh_poincare.json
python check_wigner.py --output fresh_wigner.json
python check_dirac_reference.py --output fresh_dirac.json
```

Original results use the corresponding `*_results.json` files. The [protocol](PROTOCOL.md) states assumptions and acceptance criteria.

- `check_poincare.py`: exact differential-operator algebra, mass shell, regular boost coefficient, formal adjoint and Pauli–Lubanski invariants. Formal Hermiticity alone is not a self-adjointness proof; the finite unitary construction is discussed separately.
- `check_wigner.py`: 18 finite boost/composition checks and an independent centered-difference spin-term check. Algebraic errors are below 1.6e-15; the derivative error is below 4.45e-10, within the declared tolerances. Sampling does not prove the group construction.
- `check_dirac_reference.py`: Clifford/projector/isometry/spin sums, four finite CAR modes, positive occupation energies, charge conjugation and both exchange projectors.

The note supplies the invariant-measure/cocycle argument for finite unitarity and the standard spacelike-support argument for the local reference. No interacting or observed-particle calculation is reported.

`source_manifest.json` identifies the prior checkpoint and conventional references. `manifest.json` hashes the supplied files. No prior manuscripts, governing equations, limits or negative results are overwritten.

Jason Duran Dutton leads the programme. Codex assisted with derivation, coding, execution, source checking and drafting. Author verification and independent review are pending. No novelty, electromagnetic coupling, physical mass prediction, electron/positron identification, experimental validation or promotion is claimed. Continue under the [existing research gate](../../checkpoints/SEFI-INV-001.md).
