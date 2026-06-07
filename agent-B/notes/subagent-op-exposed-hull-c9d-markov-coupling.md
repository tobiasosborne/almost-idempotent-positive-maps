# Subagent C9-D: Markov Coupling / Distributional-To-Rowwise Closure

Date: 2026-06-07.  Lane: Agent B sandbox.  Status: exploratory lemma note,
not a canonical proof shard.

## Task

Test whether `m q(B^c)<=xi` and `||mT-m||_1<=xi` upgrade to rowwise closure on
a subset/recurrent class.  If not, isolate a weaker `pi`-coupled closure for
Step 6.  Inputs read: blocker subplans, Step 1, Step 4.

## Setup

`B` is finite.  The repaired kernel `q` is stochastic on all rows, with bad
block `T_ij=q_i(j)` and exit `s_i=q_i(B^c)=1-sum_{j in B}T_ij`.  Let `m` be a
probability on `B`, usually the occupation/quasi-stationary law, and write

```text
xi_s=ms,        xi_T=||mT-m||_1.        Target: xi_s,xi_T=O(tau).
```

## What Markov Theory Gives For Free

For every `A subset B`,

```text
mq(A^c)=mT(B\A)+mq(B^c)
      <= m(B\A)+(1/2)||mT-m||_1+xi_s
      <= m(B\A)+xi_T+xi_s.                 (1)
```

For `G_lambda={i in B:s_i<=lambda}`,

```text
m(B\G_lambda)<=xi_s/lambda,
mq(G_lambda^c)<=xi_s/lambda+xi_T+xi_s.     (2)
```

If `xi_s,xi_T<=E tau` and `lambda=K tau`, the loss is only `E/K+O(tau)`.  Fixed
`K` gives constant pruning loss; `K~1/tau` destroys rowwise `O(tau)` scale.

Density transfer is available but must be assumed:

```text
pi_i<=D m_i on A        =>        pi q(A^c)<=D m q(A^c).      (3)
```

Step 4 recurrence does not by itself give dimension-free `D`.

## Counterexample: No Rowwise Core

Take

```text
B={1,...,N},
q_i = delta_{i+1} for i<N,
q_N(B^c)=1,
m_i=1/N.
```

Then

```text
m q(B^c)=1/N,
||mT-m||_1=2/N.
```

These are `<=C tau` after taking `N>=2/(C tau)`.

Every nonempty `H subset B` has a row with full leakage:

```text
if N in H, then q_N(H^c)=1;
if N notin H and k=max H, then q_k(H^c)=1.
```

Thus `max_{i in H}q_i(H^c)=1` for every nonempty `H`.  Geometry may rule this
out, but Markov quasi-closure alone does not.

## Counterexample: Shadow Recurrence Need Not Be q-Closed

Use the same path for `q`, and set

```text
S_i=delta_{i+1} for i<N,
S_N=delta_N.
```

Uniform `m` has `||mS-m||_1=2/N`, but the closed shadow class `{N}` has
`pi=delta_N` and `pi q(B^c)=1`.  So q-closure does not transfer to arbitrary
shadow recurrent classes.

## Positive Replacement: pi-Coupled Closure

The useful replacement is a common averaging law `pi` satisfying q-closure and
shadow-stationarity:

```text
pi q(H^c) <= xi_q,
||pi S-pi||_1 <= xi_S,
pi(1-S1) <= xi_S.
```

Here `S` is the substochastic shadow kernel of failed-exposedness witnesses.
Averaging Step-5 identities with weights `pi_i`, the shadow side contributes

```text
sum_j (pi S)_j p_j - sum_i pi_i p_i,
```

The imbalance is controlled by `||piS-pi||_1` plus row loss; q-repair errors
are controlled by `pi q(H^c)`.  Pointwise q-closure is not needed.

## How To Obtain pi-Coupled Closure

### Route 1: use the original quasi-stationary measure

Best target: set `pi=m`.  Step 1 gives the q side.  If `h_i=M-phi(p_i)`,
`eps_pc<=4delta`, and `H_gamma=B cap {h<=gamma}`, then

```text
m q(H_gamma^c)
 <= m q(B^c) + (m h + eps_pc)/gamma.        (5)
```

If `mh<=A delta`, `gamma=G tau`, and `mq(B^c)<=E tau`, then

```text
m q(H_gamma^c) <= (E + (A+4)/G) tau.
```

Thus C9-B should choose witnesses with `||mS-m||_1=O(tau)` and
`m(1-S1)=O(tau)` on the same slice.

### Route 2: density-controlled shadow class

If Step 4 insists on a shadow recurrent `pi`, require

```text
pi_i <= D m_i             on H,
D = O(1).
```

Then (3) transfers q-closure; without it, the path/sink example blocks the
claim.

### Route 3: recurrent class inside a rowwise-good ambient core

Let

```text
G = {i in H : q_i(H^c) <= K tau}.
```

If normalized shadow recurrence is forced into `G`, every stationary law on
that class satisfies

```text
pi q(H^c) <= K tau.
```

C9-B/C9-C must prove: witnesses avoid `H\G`, or visits to `H\G` produce
height/Lyapunov drift and the resolvent closes.

## Candidate Contracts

Proof-ready Markov lemma:

```text
lem-markov-set-flow:
For finite B, substochastic T=q|_B, exit s=1-T1, probability m on B, and
every A subset B,
  m q(A^c) <= m(B\A) + (1/2)||mT-m||_1 + m s.
Consequently low-exit quantile and density-transfer bounds (2)-(3) hold.
```

Negative observation:

```text
obs-distributional-not-rowwise:
There are finite substochastic kernels with m q(B^c), ||mT-m||_1 arbitrarily
small but with no nonempty H subset B satisfying max_{i in H} q_i(H^c)<1.
```

Preferred C9-D interface:

```text
lem-pi-coupled-shadow-q-closure:
Let H be a high bad set, q the repaired kernel, S a substochastic shadow
kernel with rho-separated witness rows, and pi a probability on H.  If
  pi q(H^c)<=xi_q,
  ||piS-pi||_1<=xi_S,
  pi(1-S1)<=xi_S,
then Step-6 averaging may use pi with q-leakage xi_q and shadow imbalance
O(xi_S).
```

## Verdict

C9-D does **not** prove distributional-to-rowwise closure; that statement is
false in pure finite Markov theory.  The replacement is to keep the q-closed
measure and shadow averaging measure coupled.

Most promising route:

```text
C9-A produces m q(H^c)=O(tau) on a high slice H;
C9-B chooses shadow witnesses with ||mS-m||_1=O(tau);
Step 6 averages with pi=m.
```

If Step 4 uses a recurrent shadow class, it needs density comparison or
confinement to a rowwise q-good ambient core.  Neither follows from Markov
quasi-stationarity alone.

## Next Handoff

1. C9-A: target `mh=O(delta)` or a positive-mass restricted high-slice law.
2. C9-B: make the shadow kernel approximately stationary for the same `m`.
3. C9-C: use the deterministic path as the minimal Lyapunov fallback test.
4. C9-E: compute `||mS-m||_1`; recurrent classes alone can pick q-leaky sinks.
