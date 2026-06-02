# Cluster-Representative Classical Stability

This note proves a non-accumulating merge criterion for the classical
near-positive projection-stability problem.

It is a bridge between the proved well-exposed case and the remaining
exposed-or-redundant dichotomy. The point is that once all rows are
`O(sqrt(delta))`-reconstructible from well-exposed representative rows, no
global affine coordinate system is needed: one can build the stochastic
idempotent directly.

## Setup

Let `P` be an `n x n` real matrix with

```text
P1=1,        P^2=P.
```

Write `p_i` for its rows, viewed as signed probability vectors, and assume

```text
neg(p_i) <= delta
```

for every row. Let

```text
K=conv{p_i}.
```

Choose representative row vertices

```text
r^1,...,r^m.
```

Assume there are parameters `rho,kappa,gamma>0` such that:

1. the representatives are pairwise separated:

   ```text
   ||r^a-r^b||_1 >= 2rho        (a!=b);
   ```

2. each representative is well exposed at scale `rho`: there is an affine
   function `h_a:K->[0,1]` with

   ```text
   h_a(r^a)=0,
   h_a(x)>=kappa        whenever ||x-r^a||_1>=rho;
   ```

3. every row outside the representative clusters is close to the convex hull
   of the representatives. With

   ```text
   U_a={j: ||p_j-r^a||_1<rho},
   U=union_a U_a,
   ```

   for every `i notin U` there is a probability vector
   `lambda(i)=(lambda_a(i))_a` such that

   ```text
   ||p_i - sum_a lambda_a(i) r^a||_1 <= gamma.
   ```

The sets `U_a` are pairwise disjoint by the separation hypothesis.

## Theorem

Under these assumptions, there is a row-stochastic idempotent `E` with

```text
||P-E||_{infty->infty}
 <= C (rho + gamma + delta/kappa + delta).       (1)
```

In particular, if

```text
rho <= C0 sqrt(delta),        gamma <= C0 sqrt(delta),
kappa >= c0 sqrt(delta),
```

then

```text
||P-E||_{infty->infty} <= C_{C0,c0} sqrt(delta).
```

## Proof

Apply the one-row concentration lemma from
`agent-B/notes/exposed-circuit-cancellation.md` to each representative `r^a`.
For every `a` there is a probability measure `pi_a` supported on `U_a` such
that

```text
||r^a-pi_a||_1 <= C(delta/kappa+delta).          (2)
```

The supports of the `pi_a` are disjoint because the `U_a` are disjoint.

Define a stochastic matrix `E` row by row.

If `i in U_a`, set

```text
e_i=pi_a.
```

If `i notin U`, use the probability vector from assumption 3 and set

```text
e_i=sum_a lambda_a(i) pi_a.
```

Every row `e_i` is a probability vector.

The matrix `E` is idempotent. Indeed, each `pi_a` is supported on `U_a`, and
for every index `j in U_a`, the row of `E` is exactly `pi_a`. Hence

```text
pi_a E=pi_a
```

for every `a`. Therefore:

- if `i in U_a`, then `e_i E=pi_a E=pi_a=e_i`;
- if `i notin U`, then

  ```text
  e_i E=sum_a lambda_a(i) pi_a E
       =sum_a lambda_a(i) pi_a
       =e_i.
  ```

Thus `E^2=E`.

It remains to estimate the row distance.

If `i in U_a`, then by definition of `U_a` and `(2)`,

```text
||p_i-e_i||_1
 = ||p_i-pi_a||_1
 <= ||p_i-r^a||_1 + ||r^a-pi_a||_1
 <= rho + C(delta/kappa+delta).
```

If `i notin U`, then assumption 3 and `(2)` give

```text
||p_i-e_i||_1
 <= ||p_i - sum_a lambda_a(i) r^a||_1
    + ||sum_a lambda_a(i)(r^a-pi_a)||_1
 <= gamma + C(delta/kappa+delta),
```

because `lambda(i)` is a probability vector.

Taking the supremum over rows proves `(1)`.

## Consequence

The full classical square-root theorem would follow if, after merging
`O(sqrt(delta))`-close vertices, one can select well-exposed representatives
such that every remaining row is `O(sqrt(delta))`-close to their convex hull.

This is slightly weaker than constructing global affine simplex coordinates:
the reconstruction coefficients in this note need only exist row by row. The
idempotent construction uses only the recurrent-support clusters `U_a`, so no
constant accumulates with the number of merged vertices or transient rows.
