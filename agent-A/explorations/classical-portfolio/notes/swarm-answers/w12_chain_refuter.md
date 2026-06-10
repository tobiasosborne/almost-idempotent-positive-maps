**VERDICT: NOT-CONSTRUCTED.** I did not find an exact-rational long thin-chain `ΛR` instance satisfying all gates. The exact s5 seed remains the best verified template, but it stays in the low-height regime:

\[
\delta=\frac{1841}{1600000},\quad H=\frac1{1000},\quad
\widetilde\sigma_v=\frac1{2000},\quad
H/\tau=0.02948,\quad \widetilde\sigma_v<\tau .
\]

So it does not enter the requested `\widetilde\sigma_v>\tau` web regime. See [s5_refute.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/swarm-answers/s5_refute.md:1).

**Failure Map**

1. Literal s5 rank-3 line cannot host a strict long chain. If hidden rows are
\[
\lambda_i=(-a,y_i,1+a-y_i),
\]
then every hidden-column value is affine in `y`:
\[
P_{c(y),c_j}=\lambda(y)\cdot q_j.
\]
A strict interior edge would need
\[
f(y_i)=\varepsilon>0,\qquad f(y_{i-1})\le0,\quad f(y_{i+1})\le0,
\]
but since `y_i` lies between its neighbors,
\[
f(y_i)=\theta f(y_{i-1})+(1-\theta)f(y_{i+1})\le0.
\]
So the s5 geometry gives either a 2-cycle, or extra positive shortcuts. Not a long thin chain.

2. Adding private transverse coordinates makes the chain support possible, but snaps the negative budget. In the exact parametrization
\[
\Lambda=\begin{bmatrix}I\\ L\end{bmatrix},\qquad R=[I-QL\mid Q],\qquad LQ=B,
\]
a strict edge \(B_{i,i+1}=\varepsilon\) localized through a private coordinate of size \(\zeta\) forces a dual coefficient of size \(\varepsilon/\zeta\). Then an archetype row gets a negative entry of size
\[
P_{z_i,2}= -\frac{\varepsilon}{\zeta}(1+a-y_i-\zeta),
\]
while the hidden row identity also pays
\[
p_{c_i}|_{\rm arch}=\lambda_i-\varepsilon\lambda_{i+1},\qquad
\nu_{c_i}\gtrsim \varepsilon\zeta .
\]
Optimizing the tradeoff still leaves \(\delta\) on the order of \(\varepsilon\), so if
\[
\widetilde\sigma_v=\varepsilon>\tau=\sqrt{\delta},
\]
the small-\(\delta\) gate is lost.

3. Allowing idempotence to add skip edges fixes the algebra but destroys thinness. From
\[
P_{c_i,c_{i+2}}=\sum_j P_{c_i j}P_{j,c_{i+2}},
\]
the path \(c_i\to c_{i+1}\to c_{i+2}\) contributes \(\varepsilon^2\). If the direct skip edge is suppressed, negative cancellation must absorb it, costing order \(\varepsilon^2\). If the skip edge is kept, the component is no longer a thin chain; it has transitive positive shortcuts.

4. Collapsing carriers to avoid the transverse tax fails the multiplicity-correct vertex check. Exact duplicates are one geometric vertex, not a long chain of vertices; near-duplicates either expose or reduce back to the s5 low-height two-cycle mechanism.

**Structural Reason**

Thin chains do not seem to break the dimension-free constant because exact idempotence refuses to let a positive path remain both long and thin at small negative budget. The chain must choose one: affine collinearity forbids strict local support, transverse localization blows up the left inverse and hence \(\delta\), or idempotence fills in positive shortcuts. The surviving obstruction is still the quantitative support-graph/Baake-Sumner web, but not a simple long path with \(\widetilde\sigma_v>\tau\) and \(H/\tau\sim0.3\) at \(\delta\le0.01\). No files were changed.