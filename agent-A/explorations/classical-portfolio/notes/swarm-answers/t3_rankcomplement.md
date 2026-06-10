**VERDICT: DIED-AT**

Not `DIED-AT-BY-COLLAPSE`: this did not reduce to the exposedness-LP dual basin. It died in the native rank/complement algebra.

For a block split
\[
P=\begin{pmatrix}A&B\\ C&D\end{pmatrix},
\]
the exact stochastic complement on the kept set \(S\), when \(I-D\) is invertible, is
\[
Q=A+B(I-D)^{-1}C .
\]
It preserves the exact structure:
\[
Q\mathbf 1=\mathbf 1,\qquad Q^2=Q.
\]
But the Schur complement of \(I-P\) gives
\[
\operatorname{rank}(I-P)
=\operatorname{rank}(I-D)+\operatorname{rank}(I-Q)
=|E|+|S|-\operatorname{rank}(Q),
\]
so
\[
\boxed{\operatorname{rank}(Q)=\operatorname{rank}(P).}
\]
Thus the exact nonsingular complement is not an induction step. This matches the earlier X2 obstruction in [X2-rank-induction.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave3/X2-rank-induction.md:1).

The only way to drop rank is to eliminate a block with a fixed mode, i.e.
\[
I-D\ \text{singular}.
\]
But then the complement becomes a quotient/group-inverse operation, and the quantitative control needed for induction fails. The sharp death certificate is:

\[
q=(\varepsilon+\delta,\,-\delta,\,1-\varepsilon),\qquad
P=\mathbf 1 q^T,\qquad S=\{1,2\}.
\]
Then \(P\mathbf1=\mathbf1\), \(P^2=P\), and row negative mass is \(\delta\). Complementing away coordinate \(3\) gives
\[
Q=\mathbf1_2
\left(
\frac{\varepsilon+\delta}{\varepsilon},
-\frac{\delta}{\varepsilon}
\right),
\]
hence
\[
\boxed{\delta(Q)=\delta/\varepsilon.}
\]
Taking \(\varepsilon\ll1\) gives unbounded loss from an exact idempotent with arbitrarily small original negativity. So the needed lemma
\[
\delta(Q)\le C\delta,\qquad H(Q)\ge cH,\qquad W(Q)\ \text{lifts back to}\ W(P)
\]
is false without an additional uniform conditioning hypothesis. A recurrent-like block is exactly the case where that conditioning degenerates.

**New Objects / Lemmas**

1. `gamma-complement gap`:
\[
\gamma_E:=\|(I-D)^{-1}\|_{\infty\to\infty}^{-1}.
\]
The real transform is \(\delta'\sim \delta/\gamma_E\), not \(O(\delta)\). Rank drop wants \(\gamma_E=0\).

2. `rank-preserving complement lemma`: nonsingular stochastic complement keeps rank, idempotence, and row-stochasticity.

3. `signed complement amplifier`: the \(P=\mathbf1q^T\) family above proves no universal \(\delta'\le C\delta\) complement lemma.

4. `height-collapse warning`: the complement map can delete the coordinate direction carrying the canonical separator, so there is no lower bound \(H'\ge cH\) without a separate frame-transfer theorem. That is the same obstruction recorded in the \(R\Lambda=I\) coupling experiments, especially [d2_fixR.py](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/experiments/d2_fixR.py:24).

**Calibration**

\(P(\)linear law true\()\): `0.82`, driven by the d13 record \(H\approx 2\delta\) and no verified \(H\gg\delta\) instance; see [wave5 final synthesis](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave5-sigma-wall-parallel.md:670).

\(P(\)this post-mortem survives audit\()\): `0.88`. The rank identity and amplifier example are algebraic; the only softer part is the interpretation that no clever singular quotient avoids the same conditioning wall.

**What This Strategy Sees**

The LP frame sees negative leakage as a dual-optimality obstruction. The rank-complement frame sees the same obstruction spectrally: to reduce rank, one must invert or quotient a near-recurrent block, and the inverse amplifies signed leakage by \(1/\gamma_E\). So the missing theorem is not “another support cleanup”; it is a quantitative frame-transfer/conditioning theorem strong enough to make a singular rank drop behave like a bounded complement.