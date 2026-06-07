# Subagent C: Robust Coordinates For `op-exposed-hull`

Date: 2026-06-07.  Lane: Agent B sandbox.  Exploratory only; not a canonical
proof shard.

## Target

Given an exact signed affine retraction

```text
P1=1,        P^2=P,        neg(p_i)<=delta,        tau=sqrt(delta),
```

construct selected rows `r^a` and affine coordinates `lambda_a` on `aff(K)`
such that

```text
sum_a lambda_a=1,
lambda_a(r^b)=delta_ab,
neg(lambda(p_i))<=O(delta),
||p_i-sum_a lambda_a(p_i)r^a||_1<=O(tau).
```

Then `robust-approximate-simplexity-reduction.md` gives a stochastic idempotent
within `O(tau)`.

## Verdict

The route is plausible but not closed.  The hard point is not rowwise
reconstruction by an exposed hull; it is producing one global affine coordinate
certificate with coefficient negative mass `O(delta)`.  Natural constructions
split into two imperfect types:

- `O(delta)` negativity with only approximate representative interpolation;
- exact interpolation with only `O(tau)` negativity.

The most promising analytic target is the interpolation-upgrade problem in
Candidate 2.

## Right-Fixity Identities

For every affine `f:K->R`,

```text
f(p_i)=sum_j p_ij f(p_j).                         (RF)
```

For coordinates `z_i=lambda(p_i)`,

```text
z_i=sum_j p_ij z_j.                               (RF-coord)
```

If `lambda_a(r^b)=delta_ab`, then

```text
sum_j r^a_j lambda_b(p_j)=delta_ab.               (BI)
```

The robust-simplex proof uses `(BI)` with `b=a`:

```text
sum_j r^a_j(1-lambda_a(p_j))=0.
```

If `lambda_a` is bounded in `[-kappa,1+kappa]`, this concentrates the positive
part of `r^a` near `{lambda_a>=1-tau}` at cost `O(sqrt(delta+kappa))`.  Hence
`kappa` must be `O(delta)` to keep the final square-root rate; `O(tau)`
coordinate negativity is too large.

## Candidate 1: Barycentric Coordinates Of An Exposed Skeleton

Let `R={r^1,...,r^m}` be a maximal separated subset of square-root-well-exposed
vertices.  Exposed-circuit cancellation gives

```text
||sum_a c_a r^a||_1 >= (1-C tau) sum_a |c_a|.     (EC)
```

So `R` is affinely independent and barycentric coordinates on `aff(R)` are
angle-free.  If a global affine map `T:aff(K)->aff(R)` fixes `R` and satisfies
`||p_i-Tp_i||_1<=gamma`, then barycentric coordinates of `Tp_i` have negative
mass `O(gamma)`.  With `gamma=O(tau)`, this is only `O(tau)`.

Needed upgrade:

```text
If lambda is the barycentric coordinate system of a maximal well-exposed
skeleton and ||p_i-sum_a lambda_a(p_i)r^a||_1<=C tau, prove
neg(lambda(p_i))<=C delta for actual rows p_i.
```

Obstacle: `(RF-coord)` is a signed harmonicity identity.  A negative coordinate
of size `-tau` can be supported by positive mass on other `-tau` rows unless
maximality/exposedness forces a new representative or a reconstruction by the
existing hull.

Also, rowwise distances `dist(p_i,conv R)<=O(tau)` do not supply a single
affine `T`; nearest-point choices are nonlinear.  This is why the cluster
theorem is easier than robust coordinates.

## Candidate 2: Push-Forward Of Canonical Coordinates

Exact idempotency gives canonical affine coordinates indexed by all row labels:

```text
x=sum_j x_j p_j,        sum_j x_j=1.
```

Choose a probability kernel from row labels to representatives,

```text
mu(j) in Delta_R,
||p_j-sum_a mu_a(j)r^a||_1<=gamma.
```

Define

```text
lambda_a(x)=sum_j x_j mu_a(j).
```

Then for every row `p_i`,

