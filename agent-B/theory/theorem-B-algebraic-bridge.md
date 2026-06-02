# Theorem B Draft: Algebraic Bridge For Almost-Idempotent UP Maps

This is a formalized version of `agent-B/notes/layer2-null-ideal-sqrt.md`.
It proves only the algebraic bridge to an approximate JB order-unit algebra.
It does **not** prove exact UP factorization maps.

## Theorem

There are universal constants `eta0,C` with the following property.

Let `H` be finite-dimensional and let `V=B(H)_sa` with order-unit/operator
norm and Jordan product

```text
x o y = (xy+yx)/2.
```

Let `Phi:V->V` be unital positive and

```text
||Phi^2-Phi|| <= eta <= eta0.
```

Let

```text
P = theta(2Phi-I)
```

be the spectral idempotent associated to the spectral cluster near `1`, and set

```text
A=Im P,        A_+=A cap V_+,        a*b=P(a o b),        a,b in A.
```

Then `(A,*,1,A_+ inherited from V)` is an `epsilon`-JB order-unit algebra with

```text
epsilon <= C sqrt(eta).
```

In particular, for `a,b in A`,

```text
1*a=a,
||a*b|| <= (1+C eta)||a||||b||,
a*a >= -C eta ||a||^2 1,
||a*a|| >= (1-C eta)||a||^2,
||((a*a)*b)*a - (a*a)*(b*a)|| <= C sqrt(eta)||a||^3||b||.
```

## Proof

All implicit constants below are universal. We decrease `eta0` whenever needed
to absorb an `O(eta)` term into an `O(sqrt(eta))` term.

Write

```text
delta = ||P-Phi||.
```

First we record the spectral estimate. Since `Phi` is unital positive, it is a
contraction for the order-unit norm:

```text
||Phi||=1.
```

Set `S=2Phi-I` as an element of the Banach algebra `End(V)`. Then

```text
||S|| <= 3,        ||S^2-I|| = 4||Phi^2-Phi|| <= 4 eta.
```

For `eta0` small, define

```text
R=(S^2)^(-1/2)
```

by the convergent binomial series around `I`, and set

```text
sgn(S)=SR,        P=(I+sgn(S))/2.
```

This agrees with the spectral idempotent `theta(2Phi-I)` for the spectral
cluster near `1`. Since `R` is a function of `S^2`,

```text
sgn(S)^2=S^2 R^2=I,
```

so `P^2=P`. Also `(S^2-I)1=0`, hence `R1=1`, `sgn(S)1=1`, and `P(1)=1`.
Finally,

```text
||R-I|| <= C eta,
```

and therefore

```text
delta = ||P-Phi||
      = 1/2 ||sgn(S)-S||
      <= 1/2 ||S||||R-I||
      <= C eta,

||P|| <= ||Phi||+delta <= 1+C eta.
```

Also `P` is `delta`-positive:

```text
x>=0  =>  P(x) >= -delta ||x|| 1.
```

Indeed `Phi(x)>=0` and `||P(x)-Phi(x)||<=delta||x||`.

### Lemma 0: Exact Order-Unit Structure On `A`

The order-unit part of the claimed epsilon-JB object is exact. Since `P(1)=1`,
the range `A=Im P` is a real linear subspace of `V` containing `1`. Give it
the inherited cone

```text
A_+ = A cap V_+.
```

For every `a in A`,

```text
-||a|| 1 <= a <= ||a|| 1
```

in `V`, so `1` is an order unit for `A`. The cone is Archimedean because
`V_+` is closed: if `a+epsilon 1 in A_+` for every `epsilon>0`, then
`a>=0` in `V`, hence `a in A_+`. Therefore `(A,A_+,1)` is an order-unit
space.

Moreover its order-unit norm is exactly the ambient operator norm on
self-adjoint matrices:

```text
||a||_{ou,A}
 = inf{t>0: -t1<=a<=t1}
 = ||a||_{B(H)}.
```

Thus no approximate norm/order structure is being introduced; all approximate
estimates below concern only the product `*`.

### Standard Order Estimates Used Below

We use only the following order facts, none of which requires complete
positivity.

1. Jordan-Schwarz for unital positive maps on self-adjoint elements:

   ```text
   Phi(x)^2 <= Phi(x^2),        x=x^*.
   ```

2. Cauchy-Schwarz for every positive functional `omega` on `B(H)_sa`:

   ```text
   |omega(x o y)|^2 <= omega(x^2) omega(y^2).
   ```

