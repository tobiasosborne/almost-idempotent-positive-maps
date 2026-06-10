**Verdict**

1. **Correct.** The relevant dual is
\[
\operatorname{dist}_1(x,C)=\max_{\|\phi\|_\infty\le 1}\{\phi(x)-\max_{y\in C}\phi(y)\}.
\]
On the affine hyperplane \(\sum x_i=1\), shifting by constants is harmless, so one may normalize \(\max_C\phi=0\). Thus \(\|\phi\|_\infty\le1\) is built in.

2. **Correct.** For
\[
f=\check\phi=\max(\phi-\mathrm{cap},0),
\]
\(f\) is convex and \(1\)-Lipschitz in \(\ell^1\). With \(y_i=\sum_j q_i(j)p_j\), repair gives
\[
f(p_i)\le f(y_i)+4\delta\le \sum_j q_i(j)f(p_j)+4\delta.
\]
So the sign is right: \(f\) is a \(4\delta\)-submartingale potential under the repaired chain.

3. **Correct, with the stated cap/oscillation condition.** If \(0\le f\le M\sim\tau\), \(L=A/\tau\), and \(\mu\) is the C2 quasi-stationary law on \(B\), then
\[
\mu f\le \mu T f+4\delta,
\qquad
|(\mu T-\mu)f|\le \|\mu T-\mu\|_1 M\le \frac{2M}{L}=O(\tau^2)=O(\delta).
\]
The exit loss is also \(M/L=O(\delta)\). Scaling \(f\) scales every term together. Powers \(f^r\) give repair error \(O(\delta\tau^{r-1})\) and exit/slop \(O(\tau^r/L)\), again matched. Signed exactness does not help by itself: \(O(\delta)\) negative mass on rows one unit lower can exactly compensate an \(O(\tau)\) exit from height \(O(\tau)\).

4. **Correct.** Optional stopping gives only
\[
\mathbb E\sigma \gtrsim \frac{\tau}{\delta}=\frac1\tau
\]
for dissipation from height \(\tau\), which is precisely the long-lifetime C2 branch.

5. **Correct as an averaging statement.** A \(\tau\)-plateau is not excluded by this potential/quasi-stationary averaging mechanism. Killing it needs geometry of vertices/exposedness or a sharper structural consequence of \(P^2=P\).

**Tau-Plateau Analysis**

The scalar plateau equations are consistent. Let plateau height be \(h=\tau\), exit \(\varepsilon\sim\tau\), and choose negative mass
\[
\eta=\frac{\varepsilon h}{1+h}\sim \tau^2=\delta.
\]
A bad row may have signed weights:
\[
(1-\varepsilon+\eta)\text{ on plateau rows},\qquad
\varepsilon\text{ on height }0,\qquad
-\eta\text{ on height }-1.
\]
Then the height equation is exact:
\[
h=(1-\varepsilon+\eta)h+\varepsilon\cdot0-\eta(-1).
\]
The repaired chain exits with probability \(\varepsilon/(1+\eta)\sim\tau\), so lifetime is \(\sim1/\tau\).

For a real matrix, the obstruction appears in block idempotence. With rows split into bad \(B\) and outside \(O\),
\[
P=\begin{pmatrix}A&U\\ V&R\end{pmatrix},
\qquad
P^2=P
\]
forces
\[
A^2+UV=A.
\]
If \(A\) has repaired lifetime \(1/\tau\), its signed row-sum defect is typically \(\Theta(\tau)\), so \(A-A^2\) must be supplied by \(UV\). Since \(U\) is the \(B\to O\) exit of size \(\Theta(\tau)\), exactness forces outside rows to feed back into \(B\) at order-one strength along the slow mode.

That feedback cannot come from already well-exposed \(W\)-vertices: if \(w\in W\) has exposer \(h_w\), then exactness gives
\[
0=h_w(w)=\sum_j P_{wj}h_w(p_j).
\]
Positive mass \(\beta\) from \(w\) into rows with \(h_w\ge\kappa\) contributes at least \(\beta\kappa\), while all negative cancellation is at most \(\delta\). Hence \(\beta\le \delta/\kappa=O(\tau)\). So any exact plateau must hide the required feedback in further non-exposed outside rows. That is the real structural pressure point.

**Candidate Lemma**

The proof-module that would forbid plateaus is:

> If \(B\) is a set of rows with \(\operatorname{dist}_1(B,\operatorname{conv}W)\ge D\tau\) and the repaired block \(q_{B\times B}\) has lifetime \(\ge a/\tau\), then \(B\) contains a row vertex of \(K\) that is \((C\tau,c\tau)\)-well-exposed.

This lemma is not produced by the averaging argument. It would have to use the exact feedback identity \(A^2+UV=A\) plus exposedness bounds to show that the required outside feedback chain cannot avoid creating a new well-exposed vertex.