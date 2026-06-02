# Sidecar: Positivity Rounding For Layer 2

## Question

After abstract JB stability, suppose we have a finite-dimensional order-unit/JB
algebra `J` and a unital linear map

```text
T : B(H)_sa -> J
```

which is only `eps`-positive:

```text
0 <= x <= 1  =>  T(x) >= -eps 1_J.
```

Can one always find a genuinely positive unital `T_+` with
`||T-T_+|| <= C eps`, with universal `C`?

## Answer

No. A dimension-free `O(eps)` rounding theorem is false, already for a
commutative domain and a finite-dimensional special JB target. The obstruction
is a signed POVM whose atomwise negative parts point in many orthogonal spin
directions. Approximate positivity controls every event only to order `eps`,
but positivity would require total vector variation that the unit cannot supply.

The best possible black-box rounding scale is at least `sqrt(eps)` in this
generality.

## Counterexample Family

Let `m >= 1`, set

```text
eps = 1/(2m),        n = 2m.
```

Let `J = R oplus R^m` be the spin factor with order unit `u=(1,0)` and cone

```text
J_+ = { (s,v) : s >= ||v||_2 }.
```

Its order-unit norm is `||(s,v)|| = |s| + ||v||_2`. Let `e_1,...,e_m` be the
standard basis of `R^m`. Define a unital map

```text
T : ell_infty^{2m} -> J
```

on the coordinate atoms by

```text
T(delta_{j,+}) = (eps,  2 eps e_j),
T(delta_{j,-}) = (eps, -2 eps e_j),        j=1,...,m.
```

The atoms sum to `(1,0)`, so `T(1)=u`.

For a positive contraction `t=(t_{j,+},t_{j,-})`, put

```text
d_j = t_{j,+}-t_{j,-},        p_j=t_{j,+}+t_{j,-}.
```

Then

```text
T(t) = (eps sum_j p_j, 2 eps d).
```

Since `|d_j| <= 1` and `sum |d_j| <= sum p_j`,

```text
2 ||d||_2 <= sum_j |d_j| + 1 <= sum_j p_j + 1.
```

Hence

```text
||2 eps d||_2 <= eps sum_j p_j + eps,
```

so `T(t) >= -eps u`. Thus `T` is `eps`-positive.

## Distance From Positive Maps

Let `S:ell_infty^{2m}->J` be any positive unital map. Write

```text
S(delta_i) = (beta_i,w_i).
```

Positivity gives `beta_i >= ||w_i||_2`; unitality gives

```text
sum_i beta_i = 1,        sum_i w_i = 0,
```

and therefore

```text
sum_i ||w_i||_2 <= 1.
```

For the vector parts `v_i` of `T(delta_i)`,

```text
sum_i ||v_i||_2 = 2m * 2 eps = 2.
```

Thus, with `u_i=v_i-w_i`,

```text
sum_i ||u_i||_2 >= 1,
sum_i ||u_i||_2^2 >= 1/(2m) = eps.
```

By the Rademacher average identity,

```text
E_sigma ||sum_i sigma_i u_i||_2^2 = sum_i ||u_i||_2^2,
```

so some sign vector `sigma_i in {+-1}` satisfies

```text
||sum_i sigma_i (v_i-w_i)||_2 >= sqrt(eps).
```

The operator norm `ell_infty^{2m}->J` dominates this vector-part sign norm.
Consequently

```text
||T-S|| >= sqrt(eps)
```

for every positive unital `S`. Since `sqrt(eps)/eps -> infinity`, no universal
`O(eps)` positivity-rounding theorem can hold.

Composing this example with the diagonal conditional expectation
`B(C^{2m})_sa -> ell_infty^{2m}` gives the same obstruction for maps with
domain `B(H)_sa`.

## Fully Commutative Check

If both domain and codomain are commutative, the obstruction is absent.
For `T:ell_infty^n -> ell_infty^r`, each output coordinate is a signed
probability vector `mu` with

```text
sum_i mu_i = 1,
sum_{mu_i<0} (-mu_i) <= eps.
```

Normalize the positive part:

```text
p_i = mu_i^+ / (1 + delta),        delta=sum_i mu_i^- <= eps.
```

Then `p` is a probability vector and

```text
||mu-p||_1 = 2 delta <= 2 eps.
```

Row by row this gives a positive unital map within `2 eps` in
`ell_infty` operator norm. The same argument works for scalar output from
`B(H)_sa` by the Jordan decomposition of a Hermitian functional.

## Effect On The Factorization Theorem

The positive-map factorization theorem cannot rely on a black-box statement

```text
approximately positive unital => O(eps)-close to positive unital.
```

That statement is false for JB targets. To obtain genuinely positive factor
maps with the same exponent, the proof must build positivity into the Layer 1
identification or use a more structured route, such as:

1. a concrete JC output with positive comparison maps,
2. near-positive projection stability,
3. additional hypotheses controlling total negative variation, or
4. accepting a possible square-root loss in any black-box rounding step.

In particular, if the bridge only gives `eps=O(eta^alpha)` approximate
positivity, abstract rounding alone cannot justify `O(eta^alpha)` UP
factorization maps.
