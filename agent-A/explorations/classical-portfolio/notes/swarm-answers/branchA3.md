VERDICT: DIED-AT the required point-energy lower bound

I cannot honestly prove Branch A from the spectral/kernel-energy route. The attempted proof dies at:

\[
\exists f=Pf,\ \operatorname{osc}(f)\le 1
\quad\text{with}\quad
\Gamma^f_v:=P(f^2)_v-f_v^2 \gtrsim \left(\frac{H_v}{\sigma_v}\right)^2 .
\]

That inequality would close the branch, but I do not see a derivation from the audited facts. For the canonical height deficit \(g\), the opposite direction is what is proved:

\[
\sum_k P^+_{vk} g_k^2
\le R\sum_k P^+_{vk}g_k
\le \delta R^2,
\]

using F-GB. So the height-profile energy at \(v\) is already small enough to evade F-E starvation.

Post-mortem: F-E gives a useful conditional lemma. Since \(P^+_{vv}\ge 1-\sigma_v-O(\delta)\ge 1/2-O(\delta)\), if \(v\) itself has \(\Gamma^f_v\ge E\), then starvation forces

\[
E \lesssim \delta\,\operatorname{osc}(f)^2 .
\]

Thus Branch A would follow if one could manufacture a fixed profile with normalized point-energy
\(\Gamma^f_v \gtrsim (H_v/\sigma_v)^2\). But the natural variance heuristic only suggests an averaged cost \(H_v^2/\sigma_v\), which would give at best \(H_v\lesssim \sqrt{\sigma_v}\tau\), not \(H_v\lesssim \sigma_v\tau\). The missing extra \(\sqrt{\sigma_v}\) is exactly the gap.

New sub-lemmas from this pass:

1. Self-starvation lemma: high \(\Gamma_v\) at a row with self-mass \(\gtrsim1\) is impossible beyond \(O(\delta R^2)\).
2. Height-energy anti-lemma: for the audited deficit \(g\), F-GB bounds the local positive quadratic energy by \(\delta R^2\), so the canonical energy cannot prove Branch A.
3. Required missing lemma: a supplier-site profile must create point-energy \(\gtrsim(H_v/\sigma_v)^2\), not merely averaged variance.

P(true): 0.72 for Branch A, mainly from the d8/d9 numerical wall.  
P(survives audit): 0.80 for this DIED-AT diagnosis; 0.05 for the attempted spectral proof as a proof.

What I learned: the budget binds geometrically, not energetically. F-GB pushes \(v\)’s supplier mass into the same top zero-face, making it low-energy for the height profile; F-E only taxes high-energy sites that receive positive mass. The dangerous architecture can keep the relevant level-mixing in low-paid or orphan rows, so a proof needs a supplier/exposedness certificate, not just \(P\Gamma=0\).