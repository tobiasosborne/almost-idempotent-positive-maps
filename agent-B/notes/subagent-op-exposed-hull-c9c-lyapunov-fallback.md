# Subagent C9-C: Lyapunov/Resolvent Fallback

Date: 2026-06-07.  Lane: Agent B sandbox.  Status: exploratory lemma note,
not a canonical proof shard.

## Verdict

The Lyapunov fallback can be made proof-ready as a finite Markov-chain
package.  It should not assert that arbitrary shadow-witness leakage creates
`q`-drift; that implication is the remaining C9 interface gap.

```text
If the killed repaired kernel admits a bounded potential with additive drift
c tau, then the bad lifetime is O(1/tau), and the bad-kernel resolvent closes.
```

Equivalently, if the lifetime is not `O(1/tau)`, the resolvent itself produces
a quasi-stationary occupation measure with `O(tau)` exit.  C9 should feed that
measure to high-core pruning and shadow recurrence rather than trying to
force a rowwise statement immediately.

## Setup

```text
P1=1,        P^2=P,        neg(p_i)<=delta,        tau=sqrt(delta),
q_i=p_i^+/(1+neg(p_i)).
```

For a finite bad/high set `E`, let
```text
T_ij=q_i(j) for i,j in E,
s_i=1-sum_{j in E}T_ij=q_i(E^c).
```

The bad-kernel note already proves that if
```text
L_E=||(I-T)^(-1)||_{inf->inf} <= A/tau,
```
then rows in `E` are within `Gamma+4A tau` of the current skeleton hull,
provided rows outside `E` are within `Gamma`.

## Lemma C9C.1: Foster/Lyapunov Resolvent Bound

```text
lem-killed-kernel-lyapunov:
Let E be finite and T>=0 be substochastic on E.  Suppose there are numbers
lambda>0, Vmax<infty and a function V:E->[0,Vmax] such that
  sum_j T_ij V_j <= V_i - lambda        for every i in E.
Then sum_{m>=0} T^m 1 is finite and
  ||(I-T)^(-1)||_{inf->inf} <= Vmax/lambda.
```

Proof.  Summing the drift inequality along the killed chain gives, for every
`N`,
```text
lambda sum_{m=0}^{N-1} (T^m 1)_i
  <= V_i - (T^N V)_i
  <= Vmax.
```

Let `N` tend to infinity.  In the application take `lambda=c tau`; if
`Vmax=O(1)`, the expected bad lifetime is `O(1/tau)`.

## Lemma C9C.2: Exit-Mass Fallback

```text
lem-rowwise-exit-resolvent:
If q_i(E^c)>=lambda for every i in E, then
  ||(I-T)^(-1)||_{inf->inf} <= 1/lambda.
```

This is Lemma C9C.1 with `V=1`, since `T1<=1-lambda`.  At
`lambda=c tau`, lifetime is at most `1/(c tau)`.  Thus a failed pruning
attempt closes immediately if every remaining candidate row leaks from the
chosen high/bad set with mass at least `c tau`.

## Lemma C9C.3: Height-Window Fallback

Let `phi` be the separator from the distance dual, normalized with
`||phi||_Lip<=1`.  Set
```text
M=max_rows phi(p_i),
h_i=M-phi(p_i),
E=B cap {h_i<=gamma},
V_i=1-h_i/gamma       for i in E.
```

Then
```text
V_i - sum_{j in E} q_i(j)V_j
  = q_i(E^c) + gamma^(-1) sum_{j in E}q_i(j)h_j - h_i/gamma
  >= q_i(E^c) - h_i/gamma.
```

Therefore:
```text
lem-height-window-fallback:
If every i in E satisfies
  q_i(E^c) >= h_i/gamma + c tau,
then ||(I-T)^(-1)||_{inf->inf} <= 1/(c tau).
```

In particular, for a top core `E0=B cap {h_i<=alpha}` inside
`E=B cap {h_i<=gamma}`, with
```text
alpha=A0 delta,        gamma=G tau,
```
the hypothesis becomes
```text
q_i(E^c) >= (A0/G) tau + c tau        for i in E0.
```

