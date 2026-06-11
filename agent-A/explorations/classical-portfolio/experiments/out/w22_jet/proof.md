# VERDICT: DIED-AT J1

J1 is false as stated.  The obstruction is not a numerical tolerance or a
tiny-mass transition.  At a boundary H-M base, there are exact nonnegative
H-M arcs which add support to a recurrent law.  Along those arcs
`delta = 0` to all orders, but the first jet is not tangent to the fixed
recoded boundary stratum.  Therefore the fixed-stratum normal projection has
positive size while the right-hand side of

```text
||(C,D)_{perp M}||^2 <= L * delta(P(C,D))
```

is zero.

This defeats the proposed dangerous-cone dichotomy in its strongest form:
there are second-order-flat, indeed all-order-flat, `delta` directions that
are not tangent to the fixed stratum.  They are tangent to a larger H-M
stratum.  Thus the sentence "the tangent cone of the delta=0 locus equals the
stratum tangent" is false at boundary strata.

This does not disprove the local linear law itself.  The counterexample has
`H = 0`, so `H <= C delta` is vacuous on it.  What fails is the proposed normal
projection estimate J1 with the normal taken against a fixed boundary stratum.
Consequently J2 cannot be assembled from the banked chain using this J1.

Artifacts:

- `jet_counterexample.py`
- `numerics_summary.txt`
- `jet_counterexample_results.json`
- `progress.md`

No `answer.md` was created.

## 1. Numerics First

I ran exact idempotent support-addition families near boundary H-M bases.
The summary from `numerics_summary.txt` is:

```text
records: 16
infinite_J1_ratios: 10
max_finite_normal_sq_over_delta: 0.10000000000000002
max_idempotence_err: 2.220446049250313e-16
max_row_stoch_err: 1.1102230246251565e-16
max_H_over_delta_finite: 0.0
```

Representative records:

```text
rank1_exact_chart 1e-08  delta=0  normal_norm_sq=1e-16  normal_sq/delta=inf
rank1_exact_chart 1e-04  delta=0  normal_norm_sq=1e-08  normal_sq/delta=inf
rank2_support_addition 1e-06  delta=0  normal_norm_sq=4e-12  normal_sq/delta=inf
rank2_support_addition 1e-03  delta=0  normal_norm_sq=4e-06  normal_sq/delta=inf
```

The finite ratios occur only on the opposite signed side of the rank-one
chart, where the new coordinate is negative and therefore pays linear
`delta`.  On the nonnegative support-adding side, every sampled point is an
exact row-stochastic idempotent and has `delta=0`.

## 2. Rank-One Exact-Chart Counterexample

Let

```text
P0 = [[1, 0],
      [1, 0]].
```

This is an H-M stochastic idempotent of rank one.  Its recurrent block is
`C={1}` and row `2` is transient with the unique coefficient of the unique
block.  The fixed H-M boundary stratum has no parameter, so
`T_{P0} M = {0}`.

Use the w18 exact chart.  Here

```text
E = im P0 = span{(1,1)}
F = ker P0 = span{e_2}.
```

The row-stochastic constraint forces `D=0`; the single chart coordinate is
`C=c`, where `C e_2 = c (1,1)`.  The projection onto `E` along
`graph(-C)` is exactly

```text
P(c) = [[1-c, c],
        [1-c, c]].
```

Direct checks:

```text
P(c)^2 = P(c),
P(c) 1 = 1,
rank P(c) = 1       for |c| small.
```

For every `c > 0` sufficiently small, `P(c)` is nonnegative.  Hence

```text
delta(P(c)) = 0.
```

The fixed boundary stratum tangent is zero, so the whole chart coordinate is
normal:

```text
||(C,D)_{perp M}||^2 = c^2
```

in the natural Euclidean chart norm.  In any other fixed norm on the chart it
is bounded below by a positive constant times `c^2`.  Thus J1 would require

```text
c^2 <= L * 0,
```

which is impossible for every `c > 0`.

The first jet is

```text
A = d/dc P(c)|_{c=0}
  = [[-1, 1],
     [-1, 1]].
```

At the active zero column `2`, the derivative is positive, not negative.
Thus `dot_delta(A)=0`.  But `A` is not tangent to the fixed H-M stratum,
because that stratum is a point.  The whole arc is inside the larger
nonnegative H-M locus with recurrent support `{1,2}` for `c>0`.

So this is an all-order-flat `delta` direction that is not fixed-stratum
tangent.

## 3. Rank-Two Variant

The same failure is not an artifact of rank one.  Let

```text
P0 = [[1, 0, 0],
      [0, 1, 0],
      [1, 0, 0]].
```

This is H-M with recurrent singleton blocks `C1={1}`, `C2={2}`, and a
transient row `3` on the boundary face `alpha_3=e_1`.

