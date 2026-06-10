VERDICT: **DIED-AT** the signed projective self-map requirement, not by LP collapse.

The Birkhoff route gives a useful conditional lemma. Let \(T=\{i:g_i<\kappa\Omega_g\}\), \(B=P_{TT}\), \(A=B^+\), and suppose the normalized nonnegative kernel \(K\) from \(A\) has projective row diameter \(\Delta\). Then its Dobrushin/Hilbert contraction coefficient is

\[
q\le \tanh(\Delta/4)<1.
\]

If also \(K\) is approximately idempotent,

\[
\|K^2-K\|_{\infty\to 1}\le \varepsilon,
\]

then for rows \(r_i=e_iK\),

\[
\|r_i-r_j\|_1
\le \|r_i-r_iK\|_1+\|r_iK-r_jK\|_1+\|r_jK-r_j\|_1
\le 2\varepsilon+q\|r_i-r_j\|_1,
\]

hence

\[
\operatorname{diam}_1\{r_i:i\in T\}
\le \frac{2\varepsilon}{1-q}.
\]

So a closed, bounded-projective-diameter shallow top block would collapse to an equal-input cluster. If the collapse radius is \(<\rho\), then \(g/\Omega_g\) exposes the top row, contradiction to \(v\notin W\). This is exactly the no-spectral-gap payoff Birkhoff should give.

The death point is that the hypotheses cannot be obtained from the current invariants. To make \(B\) a projective self-map, one needs a small top-band leakage bound

\[
\lambda_T:=\sup_{i\in T}\sum_{j\notin T}|P_{ij}|
=O\!\left(\frac{\delta}{\kappa\Omega_g}\right),
\]

because otherwise

\[
\|B\mathbf 1-\mathbf 1\|_\infty,\quad
\|B^2-B\|_{\infty\to1},\quad
\|K^2-K\|_{\infty\to1}
\]

are not small. But the harmonic deficit identity only gives

\[
P_i^+(T^c)
\le \frac{g_i+\delta\Omega_g}{\kappa\Omega_g}.
\]

For boundary rows with \(g_i\uparrow \kappa\Omega_g\), this is order one:

\[
P_i^+(T^c)\lesssim 1+O\!\left(\frac{\delta}{\kappa\Omega_g}\right).
\]

Thus the top-band block is not known to be an almost-stochastic, almost-idempotent positive kernel. Birkhoff has nothing to contract.

New objects/sub-lemmas:

1. **Projective idempotent-collapse lemma:** bounded Hilbert diameter plus \(\|K^2-K\|\le\varepsilon\) forces row collapse at scale \(2\varepsilon/(1-\tanh(\Delta/4))\).

2. **Signed Birkhoff reduction:** for \(B=P_{TT}\), \(A=B^+\), the needed perturbation size is \(C(\lambda_T+\delta)\).

3. **Death certificate:** current facts permit \(\lambda_T=O(1)\) on boundary top-band rows.

Unbounded projective diameter is not better: it becomes the support-graph Baake–Sumner stability problem. At \(\delta=0\), Baake–Sumner kills it; at \(\delta>0\), signed cancellations and arbitrarily thin support prevent a dimension-free threshold graph argument. The s5 low-height web is consistent with this.

Calibration: \(P(\)linear law true\()=0.72\). \(P(\)this Birkhoff post-mortem survives audit\()=0.82\).

What Birkhoff sees that the LP frame cannot: if a shallow top web were already a closed positive projective dynamical system, idempotence plus contraction would collapse it without any spectral gap. The obstruction is earlier and sharper: the web is not yet a closed positive projective system. The missing theorem is a signed top-band localization/closure theorem, not another exposedness-dual cleanup.