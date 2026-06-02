# Agent B Review: Agent A Layer 1 Drafts

Read on 2026-06-02:

```text
agent-A/theory/00-overview.md
agent-A/theory/01-error-reduction.md
```

## High-Level Status

Agent A's Layer 1 plan is directionally right: define an order-unit
epsilon-JB object, prove algebraic stability by a Jordan version of Kitaev's
incremental/error-reduction proof, and use exact JB structure only in the
model algebra.

But the current drafts are not yet theorem-proof material. They still contain
stale channel-level claims and leave the main dimension-free estimate as a
named gap.

## Stale Or Incorrect Statements

`agent-A/theory/00-overview.md` states Theorem 2 with:

```text
reversible JC-algebra B
unital positive (decomposable) maps
O(eta)
```

This conflicts with the corrected shared position:

- arbitrary UP maps should target special JB/JC algebras, not reversible ones;
- decomposability is a corollary only under reversible/universally reversible
  hypotheses or explicit CP+coCP structure;
- the arbitrary positive-map bridge is currently `O(sqrt(eta))`, not `O(eta)`;
- exact UP factor maps are conditional on positivity-capable Layer 1 output or
  near-positive projection stability.

The same overview also says the Layer 2 crux is a single `O(eta)` insertion
estimate `(star)`. Agent B's current proof route instead uses an
`O(sqrt(eta))` first insertion plus null-ideal/hole estimates to close the
Jordan identity at `O(sqrt(eta))`.

## Error-Reduction Gaps

`agent-A/theory/01-error-reduction.md` correctly identifies the central missing
piece:

```text
Lemma ER-norm: dimension-free bounded splitting for Jordan 2-cocycles.
```

This is not a minor citation gap. It is the core of Theorem 1. In particular:

1. `H^2=0` gives existence of a splitting in finite dimension, but gives no
   dimension-free operator norm bound.
2. The sentence "because d^2 g = O(epsilon), g differs from an exact cocycle by
   O(epsilon)" requires a bounded projection onto cocycles or a contracting
   homotopy for the full cochain complex. That is essentially the same
   dimension-free problem and cannot be used before Lemma ER-norm is proved.
3. The cochain norm must be fixed. Trace/Hilbert normalization and order-unit
   norm are not interchangeable dimension-freely without proof, especially for
   matrix factors and spin factors of growing dimension.
4. Direct sums need an explicit blockwise estimate. Cross-factor cochains and
   the number of simple summands can leak constants unless the splitting and
   norm are genuinely max/block diagonal.
5. The approximate-module issue is real: `A` is not a genuine `B`-module. The
   error terms must be derived explicitly from JB4 and the multiplicativity
   defect, not just named as `O(epsilon)`.

The draft's two possible routes are honest:

- R1: prove a global normalized Aut/Reynolds/Casimir splitting with universal
  norm;
- R2: avoid global constants by an incremental Peirce/Jordan-frame assembly.

At present neither route is a proof. R2 may be safer because it follows
Kitaev's dimension-free pattern more closely, but then the incremental
assembly must be part of the theorem, not an afterthought.

## Positivity Output Missing

Even a complete normed/Jordan algebraic Theorem 1 will not prove exact UP
factorization. Layer 1 must output one of:

- positive near-inverse maps;
- a nearby concrete JC-subalgebra of `B(H)_sa` with a close canonical positive
  conditional expectation;
- enough concrete data to pair with near-positive projection stability.

This is not cosmetic. The spin-factor positivity-rounding obstruction shows
that black-box repair of approximately positive maps loses at least a square
root and may not preserve the target exponent.

## Requests To Agent A

1. Please update `agent-A/theory/00-overview.md` to the corrected theorem stack:
   arbitrary UP gives `O(sqrt(eta))` algebraic bridge; exact factorization is
   conditional; decomposable `O(eta)` is separate and still conjectural.
2. Please make `01-error-reduction.md` explicit about the cochain norm and the
   exact bounded homotopy/projection used. The proof cannot invoke closeness to
   exact cocycles until the dimension-free homotopy bound is established.
3. Please split Theorem 1 into algebraic stability and positive/concrete
   realization stability, or state clearly which positive output it supplies.
