# Subagent Probe: Non-Simplex Classical Row Polytopes

## Question

After the simplex row-polytope theorem, the remaining classical case is:

```text
P1=1,        P^2=P,
neg(p_i) <= delta        for every row p_i,
K=conv{p_i} non-simplex.
```

Can a non-simplex row polytope stay farther than `O(sqrt(delta))` from every
stochastic idempotent, or does near positivity force it to be
`O(sqrt(delta))`-close to a simplex row polytope?

I did not find a counterexample. The strongest conclusion below is a precise
diagnosis of where the exposed-face recursion loses dimension-free constants.

Set

```text
tau = sqrt(delta).
```

## Exact Exposed-Face Identity

Let `phi` be an affine functional on the affine hull of `K`, and write

```text
M = max_{x in K} phi(x),
h(x)=M-phi(x) >= 0.
```

For any row `r=p_i`, exact idempotency gives

```text
rP = sum_j r_j p_j = r.
```

Applying `h` gives

```text
sum_j r_j h(p_j) = h(r).                         (1)
```

If `r` lies in the exposed face `F={h=0}`, then

```text
sum_j r_j h(p_j) = 0.
```

Decompose `r=r^+-r^-`. Since `0 <= h <= 1` after normalizing the functional,

```text
sum_j r^+_j h(p_j)
 = sum_j r^-_j h(p_j)
 <= neg(r)
 <= delta.                                      (2)
```

Thus for every `gamma>0`,

```text
r^+({j : h(p_j) >= gamma}) <= delta/gamma.      (3)
```

This is the exact signed version of the exposed-face leakage lemma. It is
dimension-free for one exposed face.

## Why This Does Not Yet Localize A Vertex

For a simplex vertex `r^a`, one affine coordinate `lambda_a` does all the work:

```text
0 <= lambda_a <= 1,
lambda_a(r^a)=1,
sum_a lambda_a = 1.
```

The single slack `1-lambda_a` localizes `r^a`, and the sets
`{lambda_a >= 1-tau}` are automatically disjoint.

For a general polytope, a vertex `v` is usually an intersection of several
facets. Let normalized slacks for the facets through `v` be

```text
h_1,...,h_k,        h_l >= 0,        h_l(v)=0,        0 <= h_l <= 1.
```

Equation (3) gives

```text
v^+({j : h_l(p_j) >= gamma}) <= delta/gamma
        for each l.
```

The naive corner set

```text
U_v(gamma)={j : h_l(p_j) <= gamma for all l=1,...,k}
```

therefore satisfies only

```text
v^+(U_v(gamma)^c) <= k delta/gamma.              (4)
```

Taking `gamma=tau` gives `k tau`, so the constant grows with the number of
facets through the vertex. This is the first loss.

The second loss is angular. Even if `k=2`, the geometric diameter of
`K cap {h_1<=gamma, h_2<=gamma}` can be `gamma/theta`, where `theta` is the
aperture/altitude of the corner in the ambient `l1` metric. In a thin wedge,
points at `l1`-distance `t` from `v` can have both facet slacks only
`O(theta t)`. Thus:

```text
diam(U_v(gamma)) ~ gamma/theta.
```

To make the corner slice have diameter `O(tau)`, one must take

```text
gamma ~ theta tau,
```

but then the leakage estimate becomes

```text
delta/gamma ~ tau/theta.                         (5)
```

Alternatively, taking `gamma=tau` keeps leakage `O(tau)` but permits rounding
error `O(tau/theta)`. Either way the recursive exposed-face proof depends on
inverse angle/altitude unless another argument shows that thin corners are
already redundant at scale `tau`.

A coordinate-free way to state the same obstruction is this. For a vertex `v`,
define its best normalized exposedness at scale `rho` by

```text
c_v(rho)
 = sup_phi min{ phi(v)-phi(x) :
                x in K, ||x-v||_1 >= rho },
```

where the supremum is over affine `phi` with `phi(v)=max_K phi` and
`Lip_{l1}(phi) <= 1`. From (3),

```text
v^+({j : ||p_j-v||_1 >= rho}) <= delta/c_v(rho). (6)
```

To get vertex concentration at the desired scale, one needs

```text
c_v(C tau) >= c tau
```

with universal constants. This is false for arbitrary polytopes; skinny normal
cones can make `c_v(rho)` arbitrarily smaller than `rho`. The near-positive
idempotency would have to force such skinny vertices to be `O(tau)`-redundant.

## Non-Simplex Affine Dependence Is A Real Additional Issue

