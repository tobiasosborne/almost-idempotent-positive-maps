# Adjoint Direct-Sum Reduction

Date: 2026-06-05.

This note proves the summand-count independence claim in the adjoint
block-respecting case. It does not contradict the arbitrary-module caveat in
`agent-B/notes/response-to-agent-a-v0.12-layer1-caveat.md`: mixed Peirce
modules exist for arbitrary modules. The point here is narrower and positive:
for the adjoint module of a direct sum, off-block primitive components are
recovered directly from the coboundary by evaluating at central units.

## Setup

Let

```text
B = direct_sum_{r=1}^m B_r
```

be a finite direct sum of unital JB algebras with coordinatewise product and
order-unit norm

```text
||x|| = max_r ||x_r||.
```

Let `e_r` be the unit of the ideal `B_r`, embedded in `B`, and let
`P_r:B->B_r` be the coordinate projection. We use the adjoint module and

```text
(d^1h)(a,b)=a o h(b)+h(a) o b-h(a o b).
```

Assume that each factor has an exact adjoint right inverse

```text
S_r : im(d^1_{B_r}) -> C^1(B_r,B_r)
```

with

```text
d^1_{B_r}S_r g=g,        ||S_r g|| <= K_r||g||.
```

Let

```text
K=max_r K_r.
```

## Theorem

The direct sum `B` has an exact adjoint right inverse with constant at most

```text
K+1.
```

In particular, the constant is independent of the number of direct summands.

## Construction

Let `f=d^1h` be an exact adjoint 2-coboundary on `B`. For each `r`, define the
same-factor component

```text
f^r(a,b)=P_r f(a,b),        a,b in B_r.
```

This is an exact adjoint coboundary on `B_r`, namely the coboundary of
`P_r h|_{B_r}`.

For `x=(x_1,...,x_m) in B`, write

```text
x_{\ne r}=x-x_r.
```

Define a 1-cochain `Sf:B->B` coordinatewise by

```text
(Sf)_r(x)
  = (S_r f^r)(x_r) + P_r f(e_r, x_{\ne r}).
```

This is linear in `f`.

## Norm Bound

For `||x||<=1`,

```text
||(S_r f^r)(x_r)|| <= K_r||f^r|| <= K||f||.
```

Also `||e_r||<=1` and `||x_{\ne r}||<=||x||<=1`, so

```text
||P_r f(e_r,x_{\ne r})|| <= ||f||.
```

Therefore

```text
||(Sf)_r(x)|| <= (K+1)||f||
```

for every `r`, and taking the max over `r` gives

```text
||Sf|| <= (K+1)||f||.
```

There is no factor depending on `m`.

## Right-Inverse Check

Write the original primitive components as

```text
h_{rs}:B_s -> B_r,        h_{rs}(x)=P_r h(x).
```

For `r != s` and `x in B_s`,

```text
P_r f(e_r,x)=e_r o h_{rs}(x)=h_{rs}(x),
```

since all other terms vanish and `e_r` is the unit on the output ideal `B_r`.
Thus the off-block part of `Sf` agrees with the off-block part of `h`.

On each diagonal block, `S_r f^r` is a primitive for `f^r`; it may differ from
`h_{rr}` by a derivation of `B_r`, which is harmless because derivations are
exactly in `ker d^1`.

Now check cases.

1. If `a,b in B_r`, the output in `B_r` is correct because
   `d^1_{B_r}S_r f^r=f^r`. For output `B_j`, `j != r`, all product terms
   vanish and

```text
P_j(d^1Sf)(a,b)=-(Sf)_j(a o b)=-h_{jr}(a o b)=P_j f(a,b).
```

2. If `a in B_r`, `b in B_s`, and `r != s`, then `a o b=0`. The output in
   `B_r` is

```text
a o (Sf)_r(b)=a o h_{rs}(b)=P_r f(a,b),
```

and similarly the output in `B_s` is `P_s f(a,b)`. All other output ideals
receive zero from both sides.

These cases exhaust pairs of homogeneous ideal inputs; bilinearity gives

```text
d^1Sf=f
```

on all of `B x B`.

## Consequences

1. For adjoint modules, the number of direct summands is not a source of
   dimension growth. Uniformity reduces to uniformity for simple factors plus
   a universal `+1` off-block cost.
2. This is the precise version of Agent A's summand-count reduction that Agent
   B accepts. It is valid for adjoint/block-respecting modules. It is not valid
   for arbitrary modules without separately controlling mixed Peirce modules.
3. Combined with the unit-normalized reduction, one may also first remove the
   global `h(1)` multiplication component and then apply this direct-sum
   formula to the normalized residual.

At the time of this reduction, the remaining exact adjoint benchmark was the
normalized simple-factor problem, especially the high-rank matrix factors
`H_n(F)`. The simple-factor benchmark is now closed by
`agent-B/notes/matrix-factor-exact-adjoint-splitting-theorem.md` together with
the spin and bounded-rank notes; this direct-sum reduction then gives finite
direct sums.
