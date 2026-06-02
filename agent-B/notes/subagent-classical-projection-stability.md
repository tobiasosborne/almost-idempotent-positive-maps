# Subagent Note: Classical Projection Stability

## Status

The dimension-free linear theorem is false, already for `n=3`.

There is an explicit family of unital idempotents
`P_s: ell_infty^3 -> ell_infty^3` such that

```text
delta(P_s) = s^2,
dist(P_s, {row-stochastic idempotents}) = 2s - 2s^2 + 2s^3.
```

Thus no estimate `dist <= C delta^beta` can hold uniformly for any
`beta > 1/2`.  The exponent `1/2` is the best possible exponent if the
classical theorem is true in any power form.

## Counterexample Family

For `0 < s < 1`, set

```text
v_s = (1, -1+s, -s),
u_s = (1-s+s^2, -s, 0)^T,
P_s = I - u_s v_s^T.
```

Then

```text
v_s . 1 = 0,
v_s . u_s = (1-s+s^2) + (-1+s)(-s) = 1.
```

Therefore `P_s 1 = 1` and `P_s^2=P_s`.  Written by rows,

```text
P_s =
[ s-s^2      1-2s+2s^2-s^3      s-s^2+s^3
  s          1-s+s^2             -s^2
  0          0                    1        ].
```

All rows sum to `1`.  The only negative entry is `(P_s)_{1,2}=-s^2`, so the
row negative mass is exactly

```text
delta = s^2.
```

As `s -> 0`, this approaches the stochastic idempotent with rows
`e_1,e_1,e_2`, but for `s>0` the first two rows are split at order `s` while
the positivity defect is only order `s^2`.

## Distance Computation In `n=3`

The row-stochastic idempotents on three states are exactly:

1. the identity;
2. rank-one matrices with all rows equal to one probability vector;
3. one transient state and two absorbing singleton states;
4. one two-state recurrent class, whose two rows are equal to a probability
   vector on the pair, plus one absorbing singleton.

For `P_s`, the only nearby case is item 4 with recurrent pair `{0,1}` and
singleton `2`.  Such an idempotent has rows

```text
(a, 1-a, 0),
(a, 1-a, 0),
(0, 0, 1).
```

For any `a` in the interval where the first-row absolute values balance, the
row-0 distance is

```text
2(s-s^2+s^3).
```

The row-1 distance is only `O(s^2)` for the same choices of `a`, hence this
gives

```text
dist(P_s, stochastic idempotents) <= 2s - 2s^2 + 2s^3.
```

The other stochastic-idempotent types are farther for small `s`: rank-one and
wrong-pair cases are bounded below by an absolute constant, and the nearest
transient case forces row 1 to be `e_1`, giving distance `2s`.  Therefore, for
`0<s` small,

```text
dist(P_s, stochastic idempotents) = 2s - 2s^2 + 2s^3
                                 = 2 sqrt(delta) + O(delta).
```

This disproves the desired `O(delta)` stability.

## Interpretation

The obstruction sits at a boundary stochastic idempotent.  At `s=0`, state `0`
is effectively collapsed into state `1`.  For `s>0`, exact idempotency allows
state `0` and state `1` to separate by order `s`; the separation is paid for
by a single negative transition of size only `s^2`.  Any positive idempotent
must either identify the two rows again, costing order `s`, or make one of
them an absorbing/transient row, also costing order `s`.

This is a classical analogue of a second-order boundary escape: positivity
defect measures the amount by which the path exits the stochastic-idempotent
stratum, while distance to return to the stratum is first order.

## What Remains Open

This sidecar does not prove the positive `O(sqrt(delta))` theorem.  The example
shows that `sqrt(delta)` is the only plausible dimension-free power scale.

A general proof would likely need to handle boundary strata of stochastic
idempotents by clustering rows at scale `sqrt(delta)`.  The naive repair
"truncate negative entries rowwise" gives a stochastic matrix within `2delta`
and an `O(delta)` almost-idempotent stochastic matrix, but almost-idempotent
Markov kernels can still be `Theta(sqrt(delta))` from exact stochastic
idempotents by precisely the family above.

## Scratch Files

Created under the permitted experiment directory:

```text
agent-B/experiments/classical-projection-stability/n3_rank2_search.py
agent-B/experiments/classical-projection-stability/n3_rank2_search.json
agent-B/experiments/classical-projection-stability/n3_rank2_search.csv
agent-B/experiments/classical-projection-stability/explicit_sqrt_family.py
agent-B/experiments/classical-projection-stability/explicit_sqrt_family.json
agent-B/experiments/classical-projection-stability/explicit_sqrt_family.csv
```

The explicit-family run confirms numerically:

```text
s=0.01   delta=0.0001   distance=0.019802   distance/sqrt(delta)=1.9802
s=0.003  delta=0.000009 distance=0.005982   distance/sqrt(delta)=1.9940
s=0.001  delta=0.000001 distance=0.001998   distance/sqrt(delta)=1.9980
```
