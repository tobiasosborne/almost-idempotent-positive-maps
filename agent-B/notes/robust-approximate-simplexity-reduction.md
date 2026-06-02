# Robust Approximate Simplexity Reduction

This note slightly strengthens
`agent-B/notes/approximate-simplexity-reduction.md`.

The previous reduction assumed affine coordinates that are pointwise in
`[0,1]` on all row points. The argument actually tolerates signed affine
coordinates, provided the coordinate vector at each row has small negative
mass. This may be useful for an angle-removal proof, where exact barycentric
coordinates may only be approximately positive.

## Setup

Let `P` be an `n x n` real matrix with

```text
P1=1,        P^2=P.
```

Write `p_i` for its rows and assume

```text
neg(p_i) <= delta        for every i.
```

Let `K=conv{p_i}`. Suppose there are selected rows

```text
r^1,...,r^m
```

and affine functions `lambda_a` on `aff(K)` such that:

1. `sum_a lambda_a(p_i)=1` for every row `p_i`;
2. `lambda_a(r^b)=delta_ab`;
3. the coordinate negative mass is uniformly small:

   ```text
   nu_i := sum_a max(-lambda_a(p_i),0) <= kappa
   ```

   for every row `p_i`;
4. the coordinates reconstruct all rows up to `gamma`:

   ```text
   ||p_i - sum_a lambda_a(p_i) r^a||_1 <= gamma.
   ```

The exact approximate-simplexity reduction is the special case `kappa=0`.

## Robust Reduction Theorem

There are universal constants `delta0,C` such that, whenever
`delta+kappa<=delta0`, there is a row-stochastic idempotent `E` with

```text
||P-E||_{infty->infty} <= C (gamma + sqrt(delta+kappa)).
```

Thus signed coordinates with `kappa=O(delta)` are as good as positive
coordinates for the square-root projection-stability program. If
`kappa` is only `O(sqrt(delta))`, this lemma loses to the fourth-root scale,
so the target for a full proof should still be coordinates with coefficient
negative mass `O(delta)`.

## Proof

Set

```text
tau=sqrt(delta+kappa)
```

and decrease `delta0` so that `tau<1/4`.

For brevity write

```text
lambda_a(j)=lambda_a(p_j).
```

Since `r^a P=r^a`, applying `lambda_a` gives

```text
sum_j r^a_j lambda_a(j)=1,
```

or

```text
sum_j r^a_j h_a(j)=0,        h_a(j)=1-lambda_a(j).      (1)
```

The coefficient negative-mass condition implies, for every row index `j`,

```text
-kappa <= lambda_a(j) <= 1+kappa.
```

Indeed the lower bound is immediate, and the upper bound follows from
`sum_b lambda_b(j)=1` and total negative mass at most `kappa`.

Write `h_a=h_a^+-h_a^-`. From `(1)` and
`r^a=(r^a)^+-(r^a)^-`,

```text
sum_j (r^a)^+_j h_a^+(j)
 <= sum_j (r^a)^+_j h_a^-(j)
    + sum_j (r^a)^-_j h_a^+(j).
```

Using `h_a^-<=kappa`, `h_a^+<=1+kappa`, and
`neg(r^a)<=delta`, this gives

```text
sum_j (r^a)^+_j (1-lambda_a(j))_+
 <= C(delta+kappa).                              (2)
```

Define near-vertex index sets

```text
U_a={j: lambda_a(j)>=1-tau}.
```

Equation `(2)` implies

```text
(r^a)^+(U_a^c) <= C tau.                         (3)
```

The sets `U_a` are pairwise disjoint. If some `j` were in both `U_a` and
`U_b`, then the positive mass of the coordinate vector
`lambda(j)=(lambda_c(j))_c` would be at least `2(1-tau)`, while its positive
mass is exactly `1+nu_j<=1+kappa`, impossible for small `tau`.

Define

```text
pi_a=(r^a)^+|_{U_a} / ||(r^a)^+|_{U_a}||_1.
```

By `(3)` and `neg(r^a)<=delta`,

```text
||r^a-pi_a||_1 <= C tau.                         (4)
```

Now build stochastic rows. For row index `i`, if `i in U_a`, set

```text
beta(i)=e_a.
```

If `i` is in no `U_a`, let `lambda(i)=(lambda_a(i))_a`, let
`nu_i=neg(lambda(i))`, and set

```text
beta_a(i)=max(lambda_a(i),0)/(1+nu_i).
```

Then `beta(i)` is a probability vector and

```text
||beta(i)-lambda(i)||_1 <= 2 kappa.              (5)
```

Define the `i`th row of `E` by

```text
e_i=sum_a beta_a(i) pi_a.
```

The matrix `E` is stochastic. It is idempotent because `pi_a` is supported on
`U_a`, and every row indexed by `U_a` is exactly `pi_a`; hence

```text
pi_a E=pi_a
```

for every `a`.

It remains to estimate the distance. If `i` is in no `U_a`, then `(4)` and
`(5)` give

```text
||p_i-e_i||_1
 <= gamma
    + ||sum_a lambda_a(i) r^a - sum_a beta_a(i) pi_a||_1
 <= gamma + C tau.
```

Here `sum_a |lambda_a(i)|<=1+2kappa`, and each `pi_a` has norm `1`.

If `i in U_a`, then `lambda_a(i)>=1-tau`. Since `neg(lambda(i))<=kappa`,

```text
||lambda(i)-e_a||_1 <= C(tau+kappa) <= C tau.
```

The selected rows have `l1` norm at most `1+2delta`, so the reconstruction
assumption and `(4)` imply

```text
||p_i-e_i||_1
 <= gamma + ||sum_b lambda_b(i) r^b-r^a||_1 + ||r^a-pi_a||_1
 <= gamma + C tau.
```

Taking the row supremum proves the theorem.

## Consequence

The remaining classical problem can be weakened as follows. It is enough to
prove that every nearly positive exact signed affine retraction admits
approximate simplex coordinates whose coefficient vectors are `O(delta)`-close
to the probability simplex in total negative mass and whose reconstruction
error is `O(sqrt(delta))`.

This does not remove the angle/facet-count obstruction, but it says an
eventual coordinate construction need not be exactly positive pointwise.
