# Subagent: op-exposed-hull Direct `P=A B` Search

Date: 2026-06-07.  Lane: Agent B sandbox.  Status: numerical falsification
only, not a proof and not a canonical shard.

## Verdict

No counterexample candidate was found.

The direct exact-retraction parameterization is working.  Every generated
matrix has

```text
P = A B,        B A = I,        P^2 = P,        P1 = 1
```

to machine precision, and the accepted samples satisfy the requested row
negative-mass budget.

The only large ratios came from an aggressive constants regime

```text
rho = 0.5 sqrt(delta),        kappa = 0.5 sqrt(delta),
```

where a coordinate anchor can be dropped.  The same candidates become harmless
when `rho >= sqrt(delta)`.  In the conservative regime

```text
rho in {1,2,4,8} sqrt(delta),
kappa in {0.05,0.1,0.25} sqrt(delta),
```

the worst retained finite ratio was about `0.1985`, from a barycentric sliver
with `delta ~= 9.84e-3` and distance `~= 1.97e-2`.  This is benign evidence:
the distance is on the scale `O(delta)`, not a threat to an `O(sqrt(delta))`
bound.

The free-left-inverse generator was even quieter.  After fixing the amplitude
scaling to use bisection, its best finite ratio was `0.00446`, with exactness
errors around `1e-16`.

## Parameterizations

### Anchor-barycentric

Let `A=Lambda` be an `n x r` matrix whose first `r` rows are the coordinate
anchors `e_1,...,e_r`, and whose remaining rows have coordinate sum `1` and
small negative mass.  Let

```text
B = [I_r  0].
```

Then `B A=I_r`, `B 1_n=1_r`, and

```text
P=A B
```

is an exact affine idempotent.  This searches arbitrary near-simplex
barycentric slivers directly, rather than via similarity conjugation.

### Free left inverse

Take an affine basis

```text
A = [1, U]
```

near a cluster-idempotent range.  Let

```text
B0 = (A^T A)^(-1) A^T,
N = I - A B0,
B = B0 + t C N.
```

Since `N A=0`, one has `B A=I`; since the first column of `A` is `1`,
`P1=1`.  The script scales `t` by bisection so that the row negative mass is
below the target delta.

## Artifacts

Code:

```text
agent-B/experiments/op-exposed-hull/src/direct_ab.py
agent-B/experiments/op-exposed-hull/scripts/search_direct_ab.py
```

Outputs:

```text
agent-B/experiments/op-exposed-hull/outputs/search_direct_ab_smoke.json
agent-B/experiments/op-exposed-hull/outputs/search_direct_ab_grid_20260607.json
agent-B/experiments/op-exposed-hull/outputs/search_direct_ab_conservative_20260607.json
agent-B/experiments/op-exposed-hull/outputs/search_direct_ab_free_bisect_20260607.json
```

CSV companions with the same stems were also written for quick inspection.

SHA256:

```text
ce426e7a2af2d82060bacf8d4c4be3e302a3979d63ed75edd396d263f571f9eb  src/direct_ab.py
6849b1630fa4640f9caa66ad4647658f08b31e580343d717578ebcb0757ff553  scripts/search_direct_ab.py
25e6f57eaf1478aa7ede3a12ae2e181f784f8753e9f23cc1c53cf5611f8d297d  outputs/search_direct_ab_grid_20260607.json
a38468905a56cc315178e12ef191092e5362bfca8ba6b9e57ed694e67bbda242  outputs/search_direct_ab_conservative_20260607.json
1dec3d1f6db292f1890b2464753472278d0127325811e825a20d691c0dbd2f2c  outputs/search_direct_ab_free_bisect_20260607.json
```

Reproduction commands:

