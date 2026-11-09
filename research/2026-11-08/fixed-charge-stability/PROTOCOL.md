# Step 6a: fixed charge and constrained radial energy

Exploratory / Not Promoted. AI-assisted, 2026-11-08.

Before numerical execution: use the preceding scalar-Maxwell action, lambda=12, and fixed continuous charge number N=1250.1753361265248. For each q, Qem=qN is constant under perturbations; comparing different q holds N, not the numerical value of Qem, fixed. Follow q=0,.0025,.005,.01,.015,.02,.03,.04,.05 with omega unknown, stopping at a rejected nontrivial solution. Use R=120, tolerance 1e-7, 801 initial nodes, max 30000 nodes. Repeat q=.01 at R=160, tolerance 2e-8, and require relative energy and omega agreement below 1e-5, charge and Gauss errors below 1e-5. Do not infer a charge limit from a failed continuation.

Derive the static fixed-N energy by eliminating the electrostatic field with Gauss' law. If feasible, evaluate its radial real-amplitude Hessian, keeping the nonlocal electrostatic response and fixed-N rank-one term. Use radial transformed perturbations r delta f,r delta s with Dirichlet endpoints on R=80 at h=.2,.1,.05; check q=0 and q=.01, compare at R=120,h=.1. Numerical low eigenvalues are diagnostics, not a proof of the full dynamical or three-dimensional spectrum. The neutral phase and magnetic/transverse perturbations are outside this initial Hessian restriction. Record failed runs and limitations.
