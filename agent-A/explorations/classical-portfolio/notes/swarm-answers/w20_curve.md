# w20_curve — T1 PROVED (two-scale visibility lemma); T2 died at the quadratic normal bound (codex, 2026-06-11) [T1 pending audit]
# Brief: /tmp/codex-sigma-wall/w20_curve/brief.md. Long-form proof: experiments/out/w20_curve/proof.md.

VERDICT: T1 ONLY.

I wrote the long-form proof/verdict to [proof.md](/tmp/codex-sigma-wall/w20_curve/proof.md). It proves the audit gap in a robust two-scale form: fixed positive recurrent mass gives an explicit visibility radius, and the `mu -> 0` case requires recoding to the boundary H-M stratum before applying the same visibility argument.

T2 is not proved. The exact failed estimate is the missing quadratic normal error bound:
\[
\|(C,D)_{\perp \mathcal M}\|^2 \le L_n\,\delta(P(C,D)).
\]
Without that, the chart only gives `H <= 2 delta + O(||(C,D)||^2)`, which does not close the local linear law.

Numerics are saved in [w20_curve_numerics.py](/tmp/codex-sigma-wall/w20_curve/w20_curve_numerics.py), [numerics_summary.txt](/tmp/codex-sigma-wall/w20_curve/numerics_summary.txt), and [numerics_results.json](/tmp/codex-sigma-wall/w20_curve/numerics_results.json). Corrected boundary/tiny sweep: worst stable `H/delta = 2.000000000012789`; tiny-mass stress reproduces the finite-scale transition around `mu ~= 1e-6`.

Verification run: `python3 -m py_compile w20_curve_numerics.py` passed, and the numerics sweep completed.
---
## THE FULL PROOF NOTE (proof.md, verbatim)

# VERDICT: T1 ONLY

I can prove the audit's missing visibility statement in the form actually
needed by the tangent-cone lemma: fixed-positive-mass visibility with an
explicit two-scale escape hatch as the minimum recurrent mass goes to zero.

I do **not** prove T2 as stated.  The chart computation gives the expected
estimate
\[
  H(P(C,D)) \le 2\,\delta_1(C,D)+K_n\|(C,D)\|^2,\qquad
  \delta(P(C,D)) \ge \delta_1(C,D)-K_n\|(C,D)\|^2,
\]
but this only implies
\[
  H(P(C,D))\le 2\delta(P(C,D))+K'_n\|(C,D)\|^2 .
\]
The missing estimate is the quadratic normal error bound which would replace
\(\|(C,D)\|^2\) by \(O_n(\delta)\) after quotienting the tangent directions
inside the nonnegative H-M locus.  That is exactly the still-open local
Baake-Sumner normal-form distance estimate, not a consequence of the audited
first-order lemma.

Numerics support the intended local picture after correcting near-duplicate
vertex tolerance: the worst stable exact-arc sample has \(H/\delta=2.00000000001\).
They do not supply the missing proof.

## 1. Notation

Let \(P_0\) be an H-M stochastic idempotent with recurrent blocks
\[
  C_1,\ldots,C_k,\qquad T=\{1,\ldots,n\}\setminus\bigcup_s C_s ,
\]
block laws \(\pi_s>0\) on \(C_s\), and transient rows
\[
  p_i^0=\sum_s\alpha_{is}\pi_s,\qquad i\in T .
\]
For recurrent \(i\in C_s\), put \(\alpha_i=e_s\).  Write
\[
  \mu(P_0):=\min_{s}\min_{j\in C_s}\pi_s(j).
\]
For a row vector \(x\), set
\[
  \Gamma_s(x)
  :=\sum_{j\in C_s}x_j+\sum_{\ell\in T}x_\ell\alpha_{\ell s}.
\]
Then \(xP_0=\sum_s\Gamma_s(x)\pi_s\) and \(\|\Gamma_s\|_{\ell^1\to\mathbb R}\le1\).
The H-M exposing functional for the \(s\)-th recurrent point is
\[
  g_s(x):=1-\Gamma_s(x).
\]
At \(P_0\), if a row \(y=\sum_q\alpha_q\pi_q\) satisfies
\(\|y-\pi_s\|_1\ge\rho\), then
\[
  g_s(y)=1-\alpha_s={1\over2}\|y-\pi_s\|_1\ge{\rho\over2}.
\tag{1}
\]

