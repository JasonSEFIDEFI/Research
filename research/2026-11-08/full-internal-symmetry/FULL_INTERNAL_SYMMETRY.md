# Exact internal oscillator symmetry with the identity geometry couplings retained

November 8, 2026. Exploratory / Not Promoted. Working derivation with substantive Codex assistance; author verification and independent technical review remain pending.

## Main result

There are exact internal SU(2) sectors in specified specializations of the existing foundations action. They are not restricted to a quadratic approximation:

1. **Origin–Authorship:** constant constitutive functions and equal Origin and Authorship frequencies give an exact decoupled oscillator pair even when the worldline geometry varies arbitrarily. The corresponding internal canonical transformations are symmetries of the joint action with geometry held unchanged by the transformation.
2. **Origin plus a rotated Sovereignty–Warp mode:** equal O/S/W frequencies and a common functional dependence of the two couplings yield an exact decoupled mode when their geometric forcing direction is fixed. Its pair with Origin has conserved SU(2) generators even if the other internal coupling is nonlinear. An explicit bounded sine-coupling example has a positive potential Hessian at its equilibrium and a globally bounded-below internal Hamiltonian on fixed geometry.

The second construction was not covered by the earlier coordinate-pair degeneracy table. It supplies a concrete nonlinear candidate to retain. Generic variation of the geometric forcing direction breaks these fixed dark-mode generators. Neither construction identifies the internal group with spatial spin, derives quantization, selects N=1, or establishes an electron.

## 1 Starting action and meaning of full internal Hamiltonian

The foundations source is fixed to SEFI-Manuscripts commit `6311562792bf9bd16ec278a669b4afe64ffedbc4`, file `research-updates/2026-10-18/theory-foundations/foundations.tex`, blob `d56be35e33eb0baa8cb66e2b0dcb2e8fc188cd6c`.

Its proper-time internal potential is

\[
V=\frac12\sum_a k_a I_a^2+
\kappa^2\mu_1(I_A)I_S+\tau_1^2\mu_2(I_A)I_W,
\qquad h_a,k_a>0.
\]

The canonical internal momenta are pi_a=h_a D_s I_a. Use the constant canonical mass normalization

\[
x_a=\sqrt{h_a}I_a,\quad p_a=\pi_a/\sqrt{h_a},\quad
\Omega_a^2=k_a/h_a.
\]

Put K=kappa squared, T=tau_1 squared and define

\[
f(A)=\mu_1(A/\sqrt{h_A})/\sqrt{h_S},\quad
g(A)=\mu_2(A/\sqrt{h_A})/\sqrt{h_W}.
\]

Here O,A,S,W denote the normalized x coordinates. The full internal Hamiltonian, before any Taylor expansion, is

\[
H_I=\frac12\sum_a(p_a^2+\Omega_a^2x_a^2)
+K f(A)S+T g(A)W.
\]

K and T can be prescribed functions of proper time or evaluated on a dynamical worldline. This calculation retains both coupling functions exactly. It is not a construction of the constrained reduced Hamiltonian of the higher-derivative worldline geometry, and it does not repair that sector's previously identified energy obstruction.

## 2 Exact criterion for the fixed canonical oscillator SU(2) family

Select two canonical coordinate-momentum pairs (x_i,p_i),(x_j,p_j), a positive reference frequency omega, and geometry-independent constant centers c_i,c_j. Let q_i=x_i-c_i and q_j=x_j-c_j. Define

\[
J_x=\frac{\omega q_iq_j+p_ip_j/\omega}{2},\quad
J_y=\frac{q_ip_j-p_iq_j}{2},
\]
\[
J_z=\frac{\omega q_i^2+p_i^2/\omega-\omega q_j^2-p_j^2/\omega}{4}.
\]

For a natural Hamiltonian H=sum p_a squared/2+V(x),

\[
\{J_z,H\}=\frac1{2\omega}
\left[p_i(\omega^2q_i-\partial_iV)
-p_j(\omega^2q_j-\partial_jV)\right].
\]

Because p_i and p_j are independent, its vanishing as a phase-space identity is equivalent to

\[
\partial_iV=\omega^2q_i,\qquad
\partial_jV=\omega^2q_j.
\]

On a connected coordinate domain, this integrates to

\[
V=\frac{\omega^2}{2}(q_i^2+q_j^2)+V_{\rm rest},
\]

with V_rest independent of the selected coordinates. This condition also makes J_x and J_y commute with H. Thus it is necessary and sufficient for this fixed oscillator SU(2) family. The resulting pair is exactly decoupled and harmonic, even when V_rest is nonlinear.

This theorem can also be applied after a constant orthogonal rotation of the mass-normalized coordinates and momenta. It does not classify arbitrary nonlinear canonical generators, time-dependent dynamical invariants or transformations that also move the worldline.

## 3 Exact Origin–Authorship brackets

For Omega_O=Omega_A=omega and unshifted O,A, write

\[
\mathcal D=K f'(A)S+T g'(A)W.
\]

Direct calculation gives

