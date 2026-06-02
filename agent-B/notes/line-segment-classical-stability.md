# Line-Segment Classical Near-Positive Projection Stability

This proves the sharp square-root projection-stability theorem for exact signed
affine retractions whose row polytope is a line segment.

This case is complementary to
`agent-B/notes/rank-one-classical-stability.md`: the rank-one note treats
rank-one perturbations of the identity, while this note treats affine image
dimension at most one, i.e. the first nontrivial two-recurrent-component
geometry.

## Statement

There are universal constants `delta0,C` such that the following holds.

Let `P` be an `n x n` real matrix with

```text
P1=1,        P^2=P.
```

Write `p_i` for the rows of `P`, viewed as signed probability vectors. Assume:

1. every row has negative mass at most `delta`:

   ```text
   neg(p_i)=sum_j max(-p_i(j),0) <= delta;
   ```

2. the affine hull of `{p_i}` has dimension at most `1`.

Then there is a row-stochastic idempotent `E` with

```text
||P-E||_{infty->infty} <= C sqrt(delta).
```

## Degenerate Case

If all rows of `P` are equal to a signed probability vector `r`, then
`neg(r)<=delta`. Let `pi=r^+/||r^+||_1`. The stochastic rank-one idempotent
with every row equal to `pi` satisfies

```text
||P-E||_{infty->infty} <= 2 delta.
```

So assume the row polytope is a genuine line segment.

## Affine Coordinate

Choose endpoint rows `r,s` and write every row uniquely as

```text
p_i=(1-alpha_i) r + alpha_i s,        0<=alpha_i<=1.
```

The endpoints are rows, hence `neg(r),neg(s)<=delta`. Since `P^2=P`, every row
is fixed by `P`. Applying the affine coordinate `alpha` to

```text
rP=sum_j r_j p_j = r,        sP=sum_j s_j p_j = s
```

gives

```text
sum_j r_j alpha_j = 0,        sum_j s_j alpha_j = 1.       (1)
```

Equivalently,

```text
sum_j s_j (1-alpha_j)=0.                                 (2)
```

Set

```text
tau=sqrt(delta).
```

Assume `delta0` is small enough that `tau<1/4`.

## Endpoint Concentration

Let

```text
L={j: alpha_j<=tau},        U={j: alpha_j>=1-tau}.
```

These sets are disjoint.

For `r`, decompose `r=r^+-r^-`. Since `0<=alpha_j<=1`, (1) implies

```text
sum_j r_j^+ alpha_j = sum_j r_j^- alpha_j <= neg(r) <= delta.
```

Therefore

```text
r^+({j: alpha_j>tau}) <= delta/tau = tau.          (3)
```

Similarly, using (2),

```text
s^+({j: alpha_j<1-tau}) <= tau.                   (4)
```

Thus the positive mass of `r` is concentrated on `L`, while the positive mass
of `s` is concentrated on `U`.

Define probability vectors supported on these almost-closed endpoint sets:

```text
pi_0 = r^+|_L / ||r^+|_L||_1,
pi_1 = s^+|_U / ||s^+|_U||_1.
```

The denominators are at least `1-O(tau)`. From (3), (4), and
`neg(r),neg(s)<=delta`,

```text
||r-pi_0||_1 <= C tau,        ||s-pi_1||_1 <= C tau.       (5)
```

Indeed, if a signed probability `mu` has negative mass `a` and positive mass
`b` outside the chosen support, then the distance from `mu` to the normalized
positive restriction is at most `2(a+b)`.

## Constructing The Stochastic Idempotent

Define rounded coefficients

```text
beta_i =
  0          if i in L,
  1          if i in U,
  alpha_i    otherwise.
```

Set the row `e_i` of `E` to be

```text
e_i=(1-beta_i) pi_0 + beta_i pi_1.
```

Then `E` is row-stochastic.

It is also idempotent. Since `pi_0` is supported on `L`, all rows in its
support are equal to `pi_0`; hence `pi_0 E=pi_0`. Similarly `pi_1` is supported
on `U`, all rows in its support are equal to `pi_1`, and `pi_1 E=pi_1`.
Therefore, for every `i`,

```text
e_i E = (1-beta_i) pi_0 E + beta_i pi_1 E = e_i.
```

## Distance Estimate

The endpoint signed probabilities have uniformly bounded total variation:

```text
||r||_1, ||s||_1 <= 1+2delta,
```

so `||r-s||_1<=3` after decreasing `delta0`.

If `i` is in neither `L` nor `U`, then `beta_i=alpha_i`, and (5) gives

```text
||p_i-e_i||_1
 <= (1-alpha_i)||r-pi_0||_1 + alpha_i||s-pi_1||_1
 <= C tau.
```

If `i in L`, then `alpha_i<=tau`, `beta_i=0`, and

```text
||p_i-e_i||_1
 <= ||r-pi_0||_1 + alpha_i ||s-r||_1
 <= C tau.
```

The case `i in U` is symmetric:

```text
||p_i-e_i||_1
 <= ||s-pi_1||_1 + (1-alpha_i)||s-r||_1
 <= C tau.
```

Taking the supremum over rows proves

```text
||P-E||_{infty->infty} <= C sqrt(delta).
```

## Consequence

The full classical projection-stability conjecture is true for exact signed
affine retractions whose image polytope is a point or a line segment. The proof
exhibits the same square-root mechanism as the exposed-face leakage lemma:
endpoint idempotency forces positive mass into endpoint-exposed slices, and
those slices become the disjoint recurrent supports of the rounded stochastic
idempotent.
