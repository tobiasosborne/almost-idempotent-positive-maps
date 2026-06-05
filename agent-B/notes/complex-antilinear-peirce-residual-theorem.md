# Complex Antilinear Peirce Residual Theorem

Date: 2026-06-05.

This note controls the anti-linear part of the fixed-frame sector-preserving
edge maps in `H_n(C)`. Together with
`agent-B/notes/hermitian-scalar-sector-reconstruction-corollary.md`, it closes
the fixed-frame sector-preserving edge-map residual for `H_n(C)`, modulo
diagonal frame-stabilizer derivations.

It does not address off-sector leakage globalization, and it does not address
the quaternionic internal Peirce maps.

## Setup

For ordered `a != b`, write

```text
X_ab(z)=zE_ab+conj(z)E_ba        (z in C).
```

Then `X_ba(z)=X_ab(conj(z))` and, for distinct `a,b,c`,

```text
X_ab(z) o X_bc(w) = (1/2)X_ac(zw).
```

Let `b_ab` be a Hermitian scalar symbol,

```text
b_ba=conj(b_ab),        b_aa=0.
```

Define the anti-linear sector-preserving operator

```text
B_b(e_a)=0,
B_b X_ab(z)=X_ab(b_ab conj(z)).
```

This is a well-defined real-linear map on `H_n(C)`.

For matrices over an ordered block `I x J`, write

```text
T_b(A)_{ij}=b_ij conj(A_ij).
```

This anti-linear Schur norm equals the ordinary Schur multiplier norm of
`b|_{I x J}`, because entrywise conjugation is an isometry for the operator
norm.

## Triangle Formula

For distinct `a,b,c`,

```text
d^1B_b(X_ab(z),X_bc(w))
 = (1/2)X_ac(
     b_ab conj(z)w + z b_bc conj(w) - b_ac conj(zw)
   ).
```

The key point is that the anti-linear source-edge coefficient `b_ab` can be
extracted from two matching tests.

Fix disjoint blocks `I,J,K` with `|J|=|K|`, and a matching `pi:J->K`. For
`A in M_{I,J}(C)`, let

```text
x_A=sum_{i in I,j in J} X_ij(A_ij),
y_1=sum_{j in J} X_{j,pi(j)}(1),
y_i=sum_{j in J} X_{j,pi(j)}(i).
```

The norms are

```text
||x_A||=||A||,        ||y_1||=||y_i||=1.
```

Let `F_1(A)` and `F_i(A)` be the `I x K` coefficient blocks of
`d^1B_b(x_A,y_1)` and `d^1B_b(x_A,y_i)`. The triangle formula gives

```text
2F_1(A)_{i,pi(j)}
 = (b_ij-b_{i,pi(j)})conj(A_ij)+b_{j,pi(j)}A_ij,
```

and

```text
2F_i(A)_{i,pi(j)}
 = i(b_ij+b_{i,pi(j)})conj(A_ij)-i b_{j,pi(j)}A_ij.
```

Therefore

```text
F_1(A)-iF_i(A)
```

has `I x K` coefficient

```text
b_ij conj(A_ij).
```

After relabelling columns by `pi`, every matching rectangular slice of
`T_b` has norm at most

```text
2||d^1B_b||_inj.
```

## Theorem

There is a universal constant `C` such that, for every `n`,

```text
||B_b||_{H_n(C)->H_n(C)} <= C ||d^1B_b||_inj.
```

One may take `C=40`.

## Proof

The cases `n<=1` are trivial. For `n=2`, the single edge coefficient is
controlled by square tests: choosing `z` with `z^2=b_ab/|b_ab|` gives

```text
d^1B_b(X_ab(z),X_ab(z))=2|b_ab|(e_a+e_b),
```

so `||B_b||=|b_ab|<=(1/2)||d^1B_b||_inj`.

Assume `n>=3`, and put

```text
m=floor(n/3).
```

Choose uniformly an ordered triple `(I,J,K)` of pairwise disjoint `m`-subsets.
Let `eta=eta_{I,J,K}` be the ordered symbol

```text
eta_ab=b_ab
```

if `a,b` lie in two different selected blocks, and `eta_ab=0` otherwise.