```text
neg(lambda(p_i)) <= neg(p_i) <= delta,
||p_i-sum_a lambda_a(p_i)r^a||_1 <= (1+2delta)gamma.
```

This is the cleanest `O(delta)` mechanism: stochastic push-forward cannot
increase negative mass.

Catch: representative interpolation.  Let

```text
G_ba=lambda_a(r^b)=sum_j r^b_j mu_a(j).
```

If `mu(j)=e_a` on exposed clusters `U_a`, one-row concentration gives only

```text
G=I+O(delta/kappa+delta)=I+O(tau)
```

for `kappa~tau`.  Multiplying by `G^{-1}` exactifies interpolation but can
introduce `O(tau)` negative mass.

Key open subtarget:

```text
Can mu be chosen with G=I+O(delta), gamma=O(tau), and mu(j) in Delta_R?
```

Existing exposedness estimates only give `I+O(tau)`.

## Candidate 3: LP Coordinate Certificate

Set variables `lambda_a(i)` on rows.  Feasibility constraints:

```text
sum_a lambda_a(i)=1,
lambda_a(r^b)=delta_ab,
lambda_a respects every affine relation among the p_i,
||p_i-sum_a lambda_a(i)r^a||_1 <= gamma,
sum_a max(-lambda_a(i),0) <= K delta.
```

Feasibility with `gamma=C tau` and universal `K,C` proves the coordinate route.
An infeasibility dual should either expose a missing representative or identify
the real obstruction.  This is the next computational step.

## Numerical Probe

Added and ran:

```text
python3 agent-B/experiments/op-exposed-hull/robust_coordinate_probe.py
```

Output: `agent-B/experiments/op-exposed-hull/robust_coordinate_probe.json`.
Script SHA256:
`4392fd5c70c87c5a1791a77d0cad22821c1d913b23c23c7fed7e85bc9ff4b1c4`.

Probe results:

- Hume rank-one family: best simplex coordinates have zero negative mass for
  `s=0.2,0.05,0.01`; the sharp `sqrt(delta)` family is not a coordinate
  obstruction.
- Regular polygons: best affine simplex representative coordinates have
  constant negative mass, e.g. `1/3` for `m=12,24,48`.  This is generic convex
  geometry only, not a small-defect retraction counterexample.
- Thin rectangles: best triangle coordinates have max negative mass `1` for
  aspect ratios `1,0.1,0.01,0.001`.  Hausdorff closeness to a segment does not
  imply robust affine coordinates; affine circuits must be killed separately.

## Failure Modes

1. Local chord coordinates on regular polygons can have small local negative
   mass but are not global affine coordinates.
2. Exactifying an interpolation matrix `G=I+O(tau)` via `G^{-1}` generally
   creates `O(tau)` signed coefficients, losing the target rate.
3. Rowwise convex reconstruction by `conv R` gives the cluster theorem, not
   robust coordinates, unless the choices come from one affine map.
4. Pure convex thinness is misleading: unresolved circuits can force
   order-one affine coordinate negativity.

## Next Handoff

1. Implement the full LP in Candidate 3 with `scipy.optimize.linprog`.
2. Test Hume, thin parallelograms, regular polygons with exact-retraction
   coordinate constraints, random low-rank signed idempotents, and Hume
   products.
3. Attack the interpolation-upgrade target for Candidate 2.  If it fails,
   extract the dual obstruction and feed it to the maximal-skeleton route.

Candidate sandbox contracts if this route succeeds:

```text
lem-push-forward-robust-coordinates:
rowwise probability reconstructions push canonical coordinates to affine
representative coordinates with neg <=delta and reconstruction <=(1+2delta)gamma.

lem-coordinate-interpolation-upgrade:
for a maximal square-root-exposed skeleton, choose the reconstruction kernel
with representative Gram matrix I+O(delta).

prop-robust-coordinate-exposed-hull:
combine the previous lemmas with robust approximate simplexity.
```

The interpolation-upgrade contract is the hard open piece.
