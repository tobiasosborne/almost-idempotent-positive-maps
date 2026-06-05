# Quaternionic Internal Peirce Residual Theorem

Date: 2026-06-05.

This note proves the fixed-frame sector-preserving internal edge-map estimate
for `H_n(H)`, modulo diagonal frame-stabilizer derivations, after formal
off-sector leakage removal. It uses finite quaternionic coefficient extraction
and the same random matching reconstruction mechanism used in the scalar
Schur notes.

Off-sector leakage is solved separately in
`agent-B/notes/off-sector-leakage-globalization-theorem.md`.

## Setup

Let

```text
J=H_n(H),        n>=3.
```

For ordered `a != b`, write

```text
X_ab(z)=zE_ab+conj(z)E_ba        (z in H).
```

Then, for distinct `a,b,c`,

```text
X_ab(z) o X_bc(w) = (1/2)X_ac(zw).
```

Let `S_A` be fixed-frame sector-preserving:

```text
S_A(e_a)=0,
S_A X_ab(z)=X_ab(A_ab z),
```

where `A_ab in End_R(H)` and

```text
A_ba(z)=conj(A_ab(conj(z))).
```

Set

```text
delta=||d^1S_A||_inj.
```

The triangle defect is

```text
C_A(a,b,c)(z,w)
 = A_ab(z)w + z A_bc(w) - A_ac(zw),
```

with

```text
d^1S_A(X_ab(z),X_bc(w))=(1/2)X_ac(C_A(a,b,c)(z,w)).
```

Diagonal frame-stabilizer derivations have the form

```text
G_u,ab(z)=u_a z - z u_b,        u_a in Im H.
```

## Internal Decomposition

Use the real decomposition

```text
End_R(H)=R Id direct_sum L_{Im H} direct_sum R_{Im H} direct_sum M,
M=span_R{L_r R_s : r,s in {i,j,k}}.
```

Here `L_rR_s(z)=r z s`. The projections onto these four summands are fixed
finite-dimensional real-linear maps. They can be written as finite averages
of pre- and post-compositions by left and right multiplication by unit
quaternions, so applying them entrywise to rectangular Peirce blocks changes
operator norms by at most an absolute constant.

Norms of rectangular operator-valued Schur maps are taken on quaternionic
Hilbert-space matrices. Entrywise pre- or post-composition by fixed unit
quaternion multiplications is implemented by diagonal unitary multiplication
on the rectangular block, hence is isometric. Therefore every finite twirl
projection used below has a universal operator-norm bound when applied
entrywise to rectangular blocks.

The scalar `R Id` component is exactly the real scalar Schur residual and is
controlled by
`agent-B/notes/real-symmetric-matching-reconstruction-theorem.md`. The mixed
component `M` has no gauge. The `L_{Im H} direct_sum R_{Im H}` component
contains exactly the diagonal gauge directions.

Because of the Hermitian compatibility, the left/right component can be
written with a single directed imaginary symbol `p_ab in Im H`:

```text
A_ab^{LR}(z)=p_ab z - z p_ba.
```

The gauge condition is `p_ab=u_a`.

## Matching Extraction

Let `I,J,K` be disjoint equal-size blocks and let `pi:J->K` be a matching.
For `w in U={1,i,j,k}` and a rectangular quaternionic matrix `Z in M_{I,J}(H)`,
define

```text
x_Z=sum_{i in I,j in J} X_ij(Z_ij),
y_w=sum_{j in J} X_{j,pi(j)}(w).
```

Then `||x_Z||=||Z||`: in the block decomposition
`I direct_sum J`, `x_Z` is the self-adjoint quaternionic block matrix
`[[0,Z],[Z^*,0]]`. Also `||y_w||=1`. The `I x K` output block of
`2d^1S_A(x_Z,y_w)` is the operator-valued rectangular Schur map

```text
T_w(Z)_{i,pi(j)}=C_A(i,j,pi(j))(Z_ij,w),
```

so

```text
||T_w|| <= 2delta.
```

### Mixed Component

Define

```text
G=(1/4) sum_{w in U} R_{conj(w)} T_w.
```

For each matched edge `(i,j,pi(j))`,

```text
G_ij = A_ij + R_{r_{j,pi(j)}} - P_L(A_{i,pi(j)})
```

for a quaternion `r_{j,pi(j)}` depending on the middle edge, where `P_L` is
the projection onto left multiplication. Therefore the mixed projection kills
the middle and target contaminations:

```text
P_M G_ij = P_M A_ij.
```

Thus every matching rectangular slice of the mixed component is controlled by
`C delta`.

### Left-Right Connection Component

For the left/right component

```text
A_ab^{LR}(z)=p_ab z - z p_ba,
```

write `k=pi(j)` and set

```text
a=p_ij-p_ik,
b=-p_ji+p_jk,
c=-p_kj+p_ki.
```

Then

```text
T_w(z)=a z w + z b w + z w c.
```

Postmultiply by `conj(w)`:

```text
H_w=R_{conj(w)}T_w,
H_w(z)=a z + z b + z(w c conj(w)).
```

Averaging over `U` kills the imaginary conjugation orbit:

```text
H=(1/4)sum_{w in U}H_w=L_a+R_b.
```

