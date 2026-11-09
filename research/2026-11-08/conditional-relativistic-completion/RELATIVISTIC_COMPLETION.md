# A conditional positive energy relativistic spin half construction

November 8, 2026. Exploratory / Not Promoted. Working mathematical reference with substantial Codex assistance; independent technical review pending.

## Result and its boundary

The earlier rotation-lift calculation left an explicit boost mismatch. A conventional spin-dependent boost term repairs it. For a chosen spin-half doublet and an assigned positive mass, the resulting free momentum-space operators satisfy all 45 independent Poincare commutators. Their Casimirs are P squared=m squared and W squared=-3m squared/4. A finite induced unitary representation supplies a positive-energy quantum realization.

This completes a **conditional free relativistic reference**, not a derivation of that reference from SEFI. A chosen N=1 sector, its identification with physical spin, canonical quantization, the mass and the free dispersion relation are inputs. The prior worldline action and its energy obstruction are not replaced or repaired by writing down a different positive-energy representation.

A conventional local Dirac-field reference is also described and algebraically checked. Its extra local-field and anticommutation structure is made explicit. One-particle Poincare symmetry alone does not determine many-particle exchange statistics.

## 1 Assumptions and conventions

Use hbar=c=1, metric signature (+---), m>0 and the positive mass shell

\[
E(\mathbf p)=\sqrt{m^2+\mathbf p^2}.
\]

Take

\[
\mathcal H_1=L^2(\mathbb R^3,d^3p)\otimes\mathbb C^2,
\qquad S_i=\sigma_i/2.
\]

The complex doublet can be identified abstractly with the selected internal N=1 representation from the prior calculation. That identification does not prove why this is the physical sector or why it transforms under spacetime rotations. Here it is an explicit candidate input.

The momentum operators P_i multiply by p_i; H multiplies by E. Let X_i=i partial/partial p_i. Expressions are first checked on smooth compactly supported momentum spinors, a common dense domain with no momentum boundary terms. The stated boost convention has [K_i,P_j]=i delta_ij H and [K_i,H]=i P_i.

## 2 Deriving the required boost correction within a specified ansatz

Start from J=X cross P+S. With the spin-independent canonical boost K0=half anticommutator(X,E), the commutator is -i epsilon_ijk L_k. It lacks -i epsilon_ijk S_k, as recorded in the preceding checkpoint.

Consider the rotationally covariant minimal ansatz

\[
\mathbf K=\tfrac12\{\mathbf X,E\}
+f(E)\,\mathbf S\times\mathbf p.
\]

For momentum along the third axis, the spin coefficient in the [K_1,K_2] relation requires

\[
(E^2-m^2)f^2+2Ef+1=0.
\]

Its branches are

\[
f=-\frac1{E+m},\qquad f=-\frac1{E-m}.
\]

The second branch is singular at rest. Regularity at p=0 selects the first, whose rest limit is -1/(2m). The full commutator calculation then checks sufficiency at arbitrary momentum, including derivatives of f. This is uniqueness within the stated minimal ansatz and regularity choice, not a classification of every basis, position convention or possible interacting boost.

The corrected operators on flat momentum measure are

\[
\boxed{J_i=-i(\mathbf p\times\nabla_p)_i+S_i,}
\]

\[
\boxed{K_i=iE\partial_{p_i}
+\frac{i p_i}{2E}
-\frac{(\mathbf S\times\mathbf p)_i}{E+m}.}
\]

The scalar i p_i/(2E) term comes from symmetric ordering of X and E. It is required for formal Hermiticity with the flat d3p measure; it must not be omitted while keeping that measure. With invariant mass-shell measure, the wavefunction normalization and corresponding differential expression change.

These are the conventional canonical-spin generators. In particular, equation (230) of Polyzou, Gloeckle and Witala gives the equivalent spin term p cross S divided by m+E. Their existence is not a new SEFI prediction.

## 3 Exact Poincare algebra

