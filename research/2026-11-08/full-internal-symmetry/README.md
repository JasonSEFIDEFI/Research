# Exact symmetry of the coupled internal Hamiltonian

November 8, 2026. **Exploratory / Not Promoted.**

[Full derivation and assumptions](FULL_INTERNAL_SYMMETRY.md).

## Completed calculation

The complete internal potential, including the two constitutive coupling functions and geometry factors, has been retained. Exact Poisson brackets give a necessary-and-sufficient criterion for a fixed canonical oscillator SU(2) pair. The six coordinate-aligned pairs are classified under fixed prescribed geometry and under arbitrary independent geometry factors.

Two positive cases are retained:

- An Origin–Authorship pair with equal frequencies and constant constitutive functions is an exact internal symmetry for arbitrary worldline geometry. Its geometry-independent generators also give canonical symmetries of the joint first-order variational action, up to a boundary term.
- A rotated Sovereignty–Warp mode decouples from a common nonlinear coupling when its forcing direction is fixed and the appropriate frequencies coincide. Pairing this mode with Origin gives an exact internal SU(2), not just a linearized degeneracy. The notes supply a bounded sine-coupling example, global coercivity argument and positive internal equilibrium Hessian. Rotation of the forcing direction supplies an explicit symmetry-breaking term.

The second case extends the preceding audit, whose coordinate-aligned tests did not cover this rotated nonlinear sector. It remains a conditional internal construction, not spatial spin or an electron. Prescribed-geometry internal stability is not stability or positive energy of the full higher-derivative worldline system. An N=1 sector is invariant after canonical quantization of an exactly separated pair, but its physical selection is not derived.

## Reproduction

Python 3.14.7, SymPy 1.14.0:

```sh
python -m pip install -r requirements.txt
python check_full_symmetry.py --output fresh_symmetry_results.json
```

`full_symmetry_results.json` preserves the original run. The script asserts the general criterion, exact coupling-dependent generator rates, all six sufficient pair cases with arbitrary smooth remaining functions, affine shifts and their time-dependent failure, dark-mode canonical decomposition and Poisson algebra, conserved oscillator number, potential square completion, the example Hessian and moving-frame breaking. The continuum algebra and coercivity arguments are given explicitly in the note; no particle simulation or experimental result is reported.

`source_manifest.json` and `source_excerpt.md` identify the original action. `manifest.json` hashes the supplied files. The source manuscripts and prior results are unchanged.

Jason Duran Dutton leads the programme. Codex assisted with derivation, source checking, implementation, execution and drafting. Standard Hamiltonian methods and their application are not claimed as a new general theorem. Independent technical review and author verification are pending. No spin-statistics, electromagnetic charge, electron/positron, physical-matter or promotion claim is made. The [existing research gate](../../checkpoints/SEFI-INV-001.md) remains in force.
