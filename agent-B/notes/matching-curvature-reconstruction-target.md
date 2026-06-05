# Matching Curvature Reconstruction Target

Date: 2026-06-05.

This note packages the current residual Schur/connection problem after
`agent-B/notes/matching-slice-schur-detection.md`.

It records the exact reconstruction inequality for the sector-preserving
complex skew residual, checks that the kernel is exactly the expected diagonal
derivation gauge, and records the current proof status. The pure skew estimate
is now proved in `agent-B/notes/pure-skew-matching-reconstruction-theorem.md`;
combined with the real symmetric theorem it gives the scalar Hermitian
corollary in
`agent-B/notes/hermitian-scalar-sector-reconstruction-corollary.md`.

## Symbols And Gauge

Let `Omega` be a finite set and let

```text
mu_ab,        a,b in Omega,
```

be a Hermitian Schur symbol:

```text
mu_ba=conj(mu_ab),        mu_aa=0.
```

It defines the sector-preserving Schur operator

```text
S_mu(x)_ab=mu_ab x_ab        (a != b),        S_mu(x)_aa=0
```

on `H_Omega(C)`.

Diagonal frame-stabilizer derivations are the gauge symbols

```text
mu_ab=i(alpha_a-alpha_b),        alpha_a in R.
```

These are exactly the Schur symbols of commutators with diagonal
skew-Hermitian matrices.

## Curvature

For distinct `a,b,c`, define the triangle curvature

```text
curv_mu(a,b,c)=mu_ab+mu_bc-mu_ac.
```

The full bilinear defect `d^1S_mu` contains these coefficients on products

```text
V_ab x V_bc -> V_ac.
```

The matching-slice lemma proves that for disjoint blocks `I,J,K` and a
bijection `pi:J->K`,

```text
||d^1S_mu||_inj >= (1/2)||M_{kappa_pi}||,
```

where

```text
kappa_pi(i,j)=curv_mu(i,j,pi(j)).
```

Thus the ordinary bilinear defect controls every matching curvature slice in
Schur multiplier norm.

## Zero Curvature Kernel

If

```text
curv_mu(a,b,c)=0
```

for all distinct `a,b,c`, then `mu` is a diagonal derivation gauge.

Indeed, fix a base point `o`. For distinct `a,b` different from `o`,

```text
mu_ab=mu_ao+mu_ob.
```

Write

```text
mu_oa=r_a+i s_a.
```

Then Hermiticity gives

```text
mu_ao=r_a-i s_a,
mu_ob=r_b+i s_b,
```

so the first relation gives

```text
mu_ab=r_a+r_b+i(s_b-s_a).
```

Now use the other orientation

```text
curv_mu(a,b,o)=mu_ab+mu_bo-mu_ao=0.
```

Substituting the displayed formula gives `2r_b=0`. Since `b` was arbitrary,
all `r_b` vanish. Hence

```text
mu_ab=i(s_b-s_a),
```

including edges involving `o` after setting `s_o=0`. This is the gauge form
with `alpha_a=-s_a`.

So the curvature target has the correct exact kernel.

## Reconstruction Target

The desired dimension-free estimate is:

```text
dist_gamma2(mu, Der_diag)
 <= C ( sup_{I,J,K,pi} ||M_{kappa_pi}|| + E_real(mu) ),
```

where:

- `Der_diag` is the space of diagonal derivation gauges
  `i(alpha_a-alpha_b)`;
- `dist_gamma2` is distance in Schur multiplier norm;
- the supremum is over disjoint equal-size blocks and bijections `pi:J->K`;
- `M_{kappa_pi}` is the ordinary Schur multiplier on matrices indexed by
  `I x J`;
- `E_real(mu)` is the square-detected real symmetric edge term
  `sup |Re mu_ab|`.

For the pure skew connection sector, the edge term is absent after quotienting
by gauge, and the target is simply:

```text
dist_gamma2(mu, Der_diag)
 <= C sup_{I,J,K,pi} ||M_{kappa_pi}||.
```

This pure skew estimate is now proved in
`agent-B/notes/pure-skew-matching-reconstruction-theorem.md`, with an explicit
universal constant. The companion real symmetric estimate is proved in
`agent-B/notes/real-symmetric-matching-reconstruction-theorem.md`, and the two
combine in
`agent-B/notes/hermitian-scalar-sector-reconstruction-corollary.md`.

## Basic Checks

This target is stronger than pointwise curvature control and avoids the
fixed-middle-vertex rank-one trap. Its scalar Hermitian form is now controlled.
It is only one component of the full exact-adjoint matrix benchmark; the
remaining components are handled in the later internal Peirce and leakage
notes.

Known checks before the local estimate below:

1. Gauge symbols have zero matching curvature.
2. Zero curvature implies gauge.
3. The triangular sign stress family is detected by a three-block matching
   slice.

## Local Tripartite Reconstruction

There is one useful positive result short of the global target.

Assume the pure skew case

```text
mu_ab=i beta_ab,        beta_ab in R,        beta_ba=-beta_ab.
```

Let `I,J,K` be pairwise disjoint equal-size blocks. Define a local gauge on
`I union J` by

```text
alpha_i = |K|^{-1} sum_{k in K} beta_ik        (i in I),
alpha_j = |K|^{-1} sum_{k in K} beta_jk        (j in J).
```

Then for `i in I`, `j in J`,

```text
beta_ij-(alpha_i-alpha_j)
 = |K|^{-1} sum_{k in K} (beta_ij+beta_jk-beta_ik).
```

Equivalently,

```text
mu_ij-i(alpha_i-alpha_j)
 = |K|^{-1} sum_{k in K} curv_mu(i,j,k).
```

Averaging over uniformly random bijections `pi:J->K` gives

```text
mu_ij-i(alpha_i-alpha_j)
 = E_pi kappa_pi(i,j).
```

Therefore, by convexity of the Schur multiplier norm,

```text
||M_{(mu-i d alpha)|_{I x J}}||
 <= sup_pi ||M_{kappa_pi}||.
```

So matching slices control every tripartite off-diagonal block after a
block-local gauge.

This proves that the matching-slice family is not merely a stress-test
detector; it reconstructs local inter-block Schur data. The global gluing
problem for pure skew symbols is solved by averaging these local gauges over
random disjoint triples; see
`agent-B/notes/pure-skew-matching-reconstruction-theorem.md`.

## Status

Known:

1. Gauge symbols have zero matching curvature.
2. Zero curvature implies gauge.
3. The triangular sign stress family is detected: a three-block matching slice
   recovers the ordinary triangular sign Schur multiplier up to a factor `1/2`.
4. Every tripartite off-diagonal block is reconstructed after a block-local
   average gauge by averaging matching curvature slices.
5. The local gauges glue by averaging over random disjoint triples, proving the
   pure skew reconstruction estimate dimension-free.

Status:

```text
The proved pure skew reconstruction integrates with the non-skew scalar part
through the Hermitian scalar corollary. The complex anti-linear and
quaternionic internal Peirce residuals are also controlled. Off-sector
leakage is globalized in
`agent-B/notes/off-sector-leakage-globalization-theorem.md`.
```

The pure complex skew standalone subproblem is closed, and the fixed-frame
sector-preserving matrix residual is closed after formal leakage removal.
