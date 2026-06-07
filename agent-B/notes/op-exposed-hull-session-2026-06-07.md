# op-exposed-hull Session Log

Date: 2026-06-07.  Agent B exploration.

## Setup completed

- Branch: `agent-b/op-exposed-hull-orchestration`.
- Persistent mission file:
  `agent-B/notes/op-exposed-hull-mission-control.md`.
- Experiment sandbox:
  `agent-B/experiments/op-exposed-hull/`.
- Solver inventory:
  - `gurobi_cl` present;
  - `wolframscript` present;
  - Python: `numpy`, `scipy`, `sympy` present;
  - Python modules `gurobipy`, `cvxpy` absent.

## Subagents launched

Thread limit allowed six concurrent workers:

1. LP-dual analytic attack.
2. Maximal-skeleton augmentation.
3. Robust-coordinate route.
4. Computational LP/MILP search.
5. Exact/CAS small cases.
6. Stress-test/counterexample families.

Deferred until capacity frees:

7. Deep literature search.
8. Alternative proof frameworks.

## Local artifacts added

- `agent-B/experiments/op-exposed-hull/exposed_hull_metrics.py`
  computes:
  - row negative mass;
  - row vertices;
  - exposedness moduli by LP;
  - `W_{rho,kappa}`;
  - row distance to `conv W`.
- Initial output JSON:
  - `hume_s010_metrics.json`;
  - `hume_s003_metrics.json`;
  - `hume_s001_metrics.json`;
  - random projection smoke tests for `(n,rank)=(4,2),(5,2),(5,3)`.
- Literature scout:
  `agent-B/notes/op-exposed-hull-literature-scout-2026-06-07.md`.
- Durable orchestration plan:
  `docs/plans/2026-06-07-op-exposed-hull-attack-plan.md`.

## Numerical lessons so far

Hume's sharp `3x3` family is not an exposed-hull obstruction.  At the tested
square-root scales the row vertices are strongly exposed and every row lies in
their hull.

Update: the tensor-square Hume product at `s=0.02` is also not an obstruction.
Across

```text
rho/tau in {0.5,1,2,4,8},        kappa/tau in {0.05,0.1,0.25,0.5},
```

all four vertices are well exposed and `max dist(row,conv W)=0`.

Generic random unital projections are a poor search distribution.  They usually
have `delta` not small enough, so `rho=C sqrt(delta)` exceeds the row diameter
and the exposedness test is trivial.  Future experiments must generate
small-delta idempotents near stochastic idempotents or solve a constrained
optimization problem directly.

Similarity-conjugated stochastic idempotents at `n=6, rank=3, delta~=1e-3`
also did not find an obstruction.  The best of 40 samples had
`max_dist/tau ~= 8.4e-5`; one weakly exposed row stayed within
`2.7e-6` of the exposed hull.

Small-case subagent output:

- rank `<=2`, all exact `n=3`, and simplex row polytopes satisfy the
  exposed-hull target with zero reconstruction error;
- an explicit `n=4` corank-one quadrilateral family with `delta=t^2` has all
  four vertices strongly exposed at `rho=t`;
- the remaining small symbolic target is arbitrary `n=4`, rank `3`,
  corank-one `2|2` quadrilateral circuits.

Follow-up update: the `n=4` `2|2` circuit gap is now closed at coefficient
level in `agent-B/notes/subagent-op-exposed-hull-n4-circuit.md`.  For a
positive circuit `a p_0+b p_1=c p_2+d p_3`, all four vertices are exposed at
levels `b,a,d,c`; a small coefficient collapses the corresponding vertex to
the opposite edge at `O(sqrt(delta))`.

Stress-test output:

- Hume products and direct sums remain sharp for the exponent but not for
  exposed-hull obstruction;
- dense polygon and cyclic-chain warnings fail exact idempotency or have
  constant negative mass;
- random exact signed similarities near stochastic idempotents look benign.

`search_similarity.py` had a sandbox JSON bug (`Path` in `vars(args)`);
fixed by stringifying path-valued parameters before dumping.

Solver refresh:

- `gurobi_cl` present: Gurobi 13.0.2.
- `wolframscript` present, but the kernel smoke test fails because the
  Wolfram product is not activated.
- Python `numpy` and `scipy` present; `gurobipy`, `cvxpy`, and `ortools`
  absent.

## Current proof-route hypotheses

### Route 1: LP-dual/Hoffman route

Use Farkas duality for the failure of

