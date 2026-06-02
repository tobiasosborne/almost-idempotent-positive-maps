# Simplex Classical Near-Positive Projection Stability

This proves the sharp square-root projection-stability theorem for exact signed
affine retractions whose row polytope is a simplex. The constant is universal;
it does not depend on the number of vertices of the simplex or on the ambient
dimension.

This strictly generalizes the line-segment case in
`agent-B/notes/line-segment-classical-stability.md`.

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

2. the row polytope

   ```text
   K=conv{p_i}
   ```

   is a simplex.

Then there is a row-stochastic idempotent `E` with

```text
||P-E||_{infty->infty} <= C sqrt(delta).
```

## Simplex Coordinates

Let the vertices of `K` be the endpoint rows

```text
r^1,...,r^m.
```

They are among the rows of `P`, so `neg(r^a)<=delta`. Since `K` is a simplex,
every row has unique barycentric coordinates

```text
p_i = sum_{a=1}^m lambda_a(i) r^a,
lambda_a(i)>=0,        sum_a lambda_a(i)=1.
```

The barycentric coordinate functions `lambda_a` are affine on the mass-one
affine hull of `K`. Since `P^2=P`, every vertex row is fixed:

```text
r^a P = sum_j r^a_j p_j = r^a.
```

Applying the affine coordinate `lambda_b` gives, for all `a,b`,

```text
sum_j r^a_j lambda_b(j) = delta_{ab}.             (1)
```

Equivalently, for each fixed `a`,

```text
sum_j r^a_j (1-lambda_a(j)) = 0.                  (2)
```

Set

```text
tau=sqrt(delta),
```

and assume `delta0` is small enough that `tau<1/3`.

## Vertex Concentration

For each vertex `a`, define its near-vertex slice

```text
U_a={j: lambda_a(j)>=1-tau}.
```

The sets `U_a` are pairwise disjoint. Decompose `r^a=(r^a)^+-(r^a)^-`. Since
`0<=1-lambda_a(j)<=1`, equation (2) gives

```text
sum_j (r^a)^+_j (1-lambda_a(j))
 = sum_j (r^a)^-_j (1-lambda_a(j))
 <= neg(r^a)
 <= delta.
```

Therefore

```text
(r^a)^+({j: lambda_a(j)<1-tau}) <= delta/tau = tau.       (3)
```

The positive mass of each vertex row is thus concentrated on its own
near-vertex slice.

Define

```text
pi_a = (r^a)^+|_{U_a} / ||(r^a)^+|_{U_a}||_1.
```

The denominator is at least `1-O(tau)`, and the normalized vector `pi_a` is a
probability distribution supported on `U_a`. From (3) and
`neg(r^a)<=delta`,

```text
||r^a-pi_a||_1 <= C tau.                          (4)
```

Indeed, if a signed probability `mu` has negative mass `c` and positive mass
`b` outside a chosen support, then its distance from the normalized positive
restriction to that support is at most `2(b+c)`.

## Constructing The Stochastic Idempotent

For each row index `i`, define rounded barycentric coefficients `beta_a(i)` as
follows.

If `i in U_a` for some `a`, set

```text
beta_a(i)=1,        beta_b(i)=0 for b!=a.
```

If `i` is in no `U_a`, set

```text
beta_a(i)=lambda_a(i)        for all a.
```

Now define the row `e_i` of `E` by

```text
e_i = sum_a beta_a(i) pi_a.
```

Then `E` is row-stochastic.

It is idempotent. For each `a`, the support of `pi_a` is contained in `U_a`,
and every row indexed by `U_a` is exactly `pi_a`. Hence

```text
pi_a E = pi_a.
```

Therefore, for every `i`,

```text
e_i E = sum_a beta_a(i) pi_a E = sum_a beta_a(i) pi_a = e_i.
```

## Distance Estimate

Each vertex row has bounded total variation:

```text
||r^a||_1 <= 1+2delta.
```

Thus, for all `a,b`,

```text
||r^a-r^b||_1 <= 3
```

after decreasing `delta0`.

If `i` is in no `U_a`, then `beta(i)=lambda(i)`, so (4) gives

```text
||p_i-e_i||_1
 <= sum_a lambda_a(i)||r^a-pi_a||_1
 <= C tau.
```

If `i in U_a`, then `lambda_a(i)>=1-tau`, so

```text
sum_{b!=a} lambda_b(i) <= tau.
```

Since `e_i=pi_a`,

```text
||p_i-e_i||_1
 <= ||r^a-pi_a||_1
    + ||p_i-r^a||_1
 <= C tau + sum_{b!=a} lambda_b(i)||r^b-r^a||_1
 <= C tau.
```

Taking the supremum over rows proves

```text
||P-E||_{infty->infty} <= C sqrt(delta).
```

## Consequence

The classical projection-stability conjecture is true for exact signed affine
retractions whose row polytope is a simplex, with a constant independent of
the number of vertices. The proof identifies the main desired mechanism in its
cleanest form: barycentric idempotency forces each vertex row's positive mass
to concentrate on its own near-vertex slice, and those slices become disjoint
recurrent classes after normalization.

The general polytope case remains open because a non-simplex polytope does not
have global affine barycentric coordinates attached to all vertices. The
remaining problem is to replace this simplex-coordinate argument by a
dimension-free recursive or stratified rounding for arbitrary row polytopes.
