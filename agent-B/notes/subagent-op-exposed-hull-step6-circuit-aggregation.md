# Step 6: Circuit Aggregation Across A Quasi-Closed Bad Class

Date: 2026-06-07. Lane: Agent B sandbox. Status: exploratory, not canonical.

## Verdict

Step 6 does not close from the current inputs alone.  Both natural
normalizations produce global identities, but both are blocked by the same
quantity: the uncontrolled `alpha` mass in the failed-exposedness circuits.

The usable interface is now precise:

```text
aggregation closes if either
  (i) averaged alpha mass is O(1), or at worst O(1/tau) with a compatible
      Step 7 residual-circuit lower bound; or
  (ii) the failed-exposedness duals can be chosen so their alpha side is
      calibrated to q-flow.
```

Without this, q-quasi-closedness controls only Markov flow, not the lower-face
dual variables.

## Setup

Rows are `x_i=p_i`, with

```text
P1=1,        P^2=P,        neg(p_i)<=delta,        tau=sqrt(delta).
q_i=p_i^+/(1+neg(p_i)).
||x_i-sum_j q_i(j)x_j||_1 <= eps,        eps=4delta.      (PC)
```

Let `B` be a high bad class and let `m` be q-quasi-closed:

```text
m q(B^c) <= xi,        ||m-mq|_B||_1 <= xi,        xi=O(tau).
```

For each non-exposed `b in B`, Step 5 gives

```text
sum_{j in S_b} nu^b_j (x_j-x_b)
  = sum_i (beta^b_i-alpha^b_i)(x_i-x_b),              (FE_b)

nu^b in Delta(S_b),        S_b={j: ||x_j-x_b||_1>=rho},
alpha^b,beta^b>=0,         |beta^b|_1<kappa.
```

Writing `A_b=|alpha^b|_1`, `B_b=|beta^b|_1`, this is the affine identity

```text
sum_{j in S_b} nu^b_j x_j + sum_i alpha^b_i x_i
  = sum_i beta^b_i x_i + (1+A_b-B_b)x_b.             (C_b)
```

The controlled side is `beta`; the hard side is `alpha`.

## Normalization 1: m-Average

Average `(C_b)` with weights `m_b`.  Define

```text
Nu_j=sum_b m_b nu^b_j,      Alpha_i=sum_b m_b alpha^b_i,
Beta_i=sum_b m_b beta^b_i, A=sum_i Alpha_i, B=sum_i Beta_i<=kappa,
Lambda_b=m_b(1+A_b-B_b).
```

Then

```text
sum_j Nu_j x_j + sum_i Alpha_i x_i
  = sum_i Beta_i x_i + sum_b Lambda_b x_b.           (AVG)
```

Both sides have total mass `1+A`.  After normalizing by `1+A`,

```text
controlled beta fraction <= kappa,
far witness fraction >= 1/(1+A).
```

If `A=O(1)`, this is a clean input to Step 7.  If `A=O(1/tau)`, it may still
work only if Step 7 tolerates separated witness mass `Omega(tau)`.  If
`A>>1/tau`, the square-root scale is lost.

Gap: failed-exposedness minimizes `|beta|_1`; it gives no bound on `A`.

## Normalization 2: q-Flow Balance

Use `(PC)` to replace the base row in `(C_b)`:

```text
x_b=sum_j q_b(j)x_j+e_b,        ||e_b||_1<=eps.
```

Substitution and m-averaging give residual

```text
<= eps * sum_b m_b(1+A_b-B_b) <= 4delta(1+A).
```

The q-flow leakage term is weighted by `m_b(1+A_b-B_b)`, not by `m_b`.  Hence
the quasi-closed estimate for `m` applies only if these weights are comparable,
again requiring an alpha budget or a pointwise `A_b` bound.

A more ambitious flow balance asks for weights `omega_b` with

```text
sum_b omega_b nu^b_j ~= omega_j(1+A_j-B_j)       on B.
```

That cancels the base/witness flow, but it is an extra eigenvector condition
on the chosen dual witnesses.  It is not implied by q-quasi-closedness, and
the surviving circuit still contains the uncontrolled `alpha` distribution.

## Candidate Contracts

Conditional, proof-ready target:

```text
lem-circuit-aggregation-with-alpha-budget:
Assume (PC), q-exit/stationarity defect xi for m on B, and circuits (FE_b)
with |beta^b|_1<=kappa.  If sum_b m_b |alpha^b|_1<=M, then there is a
normalized affine circuit with controlled beta mass <=kappa, q-flow residual
O((delta+xi)(1+M)), and separated witness mass >=1/(1+M).
```

The genuinely needed stronger target:

```text
lem-calibrated-circuit-aggregation:
In a q-quasi-closed high bad class, failed-exposedness witnesses can be chosen
with M=O(1), or with alpha supported in q-controlled rho-shadows.
```

This is open.

## Concrete Dual Obstruction

In the LP dual, `alpha_i` is the multiplier for the lower constraint

```text
ell(x_i-v)>=0.
```

If the lower face contains a nontrivial affine dependence

```text
sum_i c_i x_i=0,        sum_i c_i=0,
```

supported where `ell(x_i-v)=0`, its positive and negative parts can be inserted
into the dual without increasing `|beta|_1`.  This makes `alpha` arbitrarily
large while preserving the same failed-exposedness value.  q-closedness does
not see this unless the inserted lower-face circuit leaks under `q` or already
forces the Step 7 negative-mass lower bound.

This is the exact obstruction shown abstractly by dense polygon warnings.  The
known polygon examples have large negative mass, so they are not
`op-exposed-hull` counterexamples; they only refute a Step 6 proof that ignores
`alpha`.

## Constants

Use

```text
rho=R tau,        kappa=k tau,        xi<=c_q tau,        eps=4delta.
```

The conditional residual is

```text
O((delta+xi)(1+M)).
```

For `O(tau)` residual, `M<=C/tau` suffices.  For a direct constant-fraction
separated circuit, `M=O(1)` is needed.

## Next Handoff

1. Step 5 must retain complementarity support for `alpha` and `beta`.
2. LP/game mining should look for an alpha-budget or calibrated-dual
   certificate.
3. Step 7 must test whether witness mass `Omega(tau)` is enough.
4. If no budget exists, prove every lower-face null circuit either leaks under
   `q` by `Omega(tau)` or already forces `max_i neg(p_i)>=c rho^2`.
