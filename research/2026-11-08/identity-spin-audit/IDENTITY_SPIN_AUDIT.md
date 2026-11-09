# Identity variables and the missing spatial spin map

November 8, 2026. Exploratory / Not Promoted. Working mathematical analysis with substantive Codex assistance; independent technical review pending.

## Finding

There is a useful conditional construction in the existing identity oscillator system: two canonically paired modes admit the conventional Schwinger SU(2) algebra, and their one-quantum sector is two dimensional with internal representation label j=1/2. This is a real algebraic possibility, not a derivation of electron spin. It requires canonical quantization and, for the internal SU(2) to be conserved, equal frequencies and couplings that preserve it. The manuscripts do not impose those conditions generally or identify this internal group with physical spatial rotations.

The distinction that must not be missed is between **four real identity coordinates packaged as two complex numbers** and **two canonical oscillators packaged using their coordinates and momenta**. The first has zero canonical brackets between its components. The second has the nonzero brackets needed for the oscillator construction. Equal real dimension does not make these constructions dynamically or symplectically equivalent.

## 1 Source audit

All manuscript sources in this audit are pinned to SEFI-Manuscripts commit `6311562792bf9bd16ec278a669b4afe64ffedbc4` and identified in `source_manifest.json`, with relevant passages in `source_excerpts.md`.

| Source | Explicit mathematical structure | What is not derived there |
|---|---|---|
| SEFI Space, `sefi-space/sefi-space.tex` | Four real coordinates on R4 with positive diagonal metric; a possible internal action | The introduction explicitly distinguishes identity space from spinor and gauge spaces. Grassmann spin and electromagnetic terms are introduced separately. |
| Foundations, `research-updates/2026-10-18/theory-foundations/foundations.tex` | Affine R4, independent coordinates, positive kinetic weights h_a and stiffnesses k_a, scalar observable F=sum I_a, curvature/torsion couplings | A nonzero fixed identity norm, an SU(2) spatial action, a selected quantum occupation or an observed charge unit |
| Unified draft, `research-updates/2026-10-20/defining-sefi/unifiying.tex` | R4 identity metric and a proposed differential operator with chosen potentials | A unique particle spectrum or an established electron-field reconstruction |
| Revised GWFM, `research-updates/2026-11-04/word-manuscripts/GWFM-revised-October29.tex` | Phase-enriched history construction with explicit quantum inputs; a spin-equivariance obstruction | A spinor reconstructed from tensorial data alone; the revised text already states this limitation |
| DEFI, `research-updates/2026-11-04/word-manuscripts/DEFI.tex` | Coupled worldline and R4 internal variables | “Symmetric” reciprocal coupling does not establish exchange symmetry of internal coordinate labels or equal oscillator frequencies |

This is an audit of these explicit realizations, not a claim that every unpublished formulation has been examined. The canonical two-spacetime-field model from the preceding checkpoint and the worldline identity model are distinct systems. No controlled reduction identifying their coordinates and symplectic structures has been supplied by these sources.

## 2 A conserved oscillator energy is not a fixed identity norm

On prescribed constant geometry, with constant coupling functions, shift the internal equilibrium and write q_a=I_a-I_a*. The fluctuation Lagrangian is

\[
L_I=\frac12\sum_a h_a\dot q_a^2-\frac12\sum_a k_aq_a^2,
\quad p_a=h_a\dot q_a,
\quad H_I=\sum_a\left(\frac{p_a^2}{2h_a}+\frac{k_aq_a^2}{2}\right).
\]

Frequencies satisfy omega_a squared=k_a/h_a. Conservation of H_I does not preserve R squared=sum q_a squared:

\[
\frac{dR^2}{ds}=2\sum_a\frac{q_ap_a}{h_a}.
\]

For a unit-frequency uncoupled mode, q_1=cos s and p_1=-sin s, with other deviations zero, energy stays 1/2 while all deviations pass through zero at s=pi/2. A nonzero energy therefore does not justify dividing by the coordinate norm everywhere. In a zero-coupling realization whose equilibrium is I*=0, the identity vector itself passes through zero. That admissible example suffices to show that a globally nonzero identity vector is not a general consequence of the stated model.

For equal frequencies, individual trajectories q=a cos(omega s)+b sin(omega s) have constant Euclidean norm only when ||a||=||b|| and a dot b=0. These are additional initial-data conditions. Unequal kinetic weights require the corresponding weighted formulation. Imposing a fixed radius for all states as a holonomic constraint changes the variational problem.

The conserved positive Origin energy in the foundations manuscript also cannot be identified directly with a signed electric charge: it is nonnegative and is defined as an oscillator first integral.

## 3 Coordinate packing and the Hopf identity

For four real coordinates set

\[
w_1=q_1+iq_2,\quad w_2=q_3+iq_4,
\quad R^2=|w_1|^2+|w_2|^2.
\]

Define

\[
b=(2\operatorname{Re}(w_1^*w_2),\,
2\operatorname{Im}(w_1^*w_2),\,|w_1|^2-|w_2|^2).
\]

