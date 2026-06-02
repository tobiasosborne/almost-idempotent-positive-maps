# Rank-One Classical Near-Positive Projection Stability

This proves the sharp square-root stability theorem for the special class

```text
P = I - u v^T
```

of row-stochastic signed idempotents on `ell_infty^n`.

This class contains Hume's `3 x 3` sharp example.

## Statement

There are universal constants `delta0,C` such that the following holds.

Let

```text
P = I - u v^T
```

be an `n x n` real matrix with

```text
P 1 = 1,        P^2=P.
```

Equivalently,

```text
sum_j v_j = 0,        v^T u = 1.
```

Assume every row of `P` has negative mass at most `delta`:

```text
neg(P_i)=sum_j max(-P_{ij},0) <= delta.
```

Then there is a row-stochastic idempotent `E` with

```text
||P-E||_{infty->infty} <= C sqrt(delta).
```

The exponent is sharp by Hume's family.

## Normalization

Set

```text
A = I-P = u v^T.
```

Since `P1=1`, `sum_j v_j=0`. Rescale `u,v` without changing `A` so that

```text
sum_{v_j>0} v_j = 1,        sum_{v_j<0} (-v_j)=1.
```

Thus `||v||_1=2`.

Let

```text
v_j^+ = max(v_j,0),        v_j^- = max(-v_j,0).
```

The bad mass assumption says, row by row,

```text
sum_{j != i} max(u_i v_j,0) + max(u_i v_i-1,0) <= delta.        (1)
```

Indeed `P_{ij}=-u_i v_j` for `j!=i` and `P_{ii}=1-u_i v_i`.

## Consequences

For `u_i>0`, (1) gives

```text
u_i (1-v_i^+) <= delta.                                      (2+)
```

For `u_i<0`, (1) gives

```text
(-u_i)(1-v_i^-) <= delta.                                    (2-)
```

The diagonal term in (1) also gives the active coefficient bounds

```text
u_i v_i^+ <= 1+delta          when u_i>0 and v_i>0,
(-u_i) v_i^- <= 1+delta       when u_i<0 and v_i<0.            (3)
```

Let

```text
tau = sqrt(delta).
```

For `delta<1/100`, there is at most one index `a` with `u_a>tau`, and at most
one index `b` with `u_b<-tau`.

Proof: if `u_i>tau`, then (2+) implies `v_i^+>=1-tau`. Two such indices cannot
exist because the total positive mass of `v` is `1`. The negative case is the
same using (2-).

There is at least one active index of either sign. Otherwise

```text
1 = |v^T u| <= ||v||_1 max_i |u_i| <= 2 tau < 1,
```

which is impossible.

All inactive rows, i.e. rows with `|u_i|<=tau`, can be replaced by identity
rows at cost

```text
||u_i v||_1 <= 2 tau.                                      (4)
```

It remains to define a positive rank-one idempotent on the active indices.

## Case 1: One Positive Active Index Only

Suppose there is `a` with `u_a>tau` and no `b` with `u_b<-tau`.

Then (2+) gives

```text
1-v_a^+ <= delta/u_a <= tau.
```

Define

```text
v' = e_a - v^-,
u'_a = 1,       u'_i=0 for i!=a.
```

Here `v^-` is the probability vector with entries `v_j^-`; hence `sum_j v'_j=0`
and `v'^T u'=1`. The matrix

```text
E = I - u' v'^T
```

is a stochastic idempotent: all rows except `a` are identity rows, while row
`a` is the probability vector `v^-` supported off the positive direction
(with the obvious zero at `a` if `v_a^-=0`).

We need `u_a v` close to `v'`. The inactive contribution to `v^T u=1` is at
most `2 tau` in absolute value, `v_a^+>=1-tau`, and (3) bounds `u_a` by an
absolute constant; hence

```text
|u_a-1| <= C tau.
```

Also

```text
||v-v'||_1 = 2(1-v_a^+) <= 2 tau.
```

Thus

```text
||u_a v - v'||_1 <= |u_a-1| ||v||_1 + ||v-v'||_1 <= C tau.
```

Together with (4), this gives `||P-E||<=C sqrt(delta)`.

## Case 2: One Negative Active Index Only

This is symmetric.

If `b` is the unique index with `u_b<-tau`, then `v_b^- >= 1-tau`. Define

```text
v' = v^+ - e_b,
u'_b = -1,       u'_i=0 for i!=b.
```

Then `E=I-u'v'^T` is stochastic idempotent, with only row `b` nontrivial, and
the same argument gives

```text
||P-E||<=C sqrt(delta).
```

## Case 3: One Positive And One Negative Active Index

Let `a` be the unique index with `u_a>tau`, and `b` the unique index with
`u_b<-tau`.

Then

```text
v_a^+ >= 1-tau,        v_b^- >= 1-tau,
```

so

```text
||v-(e_a-e_b)||_1 <= 4 tau.                              (5)
```

Let

```text
d = u_a-u_b.
```

From `v^T u=1`, (5), the active coefficient bounds (3), and the fact that all
inactive `|u_i|<=tau`, we get

```text
|d-1| <= C tau.
```

Define

```text
v' = e_a-e_b,
u'_a = u_a/d,        u'_b = u_b/d,        u'_i=0 for i notin {a,b}.
```

Then `sum_j v'_j=0` and `v'^T u'=1`. Moreover `u'_a>=0`, `u'_b<=0`. Hence

```text
E=I-u'v'^T
```

is a stochastic idempotent: rows `a` and `b` are the same probability vector
on `{a,b}`, and all other rows are identity rows.

For inactive rows, (4) applies. For rows `a,b`, use (5) and `|d-1|<=C tau` to
get

```text
||u_i v-u'_i v'||_1 <= C tau,        i=a,b.
```

Therefore

```text
||P-E||_{infty->infty} <= C sqrt(delta).
```

## Consequence

The Markov/affine-retraction square-root conjecture is true for rank-one
signed idempotents. Hume's example shows the bound is sharp even in this
rank-one class.

The proof also explains the square root: the only forbidden signs are products
`u_i v_j` with `i!=j`; bounding their total positive part by `delta` forces
one factor to be `O(sqrt(delta))` unless the corresponding positive or negative
mass of `v` is concentrated at a single active coordinate.
