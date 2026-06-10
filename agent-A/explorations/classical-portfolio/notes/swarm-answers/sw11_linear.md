1. **VERDICT: DIED-AT**
Died at the quantitative web-exclusion inequality needed to prove the linear law:
\[
M_C(v):=\sum_{k:\,p_k\in \operatorname{conv}W}(P_{vk})_+ \ge c_0>0.
\]
What is proved is only the opposite one-sided fact
\[
M_C(v)\,H\le \nu_v R\le \delta R,
\]
so if \(H/\delta\to\infty\), then \(M_C(v)\to0\) and
\[
\widetilde\sigma_v \ge 1-\frac{\delta R}{H}.
\]
Thus a small-\(\delta\), non-linear counterexample must be an almost-closed shallow hidden web. I could not prove such webs impossible, nor construct one.

2. **Proof / Post-Mortem**
The d3/d7 “\(H\approx0.536\sqrt\delta\)” record is not analytically certified by the files I inspected. The saved small-\(\delta\) audit `d13_smalldelta.json` instead reports, for targets \(10^{-2},3\cdot10^{-3},10^{-3},3\cdot10^{-4}\), best verified ratios
\[
H/\tau=0.2000,\ 0.1095,\ 0.0632,\ 0.0346,
\]
exactly the budget-line behavior \(H\approx2\delta\), not \(H\approx c\sqrt\delta\). The large `d13_logs/d3e-*` “all-shallow” artifacts have actual \(\delta=10.54,6.85\), so they are not small-\(\delta\) evidence.

The analytic obstruction is now sharp: σ̃-small gives the linear law immediately,
\[
\widetilde\sigma_v\le s<1 \Rightarrow H\le \frac{\delta R}{1-s}.
\]
So the only possible refutation has \(\widetilde\sigma_v\to1\): almost all positive mass from \(v\) goes to non-\(W\), shallow, hidden vertices. Excluding that is exactly quantitative Baake–Sumner stability for shallow hidden webs.

3. **New Sub-Lemmas**
- **Height-collapse contrapositive.** If \(H>0\), then
\[
\widetilde\sigma_v \ge 1-\frac{\delta R}{H}.
\]
Proof: \(0=g_v=\sum_kP_{vk}g_k\), conv-\(W\) positive carriers have \(g_k\ge H\), and negative mass contributes at most \(\delta R\).

- **d3/d7 floor audit status.** The small-\(\delta\) floor is not verified by the saved outputs; the verified small-\(\delta\) search collapses to \(H=O(\delta)\). Status: numerical audit, not theorem.

4. **Calibration**
\[
P(\text{existential DMF true})\approx0.62.
\]
\[
P(\text{this sw11 linear-law diagnosis survives audit})\approx0.78.
\]

5. **Sharpest Structural Insight**
The linear-law question is equivalent to whether shallow hidden webs can carry essentially all positive mass. The old σ̃=0 witness mechanism is a corner-scale phenomenon; if \(H\gg\delta\), σ̃ must tend to 1 by a four-line inequality. So either the true small-\(\delta\) law is linear, or the missing counterexample is not a d8/d12 row-witness variant at all: it must be a genuinely new, almost-closed, mutually carrying hidden-vertex web.