\[
\dot J_x=-\frac{p_O\mathcal D}{2\omega},\qquad
\dot J_y=-\frac{O\mathcal D}{2},\qquad
\dot J_z=\frac{p_A\mathcal D}{2\omega}.
\]

For arbitrary independent nonzero K,T and unrestricted S,W, all three vanish identically if and only if f and g are constant. A linear Authorship dependence already breaks these generators: f=c_1+A gives nonzero rates proportional to K S. A quadratic dependence f=A squared produces the corresponding exact nonlinear breaking terms. Equal bare frequencies do not remove them.

Conversely f=c_1 and g=c_2 leave the entire O,A pair autonomous:

\[
H_I=\omega N_{OA}+H_{SW},\qquad
N_{OA}=\frac{\omega(O^2+A^2)+(p_O^2+p_A^2)/\omega}{2}.
\]

K and T may vary: their forces occur only in H_SW. This is an admissible constitutive specialization of the source, not a property forced by the layer definitions. Authorship no longer modulates the coupling in this specialization.

## 4 Coordinate-aligned pair classification

Every row also requires equal bare frequencies for the selected pair. Functions are considered on a connected domain. The fixed-geometry column assumes constant nonzero K,T; its affine equilibrium shifts are allowed. The arbitrary-geometry column requires fixed generators and arbitrary independent K,T.

| Pair | Fixed prescribed geometry, with constant shifts | Arbitrary independent geometry, fixed generators |
|---|---|---|
| O,A | f and g constant | f and g constant |
| O,S | f constant; g arbitrary | f=0; g arbitrary |
| O,W | g constant; f arbitrary | g=0; f arbitrary |
| A,S | f and g constant | f=0; g constant |
| A,W | f and g constant | g=0; f constant |
| S,W | f and g constant | f=g=0 |

In the fixed-geometry column, S*= -K f/ Omega_S squared and W*= -T g/Omega_W squared wherever the corresponding function must be constant. O*=A*=0. The exact criterion in section 2 proves necessity and sufficiency in this coordinate-aligned fixed-center family.

If K or T vanishes identically, conditions on its absent coupling relax. Geometries with a prescribed relation between K and T are a separate restricted class, treated below. The table does not exclude a symmetry after a rotation of coordinates; indeed the following construction supplies one.

## 5 A nonlinear rotated mode that decouples exactly

Assume

\[
\Omega_O=\Omega_S=\Omega_W=\omega,
\quad f(A)=\alpha F(A),\quad g(A)=\beta F(A),
\]

where F is any sufficiently smooth function. On fixed geometry, put u=K alpha, v=T beta, R=sqrt(u squared+v squared)>0 and make the canonical rotation

\[
B=\frac{uS+vW}{R},\qquad
D=\frac{-vS+uW}{R},
\]

with the same rotation of (p_S,p_W) to (p_B,p_D). Then

\[
Kf(A)S+Tg(A)W=R F(A)B.
\]

Equal S,W frequencies make their kinetic and quadratic potential terms invariant under this rotation. Therefore the exact Hamiltonian is

\[
H_I=\underbrace{\frac{p_O^2+p_D^2}{2}
+\frac{\omega^2(O^2+D^2)}2}_{H_{OD}}
+\underbrace{\frac{p_A^2+p_B^2}{2}
+\frac{\Omega_A^2 A^2+\omega^2 B^2}{2}
+R F(A)B}_{H_{AB}}.
\]

The mode D is dark to this internal forcing. Its pair with Origin satisfies

\[
\{J_i^{OD},H_I\}=0,\qquad
\{N_{OD},H_I\}=0
\]

for arbitrary F, with no small-amplitude expansion. This remains true even when f' and g' are nonzero: the protected candidate uses a rotated mode, not an individual S or W label. It is consistent with the earlier simple ASW Hessian spectrum: D is one ASW mode, and its degeneracy is with the independently decoupled Origin mode.

If u(s),v(s) change by a common scale factor while their direction is fixed, the same constant rotation applies, and H_AB can depend on time without affecting these O,D generators. This corresponds to a restricted fixed-ratio class of geometries when alpha,beta are nonzero. The source action does not itself establish that this geometry relation is dynamically invariant.

## 6 A globally controlled nonlinear internal example

Nonlinear coupling can make a potential unbounded below, so a conserved algebra is not enough. Complete the square exactly:

\[
V=\frac{\omega^2}{2}
\left[O^2+D^2+\left(B+\frac{R F(A)}{\omega^2}\right)^2\right]
+\frac{\Omega_A^2 A^2}{2}
-\frac{R^2F(A)^2}{2\omega^2}.
\]

If F(0)=0, |F(A)|<=L|A|, and

\[
\Omega_A^2>\frac{R^2L^2}{\omega^2},
\]

this controls the A coordinate as well as the completed squares. The potential is coercive in the internal coordinates and has its unique global minimum at O=A=B=D=0. The positive margin together with the square term controls B because its shift grows at most linearly in A. The internal equilibrium is Lyapunov stable by conservation of the autonomous internal energy. This is not attraction or a stability theorem for the coupled worldline geometry.

