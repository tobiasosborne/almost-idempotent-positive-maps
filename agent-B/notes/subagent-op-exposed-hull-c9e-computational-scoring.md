# Subagent: op-exposed-hull C9-E computational scoring

Date: 2026-06-07.  Lane: Agent B sandbox.  Status: numerical evidence only,
not a proof and not a canonical shard.

## Verdict

No C9 counterexample candidate was found.

The repaired-coordinate scorer found many reports with rows outside
`conv W`, but none with the dangerous combination

```text
bad rows far from conv W,
bad kernel long-lived under q,
shadow witnesses forced to leak out of the high slice.
```

In the broad direct-`A,B` run, the top C9-threat rows all had

```text
bad_lifetime = 1,
tau * bad_lifetime ~= 0.0993,
max shadow min-leakage = 0,
```

so the bad set exits immediately.  The largest high-slice q-leakage among top
kept reports was about `0.0594`, again in the already-benign one-step regime.

This supports the current C9 strategy: in direct exact retractions, the
bad rows that are visible from the `conv W` separator are not forming
long-lived repaired-kernel traps.  Either the resolvent side closes, or the
shadow witness is already high-supported.

## What Was Implemented

Created:

```text
agent-B/experiments/op-exposed-hull/scripts/score_c9_repaired.py
```

The script scores existing and newly generated direct `P=A B` samples by:

1. computing the repaired stochastic kernel

   ```text
   q_i = p_i^+ / ||p_i^+||_1;
   ```

2. checking the repair identity numerically through

   ```text
   ||p_i - sum_j q_i(j) p_j||_1;
   ```

3. computing `W_{rho,kappa}` via the existing exposed-hull LPs;
4. choosing the worst row-distance separator against `conv W` by the
   `l_infty` dual LP

   ```text
   max_{||phi||_infty<=1} phi(p_i) - max_{w in W} phi(w);
   ```

5. defining high slices

   ```text
   H0 = {i : M - phi(p_i) <= 16 delta},
   H1 = {i : M - phi(p_i) <= 4 tau};
   ```

6. defining bad rows by

   ```text
   dist_1(p_i, conv W) > 0.05 tau
   ```

   in the broad run;

7. measuring the bad-kernel lifetime by solving

   ```text
   (I - T) x = 1,        T = q|_{B,B};
   ```

8. measuring `q`-exit from `H0` and `H1`;
9. measuring a Step-3-style shadow leakage proxy: for each vertex, among
   outside-`rho` rows with average height high enough to satisfy the Step 3
   drop bound, minimize mass outside `H1`.

The shadow-leakage quantity is deliberately only a proxy.  It does not replace
the full Step 5 Farkas/failed-exposedness dual witness.

## Outputs

Broad run:

```text
agent-B/experiments/op-exposed-hull/outputs/c9_repaired_score_grid_20260607.json
agent-B/experiments/op-exposed-hull/outputs/c9_repaired_score_grid_20260607.csv
```

Sensitivity run with looser bad threshold `0.01 tau`:

```text
agent-B/experiments/op-exposed-hull/outputs/c9_repaired_score_threshold001_20260607.json
agent-B/experiments/op-exposed-hull/outputs/c9_repaired_score_threshold001_20260607.csv
```

SHA256:

```text
53f5f13d27470ecda351a31f8f92362e27a9fc535df91175be4effaffe90b097  scripts/score_c9_repaired.py
85cbc2df17863629866ee2d2e3c949b4f37eebf5f99a4ef2a039f660db42809b  outputs/c9_repaired_score_grid_20260607.json
2c0dee52e00f9610562f3118170813f3d2237537399e75a678ef70932ac00ee8  outputs/c9_repaired_score_threshold001_20260607.json
```

## Commands

Broad run:

```bash
python3 agent-B/experiments/op-exposed-hull/scripts/score_c9_repaired.py \
  --input-json agent-B/experiments/op-exposed-hull/outputs/search_direct_ab_grid_20260607.json \
  --input-json agent-B/experiments/op-exposed-hull/outputs/search_direct_ab_conservative_20260607.json \
  --input-json agent-B/experiments/op-exposed-hull/outputs/search_direct_ab_free_bisect_20260607.json \
  --families anchor,free \
  --n-ranks 5:2,5:3,6:2,6:3,7:3,8:3,8:4 \
  --target-deltas 0.0001,0.001,0.01 \
  --rho-mults 1,2,4 \
  --kappa-mults 0.05,0.1,0.25 \
  --samples 15 \
  --seed 2026060797 \
  --keep 32 \
  --bad-distance-mult 0.05 \
  --h0-delta-mult 16 \
  --h1-tau-mult 4 \
  --out-json agent-B/experiments/op-exposed-hull/outputs/c9_repaired_score_grid_20260607.json \
  --out-csv agent-B/experiments/op-exposed-hull/outputs/c9_repaired_score_grid_20260607.csv
```

