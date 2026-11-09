# Source excerpts for the identity audit

Public author manuscripts; line numbers refer to the retrieved fixed-version texts. These are source statements, not independent validation.


## research-updates/2026-10-18/theory-foundations/foundations.tex


Lines 55–64

```tex
A classical history contains a smooth timelike immersed curve in time-oriented Minkowski spacetime. The torsion-coupled realization is restricted to nonzero proper curvature on the interval considered.
\end{postulate}
\begin{postulate}[Independent layered state]
Each history carries four independent real internal coordinates on a fixed affine identity space. A positive constant metric specifies internal kinetic weights. A scalar identity observable is an additional chosen contraction, not a replacement for the full state.
\end{postulate}
\begin{postulate}[Common dynamics]
Geometry and identity enter one reparametrization-invariant action. The action below is the minimal constitutive example studied in this document; its coupling functions and positive stiffnesses are model inputs.
\end{postulate}
\begin{postulate}[Explicit invariance]
Any claim of sovereignty identifies what is preserved and under which transformations. A symmetry of observables, a symmetry of the action, a conserved quantity, and a flow-invariant set are distinct mathematical requirements.
```


Lines 90–117

```tex
\subsection{Independent identity coordinates and scalar observables}
The minimal internal space is a fixed affine space $\I=\mathbb R^4$, with labels
\begin{equation}
I=(I_O,I_A,I_S,I_W),\qquad F=\ell_a I^a,\qquad\ell=(1,1,1,1).\label{eq:identity}
\end{equation}
The coordinates are dimensionless real variables; labels on their subscripts do not denote metric lowering. They do not transform as a spacetime four-vector. We prescribe the constant positive kinetic metric $H=\operatorname{diag}(h_O,h_A,h_S,h_W)$ and a separate positive stiffness matrix. These are model data.

The vector and its scalar contraction have distinct roles. $I$ specifies the internal configuration; $F$ is one chosen observable. Since $\ell$ has a three-dimensional kernel, $F$ does not determine $I$. In particular, $I$ and $I+(u,-u,0,0)$ have the same sum. Independent internal dynamics are therefore an additional postulate, not a consequence of adding four scalar layer functions. The covector $\ell$ must transform along with coordinates if the same observable is described in another internal basis. Figure~\ref{fig:scalar} makes this distinction explicit.
\begin{figure}[htbp]
\centering\includegraphics[width=\linewidth]{figures/02-scalar-vector.pdf}
\caption{The identity vector contains more information than a scalar identity observable. The two states shown are examples of equal scalar contraction, not equivalent physical states established by the theory.}\label{fig:scalar}
\end{figure}

The four layer names identify modeling roles. They do not supply a gauge group, a conserved charge, or measured observables by themselves. An allowed transformation class must be specified before requiring scalar invariance $F(g\cdot z)=F(z)$ or vector invariance. Invariance of $F$ under a transformation is different from constancy of $F$ along evolution.

\subsection{Parameters and units}
We use positive stiffnesses $k_a$ and oscillator frequencies $\omega_a^2=k_a/h_a$, with dimensionless $I^a$. In natural units $[s]=L$, $[m]=L^{-1}$, $[h_a]=L$, $[k_a]=L^{-1}$, $[\kappa]=[\tau_1]=L^{-1}$, and the coupling functions $\mu_j$ have dimension $L$. A convention identifying numerical inertial and stiffness coefficients is available only after choosing dimensionless time and corresponding scales. Couplings are at least $C^2$ for the Hessian analysis and smooth where higher geometric derivatives are used.

\section{A minimal coupled action}
The joint configuration space is $M\times\I$, but the geometry-dependent Lagrangian is defined on its higher jet space. The proposed action is
\begin{align}
 S[y,I]&=\int\dd s\left[-m+\tfrac12\sum_a h_a(\Ds I^a)^2-V(I;\kappa,\tau_1)\right],\label{eq:action}\\
 V&=\tfrac12\sum_a k_a(I^a)^2+\U,\label{eq:potential}\\
 \U&=\mu_1(I_A)\kappa^2 I_S+\mu_2(I_A)\tau_1^2 I_W.\label{eq:coupling}
\end{align}
In a general parameter, $S=\int\mathcal L\dd\lambda$ with $\mathcal L=v[-m+\frac12\sum h_a(I'^a/v)^2-V]$. This makes the dependence of the proper-time measure on the varied curve explicit. Orientation-preserving reparametrizations leave the action unchanged. Fixing $v=1$ before varying $y$ without imposing its constraint would lose terms and is not legitimate.

The coupling is phenomenological. It associates sovereignty with curvature, warp with torsion, and authorship with coupling strength, as a declared constitutive choice. These associations are not unique; a geometric transformation may change both invariants. Origin is absent from $\U$ by a separate decoupling assumption. Joint variation gives reciprocal influence, but there is no exchange symmetry between the inequivalent geometry and identity sectors.
```