For an explicit example, first choose a fixed proper-time unit and the corresponding canonical coordinate units. In these dimensionless numerical units choose

\[
\omega=1,\quad \Omega_A^2=4,\quad
u=\frac12,\quad v=\frac13,\quad F(A)=\sin A.
\]

Dimensionally, the sine family can be written F(A)=A_0 sin(A/A_0) with a specified coordinate scale A_0; the displayed example uses A_0=1 in the chosen unit. No dimensionful quantity is inserted into a sine without that convention. Then R squared=13/36, and |sin A|<=|A| gives the strict margin 4-13/36=131/36. The equilibrium Hessian in coordinates (O,A,B,D) is

\[
\begin{pmatrix}
1&0&0&0\\
0&4&\sqrt{13}/6&0\\
0&\sqrt{13}/6&1&0\\
0&0&0&1
\end{pmatrix}.
\]

All leading principal minors are positive. Thus this is an explicit bounded nonlinear internal system with an exact O,D oscillator SU(2), on the stated fixed geometry. These parameter choices demonstrate existence within the allowed family; they are not measured values, selected fundamental constants, or evidence for electrons.

## 7 Changing forcing direction is an exact breaking mechanism

Let theta(s)=atan2(v(s),u(s)). An instantaneous bright/dark rotation with changing theta is time dependent. Its transformed canonical Hamiltonian contains the extra term

\[
H_{\rm frame}=-\dot\theta\,(B p_D-D p_B).
\]

This term couples the dark and bright modes. The exact brackets of the O,D generators with it are recorded in the check results and are not identically zero. Consequently an instantaneous diagonalization alone does not establish conservation. Fixed direction sets theta-dot=0 and removes this particular breaking term.

Similarly, shifting a coordinate by the instantaneous equilibrium of a forced oscillator introduces explicit proper-time dependence into its generators. The check script exhibits nonzero rates proportional to K-dot for an O,S pair. Time-dependent invariants built using a separately solved particular trajectory may exist, but they are not the fixed geometry-independent symmetry classified here.

## 8 Relation to symmetry of the joint action

For a generator G independent of geometry and of the curve parameter, use the first-order internal form of the original action in any parameter lambda:

\[
S=\int d\lambda\left[\sum_a\pi_a I_a'
-v_{\rm WL}(m+H_I(I,\pi;\kappa,\tau_1))\right].
\]

Here v_WL is the proper-time measure factor, not the forcing component v used above. Variation of pi recovers the original internal kinetic term. Under an internal canonical transformation generated by G, with the worldline unchanged,

\[
\delta\left(\sum\pi I'\right)
=\frac{d}{d\lambda}\left(\sum\pi_a\partial_{\pi_a}G-G\right).
\]

If {G,H_I}=0 for every geometric jet, the rest of the variation vanishes and the action changes only by that boundary term. The arbitrary-geometry cases in section 4, in particular the constant-coupling O,A pair, therefore extend to generalized internal canonical symmetries of the joint variational system. No illegitimate fixing of proper-time speed before worldline variation is required.

The fixed-geometry dark-mode result is not automatically such a universal symmetry: its rotation coefficients depend on geometry, and changing that geometry produces the explicit terms in section 7. A claimed symmetry of a restricted worldline class would need proof that the class is preserved by the coupled equations and transformations.

## 9 What this resolves for the electron programme

Step 1 has a conditional positive answer: there are exact internally conserved SU(2) sectors, including a nonlinear dark-mode example. It also has explicit failure conditions and a stated boundary between prescribed geometry and a symmetry of the joint action.

Canonical bosonic quantization of either exactly decoupled pair gives the conventional Schwinger construction. Its number operator commutes with the separated Hamiltonian, so an initially chosen N=1 sector stays invariant in that quantized specialization. This establishes invariance conditional on quantization; it does not explain why nature selects N=1 rather than other sectors. The spatial rotation action, relativistic quantum dynamics, fermionic exchange statistics, electromagnetic coupling and physical mass scale remain separate unresolved requirements.

The dark mode is an internal oscillator combination. Calling it dark does not identify dark matter, and calling its one-quantum representation j=1/2 does not identify physical electron spin.

## Reproduction and source

`check_full_symmetry.py` performs exact SymPy checks of the general Jz necessity identity for all six pairs, Origin–Authorship generator rates, sufficient cases for arbitrary smooth remaining couplings, fixed-geometry shifts, moving-center breaking, the nonlinear dark-mode transformation and its conserved generators, square completion, the example Hessian, and moving-frame breaking. `full_symmetry_results.json` records the completed run. The analytic coercivity argument uses the displayed global bound; the code does not replace it with a finite parameter scan.

Python 3.14.7 and SymPy 1.14.0 were used. Source metadata and the action excerpt are included. These calculations are standard Hamiltonian symmetry methods applied to the specified first-party model, with no novelty claim. No original manuscript or governing equation is changed, and no result is approved for promotion.
