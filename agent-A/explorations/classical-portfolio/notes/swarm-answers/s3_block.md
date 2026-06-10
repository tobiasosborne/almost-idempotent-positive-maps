**VERDICT: DIED-AT the leakage estimate.** The mandated route cannot currently prove the needed
\[
\|B\mathbf 1-\mathbf 1\|_\infty,\ \|B^2-B\|_{\infty\to\infty}=O(\delta/(\kappa R))
\]
for the principal top-band block \(B=P_{TT}\). The best derivable bound has an unavoidable \(g_i/(\kappa R)\) term, which is order one for boundary top-band rows.

**Proof / Post-Mortem**

Let \(T=\{j:g_j<\kappa R\}\), up to adding the named carriers, and write \(P_i^+(S)=\sum_{j\in S}\max(P_{ij},0)\). For any high set \(D_L=\{j:g_j\ge L\}\),
\[
L\,P_i^+(D_L)\le g_i+\delta R
\]
because
\[
g_i=\sum_j P_{ij}g_j\ge L P_i^+(D_L)-R\sum_j P_{ij}^- \ge L P_i^+(D_L)-\delta R.
\]

Taking \(L=\kappa R\), this gives for \(i\in T\)
\[
\left|1-(B\mathbf 1)_i\right|
=\left|\sum_{j\notin T}P_{ij}\right|
\le P_i^+(T^c)+P_i^-(T^c)
\le \frac{g_i+\delta R}{\kappa R}+\delta.
\]
Since \(T\) allows \(g_i\uparrow\kappa R\), this is only
\[
\left|1-(B\mathbf 1)_i\right|\le 1+O(\delta/(\kappa R)),
\]
not \(O(\delta/(\kappa R))\).

Likewise, for the principal block,
\[
(B^2-B)_{iT}=-\sum_{k\notin T}P_{ik}P_{kT},
\]
so
\[
\|(B^2-B)_{iT}\|_1
\le (1+2\delta)\left(\frac{g_i+\delta R}{\kappa R}+\delta\right),
\]
again order one at the top-band boundary. The good \(O(\delta/(\kappa R))\) estimate holds for the original top vertex \(v\), since \(g_v=0\), but it does not propagate to all rows of \(T\).

The exact \(\delta=0\) Baake–Sumner anchor is solid: the local source gives the idempotent Markov normal form with equal positive recurrent rows and transient rows governed by those blocks ([equal-fin.tex](/home/tobias/Projects/almost-idempotent-positive-maps/refs/baake-sumner-2007.11433/equal-fin.tex:1060)). That kills closed shallow webs at \(\delta=0\). What is missing is the quantitative step that makes the shallow top-band web approximately closed before invoking stability.

**New Sub-Lemmas**

1. **Buffered leakage lemma, proved.** If \(g=Pg\), \(0\le g\le R\), row negativity is \(\le\delta\), and \(D_L=\{g\ge L\}\), then
\[
P_i^+(D_L)\le (g_i+\delta R)/L.
\]

2. **Principal-block residual lemma, proved.** For \(T=\{g< L\}\), \(B=P_{TT}\),
\[
|1-(B1)_i|\le (g_i+\delta R)/L+\delta,\quad
\|(B^2-B)_{iT}\|_1\le(1+2\delta)((g_i+\delta R)/L+\delta).
\]

3. **Exact no-web anchor, proved modulo routine W-translation.** At \(\delta=0\), Baake–Sumner recurrent blocks give equal-input coincident row clusters; transient rows lie in the convex hull of recurrent rows. Thus no hidden all-shallow top-band web survives in the exact Markov idempotent case.

4. **Quantitative B–S closure theorem, open.** Needed input:
\[
\sup_{i\in T}\sum_{j\notin T}|P_{ij}|=O(\delta/(\kappa R))
\]
or a substitute “escape to deep mass” statement. This is exactly the unproved content, not a consequence of \(g=Pg\).

**Calibration**

\(P(\)existential DMF true\()\): 0.62.  
\(P(\)this post-mortem and the displayed inequalities survive audit\()\): 0.86.

**Sharpest Structural Insight**

The Baake–Sumner stability theorem is not the first missing brick. Before it can apply, one must prove approximate closedness of the shallow web. The deficit equation gives closure only for rows with \(g_i\ll\kappa R\); boundary top-band rows can spend their own height budget to leak order-one mass out of the block. The surviving obstruction is therefore a skinny, layered hidden web, not an almost-closed Markov idempotent block already waiting for perturbative classification.