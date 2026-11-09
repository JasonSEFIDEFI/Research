# Foundations action excerpt

Fixed source version and Git blob are in source_manifest.json. Lines 89–128 of the retrieved text follow. This is an author manuscript, not independent validation.

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

\subsection{Internal Euler--Lagrange equations}
Holding $y$ fixed and varying $I$ with vanishing endpoint variations gives
\begin{align}
 h_O\Ds^2 I_O+k_O I_O&=0,\label{eq:origin}\\
 h_S\Ds^2 I_S+k_S I_S+\mu_1(I_A)\kappa^2&=0,\label{eq:S}\\
 h_W\Ds^2 I_W+k_W I_W+\mu_2(I_A)\tau_1^2&=0,\label{eq:W}\\
 h_A\Ds^2 I_A+k_A I_A
 +\mu_1'(I_A)\kappa^2 I_S+\mu_2'(I_A)\tau_1^2 I_W&=0.\label{eq:A}
\end{align}
Here a prime on $\mu_j$ differentiates its scalar argument. Together with the geometric variational equation, these equations specify the proposed classical coupling. Their derivation uses fixed geometry only during the internal variation, not as a restriction on all joint stationary histories.
```
