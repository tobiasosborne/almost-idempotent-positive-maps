# Stochastic, Doubly Stochastic, And Stoquastic Special Cases

This note records the clean commutative model problems and the related
doubly-stochastic/stoquastic special cases.

It also records what numerical evidence we currently have.  The evidence is
meaningful but limited: it supports the square-root projection-stability
picture and the algebraic bridge, but there is not yet a dedicated
stoquastic-specific numerical search in this repo.

## Canonical Stochastic Conjecture

The cleanest commutative formulation is a Markov-kernel stability conjecture.

There should be universal constants `C,eta0>0` such that every row-stochastic
matrix `Q` satisfying

```text
||Q^2-Q||_{infty->infty} <= eta <= eta0
```

is close to a row-stochastic idempotent matrix `E`:

```text
||Q-E||_{infty->infty} <= C sqrt(eta).
```

Here the norm is the maximum `l1` norm of a row.  The exponent `1/2` is sharp
if the theorem is true.

## Equivalent Signed-Idempotent Form

Equivalently, up to constants, one may work with exact signed affine
retractions.

Let `P` be a real matrix with

```text
P1=1,        P^2=P,
```

and suppose every row has small negative mass

```text
neg(p_i)=sum_j max(-p_i(j),0) <= delta.
```

The conjecture is:

```text
dist(P, {row-stochastic idempotents}) <= C sqrt(delta).
```

The equivalence is recorded in
`agent-B/notes/subagent-classical-sqrt-stability-proof.md`: rowwise truncation
turns `P` into a stochastic almost-idempotent matrix with defect
`O(delta)`, and spectral functional calculus turns an almost-idempotent
stochastic `Q` into an exact signed idempotent with row negative mass
`O(eta)`.

## Doubly Stochastic Special Case

A natural special case is to assume, in addition, that the matrix preserves
the uniform state:

```text
1^T P = 1^T.
```

For an exactly nonnegative matrix, this case is rigid.  If `P` is row- and
column-stochastic and `P^2=P`, then the Markov chain has no transient states.
The state space splits into disjoint recurrent blocks, and on each block the
rows are the uniform distribution on that block.  Thus `P` is a block-average
projection.

Consequently, in the exact positive doubly stochastic case, the global
exposed-hull lemma holds with zero error: the row polytope is a simplex whose
vertices are the block-uniform rows.

For signed nearly positive idempotents, Birkhoff's theorem is not directly
applicable.  Birkhoff says a nonnegative doubly stochastic matrix is a convex
combination of permutations, but our hard object may have small negative
entries, and idempotency is nonlinear.  The plausible doubly stochastic
stability statement is:

```text
P1=1,        1^T P=1^T,        P^2=P,
neg(row)<=delta
  => P is O(sqrt(delta))-close to a block-average projection.
```

This should be easier than the general row-stochastic case because the
column-sum constraint removes the transient-row geometry.  It is not yet
proved here.

## Reversible And Stoquastic Forms

The symmetric/reversible subcase can be phrased in stoquastic language.

If `Q` is symmetric, row-stochastic, and nonnegative, then

```text
H=I-Q
```

is real symmetric, satisfies `H1=0`, and has nonpositive off-diagonal entries.
That is the usual stoquastic sign pattern.

Moreover,

```text
H^2-H = Q^2-Q.
```

Thus almost idempotence of `Q` is exactly almost idempotence of the
stoquastic Hamiltonian-like matrix `H`.

A stoquastic projection-stability conjecture is therefore:

```text
H=H^T,        H1=0,
offdiag(H)<=small positive error,
||H^2-H|| <= eta
  => H is O(sqrt(eta))-close to an exact stoquastic projection H0
     with H0 1=0.
```

Equivalently, in the positive symmetric case, `Q=I-H` should be close to a
symmetric stochastic idempotent, hence to a block-average projection.

This is a genuine special case.  It does not cover arbitrary stochastic
matrices, because the full problem is directed/non-self-adjoint and is
naturally controlled in the `ell_infty` norm rather than the Hilbert norm.
But it is an attractive first test case: symmetry should suppress the
directed transient pathologies that make the general theorem harder.

## Relation To The Global Exposed-Hull Lemma

The current geometric route to the stochastic conjecture is the global
exposed-hull lemma in
`agent-B/notes/simultaneous-skeleton-reduction.md`.

For an exact signed idempotent row polytope `K=conv{p_i}`, define

```text
W_{rho,kappa}
 = {row vertices v : e_v(rho)>=kappa}.
```

The target is:

```text
rho=O(sqrt(delta)),        kappa>=c sqrt(delta)
  => every row is O(sqrt(delta))-close to conv W_{rho,kappa}.
```

