# Fixed charge does not create a rotation sign in the canonical scalar phase space

November 8, 2026. Exploratory mathematical checkpoint. Codex assisted with derivation, implementation and drafting. No novelty, independent review, electron identification or experimental validation is asserted.

## Question and result

The preceding charge-conjugation note proves that the unconstrained affine H1 configuration space has contractible rotation loops. Its explicit contraction can pass through Phi=0, so it does not establish the same statement at nonzero fixed phase charge. This note supplies a separate argument that preserves that charge.

For the regular canonical phase space defined below, with Q_Phi=q nonzero and Q_Sigma=0, the full charge level is contractible. Its quotient by the global Phi phase action is simply connected. Thus fixing charge, or performing this global-phase quotient, does not supply a noncontractible loop on which to impose a flat Finkelstein–Rubinstein minus sign. This closes those two particular topological routes within this phase-space model. It does not classify every possible quantization or SEFI extension.

## 1 Definitions and assumptions

Use the existing canonical two-complex-scalar action, with potential

\[
V(\Phi,\Sigma)=\frac{|\Phi|^4}{4}+\frac{|\Phi|^2}{2}
+2|\Phi|^2|\Sigma|^2
+\frac\lambda4\left(|\Sigma|^2-\frac3\lambda\right)^2,
\quad \lambda>0.
\]

Fix the asymptotic vacuum representative Sigma=v=sqrt(3/lambda), and put chi=Sigma-v. The field space is H1(R3;C) for Phi and chi; the real-component canonical momenta p and k are in L2(R3;C). Here p and k equal time derivatives under the real-component half-modulus-squared normalization. Inner products and charge constraints are real:

\[
\langle u,w\rangle_{2,\mathbb R}
=\operatorname{Re}\int u^*w\,d^3x,
\quad I(\Phi)=\|\Phi\|_2^2,
\]
\[
Q_\Phi=\langle i\Phi,p\rangle_{2,\mathbb R},
\quad Q_\Sigma=\operatorname{Im}\int(v+\chi)^* k\,d^3x.
\]

There is an infrared qualification for the second expression: k in L2 alone need not be in L1, so its pairing with a nonzero constant vacuum is not automatically an integral. To avoid an undefined charge, take k in L2 intersect L1 with its sum norm and require Q_Sigma=0. This is a stated regular subspace, containing the static-Sigma branch. No claim that Hamiltonian evolution preserves the L1 condition is needed for the topological statement. Alternatively the theorem holds on the k=0 slice without any Sigma-charge integral. General infrared phase-space completions remain outside this result.

Define

\[
\mathcal P_{q,0}=\{(\Phi,\chi,p,k):
\Phi,\chi\in H^1,\ p\in L^2,\ k\in L^2\cap L^1,
\ Q_\Phi=q\ne0,\ Q_\Sigma=0\}.
\]

Use the inherited product norm topology. The Sigma charge is continuous on this space: its vacuum part is controlled by the L1 norm of k and its chi part by L2 Cauchy–Schwarz. Q_Phi is continuous in H1 times L2. The canonical energy is finite because H1 embeds into Lp for 2<=p<=6 and V expands into integrable terms of degrees two through four about the fixed vacuum.

This is an instantaneous finite-energy phase-space statement. It imposes neither the field equations as constraints on every point nor a fixed energy sublevel, stationary ansatz, angular momentum value, gauge field or exclusion of field zeros.

## 2 Charge preserving deformation retraction

Nonzero q implies Phi is not the zero vector. Define a continuous canonical momentum section

\[
p_0(\Phi)=\frac{q}{I(\Phi)}i\Phi,\qquad k_0=0.
\]

Then Q_Phi(Phi,p_0)=q and Q_Sigma(Sigma,0)=0. For 0<=s<=1 define

\[
R_s(\Phi,\chi,p,k)
=(\Phi,\chi,(1-s)p+s p_0(\Phi),(1-s)k).
\]

Both charges are unchanged because they are linear in momenta at fixed fields. The denominator is strictly positive, and the map is continuous in the stated norms. Every point on the section remains fixed throughout. Hence R_s is a strong deformation retraction onto a subspace homeomorphic to

\[
\mathcal B=(H^1(\mathbb R^3;\mathbb C)\setminus\{0\})\times H^1(\mathbb R^3;\mathbb C).
\]

There is also a useful energy check. Write p=p_0+w. The constraint gives <i Phi,w>_R=0, hence <p_0,w>_R=0. Along R_s the kinetic energy is

\[
T_s=\frac{q^2}{2I(\Phi)}
+\frac{(1-s)^2}{2}(\|w\|_2^2+\|k\|_2^2).
\]

It is nonincreasing along this first retraction. The later field-space contraction is not claimed to decrease energy or remain below a binding threshold.

## 3 Explicit contraction of the punctured infinite dimensional Hilbert space

H=H1(R3;C) is separable and infinite dimensional. Fix a complete complex orthonormal basis in its H1 norm, identify it with ell2, and let S be the unilateral right shift. It is an isometry, its range is orthogonal to the first basis vector e0, and it has no nonzero eigenvector with any eigenvalue.

First retract H minus zero to its H1 unit sphere by positive radial scaling. For a unit vector x, connect it to Sx by

\[
A_t(x)=\frac{(1-t)x+tSx}{\|(1-t)x+tSx\|_{H^1}},\quad 0\le t\le1.
\]

