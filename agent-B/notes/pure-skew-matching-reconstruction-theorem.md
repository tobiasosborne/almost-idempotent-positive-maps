# Pure Skew Matching Reconstruction Theorem

Date: 2026-06-05.

This note proves the matching-curvature reconstruction estimate for the pure
skew sector.

It upgrades `agent-B/notes/matching-curvature-reconstruction-target.md`: the
local tripartite reconstruction does glue, after averaging over random
disjoint triples of blocks.

## Setup

Let `Omega` be finite, `N=|Omega|`, and let

```text
mu_ab=i beta_ab,        beta_ab in R,        beta_ba=-beta_ab,        beta_aa=0.
```

Let `M_mu` be the corresponding Schur multiplier. The diagonal derivation
gauges are

```text
i(alpha_a-alpha_b).
```

For disjoint equal-size blocks `I,J,K` and a bijection `pi:J->K`, define the
matching curvature slice

```text
kappa_pi(i,j)=mu_ij+mu_{j,pi(j)}-mu_{i,pi(j)}
        (i in I, j in J).
```

Set

```text
S = sup_{I,J,K,pi} ||M_{kappa_pi}||,
```

where the supremum is over all disjoint equal-size blocks in `Omega`. If no
such nonempty triple exists, set `S=0`.

## Theorem

There is a universal constant `C` such that

```text
dist_gamma2(mu, Der_diag) <= C S.
```

One may take `C=12` for `N>=3`; for `N<=2` the distance is `0`.

Combining with the matching-slice lower bound

```text
||d^1S_mu||_inj >= (1/2)S
```

gives

```text
dist_gamma2(mu, Der_diag) <= 24 ||d^1S_mu||_inj
```

in the pure skew sector.

## Proof

The case `N<=2` is pure gauge, so assume `N>=3`. Put

```text
m=floor(N/3).
```

Choose uniformly an ordered triple `(I,J,K)` of pairwise disjoint subsets of
`Omega`, each of size `m`. Let `R` be the leftover set. Define a skew symbol
`nu=nu_{I,J,K}` as follows. If `a,b` lie in two different selected blocks,
let `C(a,b)` be the third selected block and set

```text
alpha_a^{C(a,b)} = m^{-1} sum_{c in C(a,b)} beta_ac,
alpha_b^{C(a,b)} = m^{-1} sum_{c in C(a,b)} beta_bc,
```

and

```text
nu_ab = beta_ab-(alpha_a^{C(a,b)}-alpha_b^{C(a,b)}).
```

Set `nu_ab=0` if `a,b` are not in two different selected blocks. Then
`nu_ba=-nu_ab`.

For each selected block pair, the local tripartite reconstruction in
`agent-B/notes/matching-curvature-reconstruction-target.md` writes that
rectangular block of `i nu` as an average of matching curvature slices. Hence
its Schur multiplier norm is at most `S`. Summing over the three selected
block pairs gives the crude uniform bound

```text
||M_{i nu}|| <= 6S.
```

Here we decompose the multiplier into the six ordered rectangular block maps.
Each block extraction and insertion has operator norm at most `1`; the
triangle inequality gives the displayed bound.

Now fix distinct `a,b in Omega`. The probability that `a,b` lie in two
different selected blocks is

```text
p = 6m^2/(N(N-1)).
```

Conditioned on this event, the third selected block is a uniform `m`-subset of
`Omega \ {a,b}`. With

```text
r_a=sum_{c in Omega} beta_ac,
```

we get

```text
E[alpha_a^{C(a,b)} | a,b selected in different blocks]
  = (r_a-beta_ab)/(N-2),

E[alpha_b^{C(a,b)} | a,b selected in different blocks]
  = (r_b+beta_ab)/(N-2).
```

Therefore

```text
E nu_ab
 = p ( beta_ab - (r_a-r_b-2 beta_ab)/(N-2) )
 = pN/(N-2) ( beta_ab - (r_a/N-r_b/N) ).
```

Define the global gauge

```text
gamma_a = r_a/N.
```

Then

```text
beta_ab-(gamma_a-gamma_b)
 = lambda^{-1} E nu_ab,
lambda = pN/(N-2) = 6m^2/((N-1)(N-2)).
```

For `N>=3` and `m=floor(N/3)`,

```text
lambda^{-1} <= 2.
```

Indeed, writing `N=3q+r`, `r in {0,1,2}`, this is the elementary inequality

```text
12q^2 >= (3q+r-1)(3q+r-2).
```

Thus, by convexity of the Schur multiplier norm,

```text
||M_{i(beta-d gamma)}||
 <= lambda^{-1} E ||M_{i nu}||
 <= 12 S.
```

Since `i d gamma` is a diagonal derivation gauge, this proves the theorem.

## Consequence

The pure skew sector of the sector-preserving matrix residual is controlled
dimension-free. Combined with the real symmetric reconstruction theorem, this
gives the scalar Hermitian residual recorded in
`agent-B/notes/hermitian-scalar-sector-reconstruction-corollary.md`. The
complex anti-linear edge field is handled separately in
`agent-B/notes/complex-antilinear-peirce-residual-theorem.md`, and the
quaternionic internal edge maps in
`agent-B/notes/quaternionic-internal-peirce-residual-theorem.md`. Off-sector
leakage is handled in
`agent-B/notes/off-sector-leakage-globalization-theorem.md`.
