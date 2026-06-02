# Sidecar: rank-one classical near-positive projection stability

## Result

The rank-one-perturbation case satisfies the desired dimension-free square-root
bound.

Let

```text
P = I - u v^T on ell_infty^n,
v . 1 = 0,
v . u = 1.
```

Thus `P1=1` and `P^2=P`.  Assume each row `P_i` is a signed probability
measure with negative mass

```text
neg(P_i) = sum_j max(-P_ij,0) <= delta.
```

Then, for `0 <= delta <= 1`,

```text
dist_{infty->infty}(P, {row-stochastic idempotents}) <= 20 sqrt(delta).
```

The constant is not optimized.  The exponent cannot be improved because this
class contains Hume's `3 x 3` family, whose distance is
`2 sqrt(delta)+O(delta)`.

The proof below is fully dimension-free and uses only exact sign inequalities.

## Basic sign estimates

Write

```text
t = sum_{v_j>0} v_j = sum_{v_j<0} (-v_j) > 0.
```

For row `i`,

```text
P_ij = delta_ij - u_i v_j.
```

Hence the row-negativity assumption implies the following elementary bounds.

If `u_i>0` and `v_i>0`, then the off-diagonal negative entries over the
positive part of `v` give

```text
u_i(t-v_i) <= delta.                         (1)
```

If `u_i>0` and `v_i<=0`, then all positive coordinates of `v` contribute
off-diagonal negative mass, so

```text
u_i t <= delta.                              (2)
```

Symmetrically, if `u_i<0` and `v_i<0`, then

```text
(-u_i)(t-|v_i|) <= delta,                    (3)
```

and if `u_i<0` and `v_i>=0`, then

```text
(-u_i)t <= delta.                            (4)
```

Also, whenever `u_i v_i>1`, the diagonal entry is negative, so

```text
u_i v_i <= 1+delta.                          (5)
```

## Dominant same-sign coordinates

Let

```text
S_+ = {i : u_i>0, v_i>0},       a_i = u_i v_i,
S_- = {i : u_i<0, v_i<0},       b_i = u_i v_i = (-u_i)(-v_i).
```

Choose `p in S_+` with maximal `a_i`, and set `alpha=a_p`, with
`alpha=0` if `S_+` is empty.  Choose `q in S_-` with maximal `b_i`, and set
`beta=b_q`, with `beta=0` if `S_-` is empty.

For `i in S_+`, put `r_i=v_i/t`.  By (1),

```text
a_i(1-r_i)/r_i <= delta,
```

so

```text
a_i/(a_i+delta) <= r_i.
```

Since `sum_{i in S_+} r_i <= 1`, maximality of `alpha` gives

```text
sum_{i in S_+, i != p} a_i <= delta.         (6)
```

Indeed,

```text
alpha/(alpha+delta)
 + (sum_{i != p} a_i)/(alpha+delta)
 <= sum_{i in S_+} a_i/(a_i+delta)
 <= 1.
```

The same argument on the negative part gives

```text
sum_{i in S_-, i != q} b_i <= delta.         (7)
```

The opposite-sign diagonal contribution is small.  From (2),

```text
sum_{u_i>0, v_i<0} u_i(-v_i) <= delta,
```

and from (4),

```text
sum_{u_i<0, v_i>0} (-u_i)v_i <= delta.
```

Let `Gamma` be the sum of these two opposite-sign contributions.  Then

```text
Gamma <= 2 delta.                            (8)
```

Using `v.u=1`, (6), (7), and (8),

```text
1 - 2 delta <= alpha + beta <= 1 + 2 delta.  (9)
```

Thus, for small `delta`, at most two coordinates matter: one positive-positive
coordinate `p` and one negative-negative coordinate `q`.

A useful row estimate is the following.  For every row,

```text
||P_i-e_i||_1 = |u_i| ||v||_1 = 2 |u_i| t.
```

By (1)-(4),

```text
||P_i-e_i||_1 <= 2(a_i+delta)   if i in S_+,
||P_i-e_i||_1 <= 2(b_i+delta)   if i in S_-,
||P_i-e_i||_1 <= 2 delta        in the opposite-sign cases.
```

Consequently every row except possibly `p` and `q` is within `4 delta` of the
corresponding absorbing row `e_i`.

## Case 1: one dominant sign group

Assume first that `0<delta<=1/16`, put `tau=sqrt(delta)`, and suppose

```text
beta <= tau.
```

By (9), `alpha>0`, so `p` exists.  Let

```text
rho^-_j = (-v_j)_+ / t.
```

Define the stochastic idempotent `E` by

