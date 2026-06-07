# Subagent: Step 5 Failed-Exposedness Circuit Extraction

Date: 2026-06-07.  Lane: Agent B sandbox.  Status: exploratory lemma package,
not a canonical proof shard.

## Verdict

Step 5 is ready as a small finite-dimensional LP lemma.  If a row vertex `v`
fails exposedness at scale `rho`, then a normalized barycenter of rows outside
the `rho`-ball equals, modulo the zero-face cone of an optimal exposing
functional, a vector with total coefficient mass `<kappa`.  The uncontrolled
term cannot honestly be removed by LP duality alone, so the right Step 6 normal
form is a **zero-face cone plus small top-face mass** identity.

## Setup

Let `X={x_1,...,x_n}` be finite in an affine real vector space, let `v=x_a`,
and put

```text
z_i=x_i-v,
S=S_v(rho)={i : ||x_i-v||_1 >= rho}.
```

Assume `S` is nonempty.  Let `H_v` be the affine functions `h` on `aff(X)`
with

```text
h(v)=0,        0 <= h(x_i) <= 1       for all i.
```

Define `e=e_v(rho)=max_{h in H_v} min_{j in S} h(x_j)`.  The lemma is purely
finite-dimensional; it does not use `P^2=P` or `neg(p_i)<=delta`.

## Candidate Lemma

Assume `e_v(rho)<kappa`.  Then there exist `h in H_v`, `mu in Delta(S)`, and
`alpha_i,beta_i>=0`, with `alpha_a=beta_a=0`, such that:

```text
1. h is optimal: min_{j in S} h(x_j)=e.
2. mu is supported on {j in S : h(x_j)=e}.
3. beta is supported on {i : h(x_i)=1}.
4. alpha is supported on {i : h(x_i)=0}.
5. sum_i beta_i = e < kappa.
6. sum_{j in S} mu_j (x_j-v)
     = sum_i (beta_i-alpha_i)(x_i-v).          (CE)
```

Equivalently, with `Y=sum_{j in S} mu_j (x_j-v)`,
`A=sum_i alpha_i (x_i-v)`, and `B=sum_i beta_i (x_i-v)`, one has

```text
Y + A = B,
A in cone{x_i-v : h(x_i)=0},
B in e conv{x_i-v : h(x_i)=1},
e<kappa.
```

If `e=0`, interpret the last line as `B=0`.  This is the preferred Step 6
normal form.

## Positive Affine Circuit Form

Let `A0=sum_i alpha_i`.  Expanding `(CE)` gives the positive affine identity

```text
sum_{j in S} mu_j x_j + sum_i alpha_i x_i
  = sum_i beta_i x_i + (1+A0-e)v.             (AF)
```

Both sides have total mass `1+A0`.  The outside-`rho` mass is normalized to one
on the left before any total-mass normalization.  In the intended regime
`kappa<=1/2`, the anchor coefficient satisfies `1+A0-e >= 1-kappa >= 1/2`.
This is useful for oriented-circuit bookkeeping, but `(CE)` is cleaner for
aggregation because it keeps the basepoint `v` visible.

## Minimal Proof

Work in `V=span{z_i}`.  Values of affine functions in `H_v` are the same as
linear functionals `ell` on `V` satisfying `0<=ell(z_i)<=1`.  Finite minimax
gives

```text
e_v(rho)
 = min_{mu in Delta(S)}
     max_{ell} ell(sum_{j in S} mu_j z_j),
```

where the maximum is over the same inequalities.  Choose a saddle pair
`(ell,mu)`, write `Y=sum_{j in S} mu_j z_j`, and set `h(x_i)=ell(z_i)`.

For fixed `Y`, the inner maximization is the linear program

```text
maximize    ell(Y)
subject to  ell(z_i) <= 1,
            -ell(z_i) <= 0.
```

Its dual has nonnegative variables `beta_i` for the upper constraints and
`alpha_i` for the lower constraints:

```text
minimize    sum_i beta_i
subject to  Y = sum_i (beta_i-alpha_i) z_i,
            alpha_i,beta_i >= 0.
```

Strong duality applies because this is a finite feasible bounded LP, so there
are dual optimizers with `sum_i beta_i=ell(Y)=e`.  Complementary slackness gives
`beta_i>0 => ell(z_i)=1` and `alpha_i>0 => ell(z_i)=0`.  Since
`ell(z_j)>=e` for all `j in S` and `sum_j mu_j ell(z_j)=ell(Y)=e`, every
support point of `mu` has `ell(z_j)=e`.  Finally, delete any `alpha_a` or
`beta_a` because `z_a=0`.

## Constants

There is no hidden dimension factor.

```text
outside-rho mass:     sum_{j in S} mu_j = 1,
small top mass:       sum_i beta_i = e_v(rho) < kappa,
zero-face mass:       sum_i alpha_i is uncontrolled,
diameter estimate:    ||B||_1 <= kappa * diam_1(X).
```

In the project application, `diam_1(X)<=2+4delta`, so the small side has
`l1` norm at most `(2+4delta)kappa`.  No comparable bound on `A` follows from
failed exposedness alone.

## Why Alpha Is The Step 6 Blocker

The LP dual variable `alpha` is forced by the lower constraints `h(x_i)>=0`.
It records that the outside barycenter may be made small only after adding an
arbitrary amount of zero-face cone.  Pure convex geometry does not control this
mass; dense polygon examples are exactly the warning.

Thus Step 6 must prove one of the following using the extra hypotheses
`P^2=P`, `neg(p_i)<=delta`, and `q`-quasi-closedness:

```text
1. the zero-face cone terms cancel after averaging over a recurrent high class;
2. the zero-face cone terms can be converted into q-reconstruction errors;
3. large surviving zero-face mass creates a separated affine circuit forcing
   row negative mass >= c rho^2.
```

Without one of these inputs, Step 5 only gives local failed-exposedness
certificates and does not contradict a high non-exposed cycle.

## Candidate af-Sized Contract

```text
lem-failed-exposedness-circuit:
For a finite row set X, vertex v, scale rho, and kappa>0, if
e_v(rho)<kappa, then there are h, mu, alpha, beta satisfying the support
conditions above and the identity (CE), with mu a probability on rows at
distance at least rho from v and sum beta_i<kappa.
```

Suggested dependencies: finite minimax for a matrix game and finite LP strong
duality/Farkas.  If `af` wants to avoid minimax as an external theorem, split
the contract into:

```text
lem-exposedness-minimax;
lem-fixed-barycenter-farkas-dual;
lem-complementary-slackness-normal-form.
```

## Exact Handoff To Step 6

Input available for each non-exposed high vertex `v_b`:

```text
Y_b + A_b = B_b,
Y_b = normalized barycenter of rows outside B_1(v_b,rho),
A_b in cone(zero-face of h_b),
||B_b||_coeff < kappa.
```

Step 6 must choose aggregation weights, probably from the quasi-stationary
bad-kernel measure, so that the sum of the `A_b` terms is either cancelled,
absorbed by positive-coordinate reconstruction, or turned into the final
negative-mass lower bound.  This is now the precise blocker.