Lines 175–207

```tex
\end{align}
The internal system can exchange energy with varying geometry. If both geometric invariants are constant, $E_I$ is conserved. This fact does not amount to conservation of $E_I$ along arbitrary coupled solutions.

\subsection{Prescribed constant geometry}
Let $\kappa=\bar\kappa>0$ and $\tau_1=\bar\tau$ be prescribed constants. An internal equilibrium has both $\Ds I=0$ and $\nabla_I V=0$. Its Origin coordinate is zero, and its other coordinates satisfy
\begin{align}
 I_S^*&=-\mu_1(A_*)\bar\kappa^2/k_S,\label{eq:IstarS}\\
 I_W^*&=-\mu_2(A_*)\bar\tau^2/k_W,\label{eq:IstarW}\\
 0&=k_A A_*-
 \mu_1'(A_*)\mu_1(A_*)\bar\kappa^4/k_S
 -\mu_2'(A_*)\mu_2(A_*)\bar\tau^4/k_W.\label{eq:Astar}
\end{align}
There may be no root, one root, or several. The algebraic balance set for varying geometry is located in jet space, where $\kappa$ and $\tau_1$ are defined, rather than merely in $M\times\I$. We reserve ``equilibrium'' for a state whose full internal phase-space velocity vanishes.

\begin{proposition}[Conditional internal stability]
At a root $A_*$ of Eq.~\eqref{eq:Astar}, the internal potential Hessian is positive definite if and only if
\begin{equation}
 \Delta=k_A-
 \frac{(\mu_1'^2+\mu_1\mu_1'')\bar\kappa^4}{k_S}
 -\frac{(\mu_2'^2+\mu_2\mu_2'')\bar\tau^4}{k_W}>0,
 \label{eq:schur}
\end{equation}
where the coupling functions and derivatives are evaluated at $A_*$. Under this condition the equilibrium is locally Lyapunov stable in the internal system with prescribed constant geometry. It is not asymptotically attracting.
\end{proposition}
\textit{Proof.} Origin contributes a positive one-dimensional block $k_O$. In the ordered coordinates $(A,S,W)$ the remaining Hessian is
\begin{equation}
 K=\begin{pmatrix}
 k_A+\mu_1''\bar\kappa^2I_S^*+\mu_2''\bar\tau^2I_W^*&\mu_1'\bar\kappa^2&\mu_2'\bar\tau^2\\
 \mu_1'\bar\kappa^2&k_S&0\\
 \mu_2'\bar\tau^2&0&k_W
 \end{pmatrix}.
\end{equation}
The Schur complement of the positive diagonal $(k_S,k_W)$ block is Eq.~\eqref{eq:schur}. Positive definiteness gives a strict local minimum of $V$. Conservation of the positive kinetic energy plus the potential difference confines sufficiently small initial perturbations to a neighborhood of that minimum. Linearization yields $H\Ds^2\xi+K\xi=0$ with positive squared frequencies. Conservation also precludes convergence from all nearby higher-energy states. $\square$
```


## sefi-space/sefi-space.tex


Lines 30–50