The visible-set parameters are the report's parameters
\[
  \tau=\sqrt{\delta(P)},\qquad \rho=4\tau,\qquad \kappa={\tau\over4}.
\]

For perturbations use
\[
  \varepsilon(P,P_0):=\max_i\|p_i-p_i^0\|_1 .
\]

## 2. Two-Scale Visibility Lemma

Here is the explicit replacement for the unaudited semicontinuity paragraph.
It is deliberately stated with the needed robustness parameter for cluster
vertices; vertices without this margin are exactly the harmless near-duplicate
vertices whose loss changes the recurrent cluster hull only at the smaller
cluster scale.

**Lemma T1.**  Let \(P_0\) be as above, and let \(P\) be an exact row-stochastic
idempotent with \(\varepsilon=\varepsilon(P,P_0)\).  Fix a recurrent block
\(C_s\).  Let \(v\in C_s\) be a row vertex of the row set of \(P\).  Assume
there is an affine support functional \(\ell_v\) for \(p_v\) such that
\[
  \ell_v(p_v)=0,\qquad 0\le\ell_v(p_i)\le1\quad\text{for all rows }p_i,
\]
and, for every row whose shifted block exposer is negative,
\[
  g_s(p_i)-g_s(p_v)<0\quad\Longrightarrow\quad \ell_v(p_i)\ge\eta .
\tag{2}
\]
If
\[
  \varepsilon\le
  \min\left\{ {\mu(P_0)\over8},\ {\tau\over64},\ {\eta\tau\over64},\ {1\over64}\right\},
\tag{3}
\]
then \(v\in W(P)\).

Moreover, any additional visible vertices can only decrease height:
if \(W_{\rm rec}\subseteq W(P)\), then
\[
  \dist(p_i,\conv W(P))
  \le \dist(p_i,\conv W_{\rm rec})
\]
for every row \(i\).

### Proof

Let
\[
  \widetilde g_i:=g_s(p_i)-g_s(p_v).
\]
Since \(g_s\) is \(1\)-Lipschitz in row \(\ell^1\),
\[
  |\widetilde g_i-(g_s(p_i^0)-g_s(p_v^0))|\le2\varepsilon .
\tag{4}
\]
The shift gives \(\widetilde g_v=0\).  The only possible violations of
nonnegativity are of size at most \(2\varepsilon\).  Define
\[
  \lambda={2\varepsilon\over\eta},\qquad
  f_i:=\widetilde g_i+\lambda\ell_v(p_i).
\]
By (2), \(f_i\ge0\) on every row.  Also \(f_v=0\), and
\[
  f_i\le 1+2\varepsilon+\lambda .
\]
Normalize
\[
  h_i={f_i\over 1+2\varepsilon+\lambda}.
\]
Then \(h\) is an admissible affine exposer for \(p_v\).

It remains to check the \((\rho,\kappa)\)-margin.  If
\(\|p_i-p_v\|_1\ge\rho\), then
\[
  \|p_i^0-\pi_s\|_1\ge \rho-2\varepsilon .
\]
Using (1) and perturbing \(g_s\) once more,
\[
  \widetilde g_i
  \ge {\rho-2\varepsilon\over2}-2\varepsilon
  =2\tau-3\varepsilon .
\]
The support term is nonnegative, so
\[
  h_i\ge {2\tau-3\varepsilon\over 1+2\varepsilon+2\varepsilon/\eta}.
\]
Under (3), \(2\varepsilon+2\varepsilon/\eta\le\tau/16+\tau/32<1/8\), and
\[
  h_i\ge {2\tau-\tau/16\over 9/8}>{\tau\over4}=\kappa .
\]
Thus \(v\) is visible.

The final monotonicity claim is immediate from
\(\conv W_{\rm rec}\subseteq\conv W(P)\).

### Radius along a normalized exact arc