The exact polynomial identity is b dot b=R to the fourth power. Where R is nonzero, n=b/R squared is a unit vector and gives the familiar Hopf-map construction on a normalized coordinate sphere.

However, with the manuscript's ordinary coordinate-momentum canonical structure, all coordinate-only functions commute:

\[
\{w_j,w_k^*\}=0,\qquad \{b_i,b_j\}=0.
\]

The unit-vector identity alone therefore does not give a spin Poisson algebra, select a physical rotation action or enforce avoidance of R=0. Nor is a worldline map into R4 a three-dimensional spatial texture: borrowing a Hopf-soliton sector requires an explicit spatial field, boundary conditions, admissible target and stabilizing dynamics.

## 4 A genuine conditional internal SU(2) construction

For each selected oscillator, use a canonical rescaling

\[
Q_j=\sqrt{h_j\omega_j}\,q_j,\qquad
P_j=\frac{p_j}{\sqrt{h_j\omega_j}},\qquad
z_j=\frac{Q_j+iP_j}{\sqrt2}.
\]

Now {Q_j,P_k}=delta_jk and {z_j,z_k*}=-i delta_jk. Two selected modes define N_j=|z_j| squared and

\[
J_i=\frac12z^\dagger\sigma_i z,
\quad N=N_1+N_2.
\]

In canonically normalized real variables,

\[
J_x=(Q_1Q_2+P_1P_2)/2,\quad
J_y=(Q_1P_2-P_1Q_2)/2,\quad
J_z=(N_1-N_2)/2.
\]

Direct calculation gives

\[
\{J_i,J_j\}=\epsilon_{ijk}J_k,\quad
\{N,J_i\}=0,\quad J^2=N^2/4.
\]

This is the standard classical oscillator moment map. For H=omega_1 N_1+omega_2 N_2,

\[
\dot J_x=-(\omega_1-\omega_2)J_y,\qquad
\dot J_y=(\omega_1-\omega_2)J_x,\qquad
\dot J_z=0.
\]

Thus all three generators are conserved if the selected frequencies coincide. With splitting, only the axial generator among these three is generally conserved. For the constant-coupling prescribed-geometry limit this is an exact statement. Variable geometry and nonconstant constitutive couplings require new symmetry checks; the uncoupled oscillator algebra does not establish symmetry of the full worldline action.

More generally, within number-conserving quadratic transformations a normal-mode Hamiltonian z dagger Omega z has symmetry generators T obeying [Omega,T]=0. Degenerate frequency blocks allow U(m) mixing. Four arbitrary positive stiffnesses do not automatically single out a two-mode block. This classification is limited to that linear canonical symmetry class.

## 5 Full linearized coupling and an exact degeneracy test

At a stable internal equilibrium on prescribed constant geometry, let K be the foundations manuscript's potential Hessian and H its positive kinetic metric. Squared normal-mode frequencies are eigenvalues of H^(-1/2) K H^(-1/2). Origin decouples. In the ordered Authorship, Sovereignty, Warp coordinates, the other mass-normalized block has the form

\[
M=\begin{pmatrix}a&b&c\\b&d&0\\c&0&e\end{pmatrix},
\]

where a=K_AA/h_A, d=k_S/h_S, e=k_W/h_W,
b=mu_1'(I_A*) kappa squared divided by sqrt(h_A h_S), and
c=mu_2'(I_A*) tau_1 squared divided by sqrt(h_A h_W). This follows directly from the stated constitutive coupling. The AA entry includes the corresponding second-derivative terms. Stability requires positive M and positive Origin squared frequency.

For a repeated eigenvalue r of a real symmetric 3 by 3 matrix, rank(M-r identity) is at most one. But its minor using rows (A,S) and columns (A,W) is exactly -bc. Thus **if both b and c are nonzero, the three ASW squared frequencies are all simple**. This is an exact linear algebra consequence, not a parameter scan.

The characteristic determinant is

\[
\det(M-r1)=(a-r)(d-r)(e-r)-b^2(e-r)-c^2(d-r).
\]

Origin can still coincide with an ASW mode if this determinant vanishes at r=k_O/h_O. That is a specific parameter relation, not a consequence of the layer names. For example, the positive block [[4,1,1],[1,2,0],[1,0,2]] has distinct squared frequencies 2, 3-sqrt(3), 3+sqrt(3). Choosing Origin squared frequency 2 supplies a twofold degeneracy of the full linearized system, while a small change of that independent Origin parameter splits it.

If one offdiagonal coupling vanishes, additional degeneracies can occur. For c=0, a degeneracy between the uncoupled W mode and the AS block requires (a-e)(d-e)-b squared=0. For b=c=0, diagonal frequency equalities determine degeneracy. These cases can be checked before proposing an internal doublet.

An exact degeneracy produces SU(2) mixing for the quadratic normal-mode Hamiltonian after canonical diagonalization. It does not show that cubic and higher terms of a nonconstant mu preserve that group. Those terms, or the dynamical geometry, may break it. The constant-coupling oscillator limit avoids that particular nonlinearity but still does not supply the spatial rotation lift.

