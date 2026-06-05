# Subagent Matrix Representation Audit v0.1

Date: 2026-06-05.

Source: sidecar agent Nietzsche, read-only audit.

This memo records an independent representation-theoretic audit of the
exact-adjoint high-rank matrix benchmark for

```text
J=H_n(F),        F in {R,C,H}.
```

The task was to look for plausible dimension-growth components in the
normalized adjoint primitive problem

```text
h(1)=0,        f=d^1h,
```

with order-unit/operator cochain norms.

## Representation Target

Modulo derivations, normalized adjoint 1-cochains are

```text
J_0^* tensor R1  plus  (J_0^* tensor J_0)/Der(J),
J_0={tr x=0}.
```

For `F=R`, with `G=O(n)` and

```text
J_0 = S^2_0 R^n = W,
```

the expected decomposition is

```text
C^1_0 / Der = W_c plus R Id plus W_m plus S^4_0 R^n plus V_(3,1).
```

Here `W_c` is central-valued, `W_m` is the traceless multiplication copy, and
the removed derivation kernel is the `Lambda^2 R^n` summand inside
`Lambda^2 W`.

For `F=C`, with `G=PU(n)` and `J_0=su(n)` as a real adjoint module, the
corresponding schematic decomposition is

```text
C^1_0 / Der = J_0,c plus R Id plus J_0,s plus U_s plus U_a.
```

For `SU(3)`, this matches the familiar decomposition

```text
8 tensor 8 = 1 plus 8_s plus 27 plus 8_a plus 10 plus conjugate(10).
```

This decomposition is diagnostic only; Hilbert decompositions do not by
themselves give order-norm estimates.

## Components Already Controlled

The existing Agent B notes give dimension-free control for:

- the unit value `h(1)`, by subtracting the multiplication primitive
  `L_{f(1,1)}`;
- central-valued normalized maps `h(x)=phi(x)1`;
- trace-zero rank-one maps `h(x)=phi(x)c`, `phi(1)=0`;
- fixed diagonal-frame restrictions, by the Rademacher/Schur formula;
- the scalar `Id_{J_0}` component, at least as a non-small-singular-value
  candidate, by evaluating on traceless symmetries.

The side audit also found no apparent Hilbert-norm small singular value in the
dangerous equivalent-copy pair consisting of the central-valued and
multiplication copies. This is evidence only, not an order-norm theorem.

## Blocked Routes

Two routes are rigorously blocked and should not be recycled as proofs:

1. Averaging fixed-frame splittings loses rank. Averaged diagonal pinching
   acts on `J_0` by

```text
lambda=(n-1)/(dim_R H_n(F)-1),
```

which is `2/(n+2)`, `1/(n+1)`, and `1/(2n+1)` for `F=R,C,H`.

2. Summing rank-one estimates gives only nuclear/projective control. Since

```text
nu(Id_{J_0}) >= dim J_0
```

while `||Id_{J_0}||=1`, this cannot yield a dimension-free operator-norm
splitting.

## Remaining Irreducible Targets

No order-norm counterexample was found.

The most plausible remaining danger components are the large irreducibles:

```text
S^4_0 R^n and V_(3,1)        for H_n(R),
U_s and U_a                  for H_n(C).
```

A representation-theoretic proof must supply order-norm lower bounds for
`d^1` on these components, or dimension-free Banach-norm control for the
corresponding equivariant projections. Hilbert-Schmidt estimates and Schur's
lemma are insufficient.

## Verdict

A dimension-free exact-adjoint matrix splitting remains plausible. The known
rank losses come from reconstruction/proof methods, not from proved lower
bounds for `d^1`. The next decisive audit target is the large non-scalar
irreducible part, especially the skew non-derivation component.