```tex
\section{Introduction}

Worldline formulations of quantum field theory provide an alternative representation of particle and field
dynamics in terms of path integrals over trajectories in spacetime \cite{Polyakov1987,Schubert2001,Strassler1992}.
These approaches have proven useful for perturbative calculations, effective actions, and the geometric
interpretation of quantum amplitudes. However, the ontological status of field identity, superposition, and
entity persistence remains largely external to the formalism.

The Single Entity Field Interpretation (SEFI) proposes that a given quantum field, such as the electron field,
arises from a single continuous entity whose worldline structure spans all allowed trajectories in spacetime.
The field is then understood as the projection of this worldline ensemble, with forward-time segments
corresponding to particles and backward-time segments corresponding to antiparticles, in line with established
worldline interpretations of electron--positron dynamics \cite{Schubert2001,Strassler1992}.

In previous work, SEFI introduced layered identity constructs under the labels FIELD ORIGIN, FIELD AUTHORSHIP,
FIELD SOVEREIGNTY, and WARP EXPRESSION. These layers were treated as conceptual components of the field's
identity structure. In this manuscript, we formalize these layers as basis directions of a geometric identity
space, which we call SEFI Space (SS). SEFI Space is not a spacetime manifold, nor a gauge or spinor space; it
is an abstract geometric space in which the identity of the single entity evolves as the worldline traverses
spacetime.

```


Lines 68–90

```tex
\cite{Polyakov1987}.

Spin degrees of freedom can be incorporated using Grassmann variables $\psi^\mu(\tau)$, leading to a spin
action of the form
\begin{equation}
S_{\text{spin}}[\psi] = \int d\tau \, \psi_\mu(\tau) \dot{\psi}^\mu(\tau),
\end{equation}
and coupling to an electromagnetic potential $A_\mu(x)$ is introduced via
\begin{equation}
S_{\text{EM}}[y] = q \int d\tau \, \dot{y}^\mu(\tau) A_\mu(y(\tau)),
\end{equation}
where $q$ is the charge of the entity \cite{Schubert2001,Strassler1992}.

The total worldline action for the entity is then
\begin{equation}
S_{\text{entity}}[y,\psi] = S_{\text{WL}}[y] + S_{\text{spin}}[\psi] + S_{\text{EM}}[y].
\end{equation}
In a path-integral formulation, the presence density of the entity at spacetime point $x$ can be written
schematically as
\begin{equation}
\rho(x) = \int \mathcal{D}y \, \mathcal{D}\psi \, e^{i S_{\text{entity}}[y,\psi]} \delta^{(4)}(x - y(\tau)),
\end{equation}
and an emergent field amplitude may be expressed as
```


## research-updates/2026-11-04/word-manuscripts/GWFM-revised-October29.tex


Lines 442–457

```tex
\subsection{Tensorial data alone cannot select a spinor}
\begin{proposition}[Spin-equivariance obstruction]
Let $\mathcal D$ be a collection of worldline data on which the central element $-1\in\operatorname{Spin}^+(1,3)$ acts trivially, as it does on scalar occupation and tensorial currents through the Lorentz projection. Let $S$ be a spinor representation in which $-1$ acts as minus the identity. Any equivariant map $F:\mathcal D\to S$, or to spinor-valued fields with the corresponding action, is identically zero.
\end{proposition}
\begin{proof}
For every $D\in\mathcal D$, equivariance implies $F(D)=F((-1)D)=(-1)F(D)=-F(D)$. Over $\mathbb C$, this gives $F(D)=0$.
\end{proof}
This algebraic statement applies even to nonlinear reconstruction maps; it does not assert that spinors cannot be introduced. It identifies the missing transformation data. A chosen spinor, spinorial path variable, or suitable lifted state space changes the domain and can remove the obstruction. A spin structure by itself does not canonically select a nonzero spinor section. Established spinning-particle and worldline formulations introduce the additional structures appropriate to the quantity being computed.\cite{schubert}

Likewise, an assigned orientation or an assigned coupling $q$ is not a derivation of quantized electric charge. No map from a specified topological invariant to electromagnetic charge is supplied here. The paper derives neither the canonical anticommutation relations nor a many-particle Hilbert space. Those questions are separate from the scalar and current constructions proved above.

\section{Scope for a foundational GWFM}
The results impose a concrete choice on a worldline-based field model. If the target is a diffuse coordinate-time spacetime density, fixed finite multiplicity and a uniform causal speed bound prevent arbitrarily accurate reconstruction by positive graph-supported measures. A model may instead use a genuine path ensemble, allow increasing trajectory multiplicity, change the observable, or introduce a different reconstruction map. Each is a distinct mathematical proposal with its own physical interpretation.

Increasing multiplicity already gives a controlled classical construction: the stationary grid converges to a uniform continuum with the proven $N^{-1/d}$ order. It does not turn the mixture into one regular causal curve. Connecting the stationary graphs by segments that return to an earlier time would leave the stated causal class; concatenating them at later times would change the finite-time spacetime target. Similarly, a long-time ergodic spatial occupation limit discards time and falls outside the theorem's claim.

```


