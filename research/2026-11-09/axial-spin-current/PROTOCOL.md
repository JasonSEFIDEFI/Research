# Axial spin/current checkpoint — pre-calculation scope

9 November 2026. Exploratory / Not Promoted. AI-assisted; no independent review claimed.

Keep the canonical scalar-Maxwell action unchanged. Derive the stationary axial ansatz Phi=exp(-i omega t+i n phi)f(R,z), Sigma=s(R,z), A=a dt+b dphi, and its electric current, stress angular momentum, magnetic moment and coupled Euler equations. State trivial-bundle, regular-axis and infinity assumptions explicitly. Derive total Jz including the electromagnetic contribution and its boundary term; do not equate winding with quantum spin.

Check the local variational equations, stress/current identity and potential inequalities symbolically with SymPy. In the ungauged stationary weak-electric-probe limit derive the gyromagnetic ratio and combine the potential lower bound with the three-dimensional virial identity and energetic binding. Any resulting bound is conditional on existence of the stated stationary solutions and a smooth weak-coupling branch; it does not construct that branch or cover arbitrary strong coupling.

For an independent numerical diagnostic, prescribe the smooth n=1 amplitude f=R exp[-(R^2+z^2)/2], omega=1.4,q=.2. Solve its electrostatic and azimuthal Maxwell equations on the symmetric quadrant 0<R,z<6, using cell-centered finite volumes h=.1 and .05. Use regular-axis/reflection and zero outer potential conditions. Require electric/magnetic residuals below 1e-8 and the total angular-momentum/Gauss cancellation below 1e-9 relative. This is a forced Maxwell problem, NOT a self-consistent scalar soliton. No stability, binding, physical gyromagnetic number or new solution-existence claim follows from the prescribed amplitude.

Assess JMP readiness against official current scope/policies and primary gauged-Q-ball literature. No journal submission, outside correspondence, formal promotion, novelty or successful electron derivation is authorized or claimed.
