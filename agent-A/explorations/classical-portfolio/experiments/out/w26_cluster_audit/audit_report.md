# VERDICT: HOLDS WITH IMPROVEMENT

The rank-conditioned w26 chart is not false, but its headline coefficient
constant

\[
A=R(1+R)^{k-1}
\]

is a proof-ordering artifact.  There is a clean replacement:

\[
\boxed{A=1,\qquad \Lambda\le 1,\qquad E\le R\eta}
\]

after choosing a maximum-volume basis of actual rows.  This is dimension-free.
The old greedy recursion is valid but unnecessarily weak.

The clustered chart must be read in the precise one-shot sense: choose the
basis first, then take eta-balls around those pivots.  A generic "merge rows
whenever they are within eta" or single-linkage clustering is broken by
bridging chains even for nonnegative stochastic idempotents.

Calibration:

\[
P(\text{this verdict survives})=0.88.
\]

I would not raise the probability for the full global theorem by the same
amount.  The chart-level rank disease is removable, but L3 still needs a
dimension-free mass-concentration/support-margin estimate for the rows outside
the eta-clusters.

## Corrected Chart

Let

\[
P^2=P,\qquad P{\bf 1}={\bf 1},\qquad
\delta=\max_i\sum_j(-P_{ij})_+,\qquad R=1+2\delta .
\]

Then every row \(p_i\) has

\[
\|p_i\|_1\le R.
\]

Let \(V\) be the row space and \(k=\operatorname{rank}(P)\).  Choose \(k\)
actual rows

\[
r_s=p_{u_s},\qquad s=1,\ldots,k,
\]

maximizing the absolute determinant/volume among all row bases of \(V\), with
a deterministic lexicographic tie-break.

For every row,

\[
p_i=\sum_{s=1}^k\beta_s(i)r_s.
\]

By Cramer's rule,

\[
\beta_s(i)
=
{ \det(r_1,\ldots,p_i,\ldots,r_k)\over
  \det(r_1,\ldots,r_s,\ldots,r_k)} .
\]

The numerator is the determinant of another actual-row \(k\)-tuple, hence by
maximality

\[
\boxed{|\beta_s(i)|\le 1.}
\]

This is tight because \(\beta_s(u_s)=1\).

The old rank-gap lemma from w26 is correct:
for every proper subspace \(W<V\),

\[
\max_i\operatorname{dist}_1(p_i,W)\ge 1.
\]

Apply it to \(W_s=\operatorname{span}\{r_t:t\ne s\}\).  Pick a row \(p_i\)
with \(\operatorname{dist}_1(p_i,W_s)\ge1\).  Since

\[
p_i=w+\beta_s(i)r_s,\qquad w\in W_s,
\]

we have

\[
1\le \operatorname{dist}_1(p_i,W_s)
=|\beta_s(i)|\operatorname{dist}_1(r_s,W_s)
\le \operatorname{dist}_1(r_s,W_s).
\]

Therefore the \(s\)-th coordinate functional has operator norm

\[
\|\beta_s\|_{(V,\|\cdot\|_1)^*}
=\operatorname{dist}_1(r_s,W_s)^{-1}\le1.
\]

Consequences:

1. The basis rows are pairwise \(1\)-separated.
2. For \(\eta\le1/4\), eta-balls around pivots are disjoint.
3. If \(i\in M_s:=\{i:\|p_i-r_s\|_1\le\eta\}\), then

\[
|\beta_t(i)-\delta_{st}|
\le \|p_i-r_s\|_1
\le\eta .
\]

So the corrected constants are

\[
\boxed{A=1,\qquad F=\eta,\qquad \Lambda=1,\qquad E=R\eta.}
\]

The fixedness and sum identities are unchanged:

\[
P\beta_s=\beta_s,\qquad \sum_s\beta_s(i)=1.
\]

The proof is the same uniqueness-of-coordinates argument as in w26.

## Eta Scale

The chart itself does not force \(\eta=\sqrt\delta\).  Any
\(0<\eta<1/2\) gives disjoint pivot-balls and \(F=\eta\).

What the split-block family forces is only that an automatic merge scale must
dominate the linear split:

