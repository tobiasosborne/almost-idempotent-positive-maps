# Layer 1 Obligations After The Adjoint Benchmark

Date: 2026-06-05.

The finite-dimensional adjoint JB splitting corollary closes an important
diagnostic benchmark, but it is not yet the Kitaev-style error-reduction
lemma. This note records exactly what remains.

## What Is Now Controlled

For every finite-dimensional JB algebra `B`, the adjoint coboundary map has a
dimension-free inverse modulo derivations:

```text
dist(h,Der(B)) <= C||d^1h||_inj.
```

Equivalently,

```text
d^1 : C^1(B,B)/Der(B) -> im(d^1)
```

is an isomorphism with inverse norm at most `C`, uniformly over all
finite-dimensional `B`.

This is recorded in
`agent-B/notes/finite-dimensional-adjoint-jb-splitting-corollary.md`.

## Why This Is Not Error Reduction

Kitaev-style error reduction starts with a product perturbation

```text
x*y = x o y + theta(x,y)
```

on an approximate algebra already identified, at least approximately, with an
exact algebra `B`. The first-order multiplicativity defect `theta` is not
known to lie in `im(d^1)`. The Jordan identity only says that `theta` is an
approximate 2-cocycle:

```text
||d^2 theta|| <= C(epsilon + ||theta||^2)
```

with respect to the exact adjoint complex, after lower-order bookkeeping.

To correct the product one needs a 1-cochain `h` such that

```text
theta - d^1h
```

is quadratically smaller, or at least controlled by the ambient epsilon error.
The adjoint benchmark gives `h` only after a coboundary `d^1h` has already
been found. It does not by itself produce a nearby coboundary from an
approximate cocycle.

## Missing Exact-Complex Estimate

A sufficient exact-complex estimate would be a dimension-free constant `C`
such that for every finite-dimensional JB algebra `B` and every adjoint
2-cochain `theta`,

```text
dist(theta, im d^1) <= C ||d^2 theta||.
```

Since qualitative `H^2(B,B)=0` says `ker d^2=im d^1`, this is the quantitative
closed-range estimate for the next arrow in the cochain complex:

```text
C^1/ker d^1 --d^1--> C^2 --d^2--> C^3.
```

Equivalently, one needs a dimension-free bounded projection

```text
Pi_2 : C^2(B,B) -> im(d^1)
```

which is the identity on exact coboundaries and whose defect is controlled by
`d^2 theta`.

The exact-adjoint splitting corollary supplies the inverse for the first
arrow; it does not supply this projection or the inverse for the quotient
map induced by `d^2`.

## Conditional Newton Bookkeeping

The perturbative step after such estimates are available is recorded in
`agent-B/notes/next-arrow-to-newton-error-reduction.md`. For a unit-normalized
product perturbation

```text
x*y=x o y+theta(x,y)
```

on an exact JB algebra, the Jordan identity defect satisfies

```text
Def_*=Jtheta+O(||theta||^2).
```

If the exact adjoint complex has both:

```text
dist(theta,im d^1) <= K_2||Jtheta||,
||h|| <= K_1||d^1h||
```

in the relevant unit-normalized quotient sense, then a coordinate change
`T=I-h` improves the perturbation by

```text
delta -> C(K_1,K_2)(epsilon+delta^2).
```

Thus the Newton bookkeeping itself is no longer mysterious. The remaining
open work is to prove the required `K_1,K_2` estimates for the relevant global
or incremental modules, and to control approximate-module errors when the
codomain is not an exact adjoint `B`-module.

## Positive Commutative Scalar Test

The commutative scalar sectors do satisfy the next-arrow estimate. For
`B=R^m` and every scalar irreducible module

```text
l(x)=x_k        or        l(x)=(x_p+x_q)/2,
```

`agent-B/notes/commutative-scalar-cocycle-projection-theorem.md` proves

```text
dist(theta,im d^1) <= 12||Jtheta||,
```

where `Jtheta` is the two-variable linearized Jordan identity defect. The
proof uses the support-unit projection from the exact commutative splitting
and finite defect evaluations. Thus coordinate sectors and intrinsic Peirce
`1/2` mixed scalar sectors are not the next-arrow obstruction.

## Positive Normalized Spin Test

The normalized adjoint spin sector also satisfies a next-arrow estimate. In
`agent-B/notes/spin-normalized-cocycle-projection-reduction.md`, if
`V=R1 direct_sum H` and `theta(1,z)=0`, then writing

```text
theta(x,y)=c(x,y)1+D(x,y),        x,y in H,
```

the scalar part is an exact coboundary and the vector part obeys

