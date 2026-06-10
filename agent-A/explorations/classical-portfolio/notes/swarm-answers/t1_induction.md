**VERDICT: DIED-AT**

The dimension-induction route dies at the required W-stability lemma, not at the LP-dual cleanup basin.

Base cases are clean. For `n<=3`, the row polytope is a point, segment, or `P=I`. Segment endpoints expose with
\[
e_v(\rho)\ge \frac{\rho}{2+4\delta}=\frac{4\tau}{2+4\delta}\ge \frac43\tau>\kappa
\quad(\delta\le 1/4),
\]
so all rows lie in `conv W` and `H=0`.

The exact deletion mechanism is the one-state stochastic complement. With
\[
P=\begin{pmatrix}A&b\\ c^T&d\end{pmatrix},\qquad \lambda=1-d\ne0,
\]
define
\[
Q=A+\lambda^{-1}bc^T .
\]
Then
\[
Q1=1,\qquad Q^2=Q,\qquad \operatorname{rank}Q=\operatorname{rank}P.
\]
But the induction needs more:
\[
\delta(Q)\le C\delta,\qquad H(Q)\ge cH(P),\qquad W(Q)\text{ comparable to }W(P).
\]
This is where it fails.

For row `i`, write \(\theta_i=P_{ia}/(1-P_{aa})\). The sharp native loss estimate is
\[
\nu(q_i)\le \delta(1+\theta_i^+)+(1+\delta)\theta_i^- .
\]
So deletion preserves `δ=O(δ)` only under a conditioning/sign hypothesis on the eliminated column. X2’s rank-preservation obstruction already shows this can blow arbitrarily.

The new death point is W-stability:
\[
\boxed{
e_P(v;\rho)<\kappa
\;\not\Rightarrow\;
e_{Q^{(a)}}(v;\rho')<\kappa',
\qquad
\operatorname{dist}(q_v,\operatorname{conv}W(Q^{(a)}))\not\gtrsim H(P).
}
\]
Deleting a blocker can make the old hidden vertex well-exposed.

The s5 rational web passes the induction test in the bad way. Original:
\[
\delta=1841/1600000,\quad H=1/1000,\quad e_3=1/200<\kappa,
\]
with `W={0,1,2}` and hidden rows `3,4`. Deleting row `4` keeps exactness and controlled negativity, but the old hidden row becomes exposed:
\[
\delta(Q^{(4)})\approx 9.03\cdot 10^{-4},\qquad
e_{Q^{(4)}}(3)\approx 10^{-2}>\kappa'\approx 7.51\cdot10^{-3},\qquad
H(Q^{(4)})=0.
\]
Deleting exposed rows instead can blow negativity by factors hundreds to thousands. Thus the induction has no uniformly valid deletion choice.

**New objects/sublemmas**

1. Small-`n` segment/simplex base certificate, valid for `δ<=1/4`.
2. One-state complement deletion package: exactness, row-stochasticity, rank preservation.
3. Explicit negativity transport bound:
\[
\delta(Q)\le \delta(1+\Theta^+)+(1+\delta)\Theta^- .
\]
4. Required but open/false-naive W-stability lemma above.

Calibration:
\[
P(\text{linear law true})=0.80,\qquad
P(\text{this death certificate survives audit})=0.84.
\]

What induction sees that LP does not: the obstruction is functorial. Exactness has a deletion morphism, but “being a bad hidden top vertex relative to \(W\)” is not preserved by that morphism. The LP frame sees witness support; induction exposes the deeper problem that \(W\) itself is not stable under exact state elimination.