## research-updates/2026-10-20/defining-sefi/unifiying.tex


Lines 50–75

```tex
quantum field theory \cite{Polyakov1987,Strassler1992,Schubert2001}, while noting points 
of disagreement with conventional interpretations.

\subsection{Domain of the Operator}

Let $\mathcal{H}$ denote the Hilbert space of square-integrable fields over spacetime,
\begin{equation}
\mathcal{H} = L^2(M,d\mu_g),
\end{equation}
where $d\mu_g$ is the metric measure. Let $\mathcal{I}$ denote the identity-space manifold 
(SEFI Space) equipped with metric $g_I$,
\begin{equation}
\mathcal{I} = \mathbb{R}^4, \qquad
g_I = \mathrm{diag}(\alpha,\beta,\gamma,\delta).
\end{equation}
For the Hilbert-space construction below, assume $\alpha,\beta,\gamma,\delta>0$. If an 
indefinite identity metric is intended, the operator becomes hyperbolic rather than elliptic, 
and spectral claims require separate analysis \cite{CourantHilbert}.

The unified operator acts on fields
\begin{equation}
\Psi : M \times \mathcal{I} \to \mathbb{C},
\end{equation}
arising from the worldline ensemble and identity-space trajectory.

The domain of the operator is
```


Lines 1080–1100

```tex
\subsection{Points of Disagreement with Conventional Models}

Several aspects of the unified framework diverge from established physics:

\paragraph{Single-Entity Ontology.}
The hypothesis that all excitations arise from a single continuous entity differs from 
standard QFT, which treats particles as excitations of independent fields 
\cite{WeinbergQFT1,PeskinSchroeder}. This disagreement is acknowledged explicitly.

\paragraph{Identity-Space Coordinates.}
SEFI coordinates (origin, authorship, sovereignty, warp) are phenomenological constructs 
with no standard internal-symmetry analogue.

\paragraph{Electron–Positron Interpretation.}
The interpretation of forward-time and backward-time worldline segments as electron and 
positron modes differs from the standard QFT treatment of antiparticles 
\cite{WeinbergQFT1}. The disagreement is noted explicitly.

\paragraph{Inflation Mechanism.}
Sovereignty saturation as a geometric inflation mechanism differs from scalar-field 
inflation models \cite{GuthInflation,LindeInflation}. It is presented as a hypothesis rather 
```


## research-updates/2026-11-04/word-manuscripts/DEFI.tex


Lines 30–41

```tex
than assumed. A conserved Origin charge is derived via Noether's theorem for the
decoupled Origin sector. This construction requires an explicit extension of SEFI,
promoting its originally scalar identity functional $F=O+A+S+W$ to a four-vector
$I^a=(I_O,I_A,I_S,I_W)$ on an identity-space manifold $\mathcal{I}=\mathbb{R}^4$,
which is stated here as a deliberate axiomatic extension rather than a silent
reinterpretation.
\end{abstract}

\maketitle

\section{Introduction}

```
