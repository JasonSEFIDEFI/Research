# Does the exact internal symmetry select the one quantum doublet

November 8, 2026. Exploratory / Not Promoted. First-party mathematical analysis with substantive Codex assistance; independent technical review pending.

## Result

After canonical bosonic quantization, the exactly decoupled internal oscillator pair has invariant fixed-number sectors. Its N=1 sector is an internal SU(2) doublet. The same Hamiltonian also permits N=0,2,3 and all higher sectors; conservation does not select one of them.

For the fixed-geometry sine-coupling example constructed in the preceding checkpoint, the N=1 doublet is not even the lowest nonvacuum excitation of the full internal system. A variational proof gives a competing rest-sector excitation gap strictly below 21301/21380, which is less than the dark-pair gap 1. A separately converged product-basis calculation estimates that competing gap as 0.9537928882. The proof, rather than that estimate, establishes the strict ordering.

This is a model-specific negative result to retain. It does not destroy the exact symmetry or show that an already prepared N=1 state decays under the separated Hamiltonian. It shows that symmetry, positivity and lowest-excitation language do not by themselves select this proposed doublet.

## 1 Fixed model and assumptions

Use the same dimensionless canonical units and fixed geometry as the previous nonlinear example. Canonical quantization and hbar=1 are assumptions. No coupling is fitted or changed:

\[
H=H_{OD}\otimes1+1\otimes H_{AB},\qquad
H_{OD}=N+1,
\]

\[
H_{AB}=\frac{p_A^2+p_B^2}{2}+2A^2+\frac{B^2}{2}
+R\sin(A)B,\quad R=\frac{\sqrt{13}}6.
\]

The coordinate scale implicit in sin(A) is fixed by the preceding dimensionless-unit convention. This is a quantum mechanical internal system, not a relativistic quantum field theory. The preceding coercivity argument gives a confining smooth real potential; use the corresponding semibounded Schroedinger operator on L2(R2) and its Friedrichs realization. Product Hermite functions lie in its form domain, so the trial spaces below are admissible. The spectrum is discrete.

## 2 Invariance is not selection

The Hilbert space decomposes into mutually orthogonal sectors

\[
\mathcal H=\bigoplus_{N=0}^\infty
\left(\mathbb C^{N+1}\otimes\mathcal H_{AB}\right),
\quad E_{N,r}=N+1+\varepsilon_r.
\]

The internal SU(2) label is j=N/2. Every sector projector P_N commutes with H. For a density matrix evolving by this Hamiltonian,

\[
\frac{d}{dt}\operatorname{Tr}(P_N\rho)
=-i\operatorname{Tr}([P_N,H]\rho)=0.
\]

Thus the model preserves whatever sector populations are initially present. It does not drive arbitrary states into N=1. This argument applies to both exact separated pairs identified in the previous calculation, including explicitly time-dependent rest dynamics that still commutes with N.

The internal ground sector is N=0. Selecting the lowest nonzero value of N is a statement about a chosen observable or initial constraint, not a consequence of energy minimization over all states.

## 3 Rigorous lower bound on the rest ground energy

For each fixed A, the B oscillator is a translated harmonic oscillator:

\[
\frac{p_B^2}{2}+\frac{B^2}{2}+R\sin(A)B
=\frac{p_B^2}{2}+\frac{(B+R\sin A)^2}{2}
-\frac{R^2\sin^2 A}{2}.
\]

Its quadratic-form lower bound is 1/2 minus R squared sin(A) squared divided by 2. Integrating that fiberwise inequality over A does not transform p_A or discard a derivative term. It gives

\[
H_{AB}\geq\frac{p_A^2}{2}+2A^2+\frac12
-\frac{R^2}{2}\sin^2 A
\geq\frac{p_A^2}{2}+\frac{4-R^2}{2}A^2+\frac12.
\]

Consequently

\[
\varepsilon_0\geq L=\frac12+\frac{\sqrt{131}}{12}
\simeq1.4537935952.
\]

The last inequality uses sin(A) squared<=A squared globally. It does not approximate the sine potential by its Taylor expansion.

## 4 A fixed trial space bounding the first rest excitation

Use unperturbed oscillator states |n_A,n_B> with frequencies 2 and 1. Their uncoupled energies are 2 n_A+n_B+3/2. Fix the trial coefficients before spectral evaluation:

\[
|\psi\rangle=|0,1\rangle-\frac3{16}|1,0\rangle
-\frac3{32}|1,2\rangle,
\qquad \|\psi\|^2=\frac{1069}{1024}.
\]

The exact relevant interaction matrix entries are

\[
a=\langle0,1|R\sin(A)B|1,0\rangle
=\frac{\sqrt{26}}{24}e^{-1/8},
\]
\[
b=\langle0,1|R\sin(A)B|1,2\rangle
=\frac{\sqrt{13}}{12}e^{-1/8}.
\]

They follow from <0|sin A|1>=e^(-1/8)/2 for the frequency-2 A oscillator and the frequency-1 B matrix elements 1/sqrt(2) and 1. All other offdiagonal entries among these three states vanish by parity or oscillator selection.

The Rayleigh quotient is

\[
E_\psi=
\frac{5471-32e^{-1/8}(\sqrt{26}+\sqrt{13})}{2138}
\simeq2.4439587389.
\]

Take the two-dimensional trial space spanned by |0,0> and psi. The Hamiltonian preserves joint inversion (A,B)->(-A,-B). The first vector is even and psi is odd, so their Hamiltonian cross term vanishes exactly. The two trial eigenvalues are 3/2 and E_psi. The min-max principle therefore gives

