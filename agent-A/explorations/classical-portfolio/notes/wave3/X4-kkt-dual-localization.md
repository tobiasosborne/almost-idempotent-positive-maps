**Verdict**

X4 does **not** close HLC as stated. The precise failing step is:

`Φ_min large => near-exposer with margin >= κ`

This implication is false already at the exposedness LP level. Exactness `P²=P` might still rule out the bad geometry, but that is a new exactness/cost lemma, not a KKT consequence.

**PROVED: LP/KKT Shape**

For `a_i = p_i - v`, `F={j: ||a_j||_1 >= rho}`, the exposedness margin is

```text
t_v = max t
s.t. 0 <= phi(a_i) <= 1      all i
     phi(a_j) >= t           j in F.
```

Its dual is

```text
t_v = min sum_i beta_i
s.t. mu in Prob(F), alpha,beta >= 0,
     sum_j mu_j a_j = sum_i (beta_i - alpha_i) a_i.
```

Failure is `t_v < kappa`.

If you minimize

```text
Phi = sum_j mu_j ||a_j||_1 + lambda sum_i alpha_i
```

over C10 witnesses, KKT gives reduced-cost conditions of the form

```text
mu_j > 0    =>  ||a_j||_1 + <y,a_j> + s = 0
alpha_i >0 =>  lambda + <y,a_i> = 0
beta_i >0  =>  gamma - <y,a_i> = 0
```

but `y` is not constrained by `0 <= <y,a_i> <= 1`, and it is not an exposer. If you first force primary optimality `sum beta=t_v`, then complementary slackness does tie `mu` to the active level set of a best exposer, but active level sets need not be spatially local.

**Countermodel To The Large-Φ Branch**

Take rows in `R^2`:

```text
v = (0,0)
a = (1, eps)
b = (-1, eps)
r = (0,1)
K = conv{v,a,b,r}
```

Assume `0 < eps < kappa` and `rho < 1`, so `a,b,r` are all rho-far from `v`.

Any affine `h(x,y)=ux+sy` with `h(v)=0` and `0<=h<=1` on `K` satisfies

```text
0 <= u + eps s <= 1
0 <= -u + eps s <= 1
0 <= s <= 1.
```

Thus

```text
min(h(a),h(b),h(r)) <= eps s <= eps,
```

and equality is attained by `h(x,y)=y`. So the optimal exposedness margin is exactly

```text
t_v = eps < kappa.
```

So `v` fails `(rho,kappa)`-exposedness.

But the C10 dual witness

```text
mu_a = mu_b = 1/2,
beta_r = eps,
alpha = 0
```

satisfies

```text
(1/2)a + (1/2)b = (0,eps) = eps r,
sum beta = eps < kappa.
```

Its variational cost is

```text
Phi = (1/2)||a||_1 + (1/2)||b||_1 = 1 + eps.
```

Every feasible `mu` is supported on rho-far rows with distance at least `1`, so the minimum is large, yet there is no near-exposer: the best margin is only `eps`.

**What Survives**

The localized branch is still useful, but only under a stronger hypothesis than `Phi` supplies: R1 needs localization of the relevant support radius entering the `beta` term and the non-`v` vertex components, not just average `mu` radius plus small `alpha` mass. With true radius `r`, the descent loss is the desired scale

```text
kappa r^2 / rho.
```

The proposed objective does not control `beta` radius, and the countermodel has `alpha=0`, so the `lambda sum alpha` penalty is inert.

**Conclusion**

X4 reduces back to the known missing exactness lemma:

```text
Nonlocalized C10 witnesses / high cap rows / high zero-face carriers
must force delta >= a H^2.
```

That is essentially HLC or the anchored-cycle projection-cost lemma, not a consequence of variational KKT alone.