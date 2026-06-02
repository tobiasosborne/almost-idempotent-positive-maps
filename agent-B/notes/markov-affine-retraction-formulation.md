# Markov Sqrt Stability As Affine Retraction Stability

This note reformulates the commutative core of near-positive projection
stability.

## Markov Form

The open theorem is:

```text
Q row-stochastic, ||Q^2-Q||_{infty->infty} <= eps
  => dist(Q, stochastic idempotents) <= C sqrt(eps).
```

Rows are measured in `l1`, so `||Q^2-Q||_{infty->infty}` is the maximum
`l1`-distance between the one-step and two-step laws.

## Affine Simplex Form

Let `Delta_n` be the probability simplex with `l1` metric. A row-stochastic
matrix `Q` is the same as an affine map

```text
T:Delta_n -> Delta_n,
T(e_i)=q_i.
```

The defect is

```text
sup_i ||T^2(e_i)-T(e_i)||_1 <= eps.
```

By affinity, the same bound holds on all of `Delta_n`:

```text
sup_{mu in Delta_n} ||T^2(mu)-T(mu)||_1 <= eps.
```

Thus the theorem asks whether every affine `eps`-retraction of a simplex is
`C sqrt(eps)`-close to an exact affine retraction of the same simplex.

Equivalently, for the image polytope

```text
K=T(Delta_n)=conv{q_i},
```

`T` moves every point of `K` by at most `eps`. We need an exact affine
retraction `E` of `Delta_n` whose vertex values are close to the `q_i`.

## Exact Idempotent Geometry

If `E` is stochastic and idempotent, its rows `e_i` satisfy

```text
e_i = sum_j e_i(j) e_j.
```

The distinct extreme rows are stationary laws on disjoint recurrent row
classes. Every other row is a convex combination of those extreme rows. This
is the finite-dimensional form of Blackwell/Doob idempotent Markov-chain
classification.

So the perturbative problem is not to approximate `Q` by its Cesaro limit. A
slow two-state chain is close to the identity idempotent, while its Cesaro
limit is rank one and far away.

## Elementary Consequences Of `Q^2 ~= Q`

Let `q_i` denote row `i`. For every subset `S` of states,

```text
| sum_j q_i(j) q_j(S) - q_i(S) | <= eps/2
```

if `eps` is the row `l1` defect; with harmless constants one can use `eps`.

Consequences:

1. If `q_i(S) <= alpha`, then the `q_i`-average leakage into `S` after one
   more step is at most `alpha+eps`.
2. If `q_i(S) >= 1-alpha`, then the `q_i`-average leakage out of `S` is at
   most `alpha+eps`.
3. More generally, if `q_i(j) >= beta`, then

   ```text
   q_j(S) <= (q_i(S)+eps)/beta
   ```

   for every `S`. Thus rows receiving large mass from `q_i` cannot put much
   mass where `q_i` puts almost none.

These estimates are dimension-free, but they are not yet enough. A barycenter
can be nearly fixed while its components are far away; that situation should
correspond to an exact idempotent with several recurrent components, not to
row clustering.

## Where The Square Root Enters

The spectral idempotent

```text
P=theta(2Q-I)
```

satisfies `||P-Q||=O(eps)` and is an exact signed affine retraction preserving
total mass. Since `Q` is stochastic, each row of `P` has negative mass
`O(eps)`. Therefore the Markov theorem is equivalent to:

```text
exact affine retraction P of R^n,
P(Delta_n) subset O(eps)-neighborhood of Delta_n
  => P is O(sqrt(eps))-close to an affine retraction of Delta_n.
```

For a signed probability vector `mu`, the `l1`-distance to `Delta_n` is exactly

```text
dist(mu,Delta_n)=2 neg(mu),
neg(mu)=sum_i max(-mu_i,0).
```

Thus

```text
sup_{x in Delta_n} dist(Px,Delta_n)
```

is controlled by the maximum row negative mass of `P` up to this factor. The
supremum is attained at a vertex because distance to a convex set is convex.

Hume's `3 x 3` example shows that `sqrt` is the best possible exponent at a
boundary stratum of the exact-retraction variety.

## Current Proof Target

A dimension-free proof should probably operate on the exact signed retraction
`P` rather than directly on `Q`:

1. understand the face of `Delta_n` selected by the nearly positive affine
   range `P(Delta_n)`;
2. cluster only those rows whose separation is below `sqrt(eps)`;
3. split metastable rows whose mutual transition mass is only `O(eps)`;
4. construct the exact stochastic idempotent from the resulting recurrent
   row classes.

The missing lemma is a dimension-free local error bound for affine retractions
near the simplex:

```text
dist(P, stochastic idempotent affine retractions)
 <= C sqrt( sup_{x in Delta_n} dist(Px,Delta_n) ).
```

This is the cleanest classical target currently known.