\[
\varepsilon_1\leq\max(3/2,E_\psi).
\]

For a strict inequality independent of floating-point evaluation, use

\[
e^{-1/8}>7/8,\quad \sqrt{26}>5,\quad
\sqrt{13}>18/5,\quad\sqrt{131}>57/5.
\]

The exponential inequality follows from exp(-x)>1-x for positive x; the square-root inequalities follow by squaring positive rationals. They imply

\[
\varepsilon_1<\frac{26151}{10690},\qquad
\varepsilon_0>\frac{29}{20},
\]

and hence

\[
\boxed{\varepsilon_1-\varepsilon_0
<\frac{21301}{21380}<1.}
\]

This proves that a rest-sector excitation with N=0 lies below the first dark-pair N=1 doublet, whose exact gap is 1. It does not require identifying the parity or precise value of the true first excited state.

## 5 Independent numerical calculation

The script constructs projected oscillator-basis matrices of the full sine interaction. For the A oscillator, write A=(a+a dagger)/2. Infinite-basis matrix elements of exp(i A) use eta=1/2:

\[
\langle m|e^{iA}|n\rangle=
e^{-\eta^2/2}\sqrt{\frac{\min(m,n)!}{\max(m,n)!}}
(i\eta)^{|m-n|}L_{\min(m,n)}^{|m-n|}(\eta^2).
\]

The imaginary part gives the real symmetric sine matrix. Using exact projected entries avoids replacing the operator by sin of a finite truncated position matrix. Low-order entries were checked against independent 128-point Gauss–Hermite integration; the maximum difference was approximately 1.92e-15.

The product bases contain 8,12,18,26,36 and 48 states per coordinate, reaching 2304 dimensions. The lowest six Ritz values were checked for nested-basis monotonicity, parity and finite-matrix eigenpair residuals. The largest change among the six values between the last two bases was approximately 1.78e-14, below the declared 1e-8 target.

The estimated gap is 0.9537928882466689. Differences of Ritz upper bounds are not rigorous continuum gap bounds; the separate analytic argument establishes the ordering. Full convergence data and residuals are in `basis_convergence.csv` and `sector_selection_results.json`. The protocol fixes parameters, trial coefficients and acceptance thresholds before the numerical evaluation.

## 6 What a sector selection rule would add

The following possibilities are distinct and must not be silently substituted for a derivation:

| Proposed rule | Mathematical effect | Status in the current model |
|---|---|---|
| Prepare N=1 initially | Exact separated Hamiltonian preserves the doublet | A choice of state, not universal selection |
| Restrict to odd N | The lowest dark sector becomes N=1 | The odd-sector restriction is additional; the Hamiltonian allows even sectors |
| Introduce a worldline U(1) multiplier imposing N=k | Selects a fixed quantum sector of dimension k+1 in a specified ordering convention | A new constraint/gauge structure; k=1 is not selected by the original action |
| Add a relaxation or environmental mechanism | Could change sector populations and favor a state | Requires additional dynamics and checks; absent here |

For clarity, in hbar=1 units a possible explicit extension uses canonical complex oscillator variables z and a real multiplier a(t):

\[
L=\frac{i}{2}(z^\dagger\dot z-\dot z^\dagger z)
-\omega z^\dagger z-a(z^\dagger z-k).
\]

Under z->exp(-i theta)z and a->a+theta-dot, L changes by k theta-dot. Varying a imposes the new constraint. With a compact U(1), single-valued large-gauge phases require integer level k. In a normal-ordered bosonic quantization convention the physical states obey (N-hat-k)|physical>=0. Level k=1 gives a doublet, but all allowed nonnegative integer levels remain possible; the action is not a derivation of why k=1 is physical. Ordering shifts must be stated rather than hidden in k.

This first-order extension is displayed to expose the exact additional assumption. It is not installed as a governing SEFI equation by this checkpoint. The existing global internal symmetry does not itself authorize promotion to a local gauge constraint.

## 7 Consequence for the route to matter

The current exact internal model does not select the desired one-quantum sector. The competing-state result also prevents describing the N=1 doublet as the model's automatically preferred lowest excitation. A proposed physical selection mechanism must be independently justified or clearly declared as a model extension.

Even a justified N=1 restriction would leave the physical spatial rotation action, relativistic dynamics, exchange statistics, electromagnetic charge and observed-particle comparison unresolved. The next bounded investigation is whether the available exact product symmetries admit a consistent physical rotation lift and whether the existing action selects that lift. Merely choosing the internal SU(2) to represent spatial spin would be an extra identification, not a consequence of the spectral calculation.

## Sources and attribution

The model and unit conventions are taken unchanged from [the preceding exact internal-symmetry checkpoint](../full-internal-symmetry/FULL_INTERNAL_SYMMETRY.md), pinned at Research commit `8c10ff4da342c64502de801f2613ea7245c6c785`. Its source manifest identifies the foundations action.

Standard oscillator matrix-element methods are described by J. L. Lopez-Bonilla and G. Ovando, [Matrix Elements for the One-Dimensional Harmonic Oscillator](https://www.irishmathsoc.org/bull44/oscillator.pdf), IMS Bulletin 44 (2000), pp. 61–65. The variational construction and strict inequalities used here are written out above. No novelty is claimed for the min-max principle, oscillator representation or their application.

Codex assisted with the protocol, derivation, code, execution, source checking and drafting. Author verification and independent technical review remain pending. No particle derivation, physical unit calibration, experimental result, journal submission or promotion approval is claimed.
