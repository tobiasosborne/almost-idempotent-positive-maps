# Matching-Slice Schur Detection

Date: 2026-06-05.

This note records a positive test inside the residual sector-preserving Schur
problem. It complements
`agent-B/notes/pointwise-schur-curvature-caveat.md`.

The fixed-middle-vertex test is too weak: it only sees rank-one products. But
a bounded matching input can see a full Schur multiplier slice.

The first theorem below is general. The triangular sign stress family is then
an immediate special case: it has logarithmic ordinary bilinear defect, so it
is not a counterexample to the desired residual estimate.

## General Matching-Slice Lemma

Work in

```text
J=H_N(C)
```

and let `mu_ab` be a Hermitian Schur symbol:

```text
mu_ba=conj(mu_ab),        mu_aa=0.
```

Let `S_mu` be the sector-preserving Schur operator

```text
S_mu(x)_ab = mu_ab x_ab        (a != b),
S_mu(x)_aa = 0.
```

Let `I,J,K` be pairwise disjoint index sets with `|I|=|J|=|K|=n`, and let
`pi:J->K` be a bijection. For `A in M_{I,J}(C)`, define Hermitian matrices
`X_A` and `Y_pi` by

```text
(X_A)_{ij}=A_{ij},        (X_A)_{ji}=conj(A_{ij}),
(Y_pi)_{j,pi(j)}=1,      (Y_pi)_{pi(j),j}=1,
```

with all other entries zero.

Then

```text
||Y_pi||=1,        ||X_A||=||A||.
```

The `I-K` block of `d^1S_mu(X_A,Y_pi)` is

```text
((d^1S_mu)(X_A,Y_pi))_{i,pi(j)}
 = (1/2)(mu_ij+mu_{j,pi(j)}-mu_{i,pi(j)}) A_ij.
```

No other block except the adjoint `K-I` block appears. Hence

```text
||d^1S_mu||_inj
 >= (1/2) ||M_{kappa_pi}||,
```

where `M_{kappa_pi}` is the ordinary Schur multiplier on `M_{I,J}(C)` with
symbol

```text
kappa_pi(i,j)=mu_ij+mu_{j,pi(j)}-mu_{i,pi(j)}.
```

### Proof

Since the supports are on consecutive blocks `I-J` and `J-K`, the Jordan
product `X_A o Y_pi` is supported only on `I-K` and `K-I`, with

```text
(X_A o Y_pi)_{i,pi(j)} = (1/2) A_ij.
```

The same support calculation gives

```text
(S_mu(X_A) o Y_pi)_{i,pi(j)}
  = (1/2) mu_ij A_ij,

(X_A o S_mu(Y_pi))_{i,pi(j)}
  = (1/2) mu_{j,pi(j)} A_ij,

S_mu(X_A o Y_pi)_{i,pi(j)}
  = (1/2) mu_{i,pi(j)} A_ij.
```

Subtracting gives the displayed formula. The Hermitian matrix with one
off-diagonal block `C` and adjoint block `C*` has operator norm `||C||`, so
taking the supremum over `A` proves the norm lower bound.

## Triangular Sign Stress Family

Now specialize to

```text
J=H_{3n}(C),
L={1,...,n},        M={bar 1,...,bar n},        R={hat 1,...,hat n},
```

and take `pi(bar q)=hat q`. Let `sigma_pq=sign(p-q)` and define the skew
connection

```text
beta_{p,bar q}=sigma_pq,
beta_{bar q,p}=-sigma_pq,
beta_{ij}=0        otherwise.
```

Let

```text
mu_ab=i beta_ab.
```

Then `S_mu=K_beta`. Since `mu` vanishes on `M-R` and `L-R` edges, the
matching-slice symbol is just

```text
kappa_pi(p,bar q)=i sign(p-q).
```

Equivalently, for the block flip `Y` between `M` and `R` and the `L-M` block
matrix `X_A`,

```text
d^1K_beta(X_A,Y)
 = (1/2) X_{i(sign o A)}
```

on the `L-R` block. In block matrix form,

```text
d^1K_beta(X_A,Y)
 = (1/2) [ 0   0  B ]
         [ 0   0  0 ]
         [ B*  0  0 ],
        B=i(sign o A).
```

Consequently

```text
||d^1K_beta||_inj
  >= (1/2) sup_{A != 0} ||i(sigma o A)||/||A||.
```

The right side is half the ordinary triangular sign Schur multiplier norm.

## Consequences

The triangular sign family is a serious stress test, but it is not a
counterexample to the residual estimate. Its primitive Schur multiplier norm
grows logarithmically with `n`, and the displayed three-block matching formula
shows that its ordinary bilinear defect also grows at least logarithmically.

Thus the ordinary bilinear norm can see more than the fixed-vertex rank-one
slice.

The remaining gap is now sharper: one needs a general way to recover the Schur
multiplier norm of an arbitrary residual symbol from the family of matching
curvature slices

```text
kappa_pi(i,j)=mu_ij+mu_{j,pi(j)}-mu_{i,pi(j)},
```

together with the square-detected edge weights. This is stronger than
coefficientwise curvature control but still weaker than a complete proof of
the residual Schur estimate.
