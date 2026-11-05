# Existing code and source inventory

Targeted inspection, 4 November 2026. This is not certification of all legacy modules. Revision IDs are in repository_manifest.json and reviewed-source-manifest.json. Repository names and reports indicate where to investigate; only inspected implementations support the specific observations below.

| Component | Existing implementation/evidence | Use and limit for this project |
|---|---|---|
| SEFI-PY `sefi-core/worldline.py` | Inspected parametric trigonometric path scaffold with direction, curvature/torsion scale inputs | Geometry illustration; not an optimizer or full action solver. The docstring explicitly calls it a scaffold. |
| SEFI-PY `core/time_dynamics.py` family | Existing recurrence/phase implementation identified by the prior displacement-recovery audit; local phase manuscript and verification script inspected | Candidate equation-reference code. Not imported into the new isolated benchmark; not a quantum computing resource. |
| Manuscripts `archive/v-drive/Journal Submissions/Time/verify_final_calculations.py` | Inspected RK4 driven-response and DNA energy checks; depends on accompanying Extended_Numerical_Validation.json | Mathematical simulation checks; no energy measurement. Not rerun in isolation without its complete inputs. |
| SEFI-PY Evolution calibration workbench | Inspected measurement-only inference, Jacobian/tangent projection, conventional grid fit/EWMA and seeded synthetic calibration | Reusable observation-versus-truth and held-out evaluation pattern. Its README does not establish a conventional-tracking advantage. No equipment control. |
| SEFI-PY displacement-recovery benchmark | Report inspected; code tree inventoried: bosonic.py, decoders.py, statistics.py, run_benchmark.py, tests and verification | More physically specified quantum-channel benchmark than legacy bit-list demos. Report attributes 560,000 trials and conventional posterior equivalence; historical trials not repeated here. No geometry-specific advantage follows. |
| SEFI-Voxel `phase_compiler.py` | Inspected formula -r·k, modulo 2π | Produces a phase array. Needs propagation/plant model and calibrated inverse map before computing claims. |
| SEFI-Voxel `device_interface.py` | Inspected serial float-frame sender | Communication scaffold; no device-side dynamics, response verification, readback or power measurement shown in this file. |
| SEFI_QEC_Stack `quantum/resource_estimator.py` | Inspected class totaling logical and syndrome counts; estimate_sefi uses fixed 20/5/5 inputs | A bookkeeping stub, not an error-rate-dependent resource estimate or energy model. Other quantum modules require separate evaluation. |
| Legacy SEFI-PY Evolution `benchmark.py` | Inspected local version injects X/Y/Z labels and checks list equality after correction | Classical software reliability demonstration; cannot be treated as entanglement fidelity or hardware QEC evidence. |
| Research Hamiltonian audit | Derivation/report inspected; hamiltonian_audit.py and results identified | Important stated obstruction in one unrestricted worldline realization. Not transferred to the separate fixed-geometry pilot. Symbolic audit not newly rerun here. |
| SEFI-PY localized-field research | Research status and priorities inspected; main-tree and draft PR 6 revisions identified | Separate classical field branch/critical-limit calculations. No demonstrated bridge to a computing architecture. Draft PR remains exploratory. |
| Research Lieb–Liniger branch | Remote tree compared with staged local source blobs | All eleven staged study files match already published branch blobs. No need to duplicate or overwrite the newer remote branch. |
| New `benchmark.py` and `verify.py` | Executed here, independent blocks, algebraic/CG/dynamics comparison, raw repeats, diagnostics and checks | Small justified computing pilot only. No legacy dependencies, new physics claim or hardware control. |

## Repository state reviewed

- SEFI-PY main: `847a071351ed2b1c54e240fd9a520a1cce238178`.
- Research main before this package: `86686396a7612f4b80c7225798db48af519353b6`.
- SEFI-Manuscripts main before synchronization: `72ca952eaddf608b006ebaaa4615a422e0532ff9`.
- SEFI_QEC_Stack: `7be66ac5d3e487196121dec136c3136ee5246963`.
- SEFI-Voxel: `f8737ca47620e4c9c5143e6baa8ca301bbaa8b7d`.
- Publishing-V-Drive-Content: `e9bea5800e20cc04f10449e9e874235d089db98c`.
- SEFI-PY draft PR 6 head: `18a5275df36d32af1b67d514c0c337637ff2c210`.
- Research correlation branch head: `6e77ff32c13e3a7bf8b7a22b317dd3f708713851`.

The newer October 29 GWFM source was found locally and differs from GitHub main's older GWFM source. Source/version synchronization is therefore necessary alongside this new pilot. Conversion notes and original claims are preserved; archiving does not scientifically endorse the manuscripts.

## Build next only when justified

Missing reusable components are a selected physical plant model, programmable signed coupler constraints, calibrated noise and readout, complete energy ledger, controlled interconnected problem mapping and a real workload dataset. Existing diagrams, serial output, nominal qubit totals and stable trajectories do not substitute for these components. The initial implementation plan and stage gates are in RESEARCH_BRIEF.md and PROTOCOL.md.
