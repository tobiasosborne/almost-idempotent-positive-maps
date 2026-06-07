# Subagent D: op-exposed-hull computational search

Date: 2026-06-07.  Scope: Agent B sandbox only.

Status: numerical evidence only.  Nothing below proves `op-exposed-hull`, and
nothing should be promoted to the registry without a separate analytic proof
and Agent A review.

## Built Artifacts

Experiment root:

```text
agent-B/experiments/op-exposed-hull/
```

New reusable code:

```text
src/exposed_hull.py
src/families.py
scripts/detect_solvers.py
scripts/analyze_family.py
scripts/search_similarity.py
scripts/wolfram_hume_check.wls
```

The LP code computes, for a finite row set:

```text
e_v(rho) = sup_h min_{||p_i-v||_1 >= rho} h(p_i)
W_{rho,kappa} = {row vertices v : e_v(rho) >= kappa}
dist_1(p_i, conv W_{rho,kappa})
```

The search code generates exact signed affine retractions by construction:

```text
P = S E S^{-1},       S 1 = 1,
```

where `E` is a stochastic cluster idempotent.  Thus `P^2=P` and `P1=1` hold up
to floating error; each direction is rescaled by binary search to a target row
negative-mass budget.

## Solver Inventory

Recorded in:

```text
agent-B/experiments/op-exposed-hull/outputs/solver_env.json
```

Available:

```text
scipy 1.11.4 with scipy.optimize.linprog(method='highs')
numpy 1.26.4
gurobi_cl 13.0.2
wolframscript 1.13.0 binary
```

Unavailable or blocked:

```text
cvxpy: missing
gurobipy: missing
ortools: missing
wolframscript kernel smoke test: return code 255, product not activated
```

Primary backend used here: SciPy/HiGHS LP.  Gurobi CLI was detected but not used
because the Python binding is absent and these fixed-candidate computations do
not require a mixed-integer formulation.

## Reproduction Commands

Solver inventory:

```bash
python3 agent-B/experiments/op-exposed-hull/scripts/detect_solvers.py --out agent-B/experiments/op-exposed-hull/outputs/solver_env.json
```

Fixed families:

```bash
python3 agent-B/experiments/op-exposed-hull/scripts/analyze_family.py --family hume --s 0.05 --rho-mults 0.5,1,2,4,8 --kappa-mults 0.1,0.25,0.5,1 --out-json agent-B/experiments/op-exposed-hull/outputs/hume_s005.json --out-csv agent-B/experiments/op-exposed-hull/outputs/hume_s005.csv
python3 agent-B/experiments/op-exposed-hull/scripts/analyze_family.py --family hume-product --s 0.03 --power 2 --rho-mults 0.5,1,2,4,8 --kappa-mults 0.1,0.25,0.5,1 --out-json agent-B/experiments/op-exposed-hull/outputs/hume_product_s003_p2.json --out-csv agent-B/experiments/op-exposed-hull/outputs/hume_product_s003_p2.csv
python3 agent-B/experiments/op-exposed-hull/scripts/analyze_family.py --family random-similarity --n 6 --rank 3 --amp 0.02 --seed 101 --rho-mults 0.5,1,2,4,8 --kappa-mults 0.1,0.25,0.5,1 --out-json agent-B/experiments/op-exposed-hull/outputs/random_similarity_n6_r3_seed101.json --out-csv agent-B/experiments/op-exposed-hull/outputs/random_similarity_n6_r3_seed101.csv
python3 agent-B/experiments/op-exposed-hull/scripts/analyze_family.py --family regular-polygon --n 12 --rho-mults 0.25,0.5,1,2,4 --kappa-mults 0.1,0.25,0.5,1 --out-json agent-B/experiments/op-exposed-hull/outputs/regular_polygon_n12.json --out-csv agent-B/experiments/op-exposed-hull/outputs/regular_polygon_n12.csv
```

Random/local similarity searches:

