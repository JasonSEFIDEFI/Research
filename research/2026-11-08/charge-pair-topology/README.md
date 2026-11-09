# Canonical scalar charge pairing and fixed charge topology

November 8, 2026. **Exploratory / Not Promoted.**

This checkpoint continues the existing two-complex-scalar localized-field research. It does not modify the governing action or claim that SEFI has derived an electron, positron, or physical matter.

## Mathematical findings

- [Charge conjugation](CHARGE_CONJUGATION.md): exact energy-even, charge-odd conjugation symmetry; vacuum mass Hessian; spherical angular momentum; constraints on a proposed electromagnetic extension.
- [Fixed charge topology](FIXED_CHARGE_TOPOLOGY.md): a charge-preserving deformation retraction and explicit Hilbert-space contraction show that a stated regular fixed-nonzero-charge phase space is contractible. Its global Phi phase quotient is simply connected. These spaces therefore do not support a nontrivial flat rotation-loop sign by the Finkelstein–Rubinstein route.
- The fixed-charge argument explicitly adds an L1 condition to Sigma momentum so its charge over a nonzero vacuum is defined. It does not claim invariance of that condition under evolution, contractibility of bound-energy sublevels, or a classification of other infrared/gauge completions.

These are first-party derivations using standard symmetry and topology. No independent novelty, complete quantum theory, or physical validation is asserted. A topological obstruction for one construction is not a prohibition of every emergent-fermion model.

## Reproduction

Original execution: Python 3.14.7, NumPy 2.5.2, SymPy 1.14.0. Use a fresh environment and this directory as the working directory:

```sh
python -m pip install -r requirements.txt
python check_charge_conjugation.py --output fresh_charge_results.json
python check_fixed_charge.py --output fresh_fixed_charge_results.json
```

The scripts fail on violated assertions. `charge_conjugation_results.json` and `fixed_charge_results.json` preserve the original execution records; use new output filenames for further runs. They contain symbolic checks and finite-mode numerical consistency checks, not three-dimensional soliton evolutions or numerical proofs of continuum topology. The detailed arguments and their assumptions are in the notes.

For the fixed-charge sample, charges +/-1 and +/-1000 use a declared 1e-12 acceptance tolerance. The maximum normalized charge error was about 2.73e-15, the kinetic identity error about 9.42e-16, and there was no sampled increase in kinetic energy during momentum retraction. These numbers are normalization checks, not electron predictions.

`source_manifest.json` preserves two public source texts with repository commits and Git blob IDs. `manifest.json` hashes the files in this directory. Later references and standard mathematical comparisons are linked in the notes. No ELP, student record, personal correspondence, secret, or private employment document is included.

## Next work

Audit whether the underlying SEFI identity variables require a target or constraint absent from the canonical scalar approximation. Any change of target, admissible states, gauge structure or quantization must be derived or explicitly labeled an extension. Do not infer spin-half from two charge signs, a chosen winding number or a relabeled complex scalar.

Jason Duran Dutton leads the research programme. Codex assisted with derivation, code, execution, source checking and drafting. Author verification, independent technical review and broader novelty assessment remain outstanding. This commit records exploratory work; it does not approve promotion under [SEFI-INV-001](../../checkpoints/SEFI-INV-001.md).