This avoids the false local proof architecture where one deletes
individually redundant vertices one at a time.  The local deletion statement
can accumulate error and is false as a dimension-free convex-geometric
implication.

If the global exposed-hull lemma is proved, then
`agent-B/theory/classical-cluster-factorization-theorem.md` gives exact
commutative positive/JB factorization.

## Evidence So Far

### Proved Special Cases

Several cases of the stochastic/signed-idempotent conjecture are already
proved in Agent B notes.

- Rank-one signed perturbations `P=I-u v^T` satisfy the sharp
  `O(sqrt(delta))` theorem.  This includes Hume's `3 x 3` family; see
  `agent-B/notes/rank-one-classical-stability.md`.
- Line-segment row polytopes are stable at `O(sqrt(delta))`; see
  `agent-B/notes/line-segment-classical-stability.md`.
- Simplex row polytopes are stable at `O(sqrt(delta))` with constants
  independent of the number of simplex vertices; see
  `agent-B/notes/simplex-classical-stability.md`.
- Well-exposed separated vertices cannot form affine circuits; see
  `agent-B/notes/exposed-circuit-cancellation.md` and
  `agent-B/notes/well-exposed-classical-stability.md`.
- Cluster-representative geometries give a stochastic idempotent at
  `O(sqrt(delta))`; see
  `agent-B/notes/cluster-representative-classical-stability.md`.
- Under the corresponding cluster or global exposed-hull hypothesis,
  `agent-B/theory/classical-cluster-factorization-theorem.md` gives exact
  commutative positive/JB factorization.

These are not just numerical evidence.  They are theorem-level partial
results.

### Sharpness Evidence

Hume's explicit `3 x 3` family shows that linear stability is false.

For that family,

```text
delta=s^2,
dist(P_s, stochastic idempotents)
  = 2s - 2s^2 + 2s^3
  = 2 sqrt(delta) + O(delta).
```

The experiment file
`agent-B/experiments/classical-projection-stability/explicit_sqrt_family.json`
confirms numerically, for example:

```text
s=0.01   delta=0.0001    distance=0.019802
distance/sqrt(delta)=1.9802.
```

So the square-root scale is not an artifact of the proof strategy.

### Random Small-Dimensional Classical Searches

The search files under
`agent-B/experiments/classical-projection-stability/` sampled small
`3 x 3` rank-two signed idempotents and compared them against the classified
stochastic idempotents in dimension `3`.

The searches did not find a counterexample to square-root stability.  The
largest ratios found were compatible with the Hume-type boundary behavior,
not with any worse power or dimension blow-up.

These searches are limited: they are small-dimensional and classification
based.  They are evidence against easy counterexamples, not a substitute for
the global theorem.

### Non-Simplex Stress Tests

Several sidecar probes looked for non-simplex row-polytope counterexamples.
No credible counterexample was found.

- Tensor products of Hume's family initially look dangerous, because naive
  product rounding gives an error growing like `sqrt(k)`.  Wegener observed
  this is not a lower bound: stochastic idempotent classification allows
  transient-class roundings that may stay at `O(sqrt(delta))`.
- Fixed-complexity parallelogram and product-of-simplex vertex geometries are
  ruled out under bounded affine-coordinate witnesses; see
  `agent-B/notes/parallelogram-classical-stability.md`.
- The remaining obstruction is angle/facet-count loss, not an explicit
  counterexample; see
  `agent-B/notes/subagent-non-simplex-classical-probe-v0.1.md`.

### Algebraic Bridge Numerics

The null-ideal/Jordan-bridge numerics are separate from projection stability,
but they support the positive-map bridge estimates.

`agent-B/experiments/null-ideal-probe/REPORT.md` found no low-dimensional
counterexample to the key null-ideal smallness estimate.  In the clearest
classical `R^3` family,

```text
||P(h_{r,s}^2)|| / eta -> 32/27,
```

so the defect is linear in `eta`, not growing faster.  The same report found
qubit Bloch-form defects at floating-point noise level because the relevant
holes vanish in that setting.

### What Is Missing Numerically

There is not yet a dedicated numerical search for the doubly stochastic or
stoquastic signed-idempotent conjectures.

Useful next experiments would be:

1. sample symmetric idempotents `P=P^T`, `P1=1`, with small negative
   off-diagonal/row mass, and compare to the nearest block-average projection;
2. sample signed doubly stochastic idempotents and test distance to
   nonnegative doubly stochastic idempotents;
3. test whether Hume-type boundary escapes can be made doubly stochastic or
   symmetric without increasing the negative mass from `s^2` to order `s`.

At present, the stoquastic special case is supported by structural intuition
and by the broader stochastic evidence, but not by a separate numerical
campaign.

