# Subagent C9-B: Shadow-Witness Leakage

Date: 2026-06-07.  Lane: Agent B sandbox.  Status: exploratory interface
analysis, not a canonical proof shard.

## Verdict

The strong C9-B hope is false from Step 3 alone.

For a global `phi`-maximal non-exposed top row `u`, Step 3 gives a
rho-separated witness distribution with height deficit average `O(kappa)`.
For

```text
tau=sqrt(delta),        kappa=k tau,
H1={j : M-phi(p_j)<=G tau},
```

this only forces leakage outside `H1` bounded by `O(k/G)`, not `O(tau)`.
Thus an `O(tau)`-leakage shadow kernel needs extra structure.

There are two usable replacements:

1. A direct LP condition: the minimum-leakage failed-exposedness witness has
   leakage `<=eps_s=O(tau)`.
2. A q-compatible condition: if the witness is chosen from the repaired
   positive-coordinate kernel `q`, then norm-one height drift gives
   high-slice leakage `O(tau)`, but only before normalizing by a small
   separated q-mass.

If neither condition holds, the output is not a q-drift theorem by itself.  It
is a real C9 obstruction: failed exposedness is being certified by lower-slice
rows that are not visible to the repaired Markov dynamics.  That obstruction
should be routed to C12 as a calibrated-dual / alpha-budget problem.

## Setup

Rows are `x_i=p_i`, with

```text
P1=1,        P^2=P,        neg(x_i)<=delta,
tau=sqrt(delta),          rho=R tau,        kappa=k tau.
```

Let `q_i=x_i^+/(1+neg(x_i))`.  Use the standard repair estimate

```text
||x_i - sum_j q_i(j)x_j||_1 <= eps_rec,        eps_rec=O(delta).
```

In all constants below, take `eps_rec<=4delta`.

Fix an affine separator `phi` whose linear part has `l_infty` norm at most
`1`.  Let

```text
M=max_j phi(x_j),        d_j=M-phi(x_j).
```

For a global maximizer `u`, `d_u=0`.  Put

```text
S=S_u(rho)={j : ||x_j-u||_1>=rho},
H1={j : d_j<=G tau},
L=S \ H1.
```

## What Step 3 Actually Gives

If `e_u(rho)<kappa`, Step 3 gives `mu in Delta(S)` with

```text
sum_j mu_j d_j <= D kappa,        D<=diam_1(K)<=2+4delta.
```

Therefore

```text
mu(L) <= D kappa/(G tau) = D k/G.              (1)
```

This is the best automatic estimate from height average alone.  It is
dimension-free, but it is not `O(tau)` unless `G` is allowed to grow like
`1/tau`, which makes the high slice too thick for the intended recurrence
argument.

So the desired statement

```text
mu(H1^c)<=C tau
```

cannot be a consequence of Step 3 plus the fixed two-scale definition of
`H1`.

## q-Leakage Bound

The repaired kernel does satisfy the desired high-slice estimate.

For every row `i`,

```text
sum_j q_i(j)d_j <= d_i + eps_rec.              (2)
```

Proof: since `phi` has `l_infty` dual norm at most `1`,

```text
|phi(x_i)-sum_j q_i(j)phi(x_j)| <= eps_rec.
```

Subtracting from `M` gives `(2)`.

Consequently, for any `a>0`,

```text
q_i({j : d_j>=d_i+a}) <= eps_rec/a.            (3)
```

In particular, if `i` lies in a top core with `d_i<=c0 delta`, then

```text
q_i(H1^c) <= (c0 delta+eps_rec)/(G tau)
          <= (c0+4) tau/G.                    (4)
```

This proves the high-core q-pruning estimate needed by C9-A.

## q-Compatible Shadow Witnesses

Let

```text
theta_i=q_i(S).
```

If `theta_i>0`, the normalized q-outside witness

```text
mu_i^q(j)=q_i(j)/theta_i        for j in S
```

is rho-separated by construction.  If `i` is in the top core, then

```text
mu_i^q(H1^c) <= (c0+4) tau/(G theta_i).        (5)
```

Thus normalized q-witnesses have `O(tau)` leakage only when
`theta_i=Omega(1)`.  If the separated q-mass is merely `theta_i=Omega(tau)`,
which is the scale C13 can still consume, `(5)` gives only `O(1/G)` leakage
after normalization.

This is a genuine normalization loss.  One possible fix is to let Step 4 use
an unnormalized shadow kernel of row mass `theta_i`, but then the recurrence
and C12 aggregation contracts must be rewritten with killing rate
`1-theta_i`.

## Minimum-Leakage LP

Define the minimum-leakage shadow witness value

```text
lambda_*(u;G,kappa)
  = min mu(L)
```

over all `mu in Delta(S)` such that

```text
G_u(y_mu) <= kappa,
y_mu=sum_j mu_j x_j,
G_u(y)=sup{h(y) : h(u)=0, 0<=h(x_i)<=1 for all i}.
```

Then:

```text
lambda_*<=eps_s
  => choose a Step-5 witness with H1-leakage <=eps_s.
```

This is the clean positive case for C9-B.

The negative case has a finite LP dual certificate.  Let `h^r` run through
the extreme admissible gauges for `G_u`.  The primal LP is

```text
minimize    sum_{j in L} mu_j
subject to  mu in Delta(S),
            sum_j mu_j h^r(x_j) <= kappa        for every r.
```

Its dual is

```text
maximize    nu - kappa sum_r lambda_r
subject to  nu <= 1_L(j) + sum_r lambda_r h^r(x_j)   for every j in S,
            lambda_r>=0.
```

