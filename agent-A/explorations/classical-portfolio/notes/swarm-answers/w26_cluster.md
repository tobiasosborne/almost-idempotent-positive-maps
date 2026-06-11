# w26_cluster — L2 PARTIAL: rank-conditioned clustered chart, explicit constants (codex, 2026-06-11) [audit in flight]
# Brief: /tmp/codex-sigma-wall/w26_cluster/brief.md. Long form: experiments/out/w26_cluster/proof.md.

VERDICT: PARTIAL.

I wrote the long-form artifact to [proof.md](/tmp/codex-sigma-wall/w26_cluster/proof.md). No `answer.md` was created.

What landed: a rank-conditioned clustered chart with explicit constants:
`eta = sqrt(delta)`, `F = eta`, `A = R(1+R)^(k-1)` with `R=1+2delta`, `k=rank(P)`. It kills the split-block `1/delta` coefficient blow-up, but the coefficient bound is rank-dependent, so I do not count this as the full W-free L2 needed for the global route.

Artifacts saved:
- [verify_cluster.py](/tmp/codex-sigma-wall/w26_cluster/verify_cluster.py)
- [cluster_results.json](/tmp/codex-sigma-wall/w26_cluster/cluster_results.json)
- [cluster_summary.txt](/tmp/codex-sigma-wall/w26_cluster/cluster_summary.txt)
- [progress.md](/tmp/codex-sigma-wall/w26_cluster/progress.md)

Verification:
- `python3 -m py_compile verify_cluster.py` passed.
- `python3 verify_cluster.py` reran cleanly.

Key numerical check: split-block old coeff negative mass is `500` / `5000`, while the repaired merged chart has max coefficient `1.0` and distance `2*delta`. L3 is stated precisely in `proof.md`; the remaining gap is a dimension-free support-margin/concentration estimate.
---
## Appendix: proof.md (verbatim)

# VERDICT: PARTIAL

I can prove the clustered-conditioning statement in a rank-conditioned form
which is strong enough to kill the split-block `1/delta` blow-up.  It has
explicit constants, is canonical after a deterministic pivot rule, and its
merged sum rules are exact up to a controlled `eta` error.

I do **not** regard this as the full W-free L2 needed for the global theorem:
the coefficient bound below depends on `k = rank(P)`.  The missing
dimension-free strengthening is exactly a support-margin/concentration estimate
for the merged coordinate simplex.  The first L3 estimate at the end records
the extra hypothesis under which that step works.

The proved chart also reselects the row basis after clustering.  In particular,
an old H-M `B` row may become a merged representative.  This is forced by the
split-block example: if one only merges the old representatives `{q1,q2}` and
does not promote `q3`, the merged chart loses rank and cannot represent the
matrix.

Calibration:

\[
P(\text{rank-conditioned L2 survives audit}) = 0.82,
\qquad
P(\text{W-free L2 as needed for L3/global follows from this}) = 0.38,
\]

and

\[
P(\text{L2+L3 reach the global statement}) = 0.31.
\]

## Setup

Let

\[
P^2=P,\qquad P{\bf 1}={\bf 1},
\]

and let

\[
\nu_i=\sum_j(-P_{ij})_+,\qquad \delta=\max_i\nu_i.
\]

Every row has total positive mass `1 + nu_i`, so

\[
\|p_i\|_1 = 1+2\nu_i \le R,\qquad R:=1+2\delta.
\]

For the small-delta use case take

\[
0<\delta\le {1\over 16},\qquad \eta:=\sqrt{\delta}.
\]

The split-block family forces any automatic pairwise merge scale to dominate
`4 delta + o(delta)`, since

\[
\|q_1-q_2\|_1={4\epsilon(1+\epsilon)\over 1+2\epsilon}<4\epsilon.
\]

Thus `eta = sqrt(delta)` is safely above the forced linear split scale for
`delta <= 1/16`, and it is also the scale that the old L3/L4 heuristic would
choose for an `eta + delta/eta` balance.

Because `P 1 = 1`, exact proportionality of rows means equality: if
`p_h = c p_u`, then `1 = p_h 1 = c p_u 1 = c`.  So the projective metric in
this stochastic setting is just row `l1` distance.