Even if every vertex can be localized, a non-simplex polytope cannot simply
turn all its vertices into recurrent classes.

Example obstruction: suppose four vertex rows form a parallelogram relation

```text
r^1 + r^3 = r^2 + r^4.                            (7)
```

If a nearby stochastic idempotent had four distinct recurrent distributions
`pi_1,...,pi_4` corresponding to these four vertices, then their supports would
be disjoint. Hence

```text
||pi_1 + pi_3 - pi_2 - pi_4||_1 = 4.              (8)
```

But if each `r^a` were `epsilon`-close to `pi_a`, then (7) would imply

```text
4
 = ||pi_1 + pi_3 - pi_2 - pi_4||_1
 <= 4 epsilon.                                   (9)
```

So for `epsilon<1` this is impossible. A large square row polytope would have
to be rounded by collapsing some vertices or by replacing the square with a
nearby triangle/segment. Therefore the missing theorem is not merely
"construct a recurrent class near each exposed vertex"; it must show that
macroscopic affine dependencies cannot occur when `delta` is small.

The same point can be phrased as a possible cancellation lemma. If

```text
sum_{a in A} alpha_a r^a = sum_{b in B} beta_b r^b,
sum_A alpha_a = sum_B beta_b = 1,
alpha_a,beta_b >= 0,                              (10)
```

and exposed-face leakage placed `r^a_+` near mutually separated corner sets
`U_a`, then (10), restricted to `U_a`, would force a contradiction unless some
opposite-side vertex also puts positive mass into `U_a`, or unless the corner
sets overlap at `O(tau)` scale. This suggests that well-conditioned
non-simplexity should cost a definite amount of negative mass. I do not see a
dimension-free proof of that statement without the same angle/face-control
input above.

## Counterexample Search Status

No counterexample family was found.

Some easy sources do not look dangerous:

1. Fixed `n` cannot produce an obstruction that stays a definite distance
   from stochastic idempotents as `delta -> 0`. A convergent subsequence of
   nearly positive exact idempotents limits to a positive stochastic
   idempotent, whose row polytope is a simplex. This compactness point does
   not by itself rule out a worse local exponent at fixed `n`; I found no such
   fixed-dimensional family.

2. Four-row quadrilateral images in `n=4` lie in the rank-one-perturbation
   class `P=I-u v^T`, already covered by the rank-one theorem at
   `O(sqrt(delta))`.

3. Direct sums or independent copies of Hume-type escapes keep the rowwise
   distance at the `sqrt(delta)` scale; they do not create a larger
   dimension-growth obstruction by themselves.

The plausible obstruction is therefore not an explicit square with
`delta << side^2`; it is the absence of a dimension-free lemma saying such a
square, or a higher-dimensional affine dependence, is impossible.

## Lemma That Would Remove The Obstruction

The existing approximate-simplexity reduction would finish the classical
problem if one could prove the following dimension-free statement.

**Angle-free approximate simplexity lemma.** There are universal constants
`delta0,C` such that every exact signed affine retraction with
`neg(p_i)<=delta<=delta0` admits rows

```text
r^1,...,r^m
```

and affine functions `lambda_a` on `aff(K)` satisfying

```text
0 <= lambda_a(p_i) <= 1,
sum_a lambda_a(p_i)=1,
lambda_a(r^b)=delta_ab,
```

and

```text
||p_i - sum_a lambda_a(p_i) r^a||_1 <= C sqrt(delta)
        for every row p_i.                       (11)
```

Equivalently: after discarding or merging vertices at `O(tau)` scale, the row
polytope is `O(tau)`-close to a simplex in a way witnessed by affine
partition-of-unity coordinates.

The exposed-face recursion would prove this if it had an additional
dimension-free rule of the following form:

```text
If an exposed slice has large l1-diameter compared with its slack thickness,
then that long/thin part is O(tau)-close to a lower-dimensional face or to
convex hull data already selected by the recursion.
```

This is exactly the missing angle-removal step. Without it, the estimates
remain of the form

```text
rounding error <= C tau / (angular aperture),
leakage        <= C tau * (number of facets)/(angular aperture),
```

which is not dimension-free.

## Bottom Line

I found no non-simplex counterexample. The most useful conclusion is that the
current exposed-face method fails at a precise quantitative point: one-face
leakage is dimension-free, but converting exposed slacks into global simplex
coordinates requires either a facet-count union bound or an inverse
angle/altitude bound. A successful proof needs an angle-free
approximate-simplexity/cancellation lemma showing that any macroscopic
non-simplex affine dependence forces negative mass larger than `O(delta)`.
