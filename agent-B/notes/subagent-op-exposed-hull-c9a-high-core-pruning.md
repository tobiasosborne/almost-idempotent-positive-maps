# Subagent C9-A: High-Core Pruning

Date: 2026-06-07.  Lane: Agent B sandbox.  Status: exploratory lemma note,
not a canonical proof shard.

## Task

Campaign: C9 shadow-exit/interface lemma for `op-exposed-hull`.

This note attacks the two-scale high-core and pruning step.  The requested
input is a quasi-stationary bad measure `m` with small bad exit, plus a
separator-height function

```text
h_i = M - phi(p_i).
```

The target is to decompose

```text
H0 = {i in B : h_i <= A0 delta},
H1 = {i in B : h_i <= G tau},
tau = sqrt(delta),
```

and prove either useful pruning to rows that are `q`-closed into `H1`, or an
honest fallback.

## Setup

Rows are signed probabilities `p_i` satisfying

```text
P1=1,        P^2=P,        neg(p_i)<=delta,        tau=sqrt(delta).
```

For `a_i=neg(p_i)`, set

```text
q_i = p_i^+/(1+a_i).
```

Use the positive-coordinate repair estimate from the bad-kernel note:

```text
||p_i - sum_j q_i(j)p_j||_1 <= eps,        eps <= 4 delta.      (PC)
```

Let `phi` be affine with `l1` dual Lipschitz constant `L_phi<=1`, and set

```text
phi_i = phi(p_i),        M=max_all_rows phi_i,        h_i=M-phi_i.
```

The global maximum matters.  If `M` is only a maximum over a selected bad
slice, then some `q_i`-successor can have negative height and the Markov
height bounds below are invalid.

Let `B` be the current bad set, and write

```text
s_i = q_i(B^c),
T_ij = q_i(j) for i,j in B.
```

For a probability measure `m` on `B`, use:

```text
m s = sum_i m_i s_i <= eta,
||mT-m||_1 <= zeta                         (optional stationarity defect)
```

The estimates below separate what follows from distributional closure alone
from what needs rowwise closure.

## 1. Rowwise Two-Scale Drift

From `(PC)` and the Lipschitz bound on `phi`,

```text
|phi_i - sum_j q_i(j) phi_j| <= eps.
```

Therefore

```text
sum_j q_i(j) h_j
  = M - sum_j q_i(j) phi_j
 <= M - phi_i + eps
  = h_i + eps.                              (1)
```

Since `h_j>=0`, Markov's inequality gives, for every `gamma>0`,

```text
q_i({h > gamma}) <= (h_i+eps)/gamma.        (2)
```

With

```text
alpha = A0 delta,
gamma = G tau,
H0 = B cap {h<=alpha},
H1 = B cap {h<=gamma},
```

every `i in H0` satisfies

```text
q_i(H1^c)
 <= q_i(B^c) + q_i({h>gamma})
 <= s_i + (A0 delta + 4 delta)/(G tau)
 =  s_i + ((A0+4)/G) tau.                   (3)
```

This is the clean rowwise high-core statement.

Important scale point: `H0` must be an `O(delta)`-core.  If one starts with
`h_i=O(tau)`, then (2) only gives constant leakage into `{h>G tau}`.

## 2. Distributional Closure Of The High Core

Let

```text
m0 = m(H0),
nu = m|H0 / m0                              (if m0>0).
```

Averaging (3) gives

```text
nu q(H1^c)
 <= (m_{H0}s)/m0 + ((A0+4)/G) tau
 <= eta/m0 + ((A0+4)/G) tau.                (4)
```

Thus if

```text
m0 >= eta/(S tau),
```

then

```text
nu q(H1^c)
 <= (S + (A0+4)/G) tau.                     (5)
```

This is the useful distributional pruning lemma.  It does not say every row in
`H0` is good; it says the normalized high-core measure is good on average.

## 3. Rowwise Pruning From The Distributional Bound

Set

```text
theta = eta/m0 + ((A0+4)/G) tau.
```

If `theta<1`, define the rowwise-good part

