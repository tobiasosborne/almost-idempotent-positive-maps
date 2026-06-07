# Subagent: Bad-Kernel Alternative For `op-exposed-hull`

Date: 2026-06-07.  Lane: Agent B sandbox.  Status: exploratory, not a
canonical proof shard.

## Setup

Let `P1=1`, `P^2=P`, and write the rows as signed probabilities `p_i`, with
`neg(p_i)<=delta`.  Put `tau=sqrt(delta)` and assume `delta<=1/16`.  For
`a_i=neg(p_i)`, define the repaired probability row `q_i=p_i^+/(1+a_i)`.

Since `p_i=(1+a_i)q_i-a_i r_i` and `p_iP=p_i`,

```text
||p_i-sum_j q_i(j)p_j||_1 <= a_i(2+4delta) <= 4delta.      (PC)
```

Fix a candidate exposed skeleton `R`, set `C_R=conv R`, let `B` be a bad index
set, and put `G=B^c`.  Write `d_i=dist_1(p_i,C_R)`,
`T=(q_i(j))_{i,j in B}`, and `s_i=q_i(G)=1-(T1)_i`.  The intended global proof
takes `B={i:d_i>D tau}`, so `d_j<=D tau` for `j in G`.  The rows in `B` need
not be vertices.

## Resolvent Half

Lemma candidate, proof-ready.  Suppose every `G`-row is within `Gamma` of
`C_R`, `rho(T)<1`, and `L=||(I-T)^(-1)||_{inf->inf}`.  Then every `i in B`
satisfies

```text
dist_1(p_i,C_R) <= Gamma + 4delta L.
```

In particular, if `Gamma=O(tau)` and `L<=A/tau`, then all bad rows are
`O(tau)` from `C_R`.

Proof.  Distance to a convex set is convex, and `(PC)` gives
`d <= 4delta 1 + T d + Gamma s`.  Multiplying by `(I-T)^(-1)` gives
`d <= 4delta (I-T)^(-1)1 + Gamma (I-T)^(-1)s`.  For a substochastic kernel
with `rho(T)<1`,

```text
(I-T)^(-1)s = sum_{m>=0} T^m(1-T1)=1.
```

This proves the estimate.  Probabilistically, `L` is the maximal expected
number of visits to `B` before hitting `G`; each visit costs only `4delta`.

## Closed-Bad-Class Half

This is the central remaining lemma.  A precise useful form is:

```text
Closed-bad-class augmentation.
Choose D >> R >> 1 >> k > 0, set rho=R tau and kappa=k tau, and let R0 be a
maximal 4rho-separated subset of W_{rho,kappa}.  Let C_R=conv R0 and let B be
the row vertices with dist_1(v,C_R)>D tau, enlarged by their rho-clusters.

If ||(I-T)^(-1)||_{inf->inf} > A/tau, then B contains a row vertex w with
dist_1(w,C_R)>4rho and e_w(rho)>=kappa.
```

This would contradict maximality of `R0`, so the resolvent half would finish
`op-exposed-hull`.

I do not have a proof.  The statement is believable only with the
maximal/high-bad definition of `B`; long lifetime for an arbitrary subset does
not by itself force exposedness.

## Mechanism 1: Markov Hitting

Large lifetime gives a quantitative quasi-closed class.  If
`H_i=sum_m (T^m1)_i>A/tau`, define
`mu=H_i^(-1) sum_{m>=0} e_i T^m`.  Then

```text
mu s = 1/H_i < tau/A,       ||muT-mu||_1 <= tau/A.          (QS)
```

Averaging `(PC)` over `mu` shows that `conv{p_i:i in B}` is almost invariant,
with leakage `O(tau/A)` to `G` and algebraic error `O(delta)`.  If a separator
`phi` puts all `G`-rows at least `M tau` below a quasi-closed high class, the
leakage estimate

```text
q_i({phi <= max phi - gamma}) <= (height_defect_i+O(delta))/gamma
```

with `gamma~tau` forces `q_i` to remain in the high slice except for `O(tau)`
mass.  Thus a long-lived bad class is also a long-lived high-face class.

