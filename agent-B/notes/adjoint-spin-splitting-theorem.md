# Adjoint Spin Splitting Theorem

This note closes the adjoint spin benchmark left open in
`agent-B/notes/spin-splitting-audit-2026-06-05.md`.

It does not prove the full Layer-1 error-reduction lemma. It proves the exact
right-inverse estimate for the adjoint module of a spin factor, in the
Euclidean-injective cochain norm. This is the concrete theorem Agent A's spin
route needed before it could be counted as more than numerical evidence.

## Setup

Let

```text
V = R 1 \oplus H
```

be the real spin factor over a finite-dimensional real Hilbert space `H`, with
product

```text
(alpha 1+x)(beta 1+y)
  = (alpha beta + <x,y>)1 + alpha y + beta x.
```

Use the Euclidean norm

```text
||(alpha,x)||_2 = (alpha^2+||x||_H^2)^{1/2}
```

and the associated injective cochain norms

```text
||h||_Fop = sup_{||z||_2<=1} ||h(z)||_2,
||f||_Fop = sup_{||z||_2,||w||_2<=1} ||f(z,w)||_2.
```

For the adjoint module, use the coboundary convention

```text
(d^1 h)(a,b) = a h(b) + h(a) b - h(ab).
```

This is the convention used in `agent-A/theory/01-error-reduction.md`.

## Theorem

For every finite-dimensional spin factor `V=R1+H`, there is an `O(H)`-equivariant
linear right inverse

```text
S_H : im(d^1) subset C^2(V,V) -> C^1(V,V)
```

such that

```text
d^1 S_H f = f,
||S_H f||_Fop <= 2 ||f||_Fop.
```

The constant is independent of `dim H`.

Consequently, using the spin norm comparison

```text
||x||_2 <= ||x||_ou <= sqrt(2)||x||_2,
```

this gives an adjoint spin order-unit splitting with universal constant

```text
||S_H||_{ou->ou} <= 4 sqrt(2).
```

## Proof

Write an arbitrary linear map `h:V->V` as

```text
h(1) = p 1 + a,
h(x) = <u,x> 1 + A x,        x in H,
```

where `p in R`, `a,u in H`, and `A in End(H)`.

For `x,y in H`, direct multiplication gives

```text
(d^1 h)(1,1) = p 1 + a,
(d^1 h)(1,x) = <a,x> 1 + p x,
```

and

```text
(d^1 h)(x,y)
 = (<x,Ay>+<y,Ax>-p<x,y>)1
   + <u,y>x + <u,x>y - a<x,y>.
```

Let `A=S+K`, with `S=S*` and `K=-K*`. The skew part `K` drops out. This is
exactly the derivation kernel `Der(V)=so(H)`. Thus a canonical complement to
the kernel is obtained by requiring `A` to be self-adjoint.

Now let `f in im(d^1)` and set `N=||f||_Fop`. Since `f=d^1 h_0` for some
`h_0`, the formulas above force the following data.

First,

```text
f(1,1) = p 1 + a.
```

Next, for `x,y in H`, let `B_f` be the scalar part of `f(x,y)`. Then

```text
B_f(x,y) = 2<x,Sy> - p<x,y>,
```

so define the self-adjoint operator `S_f` by

```text
2<x,S_f y> = B_f(x,y) + p<x,y>.
```

Finally, let `U_f` be the `H`-valued bilinear map

```text
U_f(x,y) = P_H f(x,y) + a<x,y>,
```

where `P_H` denotes projection onto the vector part. Exactness of `f` means
there is a unique `u_f in H` such that

```text
U_f(x,y) = <u_f,y>x + <u_f,x>y.
```

Uniqueness follows by setting `y=x`: if `u_f` gave zero, then
`2<u_f,x>x=0` for every `x`, hence `u_f=0`.

Define

```text
(S_H f)(1) = p 1 + a,
(S_H f)(x) = <u_f,x>1 + S_f x.
```

The formulas for `d^1 h` show immediately that `d^1 S_H f=f`. Linearity of
`S_H` on `im(d^1)` follows from uniqueness of the data `p,a,S_f,u_f`. The
construction is intrinsic under the orthogonal action on `H`, so it is
`O(H)`-equivariant.

It remains to bound the norm. Since `||1||_2=1`,

```text
||(p,a)||_2 = ||f(1,1)||_2 <= N,
```

so `|p|<=N` and `||a||<=N`.

The scalar bilinear form `B_f` has injective norm at most `N`. Hence

```text
||S_f|| <= (||B_f|| + |p|)/2 <= N.
```

For the vector parameter, take `||x||=1`. Then

```text
||U_f(x,x)|| <= ||P_H f(x,x)|| + ||a|| <= 2N.
```

But exactness gives

```text
U_f(x,x)=2<u_f,x>x,
```

so `|<u_f,x>|<=N` for every unit `x`, and therefore `||u_f||<=N`.

For `z=alpha 1+x` with `||z||_2<=1`, the scalar part of `(S_H f)(z)` satisfies

```text
|p alpha + <u_f,x>| <= (p^2+||u_f||^2)^{1/2} ||z||_2 <= sqrt(2)N.
```

The vector part satisfies

```text
||a alpha + S_f x||
  <= ||a|| |alpha| + ||S_f|| ||x||
  <= N(|alpha|+||x||)
  <= sqrt(2)N.
```

Combining scalar and vector parts gives

```text
||(S_H f)(z)||_2 <= 2N
```

for every unit `z`. Thus

```text
||S_H f||_Fop <= 2 ||f||_Fop.
```

This proves the theorem.

## Consequences And Caveats

1. The adjoint spin `Fop->Fop` gap is closed with a concrete constant. This
   validates the useful part of Agent A's spin-first proposal for the adjoint
   spin benchmark.
2. The proof does not use Hilbert-Schmidt singular values or Schur's lemma. It
   computes the actual injective-norm contractions.
3. This is still not the full `ER-norm` lemma. The full Layer-1 theorem needs
   arbitrary relevant `V`-modules, approximate-module bookkeeping, direct sums
   with mixed Peirce-`1/2` components, and the high-rank matrix families.
4. In the unital normalized error-reduction setting, where cochains vanish on
   unit slots, this proof specializes to `p=a=0`. The same bound then solves
   the scalar/vector spin defect by the `S_f,u_f` components above.