## The Rank-Conditioned Clustered Chart

Let `k = rank(P)`.  There are row representatives

\[
r_s=p_{u_s},\qquad s=1,\ldots,k,
\]

chosen from actual rows of `P`, and coefficient functions
`beta_s : {1,...,d} -> R`, such that:

1. The rows `r_1,...,r_k` form a basis of the row space.
2. Every row has the exact expansion

\[
p_i=\sum_{s=1}^k \beta_s(i) r_s.
\]

3. The coefficients are right fixed:

\[
P\beta_s=\beta_s.
\]

4. They are uniformly bounded in `delta`:

\[
|\beta_s(i)|\le A,\qquad
A:=R(1+R)^{k-1}.
\]

5. Their sums are exact:

\[
\sum_{s=1}^k\beta_s(i)=1\qquad\text{for every }i.
\]

The bound has no `1/delta` singularity.  Its weakness is the dependence on
`k`.

## Proof Of The Chart

The key linear-algebra fact is a rank gap for exact projections.

**Rank gap.** Let `W` be a proper subspace of the row space of `P`.  Then

\[
\max_i \operatorname{dist}_1(p_i,W)\ge 1.
\]

Indeed, if every row were within `<1` of `W`, choose rows `q_i in W` with
`||p_i-q_i||_1 < 1` and let `Q` be the matrix with rows `q_i`.  Then
`rank(Q) <= dim(W) < rank(P)`, while

\[
\|P-Q\|_{\infty\to\infty}
\le \max_i\|p_i-q_i\|_1 < 1.
\]

On the column image of `P`, the map `Q` is injective: if `x = Px` and `Qx=0`,
then

\[
\|x\|_\infty=\|(P-Q)x\|_\infty<\|x\|_\infty,
\]

unless `x=0`.  Hence `rank(Q) >= rank(P)`, a contradiction.

Now choose pivots greedily.  Start with any row, whose `l1` norm is at least
one because its row sum is one.  After choosing
`r_1,...,r_m`, if their span is still proper, the rank gap gives a row
`r_{m+1}` with

\[
\operatorname{dist}_1(r_{m+1},\operatorname{span}\{r_1,\ldots,r_m\})\ge 1.
\]

After `k` steps these rows span the row space.  Use a deterministic tie-break
(smallest row index among eligible pivots) to make this chart canonical for
the labelled matrix.

Let `V_m = span{r_1,...,r_m}`.  The coordinate functionals on `V_m` have
operator norm at most

\[
\Lambda_m\le (1+R)^{m-1}.
\]

For the induction step, write `x = y+c r_m`, with `y in V_{m-1}`.  Since
`dist(r_m,V_{m-1}) >= 1`,

\[
|c|\le \|x\|_1.
\]

The old coordinates are applied to `y=x-c r_m`, so their norm is multiplied by
at most `1+R`.  Therefore for the final basis

\[
\Lambda:=\max_s\|\beta_s\|_{(\operatorname{rowspace},\|\cdot\|_1)^*}
\le (1+R)^{k-1}.
\]

Since every row has `l1` norm at most `R`,

\[
|\beta_s(i)|\le \Lambda\|p_i\|_1\le R(1+R)^{k-1}=A.
\]

Applying row sums to `p_i=sum_s beta_s(i)r_s` gives

\[
1=p_i{\bf 1}=\sum_s\beta_s(i)r_s{\bf 1}
=\sum_s\beta_s(i).
\]

Finally, idempotence gives fixedness.  Since

\[
p_i=\sum_j P_{ij}p_j,
\]

and representation in the selected basis is unique,

\[
\beta_s(i)=\sum_jP_{ij}\beta_s(j),
\]

or `P beta_s = beta_s`.

## The Eta-Clustering

Let the exact 1.12 row classes be the exact equal-row classes.  For each pivot
row `r_s=p_{u_s}`, define the merged recurrent class

\[
M_s=\{i:\|p_i-r_s\|_1\le \eta\}.
\]

Because the pivots are `1`-separated and `eta <= 1/4`, the sets `M_s` are
disjoint.  Let

\[
B_\eta=\{1,\ldots,d\}\setminus\bigcup_s M_s.
\]

