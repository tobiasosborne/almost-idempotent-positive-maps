# Subagent B: Maximal-Skeleton Route For `op-exposed-hull`

Date: 2026-06-07.  Lane: Agent B sandbox.  Status: exploratory, not a
canonical proof shard.

## Verdict

No complete proof yet.  The maximal-skeleton route is still plausible, but the
naive augmentation statement has a precise missing ingredient:

```text
bad row far from conv(R) + not well-exposed
  => a controlled bad-to-bad shadow transition.
```

To close the route one needs either an acyclic height for these shadow
transitions, or a contraction/resolvent certificate showing that bad-to-bad
transitions cannot trap mass for longer than `O(1/tau)` steps.  The latter is
the better target because each positive-coordinate step has only `O(delta)`
error, and `O(delta)/tau = O(tau)`.

## Setup

Let `P1=1`, `P^2=P`, `neg(p_i)<=delta`, `tau=sqrt(delta)`, and
`K=conv{p_i}`.  Fix `rho=C_rho tau`, `kappa=c_kappa tau`.  Let
`W=W_{rho,kappa}` be the row vertices `v` with `e_v(rho)>=kappa`, let `R` be a
maximal `4rho`-separated subset of `W`, and set `C_R=conv(R)`.

The known reduction says: if every row is `O(tau)`-close to `C_R`, then the
cluster-representative theorem gives a stochastic idempotent within `O(tau)`.

## Desired Augmentation Lemma

A one-shot lemma would finish this route:

```text
dist_1(v,C_R)>A tau for a row vertex v
  => exists row vertex w with dist_1(w,C_R)>4rho and e_w(rho)>=kappa.
```

Then `w in W`, contradicting maximality of the `4rho`-separated set `R`.

This is the cleanest formulation, but the direct proof attempt exposes the
real missing estimate.

## Proof Attempt: Separation Gives A Shadow Step

Let `v` be a row vertex with `d = dist_1(v,C_R)`.  A Hahn-Banach separation in
the ambient `l_1/l_infty` dual gives an affine functional `ell`, with
`||ell||_Lip <= 1`, such that

```text
ell(v) - sup_{x in C_R} ell(x) >= d.
```

If `v` is not a maximizer of `ell` on `K`, replace `v` by a row vertex `w`
where `ell` is maximal.  Then `w` is at least as far from `C_R` in the `ell`
witness direction.  Normalizing the height drop

```text
h(x) = (M - ell(x))/(M - m),        M=max_K ell,  m=min_K ell,
```

gives `h:K->[0,1]` and `h=0` on the top face.  If the top face has diameter
`< rho` and all rows outside the `rho`-cluster have `h >= kappa`, then any
top-face vertex is well-exposed and the skeleton augments.

If not, there is a row `z` outside the `rho`-cluster with

```text
ell(z) >= M - (M-m) kappa.
```

Since `M-m <= diam_1(K) <= 2+4delta`, this `z` remains far from `C_R` whenever
`d >> kappa`.  Thus failure of augmentation produces a new bad row separated
from the old one but lying in the same high shadow.

This is useful but incomplete.  Repeating it can form long chains or cycles of
non-well-exposed bad rows.  Pure convex geometry allows this; the
regular-polygon warning shows the logic gap.  The proof must use `P^2=P` and
small negative mass to rule out or contract these chains.

## Positive-Coordinate Kernel

Use `P^2=P` by repairing each signed coordinate row.  For
`a_i=neg(p_i)`, set `q_i=p_i^+/(1+a_i)`.  Then `q_i` is a probability vector
and, because `p_i P = p_i`,

```text
||p_i - sum_j q_i(j) p_j||_1 <= C delta.        (PC)
```

This is the exact algebraic reason a contraction certificate would be enough:
each substitution step costs only `O(delta)`.

## Contraction Certificate

Let `B` be a set of bad row indices and let `G` be its complement.  Suppose:

1. every row in `G` is within `Gamma` of `C_R`;
2. for `i in B`, the positive-coordinate kernel `q_i` satisfies `(PC)`;
3. with `T=(q_i(j))_{i,j in B}`, the substochastic bad-to-bad kernel has

   ```text
   ||(I-T)^(-1)||_{infty->infty} <= L.
   ```

