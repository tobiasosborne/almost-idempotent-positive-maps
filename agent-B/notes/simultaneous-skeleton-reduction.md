# Simultaneous Skeleton Reduction Target

This note sharpens the remaining classical projection-stability gap.

The existing exposed-or-redundant formulation is useful, but a pointwise
deletion version is not strong enough for a dimension-free proof.  What is
needed is a simultaneous exposed skeleton: a set of representatives that is
well exposed and already reconstructs all rows, up to `O(sqrt(delta))`, in one
shot.

## Setup

Let `P` be an `n x n` real matrix with

```text
P1=1,        P^2=P.
```

Write `p_i` for its rows, viewed as signed probability vectors, and assume

```text
neg(p_i)<=delta
```

for every row.  Let

```text
K=conv{p_i},        tau=sqrt(delta).
```

## Exposed Skeleton

For parameters `rho,kappa,gamma`, call a set of row vertices

```text
R={r^1,...,r^m}
```

an exposed skeleton if:

1. the representatives are pairwise separated:

   ```text
   ||r^a-r^b||_1>=2rho        (a!=b);
   ```

2. each representative is well exposed at scale `rho`: there is an affine
   function `h_a:K->[0,1]` with

   ```text
   h_a(r^a)=0,
   h_a(x)>=kappa        whenever ||x-r^a||_1>=rho;
   ```

3. with cluster sets

   ```text
   U_a={j: ||p_j-r^a||_1<rho},        U=union_a U_a,
   ```

   every row outside the clusters is close to the representative hull:

   ```text
   dist_1(p_i, conv R)<=gamma        (i notin U).
   ```

This is exactly the hypothesis of
`agent-B/notes/cluster-representative-classical-stability.md`, except written
as a target object.

## The Sufficient Lemma

The following lemma would finish the classical projection-stability theorem.

There are universal constants `c,C` such that every nearly positive exact
signed affine retraction as above admits an exposed skeleton with

```text
rho<=C tau,        gamma<=C tau,        kappa>=c tau.
```

Indeed, the cluster-representative theorem then constructs a stochastic
idempotent `E` satisfying

```text
||P-E||_{infty->infty}
 <= C(rho+gamma+delta/kappa+delta)
 <= C tau.
```

Combined with the existing rowwise repair/spectral-functional-calculus
reductions, this gives the full commutative `sqrt` projection-stability
theorem and hence exact commutative positive/JB factorization for arbitrary
almost-idempotent stochastic maps.

## Global Exposed-Hull Form

An even cleaner sufficient statement is the following one-shot reconstruction
lemma.

Fix `rho,kappa`, and let

```text
W_{rho,kappa}
 = {row vertices v of K : e_v(rho)>=kappa},
```

where `e_v` is the exposedness modulus from
`agent-B/notes/exposed-redundant-dichotomy-target.md`.  Suppose that

```text
rho<=C0 tau,        kappa>=c0 tau,
```

and every row satisfies

```text
dist_1(p_i, conv W_{rho,kappa})<=gamma,        gamma<=C0 tau.      (GH)
```

Then the exposed-skeleton lemma follows, with changed universal constants.

### Proof Of The Reduction

Choose a maximal `4rho`-separated subset

```text
R={r^1,...,r^m} subset W_{rho,kappa}.
```

Then the representatives are pairwise separated by `4rho`.  Each `r^a`
belongs to `W_{rho,kappa}`, so it has an exposing function with gap `kappa`
outside the `rho`-ball.  The same function also has gap `kappa` outside the
larger `2rho`-ball.

By maximality, every `w in W_{rho,kappa}` lies within `4rho` of some
representative `r^a`.  Hence every point of `conv W_{rho,kappa}` lies within
`4rho` of `conv R`: push each convex weight to a nearest representative and
use the triangle inequality in `l1`.

Therefore `(GH)` gives

```text
dist_1(p_i, conv R)<=gamma+4rho
```

for every row.  In particular, this holds for every row outside the
`2rho`-clusters around the representatives.  The clusters are disjoint because
the representatives are `4rho`-separated.

Thus `R` satisfies the cluster-representative hypotheses with cluster radius
`2rho`, exposedness gap `kappa`, and reconstruction error `gamma+4rho`.
Applying `agent-B/notes/cluster-representative-classical-stability.md` gives

