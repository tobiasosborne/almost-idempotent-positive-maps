# Spin Direct-Sum Adjoint Corollary

Date: 2026-06-05.

This note combines two proved Agent B components:

- `agent-B/notes/adjoint-spin-splitting-theorem.md`;
- `agent-B/notes/adjoint-direct-sum-reduction.md`.

It records a clean theorem-level exact adjoint result for an infinite class of
JB algebras: arbitrary finite direct sums of spin factors, with no dependence
on spin dimensions or on the number of summands.

## Setup

Let

```text
B = direct_sum_{r=1}^m V_{H_r}
```

where each

```text
V_{H_r}=R1_r \oplus H_r
```

is a finite-dimensional spin factor, and give `B` the direct-sum order-unit
norm

```text
||x|| = max_r ||x_r||_{ou}.
```

Use the adjoint module and the Jordan coboundary

```text
(d^1h)(a,b)=a o h(b)+h(a) o b-h(a o b).
```

## Corollary

There is a linear right inverse

```text
S_B : im(d^1) -> C^1(B,B)
```

for exact adjoint coboundaries such that

```text
d^1 S_B f=f,
||S_B f|| <= (4 sqrt(2)+1)||f||.
```

The constant is independent of:

- the number of spin summands `m`;
- the dimensions `dim H_r`;
- the multiplicities of isomorphic spin summands.

## Proof

For a single spin factor, `adjoint-spin-splitting-theorem.md` gives an exact
adjoint splitting with Euclidean-injective norm at most `2`. The spin
rank-two norm comparison gives the order-unit estimate

```text
K_spin <= 4 sqrt(2).
```

Apply `adjoint-direct-sum-reduction.md` to the direct sum. If all factor
constants satisfy `K_r<=4 sqrt(2)`, the direct sum has constant at most

```text
max_r K_r + 1 <= 4 sqrt(2)+1.
```

The direct-sum construction recovers off-block primitive components by

```text
P_r f(e_r,x_{\ne r}),
```

so no summation over `r` appears in the norm estimate.

This proves the corollary.

## Consequences

1. The exact adjoint Layer-1 benchmark is fully controlled for all finite
   direct sums of spin factors.
2. The remaining exact adjoint simple-factor gap is concentrated in the
   high-rank matrix families `H_n(R)`, `H_n(C)`, and `H_n(H)`, plus the fixed
   Albert factor if one wants a complete abstract JB statement.
3. This corollary remains an exact adjoint-module statement. It does not handle
   arbitrary modules, approximate cocycles, or approximate-module errors.