```bash
python3 agent-B/experiments/op-exposed-hull/scripts/search_similarity.py --n 6 --rank 3 --target-delta 0.001 --max-amp 0.2 --rho-mult 4 --kappa-mult 0.25 --samples 120 --seed 2000 --keep 8 --polish --polish-iters 60 --out agent-B/experiments/op-exposed-hull/outputs/search_similarity_n6_r3_delta1e-3_rho4_kappa025.json
python3 agent-B/experiments/op-exposed-hull/scripts/search_similarity.py --n 6 --rank 3 --target-delta 0.001 --max-amp 0.2 --rho-mult 1 --kappa-mult 0.25 --samples 120 --seed 3000 --keep 8 --polish --polish-iters 60 --out agent-B/experiments/op-exposed-hull/outputs/search_similarity_n6_r3_delta1e-3_rho1_kappa025.json
python3 agent-B/experiments/op-exposed-hull/scripts/search_similarity.py --n 6 --rank 3 --target-delta 0.001 --max-amp 0.2 --rho-mult 0.5 --kappa-mult 0.25 --samples 120 --seed 4000 --keep 8 --polish --polish-iters 60 --out agent-B/experiments/op-exposed-hull/outputs/search_similarity_n6_r3_delta1e-3_rho05_kappa025.json
python3 agent-B/experiments/op-exposed-hull/scripts/search_similarity.py --n 8 --rank 4 --target-delta 0.001 --max-amp 0.15 --rho-mult 2 --kappa-mult 0.25 --samples 80 --seed 5000 --keep 8 --polish --polish-iters 40 --out agent-B/experiments/op-exposed-hull/outputs/search_similarity_n8_r4_delta1e-3_rho2_kappa025.json
python3 agent-B/experiments/op-exposed-hull/scripts/search_similarity.py --n 6 --rank 3 --target-delta 0.0001 --max-amp 0.1 --rho-mult 1 --kappa-mult 0.25 --samples 120 --seed 6000 --keep 8 --polish --polish-iters 40 --out agent-B/experiments/op-exposed-hull/outputs/search_similarity_n6_r3_delta1e-4_rho1_kappa025.json
python3 agent-B/experiments/op-exposed-hull/scripts/search_similarity.py --n 6 --rank 3 --target-delta 0.01 --max-amp 0.3 --rho-mult 0.5 --kappa-mult 0.25 --samples 120 --seed 7000 --keep 8 --polish --polish-iters 40 --out agent-B/experiments/op-exposed-hull/outputs/search_similarity_n6_r3_delta1e-2_rho05_kappa025.json
```

Wolfram exact Hume smoke script:

```bash
wolframscript -file agent-B/experiments/op-exposed-hull/scripts/wolfram_hume_check.wls
```

This currently fails because the local Wolfram kernel is not activated.

## Numerical Findings

Hume benchmark, `s=0.05`, `delta=0.0025`, `tau=0.05`:

```text
all scanned rho/kappa choices had W = all 2 row vertices,
max dist(row, conv W) = 0.
```

Hume tensor product, `s=0.03`, power `2`, `delta=0.00180162`:

```text
for kappa_mult <= 0.5: W = all 4 row vertices, distance 0;
for rho_mult <= 1 and kappa_mult = 1: W collapsed to 1 vertex and ratio ~= 47.
```

Interpretation: aggressive gap constants can be too strict even on product
stress tests.  This is a constants warning, not an asymptotic counterexample to
the open statement, which may choose small `c` and large `C`.

Random similarity, fixed `amp=0.02`, `n=6`, rank `3`, seed `101`:

```text
delta ~= 0.0192, tau ~= 0.1386.
rho_mult = 0.5, kappa_mult >= 0.25 produced ratio ~= 14.68;
rho_mult >= 1 had W = all 3 vertices and distance 0.
```

Interpretation: too-small `rho` can falsely drop a representative.  Increasing
the cluster scale repairs this example.

Regular polygon symmetric affine projection, `n=12`:

```text
delta ~= 0.20534, tau ~= 0.45315,
e_v(0.25 tau) ~= 0.066987 for every vertex.
```

The family can make `W` empty for `kappa_mult >= 0.25` at small `rho_mult`, but
its negative mass is bounded away from zero.  This matches the existing
regular-polygon obstruction note: it is a convex-geometric warning, not a
small-defect signed-retraction counterexample.

Small-delta random/local searches:

```text
n=6 rank=3 delta=1e-3 rho=4 tau kappa=0.25 tau:
  best ratio 0, W all 6 vertices.
n=6 rank=3 delta=1e-3 rho=tau kappa=0.25 tau:
  best random ratio 0.0003866; local polish ratio 0.0008608.
n=6 rank=3 delta=1e-3 rho=0.5 tau kappa=0.25 tau:
  best random ratio 0.0002471; local polish ratio 0.0003992.
n=8 rank=4 delta=1e-3 rho=2 tau kappa=0.25 tau:
  best random ratio 0.0001155; local polish ratio 0.0005683.
n=6 rank=3 delta=1e-4 rho=tau kappa=0.25 tau:
  best ratio 0.
n=6 rank=3 delta=1e-2 rho=0.5 tau kappa=0.25 tau:
  best random ratio 0.007249; local polish ratio 0.008752.
```

In these exact similarity-conjugated samples, missing well-exposed vertices are
numerically very close to the hull of the remaining well-exposed vertices once
`delta` is in the small regime.  No candidate remotely threatens a universal
`C sqrt(delta)` exposed-hull bound.

## Proof-Search Implications

The computations favor the global exposed-hull formulation over pointwise
deletion.  The dangerous-looking failures occur when constants are chosen too
aggressively or when regular-polygon geometry is used outside the small
negative-mass regime.

The most promising analytic target remains:

```text
If a row vertex v is not in W_{rho,kappa}, then the LP dual witness for
e_v(rho)<kappa, combined with P^2=P and neg(p_i)<=delta, should give an
O(sqrt(delta)) reconstruction of v by conv W_{rho,kappa}.
```

Computationally, the next extension should search beyond similarity-conjugated
cluster projections.  The natural next script is a direct nonlinear
parameterization `P=A B`, `B A=I`, `P1=1`, with penalty terms for negative mass
and exposed-hull violation.  That may explore exact retractions not near a
fixed cluster idempotent.
