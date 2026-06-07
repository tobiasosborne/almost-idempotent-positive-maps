# Subagent: C9-F Frozen Counterexample LP

Date: 2026-06-07.  Lane: Agent B sandbox.  Status: exploratory diagnostic,
not a canonical proof shard.

## Verdict

No small-`delta` C9 failure was found in the frozen-row model.

The diagnostic reproduces exactly the expected warning:

```text
regular 12-gon arc -> frozen C9 failure pattern feasible
delta = 0.20534180126147966
```

This is large negative mass, so it is a constants/calibration obstruction, not
a small-defect counterexample to `op-exposed-hull`.

All small-defect tests stopped earlier:

- Hume `s=0.01`: the bad high row is already well-exposed.
- Hume product `s=0.003`, power `2`: high bad rows are already exposed.
- top direct `P=A B`, `B A=I` candidates: with a nonmaximal skeleton the high
  bad rows are already exposed; with `R=W`, there is no bad class.

## Frozen C9 Failure Model

Fix the row matrix `P`, skeleton `R`, bad set `B`, and constants
`rho,kappa,tau`.  The diagnostic asks whether the following can hold
simultaneously.

```text
1. B has a common l_infty separator above conv(R).
2. H1={i : M-phi(p_i)<=G tau} contains a nonempty high bad set H=B cap H1.
3. The repaired kernel q_i=p_i^+/||p_i^+||_1 is quasi-closed on H.
4. The q-lifetime on H is > A/tau, so the resolvent fallback is unavailable.
5. Every failed-exposedness shadow witness for rows in H leaks more than
   ell tau below H1.
6. No row in H is already (rho,kappa)-well-exposed.
```

If all six hold at small `delta`, C9 is in danger.  If any one fails, the
certificate shape points to the proof branch:

```text
exposed row       -> augment skeleton
short lifetime    -> bad-kernel resolvent closes
small leak        -> high-supported shadow kernel exists
no separator      -> bad set was not a common high face
```

## LP Blocks

All blocks below are linear after `P`, `R`, `B`, and `H1` are fixed.

### Common Separator

Variables: `phi`, `s`, margin `m`.

```text
||phi||_infty <= 1
phi(p_r) <= s                 for r in R
phi(p_b) >= s+m               for b in B
maximize m
```

### Quasi-Closed Bad Distribution

With fixed repaired kernel `q`, variables are `mu` on `H` and l1 defect
slacks.

```text
mu >= 0, sum_H mu = 1
mu q(H^c) <= xi
||mu - mu q|_H||_1 <= xi_stat
```

The no-resolvent fallback check is fixed linear algebra:

```text
max_i ((I-q|_H)^(-1)1)_i > A/tau
```

or infinite if `q|_H` has a closed class.

### Shadow Leakage Witness

For each `b in H`, variables are Step-5 dual circuit variables:

```text
mu_j       on outside_rho(b)
alpha_i,beta_i >= 0
```

Constraints:

```text
sum_j mu_j = 1
sum_j mu_j(p_j-p_b) = sum_i (beta_i-alpha_i)(p_i-p_b)
sum_i beta_i <= kappa
sum_j mu_j phi(p_j) >= phi(p_b) - D kappa
```

Objective:

```text
minimize mu(H1^c)
```

If the minimum is `> ell tau`, leakage is forced in this frozen model.

## Linear vs Bilinear Boundary

Linear after fixed `P`:

- separator feasibility and max margin;
- repaired-kernel quasi-stationary distribution;
- fixed-submatrix lifetime computation;
- failed-exposedness dual circuit;
- high-slice leakage minimization.

Linear with fixed sign pattern but variable `P`:

- row sums;
- negative mass bounds;
- fixed-support inequalities such as `q_i(H^c)<=xi`, after multiplying by
  the positive row mass.

Bilinear/nonconvex before freezing:

- `P^2=P`;
- `mu q` if `q` depends on variable rows;
- separator values `phi(p_i)`;
- witness equations `mu_j(p_j-p_b)` and `(beta-alpha)_i(p_i-p_b)`;
- lifetime/inverse constraints.

Combinatorial:

- vertex set;
- outside-`rho` sets;
- skeleton/bad/high membership;
- sign pattern for fixed-pattern relaxations.

## Artifacts

Script:

```text
agent-B/experiments/op-exposed-hull/c9_frozen_lp.py
```

Representative outputs:

