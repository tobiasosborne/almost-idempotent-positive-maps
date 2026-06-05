# Unit-Normalized Adjoint Reduction

Date: 2026-06-04.

This note packages a basic but important reduction for the exact adjoint
cochain problem. It uses
`agent-B/notes/multiplication-primitive-estimate.md` to remove the primitive's
value at the unit with dimension-free constants.

## Setup

Let `B` be a unital JB algebra with adjoint module and order-unit norm. The
adjoint coboundary is

```text
(d^1h)(a,b)=a o h(b)+h(a) o b-h(a o b).
```

Use injective order-unit cochain norms.

Call a 1-cochain normalized if

```text
h(1)=0.
```

Call a 2-cochain unit-vanishing if

```text
f(1,x)=f(x,1)=0        for all x.
```

## Lemma

Let `f=d^1h` be an exact adjoint coboundary. Put

```text
c=f(1,1).
```

Then `c=h(1)`. Define

```text
h_0=h-L_c,        f_0=f-d^1L_c,
```

where `L_c(x)=c o x`. Then

```text
h_0(1)=0,        f_0=d^1h_0,
```

and `f_0` is unit-vanishing.

Moreover,

```text
||L_c|| <= ||f||,
||f_0|| <= 4||f||.
```

## Proof

First,

```text
f(1,1)=1 o h(1)+h(1) o 1-h(1)=h(1).
```

Thus `c=h(1)` and `h_0(1)=0`.

If `h_0(1)=0`, then for every `x`,

```text
(d^1h_0)(1,x)=1 o h_0(x)+h_0(1) o x-h_0(x)=0.
```

By symmetry the same holds for `(x,1)`, so `f_0=d^1h_0` is unit-vanishing.

For the norm, the multiplication primitive estimate gives

```text
||L_c||=||c||.
```

Since `c=f(1,1)` and `||1||=1`,

```text
||L_c|| <= ||f||.
```

Also

```text
||d^1L_c|| <= 3||L_c|| <= 3||f||,
```

so

```text
||f_0|| <= ||f||+||d^1L_c|| <= 4||f||.
```

This proves the lemma.

## Splitting Consequence

Suppose there is a linear right inverse on normalized exact coboundaries

```text
S_0 : {f=d^1h : h(1)=0} -> {h:h(1)=0}
```

with

```text
d^1S_0 f=f,        ||S_0 f|| <= K||f||,
```

for unit-vanishing exact 2-cochains. Then there is a full right inverse

```text
S f = L_{f(1,1)} + S_0(f-d^1L_{f(1,1)})
```

with

```text
d^1S f=f,
||S f|| <= (1+4K)||f||.
```

Conversely, any full right inverse restricts to normalized exact coboundaries,
although it may need a postcomposition by the above normalization map to land
inside `h(1)=0`.

## Consequences

1. The primitive value at the unit is never part of the high-rank obstruction.
   It is exactly the multiplication component `L_{h(1)}` and is controlled
   with universal constants.
2. The remaining adjoint matrix-family problem can be stated cleanly:

```text
construct a dimension-free right inverse for exact unit-vanishing
2-coboundaries with normalized primitive h(1)=0.
```

3. This is the form used implicitly in the fixed diagonal-frame proof, where
   the first step removes `m_0=f(1,1)` by the primitive `x -> x.m_0`.

This reduction should be applied before attempting any global matrix or
Peirce-frame construction.
