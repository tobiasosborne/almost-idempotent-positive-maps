VERDICT: PARTIAL / DIED-AT
Died at the missing boundary-product bound
\[
\| (e_a-e_b)P_{\{a,b\},T}P_{T,\{a,b\}}\|_1 \stackrel{?}{=} O(\delta)
\]
for a shallow hidden 2-cycle \(S=\{a,b\}\), \(T=S^c\). Exact spectrum forbids a genuinely closed separated 2-cycle, but an \(O(\tau)\) boundary term can cancel the forbidden alternating mode, and the current hypotheses do not make that boundary deep.

**Proof / Post-Mortem**
Write the block decomposition
\[
P=\begin{pmatrix}A&B\\ C&D\end{pmatrix},\qquad A=P_{S,S}.
\]
From \(P^2=P\),
\[
A^2-A=-BC.
\]
For \(S=\{a,b\}\), taking trace gives the exact identity
\[
2P_{ab}P_{ba}-P_{aa}(1-P_{aa})-P_{bb}(1-P_{bb})
=
-\sum_{k\notin S}\left(P_{ak}P_{ka}+P_{bk}P_{kb}\right).
\]
The negative part of the boundary sum is bounded by row negativity:
\[
\sum_{k\notin S}(P_{ik}P_{ki})_- \le 2\delta(1+\delta),
\]
so if \(P_{ab},P_{ba}\ge c>0\),
\[
2c^2
\le
P_{aa}(1-P_{aa})+P_{bb}(1-P_{bb})+4\delta(1+\delta).
\]
Thus a low-self reciprocal 2-cycle pays a \(\sqrt\delta=\tau\) spectral tax. At \(\delta=0\), this recovers the Baake-Sumner obstruction: a closed Markov idempotent class has equal positive rows, so separated mutual carriers cannot exist.

But this does not prove DMF. A shallow hidden row need not have low self; ND′ only forces it to be spread at scale \(O(\tau)\), allowing
\[
P_{ii}=1-O(\tau),\qquad P_{ii}(1-P_{ii})=O(\tau),
\]
which is far too large for the trace tax to bite. In alternating-mode language, for \(z=e_a-e_b\),
\[
zA^2-zA=-zBC.
\]
The forbidden near-eigenmode is killed exactly by the boundary product \(BC\). I can force a contradiction only if that boundary is \(O(\delta)\) or lands with universal mass in the deep set. That is precisely the DMF/quantitative Baake-Sumner content, not a consequence of exact spectrum alone.

**New Sub-Lemmas**
1. **Block Spectral Tax, proved.** For any \(S\), \(A^2-A=-BC\). For a reciprocal pair this yields the displayed trace identity and the bound
\[
2P_{ab}P_{ba}\le P_{aa}(1-P_{aa})+P_{bb}(1-P_{bb})+4\delta(1+\delta).
\]

2. **Closed 2-Cycle Exclusion, proved.** If \(BC=0\), then \(A\) is an exact \(2\times2\) row-stochastic idempotent. Hence either \(A=I\), or its two rows are equal. Neither gives a \(\rho\)-separated mutual hidden pair.

3. **Boundary-Product Localization, open/death point.** To close s7 one would need a theorem of the form
\[
zBC=O(\delta)
\]
or “the \(BC\)-mass escaping a shallow closed class has universal deep component.” I do not see a route from trace/rank/eigenstructure to that statement.

**Calibration**
\(P(\)existential DMF true\()\): 0.78.  
\(P(\)this s7 post-mortem/sublemmas survive audit\()\): 0.76.  
\(P(\)trace/rank/eigenstructure alone closes DMF\()\): 0.12.

**Sharpest Structural Insight**
Exact idempotence does not merely “forbid near eigenvalues”; it exports them into the boundary equation \(A^2-A=-BC\). That perfectly explains why the all-shallow web is impossible at \(\delta=0\), but at \(\delta>0\) the obstruction lives in the boundary product, not in the integer trace. The trace argument reaches exactly the \(\sqrt\delta\) scale and then stalls: to finish DMF one must prove that the boundary cancelling the shallow alternating mode necessarily escapes to deep \(W\)-mass.