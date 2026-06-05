# Hermitian Scalar Sector Reconstruction Corollary

Date: 2026-06-05.

This note combines the real symmetric and pure skew matching reconstruction
theorems. It closes the one-dimensional Hermitian scalar sector-preserving
residual, modulo diagonal frame-stabilizer derivations.

This note only handles the scalar component. The complex anti-linear and
quaternionic internal edge maps are handled in later notes; leakage
globalization remains open.

## Setup

Let `Omega` be finite and let

```text
mu_ba=conj(mu_ab),        mu_aa=0.
```

Write

```text
mu_ab = u_ab+i beta_ab,
u_ab=u_ba in R,        beta_ab=-beta_ba in R.
```

Let `M_mu` be the all-matrix Schur multiplier with ordered symbol `mu`. The
diagonal derivation gauges are

```text
g_alpha,ab=i(alpha_a-alpha_b),        alpha_a in R.
```

For disjoint equal-size blocks `I,J,K` and a bijection `pi:J->K`, set

```text
kappa_pi(i,j)=mu_ij+mu_{j,pi(j)}-mu_{i,pi(j)}.
```

Define

```text
S = sup_{I,J,K,pi} ||M_{kappa_pi}||,
E = sup_{a != b} |u_ab|.
```

If no nonempty disjoint triple exists, set `S=0`.

## Corollary

There is a universal constant `C` such that

```text
dist(M_mu, Der_diag) <= C(S+E),
```

where the distance is in all-matrix Schur multiplier norm. One may take the
more explicit bound

```text
dist(M_mu, Der_diag) <= 36S+24E.
```

Consequently, if `M_mu` is the scalar sector-preserving residual of a
fixed-frame adjoint primitive on `H_n(C)` with `h(e_i)=0`, then

```text
dist(M_mu, Der_diag) <= 84 ||d^1M_mu||_inj.
```

## Proof

Decompose

```text
M_mu = M_u + M_{i beta}.
```

For every matching slice, write

```text
kappa_pi = kappa_pi^u+i kappa_pi^beta.
```

The real and imaginary pieces are controlled by the full slice. Indeed,
entrywise conjugation preserves operator norm and gives

```text
M_{kappa_pi^u}
  = (M_{kappa_pi}+M_{conj(kappa_pi)})/2,
M_{i kappa_pi^beta}
  = (M_{kappa_pi}-M_{conj(kappa_pi)})/2.
```

Thus the matching-slice suprema for `u` and for `i beta` are each at most
`S`.

The real symmetric reconstruction theorem gives

```text
||M_u|| <= 24(S+E).
```

The pure skew reconstruction theorem gives

```text
dist(M_{i beta}, Der_diag) <= 12S.
```

Combining the two estimates,

```text
dist(M_mu, Der_diag)
  <= ||M_u||+dist(M_{i beta}, Der_diag)
  <= 36S+24E.
```

Now suppose `M_mu` is the fixed-frame scalar residual and write

```text
f=d^1M_mu.
```

The matching-slice detection lemma gives

```text
S <= 2||f||_inj.
```

The square terms detect the real part. For the standard complex Peirce vector
`x=X_ab(1)`,

```text
f(x,x)=2u_ab(e_a+e_b),
```

so

```text
E <= (1/2)||f||_inj.
```

Therefore

```text
dist(M_mu, Der_diag)
  <= 36(2||f||_inj)+24((1/2)||f||_inj)
  = 84||f||_inj.
```

This proves the residual estimate.

## Consequence

The scalar Hermitian fixed-frame Schur/connection residual is no longer an
open high-rank obstruction. The complex anti-linear and quaternionic internal
edge-map residuals are controlled in
`agent-B/notes/complex-antilinear-peirce-residual-theorem.md` and
`agent-B/notes/quaternionic-internal-peirce-residual-theorem.md`. Off-sector
leakage is handled in
`agent-B/notes/off-sector-leakage-globalization-theorem.md`.
