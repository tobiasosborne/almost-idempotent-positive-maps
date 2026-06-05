# Real Symmetric Matching Reconstruction Theorem

Date: 2026-06-05.

This note proves a dimension-free reconstruction estimate for real symmetric
sector-preserving Schur symbols. The proof works over either real or complex
all-matrix Schur multiplier norms, provided all rectangular slice norms are
measured over the same scalar field. Over the real field it closes the
one-dimensional real sector-preserving residual isolated in
`agent-B/notes/sector-preserving-schur-residual.md`; over the complex field it
is also used in the scalar Hermitian corollary
`agent-B/notes/hermitian-scalar-sector-reconstruction-corollary.md`.

## Setup

Fix `K0 in {R,C}`. Let `Omega` be finite, `N=|Omega|`, and let

```text
m_ab=m_ba in R,        m_aa=0.
```

Let `M_m` be the corresponding Schur multiplier on all matrices over `K0`,
with the same ordered symbol `m_ab`. Its norm bounds, in particular, the
restriction to real symmetric matrices when `K0=R`.
For disjoint equal-size blocks `I,J,K` and a bijection `pi:J->K`, define the
matching curvature slice

```text
kappa_pi(i,j)=m_ij+m_{j,pi(j)}-m_{i,pi(j)}
        (i in I, j in J).
```

Let `M_{kappa_pi}` denote the corresponding rectangular Schur multiplier over
the same scalar field `K0`, and set

```text
S = sup_{I,J,K,pi} ||M_{kappa_pi}||,
E = sup_{a != b} |m_ab|.
```

If no nonempty disjoint triple exists, set `S=0`.

## Theorem

There is a universal constant `C` such that

```text
||M_m|| <= C(S+E).
```

One may take `C=24`.

Consequently, for the real sector-preserving residual `f=d^1M_m`,

```text
||M_m|| <= 60 ||f||_inj
```

with the same scalar-field convention for the Schur multiplier norms.

## Proof

The cases `N<=2` are controlled by `E`, so assume `N>=3`. Put

```text
m0=floor(N/3).
```

Choose uniformly an ordered triple `(I,J,K)` of pairwise disjoint subsets of
`Omega`, each of size `m0`. Define an ordered symbol `eta=eta_{I,J,K}` as
follows. If the ordered pair `(a,b)` lies in two different selected blocks, let
`C(a,b)` be the third selected block and set

```text
eta_ab = m0^{-1} sum_{c in C(a,b)} (m_ab+m_bc-m_ac).
```

Set `eta_ab=0` otherwise. Notice that `eta_ba` is generally different from
`eta_ab`; this is why we work with the all-matrix Schur multiplier extension.

For each selected ordered rectangular block, `eta` is the average over all
bijections from the middle block to the third block of matching curvature
slices, so its Schur multiplier norm is at most `S`. Decomposing into the six
ordered rectangular block maps gives

```text
||M_eta|| <= 6S.
```

Fix distinct `a,b`. The probability that `a,b` lie in two different selected
blocks is

```text
p = 6m0^2/(N(N-1)).
```

Conditioned on this event, the third block is a uniform `m0`-subset of
`Omega \ {a,b}`. Put

```text
r_a=sum_{c in Omega} m_ac.
```

Then

```text
E[eta_ab | a,b selected in different blocks]
 = m_ab + (r_b-m_ab)/(N-2) - (r_a-m_ab)/(N-2)
 = m_ab + (r_b-r_a)/(N-2).
```

Hence

```text
E eta_ab = p m_ab + p (r_b-r_a)/(N-2).
```

Therefore

```text
m_ab = p^{-1} E eta_ab - (r_b-r_a)/(N-2).
```

The first term has Schur multiplier norm at most

```text
p^{-1} ||M_{E eta}|| <= p^{-1} E ||M_eta|| <= p^{-1} 6S.
```

For `N>=3` and `m0=floor(N/3)`, `p^{-1}<=10/3`, so this is at most `20S`.

The second term is a row-column Schur symbol on ordered matrix entries. Since

```text
|r_a| <= (N-1)E,
```

its Schur multiplier norm is at most

```text
2(N-1)E/(N-2) <= 4E.
```

Thus

```text
||M_m|| <= 20S+4E <= 24(S+E).
```

This proves the theorem.

For `f=d^1M_m`, over the same scalar field `K0`, the square terms give

```text
||f||_inj >= 2E,
```

because `f(s_ab,s_ab)=2m_ab(e_a+e_b)`. The matching-slice lemma, with
rectangular test matrices over `K0`, gives

```text
||f||_inj >= (1/2)S.
```

Therefore

```text
||M_m|| <= 24(2||f||_inj + (1/2)||f||_inj)
        = 60||f||_inj.
```

The constant is not optimized.

## Consequence

For `H_n(R)`, once the fixed-frame reductions have isolated the
sector-preserving scalar Schur residual, that residual is dimension-free
controlled by its exact adjoint coboundary.

Together with the pure skew reconstruction theorem, this gives the scalar
Hermitian residual estimate. The complex anti-linear Peirce edge field is
controlled separately in
`agent-B/notes/complex-antilinear-peirce-residual-theorem.md`, and the
quaternionic internal Peirce edge field in
`agent-B/notes/quaternionic-internal-peirce-residual-theorem.md`. Off-sector
leakage is globalized in
`agent-B/notes/off-sector-leakage-globalization-theorem.md`, and the assembled
matrix result is recorded in
`agent-B/notes/matrix-factor-exact-adjoint-splitting-theorem.md`.
