# Approximate Simplexity Reduction For Classical Projection Stability

This note isolates the remaining classical obstruction after the simplex
row-polytope theorem.

The conclusion is: the full commutative near-positive projection-stability
theorem follows if every nearly positive signed affine retraction admits
approximate simplex coordinates at `O(sqrt(delta))` scale.

A robust signed-coordinate variant is recorded in
`agent-B/notes/robust-approximate-simplexity-reduction.md`: it is enough for
the coordinate vectors to have coefficient negative mass `O(delta)`, rather
than to be exactly pointwise nonnegative, with the same square-root output.

## Setup

Let `P` be an `n x n` real matrix with

```text
P1=1,        P^2=P.
```

Write `p_i` for the rows of `P`, viewed as signed probability vectors, and
assume

```text
neg(p_i) <= delta        for all i.
```

Set

```text
tau=sqrt(delta).
```

## Approximate Simplex Coordinates

Say that the row polytope has `gamma`-approximate simplex coordinates if there
exist row vectors

```text
r^1,...,r^m          among the rows of P
```

and affine functions `lambda_a` on the affine hull of the row polytope such
that, for every row `p_i`,

```text
0 <= lambda_a(p_i) <= 1,        sum_a lambda_a(p_i)=1,
lambda_a(r^a)=1,
```

and

```text
||p_i - sum_a lambda_a(p_i) r^a||_1 <= gamma.       (A)
```

For a genuine simplex row polytope, this holds with `gamma=0`, where the
`lambda_a` are barycentric coordinates.

## Reduction Theorem

Assume `P` has `gamma`-approximate simplex coordinates. Then there is a
row-stochastic idempotent `E` with

```text
||P-E||_{infty->infty} <= C (sqrt(delta)+gamma).
```

Consequently, the full classical projection-stability conjecture follows from
the approximate-simplexity lemma:

```text
every nearly positive signed affine retraction has
gamma <= C sqrt(delta) approximate simplex coordinates.
```

## Proof

For brevity write

```text
lambda_a(i)=lambda_a(p_i).
```

Since `r^a` is a row and `P^2=P`,

```text
r^a P = sum_j r^a_j p_j = r^a.
```

Applying the affine function `lambda_a` gives

```text
sum_j r^a_j lambda_a(j) = lambda_a(r^a)=1,
```

or equivalently

```text
sum_j r^a_j (1-lambda_a(j)) = 0.                  (1)
```

Let

```text
U_a={j: lambda_a(j)>=1-tau}.
```

The sets `U_a` are pairwise disjoint once `tau<1/2`, because
`sum_a lambda_a(j)=1`.

Decompose `r^a=(r^a)^+-(r^a)^-`. Since `0<=1-lambda_a(j)<=1`, equation `(1)`
implies

```text
sum_j (r^a)^+_j (1-lambda_a(j))
 = sum_j (r^a)^-_j (1-lambda_a(j))
 <= neg(r^a)
 <= delta.
```

Thus

```text
(r^a)^+({j: lambda_a(j)<1-tau}) <= tau.          (2)
```

Define

```text
pi_a = (r^a)^+|_{U_a} / ||(r^a)^+|_{U_a}||_1.
```

As in the simplex proof,

```text
||r^a-pi_a||_1 <= C tau.                         (3)
```

Now define rows of `E`. If `i in U_a` for some `a`, put

```text
e_i=pi_a.
```

If `i` is in no `U_a`, put

```text
e_i=sum_a lambda_a(i) pi_a.
```

Then `E` is stochastic. It is idempotent because `pi_a` is supported on `U_a`,
and all rows indexed by `U_a` are equal to `pi_a`; hence `pi_a E=pi_a`.

For the distance estimate, first suppose `i` is in no `U_a`. Then `(A)` and
`(3)` give

```text
||p_i-e_i||_1
 <= gamma + sum_a lambda_a(i)||r^a-pi_a||_1
 <= gamma + C tau.
```

If `i in U_a`, then

```text
sum_{b!=a} lambda_b(i) <= tau.
```

Using `(A)`, `(3)`, and `||r^a-r^b||_1<=3` for all vertex rows,

```text
||p_i-e_i||_1
 <= gamma + ||sum_b lambda_b(i) r^b - r^a||_1 + ||r^a-pi_a||_1
 <= gamma + C tau.
```

Taking the row supremum proves the theorem.

## Meaning Of The Remaining Gap

For this route, the arbitrary non-simplex row-polytope problem is reduced to
finding dimension-free approximate simplex coordinates at square-root scale, or
to constructing a counterexample to such coordinates.

The exposed-face leakage lemma gives local candidates for the near-vertex
sets `U_a`, but it does not by itself build a global affine partition of unity
`lambda_a` satisfying `(A)`. This is the precise place where naive recursive
rounding can accumulate constants or depend on facet angles.