Let an exact arc be written as
\[
  P(t)=\exp(tY)P_0\exp(-tY),\qquad Y{\bf 1}=0,
\]
with \(\|Y\|_{\infty\to\infty}\le M\).  Then
\[
  \varepsilon(P(t),P_0)\le 2nM e^{2nMt}t .
\tag{5}
\]
Thus every \(\eta\)-robust recurrent-cluster vertex is visible for
\[
  0<t<r(P_0,\eta,M):=
  {1\over 4nM}
  \min\left\{
    {\mu(P_0)\over8},
    {\tau(t)\over64},
    {\eta\tau(t)\over64},
    {1\over64}
  \right\},
\tag{6}
\]
where the harmless factor \(1/(4nM)\) absorbs the exponential in (5).
Equivalently, whenever the two scales satisfy
\[
  \varepsilon(P(t),P_0)\ll \eta\tau(t)
  \quad\text{and}\quad
  \varepsilon(P(t),P_0)\ll\mu(P_0),
\tag{7}
\]
the visible recurrent hull used by the first-order proof is genuinely present.

### Honest \(\mu\to0\) version

If \(\mu(P_0)\) is tiny and \(t\) is not below the active-entry scale, the right
base point is not the original stratum.  Fix a threshold
\[
  \theta\ge 16\,\varepsilon(P(t),P_0).
\]
Move every recurrent coordinate with \(\pi_s(j)<\theta\) out of its recurrent
block and into the transient set, renormalizing the remaining recurrent law.
Call the resulting boundary H-M point \(P_0^{(\theta)}\).  Then
\[
  \varepsilon(P_0,P_0^{(\theta)})\le 4n\theta,
  \qquad
  \mu(P_0^{(\theta)})\ge\theta
\tag{8}
\]
on each surviving recurrent coordinate.  Applying the fixed-mass part to
\((P_0^{(\theta)},P(t))\) gives visibility once the separated scales
\[
  \varepsilon(P(t),P_0^{(\theta)})\le c\,\eta\,\tau(t)\theta
\tag{9}
\]
hold.  This is the precise two-scale cure for the audit warning: before the
arc is below the tiny recurrent mass, one must recode to the boundary stratum;
after recoding, the surviving recurrent masses again have a positive radius.

This disarms the report's "naive compactness" dead route only at the Dini/local
visibility level.  The visible set \(W\) still jumps in ordinary compactness
limits; the proof above avoids the jump by keeping the two scales
\(\varepsilon\) and \(\mu\) separated, or by changing to the boundary H-M
structure before applying visibility.

## 3. What the Exact Chart Gives

In the \(E\oplus F=\operatorname{im}P_0\oplus\ker P_0\) splitting, the exact
chart is
\[
P(C,D)=
\begin{pmatrix}
(I+CD)^{-1} & (I+CD)^{-1}C\\
D(I+CD)^{-1} & D(I+CD)^{-1}C
\end{pmatrix},
\qquad D{\bf 1}=0 .
\]
For \(\|(C,D)\|\le (4n)^{-1}\),
\[
  P(C,D)=P_0+A(C,D)+R(C,D),
\]
where \(A(C,D)\) is the tangent matrix and
\[
  \|R(C,D)\|_{\infty,1}\le K_n\|(C,D)\|^2
\tag{10}
\]
with, for example, \(K_n=64n^3\) in the max-row-\(\ell^1\) norm.  The diagonal
terms are exactly the quadratic corrections recorded in w18:
\[
  P_{EE}-I=-CD+O(\|(C,D)\|^3),\qquad
  P_{FF}=DC+O(\|(C,D)\|^3).
\]