3. Norm monotonicity in the positive cone: if `0<=x<=y`, then
   `||x||<=||y||`.

4. For self-adjoint `x`,

   ```text
   ||x|| = sup_rho |rho(x)|,
   ```

   where the supremum is over states `rho` on `B(H)`.

5. If `x,y` are self-adjoint and `||x-y||<=epsilon`, then

   ```text
   x >= y-epsilon 1        and        x <= y+epsilon 1.
   ```

### Lemma 1: Easy JB Axioms

For `a,b in A`, the unit and commutativity are exact. The product bound follows
from `||P||<=1+C eta` and `||a o b||<=||a||||b||`.

For squares,

```text
a*a=P(a^2) >= -delta ||a||^2 1.
```

For the norm lower bound, since `a=P(a)`,

```text
||Phi(a)-a|| <= delta ||a||.
```

Jordan-Schwarz gives `Phi(a^2)>=Phi(a)^2`, hence

```text
||Phi(a^2)|| >= ||Phi(a)^2|| = ||Phi(a)||^2
              >= (1-C delta)||a||^2.
```

Since `||P(a^2)-Phi(a^2)||<=delta||a||^2`,

```text
||a*a||=||P(a^2)|| >= (1-C eta)||a||^2.
```

Thus only the Jordan identity remains.

### Lemma 2: First Insertion Estimate

For every state `rho` on `B(H)` set

```text
omega = rho o Phi,
||x||_omega^2 = omega(x^2).
```

Since `Phi` is positive, `omega` is a positive functional and this is a
seminorm on `V`.

Then for all `x in V`,

```text
||Px||_omega^2 <= ||x||_omega^2 + C eta ||x||^2.
```

Proof:

```text
rho Phi((Px)^2)
 <= rho Phi((Phi x)^2) + C eta ||x||^2
 <= rho Phi^2(x^2) + C eta ||x||^2
 <= rho Phi(x^2) + C eta ||x||^2.
```

The first inequality uses `||Px-Phi x||<=delta||x||` and
`||y^2-z^2||<=2 max(||y||,||z||)||y-z||`, together with
`||P||,||Phi||<=C`; explicitly, applying the state `rho o Phi` to the
self-adjoint difference of the two squares costs at most its operator norm.
The middle inequality is Jordan-Schwarz for `Phi`.

Since `P` is an exact idempotent, this almost-contraction implies almost
orthogonality of `Im P` and `Ker P` in every seminorm `||.||_omega`:

```text
|omega(u o n)| <= C sqrt(eta)||u||||n||,
u in Im P, n in Ker P.
```

Indeed, put `c=omega(u o n)` and `a=||n||_omega^2`. Since `P(u+t n)=u`, the
almost-contraction inequality gives, for every real `t`,

```text
||u||_omega^2
 <= ||u+t n||_omega^2 + K eta ||u+t n||^2
 =  ||u||_omega^2 + 2t c + t^2 a + K eta ||u+t n||^2.
```

Choose the sign of `t` opposite to the sign of `c`, and write `s=|t|`. Using
`||u+t n||^2 <= 2||u||^2+2s^2||n||^2`,

```text
2s |c| <= s^2(a+2K eta ||n||^2)+2K eta ||u||^2
```

for all `s>0`. Optimizing in `s` gives

```text
|c| <= C sqrt(eta)||u|| sqrt(a+eta||n||^2)
     <= C sqrt(eta)||u||||n||.
```

Consequently, for all `x in V` and `b in A`,

```text
||P(Px o b)-P(x o b)|| <= C sqrt(eta)||x||||b||.        (FI)
```

Indeed `n=x-Px in Ker P`, and for every state `rho`,

```text
|rho P(n o b)|
 <= |rho Phi(n o b)| + C eta ||n||||b||
 = |omega(n o b)| + C eta ||n||||b||.
```

Here `||n||<=C||x||`. Since `P(n o b)` is self-adjoint, taking the supremum
over states gives `(FI)`.

### Lemma 3: Square Holes Are Approximately Null

For `r in A`, define the square hole

```text
q_r=P(r^2)-r^2 in Ker P.
```

The inclusion in `Ker P` follows from idempotency:
`P(q_r)=P^2(r^2)-P(r^2)=0`.

Then

