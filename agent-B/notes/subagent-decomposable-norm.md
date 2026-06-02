# Sidecar: decomposable norm versus CP/coCP component control

Question: is every unital positive decomposable map between matrix algebras of
decomposable norm 1?

Answer: no for the standard Haagerup/Wittstock decomposable norm.

Let \(u:A\to B\) be a linear map between C*-algebras and write
\(\widehat u(a)=u(a^*)^*\). The standard decomposable norm is
\[
\|u\|_{\mathrm{dec}}
 =
\inf \max\{\|S_1\|,\|S_2\|\},
\]
where the infimum is over completely positive maps \(S_1,S_2:A\to B\)
such that
\[
a\mapsto
\begin{pmatrix}
S_1(a) & u(a)\\
\widehat u(a) & S_2(a)
\end{pmatrix}
\]
is completely positive as a map \(A\to M_2(B)\). This is the
Haagerup decomposable norm on the linear span of completely positive maps.

Counterexample: the transpose \(\tau_n:M_n\to M_n\), \(n>1\), is unital,
positive, trace-preserving, and decomposable in the CP+coCP sense:
\[
\tau_n = 0 + \mathrm{id}_{M_n}\circ \tau_n .
\]
But \(\|\tau_n\|_{\mathrm{dec}}\ge \|\tau_n\|_{\mathrm{cb}}=n\). The cb
lower bound uses the flip
\[
F=\sum_{ij} e_{ij}\otimes e_{ji}, \qquad \|F\|=1,
\]
since \((\mathrm{id}_n\otimes\tau_n)(F)=\sum_{ij}e_{ij}\otimes e_{ij}
=|\Omega\rangle\langle\Omega|\), \(\Omega=\sum_i e_i\otimes e_i\), which
has operator norm \(n\). The inequality
\(\|u\|_{\mathrm{cb}}\le \|u\|_{\mathrm{dec}}\) follows from the
off-diagonal corner estimate/Cauchy-Schwarz inequality for completely
positive \(2\times 2\) block maps. Thus the standard dec norm is not 1.
In fact, by the Wittstock-Paulsen decomposition theorem for maps into
\(B(H)\), equality holds here: \(\|\tau_n\|_{\mathrm{dec}}=n\).

For the proposed CP/coCP two-hole argument, the controlled hypothesis should
not be phrased as \(\|\Phi\|_{\mathrm{dec}}=1\). The needed condition is an
explicit CP/coCP decomposition with bounded CP summands:
\[
\Phi=\Phi_0+\Psi_0\circ\tau_d,\qquad \Phi_0,\Psi_0\ \text{CP},
\]
and, for a unital map,
\[
\Phi_0(1)+\Psi_0(1)=1.
\]
This condition is automatic from any CP+coCP decomposition of a unital
decomposable positive map. Since CP maps satisfy
\(\|\Phi_0\|_{\mathrm{cb}}=\|\Phi_0(1)\|\) and similarly for \(\Psi_0\), it
gives
\[
\|\Phi_0\|_{\mathrm{cb}}\le 1,\qquad
\|\Psi_0\|_{\mathrm{cb}}\le 1,
\]
and hence a total component budget at most 2. If an argument needs total
budget 1 rather than per-summand budget 1, that is an additional normalized
decomposition hypothesis and is not supplied by the standard decomposable
norm.

Trace-preserving maps do not change the negative answer: \(\tau_n\) is
already trace-preserving. In Schrödinger picture, trace preservation is the
dual of unitality, so the same CP/coCP subunital control applies to the
adjoint decomposition; equivalently the original CP components are
trace-nonincreasing. Preserving a particular state also does not repair the
standard decomposable-norm statement; \(\tau_n\) preserves the maximally mixed
state.

Local/reliable sources checked:
- `agent-B/references/positive-maps-2604.08380/paper.tex`, lines around
  199-201 and 1861-1864: decomposable positive maps are CP + coCP.
- Same file, lines around 2130-2142: Stormer reversible conditional
  expectations imply decomposability, structurally, but no norm budget is
  stated.
- Paulsen, *Completely Bounded Maps and Operator Algebras*, Chs. 2, 8
  (Cambridge Core); standard source for positive maps and the
  Wittstock-Paulsen block decomposition.
- Haagerup, "Injectivity and decomposition of completely bounded maps",
  Lecture Notes in Math. 1132, 170-222; standard source for
  \(\|\cdot\|_{\mathrm{dec}}\).
