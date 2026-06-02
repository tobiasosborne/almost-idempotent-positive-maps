# Layer 2 Bridge: Approximate Null-Ideal Estimate

This note upgrades `layer2-bridge-sqrt.md`. The previous note proved only the
first insertion estimate. The missing ingredient was an approximate
Effros-Stormer null-ideal estimate for range-product holes. The argument below
appears to supply it at square-root scale, giving a full `O(sqrt(eta))`
Jordan-identity bridge for arbitrary unital positive maps.

This should be peer-reviewed by Agent A before being treated as locked.

## Setup

Let `V=B(H)_sa` with Jordan product `x o y=(xy+yx)/2` and operator norm.
Let `Phi:V->V` be unital positive with

```text
||Phi^2-Phi|| <= eta.
```

Let

```text
P = theta(2 Phi-I)
```

be the spectral idempotent. For sufficiently small `eta`,

```text
P^2=P,   P(1)=1,   ||P-Phi|| <= delta,   ||P|| <= 1+delta,
delta <= C eta.
```

Set `A=Im P`. For `r,s in A`, define the range-product hole

```text
h_{r,s}=r o s - P(r o s) in Ker P
```

and equivalently

```text
q_{r,s}=P(r o s)-r o s = -h_{r,s}.
```

For a state `rho`, write `omega=rho o Phi` and

```text
||x||_omega^2 = omega(x^2).
```

## 1. Square Holes Are Almost Positive Kernel Elements

For `r in A`, put

```text
q_r=q_{r,r}=P(r^2)-r^2 in Ker P.
```

Jordan-Schwarz for `Phi` gives

```text
Phi(r)^2 <= Phi(r^2).
```

Since `r=P(r)` and `||Phi-P||<=delta`,

```text
||Phi(r)-r|| <= delta ||r||.
```

Thus, in order,

```text
Phi(r^2) >= r^2 - C delta ||r||^2 1,
P(r^2)   >= r^2 - C delta ||r||^2 1,
```

so

```text
q_r >= -gamma 1,       gamma=C delta ||r||^2.
```

Let

```text
y=q_r+gamma 1 >= 0.
```

Also `||y||<=C||r||^2`. Since `P(q_r)=0`,

```text
||Phi(q_r)|| = ||(Phi-P)(q_r)|| <= C delta ||r||^2.
```

Therefore `Phi(y)>=0` and `||Phi(y)||<=C delta ||r||^2`. As
`0<=y<=C||r||^2 1`, positivity gives

```text
0 <= Phi(y^2) <= C||r||^2 Phi(y),
||Phi(y^2)|| <= C delta ||r||^4.
```

Finally `q_r^2 <= 2y^2+2 gamma^2 1`, so

```text
||Phi(q_r^2)|| <= C delta ||r||^4,
||P(q_r^2)||   <= C delta ||r||^4.
```

The second estimate uses `||P-Phi||<=delta` and `||q_r||<=C||r||^2`.

## 2. Polarized Null-Square Estimate

For `r,s in A`, `q_{r,s}` is symmetric bilinear and

```text
q_{r,s}=1/4 (q_{r+s}-q_{r-s}).
```

The square estimate above gives, for every state seminorm,

```text
||q_t||_omega <= C sqrt(delta) ||t||^2.
```

By applying the polarization identity to `lambda r` and `s`, then optimizing
`lambda>0`,

```text
||q_{r,s}||_omega <= C sqrt(delta) ||r|| ||s||.
```

Consequently

```text
||Phi(q_{r,s}^2)|| <= C delta ||r||^2 ||s||^2,
||P(q_{r,s}^2)||   <= C delta ||r||^2 ||s||^2.
```

This is the desired approximate null-square estimate for range-product holes.

## 3. Hole-Hole And Hole-Range Estimates

For `r,s,u,v in A`, Cauchy-Schwarz for the positive functional `rho o Phi`
gives

```text
|rho Phi(q_{r,s} o q_{u,v})|
 <= ||q_{r,s}||_omega ||q_{u,v}||_omega
 <= C delta ||r||||s||||u||||v||.
```

After replacing `Phi` by `P`,

