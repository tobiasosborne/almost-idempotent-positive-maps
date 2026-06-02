# Sidecar Stress Test: Local Redundancy Versus Simultaneous Skeleton

This note stress-tests the proposed non-accumulating classical projection
stability reduction.

## Verdict

The local dichotomy, in the form

```text
each vertex v is either well exposed at scale O(tau)
or dist(v, conv(V \ {v})) <= C tau,
```

is not by itself enough to produce the simultaneous skeleton required by
`cluster-representative-classical-stability.md`.

The obstruction is quantifier order.  The cluster theorem needs one fixed set
of well-exposed representatives `R` such that all remaining rows are
`O(tau)`-close to `conv(R)`, with no iteration.  Pointwise redundancy only
says that a bad vertex can be reconstructed using the rest of the current
configuration; the reconstructing vertices may all be bad too.  This permits
circular or chain-like redundancy and gives no non-accumulating final
reconstruction.

## Concrete Convex-Geometric Obstruction

This is not a counterexample to the signed-retraction theorem; it is a
counterexample to the purely convex-geometric implication from local
redundancy to a simultaneous exposed skeleton.

Fix small `tau` and take a regular `N`-gon in a fixed two-dimensional affine
slice of an `l_1` probability simplex, with

```text
N^{-2} = epsilon tau
```

for a sufficiently small constant `epsilon`.  Norm equivalence in this fixed
dimension changes only constants.

For every vertex `v_k`, the distance from `v_k` to the chord
`[v_{k-1},v_{k+1}]` is `asymp N^{-2}`, hence

```text
dist(v_k, conv(V \ {v_k})) <= C epsilon tau.
```

Thus every vertex is locally `O(tau)`-redundant.

On the other hand, let `rho = C_0 tau`.  Since the adjacent vertices are at
distance `asymp N^{-1} = sqrt(epsilon tau)`, they lie outside the `rho`-ball
for small `tau`.  For any affine `h:K->[0,1]` with `h(v_k)=0`, nonnegativity
on the polygon forces at least one adjacent value to be `O(N^{-2})`; for the
regular polygon this is immediate from the two adjacent supporting facets.
Therefore

```text
e_{v_k}(rho) <= C' epsilon tau.
```

Choosing `epsilon` below the proposed exposedness constant makes every vertex
fail the `c tau` well-exposed alternative, while every vertex satisfies the
local redundant alternative.  The set of well-exposed representatives is then
empty, and there is no way to approximate the polygon by the convex hull of
well-exposed representatives.

Equivalently, a deletion procedure can remove locally redundant vertices only
by borrowing nearby redundant vertices.  If this is iterated, the Hausdorff
error can grow from the local sagitta scale to the scale of the final coarse
polygon.  The local statement contains no mechanism preventing this growth.

## What Strengthening Is Sufficient

A non-accumulating formulation should be one-shot.  One clean version is:

```text
W_{rho,kappa} = {vertices v : e_v(rho) >= kappa}.
```

Prove directly that

```text
dist(p_i, conv(W_{rho,kappa})) <= gamma
```

for every row `p_i`, or at least for every row outside small clusters around
`W_{rho,kappa}`, with

```text
rho = O(tau),      gamma = O(tau),      kappa >= c tau.
```

This is exactly sufficient.  Indeed, choose a maximal `4 rho`-separated subset
`R` of `W_{rho,kappa}`.  Every point of `W_{rho,kappa}` is within `4 rho` of
some representative in `R`, so every point of `conv(W_{rho,kappa})` is within
`4 rho` of `conv(R)` by pushing convex weights to nearest representatives.
Thus every row is `gamma + 4 rho` close to `conv(R)`.  The representatives are
pairwise separated, and their exposing functions at scale `rho` also expose
at the larger cluster scale `2 rho`.  Applying
`cluster-representative-classical-stability.md` with cluster radius `2 rho`
gives the desired `O(tau)` stochastic idempotent.

This formulation automatically rules out the regular-polygon obstruction: if
there are no square-root-well-exposed vertices, then the exposed hull is empty
and the one-shot condition fails.

## Relation To The LP Dual

The current LP dual of failed exposedness gives, for a bad vertex `v`, a
probability measure on rows outside `B(v,rho)` whose barycenter is small
against every normalized positive affine function vanishing at `v`.  That is
still local.  It does not say that the barycenter lies near the hull of
well-exposed vertices; it may be supported entirely on other bad vertices.

The useful strengthened target is therefore:

```text
if dist(v, conv(W_{rho,kappa})) > C tau,
then v must be kappa-well-exposed at scale rho.
```

Equivalently, every LP dual witness for a non-well-exposed vertex must force
`v` to be `O(tau)`-close to `conv(W_{rho,kappa})`.  This is a global
normal-cone statement, not a pointwise deletion statement.  It is plausibly
the right place to use the exact retraction identity and row near-positivity;
it is not a consequence of arbitrary convex geometry.

