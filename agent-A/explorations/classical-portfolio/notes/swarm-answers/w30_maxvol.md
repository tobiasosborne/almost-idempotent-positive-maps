# w30_maxvol — DIED-AT the same interface: the transverse coefficient tax (codex, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w30_maxvol/brief.md. Long form: experiments/out/w30_maxvol/proof.md.

VERDICT: DIED-AT.

I wrote the long-form artifact at [proof.md](/tmp/codex-sigma-wall/w30_maxvol/proof.md). The max-volume route reduces the lemma to the transverse coefficient tax

\[
\sum_j(P_{u_sj})_+\sum_{t\ne s}(-a_t(j))_+ \le C_\mu\delta,
\]

and proves the target conditionally with \(C_D \le 2(1+2\delta_0)(2+C_\mu)\). I did not prove that tax; max-volume alone only gives the Cramer bounds and does not rule out the signed-face cancellation.

Saved and verified:

- [maxvol_displacement_audit.py](/tmp/codex-sigma-wall/w30_maxvol/maxvol_displacement_audit.py)
- [maxvol_displacement_summary.txt](/tmp/codex-sigma-wall/w30_maxvol/maxvol_displacement_summary.txt)
- [maxvol_displacement_results.json](/tmp/codex-sigma-wall/w30_maxvol/maxvol_displacement_results.json)
- [progress.md](/tmp/codex-sigma-wall/w30_maxvol/progress.md)

Verification passed:

```text
python3 -m py_compile maxvol_displacement_audit.py
python3 maxvol_displacement_audit.py
```

No `answer.md` was created.
---
## Appendix: proof.md (verbatim)

# VERDICT: DIED-AT

I did not prove the representative displacement lemma

\[
T_s:=\sum_j (P_{u_sj})_+\,\|p_j-p_{u_s}\|_1 \le C_D\delta
\tag{D}
\]

for the max-volume actual-row representatives.  I also did not find a
counterexample.  The max-volume route reduces the lemma to one precise missing
finite-dimensional estimate:

\[
\boxed{
M_s:=\sum_j(P_{u_sj})_+
\sum_{t\ne s}(-a_t(j))_+
\le C_\mu\delta .
}
\tag{M}
\]

Here \(p_j=\sum_t a_t(j)p_{u_t}\), \(|a_t(j)|\le 1\), and \(\sum_ta_t(j)=1\).
If (M) is supplied, then (D) follows with an explicit constant

\[
C_D \le 2(1+2\delta_0)(2+C_\mu).
\]

For example, if \(\delta_0\le1/4\), then \(C_D\le 3(2+C_\mu)\).

Calibration:

\[
P(\hbox{this DIED-AT diagnosis survives audit})=0.84,
\qquad
P(\hbox{representative displacement lemma is true})=0.66,
\]

\[
P(\hbox{max-volume alone proves the missing transverse tax})=0.18.
\]

No `answer.md` was created.

## 1. Coordinate Reduction

Let

\[
r_t=p_{u_t},\qquad p_i=\sum_{t=1}^k a_t(i)r_t,
\]

be the audited max-volume chart.  The imported w26 audit gives

\[
|a_t(i)|\le 1,\qquad \sum_t a_t(i)=1,\qquad P a_t=a_t.
\]

For a fixed representative \(s\), put

\[
v(j):=a(j)-e_s,\qquad
\lambda_s(j):=1-a_s(j),\qquad
\mu_s(j):=\sum_{t\ne s}(-a_t(j))_+ .
\]

Then \(\sum_tv_t(j)=0\) and

\[
\|v(j)\|_1=2(\lambda_s(j)+\mu_s(j)).
\tag{1}
\]

Since every basis row has \(\ell^1\)-norm at most \(R:=1+2\delta\),

\[
\|p_j-r_s\|_1
=\left\|\sum_t v_t(j)r_t\right\|_1
\le R\|v(j)\|_1
=2R(\lambda_s(j)+\mu_s(j)).
\tag{2}
\]

Thus

