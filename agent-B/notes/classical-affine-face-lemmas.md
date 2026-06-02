# Classical Affine Face Lemmas For Markov Sqrt Stability

This note records dimension-free lemmas for the commutative
near-positive-projection problem. They do not prove the full Markov
square-root theorem, but they isolate the geometric mechanism that should drive
any proof beyond the rank-one case.

## Setup

Let `Q` be an `n x n` row-stochastic matrix. Write `q_i` for its rows and

```text
eps = ||Q^2-Q||_{infty->infty}
    = max_i ||q_i Q-q_i||_1.
```

Equivalently, `Q` is an affine self-map `T` of the simplex `Delta_n`, with
`T(e_i)=q_i`.

For any signed vector `z` with total mass zero and any affine functional
`phi` on the simplex whose linear part has `l_infty` norm at most `1`,

```text
|phi(z)| <= ||z||_1.
```

Thus the row defect gives, for all such `phi`,

```text
|phi(q_i Q)-phi(q_i)| <= eps.                    (1)
```

## Lemma 1: Exposed-Face Leakage

Fix a `1`-Lipschitz affine functional `phi` and set

```text
m = max_j phi(q_j),        d_i = m-phi(q_i) >= 0.
```

Then

```text
sum_j q_i(j) (m-phi(q_j)) <= d_i + eps.          (2)
```

Consequently, for every `gamma>0`,

```text
q_i({j : phi(q_j) <= m-gamma}) <= (d_i+eps)/gamma.       (3)
```

Proof. Since `q_i Q=sum_j q_i(j)q_j`, (1) gives

```text
sum_j q_i(j) phi(q_j) >= phi(q_i)-eps.
```

Subtract from `m` and use `sum_j q_i(j)=1`, obtaining (2). The set in (3)
contributes at least `gamma` per unit of mass to the left side of (2).

## Corollary 2: Square-Root Closure Of Exposed Faces

If `q_i` is a maximizer of `phi` on the row polytope, then for
`gamma=sqrt(eps)`,

```text
q_i({j : phi(q_j) <= m-sqrt(eps)}) <= sqrt(eps).
```

More generally, every row in the `alpha`-exposed slice
`phi(q_i)>=m-alpha` sends all but `(alpha+eps)/gamma` of its mass into the
`gamma`-exposed slice.

This is the same square-root scale as Hume's sharp boundary example. It is the
first place where no linear estimate can be expected near a face of the
stochastic-idempotent variety.

## Lemma 3: Signed Retractions Reduce To The Same Leakage Estimate

Let `P` be a row-unital exact idempotent with row negative masses at most
`delta`. For each row `p_i`, define the repaired probability

```text
q_i = p_i^+ / ||p_i^+||_1.
```

Then the stochastic matrix `Q` with rows `q_i` satisfies

```text
||P-Q||_{infty->infty} <= 2 delta,
||Q^2-Q||_{infty->infty} <= 6 delta+4 delta^2.
```

Therefore Lemma 1 applies to every nearly positive signed affine retraction
after replacing `eps` by `O(delta)`.

## What This Gives

The leakage lemma is a dimension-free substitute for the elementary exact
fact: in an idempotent Markov chain, an exposed recurrent class cannot leak to
lower exposed levels. In the perturbative case, an exposed slice only leaks
`O(eps/gamma)`. Choosing `gamma=sqrt(eps)` gives the sharp scale.

A plausible recursive proof of the full Markov theorem would:

1. choose a functional exposing a diameter-scale face of the row polytope;
2. use Lemma 1 to show this face is almost closed at scale `sqrt(eps)`;
3. collapse/round that face to one recurrent component;
4. recurse on the complementary mass.

The missing part is a dimension-free rule that carries out this recursion
without accumulating constants with the number of faces or states. The lemma
also does not by itself control non-exposed transient rows; those must be
rounded as convex combinations of the recurrent components.

## Current Status

These estimates are compatible with the proved rank-one theorem and with
Hume's sharp `3 x 3` family. They are not yet enough to prove

```text
dist(Q, stochastic idempotents) <= C sqrt(eps)
```

with a universal `C`.
