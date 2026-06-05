# Central-Valued Matrix Primitive Estimate

Date: 2026-06-04.

This note complements `agent-B/notes/cochain-norm-conversion-caveat.md`.
The family `h(x)=x_11 1` shows that Frobenius-bounded primitives are the wrong
target. But that same family is harmless in the order norm. More generally,
all central-valued adjoint primitives in the matrix Jordan families are
uniformly controlled.

## Setup

Let

```text
J=H_n(F),        F in {R,C,H},
```

with Jordan product `a o b=(ab+ba)/2` and operator/order-unit norm. For a real
linear functional `phi:J->R`, define the central-valued 1-cochain

```text
h_phi(x)=phi(x)1.
```

Use the cochain norms

```text
||h|| = sup_{||x||<=1} ||h(x)||,
||f|| = sup_{||x||,||y||<=1} ||f(x,y)||.
```

Then

```text
||h_phi|| = ||phi||_*
```

where `||.||_*` is the dual norm to the operator norm.

The adjoint coboundary is

```text
(d^1 h)(a,b)=a o h(b)+b o h(a)-h(a o b).
```

For `h_phi` this becomes

```text
f_phi(a,b):=(d^1h_phi)(a,b)
 = phi(b)a + phi(a)b - phi(a o b)1.
```

## Theorem

The restriction

```text
d^1 : {h_phi} -> C^2(J,J)
```

is injective and has a norm-one inverse on its range:

```text
||h_phi|| <= ||d^1 h_phi||.
```

The trivial upper estimate is

```text
||d^1h_phi|| <= 3||h_phi||.
```

Thus central-valued exact coboundaries are controlled with constants
independent of `n` and of `F`.

## Proof

The upper bound follows immediately from the contractivity of the Jordan
product:

```text
||phi(b)a + phi(a)b - phi(a o b)1|| <= 3||phi||_*
```

for `||a||,||b||<=1`.

For the lower bound, represent `phi` by a self-adjoint trace-class density
`rho`:

```text
phi(x)=Re Tr(rho x),        ||phi||_* = Tr |rho|.
```

Let `u=sign(rho)` be the spectral sign symmetry, choosing arbitrary signs on
the kernel. Then

```text
u=u^*,        u^2=1,        ||u||=1,
phi(u)=Tr |rho|=||phi||_*.
```

Put

```text
A=phi(u)=||phi||_*,        B=phi(1).
```

Evaluating the coboundary at `(u,u)` gives

```text
f_phi(u,u)=2A u - B 1.
```

If `u=1`, then `rho>=0`, so `B=A` and `||f_phi(u,u)||=A`. If `u=-1`, then
`rho<=0`, so `B=-A` and again `||f_phi(u,u)||=A`.

Otherwise the spectrum of `u` contains both `+1` and `-1`, and

```text
||2A u-B1||
 = max{|2A-B|,|-2A-B|}
 >= 2A
 >= A.
```

In all cases,

```text
||d^1h_phi|| >= ||f_phi(u,u)|| >= ||phi||_* = ||h_phi||.
```

This proves the theorem.

Injectivity follows at once: if `d^1h_phi=0`, then `||h_phi||<=0`.

## Consequences

1. The high-Frobenius example `h(x)=x_11 1` is not dangerous for an
   order-norm splitting. It lies in a central-valued subspace on which
   `d^1` is uniformly invertible.
2. High-rank output is compatible with order-norm control: central values such
   as `1` have Frobenius norm `sqrt(n)` but operator norm `1`.
3. The matrix-family obstruction is therefore more specific. It is not
   "high-rank primitive values" by themselves. The remaining problem is to
   control the noncentral/noncommutative primitive components in order norm,
   or to organize an incremental construction that avoids global
   reconstruction.

This estimate should be treated as a small positive component of the full
adjoint `H_n(F)` splitting problem.