Let
\[
  \delta_1(A)=\max_i\sum_{j:P_{0,ij}=0}(-A_{ij})_+ .
\]
The active-zero expansion gives
\[
  \delta(P(C,D))\ge \delta_1(A(C,D))-K_n\|(C,D)\|^2 .
\tag{11}
\]
The audited tangent lemma plus T1 gives, on the separated visibility scale,
\[
  H(P(C,D))\le 2\,\delta_1(A(C,D))+K_n'\|(C,D)\|^2 .
\tag{12}
\]
Combining (11) and (12) yields only
\[
  H(P(C,D))
  \le 2\,\delta(P(C,D))+(2K_n+K_n')\|(C,D)\|^2 .
\tag{13}
\]

This is the exact failed estimate for T2.  To finish T2 one needs a projection
or normal-error lemma of the form
\[
  \|(C,D)_{\perp \mathcal M}\|^2\le L_n\,\delta(P(C,D))
\tag{14}
\]
where \(\mathcal M\) is the nonnegative H-M locus inside the idempotent variety,
and the tangential part is removed before (13) is applied.  Equivalently, one
needs a direct second-order comparison saying that every zero-budget tangent
motion integrates inside the H-M locus to the required order, with the residual
quadratic height paid by quadratic negative mass.

I do not have (14).  Without it, (13) is too weak: \(\|(C,D)\|\) can be mostly
tangential to \(\mathcal M\), and the chart estimate does not distinguish that
harmless motion from a normal signed displacement.  This is the local version
of the Baake-Sumner normal-form distance problem.

## 4. T3 Dependence List and Global Gap

Dimension-free part:

- The audited first-order inequality
  \[
    \dot H^+_{P_0}(A)\le2\dot\delta_{P_0}(A)
  \]
  is dimension-free and independent of \(k\), \(\mu\), and the partition.

Where dependence enters:

- T1's fixed-stratum radius depends on \(\mu(P_0)\), because originally
  positive recurrent entries must stay positive before the active-zero
  derivative is valid.
- The robust-cluster part depends on the support margin \(\eta\) of the
  recurrent-cluster vertex.  Near-duplicate vertices require either merging
  at the smaller scale or accepting a smaller radius.
- The exact-chart quadratic constants \(K_n,K_n'\) grow with \(n\) through
  norm conversion and \((I+CD)^{-1}\) bounds.
- The \(\mu\to0\) repair introduces a threshold \(\theta\) and therefore
  a boundary-stratum choice; constants depend on the number of possible
  dropped coordinates, at worst \(n\).
- A full T2 proof would also need the still-missing \(L_n\) in (14).
  Nothing in this run makes that dimension-free.

Global gap:

Even a proved T2 would cover only a neighborhood of the H-M locus.  The full
small-\(\delta\) linear law still needs the separate statement that every exact
row-stochastic idempotent with sufficiently small \(\delta\) lies in that
neighborhood in the right Baake-Sumner normal-form sense.  I do not claim that.

## 5. Numerics

Artifacts in this workdir:

- `w20_curve_numerics.py`
- `numerics_summary.txt`
- `numerics_results.json`

The script reuses
`experiments/out/w19_tangent_audit/tangent_audit.py`, but clusters rows below
\(10^{-8}\) before numerical vertex tests.  This avoids false huge-height
spikes from near-duplicate recurrent rows whose separation is below the LP
vertex oracle's reliable tolerance.

Tiny-mass stress stratum:

```text
mu: 9.99999000001e-07
zero_budget_value: 0
zero_budget_dot_delta: 0
t=0.0001  delta/t=0.99000001  H/t=1.97999602002  H/delta=1.99999595962
t=3e-05  delta/t=0.9666667   H/t=2.99666057001e-05
t=1e-06  delta/t=9.99998999893e-07  H/delta=1
t=3e-07  delta/t=0  H/t=0
```

This reproduces the audit's finite-scale warning: above the \(10^{-6}\) active
entry scale, the apparent slope can be near \(2\); below it the Dini tail is
zero.

Boundary/tiny exact-arc sweep:

```text
samples: 348
finite_samples: 348
max_H_over_delta: 2.000000000012789
worst: name=random_007 budget=0.0 t=3e-06 delta=2.30693475042e-06
       H=4.61386950087e-06 H/delta=2.00000000001
```

Numerics therefore support the local law, including arcs crossing boundary
strata, but the proof still dies at the normal quadratic estimate (14).

Calibration:

\[
  P(\text{T1 survives audit})\approx0.78,\qquad
  P(\text{T2 as a theorem follows from current ingredients})\approx0.38,
\]
\[
  P(\text{dimension-free upgrade reachable without a new normal-distance lemma})
  \approx0.18 .
\]
