**VERDICT: REFUTED** for the ψ-gap lemma as recorded. This does not refute HLC or the σ-wall programme; it refutes the standalone uniform ψ-gap input unless extra hidden-top/separator hypotheses are added.

**Formal Statement Used**
From the notes: `S` is “the site-support of the top cluster”; `S`-full means `S`-mass `>= 1-kappa`; `ψ = x(S)+λφ`; and the max-selection normalization is `ψ(v″)-ψ`. I formalized the recorded lemma as:

Let \(x(S)=\sum_{i\in S}x_i\), \(\lambda=1/2\), \(\psi(x)=x(S)+\lambda\phi(x)\), and let \(v''\) be a row vertex maximizing \(\psi\). Put
\[
Z=\max_{y\in K}\{\psi(v'')-\psi(y)\}.
\]
Then every row \(q\) with \(\|q-v''\|_1\ge\rho\) and \(q(S)<1-\kappa\) should satisfy
\[
\psi(v'')-\psi(q)\ge \kappa Z .
\]

**Counterexample**
For any integer \(m\ge 8\), set \(s=1/m\), \(\delta=s^2\), \(\tau=s\), \(\rho=4s\), \(\kappa=s/4\), and \(a=3s/8\).

Let \(P=\operatorname{diag}(B,H)\), where
\[
B=\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&1&0\\
0&1-a&a&0
\end{pmatrix}
\]
and
\[
H=I-u v^T,\quad
u=(1-s+s^2,-s,0)^T,\quad v=(1,-1+s,-s)^T.
\]
Then \(v^Tu=1\), \(v^T\mathbf 1=0\), hence \(H^2=H\), \(H\mathbf1=\mathbf1\). Thus \(P^2=P\), \(P\mathbf1=\mathbf1\). The only negative entry is \(-s^2\) in the Hume block, so \(\max_i\operatorname{neg}(p_i)=\delta\).

Take \(S=\{1,2\}\), \(\phi(x)=x_3\), and \(\psi=x(S)+\frac12\phi\). Let
\[
v''=p_1=(1,0,0,0;0,0,0),\quad q=p_4=(0,1-a,a,0;0,0,0).
\]
Then \(v''\) is a row vertex and a \(\psi\)-maximizer. Also
\[
q(S)=1-a=1-\frac{3s}{8}<1-\frac{s}{4}=1-\kappa,
\]
so \(q\) is non-\(S\)-full, and
\[
\|q-v''\|_1=2\ge 4s=\rho .
\]
But
\[
Z=1,\qquad \psi(v'')-\psi(q)=\frac a2=\frac{3s}{16}<\frac{s}{4}=\kappa Z.
\]
So the ψ-gap inequality fails exactly by the audited tradeoff: \(q\) loses \(S\)-mass but regains part of it through the \(\lambda\phi\) term.

**Calibration**
\(P(\)literal ψ-gap lemma true\() \approx 0.01\), only allowing for statement ambiguity.  
\(P(\)this refutation survives audit\() \approx 0.90\).  
Branch B still needs either a different route around the \(v''\) selection or a sharper inequality controlling the trade
\[
\lambda(\phi(q)-\phi(v'')) \le v''(S)-q(S)-\kappa Z .
\]