```bash
python3 agent-B/experiments/op-exposed-hull/scripts/search_direct_ab.py --families anchor,free --n-ranks 5:2,5:3,6:2,6:3,7:3,8:3,8:4 --target-deltas 0.0001,0.001,0.01 --rho-mults 0.5,1,2,4 --kappa-mults 0.1,0.25,0.5 --samples 20 --seed 2026060701 --keep 16 --max-amp 0.2 --feature-noises 0,0.002,0.01,0.03 --out-json agent-B/experiments/op-exposed-hull/outputs/search_direct_ab_grid_20260607.json --out-csv agent-B/experiments/op-exposed-hull/outputs/search_direct_ab_grid_20260607.csv
python3 agent-B/experiments/op-exposed-hull/scripts/search_direct_ab.py --families anchor,free --n-ranks 5:2,5:3,6:2,6:3,7:3,8:3,8:4 --target-deltas 0.0001,0.001,0.01 --rho-mults 1,2,4,8 --kappa-mults 0.05,0.1,0.25 --samples 25 --seed 2026060721 --keep 16 --max-amp 0.25 --feature-noises 0,0.001,0.005,0.02 --out-json agent-B/experiments/op-exposed-hull/outputs/search_direct_ab_conservative_20260607.json --out-csv agent-B/experiments/op-exposed-hull/outputs/search_direct_ab_conservative_20260607.csv
python3 agent-B/experiments/op-exposed-hull/scripts/search_direct_ab.py --families free --n-ranks 5:2,5:3,6:2,6:3,7:3,8:3,8:4 --target-deltas 0.0001,0.001,0.01 --rho-mults 0.5,1,2,4 --kappa-mults 0.1,0.25,0.5 --samples 40 --seed 2026060741 --keep 20 --max-amp 0.5 --feature-noises 0,0.0005,0.002,0.01 --out-json agent-B/experiments/op-exposed-hull/outputs/search_direct_ab_free_bisect_20260607.json --out-csv agent-B/experiments/op-exposed-hull/outputs/search_direct_ab_free_bisect_20260607.csv
```

## Constants

Broad grid:

```text
families: anchor, free
n: 5..8 through pairs 5:2, 5:3, 6:2, 6:3, 7:3, 8:3, 8:4
target delta: 1e-4, 1e-3, 1e-2
rho/sqrt(delta): 0.5, 1, 2, 4
kappa/sqrt(delta): 0.1, 0.25, 0.5
accepted: 573 / 840
empty-W reports: 0
```

Worst broad-grid ratio:

```text
84.04 at rho=0.5 tau, kappa=0.5 tau.
```

This is a constants warning only.  For the same candidate, `rho>=tau` puts all
four vertices in `W`, so the distance is zero.

Conservative grid:

```text
rho/sqrt(delta): 1, 2, 4, 8
kappa/sqrt(delta): 0.05, 0.1, 0.25
accepted: 764 / 1050
empty-W reports: 0
best ratio: 0.19843474222583696
```

Free-left-inverse bisection grid:

```text
accepted: 454 / 840
empty-W reports: 0
best ratio: 0.004454078789224399
best exactness: idempotence_linf_l1 ~= 1.85e-16, row_sum_linf ~= 2.22e-16
```

## Failure Modes

The anchor-barycentric generator is exact and interpretable but restrictive:
the anchor rows are coordinate simplex rows.  It is best viewed as a direct
stress test for near-simplex barycentric slivers, not as a full search over all
row geometries.

The free-left-inverse generator is more general but local: it samples affine
bases near stochastic cluster ranges.  Many noisy bases already exceed the
target negative-mass budget at `t=0`, so those samples are skipped.  Accepted
samples do not explore every possible exact affine range.

The objective ranks finite `dist(row,conv W)/sqrt(delta)` values.  If `W` were
empty, the script would count that separately rather than treating infinity as
a finite falsification score.  In these runs, `empty_w_reports=0`.

The current search is random and derivative-free.  It did not use Gurobi
because every fixed exposedness/distance subproblem is already handled by
SciPy/HiGHS, and no suspicious candidate appeared that warranted exporting a
separate LP.

## Next Handoff

Numerics should now move away from naked exposed-hull falsification and toward
the Work Package 4 negation:

```text
bad set B far from conv(R),
q-closed or long-lived under repaired positive coordinates,
all B vertices fail exposedness,
neg(P_i) <= delta.
```

The next computational task is to add `q_i=p_i^+/||p_i^+||_1` to the direct
search outputs and rank candidates by bad-kernel lifetime or closed-class
quality.  That is more likely to reveal the missing analytic certificate than
another unconstrained random search over `A,B`.