```text
||P(q_{r,s} o q_{u,v})||
 <= C delta ||r||||s||||u||||v||.        (HH)
```

Similarly, for arbitrary `z in V`,

```text
||P(q_{r,s} o z)||
 <= C sqrt(delta) ||r||||s||||z||.       (HZ)
```

The estimate `(HZ)` also follows from the first insertion lemma when `z in A`;
the point here is that `(HZ)` is available for all `z` when `q_{r,s}` is a
range-product hole.

## 4. One-Hole Iteration

If `h=h_{r,s}` is a range-product hole and `t,u in A`, then

```text
||P((h o t) o u)|| <= C sqrt(delta) ||r||||s||||t||||u||.
```

Proof: decompose `h o t=P(h o t)+n` with `n in Ker P`. The range part is
`O(sqrt(delta))` by `(HZ)` or first insertion, and the kernel part is controlled
after multiplying by `u in A` by the first insertion estimate from
`layer2-bridge-sqrt.md`.

Also, if `t,u in A`, then

```text
||P(h o (t o u))|| <= C sqrt(delta) ||r||||s||||t||||u||.
```

Indeed `t o u=P(t o u)+h_{t,u}`; the first term is controlled by first
insertion and the second by `(HH)`.

## 5. Jordan Identity Defect

For `a,b in A`, set

```text
p=P(a^2)=a^2-h_{a,a},
q=P(b o a)=b o a-h_{b,a}.
```

Let `l=h_{p,b}=p o b-P(p o b)`. Then

```text
((a*a)*b)*a
 = P(P(p o b) o a)
 = P((p o b) o a) - P(l o a)
 = P(((a^2 o b) o a)) + O(sqrt(delta)) ||a||^3 ||b||.
```

Here `P(l o a)` is controlled by first insertion, and the term created by
`p=a^2-h_{a,a}` is controlled by the one-hole iteration above.

Similarly,

```text
(a*a)*(b*a)
 = P(p o q)
 = P(a^2 o (b o a)) + O(sqrt(delta)) ||a||^3 ||b||.
```

The error terms are `P(h_{a,a} o (b o a))`, `P(a^2 o h_{b,a})`, and
`P(h_{a,a} o h_{b,a})`; these are controlled respectively by one-hole
iteration/decomposition and `(HH)`.

The ambient Jordan product satisfies the exact Jordan identity

```text
(a^2 o b) o a = a^2 o (b o a).
```

Therefore

```text
||((a*a)*b)*a - (a*a)*(b*a)||
 <= C sqrt(delta) ||a||^3 ||b||
 <= C sqrt(eta) ||a||^3 ||b||.
```

## Status

Together with the easy estimates already recorded in `layer2-bridge-sqrt.md`,
this gives a candidate proof that `A=Im P` with product

```text
a*b=P(a o b)
```

is an `O(sqrt(eta))` epsilon-JB order-unit algebra for every almost-idempotent
unital positive `Phi`.

The proof does not give `O(eta)` for arbitrary positive maps. The single-hole
terms in the final expansion are still only `O(sqrt(eta))`. An `O(eta)` theorem
still appears to require a decomposable/CP-style two-hole mechanism or a
stronger hypothesis.

## Numerical/Low-Dimensional Checks

Parfit ran a sidecar probe recorded at
`agent-B/experiments/null-ideal-probe/REPORT.md`.

The most informative classical family is the row-stochastic map on `R^3`

```text
T_a = [ 1        0          0
        0        1-a        a
        (1-a)/3  2(1-a)/3  a ].
```

For the sup norm and `l_infty -> l_infty` map norm,

```text
eta = (2/3)a(1-a),
max ||P(h_{r,s}^2)|| = (64/81)a + O(a^2),
```

so `||P(h_{r,s}^2)||/eta -> 32/27`. Thus the null-square term is genuinely
linear in `eta` in this normalization; a stronger general estimate such as
`O(eta^2)` is false. This supports the proof above and suggests the
null-ideal component itself may be sharper than the final `sqrt(eta)` Jordan
identity bound.

For qubits, the range of the spectral projection in Bloch form is closed under
the Jordan product, so `h_{r,s}=0`; numerical runs saw only floating-point
noise.
