# w27_concentration — L3 DIED-AT: O(delta) false (rank-2 family), the sqrt(delta) face estimate is the last piece (codex, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w27_concentration/brief.md. Long form: experiments/out/w27_concentration/proof.md.

VERDICT: **DIED-AT**.

Long-form artifact is in [proof.md](/tmp/codex-sigma-wall/w27_concentration/proof.md). Progress is in [progress.md](/tmp/codex-sigma-wall/w27_concentration/progress.md). I did not create `answer.md`.

What landed:
- In-class concentration: `G1(delta, eta) = eta + 2 delta`.
- Cross-cluster representative leakage:
  \[
  \sum_{j\in\cup_{t\ne s}M_t}(P_{u_sj})_+ \le \frac{2\delta}{1-\eta},
  \quad
  \ell^1 \le \frac{2\delta}{1-\eta}+\delta.
  \]
- Exact obstruction: an explicit rank-2 family has `delta(P)=delta`, `eta=sqrt(delta)`, and representative mass on `B_eta` equal to `sqrt(delta)`, so an `O(delta)` support-concentration estimate is false.

What remains missing is precisely:
\[
\max_s \sum_{j\notin M_s}|P_{u_sj}|
\le C\left(\eta+\frac{\delta}{\eta}\right)
\]
in the signed affine-face case. If that lands, the conditional L4 assembly in `proof.md` gives the W-free `O(sqrt(delta))` H-M distance in `||.||_{∞,1}`.

Numerics/code are in [analyze_l3.py](/tmp/codex-sigma-wall/w27_concentration/analyze_l3.py), [l3_numeric_results.json](/tmp/codex-sigma-wall/w27_concentration/l3_numeric_results.json), and [l3_numeric_summary.txt](/tmp/codex-sigma-wall/w27_concentration/l3_numeric_summary.txt). Verification passed:
`python3 -m py_compile analyze_l3.py`
`python3 analyze_l3.py`
---
## Appendix: proof.md (verbatim)

# VERDICT: DIED-AT

L3 is not proved in the form requested.  Two pieces do land with explicit
dimension-free constants:

1. in-class concentration at the clustering scale, and
2. cross-cluster concentration for representative rows, with an \(O(\delta)\)
   bound and no term count.

The support-concentration heart still needs one estimate which I cannot derive
from the audited tools:

\[
L_\eta:=\max_s\sum_{j\notin M_s}|P_{u_sj}|
\stackrel{?}{\le} C\left(\eta+{\delta\over\eta}\right).
\tag{L3-missing}
\]

The stronger \(O(\delta)\) version is false.  I give an exact rank-2 family
below with \(\delta(P)=\delta\), \(\eta=\sqrt\delta\), and

\[
\sum_{j\in B_\eta}(P_{u_1j})_+ = \sqrt\delta .
\]

Thus the ex-Hume-compatible rate, if this bridge closes, is necessarily
\(O(\sqrt\delta)\), not \(O(\delta)\).  The family does not refute the
\(O(\sqrt\delta)\) global target; it calibrates it.

Calibration:

\[
P(\text{this DIED-AT verdict survives audit})=0.80,
\qquad
P(\text{the global statement is still true via an }O(\sqrt\delta)\text{ L3})=0.58,
\]

\[
P(\text{this exact L3 route proves it without a new signed-face estimate})=0.24.
\]

Artifacts:

- `analyze_l3.py`
- `l3_numeric_results.json`
- `l3_numeric_summary.txt`
- `progress.md`

Verification:

```text
python3 -m py_compile analyze_l3.py
python3 analyze_l3.py
```

Both passed.

## Setup Imported From L1/L2

Let

\[
P^2=P,\qquad P{\bf 1}={\bf 1},\qquad
\nu_i=\sum_j(-P_{ij})_+,\qquad \delta=\max_i\nu_i,
\]

and write \(R=1+2\delta\).  Choose the audited maximum-volume actual-row basis

\[
r_s=p_{u_s},\qquad s=1,\ldots,k,
\]

with coordinate functions \(\beta_s\).  The imported w26 audit gives

\[
p_i=\sum_s\beta_s(i)r_s,\qquad
P\beta_s=\beta_s,\qquad
\sum_s\beta_s(i)=1,
\]

\[
|\beta_s(i)|\le1,\qquad
\|\beta_s\|_{(V,\|\cdot\|_1)^*}\le1.
\]