## 6 Quantum two-state sector and its limits

If canonical bosonic quantization is additionally adopted, define

\[
\hat J_i=\frac{\hbar}{2}a^\dagger\sigma_i a,
\qquad \hat N=a_1^\dagger a_1+a_2^\dagger a_2.
\]

The conventional Schwinger construction gives

\[
[\hat J_i,\hat J_j]=i\hbar\epsilon_{ijk}\hat J_k,
\quad \hat J^2=\hbar^2\frac{\hat N}{2}\left(\frac{\hat N}{2}+1\right).
\]

The fixed-N space has dimension N+1 and internal representation label j=N/2. At N=1, basis states |1,0> and |0,1> form a doublet, with internal 2 pi transformation minus identity. The exact matrix checks in this package cover N=0 through 6.

This construction is not new: Schwinger's 1952 oscillator representation is the primary comparison. Its usefulness here is to show precisely which extra assumptions can provide a two-state internal sector. The manuscript does not select N=1. It also has four real oscillators, not just the chosen pair; two oscillator modes use four real phase-space coordinates, whereas all four identity modes have eight real phase-space coordinates. Other modes are not removed by relabeling. A ground-state restriction, decoupling argument or consistent truncation must be justified separately.

If all four oscillator frequencies coincide, the number-conserving symmetry can be U(4); the one-quantum space is then four dimensional. Its choice of an SU(2) subgroup is not unique: it can be assigned different SU(2) representations, such as two doublets or one j=3/2 multiplet. An internal degeneracy alone does not select the spatial little-group action.

## 7 The missing spatial rotation bridge

In the stated worldline identity realization, I_a are internal scalar labels. Proper curvature, torsion and the scalar contractions used in their couplings are unchanged by a full spatial rotation. Under the inherited rotation action, a 2 pi rotation returns the classical input data to itself.

For a single-valued reconstruction F from those inputs to a spinor with a genuine Spin(3) action, equivariance under its central element would require

\[
F(D)=F((-1)D)=(-1)F(D)=-F(D),
\]

and hence F(D)=0. This argument already appears in the revised GWFM manuscript; it is not presented as a new obstruction discovered here.

The oscillator construction does not contradict it. Its internal SU(2) acts nontrivially on the oscillator state. A 2 pi internal transformation in the N=1 sector differs from the identity action inherited from rotating scalar worldline labels. Equating them requires a specified physical lift or coupling, not just matching matrix dimensions. A spin structure, a Grassmann variable or a chosen internal doublet can add the missing input, but then that input must be acknowledged and its dynamics derived.

A momentum-space or orientation-dependent state bundle could also change the reconstruction domain. Such a proposal requires its own transition functions, connection, symmetry action and observation law. An arbitrary basis-dependent sign is insufficient.

## 8 What has been established and what should be calculated next

The possible overlooked structure is a **conditional internal oscillator doublet**. Its algebra is checked. It is not produced by the coordinate-only Hopf packing, and it is not spatial spin by itself.

For a candidate to advance beyond this checkpoint, it must specify:

1. Which two physical normal modes are selected and why they are degenerate under the actual constitutive couplings.
2. What selects the N=1 sector and how it remains invariant when coupled to geometry and other modes.
3. A physical spatial-rotation lift or interaction that identifies its internal generators with the measured spin, including the central 2 pi action.
4. A local relativistic dynamical construction and many-particle exchange rule. An internal SU(2) representation alone does not imply fermionic statistics or a Dirac field.
5. A separately justified electromagnetic generator and coupling. Oscillator number is not automatically electric charge, and the two doublet components are not automatically electron and positron.

The linearized degeneracy audit above already shows that generic nonzero Authorship couplings leave no ASW doublet. A proposed Origin pairing must meet the displayed characteristic equation. The next unresolved bridge is a physical symmetry principle that protects such a degeneracy in the nonlinear action and identifies its internal group with spatial rotations. A spatial-locking proposal remains an explicitly labeled extension unless derived from the existing action.

This identifies mathematical obligations rather than declaring that no progress is possible. It avoids counting an internal representation as a successful electron derivation while still retaining the constructive result.

## Reproduction and sources

`check_identity_algebra.py` checks the coordinate Hopf identity and zero brackets, the canonical Poisson SU(2) algebra and Casimir, frequency-splitting evolution, nonconservation of coordinate radius, an anisotropy counterexample, and exact fixed-N quantum matrices through N=6. These are symbolic identities and standard representation calculations, not observed-particle predictions.

Source versions and relevant passages are in `source_manifest.json` and `source_excerpts.md`. The primary conventional comparison is Julian Schwinger, [On Angular Momentum](https://digital.library.unt.edu/ark:/67531/metadc1019338/), NYO-3071, January 26, 1952, DOI 10.2172/4389568. The exact reconstruction limitation is also stated in the revised GWFM source above.

The original scalar branch, prior negative results and source manuscripts are unchanged. No experiment, novelty, completed spin-statistics derivation, journal submission or promotion approval is claimed.