The script treats the generators as first-order differential operators, including their matrix-valued multiplication terms. It verifies every independent pair among H, the three P, three J and three K:

\[
[P_i,P_j]=0,\quad [P_i,H]=0,\quad[J_i,H]=0,
\]
\[
[J_i,J_j]=i\epsilon_{ijk}J_k,\quad
[J_i,P_j]=i\epsilon_{ijk}P_k,\quad
[J_i,K_j]=i\epsilon_{ijk}K_k,
\]
\[
[K_i,P_j]=i\delta_{ij}H,\quad
[K_i,H]=iP_i,\quad
[K_i,K_j]=-i\epsilon_{ijk}J_k.
\]

All 45 checks pass as exact rational identities on the positive mass shell. E is treated as an algebraic variable satisfying E squared=m squared+p squared, with differentiation partial E/partial p_i=p_i/E. The code reduces commutator numerators modulo that shell identity; it does not infer exact closure from sampled momenta.

Formal adjoint identities also pass. Formal Hermiticity alone is not a proof of self-adjointness or exponentiation; the finite construction below supplies the unitary representation whose infinitesimal operators agree with these expressions on smooth vectors.

## 4 Finite transformations and unitarity

Let L(p) be a canonical rotationless boost taking (m,0) to p, and let D be the chosen spin-half SU(2) representation. Define the Wigner rotation

\[
W(\Lambda,q)=L(\Lambda q)^{-1}\Lambda L(q).
\]

It fixes (m,0), so it belongs to the massive little group. For q=Lambda-inverse p, the flat-measure wavefunction transforms as

\[
[U(\Lambda)\psi](\mathbf p)
=\sqrt{\frac{E_q}{E_p}}\,
D(W(\Lambda,q))\psi(\mathbf q).
\]

The mass-shell measure d3p/E_p is invariant, and D is unitary. Substituting q in the norm integral shows that the square-root factor cancels the Jacobian. The Wigner cocycle follows directly by inserting the intermediate L(Lambda_1 q):

\[
W(\Lambda_2\Lambda_1,q)
=W(\Lambda_2,\Lambda_1q)W(\Lambda_1,q).
\]

Together with translations, this gives the conventional strongly continuous unitary representation of the proper orthochronous Poincare cover. Its one-parameter subgroups have self-adjoint generators. We have checked the displayed differential expressions on a common smooth domain; no separate claim that every chosen test domain is an essential-self-adjointness core is made.

The spinor implementation uses

\[
B(p)=\frac{(E+m)1+\boldsymbol\sigma\cdot\mathbf p}
{\sqrt{2m(E+m)}}.
\]

It satisfies B B dagger=(E1+sigma dot p)/m and det B=1. A Lorentz spin transformation A maps the Hermitian momentum matrix q dot sigma to p dot sigma. Hence B(p)^(-1) A B(q) is unitary with determinant one, which is the SU(2) Wigner matrix used above.

Independent finite checks used 18 deterministic momentum/rapidity cases at masses 0.3,1,5, with no physical interpretation assigned to those units. Unitarity and cocycle errors were below 1.6e-15. A centered-difference check matched the infinitesimal spin boost correction within 4.45e-10 at a declared 1e-8 tolerance. Sampling checks the implementation, while the preceding invariant-measure and cocycle arguments establish the construction.

## 5 Positive energy and mass spin invariants

H=E is positive and bounded below by m. The Casimirs identify the assigned representation:

\[
P_\mu P^\mu=H^2-\mathbf P^2=m^2.
\]

With the conventions above,

\[
W^0=\mathbf p\cdot\mathbf S,\qquad
\mathbf W=H\mathbf J+\mathbf p\times\mathbf K
=m\mathbf S+\frac{\mathbf p(\mathbf p\cdot\mathbf S)}{E+m}.
\]

The derivative terms cancel exactly. The checks give

