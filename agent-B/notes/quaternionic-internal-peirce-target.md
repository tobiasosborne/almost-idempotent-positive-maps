# Quaternionic Internal Peirce Target

Date: 2026-06-05.

This note records the fixed-frame sector-preserving edge-map target for
`H_n(H)` after the scalar real/complex Schur residuals and the complex
anti-linear residual have been controlled.

The target formulated here is now proved in
`agent-B/notes/quaternionic-internal-peirce-residual-theorem.md`. This file is
kept as the audit trail that identified the coefficient-extraction problem.

## Setup

For ordered `a != b`, write

```text
X_ab(z)=zE_ab+conj(z)E_ba        (z in H).
```

Then, for distinct `a,b,c`,

```text
X_ab(z) o X_bc(w) = (1/2)X_ac(zw).
```

Let a fixed-frame sector-preserving primitive have

```text
S_A(e_a)=0,
S_A X_ab(z)=X_ab(A_ab z),
```

where each `A_ab` is a real-linear endomorphism of `H`, with the Hermitian
compatibility condition

```text
A_ba(z)=conj(A_ab(conj(z))).
```

For distinct `a,b,c`, the internal Peirce curvature is the bilinear map

```text
C_A(a,b,c)(z,w)
 = A_ab(z)w + z A_bc(w) - A_ac(zw).
```

The coboundary satisfies

```text
d^1S_A(X_ab(z),X_bc(w))=(1/2)X_ac(C_A(a,b,c)(z,w)).
```

## Gauge

The diagonal frame-stabilizer derivations come from

```text
U=diag(u_a),        u_a in Im H,
```

and act by

```text
G_u,ab(z)=u_a z - z u_b.
```

Thus the fixed-frame target is

```text
dist(S_A,{G_u}) <= C ||d^1S_A||_inj
```

with `C` independent of `n`.

This target is after formal removal of off-sector leakage. It would not by
itself prove the full high-rank matrix benchmark unless the leakage
globalization problem is also solved.

## Endomorphism Decomposition

Use the real basis

```text
End_R(H)=span_R { L_r R_s : r,s in {1,i,j,k} },
```

where `L_r R_s(z)=r z s`. This separates the finite-dimensional internal
problem into concrete sectors:

1. `L_1 R_1`, the real scalar Schur multiplier sector, already controlled by
   `agent-B/notes/real-symmetric-matching-reconstruction-theorem.md`.
2. `L_u R_1` and `L_1 R_v`, `u,v in Im H`, which contain the diagonal
   frame-stabilizer gauges `u_a z-z u_b` and form the left-right connection
   subtarget below.
3. `L_u R_v`, `u,v in Im H`, a nine-dimensional mixed tensor sector with no
   gauge directions. This is analogous to the complex anti-linear sector and
   is directly extracted in
   `agent-B/notes/quaternionic-internal-peirce-residual-theorem.md`.

## Skew Left-Right Subtarget

A particularly important quaternionic subfamily is

```text
A_ab(z)=p_ab z + z q_ab,        p_ab,q_ab in Im H.
```

The gauge form is

```text
p_ab=u_a,        q_ab=-u_b.
```

Its curvature expands as

```text
C_A(a,b,c)(z,w)
 = (p_ab-p_ac)zw
   + z(q_ab+p_bc)w
   + zw(q_bc-q_ac).
```

Thus the natural matching-slice data should recover the three component
symbols

```text
p_ab-p_ac,        q_ab+p_bc,        q_bc-q_ac
```

in ordinary Schur multiplier norm. If those can be extracted with universal
constants, the random matching reconstruction methods used for the real,
pure-skew, and complex anti-linear sectors plausibly apply to this subtarget.

## Coefficient-Extraction Problem

For disjoint blocks `I,J,K` and a matching `pi:J->K`, set

```text
y_w=sum_{j in J} X_{j,pi(j)}(w),
x_Z=sum_{i in I,j in J} X_ij(Z_ij).
```

The `I x K` output block of `2d^1S_A(x_Z,y_w)` has coefficients

```text
A_ij(Z_ij)w + Z_ij A_{j,pi(j)}(w) - A_{i,pi(j)}(Z_ij w).
```

For `F=C`, the phase choices `w=1,i`, plus the projections
`G(Z) -> (G(Z) +/- iG(iZ))/2`, isolate either the scalar curvature slice or
the anti-linear source-edge slice. For `F=H`, the analogous finite extraction
is not automatic because the target-edge term

```text
A_{i,pi(j)}(Z_ij w)
```

mixes the right multiplication by `w` through an arbitrary real-linear
endomorphism of `H`.

The immediate audit target was therefore:

```text
Given the family of maps
Z -> A_ij(Z)w + Z A_{j,pi(j)}(w) - A_{i,pi(j)}(Zw)
for a fixed finite set of unit quaternions w,
can one recover, modulo gauge, the rectangular Schur slice of A_ij with a
universal constant?
```

This audit is discharged in
`agent-B/notes/quaternionic-internal-peirce-residual-theorem.md`: finite
twirls extract the mixed `L_{Im}R_{Im}` component directly, and extract the
left/right gauge-invariant row differences in the `L_{Im} direct_sum R_{Im}`
component.

## Current Status

The real scalar, complex scalar, pure diagonal-skew, complex anti-linear, and
quaternionic internal Peirce mechanisms are controlled at the fixed-frame
sector-preserving level, after formal leakage removal.

The other independent high-rank matrix target is coherent operator-norm
globalization of the pointwise off-sector leakage estimate from
`agent-B/notes/fixed-frame-peirce-matrix-reduction.md`.
