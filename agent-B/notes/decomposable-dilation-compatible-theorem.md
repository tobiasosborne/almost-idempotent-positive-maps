# A Dilation-Compatible `O(eta)` Decomposable Bridge

This note records a clean positive result after the obstruction in
`decomposable-doubling-obstruction.md`.

## Setup

Let `M` be a finite-dimensional C*-algebra. Suppose there are:

- a finite-dimensional C*-algebra `D`;
- a unital order-isometric Jordan embedding

```text
j:M_sa -> D_sa
```

  so

```text
j(x o y)=j(x) o j(y)
```

  for self-adjoint `x,y`;
- a unital positive linear map `C:D_sa -> M_sa`.

Set

```text
Phi = C j        on M_sa,
F   = j C        on D.
```

Assume that `F` extends complex-linearly to a UCP map `D -> D`.

The obstruction note shows that `Phi` being almost idempotent does not imply
`F` is almost idempotent. Add this as a separate hypothesis:

```text
||F^2-F||_cb <= eta.
```

## Theorem

Under the hypotheses above, the spectral idempotent

```text
P = theta(2Phi-I)
```

has range `A=Im P` whose projected Jordan product

```text
a*b=P(a o b)
```

is an `O(eta)` epsilon-JB order-unit algebra.

## Proof

Since `F` is UCP and `eta`-idempotent, Kitaev's algebraic bridge applies to

```text
tilde F = theta(2F-I),        B=Im tilde F,
X star Y = tilde F(XY).
```

Thus `B` is an `O(eta)` extended C*-algebra. Its self-adjoint part with the
symmetrized product

```text
X circ_star Y = (X star Y + Y star X)/2
              = tilde F((XY+YX)/2)
```

is therefore an `O(eta)` epsilon-JB order-unit algebra. The only order-specific
axiom to check is approximate positivity of squares in the ambient order:

```text
X circ_star X = tilde F(X^2) = F(X^2)+O(eta)||X||^2 >= -C eta ||X||^2 1,
```

because `F` is UCP and `X^2>=0` for self-adjoint `X`.

The intertwining relation

```text
F j = j Phi
```

implies by polynomial functional calculus that

```text
tilde F j = j P.
```

Indeed this holds first for every polynomial in `F` and `Phi`, then for the
holomorphic functional calculus defining the spectral idempotents.

Therefore `j(A) subset B`. For `a,b in A`,

```text
j(a) circ_star j(b)
 = tilde F(j(a) o j(b))
 = tilde F(j(a o b))
 = j(P(a o b))
 = j(a*b).
```

So `j:A -> j(A)` is an exact unital order isometry and exact Jordan
identification between `(A,*)` and the Jordan subalgebra `j(A)` of the
`O(eta)` epsilon-JB algebra `B_sa`.

Restricting the `O(eta)` JB estimates from `B_sa` to `j(A)` gives the claim.

## Consequence

The `O(eta)` branch is valid under the stronger dilation-compatible assumption

```text
||jCjC-jC||_cb <= eta.
```

The missing step for the original decomposable conjecture is exactly to derive
such a dilation-compatible UCP model and this condition, or an equivalent
two-hole estimate, from

```text
||CjCj-Cj|| <= eta.
```

The obstruction note shows that this derivation is false in general.

In particular, this note should not be read as saying that every CP+coCP
decomposition automatically gives such a UCP `F`. For a genuinely coCP leg,
one has to choose between making the doubled embedding multiplicative into an
opposite algebra or making the output map CP in the ordinary C*-sense; both do
not hold simultaneously in a way that would turn every decomposable map into a
CP map.