The numerator cannot vanish: for 0<t<1 that would make x an eigenvector of S with a negative eigenvalue. Directly, the first nonzero coordinate of x remains nonzero until t=1, where Sx is nonzero. Next connect Sx to e0 by

\[
B_t(x)=\frac{(1-t)Sx+t e_0}{\sqrt{(1-t)^2+t^2}}.
\]

Orthogonality makes the denominator exact and positive. These homotopies give a continuous contraction of the unit sphere, and therefore of H minus zero. This is the standard infinite-dimensional Hilbert-space contraction, applied here with a specified topology; it is not a finite-dimensional sphere argument.

The second factor chi contracts by linear interpolation to zero. Thus B is contractible, and the deformation retraction proves P_(q,0) is contractible.

The contraction cannot reach the zero Phi vector, so the momentum section keeps the charge exactly q. For any fixed starting point and compact homotopy parameter set, continuity and nonvanishing give a positive minimum of ||Phi||_L2. Momentum and energy remain finite along that path. A uniform bound valid for all starting points is not asserted. The abstract H1 shift need not preserve a preferred ansatz or pointwise compact support, which are not constraints in P_(q,0).

## 4 Global phase quotient

The global Phi U(1) action rotates Phi and p together, leaving chi and k unchanged. It acts freely for q nonzero. The retraction R_s is equivariant, and hence induces a deformation retraction of the quotient onto B/U(1).

After radial retraction, the nontrivial factor is the unit Hilbert sphere modulo scalar complex phase, the infinite-dimensional projective Hilbert space. The principal circle bundle has contractible total space and connected fiber. Its homotopy exact sequence gives

\[
\pi_1(\mathcal P_{q,0}/U(1))=0,
\qquad \pi_2(\mathcal P_{q,0}/U(1))\cong\mathbb Z.
\]

Only the first conclusion is needed here. It means that this quotient also lacks a nontrivial fundamental-group sign representation for the proposed rotation loop. It does not mean that all bundles, Berry phases or geometric quantization data on the quotient are trivial. In particular, the nonzero second homotopy group prevents that inference.

This is a global internal-phase quotient, not a local electromagnetic gauge quotient and not a quotient identifying physical spatial orientations. There is no Maxwell field or Gauss constraint in this starting model.

## 5 What this says about spin and statistics

A flat topological sign assigned to loops factors through the fundamental group. That route is unavailable on either of the spaces just analyzed. A spin-half state cannot be obtained merely by fixing the global phase charge and declaring a 2 pi rotation to have sign minus one.

This is not a theorem excluding every form of half-integer quantum behavior in all bosonic theories. For example, other theories can have target-space restrictions, topological sectors, gauge structure or nontrivial quantization data. Any proposed replacement must be derived or explicitly introduced, with its own finite-energy, stability and quantum-consistency analysis. A restricted moduli space can have different topology, but its loops must be checked against the full admissible theory before treating its signs as exact.

The argument also does not show that a low-energy or bound-state sublevel is contractible. Effective energetic barriers and global topological protection are different questions.

## 6 Numerical checks and their role

The accompanying script checks the momentum section, exact-charge interpolation, orthogonality identity, nonincreasing fiber kinetic energy, conjugation, and a two-mode loop contraction at positive and negative charges. It uses smooth periodic scalar modes only as a finite-dimensional illustration; it is not a discretized proof of the infinite-dimensional theorem, a three-dimensional soliton calculation, or a dynamical tunneling path.

The proof is the analytic deformation retraction and Hilbert-space contraction above. Sampled checks only catch implementation and normalization mistakes.

## 7 Consequence for the next investigation

The remaining mathematical route must supply structure beyond fixed global charge alone. Before adding a spinor or changing the action, inspect the underlying SEFI identity variables and their admissible targets. Determine whether those targets and constraints are actually consequences of the existing formulation, whether the canonical model faithfully retains them, and whether a noncontractible rotational sector survives finite-energy deformations. A new target-space constraint or gauge degree of freedom must be recorded as a model extension unless derived.

Meanwhile, a prospective electromagnetic extension must keep a massless unbroken gauge generator and solve its Gauss equation; the prior note explains why charging the existing Sigma condensate under a lone U(1) would instead give the vector a mass.

## Sources and attribution

- [Existing action](https://github.com/JasonSEFIDEFI/SEFI-PY/blob/18a5275df36d32af1b67d514c0c337637ff2c210/research/2026-10-25/critical-correction/MANUSCRIPT_DRAFT.md), section 2, and the preceding charge-conjugation checkpoint in this directory.
- Bruce Blackadar, [Operator Algebras](https://bruceblackadar.com/Mathematics/Cycr.pdf), standard contractibility of the infinite-dimensional Hilbert sphere; the explicit proof is supplied above.
- Steffen Krusch and Martin Speight, [Fermionic quantization of Hopf solitons](https://arxiv.org/abs/hep-th/0503067v2), Commun. Math. Phys. 264 (2006), 391–410. This is a comparison illustrating why full configuration-space loop topology matters; it is a different theory and does not establish a Hopf sector for SEFI.

This proof is a first-party working derivation awaiting independent review. Standard topology and its application are not claimed as a novel theorem. No result has been promoted to an electron, positron or physical-matter claim.
