# Theorem C: Conditional Exact UP Factorization From Projection Stability

This file records a theorem-level implication. It does not prove
near-positive projection stability; it proves that such stability would convert
the algebraic bridge into exact unital-positive factor maps.

## Hypothesis: Near-Positive Projection Stability

Assume there are universal constants `delta0,K` such that the following holds
for every finite-dimensional Hilbert space `H`.

Let `V=B(H)_sa`. If `R:V->V` is linear and satisfies

```text
R^2=R,        R(1)=1,        ||R||<=1+delta,
x>=0, ||x||<=1  =>  R(x)>=-delta 1,
0<delta<=delta0,
```

then there is a unital positive idempotent `E:V->V` with

```text
||E-R|| <= K sqrt(delta).
```

The exponent `1/2` is sharp already in the classical `ell_infty^3` case.

## Theorem

Assume the projection-stability hypothesis. Then there are universal constants
`eta0,C` with the following property.

Let `V=B(H)_sa` with `dim H<infty`, and let `Phi:V->V` be unital positive with

```text
||Phi^2-Phi|| <= eta <= eta0.
```

Then there are:

- a finite-dimensional special JB algebra `J`;
- unital positive maps

```text
Delta:J -> V,        Upsilon:V -> J
```

such that

```text
||Delta Upsilon - Phi|| <= C sqrt(eta),
Upsilon Delta = id_J,
```

and, for the Jordan product `*` of `J`,

```text
Upsilon(Delta(x) o Delta(y)) = x*y,        x,y in J.
```

Here `o` is the ambient Jordan product on `B(H)_sa`.

Thus the only conditional ingredient in this route is the projection-stability
hypothesis; no abstract positivity rounding is used.

## Proof

Let

```text
P = theta(2Phi-I)
```

be the spectral idempotent. As in
`agent-B/theory/theorem-B-algebraic-bridge.md`, with `S=2Phi-I` we have
`S^2-I=4(Phi^2-Phi)`. The Banach-algebra formula

```text
sgn(S)=S(S^2)^(-1/2),        P=(I+sgn(S))/2
```

gives, after decreasing `eta0`,

```text
P^2=P,        P(1)=1,        ||P-Phi||<=C eta,        ||P||<=1+C eta.
```

Moreover `P` is `C eta`-positive. Indeed, if `x>=0`, then `Phi(x)>=0`, so

```text
P(x) >= -||P(x)-Phi(x)|| 1 >= -C eta ||x|| 1.
```

Set `delta=C eta`. For `eta0` small enough, the projection-stability hypothesis
applies to `R=P`. Hence there is a unital positive idempotent `E:V->V` with

```text
||E-P|| <= C sqrt(eta).
```

By the Effros-Stormer positive-projection theorem, the range

```text
J=E(V)
```

is a finite-dimensional special JB algebra for the product

```text
x*y = E(x o y),        x,y in J,
```

with the given vector-space structure and inherited Banach norm.

Here is the real-to-complex justification for invoking Effros-Stormer. The
map `E` is defined on the real self-adjoint part `V=B(H)_sa`. Its complex
linear extension

```text
E_C(a+ib)=E(a)+iE(b),        a,b in V,
```

is unital, self-adjoint, idempotent, and positive as a map
`B(H)->B(H)`: positivity of a complex-linear map is checked on positive
self-adjoint inputs, where it agrees with the original `E`. Thus the
Effros-Stormer theorem for unital positive projections on C*-algebras applies
to `E_C`. Restricting the resulting Choi-Effros/Jordan product to the
self-adjoint range gives exactly the real product above:

```text
x*y=E(x o y),        x,y in E(V).
```

The JB positive cone on `J` is exactly the inherited cone

```text
J_+ = J cap B(H)_+.
```

For one inclusion, if `x=y*y` in the Effros-Stormer product, then

```text
x=E(y o y),
```

and `y o y>=0` in `B(H)_sa`; positivity of `E` gives `x>=0` ambiently.

For the converse, use the standard unital JB criterion

```text
z>=0  iff  || ||z|| 1-z || <= ||z||,
```

which follows from the JB spectral calculus. If `z in J cap B(H)_+` and
`m=||z||`, then `0<=z<=m1` ambiently, so `||m1-z||_{B(H)}<=m`. Effros-Stormer
gives `J` the inherited Banach norm, hence `||m1-z||_J<=m`, and the criterion
implies that `z` is positive in the JB cone of `(J,*)`.

Thus `J` is a special JB algebra with the inherited order-unit cone and
operator norm.

Define

```text
Delta:J -> V,        Delta(x)=x,
Upsilon:V -> J,      Upsilon(a)=E(a).
```

Both maps are unital. They are positive with respect to the stated cones:

- if `x in J_+`, then `x in B(H)_+`, so `Delta(x)=x` is positive in `V`;
- if `a in V_+=B(H)_+`, then `E(a)` is positive in `B(H)_+` because `E` is
  positive, and `E(a) in J` because `E` is idempotent. Hence
  `Upsilon(a)=E(a) in J_+`.

The factorization estimates are immediate:

```text
Upsilon Delta = id_J,
Delta Upsilon = E,
```

and therefore

```text
||Delta Upsilon - Phi||
 <= ||E-P|| + ||P-Phi||
 <= C sqrt(eta).
```

Finally, for `x,y in J`,

```text
Upsilon(Delta(x) o Delta(y))
 = E(x o y)
 = x*y
```

by definition of the Effros-Stormer product. This proves the theorem.

## Consequence

The route from arbitrary almost-idempotent UP maps to exact UP factor maps is
therefore reduced to the single perturbative projection-stability theorem
above. The remaining open classical core is the dimension-free Markov theorem
recorded in `agent-B/notes/near-positive-projection-stability-program.md`.