Take \(0<\eta\le1/4\), eventually \(\eta=\sqrt\delta\), and define the one-shot
pivot-ball clusters

\[
M_s=\{i:\|p_i-r_s\|_1\le\eta\},\qquad
B_\eta=[n]\setminus\bigcup_sM_s.
\]

The sets \(M_s\) are disjoint because the pivots are \(1\)-separated.

## L3(a): In-Class Concentration

For each pivot row \(r_s\), define its clipped probability row

\[
\widehat r_s={r_s^+\over 1+\nu_{u_s}}.
\]

Since \(r_s{\bf 1}=1\),

\[
\|r_s-\widehat r_s\|_1=2\nu_{u_s}\le2\delta.
\]

Therefore every row in \(M_s\) satisfies

\[
\boxed{\|p_i-\widehat r_s\|_1\le \eta+2\delta,\qquad i\in M_s.}
\tag{1}
\]

This proves the in-class concentration available from the max-volume chart.
It is \(O(\eta+\delta)\).  With \(\eta=\sqrt\delta\), it is
\(O(\sqrt\delta)\).  An \(O(\delta)\) in-class statement would require a
smaller clustering scale or an extra argument.

## Cross-Cluster Concentration

The key telescoping identity is scalar and does not count terms.  For a pivot
row \(u_s\),

\[
1=\beta_s(u_s)=\sum_jP_{u_sj}\beta_s(j),
\qquad
1=\sum_jP_{u_sj},
\]

hence

\[
\sum_jP_{u_sj}\bigl(1-\beta_s(j)\bigr)=0.
\tag{2}
\]

Because \(|\beta_s(j)|\le1\), we have \(0\le1-\beta_s(j)\le2\).  Thus the
positive contribution in (2) can be canceled by the negative part of row
\(u_s\) by at most \(2\nu_{u_s}\le2\delta\):

\[
\sum_{P_{u_sj}>0}P_{u_sj}\bigl(1-\beta_s(j)\bigr)\le2\delta.
\tag{3}
\]

If \(j\in M_t\) and \(t\ne s\), then

\[
|\beta_s(j)-\beta_s(u_t)|
\le\|p_j-r_t\|_1\le\eta,
\]

and \(\beta_s(u_t)=0\).  Hence \(\beta_s(j)\le\eta\), so
\(1-\beta_s(j)\ge1-\eta\).  Applying (3) to any union of other clusters gives

\[
\boxed{
\sum_{\substack{j\in\bigcup_{t\ne s}M_t\\P_{u_sj}>0}}P_{u_sj}
\le {2\delta\over1-\eta}.
}
\tag{4}
\]

Including the possible negative entries on those clusters,

\[
\boxed{
\sum_{j\in\bigcup_{t\ne s}M_t}|P_{u_sj}|
\le {2\delta\over1-\eta}+\delta.
}
\tag{5}
\]

For \(\eta\le1/2\), this is at most \(4\delta\) positive mass and \(5\delta\)
\(\ell^1\)-mass.  This is the desired dimension-free telescope: the cancellation
is charged to row negative mass, not to the number of columns.

## What Remains Uncontrolled

Equation (3) also gives, for any \(\rho>0\),

\[
\sum_{\substack{P_{u_sj}>0\\ \beta_s(j)\le1-\rho}}P_{u_sj}
\le {2\delta\over\rho}.
\tag{6}
\]

This controls all bad columns that lose a definite amount of the \(s\)-th
coordinate.  It also controls convex transient rows outside \(M_s\): if
\(\beta(j)\in\Delta_{k-1}\) and \(\|p_j-r_s\|_1>\eta\), then

\[
\eta<\|p_j-r_s\|_1
\le 2R(1-\beta_s(j)),
\]

so \(1-\beta_s(j)>\eta/(2R)\), and (6) gives

\[
\sum_{\substack{j\in B_\eta,\ P_{u_sj}>0\\ \beta(j)\in\Delta}}
P_{u_sj}
\le {4R\delta\over\eta}.
\tag{7}
\]

The missing case is the signed affine face

\[
\beta_s(j)\approx1,\qquad
\sum_{t\ne s}\beta_t(j)\approx0,
\]

where the row can be far from \(r_s\) because of a \(+/-\) coefficient pair.
The linear identities \(P\beta_t=\beta_t\) can cancel such rows in pairs using
positive mass alone.  A naive proof separates the possible negative-coordinate
sets and then pays for a cone cover depending on the number of coordinate
sign patterns.  I do not see a dimension-free telescope for that step.

