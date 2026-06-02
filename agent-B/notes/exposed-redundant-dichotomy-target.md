# Exposed-Or-Redundant Dichotomy Target

This note formalizes the remaining geometric lemma suggested by
`agent-B/notes/subagent-exposed-redundant-classical-v0.1.md`.

It is not a proof. It is a sharpened target for the classical square-root
projection-stability theorem.

Update: the pointwise version below is no longer considered sufficient by
itself.  The non-accumulating formulation is the global exposed-hull target in
`agent-B/notes/simultaneous-skeleton-reduction.md`: if
`W_{rho,kappa}` is the set of vertices well exposed at
`rho=O(sqrt(delta))` with gap `kappa>=c sqrt(delta)`, then every row should be
`O(sqrt(delta))`-close to `conv W_{rho,kappa}`.  That global statement implies
the cluster-representative hypotheses without sequential deletion.  The local
dichotomy below remains useful only as motivation or if strengthened by a
non-accumulating reconstruction certificate.

## Setup

Let `P` be an exact signed affine retraction:

```text
P1=1,        P^2=P,
```

with rows `p_i`, row polytope `K=conv{p_i}`, and

```text
neg(p_i)<=delta
```

for every row. Set

```text
tau=sqrt(delta).
```

For a row vertex `v` of `K` and scale `rho`, define the outside row set

```text
S_v(rho)={p_i: ||p_i-v||_1>=rho}.
```

## Exposedness Modulus

Define

```text
e_v(rho)
 = sup_h  min_{x in S_v(rho)} h(x),
```

where the supremum is over affine functions

```text
h:K->[0,1],        h(v)=0.
```

Thus `e_v(rho)>=kappa` exactly means that `v` is exposed with gap `kappa`
outside the `rho`-cluster.

Wegener's exposed-vertex concentration lemma says:

```text
e_v(rho)>=kappa
  =>  v is C(delta/kappa+delta)-close
      to a probability supported on {i: ||p_i-v||_1<rho}.
```

In particular, `e_v(rho)>=c tau` gives `O(tau)` concentration.
The proved form, including the multi-vertex circuit-cancellation consequence,
is recorded in `agent-B/notes/exposed-circuit-cancellation.md`.

## Desired Dichotomy

The original local missing lemma was expected to have the following form.

There are universal constants `c,C` such that, for every row vertex `v` and
`rho=C tau`, either:

1. `e_v(rho)>=c tau`; or
2. `v` is `C tau`-redundant, meaning

   ```text
   dist_1(v, conv{p_i: p_i != v}) <= C tau
   ```

   or, more flexibly, `v` can be removed from the candidate vertex set while
   preserving every row of `K` up to `C tau` reconstruction error by the
   remaining rows.

The second, flexible version is the one needed by
`agent-B/notes/robust-approximate-simplexity-reduction.md`.

This local statement is not enough on its own.  Pointwise redundancy can be
circular: a non-well-exposed vertex may be reconstructed only from other
non-well-exposed vertices.  Iterating such reconstructions can accumulate
dimension-dependent error.  The replacement target is:

```text
dist_1(v, conv W_{rho,kappa}) > C tau
  => e_v(rho)>=kappa,
```

or equivalently,

```text
dist_1(p_i, conv W_{rho,kappa}) <= C tau
```

for every row `p_i`, with `rho=O(tau)` and `kappa>=c tau`.

## LP Dual Form Of Failure

For fixed `v,rho,kappa`, the assertion `e_v(rho)<kappa` is an LP statement.
By minimax/Farkas, it is equivalent to the existence of a probability measure
`mu` on `S_v(rho)` such that its barycenter

```text
y=sum_{x in S_v(rho)} mu_x x
```

has small value against every normalized positive affine function vanishing at
`v`:

```text
h(y)<kappa
```

for all affine `h:K->[0,1]` with `h(v)=0`.

Thus the local missing dichotomy would amount to proving that such a dual
witness forces `y` to be `O(tau)`-close to `v`, or at least forces `v` to be
`O(tau)`-reconstructible from non-`v` rows, under the additional signed
retraction and row near-positivity hypotheses.

For the current global target, this is still too local.  The dual witness
must instead force `v` to be `O(tau)`-close to the hull of
`W_{rho,kappa}`, the already well-exposed vertices.  A witness supported only
on other non-well-exposed vertices does not close the proof.

This is the exact place where arbitrary convex geometry can lose inverse
angle constants: small values of all normalized supporting functions do not
by themselves give an `l1` distance bound without some normal-cone control.
The conjectural content is that the retraction identity plus
`neg(p_i)<=delta` supplies this missing normal-cone control at scale `tau`.

## How The Local Version Would Have Finished The Classical Theorem

Assume the local dichotomy plus a non-accumulating removal procedure.

1. Start with all row vertices of `K`.
2. Remove every `C tau`-redundant vertex. This changes row reconstruction only
   by `O(tau)`.
3. The remaining vertices are `c tau`-well-exposed at scale `C tau`.
4. The exposed-circuit cancellation lemma says the remaining vertices cannot
   satisfy a nontrivial affine dependence when `delta` is small.
   Hence they form a simplex.
5. The robust approximate-simplexity reduction then produces a stochastic
   idempotent within `O(tau)`.

The hard step is exactly the non-accumulation.  Hubble's sidecar report
`agent-B/notes/subagent-skeleton-reduction-v0.1.md` gives the convex-geometric
warning: dense regular polygons can satisfy pointwise redundancy while having
no square-root-well-exposed vertices.  They are not claimed to be
near-positive signed retractions, but they show the local implication is
logically invalid without an additional global certificate.

## Stress-Test Boundary

Tensor products of Hume's sharp `3 x 3` example remain a useful stress test.
Naive product rounding gives a dimension-growing error, but transient-class
rounding may keep the error at `O(sqrt(delta_k))`. A lower bound against all
such roundings would be needed for a counterexample.

Current evidence therefore still favors the square-root theorem, but the
global exposed-hull statement in
`agent-B/notes/simultaneous-skeleton-reduction.md` is now the precise
unproved geometric core.
