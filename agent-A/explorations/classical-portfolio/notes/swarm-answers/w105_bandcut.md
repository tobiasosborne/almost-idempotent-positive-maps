VERDICT: DIED-AT the uniform cut leakage estimate.

`t10_birkhoff.md` was not present at the requested path; I used the embedded t10 finisher in [wave5-sigma-wall-parallel.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave5-sigma-wall-parallel.md:725). The finisher is usable only after a uniform block-closure bound
\[
\lambda_T:=\sup_{i\in T}\sum_{j\notin T}|P_{ij}|\le c(1-q)\tau
\]
where \(q\le\tanh(\Delta/4)\). The adaptive level-cut/coarea argument does not give that.

**Precise Failure**

For \(T_t=\{j:g_j<t\}\), positive leakage from row \(i\in T_t\) satisfies the known bound
\[
\sum_{g_j\ge t}P^+_{ij}\le {g_i+\delta\Omega\over t}.
\]
Negative leakage adds only \(\le\delta=\tau^2\), so negativity is not the obstruction.

The proposed coarea average gives, for \(a<b\),
\[
\int_a^b \mathbf 1_{\{g_i<t\}}\sum_{g_j\ge t}P^+_{ij}\,dt
=
\sum_j P^+_{ij}\,[\min(b,g_j)-\max(a,g_i)]_+
\le g_i+\delta\Omega.
\]
Taking the relevant band \(a=\kappa\Omega/2,\ b=\kappa\Omega\), a boundary row with
\(g_i\approx a\) gives
\[
{1\over b-a}\int_a^b L_i(t)\,dt
\lesssim {a+\delta\Omega\over a}
=O(1),
\]
not \(O(\tau)\). With dense levels, for every \(t\) there may be some row just below \(t\) with order-one leakage. Thus pigeonhole controls at best a weighted average, not the required row supremum.

**Why Weighted Leakage Does Not Save It**

A weighted version would only give average collapse under the Birkhoff contraction. Hiddenness is blocked by any single \(\rho\)-far shallow row, even one with tiny or zero weight in the chosen measure. Without a uniform minorization or support-graph theorem, weighted leakage cannot imply the all-row collapse needed to expose \(v\).

**Conditional Assembly Still Valid**

If one had \(\lambda_T\le\eta\), then for \(B=P_{TT}\),
\[
\|B^2-B\|_{\infty\to1}\le (1+2\delta)\eta,
\]
and row normalization of \(B^+\) would give a nonnegative kernel \(K\) with
\[
\|K^2-K\|_{\infty\to1}\le C(\eta+\delta).
\]
The t10 finisher would then yield
\[
\operatorname{diam}_1\{\text{rows of }K\}
\le {2C(\eta+\delta)\over 1-q}.
\]
To make this \(<\rho=4\tau\), one needs \(\eta=O((1-q)\tau)\). The coarea estimate above only supplies \(O(1)\).

There is also a constants issue: a cut below \(\kappa\Omega\) only gives outside margin \(t/\Omega<\kappa\). To contradict hiddenness with the current \(W=(\rho,\kappa)\) convention, the final cut must be at or above \(\kappa\Omega\), or the constants must be reset.

**New Sub-Lemmas**

1. Level-cut coarea identity: proved above.
2. Uniform leakage obstruction: coarea over a \(\kappa\Omega\)-band gives only order-one boundary leakage for boundary rows.
3. Weighted finisher insufficiency: average residual implies average collapse, not exposure-grade uniform collapse.
4. Residual open branch: \(\Delta=\infty\) is exactly the zero-pattern/support-graph quantitative Baake-Sumner problem; s5’s low-height web lives in that danger zone.

So the band-cut closure lemma is still open; the linear law is not assembled.

Calibration: \(P(\text{linear law true})\approx0.65\).  
\(P(\text{this DIED-AT diagnosis survives audit})\approx0.86\).