Then every merged class has an actual representative row, and every row in it
is close to proportional to that representative:

\[
\|p_i-r_s\|_1\le F(\eta,\delta),\qquad F(\eta,\delta)=\eta,
\qquad i\in M_s.
\]

Equivalently, because row sums are one, this is the projective row-distance
bound.

The coordinate vectors are also stable inside each merged class:

\[
|\beta_t(i)-\delta_{st}|
\le \Lambda\|p_i-r_s\|_1
\le \Lambda\eta,
\qquad i\in M_s.
\]

This is the quantitative replacement for exact proportionality.

## Merged Sum Rules

For a pivot row `u_s`, the exact fixed-coordinate identity gives

\[
\delta_{st}=\sum_j P_{u_sj}\beta_t(j).
\]

Split this over the merged classes and `B_eta`.  Since
`beta_t(j)=delta_{rt}+O(Lambda eta)` on `M_r`,

\[
\delta_{st}
=
\sum_{j\in M_t}P_{u_sj}
+\sum_{j\in B_\eta}\beta_t(j)P_{u_sj}
+e_{st},
\]

where

\[
|e_{st}|
\le
\Lambda\eta\sum_{r=1}^k\sum_{j\in M_r}|P_{u_sj}|
\le
\Lambda\eta\|p_{u_s}\|_1
\le
E,
\]

with

\[
E:=R(1+R)^{k-1}\eta.
\]

Thus the merged descendants of H-M (1.2)/(1.3) are:

\[
\left|
1-\sum_{j\in M_s}P_{u_sj}
-\sum_{j\in B_\eta}\beta_s(j)P_{u_sj}
\right|
\le E,
\]

and for `s != t`,

\[
\left|
\sum_{j\in M_t}P_{u_sj}
+\sum_{j\in B_\eta}\beta_t(j)P_{u_sj}
\right|
\le E.
\]

These are exactly the old sum rules with exact classes replaced by eta-merged
classes and with the controlled class-diameter error.

## Well-Definedness

The pivot rule "smallest eligible row index at each rank-gap step" gives one
canonical chart for a labelled matrix.  If one instead allows all admissible
pivot bases satisfying the same distance-to-previous-span condition, the set of
charts is finite.  All of them obey the same bounds `A`, `F`, and `E`.

Representative choices inside a merged class change the representative row by
at most `2 eta`, and hence change the coordinate values by at most
`2 Lambda eta`.  Therefore the merged sum rules change by at most
`2 R Lambda eta`.  This is the intended cure for the conjugation-smearing
problem: exact row equality is not used as a robust invariant, only the
eta-thickened row class is.

## Verification Families

The verifier is `verify_cluster.py`; saved outputs are `cluster_results.json`
and `cluster_summary.txt`.

### Split Block

For

\[
q_1=(1/2,1/2+\epsilon,-\epsilon),\quad
q_2=\left({1\over 2(1+2\epsilon)},1/2,{\epsilon\over1+2\epsilon}\right),
\quad
q_3=e_3,
\]

the unmerged exact chart with representatives `{q1,q2}` has

\[
a(q_3)=\left(-{1\over2\epsilon},1+{1\over2\epsilon}\right),
\]

so the negative coefficient mass is `1/(2 epsilon)`.

The clustered chart uses representatives `{q1,q3}` and merges `{q1,q2}`.
Then

\[
q_2={1\over 1+2\epsilon}q_1
+{2\epsilon\over1+2\epsilon}q_3,
\]

with convex coefficients.  The merged H-M candidate

\[
Q_\epsilon=
\begin{pmatrix}
1/2&1/2&0\\
1/2&1/2&0\\
0&0&1
\end{pmatrix}
\]

satisfies

\[
\|P_\epsilon-Q_\epsilon\|_{\infty,1}=2\epsilon.
\]

Numerics:

| instance | old negative coeff mass | old singleton distance | merged max coeff | merged distance |
|---|---:|---:|---:|---:|
| eps = 1e-3 | 500 | 2.0 | 1.0 | 0.002 |
| eps = 1e-4 | 5000 | 2.0 | 1.0 | 0.0002 |

