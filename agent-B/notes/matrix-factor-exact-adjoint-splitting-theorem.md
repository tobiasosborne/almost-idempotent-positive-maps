# Matrix Factor Exact Adjoint Splitting Theorem

Date: 2026-06-05.

This note assembles the fixed-frame matrix estimates into the exact-adjoint
simple-factor benchmark for

```text
J=H_n(F),        F in {R,C,H}.
```

It is still only an exact adjoint-module theorem. It does not handle arbitrary
Jordan modules, approximate cocycles, approximate module errors, or the
positivity/concrete output needed for the positive-map factorization theorem.

## Theorem

There is a universal constant `C` such that for every `n` and
`F in {R,C,H}`, if

```text
f=d^1h
```

is an exact adjoint coboundary on `J=H_n(F)`, then there is a derivation
`delta` of `J` such that

```text
||h-delta|| <= C ||f||_inj.
```

Equivalently, the induced inverse

```text
C^1(J,J)/Der(J) -> im(d^1)
```

has norm bounded by `C`, uniformly in `n` and `F`.

The bounded-rank cases, including `n<=2`, are already covered by
`agent-B/notes/bounded-rank-adjoint-reduction.md`; the proof below is the
high-rank fixed-frame argument.

## Proof Structure

Start with an arbitrary primitive `h`.

1. **Unit normalization.** Use
   `agent-B/notes/unit-normalized-adjoint-reduction.md` to remove the
   multiplication primitive. This reduces to a primitive with `h(1)=0`, at
   the cost of replacing `||f||` by a universal multiple of `||f||`.

2. **Diagonal gauge.** Fix the standard Jordan frame. The diagonal-frame
   splitting in `agent-B/notes/diagonal-frame-matrix-module-splitting.md`
   gives a bounded primitive on `D x D`. The difference between the original
   diagonal restriction and this bounded one is the restriction of a
   frame-stabilizer derivation. Subtract that derivation. We may assume

   ```text
   ||h|_D|| <= C||f||.
   ```

3. **Off-sector leakage.** Let `E` be the off-diagonal Peirce subspace and
   `H=h|_E`. The global leakage theorem
   `agent-B/notes/off-sector-leakage-globalization-theorem.md` gives

   ```text
   ||(I-P_sec)H|| <= C||f||.
   ```

   This is the step that replaces the earlier single-source leakage estimate.

4. **Sector-preserving residual.** Extend `P_sec H` to a full 1-cochain by
   setting it equal to zero on `D`. Similarly extend the leakage part
   `H_leak=(I-P_sec)H` by zero on `D`. Then

   ```text
   h = h|_D + H_leak + P_sec H
   ```

   as 1-cochains, with `h|_D` also extended by zero on `E`. Hence on all
   sector tests,

   ```text
   d^1(P_sec H)=f-d^1(h|_D)-d^1(H_leak).
   ```

   The diagonal and leakage pieces have bounded norm, and `||d^1T||<=3||T||`
   for bounded adjoint primitives. Therefore the coboundary of `P_sec H` is
   bounded by `C||f||`. The sector-preserving estimates control it modulo the
   frame-stabilizer derivation kernel:

   - `F=R`: `agent-B/notes/real-symmetric-matching-reconstruction-theorem.md`;
   - scalar Hermitian part:
     `agent-B/notes/hermitian-scalar-sector-reconstruction-corollary.md`;
   - complex anti-linear part:
     `agent-B/notes/complex-antilinear-peirce-residual-theorem.md`;
   - quaternionic internal part:
     `agent-B/notes/quaternionic-internal-peirce-residual-theorem.md`.

   Hence there is a frame-stabilizer derivation `delta_sec` such that

   ```text
   ||P_sec H-delta_sec|_E|| <= C||f||.
   ```

Combining the bounded diagonal part, bounded leakage part, and bounded
sector-preserving representative gives bounded control on all of `J`. Indeed,
the diagonal pinching `E_D:J->D` is contractive and `I-E_D` has norm at most
`2`, so for any `x in J`,

```text
||(h-delta)(x)||
 <= C||f|| (||E_Dx||+||(I-E_D)x||)
 <= C||f||||x||.
```

Thus

```text
||h-delta|| <= C||f||,
```

where `delta` is the sum of the derivations subtracted in the diagonal and
sector-preserving gauges. Since derivations are exactly the kernel directions
for the adjoint coboundary, this proves the theorem.

## Consequence

Together with the spin and bounded-rank/direct-sum notes, this closes the
exact-adjoint simple-factor and finite direct-sum benchmark in order norm.

The full Layer 1 theorem remains open because it still requires dimension-free
control for the relevant non-adjoint modules, approximate cocycles,
approximate module errors, and a positivity-capable or concrete output.