The standard twirl projections

```text
P_L(T)=(1/4)sum_{u in U} R_{conj(u)} T R_u,
P_R(T)=(1/4)sum_{u in U} L_{conj(u)} T L_u
```

extract the left and right imaginary summands. Indeed, `P_L` fixes
`L_{Im H}` and kills `R_{Im H}` and `M`, while `P_R` fixes `R_{Im H}` and
kills `L_{Im H}` and `M`. Therefore

```text
P_L(H)=L_{p_ij-p_ik},
P_R(H)=R_{-p_ji+p_jk}.
```

Also `H_1-H=R_{-p_kj+p_ki}`. Hence finite matching tests recover the
rectangular Schur slices of all row differences

```text
p_ij-p_ik
```

with norm at most `C delta`.

## Random Reconstruction Lemmas

We use two elementary random matching reconstructions.

### Direct Symbol Reconstruction

Let `B_ab` be any ordered operator-valued symbol. If every matching
rectangular slice of `B` has norm at most `S`, then

```text
||M_B|| <= 20S.
```

Indeed, choose uniformly an ordered triple `(I,J,K)` of disjoint
`m=floor(N/3)` subsets. Let `eta_ab=B_ab` when `a,b` lie in two different
selected blocks, and `eta_ab=0` otherwise. Each `eta` is a sum of six
controlled rectangular block maps, so `||M_eta||<=6S`. Since

```text
E eta_ab = p B_ab,        p=6m^2/(N(N-1)),        p^{-1}<=10/3,
```

convexity gives the estimate.

### Row-Gauge Reconstruction

Let `P_ab` be an ordered operator-valued symbol. If every matching
rectangular slice

```text
P_ij-P_{i,pi(j)}
```

has norm at most `S`, then there are row constants

```text
gamma_a=(N-1)^{-1}sum_{c != a} P_ac
```

such that

```text
||M_{P_ab-gamma_a}|| <= 20S.
```

The proof is the same random triple averaging. For selected ordered blocks and
third block `C(a,b)`, put

```text
eta_ab=|C(a,b)|^{-1}sum_{c in C(a,b)}(P_ab-P_ac)
```

on different selected blocks and zero otherwise. Each ordered rectangular
block is an average over matching row-difference slices. For fixed `a != b`,

```text
E[eta_ab | a,b selected in different blocks]
 = P_ab - (sum_{c != a,b}P_ac)/(N-2)
 = ((N-1)/(N-2))(P_ab-gamma_a).
```

After multiplying by the same selection probability `p`, the inverse scalar
is bounded by `p^{-1}`, hence at most `10/3`; the six-block decomposition
again gives the displayed constant.

## Theorem

There is a universal constant `C` such that

```text
dist(S_A,{G_u}) <= C ||d^1S_A||_inj
```

for all fixed-frame sector-preserving `S_A` on `H_n(H)`, `n>=3`.

## Proof

We separate the components in an order that is visible from the full defect.
All losses below are absorbed into the universal constant.

First apply the mixed extraction above directly to the full matching defect.
It gives matching rectangular slices of `P_M A_ij` bounded by `C delta`.
The direct random reconstruction therefore gives

```text
||S_A^M|| <= C delta.
```

Subtract this controlled mixed primitive. Since `||d^1T||<=3||T||` for every
bounded primitive `T`, the new residual has defect norm at most `C delta`.

Next project the residual onto the scalar `R Id` component. Finite twirls
extract the scalar matching curvature slices and the scalar square terms from
the residual defect with norm at most `C delta`. The scalar quaternionic
amplification lemma says that a real scalar Schur multiplier acting on
quaternionic matrices has norm bounded, up to a universal constant, by the
corresponding real or complex all-matrix Schur norm. Equivalently, under the
standard complex `2 x 2` representation of quaternionic matrices, it is a
fixed finite amplification of the same scalar Schur multiplier. Hence the
real symmetric matching reconstruction theorem gives

```text
||S_A^{scal}|| <= C delta.
```

Subtract the scalar component as well. The remaining residual lies in
`L_{Im H} direct_sum R_{Im H}` and has defect norm at most `C delta`.
For this residual the left/right extraction gives row-difference slices of
`L_{p_ab}` bounded by `C delta`. The row-gauge reconstruction gives imaginary
quaternions `u_a` such that

```text
||M_{L_{p_ab-u_a}}|| <= C delta.
```

Hermitian compatibility gives the corresponding right component as the
transpose field, so

```text
||M_{R_{-p_ba+u_b}}|| <= C delta.
```

Therefore

```text
S_A^{LR}-G_u
```

has norm at most `C delta`.

Adding back the controlled mixed and scalar components proves the theorem.

## Consequence

After the fixed-frame diagonal gauge and after formal removal of off-sector
leakage, the sector-preserving edge-map residual is controlled for
`H_n(R)`, `H_n(C)`, and `H_n(H)`.

Off-sector leakage is globalized in
`agent-B/notes/off-sector-leakage-globalization-theorem.md`. The assembled
matrix-factor exact-adjoint result is recorded in
`agent-B/notes/matrix-factor-exact-adjoint-splitting-theorem.md`.