The row-reproduction modulus also does not remove this gap.  It gives

\[
\operatorname{dist}\bigl(p_{u_s},\operatorname{conv}\{p_j:P_{u_sj}>0\}\bigr)
\le (2+4\delta)\delta,
\]

but a convex average of far rows in the exposed face \(\beta_s=1\) can still
equal \(r_s\).  That is exactly the cancellation geometry not seen by (6).

## B-Row Convexity Is Conditional On The Same Missing Estimate

For any row \(i\), put

\[
\mu_i=\sum_s(-\beta_s(i))_+.
\]

Clipping the coefficient vector to the simplex gives

\[
\operatorname{dist}_1\bigl(p_i,\operatorname{conv}\{r_s\}\bigr)
\le 2R\mu_i.
\tag{8}
\]

If one already knew a representative leakage bound

\[
L_\eta=\max_s\sum_{j\notin M_s}|P_{u_sj}|\le L<1/2,
\]

then the usual disjoint-support estimate would give

\[
\mu_i\le{\delta+L\over1-2L}.
\tag{9}
\]

Indeed, summing row \(p_i=\sum_s\beta_s(i)r_s\) over the union of clusters
corresponding to the negative coordinates of \(\beta(i)\), the negative
coefficients contribute at least \(\mu_i(1-L)\), while all positive
coefficients can leak into that union by at most \((1+\mu_i)L\).  Since the
negative part of \(p_i\) is at most \(\delta\), (9) follows.

Thus the \(B\)-row convex-mixture statement is not independently blocked; it
would follow from (L3-missing).  But without (L3-missing), (8) has no
dimension-free content because \(\mu_i\) may be large even though every
coordinate is bounded by \(1\).

## Conditional L4 Assembly

Assume the missing estimate is supplied in the form

\[
L_\eta\le C_L\left(\eta+{\delta\over\eta}\right)=:L,
\qquad L\le {1\over8}.
\tag{10}
\]

Construct an H-M point \(Q\) as follows.

1. For each \(s\), let \(\pi_s\) be the positive part of \(r_s\) restricted to
   \(M_s\), normalized to a probability row.
2. Put every row in \(M_s\) equal to \(\pi_s\).
3. For \(i\in B_\eta\), clip \(\beta(i)\) to the simplex and use that convex
   mixture of the \(\pi_s\)'s.
4. Put all transient columns \(B_\eta\) to zero.

This is an exact H-M stochastic idempotent.  The representative law error is

\[
\|r_s-\pi_s\|_1\le 2L+4\delta.
\tag{11}
\]

Using (1), (9), and (11), one obtains the explicit row-wise bound

\[
\boxed{
\|P-Q\|_{\infty,1}
\le \eta+12L+24\delta.
}
\tag{12}
\]

With \(\eta=\sqrt\delta\) and (10), this is

\[
\|P-Q\|_{\infty,1}
\le (1+12C_L)\sqrt\delta+(12C_L+24)\delta.
\]

This is the desired ex-Hume-compatible \(O(\sqrt\delta)\) bridge, but it is
conditional on exactly the missing leakage estimate.

## Exact Family Showing \(O(\delta)\) Support Concentration Is False

Let \(0<\delta<10^{-2}\), set \(\eta=\sqrt\delta\), \(\varepsilon=\eta\), and
\(m=\delta/\varepsilon=\sqrt\delta\).  Define

\[
B=
\begin{pmatrix}
1-m+\delta & -\delta & m\\
0&1&0
\end{pmatrix},
\qquad
L=
\begin{pmatrix}
1&0\\
0&1\\
1-\varepsilon&\varepsilon
\end{pmatrix},
\]

and put

\[
P=LB.
\]

Since

\[
BL=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix},
\]

we have \(P^2=P\).  Row sums are \(1\).  The maximum row negative mass is
exactly \(\delta\), attained in the first row:

\[
p_1=(1-\sqrt\delta+\delta,\ -\delta,\ \sqrt\delta).
\]

The second row is \(p_2=(0,1,0)\), and the third row is the convex coefficient
row

\[
p_3=(1-\varepsilon)p_1+\varepsilon p_2.
\]

The max-volume basis is \(\{p_1,p_2\}\).  The row \(p_3\) is not in the
\(\eta\)-ball around \(p_1\), because

