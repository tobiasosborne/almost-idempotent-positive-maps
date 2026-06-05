# Bounded-Rank Adjoint Reduction

Date: 2026-06-05.

This note was an intermediate consolidation of the exact adjoint Layer-1
benchmarks. It showed that, after the spin and direct-sum results, the only
asymptotic exact-adjoint simple-factor problem left at that stage was the
high-rank matrix sequence

```text
H_n(R), H_n(C), H_n(H),        n -> infinity.
```

The high-rank matrix proof is now supplied by
`agent-B/notes/matrix-factor-exact-adjoint-splitting-theorem.md`. The constants
below remain useful for the fixed-rank and Albert pieces.

## Setup

For a unital finite-dimensional JB algebra `B`, let `K_adj(B)` be the best
constant of an exact adjoint right inverse:

```text
S_B : im(d^1_B) -> C^1(B,B),
d^1_B S_B f=f,
||S_B f|| <= K_adj(B)||f||,
```

where cochains use the order-unit injective norms. If no such right inverse is
chosen, set `K_adj(B)=infinity`.

Because `B` is finite-dimensional and `im(d^1_B)` is a finite-dimensional
subspace, `K_adj(B)<infinity` for every fixed `B` after choosing any linear
complement to `ker d^1_B`.

## Theorem

Fix a rank cutoff `R0`. Consider finite direct sums whose simple summands are
drawn from:

1. arbitrary spin factors;
2. matrix factors `H_n(R)`, `H_n(C)`, `H_n(H)` with `n<=R0`;
3. the Albert factor `H_3(O)`.

Then there is a finite constant `K(R0)` such that every such direct sum has an
exact adjoint right inverse with norm at most `K(R0)`, independent of:

- the number of direct summands;
- the dimensions of the spin factors;
- multiplicities of isomorphic summands.

## Proof

Spin factors have the explicit dimension-free adjoint constant

```text
K_spin <= 4 sqrt(2)
```

from `agent-B/notes/adjoint-spin-splitting-theorem.md`.

For fixed `R0`, there are only finitely many matrix factor types

```text
H_n(R), H_n(C), H_n(H),        1<=n<=R0
```

up to the usual low-rank coincidences, and the Albert factor is a single fixed
finite-dimensional algebra. Each fixed factor has a finite exact adjoint
constant by finite-dimensional closed-range linear algebra. Define

```text
K_simple(R0)
 = max(
     4 sqrt(2),
     K_adj(H_n(F)) for F in {R,C,H}, n<=R0,
     K_adj(H_3(O))
   ).
```

This maximum is finite.

Now apply `agent-B/notes/adjoint-direct-sum-reduction.md`. A direct sum of
factors with constants at most `K_simple(R0)` has exact adjoint splitting
constant at most

```text
K_simple(R0)+1.
```

Thus one may take

```text
K(R0)=K_simple(R0)+1.
```

The direct-sum estimate is a max-norm estimate and therefore has no dependence
on the number of summands.

## Consequences

1. The exact adjoint problem has no hidden dependence on the number of simple
   summands.
2. Spin dimensions are not a source of growth.
3. Fixed-rank matrix factors and the exceptional Albert factor are not
   asymptotic obstacles; they contribute only fixed constants.
4. At this stage, the only remaining exact adjoint asymptotic benchmark was:

```text
prove sup_n K_adj(H_n(F)) < infinity
for F=R,C,H,
```

preferably in the normalized/unit-vanishing form from
`agent-B/notes/unit-normalized-adjoint-reduction.md`.

This benchmark is now closed by
`agent-B/notes/matrix-factor-exact-adjoint-splitting-theorem.md`. The full
Layer-1 theorem still requires arbitrary relevant modules, approximate
cocycle control, and approximate-module error estimates.
