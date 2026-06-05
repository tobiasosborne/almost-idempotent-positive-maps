# Regular Polygon Retraction Obstruction

This note records a counterexample search that turned into a useful obstruction:
dense regular polygons are not plausible counterexamples to the classical
near-positive projection-stability conjecture.

The reusable abstraction is recorded separately in
`agent-B/notes/symmetric-coordinate-negative-mass-criterion.md`.

## Setup

Let `K_m` be the regular `m`-gon in `R^2`, with vertices

```text
x_i=(cos(2*pi*i/m), sin(2*pi*i/m)).
```

An exact row-unital idempotent whose row polytope is affinely equivalent to
`K_m` gives affine coordinate functions on `K_m`. In abstract form, there are
row points `y_alpha in K_m` and affine functions `lambda_alpha:K_m->R` such
that

```text
sum_alpha lambda_alpha(x)=1,
sum_alpha lambda_alpha(x)y_alpha=x
```

for all `x in K_m`. The row negative-mass defect at a vertex is

```text
neg_x(lambda)=sum_alpha max(-lambda_alpha(x),0).
```

If the classical square-root theorem failed through dense regular polygons, one
would expect such systems with `max_i neg_{x_i}(lambda)->0` as `m->infty`.
This cannot happen.

## Proposition

There is a universal constant `c0>0` such that every dihedrally symmetric affine
coordinate system for `K_m` has vertex negative mass at least `c0-o_m(1)`.
In fact the sharp asymptotic lower bound is

```text
sqrt(3)/pi - 1/3 ~= 0.218.
```

Consequently, a dense regular polygon of fixed diameter cannot be the row
polytope of exact signed affine retractions with row negative mass tending to
zero.

## Proof Sketch

The minimization of the maximum vertex negative mass is convex and invariant
under the dihedral group. Averaging any coordinate system over the group gives a
dihedrally symmetric system with no larger maximum negative mass. It is enough
to analyze symmetric systems.

A symmetric orbit of row points at radius `0<=r<=1` contributes coefficients of
the form

```text
lambda_k(x_i) = (a + 2c cos(2*pi*(i-k)/m))/m.
```

The total mass contribution of the orbit is `a`, and its barycentric
contribution is `cr x_i`. A possible center coordinate contributes a scalar
`t`. Therefore the constraints are

```text
sum_l a_l + t = 1,
sum_l c_l r_l = 1.
```

Since `r_l<=1`, one has `sum_l |c_l|>=1`.

For the continuous limiting negative-part functional

```text
Phi(a,c) = (1/(2*pi)) int_0^{2*pi} max(0, -a - 2c cos theta) dtheta,
```

convexity at `(a,c)=(1,1)` gives the supporting bound

```text
Phi(a,c) >= (sqrt(3)/pi)|c| - a/3.                 (1)
```

Indeed the active set at `(1,1)` is
`{theta: cos theta < -1/2}`, which has normalized measure `1/3`, and

```text
(1/(2*pi)) int_{cos theta<-1/2} -2 cos theta dtheta = sqrt(3)/pi.
```

The center coefficient satisfies `max(0,-t) >= -t/3`. Summing `(1)` over
orbits and adding the center gives

```text
total negative mass
  >= (sqrt(3)/pi) sum_l |c_l| - (1/3)(sum_l a_l+t)
  >= sqrt(3)/pi - 1/3.
```

The discrete `m`-gon version is the corresponding Riemann sum and converges to
the same constant.

For the vertex-only coordinate system the symmetric formula is forced:

```text
lambda_j(x_i) = (1 + 2 cos(2*pi*(i-j)/m))/m,
```

and its negative mass tends exactly to the same constant. Thus the bound is
sharp asymptotically.

## Why The Tempting Local Construction Fails

The local identity

```text
x_i = (x_{i-1}+x_{i+1})/(2 cos theta)
      + (1 - 1/cos theta) * 0,        theta=2*pi/m,
```

has negative mass `1/cos(theta)-1=O(theta^2)`. But it is not an affine coordinate
system on `K_m`. As a circulant matrix stencil its Fourier multipliers are

```text
mu_k = cos(k theta)/cos(theta),
```

so exact idempotency would require all `mu_k` to be `0` or `1`, which already
fails at `k=2`. Exact projection onto the affine modes `0, +/-1` recovers the
first-harmonic coordinate kernel above and hence the constant negative mass.

## Consequence For The Global Exposed-Hull Program

The regular-polygon warning in
`agent-B/notes/simultaneous-skeleton-reduction.md` remains logically useful:
arbitrary convex geometry can make pointwise deletion accumulate. But regular
polygons do not appear realizable as small-defect exact signed affine
retractions. A genuine counterexample to the global exposed-hull lemma would
need more subtle, non-regular geometry or would have to shrink its offending
non-simplex feature to the `O(sqrt(delta))` scale, which would no longer violate
the desired conclusion.