```text
E_p = rho^-,
E_i = e_i  for i != p.
```

This is the idempotent with one transient state `p` and all other states
absorbing.

Let `r=v_p/t` and

```text
A = u_p(t-v_p) <= delta.
```

The `p`-row of `P` has:

- diagonal entry `1-alpha`;
- negative entries over the positive coordinates other than `p`, with total
  absolute mass `A`;
- on the negative support of `v`, the probability vector `rho^-` scaled by
  `u_p t = alpha + A`.

Therefore

```text
||P_p-rho^-||_1
 <= |1-alpha| + A + |alpha+A-1|.
```

By (9),

```text
|1-alpha| = |beta + 1 - (alpha+beta)|
          <= beta + 2 delta,
```

and hence

```text
|alpha+A-1| <= beta + 3 delta.
```

So

```text
||P_p-rho^-||_1 <= 2 beta + 6 delta <= 8 sqrt(delta).
```

Every other row is within `4 sqrt(delta)` of its absorbing row, including the
`q`-row if it exists because `beta<=sqrt(delta)`.  Hence

```text
||P-E||_{infty->infty} <= 8 sqrt(delta).
```

The case `alpha<=sqrt(delta)` is symmetric: use the stochastic idempotent with
one transient row `q` equal to

```text
rho^+_j = (v_j)_+ / t
```

and all other rows absorbing.  The same estimate holds.

## Case 2: two visible sign groups

Now suppose

```text
alpha >= tau,     beta >= tau,
tau = sqrt(delta),
```

with `0<delta<=1/16`.  Put

```text
S = alpha + beta.
```

By (9), `S in [1-2delta,1+2delta]`.  Define the stochastic idempotent `E` by
making `{p,q}` one recurrent class and all other states absorbing:

```text
E_p = E_q = (beta/S) e_p + (alpha/S) e_q,
E_i = e_i  for i not in {p,q}.
```

The inactive rows are again within `4 delta` of their absorbing rows.  It
remains to estimate rows `p` and `q`.

Let

```text
r = v_p/t,       s = (-v_q)/t,
A = u_p(t-v_p) <= delta.
```

From the negative-sign version of (1),

```text
1-s <= delta/(beta+delta).
```

Since `beta>=tau` and `delta<=1/16`,

```text
u_p(t-|v_q|) = (alpha+A)(1-s) <= 2 sqrt(delta).       (10)
```

This is the positive mass in row `p` outside the coordinate `q` on the
negative support of `v`.  The negative mass in row `p` on positive coordinates
outside `p` is `A<=delta`.

For the two coordinates in the recurrent pair,

```text
|P_pp - beta/S|
 = |1-alpha - beta/S|
 <= 3 delta,
```

using `S in [1-2delta,1+2delta]`.  Also

```text
P_pq = u_p(-v_q) = (alpha+A)s,
```

so, using (10),

```text
|P_pq - alpha/S|
 <= |(alpha+A)s-alpha| + |alpha-alpha/S|
 <= 2 sqrt(delta) + 4 delta.
```

Together with the mass outside `{p,q}`, this gives

```text
||P_p-E_p||_1 <= 12 sqrt(delta).
```

The same argument with signs reversed gives

```text
||P_q-E_q||_1 <= 12 sqrt(delta).
```

Therefore

```text
||P-E||_{infty->infty} <= 12 sqrt(delta)
```

in the two-visible-groups case.

## Large and zero delta

If `delta=0`, then `P` itself is row-stochastic and idempotent, so the distance
is zero.

If `1/16 <= delta <= 1`, use the identity stochastic idempotent.  Since each
row has total mass `1` and negative mass at most `delta`,

```text
||P_i||_1 = 1 + 2 neg(P_i) <= 1+2delta,
```

and hence

```text
||P-I||_{infty->infty} <= 2+2delta <= 4 <= 20 sqrt(delta).
```

Combining this with the small-`delta` construction proves the announced
dimension-free estimate for all `0<=delta<=1`.

## Relation to Hume's family

For Hume's example

```text
v_s = (1, -1+s, -s),
u_s = (1-s+s^2, -s, 0)^T,
P_s = I-u_s v_s^T,
```

the row negative mass is `delta=s^2`.  Here

```text
alpha = 1-s+s^2,
beta = s(1-s) <= sqrt(delta).
```

Thus the proof falls into Case 1.  The constructed idempotent has one transient
row and is `O(s)` from `P_s`, matching the sharp `sqrt(delta)` scale.  The
exact nearest idempotent in the earlier `3 x 3` computation is slightly closer,
but the exponent mechanism is the same: a boundary state separates at first
order while the positivity defect is second order.