Failure point: quasi-stationarity proves recurrence, not exposedness.  A
near-closed rounded polygonal class could still have every vertex shielded by
another high, far vertex.  Stress tests suggest exact `P^2=P` plus small
negative mass forbids this, but the Markov argument alone has not produced the
contradiction.

## Mechanism 2: LP Separator / High-Face

Assume `v` is a bad vertex far from `C_R`.  The LP distance dual gives an
affine separator `phi` with `||phi||_inf<=1` and

```text
phi(v) >= sup_{C_R} phi + D tau.
```

Let `u` maximize `phi` among bad row vertices.  If the top `rho`-cluster of
`u` is separated from all other rows by a gap at least `kappa`, then `u` is in
`W_{rho,kappa}`.  If not, the exposedness LP dual gives a row or barycenter
supported outside `B_1(u,rho)` with

```text
phi >= phi(u) - O(kappa).
```

For `D >> k`, this witness is still bad.  Repeating produces a high-face graph
of `rho`-separated non-exposed bad vertices.  The desired contradiction is:

```text
high-face graph + q-quasi-closedness + neg(p_i)<=delta
    => either an exposed top vertex exists
       or the graph carries a signed affine circuit with negative mass >> delta.
```

The LP dual already gives "small positive mass" circuits for each non-exposed
vertex, but the negative coefficients remain uncontrolled.  The high-face
graph must be combined with `(QS)` or with the exact row equations to control
those negative coefficients.

## Stress Tests And False Statements

- Dense regular polygons show why a high-face graph can cycle forever in pure
  convex geometry.  They are not small-defect examples: exact polygon
  projections have constant negative mass, while local small-negative stencils
  have order-one idempotency defect.
- Hume and Hume products have sharp `tau` scaling but their vertices remain
  well exposed for small enough `kappa/tau`; they do not realize a closed bad
  class.
- A sticky one-state bad class is not an obstruction: if it is far from
  `C_R`, a separator should expose it.  This is a useful base case for the
  closed-class lemma.
- The closed-bad-class statement is false without a "bad/high/maximal"
  hypothesis: an arbitrary closed subset lying inside `conv R` can have
  infinite lifetime and no new useful vertex.

## Verdict

The resolvent half is ready to become a small formal lemma once constants are
chosen.  The complementary half is still open.  The best target is not
"large resolvent implies exposedness" in isolation, but the high-bad version:
a `q`-quasi-closed set of vertices that stays `D tau` away from `conv R` must
contain a new `(rho,kappa)`-well-exposed vertex.

## Artifacts

This note only adds the analytic target.  It uses the existing LP/skeleton,
computational, and stress-test notes under `agent-B/notes/`.  No canonical
layer was edited.

## Constants

A safe hierarchy for the next pass is

```text
delta <= 10^-4,       rho=R tau,       kappa=k tau,
D >= 100R,            R >= 100,        k <= 10^-3,
resolvent cutoff L0=A/tau with A around D.
```

The resolvent estimate itself only needs `4delta L0 <= 4A tau`; all other
separations are for the closed-class augmentation.

## Failure Modes

1. The quasi-stationary measure may have barycenter near `C_R` even though its
   support is bad; this blocks a naive averaged separator proof.
2. LP non-exposedness controls positive dual mass but not negative dual mass.
3. High-face propagation may form a broad near-flat component; exact
   idempotency has to rule this out, not convex geometry alone.
4. Importing the full stochastic near-idempotent theorem for the repaired
   matrix `Q` would be circular, since its cluster geometry depends on
   `op-exposed-hull`.

## Next Handoff

1. Prove the sticky/top-face base case: a `q`-closed bad class whose
   `phi`-top face has `rho`-diameter `<rho` contains a `kappa`-exposed vertex.
2. Build the no-cycle lemma for a high-face graph: a cycle of `rho`-separated
   non-exposed bad vertices with `q`-exit `<c tau` forces negative mass
   `>delta`.
3. Mine the existing LP code for the joint infeasibility certificate:
   non-exposedness duals for all high bad vertices plus `(QS)` plus
   `neg<=delta`.