If `lambda_*>eps_s`, there is a nonnegative combination

```text
F=sum_r lambda_r h^r
```

such that

```text
nu <= F(x_j)          for high outside rows j in S cap H1,
nu <= 1+F(x_j)        for low outside rows j in L,
nu - kappa sum_r lambda_r > eps_s.
```

Interpretation: every failed-exposedness certificate with small gauge value
must pay substantial mass in the lower slice.  This is a geometric obstruction
to constructing a high-supported shadow kernel.

Important caveat: this dual certificate is not automatically a q-Lyapunov
function.  The gauges `h^r` are normalized only by row values
`0<=h^r(x_i)<=1`; their linear parts can have large `l_infty` norm.  The
repair estimate controls norm-one affine functionals such as `phi`, not these
arbitrary gauges.

## Leakage Does Not By Itself Imply q-Drift

Suppose the Step-3/Step-5 witness leaks a fixed amount below `H1`.  This gives

```text
sum_j mu_j d_j >= G tau mu(L),
```

but `mu` is not tied to `q_i`.  The repaired dynamics may still satisfy
`q_i(H1^c)=O(tau)` by `(4)`.  Therefore large shadow leakage does not imply
large q-exit or a resolvent bound without an additional coupling assumption.

The correct conditional drift statement is:

```text
If a shadow witness mu is dominated by q_i on low rows in the sense
  theta mu(A) <= C_dom q_i(A) + r(A)
for A subset H1^c,
then
  theta mu(H1^c) <= C_dom (d_i+eps_rec)/(G tau) + r(H1^c).
```

For `d_i<=c0 delta`, this is

```text
mu(H1^c) <= C_dom(c0+4) tau/(G theta) + r(H1^c)/theta.
```

Thus any large leaked mass below `H1` proves that the shadow witness is not
q-compatible.  It does not, alone, close C9.

## Candidate Contracts

### C9B-1: height-average leakage

```text
lem-shadow-average-leakage:
Let u be a global phi-maximal row and let e_u(rho)<kappa.  Then there is
mu in Delta(S_u(rho)) with

  sum_j mu_j(M-phi(x_j)) <= (2+4delta)kappa.

Hence for H1={M-phi<=G tau},

  mu(H1^c) <= (2+4delta)k/G.
```

Status: proof-ready from Step 3 plus Markov inequality.

### C9B-2: repaired-kernel high leakage

```text
lem-q-high-slice-leakage:
If ||x_i-sum_j q_i(j)x_j||_1<=eps_rec and ||phi||_*=1, then for
d_j=M-phi(x_j),

  q_i({d_j>=d_i+a}) <= eps_rec/a.

In particular, for d_i<=c0 delta and a=G tau,

  q_i(H1^c) <= (c0+4)tau/G.
```

Status: proof-ready.

### C9B-3: q-compatible shadow witness

```text
lem-q-compatible-shadow-leakage:
Assume a rho-separated shadow witness mu for row i is theta-dominated by
q_i on H1^c.  Then its H1-leakage is bounded by

  O(tau/(G theta)) + domination residual.
```

Status: proof-ready conditional lemma.  Useful only if Step 4/C12 can handle
the `1/theta` normalization.

### C9B-4: LP obstruction alternative

```text
lem-shadow-leakage-lp-alternative:
Either lambda_*(u;G,kappa)<=eps_s and an H1-supported Step-5 witness exists,
or the finite dual certificate above proves that all failed-exposedness
witnesses rely on lower-slice rows with mass >eps_s.
```

Status: finite LP duality; proof-ready after choosing a representation of the
extreme admissible gauges.  This is an obstruction/certificate, not yet a
q-drift lemma.

## Constants

Use the hierarchy

```text
delta<=1/16,        tau=sqrt(delta),
rho=R tau,          kappa=k tau,
D=2+4delta<=9/4.
```

Automatic Step-3 leakage:

```text
mu(H1^c) <= Dk/G.
```

q leakage from top core:

```text
q_i(H1^c) <= (c0+4)tau/G.
```

For `eps_s=tau/100`, Step 3 alone would require

```text
G >= 100 D k / tau,
```

which is not an acceptable fixed-constant high-slice choice.

## Gaps

1. Need a bridge from the LP obstruction certificate to either C12 alpha
   control or C13 negative-mass lower bound.
2. Need to decide whether Step 4 can operate with an unnormalized shadow
   kernel of separated q-mass `theta=Omega(tau)`.  If yes, `(5)` may be
   salvageable without requiring `theta=Omega(1)`.
3. Need a computational LP probe for `lambda_*` on the direct `A,B` samples:
   measure whether the minimum leakage is usually `O(tau)`, `O(1/G)`, or
   exactly tied to the q-compatible obstruction.
4. The dual certificate uses arbitrary exposedness gauges, not norm-one
   separators.  Any Lyapunov fallback must be built from `phi` or another
   norm-controlled functional.

## Next Handoff

1. C9-C should use `lem-q-high-slice-leakage` as the rigorous q-side drift
   input; do not try to derive q-drift from arbitrary Step-5 shadow leakage.
2. C9-D should test whether an unnormalized q-shadow kernel with mass
   `theta=Omega(tau)` can feed Step 6 while keeping residual `E=O(delta)`.
3. C12 should consume the LP obstruction case: large minimum leakage means
   lower-slice rows are essential in failed-exposedness duals, exactly where
   alpha-budget or calibrated-dual control is needed.
4. C9-E should implement the minimum-leakage LP `lambda_*` and compare it to
   q-outside mass `theta_i=q_i(S_u(rho))` and q-low leakage.