```text
dist(D,{D_u}) <= (2sqrt(2)+2)||J_D||.
```

The proof uses the identity

```text
J_D(a,b)=<a,b>D(a,a)-<b,D(a,a)>a
```

and a dimension-free Hilbert lemma: a symmetric bilinear map whose quadratic
map `Q(x)=D(x,x)` is nearly radial is close to
`D_u(x,y)=<u,x>y+<u,y>x`.

Thus spin factors are not the next-arrow obstruction in the normalized adjoint
sector.

## Positive Diagonal-Frame Matrix Test

The fixed diagonal-frame module for `H_n(F)`, `F=R,C,H`, now satisfies the
next-arrow estimate. In
`agent-B/notes/diagonal-frame-matrix-next-arrow-walsh-target.md`, after
subtracting the algebraic support-unit coboundary, each off-diagonal residual
has the scalar half-sum form

```text
r_ij(x,y)
 = A_ij delta_x delta_y
   + B_ij(alpha_x delta_y+alpha_y delta_x)
   + delta_x U_ij(y^{ij})
   + delta_y U_ij(x^{ij})
   + W_ij(x^{ij},y^{ij}).
```

The coherent `A` and `B` coefficient matrices are recovered by ordinary
diagonal-sign averages of `Jtheta`. The one-tail map `U` is recovered by a
sparse-sign `{0,+-1}` average, avoiding edgewise Peirce summation. These
recoveries are all matrix-valued and contractive up to universal constants.
The tail-tail tensor

```text
W_ij(x^{ij},y^{ij}).
```

is recovered by a two-density sparse-sign identity. If

```text
Q_W(y)_ij=W_ij(y^{ij},y^{ij}),
```

then

```text
Q_W(y)=(64/3)T_{1/4}(y)-4T_{1/2}(y),
```

where `T_p` is an average of double diagonal commutators applied to
`J_W(xi+N_xi y,xi)-J_W(xi,xi)`. This gives

```text
dist(theta,im d^1) <= C||Jtheta||,
||theta-Pi_n theta|| <= C'||Jtheta||
```

for the bounded Rademacher projection `Pi_n`. Thus fixed diagonal-frame matrix
modules are not a next-arrow obstruction.

## Additional Robustness Still Needed

Even the exact-complex estimate above would not finish Layer 1. The actual
error-reduction lemma also needs:

1. **Approximate cocycle derivation.** The epsilon-JB axioms must imply the
   displayed bound on `d^2 theta` in order norm, with dimension-free
   constants, for the chosen identification with `B`.
2. **Approximate module actions.** During Newton iteration the codomain is not
   exactly the adjoint module of `B`; the module action itself is perturbed by
   `theta`. The homotopy/projection must tolerate those perturbations without
   dimension-dependent losses.
3. **Gauge control.** The derivation kernel is harmless for exact products,
   but iterative corrections require a canonical or at least stable gauge
   choice so that accumulated coordinate changes do not drift.
4. **Incremental assembly.** A global projection on all 2-cochains may still be
   hard. Kitaev avoids dimension growth by applying error reduction only to
   controlled subalgebras during merge/extend steps. The Jordan proof may need
   the same incremental strategy even though the adjoint global benchmark is
   now positive.
5. **Positive-map output.** For factorization, an abstract nearby JB algebra
   is not enough unless it is paired with a positivity-capable comparison or
   with the separate near-positive projection stability route.

## Next Sharp Target

The next mathematical target should be one of the following.

1. Prove the exact 2-cocycle projection estimate

   ```text
   dist(theta, im d^1) <= C||d^2theta||
   ```

   for adjoint JB cochains in order norm. The commutative scalar, normalized
   spin adjoint, and fixed diagonal-frame matrix module tests are now
   positive. The main remaining families are genuinely noncommutative
   matrix/internal Peirce sectors and their module variants. For high-rank
   matrix factors, `agent-B/notes/full-matrix-next-arrow-source-decomposition-target.md`
   decomposes the next target into source blocks: `D x D` is closed, while
   `D x E` cochain-level leakage and `E x E` Peirce curvature/matching remain
   open.

2. If the global estimate is false or hard, prove the corresponding estimate
   only for the finite-rank incremental configurations used in a Jordan
   frame/Peirce merge step.

3. Exhibit a family of adjoint 2-cochains with bounded `d^2theta` but growing
   distance to `im d^1`; this would force the incremental route and prevent
   another false global-averaging claim.

Until one of these is done, the exact-adjoint benchmark should be treated as a
major diagnostic success, not as the Layer 1 theorem.
