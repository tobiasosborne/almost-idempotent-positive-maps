# Finite-Dimensional Adjoint JB Splitting Corollary

Date: 2026-06-05.

This note records the exact-adjoint benchmark now obtained from the spin,
matrix, bounded-rank, and direct-sum notes.

It is not the full Layer 1 stability theorem. It concerns only the adjoint
module, only exact coboundaries, and only exact finite-dimensional JB
algebras.

## Corollary

There is a universal constant `C` such that for every finite-dimensional JB
algebra `B` and every exact adjoint coboundary

```text
f=d^1h in C^2(B,B),
```

there is a derivation `delta in Der(B)` with

```text
||h-delta|| <= C||f||_inj.
```

Equivalently, `d^1` induces an inverse

```text
C^1(B,B)/Der(B) -> im(d^1)
```

with norm at most `C`, independently of the dimension and of the number of
simple summands.

## Proof

By the finite-dimensional JB classification, `B` is a finite direct sum of
simple factors:

```text
spin factors,        H_n(R), H_n(C), H_n(H),        H_3(O).
```

The factors have uniform exact-adjoint constants:

- spin factors:
  `agent-B/notes/adjoint-spin-splitting-theorem.md`;
- matrix factors, all ranks and `F=R,C,H`:
  `agent-B/notes/matrix-factor-exact-adjoint-splitting-theorem.md`;
- the Albert factor `H_3(O)`:
  fixed finite-dimensional closed-range linear algebra, already allowed in
  `agent-B/notes/bounded-rank-adjoint-reduction.md`.

Let `K` be the maximum of these universal/fixed constants. The adjoint
direct-sum reduction
`agent-B/notes/adjoint-direct-sum-reduction.md` gives a direct-sum constant
at most

```text
K+1,
```

independent of the number of summands. This proves the corollary.

## Remaining Layer 1 Gap

The corollary is strong evidence for the cohomological engine, but it is not
the required error-reduction theorem. Layer 1 still needs:

1. relevant non-adjoint Jordan modules produced by perturbing the product;
2. approximate cocycles, not only exact coboundaries;
3. approximate module-action errors, because the codomain is an
   `epsilon`-JB algebra before correction;
4. a dimension-free projection or homotopy that is stable under those
   approximate errors;
5. for the positive-map factorization route, a positivity-capable or concrete
   output, or a separate near-positive projection stability theorem.