```text
H0_good(lambda)
  = {i in H0 : q_i(H1^c) <= lambda tau}.
```

By Markov,

```text
nu(H0 \ H0_good(lambda))
 <= theta/(lambda tau).                     (6)
```

A dimension-free useful choice is possible only when `theta=O(tau)`.  For
example, if `m0>=eta/(S tau)`, then

```text
theta <= C0 tau,        C0 = S + (A0+4)/G,
```

and

```text
nu({i in H0 : q_i(H1^c) > sqrt(C0) sqrt(tau)})
 <= sqrt(C0) sqrt(tau).                     (7)
```

For genuinely rowwise `O(tau)` leakage on a large subcore, use a fixed
threshold `lambda tau`:

```text
nu({i in H0 : q_i(H1^c) > lambda tau})
 <= C0/lambda.                              (8)
```

So to retain, say, `90%` of the high-core mass with rowwise `O(tau)` leakage,
one must choose the hidden constant in `O(tau)` about `10 C0`.  This is
acceptable for C9, but the constants must be carried into Step 6.

One can also split exit and height leakage:

```text
nu({s_i > S1 tau}) <= eta/(m0 S1 tau),
nu({q_i({h>G tau}) > S2 tau}) <= ((A0+4)/(G S2)).
```

This is useful when Step 4 wants separate bad-set closure and high-slice
closure.

## 4. What Quasi-Stationarity Adds

If `||mT-m||_1<=zeta`, then high-core mass cannot disappear under one killed
`q`-step without being visible in `m`.

Indeed,

```text
mT(H1)
 >= sum_{i in H0} m_i q_i(H1)
 >= m0 - m_{H0}s - m0 ((A0+4)/G) tau
 >= m0 - eta - m0 ((A0+4)/G) tau.
```

Since `|mT(H1)-m(H1)|<=zeta`, this gives

```text
m(H1)
 >= m0 - eta - zeta - m0 ((A0+4)/G) tau.    (9)
```

So a large `O(delta)` core forces a large `O(tau)` high slice for any
quasi-stationary measure.  This is a consistency estimate, not a substitute
for rowwise pruning.

## 5. The Requested Fallback: What Is And Is Not True

The tempting statement

```text
if m(H0) is small, then there is a Lyapunov/resolvent fallback
```

is false from the hypotheses above.

Toy obstruction: take a stochastic idempotent kernel with two closed states
inside `B`, one at height `0` and one at height `G tau/2`.  Let `m` be the
stationary measure on the lower closed state.  Then

```text
m q(B^c)=0,        ||mT-m||_1=0,        m(H0)=0,
```

but there is no bad-exit drift and no resolvent bound.  The measure is simply
quasi-stationary on the wrong closed class.  This example is not a
counterexample to `op-exposed-hull`; it is a counterexample to the proposed
C9-A fallback as a standalone Markov lemma.

Therefore C9-A must be stated with an additional interface hypothesis.  The
right missing quantity is not just `m(H0)`, but **return mass to the high
core** for the long-lived class being analyzed.

## 6. Corrected Alternatives

### Alternative A: High-Core Mass Hypothesis

This is immediately proof-ready.

```text
Assume m(H0)>=eta/(S tau).
Then the normalized high-core measure nu=m|H0/m(H0) satisfies
  nu q(H1^c) <= (S+(A0+4)/G) tau.
After Markov pruning, most of nu is supported on rows i with
  q_i(H1^c) <= C tau.
```

This is the clean C9-A output for Step 4.

### Alternative B: Occupation-Return Hypothesis

Suppose `m` is not an arbitrary quasi-stationary measure but a normalized
occupation measure of the killed bad chain started from a distribution
`lambda` on `H0`:

```text
m = L^{-1} sum_{t>=0} lambda T^t,
L = sum_{t>=0} lambda T^t 1.
```

Then

```text
eta = m s = 1/L.
```

The high-core pruning condition becomes

```text
m(H0) >= 1/(S tau L),
```

equivalently,

```text
expected number of visits to H0 before bad exit >= 1/(S tau).   (10)
```

So the precise dichotomy is:

```text
many high-core returns
  -> normalize visits to H0 and get q-closure into H1;

few high-core returns
  -> the chain drops from the top core and spends its long lifetime elsewhere.
```

The second branch is not yet a resolvent fallback.  It is a handoff to C9-B/C:
one must either show that this drop produces a separator-height Lyapunov
function, or restart the high-core argument on the lower long-lived component
with a new top face.

### Alternative C: Rowwise Top-Core Closure Hypothesis

If C9-C can supply directly that the relevant top rows satisfy

```text
s_i <= S tau        for i in H0,
```

then (3) gives rowwise closure

```text
q_i(H1^c) <= (S+(A0+4)/G) tau        for i in H0.
```

This bypasses distributional pruning entirely.  It is the strongest interface
for Step 4, but it is not implied by distributional quasi-stationarity.

## 7. Candidate Contracts

Proof-ready contract:

```text
lem-c9a-high-core-distributional-pruning:
Let q be the repaired kernel and assume (PC) with error eps<=4delta.  Let
phi be 1-Lipschitz in l1, M=max_all_rows phi(p_i), h_i=M-phi(p_i), and
B be a bad set.  Put H0=B cap {h<=A0 delta}, H1=B cap {h<=G tau}.

If m is a probability on B with m q(B^c)<=eta and m0=m(H0)>0, then
the normalized restriction nu=m|H0/m0 satisfies

  nu q(H1^c) <= eta/m0 + ((A0+4)/G) tau.

Consequently, if m0>=eta/(S tau), then nu q(H1^c)
<= (S+(A0+4)/G)tau, and Markov pruning gives a submeasure of nu of mass
at least 1-C0/lambda supported on rows i with q_i(H1^c)<=lambda tau.
```

Useful quasi-stationary corollary:

```text
lem-c9a-high-slice-persistence:
Under the previous hypotheses, if additionally ||mT-m||_1<=zeta, then

  m(H1) >= m(H0) - eta - zeta - m(H0)((A0+4)/G)tau.
```

Open interface contract:

```text
lem-c9a-return-or-drift:
For the specific long-lived bad component arising in C9, either the
occupation measure has high-core return mass satisfying (10), or the drop
away from H0 yields a Lyapunov/resolvent fallback.
```

This last statement remains open.  It needs extra structure beyond
distributional quasi-stationarity.

## 8. Constants

Recommended safe bookkeeping:

```text
delta <= 10^-4,
tau = sqrt(delta),
A0 >= 8,
G >= 100(A0+4),
eta <= e0 tau,
zeta <= e0 tau.
```

If `m0>=eta/(S tau)`, then

```text
nu q(H1^c) <= (S + 1/100) tau.
```

Choosing `lambda=100(S+1/100)` retains at least `99%` of the normalized
high-core mass with rowwise leakage at most `lambda tau`.

If Step 6 can tolerate larger constants, reduce `G` accordingly.  The key
scale is:

```text
O(delta)-core -> O(tau)-slice with O(tau) leakage.
```

## Verdict

C9a/C9b are sharpened as follows.

What is proved:

```text
large enough high-core mass
  -> distributional q-closure into H1
  -> rowwise pruning on most of the normalized high core.
```

What is not proved:

```text
small high-core mass
  -> Lyapunov/resolvent fallback.
```

That implication is false for an arbitrary quasi-stationary bad measure.  The
next handoff must add a return/drift hypothesis tied to the particular
long-lived component selected by the bad-kernel resolvent.

## Next Handoff

1. C9-B should test whether failed-exposedness shadow witnesses supply the
   missing return-to-high-core condition.
2. C9-C should formalize a true Lyapunov fallback: identify a potential whose
   expected drift is negative when high-core returns fail.
3. C9-D should work with occupation measures, not arbitrary stationary
   measures, because the relevant branch is "many returns to H0" versus
   "long lifetime after dropping below H0".
4. Computational C9-E should record `m(H0)`, expected returns to `H0`, and
   `nu q(H1^c)` separately.  Lumping them into a single q-exit score hides the
   real obstruction.
