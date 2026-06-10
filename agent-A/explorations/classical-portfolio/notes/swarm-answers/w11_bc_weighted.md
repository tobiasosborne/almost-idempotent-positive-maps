VERDICT: PARTIAL. Weighted contraction can be proved, but it does not kill the sup-leakage requirement needed by the t10 exposure finisher.

DIED-AT:
\[
\sum_i w_i\lambda_i\le \bar\eta
\quad\Longrightarrow\quad
\sum_{i,j}w_iw_j\|K_i-K_j\|_1
 \lesssim { \bar\eta+\delta \over 1-q}
\quad\not\Longrightarrow\quad
\sup_{i\in T}\|K_i-K_v\|_1=O(\tau).
\]

**Weighted Finisher**
Let \(K\) be a nonnegative stochastic kernel with Dobrushin/Birkhoff contraction
\[
\|\mu K-\nu K\|_1\le q\|\mu-\nu\|_1,\qquad q<1.
\]
Write \(r_i=e_iK\), \(e_i=\|r_iK-r_i\|_1\), and \(E_w=\sum_i w_i e_i\). Then
\[
\|r_i-r_j\|_1
\le e_i+q\|r_i-r_j\|_1+e_j,
\]
so
\[
\|r_i-r_j\|_1\le {e_i+e_j\over 1-q}.
\]
Averaging gives the sharp weighted version:
\[
D_w:=\sum_{i,j}w_iw_j\|r_i-r_j\|_1
\le {2E_w\over 1-q}.
\]
If averaged block leakage gives \(E_w\le C(\bar\lambda_w+\delta)\), this proves only
\[
D_w\le {2C(\bar\lambda_w+\delta)\over 1-q}.
\]

**Counterexample**
For \(0<\theta\ll1\), set
\[
\pi_\theta=\left({1-\theta\over2},{1-\theta\over2},\theta\right),\qquad
r_\theta=\left({3(1-\theta)\over4},{1-\theta\over4},\theta\right),
\]
\[
K_\theta=
\begin{pmatrix}
\pi_\theta\\
\pi_\theta\\
r_\theta
\end{pmatrix},
\qquad
w=\pi_\theta .
\]
Then \(K_\theta\) is positive stochastic, its Hilbert row diameter is \(\log 3\), hence
\[
q\le \tanh(\log 3/4)=2-\sqrt3.
\]
But
\[
E_w=\sum_iw_i\|(K_\theta^2-K_\theta)_i\|_1
=\theta(1-\theta)^2\to0,
\]
while
\[
\operatorname{diam}_1\{K_{\theta,i}\}
=\|r_\theta-\pi_\theta\|_1
={1-\theta\over2}\to {1\over2}.
\]
So even bounded projective diameter plus vanishing weighted defect cannot imply exposure-grade sup collapse.

**Interior-Row Chase**
For \(T_t=\{g<t\}\),
\[
\lambda_i(t)\le {g_i+\delta\Omega\over t}+\delta.
\]
Rows with \(g_i\le t/2\) only give
\[
\lambda_i(t)\le {1\over2}+{\delta\Omega\over t}+\delta.
\]
At \(t=\kappa\Omega\), this is \(1/2+4\tau+O(\tau^2)\), not \(O(\tau)\). Iteration does not repair it:
\[
\|K^m-K\|_{\infty\to1}\le (m-1)\|K^2-K\|_{\infty\to1},
\]
hence
\[
D\le {2(m-1)\varepsilon\over 1-q^m}.
\]
Each contraction step pays the defect again. A \(1/2\)-leakage bound stays order-one; the t10 contradiction still needs \(\varepsilon=O((1-q)\tau)\).

**Renormalization Constraint**
Uniform band weights miss one bad row when \(|T|\) is large. Carrier or witness weights can give zero weight to the row that kills exposure. The s8 pushed-witness death certificate blocks the tempting fix: pushing through \(P\) changes the objective to
\[
{B+N\over M_F},
\]
and optimality would require \(M_F\ge 1+N/B\), impossible when \(N>0\) and \(B<\kappa<1\).

**New Sub-Lemmas**
1. Weighted idempotent-contraction lemma:
\[
D_w\le 2E_w/(1-q).
\]
2. Weighted leakage gives weighted collapse only, not sup collapse.
3. Three-row bounded-\(\Delta\) counterexample above.
4. Iterated contraction pays defect linearly:
\[
\|K^m-K\|\le(m-1)\|K^2-K\|.
\]

\(P(\text{linear law true})\approx0.65\).  
\(P(\text{this diagnosis survives audit})\approx0.87\).