```text
dist_1(v, conv W) <= A tau
```

and for the failure of exposedness.  The missing estimate is a universal
Hoffman-type bound whose conditioning is supplied by right-fixity and
near-positivity, not by arbitrary polytope angles.

Subagent A produced `subagent-op-exposed-hull-lp-dual.md`.  The exact dual of
failed exposedness is a signed row-difference circuit with small positive
mass:

```text
sum_{j in S_v} mu_j (x_j-v)
  = sum_i (beta_i-alpha_i)(x_i-v),        sum_i beta_i < kappa.
```

The uncontrolled `alpha` mass is the current analytic blocker.

### Route 2: face-descent route

If a row is far from `conv W`, separate it from `conv W` by an affine function
and look at a high face/near-face.  Affine-face leakage makes the near-face
almost closed under the positive part of the row dynamics.  A minimal such
near-face with no well-exposed vertex should contradict small negative mass.

This route must avoid sequential deletion; it needs a one-shot face/skeleton
certificate.

### Route 3: redundancy-contraction route

Plain convex geometry may give:

```text
not well exposed  =>  locally O(tau)-redundant.
```

The known gap is accumulation.  The desired new lemma is that redundancy among
non-well-exposed vertices is a contraction, acyclic after a height assignment,
or otherwise one-shot reconstructible because of `P^2=P` and `neg<=delta`.

Follow-up update: the bad-kernel worker sharpened the resolvent half to

```text
dist_1(p_i,conv R) <= Gamma + 4 delta ||(I-T)^(-1)||_{inf->inf}.
```

Thus only the long-lived closed-bad-class/high-face augmentation remains as
the central proof blocker on this route.

### Route 4: robust-coordinate route

Instead of selecting well-exposed vertices directly, construct affine
coordinates on representatives with coefficient negative mass `O(delta)` and
row reconstruction error `O(tau)`.  Then
`robust-approximate-simplexity-reduction.md` finishes the stochastic idempotent
construction.  Coefficient negativity `O(tau)` is not enough.

Follow-up update: `agent-B/notes/subagent-op-exposed-hull-interpolation-upgrade.md`
keeps this route active but narrows it to an LP kernel lemma.  Cluster
assignment alone gives only `G=I+O(tau)`, and exactifying can introduce
`O(tau)` negativity.  The optimized kernel target is row reconstruction
`O(tau)` plus representative interpolation defect `O(delta)`, which held in
the current Hume, quadrilateral, and small-defect similarity probes.

### Route 5: frozen LP/game diagnostics

`agent-B/notes/subagent-op-exposed-hull-lp-game.md` starts the joint
certificate miner.  The full negation of the closed-bad-class lemma is
bilinear/nonconvex unless `P` and the combinatorics are frozen.  The frozen
diagnostic behaves correctly so far: Hume immediately has an augmenting
exposed vertex, while the regular-polygon warning is feasible only at
constant negative mass.

### Route 6: direct exact-retraction search

`agent-B/notes/subagent-op-exposed-hull-direct-search.md` adds exact
`P=A B`, `B A=I`, `P1=1` generators.  No counterexample was found.  Broad
grids only create large ratios for aggressive constants (`rho=0.5 tau`,
`kappa=0.5 tau`), and the same candidates become harmless for `rho>=tau`.
Conservative grids show benign `O(delta)`-scale distances.  Next numerics
should score repaired-coordinate bad-kernel lifetime, not raw hull distance.

## Literature leads

No external theorem found so far closes the problem.  Subagent G also found no
direct theorem; its sandbox report is
`agent-B/notes/subagent-op-exposed-hull-literature.md`.  Candidate background:

- Gonzalez-Torres 2017 on cores of idempotent stochastic matrices.
- Gonzalez-Hartfiel 1991 on the stochastic idempotent matrix space.
- Schwarz 1964 on the semigroup of stochastic matrices.
- Blackwell 1942 on idempotent Markoff chains.
- Agaev-Chebotarev 2011 on regularized power limits.
- Hoffman error-bound literature for LP distance certificates.
- Choquet-Corson-Klee 1966 / Straszewicz exposed-point background.

All are scout leads only until added to local `refs/`.

## Next follow-up workers

As of the orchestration plan update:

- repaired-coordinate bad-kernel lifetime scoring on direct `A,B` samples;
- Farkas dual extraction for the interpolation-upgrade LP;
- no-cycle/high-face lemma for quasi-closed bad classes.