Sensitivity run:

```bash
python3 agent-B/experiments/op-exposed-hull/scripts/score_c9_repaired.py \
  --input-json agent-B/experiments/op-exposed-hull/outputs/search_direct_ab_grid_20260607.json \
  --input-json agent-B/experiments/op-exposed-hull/outputs/search_direct_ab_conservative_20260607.json \
  --input-json agent-B/experiments/op-exposed-hull/outputs/search_direct_ab_free_bisect_20260607.json \
  --families anchor,free \
  --n-ranks 5:2 \
  --target-deltas 0.001 \
  --rho-mults 1,2,4 \
  --kappa-mults 0.05,0.1,0.25 \
  --samples 0 \
  --keep 32 \
  --bad-distance-mult 0.01 \
  --h0-delta-mult 16 \
  --h1-tau-mult 4 \
  --out-json agent-B/experiments/op-exposed-hull/outputs/c9_repaired_score_threshold001_20260607.json \
  --out-csv agent-B/experiments/op-exposed-hull/outputs/c9_repaired_score_threshold001_20260607.csv
```

## Numerical Results

Broad run aggregate:

```text
loaded existing samples: 52
attempted generated samples: 630
accepted generated samples: 445
scored constants reports: 4473
nonempty bad reports: 997
errors: 0
```

Worst kept C9 reports:

```text
family: direct_anchor_barycentric
n, rank: 5, 3
delta: 0.009844086730558406
tau: 0.09921737111291755
rho/tau: 1
kappa/tau: 0.1 or 0.25
dist(row,conv W)/tau: 0.19843474222583696
bad_count: 2
bad_lifetime: 1
tau * bad_lifetime: 0.09921737111291755
bad_exit max: 1
H0 size, H1 size: 3, 3
q_exit(H0 to H1^c) max: 0
max shadow min-leakage: 0
repair_error/delta max: 2.0000000000000075
```

The next cluster had the same pattern:

```text
delta ~= 0.0098313
dist(row,conv W)/tau ~= 0.1983
bad_count: 2 or 3
bad_lifetime: 1
q_exit(H0 to H1^c) max ~= 0.0594
max shadow min-leakage: 0
repair_error/delta max ~= 2
```

Sensitivity run aggregate:

```text
loaded existing samples: 52
scored constants reports: 468
nonempty bad reports: 194
errors: 0
```

The looser threshold did not expose a hidden long-lived class.  The same
anchor-barycentric samples stayed at `bad_lifetime=1`, with zero shadow
min-leakage.

## Constants And Interpretation

The repaired identity is numerically sharp in these direct samples:

```text
max_i ||p_i - sum_j q_i(j)p_j||_1 <= 2 delta
```

on the top reports.  This is stronger than the coarse analytic budget used in
the C9 plan and is a useful sanity check for the repair mechanism.

The top-separator high slices are also clean: in the worst report, `H0=H1`
and `q` does not leave that high slice.  Where `q`-exit appears in the next
cluster, the bad set still exits in one step, so the resolvent side is already
stronger than needed.

## Failure Modes

The scorer uses `W_{rho,kappa}` as the skeleton.  C9 eventually needs arbitrary
maximal exposed skeletons, so this is a targeted stress test rather than the
full negation.

The direct `A,B` generators are exact but not exhaustive.  They cover
anchor-barycentric and free-left-inverse families up to `n<=8` in these runs.

The shadow-leakage statistic is a Step-3 proxy.  It optimizes mass outside
`H1` under a high-average `phi` constraint, but it does not compute the full
Step 5 failed-exposedness dual measure.

The high-slice constants were fixed at `16 delta` and `4 tau`.  A future
adversarial scorer should scan these constants too.

## Next Handoff

Computationally, the next useful move is not more random exposed-hull scoring.
It is an adversarial optimization whose objective directly maximizes

```text
tau * ||(I-T)^(-1)||_infty
  - penalties for large q-exit
  + penalties for forced shadow leakage.
```

Analytically, the current evidence points to this C9 sublemma:

```text
For a separator phi obtained from dist(row,conv W), either the q-bad kernel
exits on O(1) time in the direct-coordinate bad set, or the Step-3 shadow
witness can be chosen inside the two-scale high slice.
```

That sublemma should be checked against the C9-A/B/C notes once they exist:
high-core pruning should explain the one-step exit cases, and shadow-leakage
should formalize the observed zero-leakage witnesses.