```text
||P-E||_{infty->infty}
 <= C(2rho + gamma+4rho + delta/kappa + delta)
 <= C tau.
```

This proves that the global exposed-hull form is exactly strong enough for
the classical square-root theorem.

## Why Pointwise Redundancy Is Not Enough

A local dichotomy of the form

```text
each vertex v is either well exposed, or
dist(v, conv{other vertices})<=C tau
```

does not by itself imply a simultaneous skeleton with dimension-free error.
The problem is accumulation.

Pure convex geometry already shows the logical gap.  Take a regular polygon
with many vertices.  If the vertex spacing is much smaller than `tau`, then at
scale `rho=tau` no vertex has an exposedness gap comparable to `tau`: the best
supporting affine functions separate the first outside points only at the
quadratic curvature scale.  At the same time each vertex is `O(spacing^2)`,
hence `O(tau)`, from the convex hull of the remaining vertices.  Thus the
pointwise redundancy alternative can hold for every vertex while producing no
distinguished well-exposed representative set.

This polygon is not asserted to arise from a nearly positive signed
idempotent.  It is only a warning about the logic: pointwise removability is
not a dimension-free reconstruction procedure.  Sequentially substituting one
`O(tau)` convex approximation into another may lose a factor equal to the
length of the deletion chain.

## Strengthened Redundancy Needed

The redundancy side should therefore be one of the following stronger,
non-accumulating statements.

### Global Exposed Hull

Let `W_{rho,kappa}` be the set of square-root-well-exposed vertices.  Prove
directly that every row is `O(tau)`-close to `conv W_{rho,kappa}`.  The
previous section shows this is enough: a maximal separated subset of `W` gives
the exposed skeleton, and no sequential deletion is used.

### One-Shot Redundancy

For some set `R` of well-exposed separated representatives, every
non-cluster row is already `O(tau)`-close to `conv R`.

This is the exposed-skeleton lemma above.  It is exactly sufficient and
matches the cluster-representative theorem without any further bookkeeping.

### Acyclic Redundancy

Assign to vertices a height or rank `q(v)` such that every non-well-exposed
vertex `v` is `O(tau)`-close to the convex hull of vertices with strictly
larger height, together with nearby cluster vertices.  Then a single
backward-substitution argument can terminate at the maximal-height vertices.

To be useful dimension-free, the substitution operator must be a contraction
on reconstruction error, not merely a stochastic matrix with long paths.  In
practice this means the certificate should be rewritten as a one-shot
approximation to the final maximal set.

### Robust Coordinate Version

Produce affine coordinates on a selected representative set whose coefficient
negative mass is `O(delta)` and whose row reconstruction error is `O(tau)`.
Then `agent-B/notes/robust-approximate-simplexity-reduction.md` gives the
stochastic idempotent directly.  This route does not require exact pointwise
positive barycentric coordinates, but it still needs a one-shot global
coordinate certificate.

## LP-Dual Rephrasing

The LP-dual witness for failure of exposedness at a vertex `v` gives a
probability measure on outside rows whose barycenter has small value against
all normalized affine functions `h:K->[0,1]` with `h(v)=0`.

For the old local dichotomy, one tries to show that this barycenter forces

```text
dist_1(v, conv{p_i: p_i!=v})=O(tau).
```

For the skeleton lemma, the stronger target is:

```text
failure of a global exposed skeleton
  => existence of a dual witness incompatible with
     P^2=P and neg(p_i)<=delta.
```

In the global exposed-hull form, it is:

```text
dist_1(v, conv W_{rho,kappa}) > C tau
  =>  e_v(rho)>=kappa.
```

Equivalently, every non-well-exposed vertex must be reconstructed at scale
`O(tau)` by the hull of the well-exposed vertices, not merely by the hull of
the other non-well-exposed vertices.

Equivalently, the LP-dual argument should not be run independently at each
vertex.  It should be run against a maximal candidate skeleton and should
produce either:

1. a new well-exposed representative separated from the existing clusters; or
2. a one-shot `O(tau)` reconstruction of the offending row by the current
   representative hull.

This maximal-skeleton formulation is now the cleanest classical target.  It
keeps all constants tied to the exposed-circuit and cluster-representative
lemmas, and it avoids any hidden dependence on the number of redundant
vertices.