This is the clean height-based fallback.  Rows in the `O(delta)` top core
either have `O(tau)` leakage into the `G tau` high window, or they give a
bounded-lifetime certificate.

## Lemma C9C.4: Occupation-Measure Alternative

```text
lem-resolvent-occupation-alternative:
Let T be a finite substochastic kernel on E and s=1-T1.  For L0>0, either
  ||(I-T)^(-1)||_{inf->inf} <= L0,
or there is a probability mu on E with
  mu s <= 1/L0,
  ||mu T-mu||_1 <= 1/L0.
```

If `T` has a closed recurrent class, take `mu` stationary there and the right
side holds with zero.  Otherwise choose `i` with expected killed lifetime
`H_i>L0` and set
```text
mu = H_i^(-1) sum_{m>=0} e_i T^m.
```

Then `mu1=1`,
```text
mu s = 1/H_i < 1/L0,
mu-muT = H_i^(-1)e_i,
```
so `||muT-mu||_1<1/L0`.

At the target scale `L0=A/tau`, failure of the fallback produces
```text
mu q(E^c) <= tau/A,
||muT-mu||_1 <= tau/A.
```

This is the correct input to C9-A/C9-D pruning and coupling.

## Distributional No-Quasi-Stationary Certificate

The occupation alternative gives a useful dual form:
```text
lem-no-quasistationary-implies-resolvent:
If every probability mu on E satisfies
  mu q(E^c) + ||muT-mu||_1 >= c tau,
then ||(I-T)^(-1)||_{inf->inf} <= 2/(c tau).
```

Proof is by contraposition from Lemma C9C.4.  This is often easier to prove
than a rowwise potential because it matches the output of long-lifetime
Markov occupation.

## How This Interfaces With C9

C9 should use the fallback as the following dichotomy.
```text
Choose a high/bad set E.

1. If rowwise or distributional leakage from E is >= c tau in the senses
   above, apply C9C.1-C9C.4 and close by the bad-kernel resolvent.

2. Otherwise, a quasi-stationary measure survives with O(tau) q-exit and
   O(tau) stationarity defect.  Pass that measure to high-core pruning,
   shadow-witness leakage, and Markov coupling.
```

The exact gap is:
```text
Large leakage of failed-exposedness shadow witnesses sigma_i below the high
slice does not by itself imply large q_i(E^c) or height drift for the repaired
kernel q.
```

To turn shadow leakage into this fallback, C9-B or C9-D must add a coupling or
calibration statement relating shadow witness mass to the repaired `q`-flow.
Without that extra input, the Lyapunov package is true but cannot consume a
bare shadow-leakage failure.

## Constants

Safe hierarchy for later packaging:
```text
eps_PC <= 4 delta,
tau=sqrt(delta),
gamma=G tau,
alpha=A0 delta,
L0=A/tau.
```

Rows with `h_i<=alpha` have height-window loss `h_i/gamma<=(A0/G)tau`.
Choose `G>=100A0`.  If the remaining `q`-exit is at least `c tau`, Lemma
C9C.3 gives lifetime at most `1/(c tau)`, and the bad-kernel estimate gives
distance error at most
```text
Gamma + 4delta/(c tau) = Gamma + (4/c)tau.
```

For the occupation alternative, choosing `A>=100/c` makes the produced
quasi-stationary errors at most `0.01 c tau`.

## Next Handoff

1. C9-A should use Lemma C9C.4 as its formal input: start from a
   quasi-stationary `mu` rather than a rowwise closed set.
2. C9-B should either prove a coupling from shadow leakage to `q`-exit, or
   explicitly route uncoupled shadow leakage to C12 instead of C9-C.
3. C9-D should formulate the `mu`-coupled closure needed by Step 6:
   ```text
   mu q(E^c)=O(tau),        ||muT-mu||_1=O(tau).
   ```
4. Agent A-ready package should split C9-C into three tiny lemmas:
   killed-kernel Lyapunov, rowwise exit, and occupation-measure alternative.