Also `||q1-q2||_1` is `0.003996007984031963` for `eps=1e-3` and
`0.00039996000799837853` for `eps=1e-4`, so the `eta=sqrt(delta)` clustering
merges the split block.

### w19 Leftcone

For `eps=1e-3`, the representatives remain separated:

\[
\|r_0-r_1\|_1=2.0026666666666664,\quad
\|r_0-r_2\|_1=2.001333333333333,\quad
\|r_1-r_2\|_1=2.001333333333333.
\]

Since `sqrt(delta)=0.03162277660168379`, no merge occurs.  The row-4
coefficient is exactly convex `(1/3,1/3,1/3)`, the maximum coefficient negative
mass is `0`, and the direct H-M distance is `0.001999999999999963 = 2 delta`
up to roundoff.  This family remains harmless.

### Certified w16/w17 Rational Instances

These are above the small-delta corner, so this is not a small-delta
verification.  It checks only that the merged chart does not invent the
split-block pathology.

| instance | delta | sqrt(delta) | min representative distance | max coeff negative mass | old singleton distance |
|---|---:|---:|---:|---:|---:|
| w16 best rational | 0.2284002678967354 | 0.47791240609209484 | 2.3163720125974776 | 0.0037735849056603774 | 1.9372524801592854 |
| w17 main rational | 0.2329335240003862 | 0.4826318721348459 | 2.139613058458305 | 0.02387204535160837 | 1.8724196588770992 |
| w17 robust rational | 0.23459249106770677 | 0.4843474899983552 | 2.1406030934679188 | 0.02390954533290774 | 1.8857127302782624 |

The representatives are far apart relative to `sqrt(delta)`, so the simple
eta-clustering performs no recurrent merge.  Their coefficient negativity is
small; the poor singleton candidate is therefore not the same as the
split-block coefficient blow-up.  It is the already-recorded above-corner
nearest-branch problem.

## What L3 Still Needs

The merged sum rules give, for `s != t`,

\[
\sum_{j\in M_t}P_{u_sj}
=
-\sum_{j\in B_\eta}\beta_t(j)P_{u_sj}+O(E).
\]

Because entries are bounded below by `-delta`,

\[
\|p_{u_s}|_{M_t}\|_1
\le
\left|\sum_{j\in M_t}P_{u_sj}\right|+2\delta.
\]

Thus L3 would follow if one can show

\[
\sum_{j\in B_\eta}|P_{u_sj}| \le C(\delta+\eta)
\]

with a dimension-free constant, since `|beta_t(j)| <= A`.

The first estimate works under a support-margin hypothesis.  Suppose for a
fixed representative `s` and a bad set `U subset B_eta` there is a linear
functional `ell` on coefficient space with

\[
\ell(e_s)=0,\qquad \ell(\beta(j))\ge \rho>0\quad(j\in U),
\]

and

\[
|\ell(\beta(j))|\le L\quad\text{for all }j.
\]

Apply `ell` to the fixed-coordinate identity

\[
0=\sum_jP_{u_sj}(\beta(j)-e_s).
\]

The positive mass of row `u_s` on `U` is then bounded by

\[
\sum_{j\in U:P_{u_sj}>0}P_{u_sj}
\le {L\over \rho}\nu_{u_s}
\le {L\over \rho}\delta,
\]

provided the remaining positive terms have nonnegative `ell` value.  With a
finite cone cover this yields concentration on all separated bad coefficient
regions, but the constants depend on the support margin `rho` and, in the
naive cover, on the number of cones.

So the exact L3 requirement is:

**L3 needed statement.** From the rank-conditioned chart plus
`P_{ij} >= -delta`, prove a dimension-free lower support margin separating
the coefficient vector `e_s` from every row outside the eta-cluster `M_s`, or
replace that margin by a one-shot final-profile merge/recoding in the audited
w21 sense, measured in original merged mass.  Then the displayed estimate gives
each representative row within

\[
G(\delta,\eta)\simeq E + C\delta/\rho + 2\delta
\]

of an equal-input block, and every `B_eta` row within the corresponding
coefficient-clipped convex mixture.

This is the current stopping point.  The split-block obstruction is repaired,
but the W-free concentration estimate is not yet proved.