\[
\|q_1-q_2\|_1
= {4\epsilon(1+\epsilon)\over 1+2\epsilon}
=4\epsilon+O(\epsilon^2).
\]

Thus \(\eta=\delta\) with constant \(1\) fails on the split block; \(C\delta\)
with \(C>4\) would merge it.  The reason for \(\sqrt\delta\) is downstream,
not chart-level: if L3 has the usual competing terms

\[
\eta+\delta/\eta,
\]

then \(\sqrt\delta\) is the balancing scale.  \(\eta=\delta^{1/4}\) is
admissible for the chart but gives the weaker visible error
\(\delta^{1/4}\).  \(\eta\asymp\delta\) makes \(\delta/\eta\) order one in
that heuristic.

There is also tension with the w16 quotient-smearing caveat.  In the quotient
finisher, an eta-cluster perturbation can enter divided by a path scale
\(\theta\asymp\sqrt\delta\), so that route may require
\(\eta_{\rm cl}\lesssim\delta\).  The chart is robust at scale \(\sqrt\delta\);
the quotient finisher is not automatically robust to that large a clustering
scale.

## Independent Numerics

Artifacts:

- `independent_cluster_audit.py`
- `independent_cluster_results.json`
- `independent_cluster_summary.txt`

Verification:

```text
python3 -m py_compile independent_cluster_audit.py
python3 independent_cluster_audit.py
```

Both completed cleanly.

### Split Block

The repaired chart chooses pivots \([q_1,q_3]\), merges \(q_2\) into the
\(q_1\)-ball, and kills the old \(1/\delta\) coefficient blow-up.

| eps | old negative coeff mass | \(\|q_1-q_2\|_1\) | chart max coeff | merged H-M distance |
|---:|---:|---:|---:|---:|
| 1e-3 | 500 | 0.003996007984 | 1.0 | 0.002 |
| 1e-4 | 5000 | 0.000399960008 | 1.0 | 0.0002 |
| 1e-5 | 50000 | 0.000039999600 | 1.0 | 0.00002 |

The distance is \(2\delta\), as claimed.

### w19 Leftcone

For eps \(10^{-3},10^{-4},10^{-5}\), the chart keeps the three representative
rows separated.  The transient row remains convex.  Measured constants:

| eps | delta | eta | max coeff | max-volume Lambda |
|---:|---:|---:|---:|---:|
| 1e-3 | 1e-3 | 0.0316228 | 1.0 | 1.0 |
| 1e-4 | 1e-4 | 0.01 | 1.0 | 1.0 |
| 1e-5 | 1e-5 | 0.00316228 | 1.0 | 1.0 |

No leftcone pathology appears in this chart.

### Certified w16/w17 Instances

These are not in the small-delta corner, but they are useful regression tests.
The corrected chart stays bounded.

| instance | delta | eta | max coeff | max-volume Lambda | improved \(E=R\eta\) |
|---|---:|---:|---:|---:|---:|
| w16 best rational | 0.2284002679 | 0.4779124061 | 1.0 | 0.959757 | 0.696223 |
| w17 main rational | 0.2329335240 | 0.4826318721 | 1.0 | 0.959640 | 0.707474 |
| w17 robust rational | 0.2345924911 | 0.4843474900 | 1.0 | 0.959422 | 0.711596 |

The old singleton H-M candidate remains poor at these large deltas, but that
is the known nearest-branch issue, not coefficient blow-up.

## Decisive Rank-Growth Experiment

I tested a deliberately bad ordered simplex family.  It is already a
nonnegative stochastic idempotent.  Row 0 is the uniform transient row and rows
1 through \(k\) are singleton recurrent rows.  If the greedy chart starts with
row 0, the last vertex has coordinates

\[
e_k=k\,u-\sum_{s=1}^{k-1}e_s,
\]

so the greedy coefficient grows like \(k\).  A small row-sum-preserving
similarity smear was then applied and scaled to \(\delta=10^{-5}\).

