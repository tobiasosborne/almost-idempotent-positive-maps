# Trace-Zero Rank-One Matrix Primitive Estimate

Date: 2026-06-05.

This note controls another explicit normalized component of the high-rank
matrix adjoint problem. It extends the central-valued estimate from
`h(x)=phi(x)1` to normalized rank-one primitives

```text
h(x)=phi(x)c,        phi(1)=0,
```

with arbitrary output `c`.

## Setup

Let

```text
J=H_n(F),        F in {R,C,H},
```

with Jordan product `a o b=(ab+ba)/2` and operator/order-unit norm. Let
`phi:J->R` be a real linear functional satisfying

```text
phi(1)=0,
```

and let `c in J`. Define

```text
h_{phi,c}(x)=phi(x)c.
```

Use injective order-unit cochain norms. Then

```text
||h_{phi,c}|| = ||phi||_* ||c||.
```

## Theorem

For every `phi(1)=0` and `c in J`,

```text
(1/2)||h_{phi,c}|| <= ||d^1h_{phi,c}|| <= 3||h_{phi,c}||.
```

Equivalently, the coboundary has inverse norm at most `2` on this trace-zero
rank-one primitive subspace. The constants are independent of `n` and of
`F in {R,C,H}`.

## Proof

The upper bound is immediate from contractivity of the Jordan product.

For the lower bound, scale so that

```text
||phi||_*=1,        ||c||=1.
```

Represent `phi` by a self-adjoint trace-class density `rho`:

```text
phi(x)=Re Tr(rho x),        Tr rho=0,        Tr |rho|=1.
```

Let

```text
u=sign(rho),
```

choosing arbitrary signs on the kernel. Then

```text
u=u^*,        u^2=1,        ||u||=1,        phi(u)=1.
```

Let `f=d^1h_{phi,c}`. Since `phi(1)=0`,

```text
f(u,u)=2 u o c.
```

If

```text
||u o c|| >= 1/4,
```

then

```text
||f|| >= ||f(u,u)|| >= 1/2.
```

Otherwise `||u o c||<1/4`. Evaluate at `(u,c)`:

```text
f(u,c)=phi(c)(u o c) + c o c - phi(u o c)c.
```

The two error terms satisfy

```text
||phi(c)(u o c)|| <= 1/4,
||phi(u o c)c|| <= 1/4,
```

because `||phi||_*=||c||=1`. The JB norm identity gives

```text
||c o c||=||c||^2=1.
```

Hence

```text
||f(u,c)|| >= 1-1/4-1/4 = 1/2.
```

Again `||u||=||c||=1`, so `||f||>=1/2`.

Rescaling gives

```text
||d^1h_{phi,c}|| >= (1/2)||phi||_*||c||
 = (1/2)||h_{phi,c}||.
```

This proves the theorem.

## Consequences

1. Normalized rank-one primitive maps are not a high-rank obstruction, even
   when their output `c` is noncentral.
2. The estimate uses both evaluations `(u,u)` and `(u,c)`: if `u o c` is large,
   the first recovers the primitive; if `u o c` is small, then `c^2` appears
   visibly in the second.
3. This is an exact adjoint subspace estimate. It does not by itself control
   arbitrary sums of many rank-one maps, because the projective/nuclear norm of
   a general endomorphism can grow with dimension. The remaining high-rank
   matrix problem is therefore a collective operator-norm question, not a
   rank-one primitive question.

This estimate is another guardrail for proposed matrix proofs: any obstruction
must involve coherent sums or genuinely higher-rank endomorphism geometry, not
a single normalized rank-one primitive.
