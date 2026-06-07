# Subagent: op-exposed-hull Step 4 Shadow Recurrence

Date: 2026-06-07.  Lane: Agent B sandbox.  Status: exploratory proof
decomposition, not a canonical proof shard.

## Verdict

The Happynet-like no-cycle step should be split into a clean finite
recurrence lemma plus one still-open interface lemma.

Once Steps 1-3 provide a high bad set `H` and, for each non-exposed
`i in H`, a high-supported shadow witness distribution, recurrence is not the
hard part.  A substochastic shadow kernel with row loss `<=eps_s` always has a
closed recurrent class and a probability `pi` with

```text
||pi S - pi||_1 <= eps_s.
```

If `H` is also rowwise `q`-closed, then `pi q(H^c)<=eps_q`.  This is exactly
the normalization Step 6 needs to average the failed-exposedness circuits:
the shadow left side almost cancels, and the averaged object remains in the
bad high class.

The real blocker is the interface: convert LP non-exposedness witnesses into
such a high-supported shadow kernel, and upgrade long-lifetime closure from
distributional to rowwise or otherwise couple it to the recurrent `pi`.

## Setup

Use the global normalization

```text
P1=1,        P^2=P,        neg(p_i)<=delta,        tau=sqrt(delta),
rho=R tau,  kappa=k tau.
```

Let `q_i=p_i^+/(1+neg(p_i))`.  Fix a skeleton `R0`, `C_R=conv R0`, a bad
row-vertex set `B`, and a separator/high-face functional `phi`.  Write
`h_i=phi(p_i)`.

The input high slice is

```text
H={i in B : h_i >= theta},
q_i(H^c) <= eps_q       for i in H.              (QH)
```

For every non-exposed `i in H`, Step 3 should supply a shadow distribution
`sigma_i` with

```text
sigma_i({j : ||p_j-p_i||_1 >= rho}) = 1,
sigma_i(H) >= 1-eps_s,
sum_j sigma_i(j) h_j >= h_i - chi,    chi=O(kappa).
```

Let `S_ij=sigma_i(j)` for `i,j in H`.  Then `S` is substochastic and every row
has mass at least `1-eps_s`.

## Lemma 4A: Shadow Recurrence

Candidate contract:

```text
lem-shadow-recurrence:
Let H be finite and S>=0 be substochastic on H with row sums
m_i>=1-eps_s.  Then there are a nonempty C subset H and a probability pi
supported on C such that:

  S has no H-transition from C to H\C after row-normalization;
  ||pi S-pi||_1 <= eps_s.

If also q_i(H^c)<=eps_q for all i in H, then pi q(H^c)<=eps_q.
```

Proof.  Normalize rows:

```text
\hat S_ij=S_ij/m_i.
```

The finite stochastic matrix `\hat S` has a closed recurrent communicating
class `C` and a stationary probability `pi` on `C`.  Closedness gives no
positive `S`-mass from `C` to `H\C`.  Since `pi \hat S=pi`,

```text
||pi S-pi||_1
 <= sum_i pi_i(1-m_i)
 <= eps_s.
```

The `q` estimate is immediate from `(QH)`.

## Output For Step 6

For each `i in C`, failed exposedness supplies

```text
sum_j sigma_i(j)(p_j-p_i)
  = sum_l (beta_il-alpha_il)(p_l-p_i),
sum_l beta_il < kappa.
```

Averaging with `pi`, the shadow side is

```text
sum_j (pi S)_j p_j - sum_i pi_i p_i
```

plus leakage outside `H`.  Lemma 4A bounds its coefficient imbalance by
`O(eps_s)`.  Thus Step 6 may start from an averaged signed circuit with small
positive mass `O(kappa)` and shadow imbalance `O(eps_s)`.

Target scale:

```text
eps_s <= c_1 kappa,        eps_q <= c_2 tau,        chi <= c_3 kappa.
```

## Lemma 4B: Component Potential Alternative

Candidate contract:

```text
lem-component-resolvent-alternative:
For a substochastic q-block T on a finite set C with exit vector s=1-T1
and L>0, either

  max_i ((I-T)^(-1)1)_i <= L,

or there is a probability mu on C with

  mu s <= 1/L,
  ||mu T-mu||_1 <= 2/L.
```

Proof.  If `H_i=sum_m (T^m1)_i>L`, use the normalized occupation measure

```text
mu = H_i^(-1) sum_{m>=0} e_i T^m.
```

Then `mu s=1/H_i<1/L` and `||mu T-mu||_1<=2/H_i`.  The contrapositive gives
the Lyapunov/resolvent fallback with potential `V=(I-T)^(-1)1`.  If
`||V||_infty<=A/tau`, the bad-kernel resolvent closes the component at cost
`O(delta/tau)=O(tau)`.

## Lemma 4C: No-Escape Shadow Component

Candidate contract:

```text
lem-no-escape-shadow-component:
If H is rowwise eps_q-closed under q and every i in H has a rho-separated
shadow witness with H-leakage eps_s, then there is a probability pi on H such
that

  ||pi S-pi||_1 <= eps_s,
  pi q(H^c) <= eps_q,

and pi-a.e. source has rho-separated shadow support.
```

This is the Step 4 package to hand to circuit aggregation.

## Open Interface Lemma

Candidate open contract:

```text
lem-shadow-exit-gap:
For a high bad slice coming from Steps 1-3, either the LP shadow witnesses can
be chosen with H-leakage O(tau), or q admits a Lyapunov drift and the
bad-kernel resolvent closes the slice.
```

This is the genuine remaining Step 4 gap.  LP failed-exposedness gives only a
barycentric outside-`rho` witness with high average height.  It does not by
itself force most witness mass to stay in the selected high slice.  Similarly,
long bad lifetime naturally gives a quasi-stationary distribution, not
rowwise closure of every high vertex.

## Constants

Safe hierarchy for this step:

```text
delta <= delta_0,
rho=R tau,              kappa=k tau,
eps_s <= k tau/100,     eps_q <= tau/100,
chi <= k tau/10,        L0=A/tau.
```

Then the component resolvent cost is `4 delta L0=4A tau`, and the recurrence
imbalance is lower order if `eps_s+eps_q+chi << kappa << rho`.

## Counterexample Warnings

1. Dense regular polygons have shadow recurrent classes in pure convex
   geometry.  Step 4 alone must not try to contradict them; Steps 6-7 must use
   `P^2=P` and `neg(p_i)<=delta`.
2. A recurrent class for `S` is useless unless it also carries averaged or
   rowwise `q`-closure.
3. Deterministic shadow-edge paths can have length depending on `|H|`.
   Passing directly to a recurrent class of the normalized kernel avoids this
   dimension-dependent path length.
4. If the high slice is too thin, the shadow witness can leak below it with
   large mass while keeping only its average height high.

## Next Handoff

1. Step 1 must specify rowwise high-slice `q`-closure, or provide a coupling
   that proves `pi q(H^c)<=O(tau)` for the Step 4 recurrent `pi`.
2. Step 3 must output a full shadow kernel `S`, not just one row outside the
   `rho`-ball, and must bound `1-S1`.
3. Step 6 should budget an `O(eps_s)` coefficient imbalance in the averaged
   failed-exposedness identity.
4. Computational check: on frozen LP-game examples, construct `S`, find
   recurrent classes of normalized `S`, and measure `pi q(H^c)`.