| k | greedy max coeff after smear | max-volume max coeff | max-volume Lambda | claimed greedy bound |
|---:|---:|---:|---:|---:|
| 2 | 1.99998 | 1.0 | 0.999992 | 2.00006 |
| 3 | 2.99988 | 1.0 | 0.999996 | 4.00016 |
| 4 | 4.00001 | 1.0 | 0.999999 | 8.00040 |
| 8 | 7.99978 | 1.0 | 0.999999 | 128.0115 |
| 12 | 12.0004 | 1.0 | 0.999999 | 2048.266 |
| 16 | 15.9987 | 1.0 | 0.999999 | 32773.571 |

Conclusion: the recursive \((1+R)^{k-1}\) cascade is not intrinsic.  Even the
bad greedy ordering only shows linear growth in this stress family, while the
maximum-volume chart removes the growth completely.  The rank-dependence is
loose, not real, for the chart coefficient and coordinate-stability constants.

## Well-Definedness

The corrected chart is well-defined after a deterministic maximum-volume
tie-break.  If there are several maximum-volume bases, every one satisfies the
same constants \(A=1\), \(\Lambda\le1\), \(F=\eta\), and \(E\le R\eta\).

Representative choice needs care.  The bound \(F=\eta\) is for the pivot
representative \(r_s\).  If one names a cluster by an arbitrary member
\(h\in M_s\), then only

\[
\|p_i-p_h\|_1\le2\eta
\]

is automatic.  Re-basing on that arbitrary member is not covered unless the
new basis is again chosen by the maximum-volume rule.

Merge order is a real failure mode.  I built rank-2 nonnegative stochastic
idempotents with rows forming a chain from one recurrent row to the other.
At a threshold just above the consecutive spacing, single-linkage clustering
merges every row into one component, including both rank pivots.  The pivot-ball
chart keeps two clusters.

For a 24-point bridge:

```text
pivot-ball clusters: [[0, 1], [24, 25]]
single-linkage component: [[0, 1, 2, ..., 25]]
```

So the chart is robust only as one-shot final clustering around fixed pivots.
It is not an order-independent eta-clustering theorem.

For conjugation smearing \(P_\eta=SPS^{-1}\) with \(S{\bf1}={\bf1}\) and
\(S=I+O(\eta')\), idempotence and row sums persist.  The row geometry changes
by \(O(\eta')\), so after recomputing the maximum-volume chart the constants
remain dimension-free, with boundary rows allowed to change membership:

\[
F=\eta+O(\eta'),\qquad E\le R(\eta+O(\eta')).
\]

This is enough to cure exact-equality fragility in the chart.  It is not enough
to close the stronger w16 quotient finisher unless the extra
\(O(\eta')\) cost is compatible with that finisher's \(\theta\)-denominators.

## L3 Propagation

With the corrected chart, the merged sum rule is

\[
\delta_{st}
=
\sum_{j\in M_t}P_{u_sj}
\sum_{j\in B_\eta}\beta_t(j)P_{u_sj}
e_{st},
\qquad |e_{st}|\le R\eta .
\]

For \(s\ne t\),

\[
\sum_{j\in M_t}P_{u_sj}
=
-\sum_{j\in B_\eta}\beta_t(j)P_{u_sj}
O(R\eta).
\]

Since \(|\beta_t(j)|\le1\), the coefficient factor no longer carries any
rank-dependence.  But L3 still needs a dimension-free concentration estimate
such as

\[
\sum_{j\in B_\eta}|P_{u_sj}|\le C(\delta+\eta)
\]

or a support-margin argument that implies it.  Without that, the \(B_\eta\)
term is uncontrolled.

Thus the original L3 statement is incorrectly posed if it treats the w26
rank-dependent \(A\) as the essential obstruction.  The chart-level \(A\) can
be made dimension-free.  The real remaining obstruction is support
concentration outside the eta-pivot balls, plus compatibility with the
one-shot final-profile recoding discipline from w21.

Minimal dimension-free route:

1. Use the maximum-volume chart above, not the greedy ordered chart.
2. Prove a dimension-free bound on the \(P_{u_s}\)-mass of \(B_\eta\), measured
   in the final one-shot clustering/recoding profile.
3. Feed that bound into the corrected merged sum rule with \(E\le R\eta\).

The split-block obstruction is repaired.  The rank-dependent coefficient
disease is also repaired.  The global route is still not closed.
