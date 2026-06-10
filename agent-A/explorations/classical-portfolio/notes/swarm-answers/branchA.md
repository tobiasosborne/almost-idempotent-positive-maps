VERDICT: STUCK — the precise failing inequality is the missing supplier-deficit lower bound
\[
A_v:=\sum_{s\in S_v}P_{vs}^+\,g_s
\;\ge\;
c_0\,\frac{H_v^2}{\sigma_v^2},
\]
for the distance-separator deficit \(g=H_v-\phi\). What is available is only the opposite-side budget
\[
A_v\le \delta\,R,\qquad R=\operatorname{osc}(g),
\]
from F-GB. With \(R\le 3\), the missing lower bound would imply
\[
c_0H_v^2/\sigma_v^2\le 3\delta
\quad\Rightarrow\quad
H_v\le \sqrt{3/c_0}\,\sigma_v\tau .
\]

**Partial Proof**

Assume first that \(v\) is a global top vertex for the chosen separator. Pick affine \(\phi\) with dual \(\ell^\infty\)-norm \(\le1\), \(\sup_{\operatorname{conv}W}\phi=0\), and \(\phi(p_v)=H_v\). Since \(v\) is top, \(\phi(p_i)\le H_v\) for all rows, so
\[
g_i:=H_v-\phi(p_i)\ge0,\qquad g_v=0,\qquad Pg=g.
\]
Also \(R=\operatorname{osc}(g)\le\operatorname{diam}_1(K)\le2+4\delta\le3\) for \(\delta\le1/4\).

For any row \(j\), subset \(E=\{k:g_k\ge\ell\}\), and positive mass \(\sigma=P_j^+(E)\), F-GB gives
\[
\sigma\ell\le g_j+\delta R.
\]
For \(j=v\), this is only
\[
P_v^+\{g\ge\ell\}\le \frac{\delta R}{\ell},
\qquad
A_v=\sum_{s\in S_v}P_{vs}^+g_s\le\delta R.
\]
This controls how high the supplier mass may sit in deficit level. It does not lower-bound its deficit in terms of \(H_v\).

Non-exposedness of \(v\) gives a blocker, not a contradiction. Since \(g/R\) is an admissible exposure function with value \(0\) at \(v\), hiddenness implies some \(\rho\)-far row \(b\) has
\[
g_b<\kappa R\le 3\tau/4.
\]
F-WR and F-BC can force external mass in a surrounding/self-indexed web under their side conditions, but they do not force \(A_v\gtrsim H_v^2/\sigma_v^2\). FA3 also records that the \(v\to v''\) max-selection route needs the unproved uniform \(\psi\)-gap, so it cannot supply the missing lower bound either.

**Stress Test**

The obstruction is real at the inequality level. Let \(\tau=\varepsilon\), \(\delta=\varepsilon^2\), \(\sigma_v=\sqrt\varepsilon\), supplier deficit \(\ell=\varepsilon^{3/2}\), and compensating negative mass \(\delta\) at level \(R=1\). Then
\[
\sigma_v\ell=\sqrt\varepsilon\,\varepsilon^{3/2}=\varepsilon^2=\delta R,
\]
so F-GB is exactly saturated. But taking \(H_v=\varepsilon\) violates \(H_v\le B\sigma_v\tau=B\varepsilon^{3/2}\) for small \(\varepsilon\). This is not a counterexample matrix; it shows the audited inequalities allow the two-level evasion.

**New Sub-Lemmas**

1. Supplier budget restatement: for top \(v\),
\[
A_v\le\delta R\le3\delta.
\]
Proof: direct F-GB with \(g_v=0\).

2. Conditional Branch A: if
\[
A_v\ge c_0H_v^2/\sigma_v^2,
\]
then Claim A holds with \(B_A=\sqrt{3/c_0}\). Proof shown above.

3. Status: the supplier-deficit lower bound is open; no audited fact proves it.

**Probabilities**

\(P(\)Claim A true\()\): 0.70.

\(P(\)this negative audit survives adversarial review\()\): 0.82.