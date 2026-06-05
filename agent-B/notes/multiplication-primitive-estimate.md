# Multiplication Primitive Estimate

Date: 2026-06-04.

This note records a second uniformly controlled component of the adjoint
cochain problem. Unlike
`agent-B/notes/central-valued-matrix-primitive-estimate.md`, this one is not
specific to matrix factors.

## Setup

Let `B` be a unital JB algebra with adjoint module and order-unit norm. For
`c in B`, let

```text
L_c(x)=c o x.
```

Use the adjoint coboundary

```text
(d^1 h)(a,b)=a o h(b)+h(a) o b-h(a o b).
```

The cochain norms are the injective order-unit norms:

```text
||h|| = sup_{||x||<=1} ||h(x)||,
||f|| = sup_{||a||,||b||<=1} ||f(a,b)||.
```

## Theorem

On the multiplication-operator subspace

```text
{L_c : c in B},
```

the coboundary has a norm-one inverse on its range:

```text
||L_c|| <= ||d^1 L_c||.
```

The upper estimate is

```text
||d^1 L_c|| <= 3||L_c||.
```

Thus multiplication primitives are controlled with universal constants,
independent of dimension and independent of the JB factor type.

## Proof

The JB product is contractive, so

```text
||L_c|| <= ||c||.
```

Evaluating at the unit gives equality:

```text
L_c(1)=c,
```

hence

```text
||L_c||=||c||.
```

Let `f_c=d^1L_c`. Then

```text
f_c(1,1)
 = 1 o L_c(1)+L_c(1) o 1-L_c(1)
 = c+c-c
 = c.
```

Since `||1||=1`,

```text
||d^1L_c|| >= ||f_c(1,1)||=||c||=||L_c||.
```

The upper estimate is immediate from contractivity:

```text
||d^1L_c(a,b)||
 <= ||a||||L_c(b)|| + ||L_c(a)||||b|| + ||L_c(a o b)||
 <= 3||L_c|| ||a||||b||.
```

This proves the theorem.

## Consequences

1. The noncentral multiplication part of an adjoint primitive is not a source
   of dimension growth.
2. Together with the central-valued estimate, this controls two basic
   finite-rank-looking components of `End(B)` in the exact adjoint complex:

```text
h(x)=c o x,        h(x)=phi(x)1.
```

3. The uncontrolled matrix-family part must lie in the remaining
   nonmultiplication, noncentral endomorphisms modulo derivations. Any proposed
   full adjoint splitting should explicitly say how it handles that residual
   component.

This estimate is small, but it is useful bookkeeping: it prevents the full
Layer-1 obstruction from being misattributed to the obvious multiplication
operators.
