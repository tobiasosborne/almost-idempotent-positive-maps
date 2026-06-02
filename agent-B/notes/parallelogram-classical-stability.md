# Bounded-Coordinate Cancellation For Classical Projection Stability

This note corrects and sharpens the first non-simplex row-polytope analysis.
The parallelogram geometry is not a new nontrivial stability case: for small
near-positivity defect it cannot occur at all.

The useful result is a cancellation lemma. Bounded affine coordinate witnesses
force selected signed rows to concentrate on disjoint state sets. Therefore
any linear combination of those rows has almost the full `l1` norm of its
coefficient vector. In particular, an exact parallelogram identity is
impossible for small `delta`.

This incorporates Popper's sidecar observation.

## Setup

Let `P` be an `n x n` real matrix with

```text
P1=1,        P^2=P.
```

Write `p_i` for the rows of `P`, viewed as signed probability vectors, and
assume

```text
neg(p_i)=sum_j max(-p_i(j),0) <= delta        for every i.
```

Let

```text
K=conv{p_i}.
```

## Binary-Coordinate Cancellation Lemma

Let `A` be a finite label set. Suppose we are given rows

```text
r_a        (a in A)
```

of `P`, affine functions

```text
s_1,...,s_m:K -> [0,1],
```

and distinct binary code words

```text
sigma(a) in {0,1}^m
```

such that

```text
s_k(r_a)=sigma_k(a)        for all a in A and 1<=k<=m.
```

Set `tau=sqrt(delta)` and assume `m tau<1/8`. Define the code cell

```text
U_a={j: |s_k(p_j)-sigma_k(a)|<=tau for every k=1,...,m}.
```

Then the sets `U_a` are pairwise disjoint, and for each `a` there is a
probability measure `pi_a` supported on `U_a` such that

```text
||r_a-pi_a||_1 <= C m tau.                       (BC1)
```

Consequently, for any real coefficients `c_a`,

```text
|| sum_a c_a r_a ||_1
  >= (1-C m tau) sum_a |c_a|.                    (BC2)
```

The constant `C` is universal. The estimate is meaningful for fixed `m`; it
is not dimension-free if the number of coordinate bits grows.

### Proof

Fix `a` and a coordinate `k`. If `sigma_k(a)=0`, apply idempotency

```text
r_a P=sum_j (r_a)_j p_j=r_a
```

to the affine function `s_k`. Since `s_k(r_a)=0` and `0<=s_k<=1`,

```text
sum_j (r_a)^+_j s_k(p_j) <= neg(r_a) <= delta.
```

Hence `(r_a)^+` puts at most `delta/tau=tau` mass on
`{j:s_k(p_j)>tau}`.

If `sigma_k(a)=1`, use `1-s_k` instead and get the same bound on
`{j:s_k(p_j)<1-tau}`. A union bound over the `m` coordinates gives

```text
(r_a)^+(U_a^c) <= m tau.                         (BC3)
```

Define

```text
pi_a=(r_a)^+|_{U_a} / ||(r_a)^+|_{U_a}||_1.
```

The denominator is at least `1-O(m tau)`, because each `r_a` has total mass
`1` and negative mass at most `delta`. The usual truncation estimate for a
signed probability gives `(BC1)`.

If `a != b`, the code words differ in some coordinate `k`; the inequalities
defining `U_a` and `U_b` are then incompatible for `tau<1/2`. Thus the
supports of the `pi_a` are disjoint. Therefore

```text
|| sum_a c_a pi_a ||_1 = sum_a |c_a|.
```

Using `(BC1)` and the triangle inequality proves `(BC2)`.

## Coordinate-Rectangle Cancellation Lemma

Assume there are affine functions

```text
s,t:K -> [0,1]
```

and four rows `r_{ab}` of `P`, indexed by `a,b in {0,1}`, such that

```text
s(r_{ab})=a,        t(r_{ab})=b.
```

Set `tau=sqrt(delta)`, and assume `tau<1/4`. Then there are probability
measures `pi_{ab}` supported on the disjoint sets

```text
U_{ab}={j: |s(p_j)-a|<=tau and |t(p_j)-b|<=tau}
```

such that

```text
||r_{ab}-pi_{ab}||_1 <= C tau.
```

Consequently,

```text
||r_{00}+r_{11}-r_{10}-r_{01}||_1 >= 4-C tau.      (RC1)
```

This is the binary-coordinate lemma with `m=2` and coefficients
`+1,-1,-1,+1`. The direct proof below is included because it is the cleanest
way to see the parallelogram obstruction.

## Direct Proof Of The Rectangle Case

For any row `r` of `P`, idempotency gives

```text
rP=sum_j r_j p_j=r.
```

If `phi:K->[0,1]` is affine, applying `phi` gives

```text
sum_j r_j phi(p_j)=phi(r).                         (R2)
```

For `r_{00}`, use `(R2)` with `phi=s` and `phi=t`. Since
`s(r_{00})=t(r_{00})=0` and `0<=s,t<=1`,