```text
q_r >= -C eta ||r||^2 1,                         (3.1)
||P(q_r^2)|| <= C eta ||r||^4,                   (3.2)
||q_r||_omega <= C sqrt(eta)||r||^2              (3.3)
```

for every state seminorm `omega=rho o Phi`.

Proof. Since `||Phi(r)-r||<=delta||r||`,

```text
Phi(r^2) >= Phi(r)^2 >= r^2-C delta||r||^2 1.
```

The second inequality follows from
`||Phi(r)^2-r^2||<=C delta||r||^2` and the order-perturbation rule above.
Replacing `Phi(r^2)` by `P(r^2)` costs another `delta||r||^2` in the same
order sense, giving `(3.1)`.

Choose `gamma=C delta||r||^2` so that

```text
y=q_r+gamma 1 >= 0.
```

Also `||q_r||<=C||r||^2` and hence `||y||<=C||r||^2`. Since `P(q_r)=0`,

```text
||Phi(q_r)|| = ||(Phi-P)(q_r)|| <= C delta||r||^2,
```

and hence `0<=Phi(y)` with `||Phi(y)||<=C delta||r||^2`.

Because `0<=y<=C||r||^2 1`, functional calculus gives

```text
0<=y^2<=C||r||^2 y.
```

Applying positivity of `Phi`,

```text
||Phi(y^2)|| <= C||r||^2 ||Phi(y)|| <= C delta||r||^4.
```

Finally `q_r^2 <= 2y^2+2gamma^2 1`, so

```text
||Phi(q_r^2)|| <= C delta||r||^4.
```

The term `gamma^2 1` is `O(delta^2||r||^4)` and is absorbed into
`O(delta||r||^4)` after decreasing `eta0`.
Replacing `Phi` by `P` costs at most `delta||q_r^2||<=C delta||r||^4`, proving
`(3.2)`. Estimate `(3.3)` follows from the preceding bound on `Phi(q_r^2)`:

```text
||q_r||_omega^2 = rho Phi(q_r^2).
```

### Lemma 4: Polarized Hole Estimates

For `r,s in A`, set

```text
q_{r,s}=P(r o s)-r o s = -h_{r,s}.
```

Then for every state seminorm,

```text
||q_{r,s}||_omega <= C sqrt(eta)||r||||s||.       (4.1)
```

Indeed,

```text
lambda q_{r,s}
 = q_{lambda r,s}
 = 1/4 (q_{lambda r+s}-q_{lambda r-s}),
```

where `q_x` on the right denotes the square hole `P(x^2)-x^2`. This is just
the polarization identity for the symmetric bilinear map

```text
(r,s) -> q_{r,s}=P(r o s)-r o s.
```

and Lemma 3 gives

```text
||q_{r,s}||_omega
 <= C sqrt(eta)(lambda||r||^2 + lambda^{-1}||s||^2).
```

If `r=0` or `s=0` this is trivial. Otherwise choose
`lambda=||s||/||r||`, proving `(4.1)`.

We will also use the crude bound

```text
||q_{r,s}|| <= C||r||||s||.
```

Cauchy-Schwarz for the positive functional `rho o Phi`, followed by replacing
`Phi` with `P`, gives the hole-hole estimate

```text
||P(q_{r,s} o q_{u,v})||
 <= C eta ||r||||s||||u||||v||.                  (HH)
```

Explicitly, for every state `rho`,

```text
|rho Phi(q_{r,s} o q_{u,v})|
 <= ||q_{r,s}||_omega ||q_{u,v}||_omega
 <= C eta ||r||||s||||u||||v||.
```

The replacement of `Phi` by `P` costs at most
`delta ||q_{r,s}||||q_{u,v}||`, which has the same bound after increasing `C`.
The element `P(q_{r,s} o q_{u,v})` is self-adjoint, so the state supremum is
its operator norm.

Similarly, for arbitrary `z in V`,

```text
||P(q_{r,s} o z)||
 <= C sqrt(eta)||r||||s||||z||.                  (HZ)
```

Here `||z||_omega<=||z||` because `z^2<=||z||^2 1` and `Phi` is positive
unital. The replacement of `Phi` by `P` costs at most
`C eta ||r||||s||||z||`, which is absorbed into the displayed
`O(sqrt(eta))` bound. The same state-supremum argument converts the state
estimates into operator norm.

### Lemma 5: One-Hole Contexts

Let `h=h_{r,s}=r o s-P(r o s)` be a range-product hole and let `t,u in A`.
Then

