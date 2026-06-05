# Cochain Norm Conversion Caveat

Date: 2026-06-04.

This note refines the criticism of the Frobenius-to-order-norm route in
`agent-B/notes/spin-splitting-audit-2026-06-05.md`.

The element norm comparison

```text
||x||_op <= ||x||_2 <= sqrt(rank) ||x||_op
```

does not by itself describe the cochain problem. At cochain level there are
input-slot conversions, output conversions, and tensor/injective norm
conversions. The following elementary family shows why an `H_n` proof should
not ask for Frobenius-bounded primitives when the theorem only needs
order-bounded primitives.

## Setup

Let

```text
J=H_n(R)
```

with Jordan product `a o b=(ab+ba)/2`, operator norm `||.||_op`, and Frobenius
norm `||.||_2`. Let `e=e_11` and `1=I_n`.

For 1-cochains, write

```text
||h||_op = sup_{||x||_op<=1} ||h(x)||_op,
||h||_F  = sup_{||x||_2<=1}  ||h(x)||_2.
```

For 2-cochains, use the analogous bilinear norms.

Define

```text
h_n(x)=x_11 1.
```

## Order Norm Is Small, Frobenius Norm Is Large

For `||x||_op<=1`, `|x_11|<=1`, so

```text
||h_n||_op = 1.
```

For `||x||_2<=1`, `|x_11|<=1`, and equality is attained at `x=e`. Hence

```text
||h_n||_F = ||1||_2 = sqrt(n).
```

Thus this is a perfectly order-bounded 1-cochain whose Euclidean-injective norm
has the maximal rank growth.

## Its Coboundary Is Order-Bounded

Let

```text
f_n=d^1 h_n.
```

For `a,b in H_n(R)`,

```text
f_n(a,b)=b_11 a + a_11 b - (a o b)_11 1.
```

Since

```text
(a o b)_11 = <a e_1, b e_1>,
```

we get, for `||a||_op,||b||_op<=1`,

```text
|a_11|<=1,        |b_11|<=1,        |(a o b)_11|<=1.
```

Therefore

```text
||f_n||_op <= 3.
```

So `f_n` is an exact adjoint coboundary with dimension-free order norm, and it
has the order-bounded primitive `h_n`.

## But Every Primitive Has Large Frobenius Norm

If `k` is another primitive with `d^1 k=f_n`, then `k-h_n` is a derivation.
For `H_n(R)`, derivations are commutators

```text
D_K(x)=Kx-xK,        K^T=-K.
```

In particular, `D_K(e)` has zero diagonal. Hence

```text
k(e)=h_n(e)+D_K(e)=1+D_K(e)
```

has diagonal entries all equal to `1`, and therefore

```text
||k(e)||_2 >= ||1||_2 = sqrt(n).
```

Since `||e||_2=1`,

```text
||k||_F >= sqrt(n)
```

for every primitive `k` of `f_n`.

This is not a lower bound for the desired order-norm splitting: `h_n` itself
has `||h_n||_op=1`. It is only a lower bound for the wrong target, namely a
Frobenius-bounded primitive measured against an order-norm 2-cochain.

It also does not contradict Frobenius-to-Frobenius numerical canaries. Indeed,

```text
f_n(e,e)=2e-1,
```

so `||f_n||_F >= ||2e-1||_2 = sqrt(n)`. In Frobenius cochain norm, both the
input and the output are large.

## Consequences

1. A global Hilbert/Frobenius splitting cannot simply be converted into the
   order-unit theorem by proving that its primitive has small Frobenius norm
   for every order-bounded exact coboundary. That assertion is false.
2. High Frobenius rank in a primitive value can be harmless for the order norm:
   `h_n(e)=1` is maximally high-rank but has operator norm `1`.
3. Agent A's proposed low-effective-rank "rank-balance" condition points in
   the wrong direction, and the opposite high-spread condition is also not a
   standalone target. The correct target is a direct order-norm homotopy, or an
   incremental Peirce/frame construction whose estimates never require a
   global Frobenius primitive bound.

This example should be used as a guardrail: any proposed matrix-family Layer-1
proof that passes through Frobenius primitives must specify exactly how it
avoids this family.