```text
sum_j (r_{00})^+_j s(p_j) <= neg(r_{00}) <= delta,
sum_j (r_{00})^+_j t(p_j) <= neg(r_{00}) <= delta.
```

Thus `(r_{00})^+` puts at most `2delta/tau=2tau` mass outside `U_{00}`.

For the other corners, use `s` or `1-s` and `t` or `1-t` according to the
corner. The same argument gives

```text
(r_{ab})^+(U_{ab}^c) <= 2 tau.                    (R3)
```

Define

```text
pi_{ab}=(r_{ab})^+|_{U_{ab}} / ||(r_{ab})^+|_{U_{ab}}||_1.
```

The denominator is at least `1-O(tau)`, because each `r_{ab}` has total mass
`1` and negative mass at most `delta`. The standard truncation estimate for a
signed probability now gives

```text
||r_{ab}-pi_{ab}||_1 <= C tau.
```

Indeed, if a signed probability `mu` has negative mass `c` and positive mass
`b` outside a retained support, then its distance from the normalized positive
restriction to that support is at most `C(b+c)` while `b+c<1/2`.

The sets `U_{ab}` are pairwise disjoint for `tau<1/2`. Therefore the signed
measure

```text
pi_{00}+pi_{11}-pi_{10}-pi_{01}
```

has mutually singular positive and negative parts, each of total mass `2`.
Hence its `l1` norm is exactly `4`. The triangle inequality gives `(RC1)`.

## Corollary: No Small-Delta Parallelogram Row Polytope

Suppose `K=conv{p_i}` is exactly a parallelogram with vertices, among the rows,

```text
r_{00}, r_{10}, r_{01}, r_{11},
```

labelled so that

```text
r_{00}+r_{11}=r_{10}+r_{01}.
```

The affine parallelogram coordinates `s,t:K->[0,1]` satisfy the hypotheses of
the cancellation lemma. The parallelogram identity makes the left side of
`(RC1)` equal to `0`, a contradiction once `delta` is sufficiently small.

Therefore a near-positive exact signed affine retraction with small `delta`
cannot have a genuine parallelogram as its row polytope. The formal stability
statement for exact parallelogram row polytopes is true but vacuous in the
small-defect regime.

## Corollary: No Bounded Product-Of-Simplexes Vertex Geometry

The same argument rules out a broader fixed-complexity class.

Suppose the vertex rows of `K` are labelled by tuples

```text
a=(a_1,...,a_q),        a_l in {1,...,N_l},
```

and that there are affine coordinate functions

```text
lambda_{l,b}:K -> [0,1]        (1<=l<=q, 1<=b<=N_l)
```

such that, on the labelled vertex rows,

```text
lambda_{l,b}(r_a)=1_{a_l=b}.                    (P1)
```

This is exactly the vertex-coordinate situation for a polytope affinely
isomorphic to a product

```text
Delta_{N_1-1} x ... x Delta_{N_q-1},
```

with the `lambda_{l,b}` pulled back from the simplex factors.

Let

```text
m=sum_l N_l.
```

The binary-coordinate cancellation lemma applies to all vertex rows, using
the `m` coordinates `lambda_{l,b}`. Hence, for all coefficients `c_a`,

```text
||sum_a c_a r_a||_1
  >= (1-C m sqrt(delta)) sum_a |c_a|.            (P2)
```

If at least two factors are nontrivial, the product polytope has exact affine
dependencies among its vertices. For example, fixing all other coordinates
and choosing two different values in two factors gives a rectangle relation

```text
r_{...b...d...}+r_{...b'...d'...}
 = r_{...b...d'...}+r_{...b'...d...}.            (P3)
```

Taking the coefficients in `(P3)` in `(P2)` gives a contradiction once
`m sqrt(delta)` is small enough.

Therefore a near-positive exact signed affine retraction cannot have, at
small `delta`, a fixed-complexity non-simplex product-of-simplexes row
polytope with the factor coordinates bounded on all of `K`.

## Consequence For The Non-Simplex Program

The basic parallelogram affine dependence

```text
r_{00}+r_{11}=r_{10}+r_{01}
```

is not a surviving obstruction. If bounded `[0,1]` coordinate witnesses exist,
near-positivity and idempotency force the four corners onto disjoint recurrent
slices, making the alternating dependence macroscopic rather than small.

Thus a genuine remaining non-simplex obstruction must hide its affine
dependencies in ill-conditioned geometry: the relevant coordinate functions
cannot be uniformly bounded on all of `K`, or the dependency must decompose
through many factors/facets in a way that risks accumulating constants.

This sharpens the approximate-simplexity gap. The missing theorem can be
phrased as an angle-free bounded-coordinate/cancellation principle: every
macroscopic non-simplex affine dependence in a nearly positive exact
retraction either admits bounded coordinate witnesses and is impossible, or is
mergeable at `O(sqrt(delta))` scale into a lower-complexity recurrent
description.
