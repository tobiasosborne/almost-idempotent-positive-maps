# Next-Arrow To Newton Error Reduction

Date: 2026-06-05.

This note records the perturbative algebra that turns a dimension-free
next-arrow estimate into a Kitaev-style error-reduction step. It is conditional:
it does not prove the global Layer 1 homotopy. It clarifies exactly what the
exact-complex estimates must deliver.

## Setup

Let `B` be a unital JB algebra with product `o` and norm `|| ||`. Assume

```text
||a o b|| <= ||a||||b||.
```

Let `theta:B x B -> B` be a symmetric bilinear 2-cochain with

```text
theta(1,x)=0,        ||theta||=delta.
```

Define a unit-preserving perturbed product

```text
x*y = x o y + theta(x,y).
```

Use the adjoint coboundary convention

```text
(d^1h)(x,y)=x o h(y)+y o h(x)-h(x o y).
```

For a 2-cochain `theta`, define the linearized Jordan defect

```text
Jtheta(a,b)
 = theta(a^2,a o b) + a^2 o theta(a,b) + (a o b) o theta(a,a)
   - theta(a^2 o b,a) - a o theta(a^2,b)
   - a o (b o theta(a,a)).
```

This is the first-order coefficient of

```text
(a*a)*(b*a) - ((a*a)*b)*a
```

at the exact product `o`.

## Exact Estimates Assumed

Assume the unit-normalized adjoint complex of `B` has constants `K_1,K_2`:

1. **Exact coboundary inverse.** If `c=d^1h_0` and `c(1,x)=0`, then there is
   `h` with

   ```text
   h(1)=0,        d^1h=c,        ||h|| <= K_1||c||.
   ```

2. **Next-arrow estimate.** Every unit-normalized symmetric 2-cochain `eta`
   satisfies

   ```text
   dist(eta,im d^1) <= K_2||Jeta||.
   ```

These are exactly the two estimates isolated in
`agent-B/notes/layer1-after-adjoint-benchmark-obligations.md`: inversion of
exact coboundaries is not enough; one also needs the next arrow.

## Lemma 1: Approximate Jordan Identity Gives An Approximate Cocycle

Let

```text
Def_*(a,b)=(a*a)*(b*a)-((a*a)*b)*a.
```

For `||a||,||b||<=1`,

```text
Def_*(a,b)=Jtheta(a,b)+E_2(a,b),
```

where

```text
||E_2|| <= C_0 delta^2
```

with a universal numerical constant `C_0`.

Indeed, expand the three products in the Jordan identity using
`*=o+theta`. The zeroth-order term vanishes by the exact Jordan identity in
`B`; the terms linear in `theta` are precisely the displayed `Jtheta`; every
remaining term contains at least two occurrences of `theta` and at most three
contractive products, so it is bounded by a universal multiple of `delta^2`.

Consequently, if the perturbed product has Jordan defect

```text
||Def_*|| <= epsilon,
```

then

```text
||Jtheta|| <= epsilon + C_0 delta^2.
```

This is the precise version of the informal statement
`d^2theta=O(epsilon+delta^2)`.

## Lemma 2: Coordinate Change Kills A Coboundary To First Order

Let `h:B->B` satisfy

```text
h(1)=0,        ||h|| <= 1/4,
```

and put

```text
T=I-h.
```

Transport `*` by `T`:

```text
x *' y = T^{-1}(Tx * Ty).
```

Then `1` remains the unit and

```text
x *' y = x o y + theta'(x,y),
```

where

```text
theta' = theta - d^1h + E_T,
||E_T|| <= C_1(delta||h||+||h||^2)
```

for a universal `C_1`.

Proof: since `||h||<=1/4`,

```text
T^{-1}=I+h+R_h,        ||R_h|| <= 2||h||^2.
```

Expanding

```text
(x-hx)*(y-hy)
```

and applying `I+h+R_h`, the first-order terms are

```text
theta(x,y)-x o h(y)-y o h(x)+h(x o y)
 = theta(x,y)-(d^1h)(x,y).
```

All other terms contain either one `theta` and one `h`, or at least two `h`'s,
hence have the displayed bound.

## Conditional Newton Step

Assume `||theta||=delta` and `||Def_*||<=epsilon`. Put

```text
rho=K_2(epsilon+C_0delta^2).
```

By Lemma 1 and the next-arrow estimate, choose `c in im d^1` with

```text
||theta-c|| <= rho.
```

Then

```text
||c|| <= delta+rho.
```

Using the exact coboundary inverse, pick `h(1)=0` with

```text
d^1h=c,        ||h|| <= K_1(delta+rho).
```

If `K_1(delta+rho)<=1/4`, Lemma 2 gives a transported product whose
perturbation `theta'` satisfies

```text
||theta'|| <= K_2(epsilon+C_0delta^2)
              + C_1(delta||h||+||h||^2)
            <= C(K_1,K_2)(epsilon+delta^2),
```

where the last inequality uses the smallness of `delta+rho` to absorb
`rho^2` into `rho`.

Thus the defect size improves by the Newton rule

```text
delta -> C(K_1,K_2)(epsilon+delta^2).
```

If `K_1` and `K_2` are universal for the family of algebras/modules under
consideration, this is the desired dimension-free error-reduction step.

## What This Does And Does Not Prove

This note proves the perturbative bookkeeping after the exact-complex
estimates are available. It does **not** prove the global Layer 1 theorem,
because the needed `K_2` estimate is still open for full noncommutative
matrix/internal Peirce cochains and for the approximate modules arising during
iteration.

It does show that the recently proved positive tests have the correct form:

- commutative scalar sectors;
- normalized adjoint spin sector;
- fixed diagonal-frame matrix modules.

In any incremental Jordan-frame construction where the relevant local
configuration has uniform `K_1` and `K_2`, this lemma supplies the Newton
improvement without further cohomological input.