Then every row in `B` is within

```text
Gamma + C L delta
```

of `C_R`.  In particular, if `Gamma=O(tau)` and `L=O(1/tau)`, then all bad
rows are `O(tau)`-close to `C_R`.

Proof: with `d_i=dist_1(p_i,C_R)` for `i in B`,

```text
d_i <= C delta + sum_{j in B} q_i(j) d_j
       + Gamma * q_i(G).
```

Vectorially,

```text
d <= C delta * 1 + T d + Gamma * s,        s_i=q_i(G).
```

Since `(I-T)^(-1)s <= 1` for a substochastic kernel that eventually exits,

```text
d <= C L delta * 1 + Gamma * 1.
```

This proves the certificate.

## Remaining Hard Alternative

It is now enough to prove the following alternative.

```text
Closed-bad-class augmentation lemma.
Let B be the set of row vertices with dist_1(.,C_R) > A tau, enlarged by
rho-clusters.  Either
  (a) the positive-coordinate bad kernel has
      ||(I-T)^(-1)||_{inf->inf} <= C/tau; or
  (b) B contains a row vertex w with e_w(rho) >= kappa and
      dist_1(w,C_R) > 4rho.
```

Case `(a)` reconstructs every bad row; case `(b)` augments the maximal
skeleton, contradiction.  This is the sharp form of the route.

## Acyclic Variant

An acyclic certificate would also work.  Assign a height `H` to bad vertices so
that every non-well-exposed bad vertex is `O(delta)`-close, via its
positive-coordinate representation, to a convex combination of:

```text
rows already O(tau)-close to C_R, and bad rows with strictly larger H.
```

If the total bad-to-bad weight along each height step is at most `1-c tau`,
then the same `O(delta)/tau=O(tau)` summation closes.  If the weight is `1`,
mere acyclicity is too weak: an arbitrarily long chain can accumulate
`O(length * delta)`.

Thus the useful target is not "acyclic" alone but "acyclic with escape
`>= c tau`" or, equivalently, the resolvent bound above.

## Obstructions

1. Local exposed-or-redundant dichotomies can be circular.
2. A separator from `C_R` may expose a high face or dense chain, not one row.
3. Pure convex geometry cannot rule out chains/cycles; the missing estimate
   must use the positive-coordinate kernel coming from `P^2=P`.
4. A path-length bound independent of `n` is unrealistic.  The right target is
   a resolvent bound `O(1/tau)`, because each step costs `O(delta)`.

## Next Lemmas To Prove Or Falsify

1. **Positive-coordinate shadow lemma.** If `v` is bad and not well-exposed,
   then the repaired coordinate distribution `q_v` puts all but `O(tau)` mass
   on rows that are still bad, unless `v` is already `O(tau)`-close to `C_R`.

2. **Closed-bad-class augmentation.** If a bad set is `O(tau)`-closed under
   `q`, then some vertex of that bad set is `(rho,kappa)`-exposed relative to
   the full row polytope.

3. **Shadow-cycle lower bound.** A `rho`-separated cycle of non-well-exposed
   bad vertices whose shadow transitions stay in the bad set forces
   coordinate negative mass larger than `delta`, unless the cycle has an
   exit rate `>= c tau`.

4. **LP/resolvent experiment.** Search for exact signed affine retractions
   with small `delta`, a prescribed skeleton `R`, and a bad subkernel with
   `||(I-T)^(-1)|| >> 1/tau`.  `gurobi_cl`, `wolframscript`, and `scipy` are
   available locally; `gurobipy` is not installed in this environment.

## Handoff

The next subagent should attack Lemma 1 or 2.  A decisive counterexample should
output an exact/rational signed idempotent `P` with:

```text
max_i neg(p_i) = delta,
rho ~= sqrt(delta),
R subset W_{rho,kappa},
some row at distance >> sqrt(delta) from conv(R),
and no augmenting well-exposed vertex.
```

A proof should package the contraction certificate as an independent lemma;
it is small enough to become an `af` node once Agent A reviews the constants.
