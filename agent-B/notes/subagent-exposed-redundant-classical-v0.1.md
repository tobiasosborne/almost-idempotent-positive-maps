# Subagent Report: Exposed-Or-Redundant Classical Route

Sidecar: Wegener.

Status: read-only probe; no files edited by the sidecar.

## Bottom Line

No credible counterexample to the classical square-root projection-stability
conjecture was found. The useful output is a sharper remaining target:
replace the vague "find approximate simplex coordinates" problem by an
exposed-or-redundant vertex dichotomy plus an exposed-circuit cancellation
lemma.

The exposed-circuit cancellation lemma below is complete under its
hypotheses. The missing ingredient is the dimension-free angle-removal
dichotomy.

The complete proof has been extracted to
`agent-B/notes/exposed-circuit-cancellation.md`; the present note preserves
the sidecar stress-test report and the route formulation.

## Tensor Hume Stress Test

The most dangerous test family is the `k`-fold tensor product of Hume's
`3 x 3` sharp family.

For one factor, the negative mass is `s^2` and the distance to stochastic
idempotents is `~2s`. For the tensor product,

```text
delta_k=max row negative mass
       = ((1+2s^2)^k-1)/2
       = k s^2 + O(k^2 s^4).
```

Naively tensoring one-factor nearest stochastic idempotents gives error about
`2ks`, so the ratio to `sqrt(delta_k)` appears to grow like `sqrt(k)`.

This is not a lower bound. Stochastic idempotent classification allows
high-escape rows to be made transient, while recurrent supports are truncated
to low escape count. That rounding plausibly stays at `O(sqrt(delta_k))`.
Thus the tensor Hume family is a false alarm unless one proves a lower bound
against all transient-class roundings, not just product roundings.

## Exposed Vertex Concentration Lemma

Let

```text
P1=1,        P^2=P,
```

with rows `p_i`, row polytope `K=conv{p_i}`, and

```text
neg(p_i)<=delta
```

for every row. Put `tau=sqrt(delta)`.

Suppose a row vertex `v` has an affine function

```text
h:K->[0,1]
```

such that

```text
h(v)=0,
h(x)>=kappa        whenever ||x-v||_1>=rho.
```

Since `vP=v`, idempotency gives

```text
sum_j v_j h(p_j)=0.
```

With `v=v^+-v^-` and `0<=h<=1`,

```text
sum_j v^+_j h(p_j)
 = sum_j v^-_j h(p_j)
 <= neg(v)
 <= delta.
```

Hence

```text
v^+({j: ||p_j-v||_1>=rho}) <= delta/kappa.       (E1)
```

Let `U_v={j: ||p_j-v||_1<rho}` and define

```text
pi_v=v^+|_{U_v}/||v^+|_{U_v}||_1.
```

Then `pi_v` is a probability measure supported on `U_v` and

```text
||v-pi_v||_1 <= C(delta/kappa + delta).          (E2)
```

In particular, if `kappa>=c tau`, then

```text
||v-pi_v||_1 <= C_c tau.
```

## Exposed-Circuit Cancellation

Take pairwise `2rho`-separated row vertices `v_a`, each satisfying the same
exposedness hypothesis with `kappa>=c tau`. The supports `U_{v_a}` are
disjoint, so the probability measures `pi_a` above are mutually singular.

For any real coefficients `c_a`,

```text
||sum_a c_a v_a||_1
 >= (1-C_c tau) sum_a |c_a|.                    (E3)
```

Therefore well-exposed separated vertices cannot satisfy a nontrivial affine
dependence when `delta` is small. This intrinsically subsumes the bounded
binary-coordinate/parallelogram cancellation lemma: instead of requiring
explicit `[0,1]` coordinate bits, it requires each vertex to be exposed with a
uniform gap at scale `rho`.

## Missing Dichotomy

The remaining theorem can be phrased as:

For every vertex `v` and scale `rho~tau`, either

1. `v` has a `[0,1]`-valued exposing function with gap `>=c tau` outside
   `B_1(v,rho)`; or
2. `v` is `O(tau)`-close to the convex hull of rows outside, or around, that
   vertex cluster, so it can be merged without changing the row polytope
   beyond `O(tau)`.

If this exposed-or-redundant dichotomy is proved dimension-free, then
`(E3)` rules out the well-exposed non-simplex circuits, while redundant
vertices can be merged. Combined with the robust approximate-simplexity
reduction, this would finish the classical square-root theorem.

## Obstacle

The one-face leakage estimate is already sharp and dimension-free. The only
remaining loss is converting many local facet slacks into global simplex data
without constants depending on facet count or inverse angle/altitude.

This formulation isolates the missing angle-removal step as an intrinsic
exposedness-versus-redundancy problem.

A more formal statement of the exposedness modulus, LP-dual obstruction, and
the exact dichotomy target is recorded at
`agent-B/notes/exposed-redundant-dichotomy-target.md`.
