# VERDICT: LEMMA HOLDS WITH REPAIR

The first-order inequality survives:

\[
\dot H^+_{P_0}(A)\le 2\,\dot\delta_{P_0}(A)
\]

for fixed H-M base point \(P_0\), exact \(C^1\) idempotent arcs, and tangent
\(A\) satisfying \(P_0A+AP_0=A,\ A\mathbf 1=0\).

The repair is textual/proof-level, not a counterexample: the sharpness claim
must be limited to the frozen recurrent-hull derivative. I did not confirm
that \(2\) is sharp for the actual visible-set height. In the explicit frozen
sharp \(n=3\) direction, the actual height is zero because the displaced row
itself becomes visible.

The proof note also needs the semicontinuity paragraph replaced by an explicit
two-scale visibility lemma. The lemma is pointwise at a fixed H-M base point;
the \(o(t)\) neighborhood is not uniform in the minimum positive recurrent
mass or in face depths of transient mixtures.

## Tangent Re-Derivation

For a row vector \(x\), set

\[
\Gamma_q(x)=\sum_{j\in C_q}x_j+\sum_{\ell\in T}x_\ell\alpha_{\ell q},
\qquad xP_0=\sum_q\Gamma_q(x)\pi_q .
\]

Let

\[
B_s=\sum_{r\in C_s}\pi_s(r)A_r .
\]

Averaging \(P_0A+AP_0=A\) over \(C_s\) gives \(B_sP_0=0\). Rowwise,

\[
A_i=\sum_s\alpha_{is}B_s+\sum_q\Gamma_q(A_i)\pi_q .
\]

For recurrent \(i\in C_s\), writing \(h_{iq}=\Gamma_q(A_i)\), this gives

\[
A_i=B_s+\sum_q h_{iq}\pi_q,\qquad
\sum_qh_{iq}=0,\qquad
\sum_{i\in C_s}\pi_s(i)h_{iq}=0 .
\]

For transient rows the same formula holds without the recurrent averaging
constraint. This matches the claimed tangent structure; I found no algebraic
error.

The first-order normal cost is also as claimed:

\[
\dot\delta(A)=\max_i\sum_{j:P_{0,ij}=0}(-A_{ij})_+ .
\]

Only active zero entries contribute to the derivative; positive H-M entries
stay positive for sufficiently small \(t\) at fixed \(P_0\).

## Core Inequality

For row \(i\), let \(S_i=\{s:\alpha_{is}>0\}\). The frozen distance to the
recurrent-hull tangent cone is

\[
D_i(A)=2\sum_{q\notin S_i}(-\Gamma_q(A_i))_+ .
\]

For \(q\notin S_i\),

\[
\Gamma_q(A_i)=\sum_{j:P_{0,ij}=0}w_{jq}A_{ij},
\]

where \(w_{jq}=1\) on \(C_q\), \(w_{jq}=\alpha_{jq}\) on transient columns, and
\(\sum_{q\notin S_i}w_{jq}\le1\) for each active zero column \(j\). Hence

\[
\sum_{q\notin S_i}(-\Gamma_q(A_i))_+
\le \sum_{j:P_{0,ij}=0}(-A_{ij})_+
\le \dot\delta(A),
\]

so \(D_i(A)\le2\dot\delta(A)\), uniformly in \(n,k,\pi,\alpha\).

## Visibility Repair

The claimant's paragraph is directionally right but too compressed. The needed
replacement is:

Along a fixed exact \(C^1\) arc, recurrent clusters remain \(O(t)\)-diameter
and different recurrent blocks remain \(2+O(t)\) apart. New visible vertices
can only enlarge the visible hull. Recurrent-cluster row vertices that are
needed at first order are visible after the local exposing rescaling; vertices
that fail this robust visibility lie \(o(t)\) inside the hull of the visible
cluster vertices.

The dangerous cone \(\dot\delta=0\) is especially constrained: for recurrent
rows, forbidden coefficients \(h_{iq}\) are rowwise nonnegative and have
\(\pi_s\)-weighted average zero, so they vanish. That kills first-order hidden
cluster loss. Boundary transient rows are handled by the same face tangent-cone
condition.

This verifies the actual upper Dini derivative is bounded by the frozen
derivative, but only pointwise at the fixed base point.

## Constant Check

The \(n=3,k=2\) endpoint example certifies frozen sharpness. Take

\[
P_0=\begin{pmatrix}1&0&0\\0&1&0\\1&0&0\end{pmatrix},
\qquad
A=\begin{pmatrix}0&0&0\\0&0&0\\1&-1&0\end{pmatrix}.
\]

Then \(\dot\delta=1\), \(\Gamma_2(A_3)=-1\), and \(D=2\).
The exact arc \(P(t)=P_0+tA\) is idempotent and row-stochastic signed, with
\(\delta/t=1\). Its actual \(H/t=0\): the new row \((1+t,-t,0)\) is a visible
vertex and \(e_1\) lies between it and \(e_2\).

So \(2\) is sharp for the frozen bound; actual-height sharpness remains
unproved and may be false.

## Numerics

Independent code, not importing the claimant's decider:

- `tangent_audit.py`
- `targeted_checks.py`
- `semicontinuity_probe.py`

Large LP sweep:

- samples: 209 total, random seed 19020
- includes \(k=1\), boundary \(\alpha\), tiny recurrent masses near \(10^{-6}\),
  many transients, \(n\le12\), and the left-cone H-M anchor
- zero-budget max: `0.0`
- positive zero-budget count: `0`
- budget-1 max frozen derivative: `2.000000000000002`

Worst exact-arc spot check from the LP sample had
\(\dot\delta(A)=1.000000000000001\), \(2\dot\delta=2.000000000000002\), and
all sampled \(H/t\le0.098\), with exact idempotence residual around \(10^{-16}\).

The zero-budget exact-arc probe sampled 265 LP-generated directions with
\(\dot\delta=0\) and frozen \(D=0\). It found finite-scale stress when
\(t\) exceeded a \(10^{-6}\) recurrent mass: \(H/t\approx2\). Below that active
entry scale, the tail max was `0.0`. This is not a Dini refutation; it is a
warning that no uniform local radius follows from the lemma.

The refuted w19_leftcone family does not stress this lemma at first order:
at its H-M anchor, the derivative has \(\dot\delta=1\) and frozen \(D=0\).

## Remaining Gap

The proof note's remaining-gap description is basically honest but incomplete.
For the local linear law, this lemma alone does not supply:

- a uniform neighborhood over strata with \(\min\pi_s\to0\);
- control of second-order active-set changes when \(\dot\delta=0\);
- conversion of arbitrary small-\(\delta\) counterexamples into \(C^1\) arcs
  starting at an H-M point rather than merely approaching the H-M locus;
- treatment of non-\(C^1\)/Puiseux curve-selection arcs;
- a uniform stratum-boundary argument when transient \(\alpha\)'s lose support.

The zero-budget finite-scale probe is the concrete warning: before \(t\) is
below the smallest positive recurrent coordinate, originally positive entries
can cross zero and create apparent \(H/t\approx2\) even though
\(\dot\delta=0\).

## Calibration

P(this repaired first-order verdict survives further audit): `0.82`.

P(the unqualified phrase "sharp constant for actual H" survives): `0.35`.

P(this lemma alone gives the needed uniform local linear law): `0.18`.