\[
P\cdot W=0,\qquad
W_\mu W^\mu=-m^2 S^2=-\frac34m^2.
\]

Thus this reference has massive spin-half kinematics. The mass and spin values were input through m and S; the Casimir checks verify consistency, not emergence or parameter prediction. An additional identical copy can represent an antiparticle sector, but its existence and electric charge are not derived by the single copy.

## 6 Bridge to a conventional Dirac reference

Let beta=diag(1,1,-1,-1), alpha_i have Pauli offdiagonal blocks, and

\[
H_D=\boldsymbol\alpha\cdot\mathbf p+\beta m.
\]

The matrices obey the Clifford algebra and H_D squared=E squared. Its spectral projectors are

\[
\Pi_\pm=\frac12(1\pm H_D/E).
\]

The rank-two positive-energy isometry

\[
u(p)=\sqrt{\frac{E+m}{2E}}
\begin{pmatrix}1\\\boldsymbol\sigma\cdot\mathbf p/(E+m)\end{pmatrix}
\]

satisfies u dagger u=1, u u dagger=Pi_plus and H_D u=E u. This embeds the two-component positive-energy wavefunction in the positive-energy Dirac subspace. The spin basis and induced spacetime transformations are additional conventional choices, not reconstructed from the original scalar identity observable.

The complementary negative-energy spectral basis at momentum p is

\[
w_-(p)=\sqrt{\frac{E+m}{2E}}
\begin{pmatrix}-\boldsymbol\sigma\cdot\mathbf p/(E+m)\\1\end{pmatrix}.
\]

For the negative-frequency term of a local Dirac field, use v(p)=w_-(-p), not w_-(p). This momentum distinction is needed for the standard spin sums and is checked explicitly. It does not mean physical antiparticles have negative observed energy.

The full first-quantized H_D has both signs of energy. A positive many-particle free Hamiltonian is obtained in the conventional field reference through fermionic Fock quantization and normal ordering, as below. This is separate from repairing any energy problem in the SEFI worldline action.

## 7 Two-excitation states do not fix statistics by themselves

For a one-particle representation U, the two-copy action is U tensor U. It commutes with exchange. Both symmetric and antisymmetric tensor subspaces are invariant. Exact two-spin matrix checks give projector ranks three and one, respectively, and both commute with the collective spin generators.

Consequently the one-particle Poincare algebra does not, by itself, select Fermi statistics. A local relativistic quantum field framework carries additional assumptions linking spin, locality, positivity and statistics. This checkpoint does not present a new general spin-statistics theorem.

## 8 A local free field reference under explicit added structure

For comparison, introduce a complex Dirac field with canonical anticommutation relations (CAR) and the standard free expansion

\[
\psi(x)=\int\frac{d^3p}{(2\pi)^{3/2}}
\sum_s\left[u_s(p)b_s(p)e^{-ipx}
+v_s(p)d_s^\dagger(p)e^{ipx}\right].
\]

The chosen spinor normalization is the one above. CAR makes repeated creation operators antisymmetric. After normal ordering,

\[
H_F=\sum_s\int d^3p\,E_p
\left(b_s^\dagger b_s+d_s^\dagger d_s\right)\geq0.
\]

One may assign a conserved global charge

\[
Q=q\sum_s\int d^3p\left(b_s^\dagger b_s-d_s^\dagger d_s\right).
\]

The value q and any electromagnetic gauge interpretation are still inputs. A conjugation exchanging b and d preserves energy and reverses Q. Four finite CAR modes, consisting of two particle and two antiparticle spin labels at a single momentum, were checked in a 16-dimensional Fock space. The Hamiltonian has nonnegative occupation energies, and an explicit fermionic mode permutation preserves H and reverses Q. This finite-mode check is not a test of spacetime microcausality.

For the continuum local reference, the spin sums are

\[
\sum_su_s\bar u_s=\frac{\slashed p+m}{2E},\qquad
\sum_sv_s\bar v_s=\frac{\slashed p-m}{2E}.
\]