Each selected ordered rectangular block has anti-linear Schur norm at most
`2||d^1B_b||_inj` by the matching extraction above. Decomposing into the six
ordered rectangular block maps gives

```text
||B_eta|| <= 12||d^1B_b||_inj.
```

For fixed distinct `a,b`, the probability that `a,b` lie in two different
selected blocks is

```text
p=6m^2/(n(n-1)).
```

Thus

```text
E eta_ab=p b_ab.
```

By convexity of the real-linear operator norm,

```text
||B_b||
 = p^{-1}||B_{E eta}||
 <= p^{-1} E||B_eta||
 <= 40||d^1B_b||_inj,
```

since `p^{-1}<=10/3`.

This proves the theorem.

## Complex Fixed-Frame Corollary

Every real-linear edge map on `C` decomposes uniquely as

```text
A_ij z = a_ij z + b_ij conj(z).
```

For a well-defined real-linear map on Hermitian matrices, both ordered symbols
are Hermitian:

```text
a_ji=conj(a_ij),        b_ji=conj(b_ij).
```

The complex-linear part `a_ij z` is a scalar Hermitian Schur/connection
residual. The anti-linear part is the residual controlled above. In a general
sector-preserving map the two parts must first be separated at the level of
the defect; this costs only an absolute factor.

Let `S_A` be a sector-preserving map with `S_A(e_i)=0` and

```text
S_A X_ij(z)=X_ij(a_ij z+b_ij conj(z)),
```

and set `delta=||d^1S_A||_inj`. For a matching `pi:J->K`, define `F_1(A)` and
`F_i(A)` as above, but with `B_b` replaced by `S_A`. If

```text
c_{i,j,pi(j)}=a_ij+a_{j,pi(j)}-a_{i,pi(j)},
```

then

```text
G(A):=F_1(A)-iF_i(A)
```

has coefficient

```text
G(A)_{i,pi(j)}=c_{i,j,pi(j)}A_ij+b_ij conj(A_ij).
```

The finite phase projections

```text
P_lin G(A)  = (G(A)-iG(iA))/2,
P_anti G(A) = (G(A)+iG(iA))/2
```

give respectively

```text
P_lin G(A)_{i,pi(j)}=c_{i,j,pi(j)}A_ij,
P_anti G(A)_{i,pi(j)}=b_ij conj(A_ij).
```

Since `||G||<=2delta`, both projected matching slices have norm at most
`2delta`.

The square terms similarly separate the real scalar edge coefficient. For
`x_z=X_ab(z)` with `|z|=1`,

```text
d^1S_A(x_z,x_z)
 =2 Re(conj(a_ab)+conj(b_ab)z^2)(e_a+e_b).
```

Averaging the tests `z=1` and `z=i` gives

```text
sup_{a != b}|Re a_ab| <= (1/2)delta.
```

Thus the scalar Hermitian corollary applies with matching-slice supremum
`S<=2delta` and real edge term `E<=(1/2)delta`, and gives

```text
dist(M_a,Der_diag) <= 84delta.
```

The anti-linear random matching argument above, using the projected matching
slices `P_anti G`, gives

```text
||B_b|| <= 40delta
```

for `n>=3`. For `n<=2`, after removing the diagonal derivation gauge
`i Im(a_ab)z`, the residual is `u z+b conj(z)`. The square tests with
`z in {1,i,exp(pi i/4),exp(3pi i/4)}` control `u`, `Re b`, and `Im b` by
an absolute multiple of `delta`, so the same conclusion holds after enlarging
the universal constant if necessary.

Consequently, after the diagonal gauge and after formal removal of off-sector
leakage, the fixed-frame sector-preserving edge maps for `H_n(C)` are
dimension-free controlled modulo diagonal frame-stabilizer derivations by
their exact adjoint coboundary. One crude bound from the displayed estimates
is

```text
dist(S_A,Der_diag) <= 124 ||d^1S_A||_inj.
```

The quaternionic internal edge-map benchmark is controlled separately in
`agent-B/notes/quaternionic-internal-peirce-residual-theorem.md`, and
off-sector leakage is globalized in
`agent-B/notes/off-sector-leakage-globalization-theorem.md`.
