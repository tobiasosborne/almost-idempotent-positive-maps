# Symmetric Coordinate Negative-Mass Criterion

This note extracts a reusable obstruction from
`regular-polygon-retraction-obstruction.md`.

## Signed Coordinate Systems

Let `K` be the row polytope of an exact row-unital signed idempotent `P`.
Writing the row points as `y_alpha in K`, exact idempotency gives affine
coordinates

```text
lambda_alpha:K -> R
```

with

```text
sum_alpha lambda_alpha(x)=1,
sum_alpha lambda_alpha(x)y_alpha=x                       (1)
```

for every `x in K`. Conversely, such a signed affine coordinate system is the
geometric content of the row-retraction identity. The row near-positivity defect
is the maximum negative coordinate mass at the row points:

```text
delta(lambda)=sup_x sum_alpha max(-lambda_alpha(x),0).
```

Thus a proposed row-polytope counterexample to projection stability must carry
signed affine coordinates satisfying `(1)` with `delta(lambda)->0`.

## Symmetrization Lemma

Let a finite group `G` act affinely on `K`, and suppose `V subset K` is a
`G`-invariant set of row points. If there is a coordinate system with

```text
max_{v in V} neg_v(lambda) <= delta,
```

then there is a `G`-equivariant coordinate system, possibly after splitting
coordinates into more labels, with the same barycentric identity `(1)` and

```text
max_{v in V} neg_v(lambda^G) <= delta.
```

Indeed, for each coordinate pair `(lambda_alpha,y_alpha)` and each `g in G`,
add the coordinate

```text
|G|^{-1} lambda_alpha(g^{-1}x)
```

at the point `g y_alpha`. The identities `(1)` average correctly. At a point
`v`,

```text
neg_v(lambda^G)
 <= |G|^{-1} sum_g neg_{g^{-1}v}(lambda)
 <= max_{w in V} neg_w(lambda).
```

Therefore any lower bound proved for equivariant coordinate systems is a lower
bound for all coordinate systems.

This is the main correction to naive convex-geometric counterexample searches:
one cannot test a symmetric polytope by writing down an arbitrary local
barycentric identity. Exact idempotency asks for a global affine coordinate
system, and the optimum can be assumed symmetric.

## Harmonic Lower-Bound Template

Assume the symmetrized coordinate system decomposes into orbit families whose
coefficient functions at a test point are affine first-harmonic kernels

```text
a_l + <b_l, x>
```

normalized over the orbit. If the barycentric identity forces a nonzero total
first-harmonic coefficient, then negative mass is bounded below by any
supporting functional for the convex function

```text
(a,b) |-> average_orbit max(0, -a-<b,x>).
```

Concretely, if for all orbit families one has

```text
average_orbit max(0, -a_l-<b_l,x>)
  >= A ||b_l|| - B a_l,
```

and the affine constraints imply

```text
sum_l ||b_l|| >= L,        sum_l a_l = 1,
```

then every exact signed retraction with this symmetric row geometry has

```text
delta >= A L - B.
```

If `A L-B` is a positive absolute constant, that geometry is impossible in the
small-defect regime.

## Application: Regular Polygons

For the regular `m`-gon, symmetrization over the dihedral group reduces all
orbits to kernels

```text
(a+2c cos theta)/m.
```

The barycentric constraint gives `sum_l |c_l|>=1`, while total mass gives
`sum_l a_l+t=1`, including a possible center coordinate `t`.

The continuous limiting negative-part functional

```text
Phi(a,c)=(1/(2*pi)) int max(0,-a-2c cos theta) dtheta
```

has the supporting lower bound at `(a,c)=(1,1)`

```text
Phi(a,c) >= (sqrt(3)/pi)|c| - a/3.
```

Adding the center contribution `max(0,-t)>=-t/3` yields

```text
delta >= sqrt(3)/pi - 1/3 - o_m(1).
```

So fixed-diameter dense regular polygons are ruled out as small-defect exact
signed affine retractions.

## Use In Future Counterexample Searches

Before trying to turn a symmetric convex-geometric warning example into a
signed-idempotent counterexample, compute the equivariant coordinate
negative-mass optimum. If it has a positive lower bound, the geometry cannot
occur with `delta->0`.

The global exposed-hull lemma remains open because this criterion only rules
out geometries with enough symmetry to force a large first-harmonic coefficient.
It does not control arbitrary non-regular thin chains or asymmetric
near-circuits.