They give

\[
\{\psi_\alpha(x),\bar\psi_\beta(y)\}
=\left[(i\slashed\partial+m)\Delta(x-y)\right]_{\alpha\beta},
\]

\[
\Delta(z)=\int\frac{d^3p}{(2\pi)^3\,2E}
\left(e^{-ipz}-e^{ipz}\right).
\]

The measure and scalar integrand make Delta Lorentz invariant. At spacelike z choose an equal-time frame; the two spatial integrals cancel under p->-p. Delta vanishes on the open spacelike region, as do its derivatives in the distributional sense. Thus the continuum free-field anticommutator vanishes at spacelike separation. Even local observables built from the field obey the corresponding microcausality condition. This analytic reference argument uses the local field expansion and CAR; no finite-mode matrix or positive-energy one-particle wavefunction alone proves it.

This constructs a familiar consistent free particle/antiparticle field **under the added reference assumptions**. It does not establish that the SEFI fields obey those assumptions or that their excitations are the measured electron and positron.

## 9 What is supplied and what is still missing

| Item | Status in this checkpoint |
|---|---|
| Exact internal oscillator sectors in specializations of the original action | Retained from the earlier internal-symmetry calculation |
| Physical N=1 selection | Still absent; the earlier negative selection result is unchanged |
| Identification of that internal pair with physical canonical spin | Assumed for this reference, not selected by the original action |
| Positive mass and relativistic dispersion | Assigned inputs, not derived values |
| Corrected free boost and Poincare algebra | Constructed and checked exactly conditional on those inputs |
| Positive-energy unitary one-particle representation | Supplied by the conventional induced construction |
| Local free Dirac field, Fermi exchange and positive Fock energy | Supplied as a conventional reference with explicit local-field and CAR structure |
| Derivation of CAR/locality and the field map from SEFI | Not supplied |
| Electromagnetic coupling and observed charge | Not supplied; a global charge label is not yet electromagnetism |
| Higher-derivative worldline stability/positive energy | Not repaired by this reference |
| Observed electron identification or experimental validation | Not established |

Step 4 therefore has a conditional consistent target. The next SEFI-specific obligation is a controlled map from a justified physical sector of its actual dynamics into this target, including why the new boost and field structures apply. Merely adjoining a known free Dirac representation would assume the desired particle structure rather than derive it.

## Sources and reproducibility

- [Preceding rotation-lift obstruction](../sector-selection-rotation/ROTATION_LIFT.md), Research commit `59c1b3a5a6ccfa1fd11f131362690b84267efad8`.
- E. Wigner, [On Unitary Representations of the Inhomogeneous Lorentz Group](https://www.math.toronto.edu/mgualt/courses/25-QM/docs/Wigner-1939.pdf), Annals of Mathematics 40 (1939), 149–204.
- W. N. Polyzou, W. Gloeckle and H. Witala, [Spin in relativistic quantum theory](https://homepage.physics.uiowa.edu/~wpolyzou/papers/arx_general_ext_20.pdf), especially equations (229)–(230) for the canonical generators.

`check_poincare.py` verifies all differential-operator commutators, the minimal regular boost coefficient, formal adjoints and Casimirs. `check_wigner.py` checks the independent finite-transform implementation. `check_dirac_reference.py` checks Clifford/projector/isometry/spin-sum identities, CAR, charge conjugation, positive finite-mode occupation energy and the two exchange projectors. The operator-domain, unitary-group and spacelike-support arguments are written out above and are not replaced by those tests.

Original execution used Python 3.14.7, SymPy 1.14.0 and NumPy 2.5.2. Protocol, machine-readable results, source metadata and hashes accompany the files. These are conventional reference constructions and their explicit checks, not claims of novelty. Codex assisted with derivation, code, source review, execution and drafting; author verification and independent technical review remain outstanding. No result is promoted to physical matter or an electron–positron field.
