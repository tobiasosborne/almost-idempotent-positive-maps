# Peirce Sector Norm Accumulation

Date: 2026-06-04.

This note records the main caveat left after
`agent-B/notes/commutative-scalar-module-splitting.md`.

For `R^m`-modules, the algebraic decomposition into coordinate and pair
half-sum sectors is harmless in the max sector norm. But in the adjoint module
of a high-rank matrix Jordan algebra, the ambient operator norm is not the max
over Peirce sectors. Many uniformly bounded Peirce components can add to an
element with norm growing like the rank.

This is a concrete reason why the commutative scalar-sector splitting does not
settle the high-rank `H_n(F)` Layer-1 problem.

Follow-up: `agent-B/notes/diagonal-frame-matrix-module-splitting.md` shows that
this accumulation is not a lower bound for the exact coboundary inverse on a
fixed diagonal frame. A Rademacher/Schur-multiplier formula gives a
dimension-free right inverse for the restriction of the adjoint `H_n(F)` module
to the diagonal `R^n` subalgebra. Thus this note rules out the naive route
"split in max sector norm and include"; it does not rule out a direct
order-unit splitting.

## Example: Diagonal Frame In `H_n(R)`

Let

```text
J = H_n(R)
```

with Jordan product

```text
a o b = (ab+ba)/2
```

and order-unit norm equal to the usual operator norm. Let

```text
B = R^n
```

be the diagonal Jordan subalgebra with frame idempotents `e_i=E_{ii}`.

For `i<j`, put

```text
F_{ij}=E_{ij}+E_{ji}.
```

Then

```text
diag(x_1,...,x_n) o F_{ij}
  = ((x_i+x_j)/2) F_{ij}.
```

Thus each off-diagonal Peirce line `R F_{ij}` is exactly one of the half-sum
scalar modules controlled in
`commutative-scalar-module-splitting.md`. Also

```text
||F_{ij}||_op = 1.
```

Now sum all off-diagonal sectors with coefficient `1`:

```text
A_n = sum_{i<j} F_{ij}.
```

This is the matrix with zero diagonal and every off-diagonal entry equal to
`1`, i.e.

```text
A_n = 11^T - I.
```

Its spectrum is

```text
n-1        on span{1},
-1         with multiplicity n-1.
```

Hence

```text
||A_n||_op = n-1.
```

But every Peirce-sector coefficient has norm `1`. Therefore the inclusion

```text
direct_sum_{i<j}^{l_infty} R F_{ij} -> H_n(R)
```

has norm at least `n-1`.

## Consequence

The exact commutative module decomposition gives a norm-one splitting only in
the max sector norm. To use it inside the ambient matrix order-unit norm one
cannot merely include the sectorwise result. One needs additional structure
using the fact that the cochain is an exact coboundary. The Rademacher formula
in `diagonal-frame-matrix-module-splitting.md` supplies that structure for a
fixed diagonal frame.

Equivalently, any matrix-family Layer-1 proof must supply one of the following:

1. a direct order-unit estimate that does not pass through the max sector norm;
2. a cancellation/balance theorem for the cochains in `im(d^1)`;
3. an incremental Peirce/frame construction that never sums too many
   uncontrolled sectors at once.

This is the same high-rank warning seen from a different angle. The scalar
Peirce-`1/2` modules are individually harmless; coherent accumulation of many
such sectors invalidates the naive sector-inclusion proof. The remaining
obstruction, after the diagonal-frame splitting theorem, is the full
noncommutative matrix cochain problem.
