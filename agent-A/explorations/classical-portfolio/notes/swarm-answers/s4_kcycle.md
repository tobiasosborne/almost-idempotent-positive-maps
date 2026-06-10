VERDICT: DIED-AT the missing μ-to-P closure / α-slack inequality.

For a closed shallow witness class \(C\), choose optimal witnesses
\[
(\mu^x,\alpha^x,\beta^x),\qquad x\in C,
\]
with \(\mu^x\) supported in \(C\). Let \(M_{xy}=\mu^x_y\), and let \(\pi M=\pi\). Averaging the dual identity (♦) gives the exact cancellation
\[
\sum_x\pi_x\sum_y \mu^x_y(p_y-p_x)=0,
\]
so the only remaining identity is
\[
\sum_x\pi_x\sum_k \alpha^x_k(p_k-p_x)
=
\sum_x\pi_x\sum_k \beta^x_k(p_k-p_x). \tag{S}
\]
Pairing with the canonical deficit \(g\):
\[
\sum_x\pi_x\sum_k \alpha^x_k(g_k-g_x)
=
\sum_x\pi_x\sum_k \beta^x_k(g_k-g_x), \qquad \sum_k\beta^x_k=t_x^*<\kappa.
\]
This is where the Perron attack dies. Stationarity makes the \(\mu\)-drift in \(g\) exactly zero:
\[
\sum_x\pi_x\sum_y\mu^x_y(g_y-g_x)=0,
\]
so a closed class is not contradicted unless one proves a new estimate controlling the averaged \(\alpha\)-slack, or proves that μ-closure implies approximate \(P\)-closure:
\[
\sum_{x\in C}\pi_x P^+_{x,C^c}\ll 1
\quad\text{or}\quad
\|P_{CC}^2-P_{CC}\|\ll 1.
\]
I do not see that implication. The witness Markov chain \(M\) is an LP-dual object, not the row-coefficient chain \(P\). Baake–Sumner applies to nonnegative idempotent Markov \(P\)-blocks, not to \(M\).

New sub-lemmas:

1. **Closed-class slack balance, proved.** The stationary average of (♦) over a μ-closed class gives exactly (S), and for every affine \(\psi\),
\[
\sum_x\pi_x\sum_k \alpha^x_k(\psi_k-\psi_x)
=
\sum_x\pi_x\sum_k \beta^x_k(\psi_k-\psi_x).
\]

2. **Edge separation only, proved.** If \(x\to y\), then \(\|p_x-p_y\|_1\ge \rho\). A closed communicating class need not be pairwise \(\rho\)-separated; non-adjacent vertices in a directed cycle may be close. Thus X1/F-WR cannot be invoked from closedness alone.

3. **μ-closure ≠ \(P\)-closure, open gap.** To use Baake–Sumner quantitatively one needs a shallow top-band block \(P_{CC}\) that is approximately stochastic/idempotent. The witness graph does not provide this.

Calibration: \(P(\)existential DMF true\()\approx 0.70\), mainly from RW + d12 saturation and failure to realize mutual-shadow webs. \(P(\)this post-mortem survives audit\()\approx 0.86\).

Sharpest structural insight: the Perron average is real but points the wrong way. It kills the μ-transport term exactly, leaving only LP slack. Therefore the closed-class obstruction is not “a Markov chain recurrent class” until one proves that optimal witness recurrence is also row-coefficient recurrence. The missing bridge is μ-to-\(P\) closure, not Perron theory itself.