# Saved spin/current checkpoint — 9 November 2026

Exploratory / Not Promoted. AI-assisted; not independently reviewed. Work paused here at the author's instruction to update the double-slit repository.

## Completed and checked

`check_axial_algebra.py` and `axial_algebra_results.json` verify eight exact identities: axial scalar/current/Maxwell Euler equations, angular-momentum boundary cancellation, a potential sum-of-squares identity, the regular magnetic-variable transformation and the virial energy identity.

For cylindrical coordinates R,z and regular trivial-bundle ansatz Phi=exp(-i omega t+i n phi)f, Sigma=s, A=a dt+b dphi, define Omega=omega-qa and k=n+qb. The equations are

- Delta_cyl f=[1+f^2+4s^2+k^2/R^2-Omega^2]f.
- Delta_cyl s=[4f^2+lambda s^2-3]s.
- Delta_cyl a=-q Omega f^2.
- b_RR-b_R/R+b_zz=q k f^2.

The physical azimuthal current is j_hat_phi=q k f^2/R. With the regular-axis and decaying-field boundary term vanishing, total Jz=nN, N=integral Omega f^2, Qem=qN. Matter alone has angular density Omega k f^2; electromagnetic angular density is -grad a dot grad b. Their sum integrates to nN. The magnetic moment is mu_z=(q/2) integral k f^2. Nonzero current is possible; spin-half is not thereby derived.

`forced_maxwell.py` solves a prescribed n=1 Gaussian-vortex amplitude's electric and magnetic equations on two finite-volume grids. Both satisfy J=nN to below 6e-16 relative and Maxwell residuals below 6e-14. This is a **forced Maxwell diagnostic, not a self-consistent scalar soliton**, not an existence/stability proof and not an asymptotic dipole measurement. The finite outer potentials are zero.

## Derived conditional weak-probe bound (write-up still pending)

Put t=sqrt(lambda), rho=|Phi|^2, eta=|Sigma|^2. Exactly,

2V-(1+3/t)rho = (rho+t eta-3/t)^2/2+(4-t)rho eta.

For 0<lambda<16 this gives V >= c rho/2, c=1+3/sqrt(lambda). For any nontrivial localized ungauged stationary spinning solution, define I=integral f^2, T=omega^2 I/2, U=integral V, K=one-half total spatial scalar gradient energy (including n^2 f^2/R^2). Dilation gives K+3U-3T=0, hence E=omega N+2K/3 and omega>sqrt(c) for omega>0.

If additionally E<mPhi N, mPhi^2=1+12/lambda, then the infinitesimal-electric-probe gyromagnetic coefficient g0=E/(omega N) obeys

1<g0<mPhi/sqrt(c).

At lambda=12 the upper bound is 1.035276180410083. This is conditional on existence and on a smooth branch approaching the ungauged solution; it is not a theorem about arbitrary finite electromagnetic coupling, a quantum g factor, or a constructed rotating branch. Novelty has not been established. The full proof and assumptions still need a polished write-up.

## JMP assessment so far

The topic fits Journal of Mathematical Physics, but the current package is **not recommended for immediate submission**: a new mathematical contribution of specialist interest has not been established. The numerical correction and familiar J=nN identity alone do not demonstrate novelty. Possible next work is a substantive continuum stability/coercivity theorem or another clearly new, well-checked result, followed by a detailed literature comparison. External review is advisable, not a stated JMP prerequisite for initial submission.

Official sources checked 9 November 2026:

- https://pubs.aip.org/aip/jmp/pages/about
- https://pubs.aip.org/aip/jmp/pages/policies (precise mathematics, new specialist information; prior-submission disclosure)
- https://publishing.aip.org/resources/researchers/author-instructions/ (compiled PDF, author declarations, data availability)
- https://publishing.aip.org/resources/researchers/policies-and-ethics/ai-policy/ (substantive research AI use described in Methods; human author responsibility; AI not an author)
- https://arxiv.org/html/1906.01943v2 (existing spinning gauged FLS solutions and J=nQ in its conventions)

No manuscript has been submitted, no external reviewer contacted and no formal promotion recorded. Ordinary scalar/vector canonical Fock quantization still has a trivial 2pi spatial-rotation action; a physical half-spin map remains missing. Do not confuse this with the earlier conditional internal oscillator doublet or assert a no-go theorem covering all possible topological/quantum extensions.

## Resume next

Finish the axial derivation and conditional weak-probe proposition with explicit boundary assumptions; assess novelty against primary literature. A full rotating scalar-Maxwell solution has not been computed. Current task is switched to the double-slit repository at the user's request.