\[
T_s
\le 2R
\sum_j(P_{u_sj})_+\lambda_s(j)
+2R
\sum_j(P_{u_sj})_+\mu_s(j).
\tag{3}
\]

The first term is already controlled.  Applying \(P a_s=a_s\) to the row
\(u_s\),

\[
0=\sum_j P_{u_sj}(1-a_s(j)).
\]

Because \(0\le1-a_s(j)\le2\),

\[
\sum_j(P_{u_sj})_+(1-a_s(j))
\le
2\sum_j(P_{u_sj})_-
\le 2\delta.
\tag{4}
\]

Combining (3) and (4), the displacement lemma follows from (M):

\[
T_s\le 2R(2\delta+C_\mu\delta)
\le 2(1+2\delta_0)(2+C_\mu)\delta .
\]

This is the cleanest form of what remains.

## 2. Basis Geometry

The useful scale constants are:

\[
D_s:=\max_t\|r_t-r_s\|_1,\qquad
D:=\max_{q,t}\|r_q-r_t\|_1\le 2R,
\]

and the coefficient lower gap

\[
\gamma:=\inf_{\substack{c\ne0\\ \sum_tc_t=0}}
{\left\|\sum_t c_t r_t\right\|_1\over \|c\|_1}.
\]

For every row \(j\),

\[
\gamma\|a(j)-e_s\|_1
\le \|p_j-r_s\|_1
\le R\|a(j)-e_s\|_1.
\tag{5}
\]

Max-volume gives a dimension-free \(\ell^\infty\) lower bound, not an
\(\ell^1\) one:

\[
\max_t|a_t(j)-\delta_{ts}|
\le \|p_j-r_s\|_1.
\tag{6}
\]

Indeed each coordinate functional has operator norm at most \(1\) in the row
\(\ell^1\)-norm.  In particular the basis rows are pairwise \(1\)-separated:

\[
\|r_q-r_t\|_1\ge1\qquad(q\ne t).
\]

But (6) only implies \(\gamma\ge1/k\), which is rank-dependent.  The target
must therefore use the one-sided identity (4) and the missing transverse tax
(M), not norm equivalence alone.

## 3. What Idempotence Gives In Coordinates

Applying the coordinate map to

\[
\sum_jP_{u_sj}(p_j-r_s)=0
\]

gives the exact component identities

\[
\sum_jP_{u_sj}(a_t(j)-\delta_{ts})=0,
\qquad t=1,\ldots,k.
\tag{7}
\]

For \(t=s\), (7) is exactly the controlled deficit estimate (4).
For \(t\ne s\), it says only

\[
\sum_jP_{u_sj}a_t(j)=0.
\tag{8}
\]

Since \(a_t(j)\) has both signs, (8) does not control
\(\sum(P_{u_sj})_+(-a_t(j))_+\).  Positive mass can split between opposite
transverse coefficient directions and cancel inside (8).

The promised "second application of idempotence at coefficient level" is
tautological.  If \(L\) is the matrix of coefficient rows and \(B\) is the
matrix of representative rows, then

\[
P=LB,\qquad BL=I_k,\qquad PL=LBL=L.
\]

Thus the coefficient functions are fixed, but no new positive inequality is
created by iterating the coordinate equations.

The Hognas-Mukherjea 1.12 sum rules are the same identities grouped by exact
proportional-row classes.  In the row-stochastic specialization, proportional
rows in a class are equal, and the sum rules reduce to (7).  They do not bound
the \(B\)-row signed-face terms without an additional estimate such as (M).

## 4. What Max-Volume Forbids, And What It Does Not

Replacing the pivot \(r_s\) by a row \(p_j\) changes the basis volume by the
factor

\[
|a_s(j)|.
\]

Maximality is exactly the Cramer-rule bound \(|a_s(j)|\le1\).  More generally,
replacing several basis rows bounds the determinants of the corresponding
coordinate submatrices by \(1\).

This is not enough to rule out the signed face

\[
a_s(j)=1,\qquad \sum_{t\ne s}a_t(j)=0,\qquad
\sum_{t\ne s}|a_t(j)|>0.
\tag{9}
\]

