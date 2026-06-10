VERDICT: NOT-CONSTRUCTED.

I did not find a verified exact-rational instance with

\[
\delta\le 0.01,\qquad \widetilde\sigma_v>\tau=\sqrt\delta,\qquad H/\tau\ge 0.1 .
\]

The periodic-component attack was the priority. It gets closest structurally, but it fails the gates: either the period-two mass stays below \(\tau\), or increasing height makes the candidate rows well-exposed and they enter \(W\).

**Periodic/Cyclic Template**

I tested the frame form

\[
\Lambda=\begin{bmatrix}I\\L\end{bmatrix},\qquad
R=[I-QL\mid Q],\qquad P=\Lambda R,\qquad R\Lambda=I,
\]

with a strict period-two hidden block

\[
B=LQ=\begin{pmatrix}0&m\\ m&0\end{pmatrix}.
\]

A representative small-budget point:

\[
a=\frac1{2000},\quad y=\frac1{20},\quad Y=\frac{17}{20},\quad m=\frac1{200}
\]

gave

\[
\delta\approx0.006439,\quad \tau\approx0.080245,\quad
H\approx0.001,\quad H/\tau\approx0.0125,\quad
\widetilde\sigma_v=m\approx0.0623\tau .
\]

So it is periodic and hidden, but far below both target inequalities. Raising \(m\) raises \(\delta\) roughly linearly in this frame before \(\widetilde\sigma_v\) reaches \(\tau\). Raising \(a\) to make \(H/\tau\) larger triggers the margin-max exposedness gate: at \(a=1/100,m=1/200\), \(\delta=0.00995\) but the hidden rows join \(W\), so \(H=0\).

The diagonal idempotence identity only gives the weak quadratic obstruction

\[
m^2 \lesssim \delta,
\]

but the frame left-inverse adds the stronger observed tax

\[
\delta \gtrsim c_L m + O(a).
\]

That linear tax is what kills the 2-periodic construction at \(\delta\le0.01\).

**Trees/DAGs**

Branching does not reduce the row-budget cost because the idempotence error is additive in \(\ell^1\). If \(v\) sends total mass \(\sigma\) over \(N\) branches and each branch sends mass \(e\) onward, then the two-step mass is

\[
\sum_{r=1}^N \frac{\sigma}{N}e=\sigma e,
\]

not \(\sigma e/N\). Suppressing the induced shortcuts requires cancellation of total size \(\sigma e\). Keeping the shortcuts makes the component fat, so the component finisher applies.

**Frame-Coordinate Chains**

Chaining \(\Lambda\)-rows rather than \(P\)-rows changes the coordinates but not the obstruction. Since

\[
B_{ij}=\lambda_i\cdot q_j,
\]

a hidden-column value is affine along a collinear \(\Lambda\)-chain. A strict interior edge with both neighbors suppressed would require an affine function positive at an interior point and nonpositive at both neighbors, impossible. Adding transverse/private coordinates makes support possible, but the inverse scale appears in \(Q\), and archetype rows pay the negative mass.

**Parallel Chains / Multiplicity**

Parallel chains sharing endpoints do not help: their two-step contributions sum. Exact duplicate endpoints are one geometric vertex under the multiplicity-correct \(W\) test. Adding positive mass on duplicate rows without changing the realized barycenter requires an opposite signed duplicate coefficient, costing at least the added mass, so it cannot make \(\widetilde\sigma_v>\tau\) under \(\delta=\tau^2\).

No files were changed.