\[
\|p_3-p_1\|_1
=\varepsilon\|p_2-p_1\|_1
=\sqrt\delta(2+2\delta)>\eta.
\]

Hence \(3\in B_\eta\).  But the representative row \(p_1\) places mass

\[
(P_{13})_+=\sqrt\delta
\]

on this \(B_\eta\) column.  Therefore no estimate of the form

\[
\sum_{j\in B_\eta}(P_{u_sj})_+\le C\delta
\]

can hold with \(C\) independent of \(\delta\).

The natural H-M projection, which zeros the transient column and normalizes the
first recurrent law, has row-wise distance

\[
\|P-Q\|_{\infty,1}=2\sqrt\delta+O(\delta).
\]

This is not a counterexample to the global \(O(\sqrt\delta)\) statement.  It is
a sharp warning that the last bridge lemma cannot honestly claim a linear
support-concentration modulus.

## Numerical Verification

The script `analyze_l3.py` checks the named families and random exact-variety
samples.  Summary:

```text
split_block_eps_0.001: delta=0.001 eta=0.0316228 pivots=[0, 2] B_eta=[] rep_cross=0 rep_B=0 HMdist=0.002
split_block_eps_0.0001: delta=0.0001 eta=0.01 pivots=[0, 2] B_eta=[] rep_cross=0 rep_B=0 HMdist=0.0002
split_block_eps_1e-05: delta=1e-05 eta=0.00316228 pivots=[0, 2] B_eta=[] rep_cross=0 rep_B=0 HMdist=2e-05
w19_leftcone_eps_0.001: delta=0.001 eta=0.0316228 pivots=[0, 1, 2] B_eta=[3] rep_cross=0.000666667 rep_B=0.001 HMdist=0.002
w19_leftcone_eps_0.0001: delta=0.0001 eta=0.01 pivots=[0, 1, 2] B_eta=[3] rep_cross=6.66667e-05 rep_B=0.0001 HMdist=0.0002
w19_leftcone_eps_1e-05: delta=1e-05 eta=0.00316228 pivots=[0, 1, 2] B_eta=[3] rep_cross=6.66667e-06 rep_B=1e-05 HMdist=2e-05
leakage_family_delta_0.001: delta=0.001 eta=0.0316228 pivots=[0, 1] B_eta=[2] rep_B=0.0316228 HMdist=0.0632456
leakage_family_delta_0.0001: delta=0.0001 eta=0.01 pivots=[0, 1] B_eta=[2] rep_B=0.01 HMdist=0.02
leakage_family_delta_1e-05: delta=1e-05 eta=0.00316228 pivots=[0, 1] B_eta=[2] rep_B=0.00316228 HMdist=0.00632456
w16_best_rational_above_corner: delta=0.2284 eta=0.477912 HMdist=0.479396
w17_main_rational_above_corner: delta=0.232934 eta=0.482632 HMdist=0.484047
w17_robust_rational_above_corner: delta=0.234592 eta=0.484347 HMdist=0.487488
random small-delta conjugations: samples=16 max_candidate_l1=0.00306482 max_rep_B_eta=0 max_rep_cross=0.000999395
```

Interpretation:

- split-block is repaired by the max-volume basis and merges correctly;
- w19 leftcone remains harmless, with leakage \(O(\delta)\);
- the new leakage family saturates the unavoidable \(\delta/\eta\) scale;
- certified w16/w17 are above-corner checks only, not small-\(\delta\) claims;
- random small-\(\delta\) exact conjugations did not find a worse pattern.

## Final Status

What is proved:

\[
G_1(\delta,\eta)=\eta+2\delta
\]

for in-class concentration, and

\[
\sum_{j\in\cup_{t\ne s}M_t}(P_{u_sj})_+
\le {2\delta\over1-\eta},
\qquad
\sum_{j\in\cup_{t\ne s}M_t}|P_{u_sj}|
\le {2\delta\over1-\eta}+\delta
\]

for cross-cluster representative leakage.

What is not proved:

\[
\sum_{j\in B_\eta}|P_{u_sj}|
\le C\left(\eta+{\delta\over\eta}\right)
\]

in the signed affine-face case.  This is the exact remaining estimate.  If it
lands, the conditional assembly above gives the global W-free
\(O(\sqrt\delta)\) H-M distance in \(\|\cdot\|_{\infty,1}\).  Without it,
L3+L4 are not established.
