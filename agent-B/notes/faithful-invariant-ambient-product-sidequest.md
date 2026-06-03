# Faithful Invariant State Sidequest: Ambient Jordan Product

Question from colleague:

> If `E` is an idempotent unital positive map on `L(H)` with a faithful
> invariant state, then `Ran E` is a Jordan algebra under the ambient Jordan
> product of `L(H)`, not merely under `E(x o y)`. Does this transfer to the
> approximate setting?

## Verdict

Not in the dimension-free operator-norm sense needed by the project.

The exact theorem is qualitative in the faithfulness hypothesis. Its proof uses
that a positive Jordan-Schwarz defect has exactly zero expectation under a
faithful state; faithfulness then forces the positive operator to vanish. In an
approximate theorem, small expectation under a faithful state does not control
operator norm unless the density of the state is bounded below. The obstruction
is real: there is an explicit commutative `3 x 3` family of unital positive
almost-idempotent maps with faithful invariant states whose spectral
near-fixed-point range is not even approximately closed under the ambient
Jordan product.

The correct replacement is:

- with only "admits a faithful invariant state": no uniform transfer;
- with a quantitative lower bound `sigma >= mu I`: ambient closure transfers
  with constants of order `eta/mu`;
- in the project theorem, the projected product `P(x o y)` remains necessary.

## Exact Mechanism

Let `T:L(H)->L(H)` be unital positive and `sigma` a faithful invariant state.
For a fixed point `a=Ta`, Jordan-Schwarz gives

```text
D_a := T(a* o a) - T(a)* o T(a) >= 0.
```

Invariance gives `sigma(D_a)=0`; faithfulness gives `D_a=0`. Thus fixed points
lie in the positive-map multiplicative domain, and the multiplicative-domain
theorem gives closure under ambient Jordan products. This is exactly
`agent-A/refs/vlw-src/paper.tex` Proposition `prop:fixpoint` (lines 600--610),
using `prop:multiplicative_dom`.

This proof has no dimension-free quantitative version without a lower bound on
`sigma`.

## Counterexample Family

Work first on the commutative algebra `ell_infty^3`, with row-stochastic
matrices acting on observables. Let

```text
P0 = [ 1    0    0
       0    1    0
       1/3  2/3  0 ],

J  = (1/3) [ 1 1 1
             1 1 1
             1 1 1 ],

T_a = (1-a) P0 + a J,        0<a<1/2.
```

Equivalently,

```text
T_a =
[ 1-2a/3      a/3          a/3
  a/3         1-2a/3       a/3
  1/3         2/3-a/3      a/3 ].
```

Then `T_a` is strictly positive row-stochastic, hence it has a faithful
stationary state. Direct calculation gives

```text
pi_a = (4/9-a/9, 5/9-2a/9, a/3),
pi_a T_a = pi_a,
```

so the invariant state is faithful for every `a>0`, but its minimum weight is
`a/3`.

The characteristic polynomial is

```text
lambda (lambda-1) (lambda+a-1).
```

Thus the spectral idempotent onto the two eigenvalues near `1` is

```text
P_a = ((2-a)T_a - T_a^2)/(1-a)

    = [ 1-a/9      -2a/9       a/3
        -a/9       1-2a/9      a/3
        1/3-a/9    2/3-2a/9    a/3 ].
```

The almost-idempotence defect is

```text
T_a^2 - T_a =
  a(1-a)/9 [ -5   5   0
               4  -4   0
               1  -1   0 ],
```

so

```text
eta_a := ||T_a^2-T_a||_{infty->infty}
       = 10 a(1-a)/9 -> 0.
```

Now take

```text
r = (1,0,1/3).
```

One checks exactly that `P_a r = r`, so `r in Ran P_a`. But with the ambient
Jordan product, which is just pointwise multiplication in this commutative
example,

```text
(I-P_a)(r^2)
  = (2a/27, 2a/27, 2a/27 - 2/9).
```

Therefore

```text
||r^2 - P_a(r^2)||_infty = 2/9 - 2a/27 -> 2/9,
```

even though `eta_a -> 0` and `T_a` has a faithful invariant state for every
`a>0`.

This also gives a best-distance obstruction. Since `||I-P_a||_{infty->infty}`
is uniformly bounded, `dist(r^2, Ran P_a)` is bounded below by a positive
constant for all sufficiently small `a`.

To embed this literally into `L(C^3)`, define

```text
Phi_a(X) = diag( T_a diag(X) ).
```

This map is unital and positive on `M_3`. With
`rho_a=diag(pi_a)`, it satisfies `tr(rho_a Phi_a(X))=tr(rho_a X)`, so it has a
faithful invariant state. Its spectral idempotent kills off-diagonal matrices
and acts as `P_a` on the diagonal. The same diagonal element `r` gives the same
ambient Jordan-product defect in `L(C^3)_sa`.

Hence the colleague's exact statement does not transfer to the approximate
setting at the uniform operator-norm level.

Since the only zero eigenvalue of `T_a` is the excluded spectral value and the
other two eigenvalues are nonzero, `Ran T_a = Ran P_a`. Thus the same example
also defeats the naive formulation using the literal range of the
almost-idempotent map rather than the spectral near-fixed-point range.

## Conditional Positive Statement

There is a quantitative statement if the invariant state is uniformly faithful.

Let `T:L(H)_sa -> L(H)_sa` be unital positive, `sigma`-preserving, and
`||T^2-T|| <= eta`. Let `P=theta(2T-I)` and `A=Ran P`. Suppose the density of
`sigma` satisfies

```text
rho_sigma >= mu I
```

with `mu>0`. Then, for `eta` small and `a,b in A`,

```text
||a o b - P(a o b)|| <= C (eta/mu) ||a|| ||b||.
```

Sketch with the needed constants exposed. Spectral calculus gives
`delta:=||P-T||<=C eta`, and for `a in A`,

```text
||T a-a|| <= delta ||a||.
```

For self-adjoint `a`, Jordan-Schwarz gives the positive defect

```text
D_a := T(a^2)-T(a)^2 >= 0.
```

Invariance gives

```text
sigma(D_a)
 = sigma(a^2 - T(a)^2)
 <= ||a^2-T(a)^2||
 <= 2 delta ||a||^2.
```

Since `rho_sigma >= mu I`, positivity implies

```text
||D_a|| <= mu^{-1} sigma(D_a)
         <= 2 delta mu^{-1} ||a||^2.
```

Now

```text
P(a^2)-a^2
 = (P-T)(a^2) + D_a + (T(a)^2-a^2),
```

so

```text
||P(a^2)-a^2|| <= C (eta/mu) ||a||^2.
```

Polarization, with the usual optimizing scalar, gives the bilinear estimate
for `a o b - P(a o b)`.

This bound is not dimension-free in the usual trace-preserving case unless one
allows a dimension factor (`mu=1/dim H` for the normalized trace). In the
counterexample above, `mu=a/3` and `eta/mu` is order one, exactly matching the
failure of ambient closure.

## Project Consequence

For the main bridge theorem, faithful invariant states do not justify replacing
the projected Choi-Effros/Jordan product

```text
x bullet y = P(x o y)
```

by the ambient product on `Ran P`. They only justify such a replacement under
extra quantitative conditioning assumptions on the invariant state, or in fixed
dimension with constants allowed to depend on that state.