```text
outputs/c9f_hume_s001.json
outputs/c9f_hume_product_s003_p2.json
outputs/c9f_regular_polygon_n12_arc.json
outputs/c9f_direct_conservative_top0_fullW.json
outputs/c9f_direct_conservative_top0.json
outputs/c9f_direct_conservative_top1.json
...
outputs/c9f_direct_conservative_top7.json
outputs/c9f_direct_free_top0.json
```

Commands are embedded in each JSON payload, along with the script SHA256.

## Numerical Results

### Hume

```text
family: hume, s=0.01
delta=1e-4, tau=0.01
R=[1], H=[2]
verdict=augmentation_vertex_present
e_2(rho)=0.99
```

The repaired kernel is closed on the bad row, so lifetime is infinite, but this
does not matter because the row is already an augmenting exposed vertex.

### Hume Product

```text
family: hume_product, s=0.003, power=2
delta=1.8000162e-05, tau=0.0042426597789594215
verdict=augmentation_vertex_present
H=[5,7,8]
```

Again the model stops before C9: the high bad rows are exposed at the tested
threshold.

### Regular Polygon Warning

```text
family: regular 12-gon projection
delta=0.20534180126147966, tau=0.4531465560516594
R=[0], H=[5,6,7]
rho=0.5 tau, kappa=0.25 tau
q-lifetime=2.3076290459731106
threshold=1/tau=2.2067915702883516
aggregate forced leak=0.05652055018244105
leak tolerance=0.04531465560516594
verdict=c9_frozen_failure_candidate
```

This is the known pure-convex-geometry warning.  It is useful for constants
and for testing the diagnostic, but the negative mass is not in the small
regime.

### Direct `A/B` Candidates

Top eight conservative direct-search samples, using the first exposed vertex
as a deliberately nonmaximal skeleton:

```text
8/8 verdict = augmentation_vertex_present
delta range about 0.0094 to 0.0099
```

The top `free_left_inverse` direct candidate has very long repaired-kernel
lifetime,

```text
q-lifetime ~= 550.93, threshold ~= 10.34,
```

but every high bad row is already exposed at the chosen threshold.  With the
full skeleton `R=W` on the top conservative direct sample:

```text
verdict=no_bad_vertices
```

## Dual Certificate Shape

The small-defect examples did not need a Farkas infeasibility certificate: they
stop by primal exposedness witnesses.  If a fixed example fails the diagnostic
in a nontrivial way, the expected dual certificates are:

1. separator dual: a convex combination of bad rows lies within the target
   margin of `conv(R)`;
2. quasi-closure dual: a potential giving `q`-drift to exit, hence the
   resolvent fallback;
3. shadow-leakage dual: a high-supported failed-exposedness witness exists, or
   the row is actually exposed at threshold.

The next mining step should export these LPs in a solver-readable format and
inspect HiGHS/Gurobi dual marginals when one of the nontrivial alternatives is
infeasible.

## Constants

Smoke constants used here are diagnostic, not proposed proof constants:

```text
Hume: rho=tau, kappa=0.25 tau.
Hume product: rho=tau, kappa=0.1 tau.
Regular polygon: rho=0.5 tau, kappa=0.25 tau, H1 gap=tau,
                 leak tolerance=0.1 tau.
Direct A/B: rho=tau, kappa in {0.05,0.1} tau.
```

The regular-polygon warning is sensitive to these constants; that is expected.
The small-defect examples are not.

## Failure Modes

1. A frozen C9 failure at large `delta` does not threaten `op-exposed-hull`.
2. The model currently uses a fixed separator returned by the max-margin LP;
   a different separator could change `H1` and the leakage optimum.
3. The high-average shadow constraint is imposed with a fixed drop multiple.
   It is a Step-3/C9 interface proxy, not a theorem.
4. The model tests distributional q-closure and lifetime on `H`; rowwise
   closure is stronger.
5. Once `P` is unfrozen, the witness equations and `P^2=P` are bilinear.

## Next Handoff

1. Add an LP-export mode for the separator and shadow-leak blocks so Gurobi can
   return basis/dual data.
2. Scan regular polygons across constants to learn the exact C9 constants that
   exclude the large-`delta` warning.
3. Search small `delta` direct `A/B` samples scored by long `q`-lifetime but
   with all high exposedness values just below threshold.
4. Build a fixed-sign-pattern nonlinear model for `n=4`/rank-3 circuits:
   keep sign supports fixed, impose `P^2=P`, and minimize `delta` subject to
   the frozen C9 failure inequalities.