Rows in (9) have replacement ratio \(1\).  They can tie the maximum-volume
basis while being far from \(r_s\) in transverse directions.

A concrete coefficient picture is

\[
x_\pm=e_s\pm a(e_t-e_r).
\]

Then \(e_s=(x_++x_-)/2\), while the single-swap volume ratio is
\(|(x_\pm)_s|=1\).  Even two-row swaps only impose restrictions such as
\(2a\le1\) in the \(k=3\) toy simplex; they do not force \(a=O(\delta)\).

The w29 transverse-pair idempotent realizes this geometry inside an exact
row-stochastic projection:

\[
a(3)=e_0+a(e_1-e_2),\qquad
a(4)=e_0-a(e_1-e_2),
\]

and the representative row \(0\) places positive mass on rows \(3,4\).  In
that family the near-positivity budget does charge the transverse amplitude:
\(\delta\sim a\), and \(T_0/\delta\to2\).  But the charge comes from row
near-positivity, not from max-volume maximality alone.

So the proposed geometric heart,
"a max-volume vertex cannot be an almost-convex average of far rows", is false
as stated.  It becomes plausible only after adding the missing transverse tax:
positive mass on such signed-face averages must pay row negative mass.

## 5. Numerical Audit

Artifacts:

- `maxvol_displacement_audit.py`
- `maxvol_displacement_results.json`
- `maxvol_displacement_summary.txt`
- `progress.md`
- `proof.md`

Verification:

```text
python3 -m py_compile maxvol_displacement_audit.py
python3 maxvol_displacement_audit.py
```

Both commands completed cleanly.

Key lines from `maxvol_displacement_summary.txt`:

```text
w27_rank2_leakage_delta_1e-05: T/delta=2.00002 lambda/delta=1 mu/delta~0
split_block_eps_1e-05:         T/delta=2.00002 lambda/delta=1 mu/delta~0
w19_leftcone_eps_1e-05:        T/delta=1.33335 lambda/delta=0.666667 mu/delta~0
transverse_pair_a_0.02_m_0.99: max_faceT/delta=2.0592 max_mu/delta=0.991584
w16_best_rational_above_corner: T/delta=2.42781
w17_main_rational_above_corner: T/delta=2.37327
w17_robust_rational_above_corner: T/delta=2.37642
random_hm_conjugation_summary: max_T/delta=3.27115 max_mu/delta=0.752089
random_coordinate_projection_summary: max_T/delta=3.95104 max_mu/delta=0.928359
```

The numerics support (D) and (M), including random exact \(LB\) projections.
They also show why (M) is the right missing statement: the sharp rank-2 and
split-block examples use the controlled \(\lambda\)-deficit, while the
transverse-pair row \(0\) has \(\lambda\approx0\) and all visible transport
comes from \(\mu\).

## 6. Minimal Handoff Fact

The minimal interface fact I would request from the telescope route is the
following dimension-free positive transverse variation bound:

\[
\boxed{
\sum_j(P_{u_sj})_+
\sum_{t\ne s}(-a_t(j))_+
\le C_\mu\delta
\quad\hbox{for every max-volume representative }u_s.
}
\]

Equivalently, after removing the already-controlled deficit term
\(1-a_s(j)\), positive representative mass cannot sit in mutually cancelling
signed-face directions except at total \(O(\delta)\) cost.

If a row-space rather than coefficient-space interface is preferred, the needed
form is:

\[
\sum_j(P_{u_sj})_+
\left\|
\sum_{t\ne s}a_t(j)(r_t-r_s)
\right\|_1
\le C_{\rm tr}\delta
\]

on the signed-face part \(a_s(j)\approx1\).  This is slightly closer to (D)
and avoids any rank-dependent lower conversion from row distance to coefficient
\(\ell^1\)-distance.

Everything else in the max-volume route is banked: Cramer's rule gives
\(|a_t|\le1\), the deficit identity gives (4), and (M) would give the displayed
constant for the displacement lemma.
