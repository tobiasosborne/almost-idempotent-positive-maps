# Subagent: LP/Game Certificate Mining For `op-exposed-hull`

Date: 2026-06-07.  Lane: Agent B sandbox.  Status: exploratory, not a
canonical proof shard.

## Verdict

Started Work Package 5.  The full negation of closed-bad-class augmentation is
not a single LP unless the row matrix and the combinatorics are fixed.  The
smallest useful model is a frozen-`P` linear diagnostic:

```text
fixed exact signed retraction P
+ chosen skeleton R
+ chosen bad vertex set B
+ common l1-dual separator from conv R
+ quasi-closed repaired-kernel distribution on B
+ failed-exposedness LP-dual circuits for all vertices in B.
```

This already distinguishes two important regimes:

- small Hume test: the model stops because an augmenting exposed vertex is
  present;
- regular-polygon warning: the frozen linear negation is feasible, but only at
  large negative mass (`delta ~= 0.205`), so it is a calibration obstruction,
  not a small-defect counterexample.

## Full Finite Negation Model

Unfrozen variables:

```text
p_ij                 row matrix P
u_ij,v_ij >= 0        sign split p_ij=u_ij-v_ij
binary signs          fixed sign pattern or MILP sign choices
R,B binaries          skeleton and bad-class choices
phi,s                 common separator
mu                    bad quasi-stationary distribution
alpha,beta,nu         failed-exposedness circuit witnesses
```

Core constraints:

```text
sum_j p_ij = 1
sum_j v_ij <= delta
P^2 = P
q_i = p_i^+/(1+neg(p_i))
B is q-closed or mu is q-quasi-stationary
phi(p_b)-sup_{r in R} phi(p_r) >= A tau
e_b(rho) < kappa for every b in B
```

Status of pieces:

- fixed `P`: separator, quasi-closure, and failed-exposedness circuits are LPs;
- fixed sign pattern but variable `P`: row sums, `neg<=delta`, rowwise exit
  bounds, and fixed-coefficient affine combinations are linear;
- bilinear/non-LP: `P^2=P`, `mu q` with variable `P`, variable separator
  against variable rows, and variable-row failed-exposedness circuits;
- combinatorial: vertices, outside sets, skeleton/bad membership, sign pattern.

Conclusion: a full unfrozen feasibility search is at least fixed-pattern
bilinear, and naturally a mixed-integer bilinear/nonconvex model.  The LP
route should mine frozen instances and fixed combinatorial patterns first.

## Frozen Linear Subproblem

I implemented:

```text
agent-B/experiments/op-exposed-hull/lp_game_certificate.py
```

For a fixed row matrix it computes `q_i=p_i^+/(1+neg(p_i))`,
`W_{rho,kappa}`, and three LP blocks.

Common separator:

```text
find phi,s
|phi_l| <= 1
phi(r)-s <= 0                 for r in R
phi(b)-s >= bad_margin         for b in B.
```

Quasi-closed bad distribution:

```text
mu >= 0, sum_B mu=1
mu q(B^c) <= exit_tol
||mu - mu q|_B||_1 <= stationarity_tol.
```

Failed-exposedness dual for each `b in B`:

```text
min sum_i beta_i
sum_{j outside rho(b)} nu_j = 1
sum_j nu_j(p_j-p_b) = sum_i (beta_i-alpha_i)(p_i-p_b)
alpha,beta,nu >= 0.
```

The bad vertex fails the exposedness threshold when the optimum is `< kappa`.

The script returns:

```text
augmentation_vertex_present
no_common_separator_for_bad_set
bad_set_not_quasi_closed
frozen_linear_negation_feasible
```

## Smoke Tests

Commands are recorded in the JSON outputs.  I ran `py_compile`, both smoke
models, and `git diff --check` on the new LP-game artifacts.

Hume `s=0.01`:

```text
delta=1e-4, tau=0.01, rho=0.01, kappa=0.0025
R=[1], B=[2]
verdict=augmentation_vertex_present
e_2(rho)=0.99, dual beta minimum=0.99
```

Regular polygon `n=12`, opposite arc:

```text
delta=0.20534180126147966, tau=0.4531465560516594
rho=0.2265732780258297, kappa=0.11328663901291485
R=[0], B=[5,6,7]
verdict=frozen_linear_negation_feasible
common separator margin=2.3213672050459184
quasi-closed exit=0.4333452128040396
stationarity_l1=0.43334521280403954
e_b(rho)=0.066987298... < kappa for b=5,6,7
```

Hashes are in the JSON payloads; external `sha256sum` was also recorded in the
session transcript.

## Constants

The smoke model used deliberately loose constants:

```text
Hume: rho=tau, kappa=0.25 tau, bad_margin=0.25 tau.
Polygon: rho=0.5 tau, kappa=0.25 tau, bad_margin=0.25 tau,
         exit_tol=10 tau, stationarity_tol=20 tau.
```

These are not proposed proof constants.  The next mining pass should scan:

```text
rho_mult in {1,2,4,8}
kappa_mult in {0.01,0.05,0.1,0.25}
bad_mult in {1,4,16}
exit_mult in {0.01,0.05,0.1,0.25,1}
```

## Failure Modes

1. The regular-polygon feasible certificate is expected: it is a pure convex
   geometry obstruction with large `delta`.
2. The common-separator LP is stronger than "each bad row is far from
   `conv R`"; failure of a common separator does not disprove a bad class.
3. The quasi-closed distribution LP is weaker than rowwise closure.  It finds
   long-lived averages, not necessarily a closed communicating class.
4. The failed-exposedness LP is frozen-row only.  With variable rows its
   circuit equation is bilinear in row positions and circuit weights.
5. The current model does not yet extract a dual certificate tying the three
   LP blocks together; it is a feasibility/diagnostic layer.

## Next Handoff

1. Grid-scan small bad subsets for fixed `P`.
2. Add fixed-sign-pattern bilinear search for `n=4` corank-one `2|2`.
3. Compare distributional closure with rowwise exit bounds.
4. Export LP blocks for `gurobi_cl` dual/basis inspection.
5. If small-`delta` frozen negations never appear, prove the mined inequality:
   frozen feasible negation forces `max_i neg(p_i) >= c rho^2`.
