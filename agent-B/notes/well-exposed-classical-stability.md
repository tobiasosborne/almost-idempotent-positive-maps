# Well-Exposed Classical Stability

This note records a closed special case of the classical near-positive
projection-stability problem.

The point is not that the final stability proof is new once the row polytope
is known to be a simplex; that is already
`agent-B/notes/simplex-classical-stability.md`. The new content is that a
non-simplex row polytope cannot have all of its vertices well exposed and
separated at the square-root scale.

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
K=conv{p_i}
```

and let `v_1,...,v_m` be the distinct vertices of `K`. Each `v_a` is one of
the rows.

## Well-Exposed Separated Vertex Hypothesis

Assume there are numbers `rho,kappa>0` such that:

1. the vertices are pairwise separated:

   ```text
   ||v_a-v_b||_1 >= 2rho        (a!=b);
   ```

2. each vertex has a `[0,1]`-valued exposing function at scale `rho`: there is
   an affine function `h_a:K->[0,1]` with

   ```text
   h_a(v_a)=0,
   h_a(x)>=kappa        whenever ||x-v_a||_1>=rho.
   ```

3. the defect is small relative to the exposedness gap:

   ```text
   C_ec(delta/kappa+delta)<1,
   ```

   where `C_ec` is the universal constant in
   `agent-B/notes/exposed-circuit-cancellation.md`.

## Theorem

Under the setup and well-exposed separated vertex hypothesis, the row polytope
`K` is a simplex.

Consequently, by the simplex stability theorem, there is a row-stochastic
idempotent `E` with

```text
||P-E||_{infty->infty} <= C sqrt(delta).
```

In particular, if

```text
kappa >= c sqrt(delta)
```

for a fixed `c>0` and `delta` is sufficiently small, the conclusion holds with
a constant depending only on `c`.

## Proof

Apply the exposed-circuit cancellation lemma to the full vertex set
`{v_1,...,v_m}`. For all real coefficients `c_a`, it gives

```text
||sum_a c_a v_a||_1
 >= (1-C_ec(delta/kappa+delta)) sum_a |c_a|.     (1)
```

By the smallness assumption, the coefficient in front of `sum_a |c_a|` is
strictly positive.

If the vertices were affinely dependent, then there would be real
coefficients `c_a`, not all zero, such that

```text
sum_a c_a=0,        sum_a c_a v_a=0.
```

Equation `(1)` would force

```text
0 >= (1-C_ec(delta/kappa+delta)) sum_a |c_a| > 0,
```

a contradiction. Hence the vertices are affinely independent.

A compact convex polytope is a simplex exactly when its vertices are affinely
independent. Therefore `K` is a simplex. The stochastic idempotent `E` and the
distance estimate now follow directly from
`agent-B/notes/simplex-classical-stability.md`.

If `kappa>=c sqrt(delta)`, then

```text
delta/kappa+delta <= C_c sqrt(delta),
```

so the smallness assumption is satisfied after decreasing the universal
`delta0`.

## Consequence For The Full Classical Program

This theorem closes the well-exposed separated branch of the non-simplex
problem. Any remaining non-simplex obstruction to square-root stability must
involve at least one of:

- vertices closer than the chosen `sqrt(delta)` scale, hence candidates for
  merging;
- vertices whose exposedness modulus is below `c sqrt(delta)`, hence the
  non-well-exposed side of
  `agent-B/notes/exposed-redundant-dichotomy-target.md`;
- a failure to remove or merge such vertices without accumulating constants.

Thus the full classical theorem is reduced further: it is enough to prove the
dimension-free exposed-or-redundant dichotomy and a non-accumulating merging
procedure. The genuinely well-exposed affine-circuit case is no longer an
open obstruction.
