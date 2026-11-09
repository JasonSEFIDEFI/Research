# One quantum selection and the physical rotation bridge

November 8, 2026. **Exploratory / Not Promoted.**

This continues steps 2 and 3 of the electron-identification programme without changing the preceding fixed-geometry internal example.

- [Sector selection](SECTOR_SELECTION.md): conservation preserves every N sector, not only N=1. A min-max trial bound proves a competing rest-sector excitation below the dark doublet in the existing sine example. The rigorous gap bound is below 21301/21380, while the dark-pair gap is exactly 1 in the stated units. Independent basis calculations estimate the competing gap as 0.9537928882.
- [Rotation lift](ROTATION_LIFT.md): the product symmetry admits both original scalar and chosen diagonal rotation actions. Their central signs differ. The action does not select the diagonal assignment, and leaving the original boosts unchanged fails its Lorentz algebra. A physical rotation/boost map remains missing.
- [Protocol](PROTOCOL.md): parameters, trial coefficients, numerical basis sizes and acceptance thresholds were fixed before evaluation. No experimental inputs or fitted electron parameters were used.

An explicit U(1) multiplier construction is discussed only to show what an imposed N=1 constraint would add. It is not adopted as a new governing model, and its level is not derived by the existing action. The earlier exact internal symmetry remains valid; a lower rest excitation does not imply decay from a strictly conserved N=1 sector.

## Reproduce

Original environment: Python 3.14.7, NumPy 2.5.2, SciPy 1.18.1, SymPy 1.14.0.

```sh
python -m pip install -r requirements.txt
python check_sector_selection.py --output-dir fresh_results
python check_rotation_lift.py --output fresh_rotation_results.json
```

The scripts fail on violated assertions. Preserved records are `sector_selection_results.json`, `rotation_lift_results.json` and `basis_convergence.csv`. Checks include exact trial arithmetic, strict rational inequalities, oscillator matrix entries against independent quadrature, six nested basis sizes, residuals/parities, two rotation representations, their Casimirs and an algebraic unchanged-boost mismatch.

The spectrum calculation uses exact infinite-basis sine matrix elements before projection. Finite-matrix residuals and convergence are not certified continuum error bounds; the separate analytic argument proves the ordering. Matrix calculations are internal quantum mechanics with quantization assumed, not a relativistic particle or physical matter simulation.

`source_manifest.json` pins the preceding model and links the conventional mathematical references. `manifest.json` hashes the directory files. Existing source manuscripts, governing action and historical results remain unchanged.

Jason Duran Dutton leads the programme. Codex assisted with protocol, derivation, source checking, implementation, execution and drafting. Author verification and independent technical review remain pending. No novelty, spin-statistics derivation, physical mass or electric-charge prediction, observed-particle identification, experimental validation or promotion approval is claimed. The [existing gate](../../checkpoints/SEFI-INV-001.md) remains in force.