For `eps > 0`, define

```text
P_eps = [[1-eps, 0, eps],
         [0,     1, 0  ],
         [1-eps, 0, eps]].
```

Then

```text
P_eps^2 = P_eps,
P_eps 1 = 1,
rank P_eps = 2,
P_eps >= 0.
```

It is an H-M point with recurrent blocks `{1,3}` and `{2}`.  Therefore
`delta(P_eps)=0` and `H(P_eps)=0`.

Relative to the fixed recoded boundary profile at `P0`, however, the first
variation

```text
A = [[-1, 0, 1],
     [ 0, 0, 0],
     [-1, 0, 1]]
```

creates positive mass in the old transient column `3` of the recurrent block.
No tangent vector to the fixed support/face stratum can do that: fixed-stratum
H-M variations keep transient columns zero.  Even if one allowed the
transient coefficient `alpha_3` to leave its boundary face, that only changes
row `3` in columns `1,2`; it still cannot create column `3` in recurrent row
`1`.

Hence the projection of this first variation onto the fixed-stratum normal is
nonzero.  The script records the Frobenius-square proxy `4 eps^2`; any exact
chart norm is equivalent and gives a positive multiple of `eps^2`.  Since
`delta(P_eps)=0`, J1 fails again.

## 4. What Exactly Failed

The banked w19 tangent-cone lemma remains intact.  It says

```text
dot H+ <= 2 dot delta.
```

In the examples above, `dot delta=0` and also `dot H+=0`, so w19 is not
challenged.

The banked w21_second empirical observation also remains consistent: the
fixed-base dangerous directions do not produce positive second-order height.
Here the dangerous direction produces no height at all.  The failure is
geometric: the normal projection in J1 counts harmless support-adding H-M
motion as normal because the reference space is the tangent of one boundary
stratum rather than the tangent cone, or a local model, of the whole H-M
locus.

The bad implication is:

```text
delta vanishes to second order along a variety arc
=> the arc is tangent to the fixed H-M stratum to second order.
```

Corrected statement:

```text
delta vanishes along these arcs because the arc lies in an adjacent
nonnegative H-M stratum.
```

Thus the full `delta=0` tangent cone at a boundary H-M point strictly contains
the tangent space of the fixed stratum.

## 5. Consequence For J2

J2 asked for assembly of the local linear law if J1 holds.  Since J1 is false
as stated, the requested assembly cannot be made from this estimate.

The counterexample does not refute the local linear law:

```text
H(P(c)) = 0 = delta(P(c)),
H(P_eps) = 0 = delta(P_eps).
```

It refutes only the use of fixed-stratum normal distance as a quantity
controlled by `delta`.

To revive the route, one must replace J1 by a statement that first quotients
or absorbs all adjacent H-M support-addition directions.  Plausible repairs
are:

1. Project to the tangent cone, or to a finite union of tangent spaces, of the
   full H-M locus `I cap {P >= 0}` rather than to a single stratum tangent.
2. Rebase to the minimal H-M support/face profile containing the target point
   before measuring the normal component.
3. Prove a stratified error bound of the form

```text
dist_chart((C,D), M_HM)^2 <= L * delta(P(C,D)),
```

where the distance is to the local H-M set itself, not to one fixed stratum.

Only after such a repair would the one-shot final-profile recode, fixed-mass
visibility lemma, and w19 tangent lemma have a chance to assemble the local
linear law.

## 6. Dependence List

For the failed J1 there is no finite constant `L`, even with all data fixed:

- `n=2`, `k=1`, recurrent mass floor `mu=1`;
- `n=3`, `k=2`, recurrent mass floor `mu=1`;
- no small recurrent mass is involved;
- no LP support margin `eta` is involved in the rank-one example;
- the obstruction occurs at arbitrarily small chart radius.

Thus no dependence on `n`, `mu`, `eta`, block count, or profile can rescue J1
with the fixed-stratum normal used in the target.

For a repaired theorem, honest dependencies would include:

- the chosen local H-M stratification or final rebase profile;
- survivor recurrent mass floors `mu_m`;
- visibility margins `eta_m` and functional norms `Lambda_m` from w20/w21;
- a stratified quadratic error-bound constant for distance to the whole H-M
  locus;
- chart norm equivalence constants, which may depend on `n` unless proved
  uniformly.

Dimension-freeness would require a dimension-free version of that stratified
distance-to-H-M-locus estimate.  The present counterexample shows that a
dimension-free fixed-stratum estimate is not merely unproved; it is false.

## 7. Calibration

```text
P(J1 true as stated) = 0.00
P(J2 survives audit via this J1) = 0.00
P(local linear law still true after replacing J1 by a stratified/full-H-M
  distance estimate) = 0.78
P(a repaired J2 assembly survives audit once that estimate is available) = 0.55
```