```text
||P((h o t) o u)|| <= C sqrt(eta)||r||||s||||t||||u||,       (5.1)
||P(h o (t o u))|| <= C sqrt(eta)||r||||s||||t||||u||.       (5.2)
```

For `(5.1)`, put `y=h o t`. The range part `P(y)` is
`O(sqrt(eta)||r||||s||||t||)` by `(HZ)`. Hence

```text
||P(P(y) o u)|| <= C sqrt(eta)||r||||s||||t||||u||.
```

For the kernel part `y-P(y)`, apply `(FI)` with `x=y` and `b=u`:

```text
P((y-P(y)) o u)=P(y o u)-P(P(y) o u)
```

has the same `O(sqrt(eta)||r||||s||||t||||u||)` bound, using the crude estimate
`||y||<=C||r||||s||||t||`. This proves `(5.1)`.

For `(5.2)`, write

```text
t o u = P(t o u)+h_{t,u}.
```

The first term is controlled by `(HZ)` because `P(t o u) in A`; the second is
`P(h o h_{t,u})`, controlled by `(HH)`, hence `O(eta)` and absorbed into the
`O(sqrt(eta))` target.

### Jordan Identity

Fix `a,b in A`. Write

```text
p=P(a^2)=a^2-h_{a,a},
q=P(b o a)=b o a-h_{b,a}.
```

Then `p,q in A` and

```text
||p|| <= C||a||^2,        ||q|| <= C||a||||b||.
```

For the left side, let `l=h_{p,b}=p o b-P(p o b)`. Then

```text
((a*a)*b)*a
 = P(P(p o b) o a)
 = P((p o b) o a) - P(l o a).
```

Here `l in Ker P`, because `P(l)=P(p o b)-P^2(p o b)=0`, and

```text
||l|| <= ||p o b||+||P(p o b)|| <= C||a||^2||b||.
```

Since `P(l)=0`, `(FI)` applied with `x=l` and the range element `a` gives

```text
||P(l o a)|| <= C sqrt(eta)||a||^3||b||.        (6.1)
```

Next use `p=a^2-h_{a,a}`:

```text
P((p o b) o a)
 = P(((a^2 o b) o a)) - P((h_{a,a} o b) o a).
```

The last term is `O(sqrt(eta)||a||^3||b||)` by `(5.1)` with
`h=h_{a,a}`, `t=b`, and `u=a`. Combining this with `(6.1)` gives

```text
((a*a)*b)*a
 = P(((a^2 o b) o a)) + O(sqrt(eta)||a||^3||b||).      (L)
```

For the right side, expand both holes:

```text
P(p o q)
 = P((a^2-h_{a,a}) o (b o a-h_{b,a}))
 = P(a^2 o (b o a))
   - P(h_{a,a} o (b o a))
   - P(a^2 o h_{b,a})
   + P(h_{a,a} o h_{b,a}).
```

The first error term is controlled by `(5.2)` with `h=h_{a,a}`, `t=b`, and
`u=a`:

```text
||P(h_{a,a} o (b o a))|| <= C sqrt(eta)||a||^3||b||.
```

For the second error term, decompose `a^2=p+h_{a,a}`:

```text
P(a^2 o h_{b,a}) = P(p o h_{b,a}) + P(h_{a,a} o h_{b,a}).
```

Since `h_{b,a} in Ker P` and `p in A`, `(FI)` applied with `x=h_{b,a}` and
range element `p` gives `P(P(h_{b,a}) o p)=0` and therefore

```text
||P(p o h_{b,a})|| <= C sqrt(eta)||p||||h_{b,a}||
                   <= C sqrt(eta)||a||^3||b||.
```

Both occurrences of `P(h_{a,a} o h_{b,a})` are bounded by `(HH)`:

```text
||P(h_{a,a} o h_{b,a})|| <= C eta ||a||^3||b||.
```

For `eta<=eta0`, this is absorbed into the `O(sqrt(eta))` error. Therefore

```text
(a*a)*(b*a)
 = P(a^2 o (b o a)) + O(sqrt(eta)||a||^3||b||).       (R)
```

The ambient product `o` satisfies the exact Jordan identity

```text
(a^2 o b) o a = a^2 o (b o a).
```

Subtracting `(R)` from `(L)` proves

```text
||((a*a)*b)*a - (a*a)*(b*a)||
 <= C sqrt(eta)||a||^3||b||.
```

This completes the proof of the theorem.
