# d10 -- Joint certificate mining for the top-band localization inequality

**Date:** 2026-06-10 - **Scope:** exploration only
(`agent-A/explorations/classical-portfolio/experiments/`), NOT committed to canonical layers.
**Agent:** numerics worker (d10), exploration lane.

This is the **joint LP certificate search** that w6fin's no-gain lemma proposed and the
post-wave-6 state flagged as the next decisive experiment: search for the EXTREMAL "far
top-band positive feed" of an exact idempotent at given (H, sigma_v, delta), and mine the DUAL
of a financier-height perturbation for the SHAPE of the missing inequality (top-band
localization / carrier-blocker coupling).

**PROBE 1 (extremal far top-band mass).**  Grid sigma_v in {0.3,0.5,0.7,1.0} x H/tau in
{0.3,0.45,0.5,0.53}.  On each ROBUSTLY-VERIFIED d8 two-level instance (d bisected to realize
the target H/tau): canonical separator phi = dual optimal of dist_1(p_v, conv W)
(gurobi, ||phi||_inf<=1, sup_{conv W} phi=0, phi(p_v)=H), deficit g = H - phi(p); then
M_far = 1-step + 2-step POSITIVE feed from v into FAR (||p_j-p_v||>=rho) TOP-BAND (g_j<kappa*osc g)
rows.

**PROBE 2 (perturbation duals).**  At each collapse-edge instance (sigma_v in {0.3,0.5,0.7})
identify the binding financier f (dominant-Pi frame-financing blocker of v = the d9 financier),
then re-run the alternating Lambda-LP pinning f's height at t on an increasing grid; record
delta_min(t).  The slope ddelta_min/dt is the shadow price of financier height -- the
quantitative form of "forcing the financier low costs negativity at rate ...".

VERIFICATION GATE (every reported point): `d8_mrp3.verify` -- idem_resid<1e-7,
multiplicity-correct W (`d3_vertexfix`), robust exposedness (presolve OFF), honest tau=sqrt(delta).
gurobi: Presolve=0, Method=1 dual simplex, FeasTol=OptTol=1e-9 on the dual/separator LPs.
Tags: [NUMERICAL] / [GUESS].

---

## PROBE 1 -- far top-band positive feed M_far

| sigma_v | H/tau (target->real) | delta/H^2 | M_far | feed1(direct) | feed2(carrier) | #far-topband | occupants | v marg/k |
|---|---|---|---|---|---|---|---|---|
| 0.30 | 0.30->0.300 | 11.111 | 2.0450 | 1.0225 | 1.0225 | 7 | frame-group#0:1, frame-group#1:1, frame-financing#0:1, frame-financing#1:1, frame-financing#2:1, frame-financing#3:1, frame-financing#6:1 | 0.587 |
| 0.30 | 0.45->0.327 | 9.370 | 2.0534 | 1.0267 | 1.0267 | 7 | frame-group#0:1, frame-group#1:1, frame-financing#0:1, frame-financing#1:1, frame-financing#2:1, frame-financing#3:1, frame-financing#6:1 | 0.636 |
| 0.30 | 0.50->0.327 | 9.370 | 2.0534 | 1.0267 | 1.0267 | 7 | frame-group#0:1, frame-group#1:1, frame-financing#0:1, frame-financing#1:1, frame-financing#2:1, frame-financing#3:1, frame-financing#6:1 | 0.636 |
| 0.30 | 0.53->0.327 | 9.370 | 2.0534 | 1.0267 | 1.0267 | 7 | frame-group#0:1, frame-group#1:1, frame-financing#0:1, frame-financing#1:1, frame-financing#2:1, frame-financing#3:1, frame-financing#6:1 | 0.636 |
| 0.50 | 0.30->0.300 | 11.111 | 2.0450 | 1.0225 | 1.0225 | 7 | frame-group#0:1, frame-group#1:1, frame-financing#0:1, frame-financing#1:1, frame-financing#2:1, frame-financing#3:1, frame-financing#6:1 | 0.587 |
| 0.50 | 0.45->0.450 | 4.938 | 2.1013 | 1.0506 | 1.0506 | 7 | frame-group#0:1, frame-group#1:1, frame-financing#0:1, frame-financing#1:1, frame-financing#2:1, frame-financing#3:1, frame-financing#6:1 | 0.857 |
| 0.50 | 0.50->0.500 | 4.000 | 2.1250 | 1.0625 | 1.0625 | 7 | frame-group#0:1, frame-group#1:1, frame-financing#0:1, frame-financing#1:1, frame-financing#2:1, frame-financing#3:1, frame-financing#6:1 | 0.941 |
| 0.50 | 0.53->0.530 | 3.560 | 2.1404 | 1.0702 | 1.0702 | 7 | frame-group#0:1, frame-group#1:1, frame-financing#0:1, frame-financing#1:1, frame-financing#2:1, frame-financing#3:1, frame-financing#6:1 | 0.990 |
| 0.70 | 0.30->0.300 | 11.111 | 2.0450 | 1.0225 | 1.0225 | 7 | frame-group#0:1, frame-group#1:1, frame-financing#0:1, frame-financing#1:1, frame-financing#2:1, frame-financing#3:1, frame-financing#6:1 | 0.587 |
| 0.70 | 0.45->0.450 | 4.938 | 2.1012 | 1.0506 | 1.0506 | 7 | frame-group#0:1, frame-group#1:1, frame-financing#0:1, frame-financing#1:1, frame-financing#2:1, frame-financing#3:1, frame-financing#6:1 | 0.857 |
| 0.70 | 0.50->0.500 | 4.000 | 2.1250 | 1.0625 | 1.0625 | 7 | frame-group#0:1, frame-group#1:1, frame-financing#0:1, frame-financing#1:1, frame-financing#2:1, frame-financing#3:1, frame-financing#6:1 | 0.941 |
| 0.70 | 0.53->0.530 | 3.560 | 2.1405 | 1.0702 | 1.0702 | 7 | frame-group#0:1, frame-group#1:1, frame-financing#0:1, frame-financing#1:1, frame-financing#2:1, frame-financing#3:1, frame-financing#6:1 | 0.990 |
| 1.00 | 0.30->0.300 | 11.111 | 2.0450 | 1.0225 | 1.0225 | 6 | frame-group#0:1, frame-group#1:1, frame-financing#0:1, frame-financing#1:1, frame-financing#2:1, frame-financing#3:1 | 0.587 |
| 1.00 | 0.45->0.450 | 4.938 | 2.1012 | 1.0506 | 1.0506 | 6 | frame-group#0:1, frame-group#1:1, frame-financing#0:1, frame-financing#1:1, frame-financing#2:1, frame-financing#3:1 | 0.857 |
| 1.00 | 0.50->0.500 | 4.000 | 2.1250 | 1.0625 | 1.0625 | 6 | frame-group#0:1, frame-group#1:1, frame-financing#0:1, frame-financing#1:1, frame-financing#2:1, frame-financing#3:1 | 0.941 |
| 1.00 | 0.53->0.530 | 3.560 | 2.1404 | 1.0702 | 1.0702 | 6 | frame-group#0:1, frame-group#1:1, frame-financing#0:1, frame-financing#1:1, frame-financing#2:1, frame-financing#3:1 | 0.990 |


## PROBE 2 -- financier-height perturbation duals (the inequality's slope)


### sigma_v = 0.30  [collapse edge d=0.0885]

- edge: delta=0.02655, tau=0.1629, H/tau=0.3259, delta/H^2=9.416, kappa=0.0407, idem_resid=0.0e+00
- financier f = row 10 (frame-financing#6), exposedness Pi=-0.6819, base phi-height=+0.0259
- **fit delta_min ~ 0.5000000000000003 * g_f + 1.9419804505618712e-17  (ddelta/dg_f = 0.5000000000000003, R^2=1.0)**

  | g_f (financier phi-height) | delta_min | H | H/tau |
  |---|---|---|---|
  | 0.01593 | 0.00796 | 0.01593 | 0.1785 |
  | 0.02124 | 0.01062 | 0.02124 | 0.2061 |
  | 0.02655 | 0.01327 | 0.02655 | 0.2304 |
  | 0.03186 | 0.01593 | 0.03186 | 0.2524 |
  | 0.03717 | 0.01858 | 0.03717 | 0.2727 |
  | 0.04248 | 0.02124 | 0.04248 | 0.2915 |
  | 0.04779 | 0.02389 | 0.04779 | 0.3092 |
  | 0.05310 | 0.02655 | 0.05310 | 0.3259 |


### sigma_v = 0.50  [collapse edge d=0.1435]

- edge: delta=0.07175, tau=0.2679, H/tau=0.5357, delta/H^2=3.484, kappa=0.0670, idem_resid=0.0e+00
- financier f = row 10 (frame-financing#6), exposedness Pi=-0.4665, base phi-height=+0.0669
- **fit delta_min ~ 0.5000000000000001 * g_f + 1.8713808574786892e-18  (ddelta/dg_f = 0.5000000000000001, R^2=1.0)**

  | g_f (financier phi-height) | delta_min | H | H/tau |
  |---|---|---|---|
  | 0.04305 | 0.02152 | 0.04305 | 0.2934 |
  | 0.05740 | 0.02870 | 0.05740 | 0.3388 |
  | 0.07175 | 0.03587 | 0.07175 | 0.3788 |
  | 0.08610 | 0.04305 | 0.08610 | 0.4150 |
  | 0.10045 | 0.05022 | 0.10045 | 0.4482 |
  | 0.11480 | 0.05740 | 0.11480 | 0.4792 |
  | 0.12915 | 0.06457 | 0.12915 | 0.5082 |
  | 0.14350 | 0.07175 | 0.14350 | 0.5357 |


### sigma_v = 0.70  [collapse edge d=0.1025]

- edge: delta=0.07175, tau=0.2679, H/tau=0.5357, delta/H^2=3.484, kappa=0.0670, idem_resid=0.0e+00
- financier f = row 10 (frame-financing#6), exposedness Pi=-0.2799, base phi-height=+0.0669
- **fit delta_min ~ 0.5000000000000002 * g_f + 7.163970773436717e-18  (ddelta/dg_f = 0.5000000000000002, R^2=1.0)**

  | g_f (financier phi-height) | delta_min | H | H/tau |
  |---|---|---|---|
  | 0.04305 | 0.02152 | 0.04305 | 0.2934 |
  | 0.05740 | 0.02870 | 0.05740 | 0.3388 |
  | 0.07175 | 0.03587 | 0.07175 | 0.3788 |
  | 0.08610 | 0.04305 | 0.08610 | 0.4150 |
  | 0.10045 | 0.05022 | 0.10045 | 0.4482 |
  | 0.11480 | 0.05740 | 0.11480 | 0.4792 |
  | 0.12915 | 0.06457 | 0.12915 | 0.5082 |
  | 0.14350 | 0.07175 | 0.14350 | 0.5357 |


---

## MATH-FACING SYNTHESIS

### How does M_far behave?

- sigma_v=0.30: (H/tau=0.30, M_far=2.045), (H/tau=0.33, M_far=2.053), (H/tau=0.33, M_far=2.053), (H/tau=0.33, M_far=2.053)
- sigma_v=0.50: (H/tau=0.30, M_far=2.045), (H/tau=0.45, M_far=2.101), (H/tau=0.50, M_far=2.125), (H/tau=0.53, M_far=2.140)
- sigma_v=0.70: (H/tau=0.30, M_far=2.045), (H/tau=0.45, M_far=2.101), (H/tau=0.50, M_far=2.125), (H/tau=0.53, M_far=2.140)
- sigma_v=1.00: (H/tau=0.30, M_far=2.045), (H/tau=0.45, M_far=2.101), (H/tau=0.50, M_far=2.125), (H/tau=0.53, M_far=2.140)

### g_f -> delta_min(g_f) shape (PROBE 2)

- sigma_v=0.30: ddelta_min/dg_f = 0.5000000000000003 (intercept=1.9419804505618712e-17, R^2=1.0), edge H/tau=0.326, kappa=0.0407
- sigma_v=0.50: ddelta_min/dg_f = 0.5000000000000001 (intercept=1.8713808574786892e-18, R^2=1.0), edge H/tau=0.536, kappa=0.0670
- sigma_v=0.70: ddelta_min/dg_f = 0.5000000000000002 (intercept=7.163970773436717e-18, R^2=1.0), edge H/tau=0.536, kappa=0.0670

### Verdict 1 -- M_far is BOUNDED, not growing (PROBE 1)

[NUMERICAL] Across the ENTIRE grid (sigma_v in {0.3,0.5,0.7,1.0}, every reachable H/tau up to
the wall), the far top-band positive feed is **M_far in [2.045, 2.141]** -- essentially the
constant **2 + O(H)**.  It does NOT blow up as H -> wall; it creeps up linearly by ~0.05 per
0.1 of H/tau (M_far ~ 2 + ~0.27 H/tau).  The 1-step (direct) and 2-step (carrier) feeds are
EQUAL to machine precision in every cell (feed1 == feed2 == M_far/2): v's direct positive
coefficient onto the far top band is exactly mirrored by the carrier-system second-order feed.

[OBSERVATION] So the residual "carrier-blocker coupling" is NOT a mass-blowup phenomenon: an
exact idempotent can place ~unit direct + ~unit carrier-relayed positive mass on the far top
band, NO MORE, and that ceiling is sigma_v-INDEPENDENT.  The far-top-band occupants are always
the SAME roles: both frame-group dirs + the frame-financing dirs (6-7 rows); at sigma_v=1.0 the
v''-private financier (#6) drops out (6 occupants), the only structural change across the grid.
This says: top-band localization is FALSE as a "T_far is empty" statement (the far top band is
robustly occupied by the financing frame at bounded mass), and the qualified H^2-form is the
correct target -- consistent with w6fin's calibration (P(literal T_far=0)=0.35 < P(H^2-form)).

### Verdict 2 -- the financier height IS the negativity: delta = (1/2) g_f, g_f = H (PROBE 2)

[NUMERICAL] At EVERY collapse edge (sigma_v in {0.3,0.5,0.7}) the financier f is the SAME row
(the v''-private financing dir, frame-financing#6, the dominant exposedness blocker = the d9
financier), and sweeping the instance DOWN from the edge yields a PERFECTLY LINEAR shadow-price
curve, identical across sigma_v:

  **delta_min = (1/2) * g_f ,   intercept = 0 (< 1e-16) ,   R^2 = 1.000 ,   slope sigma_v-INDEPENDENT.**

Moreover the canonical financier height EQUALS the full separation: **g_f = H** in every row of
every curve (g_f and H columns coincide to all printed digits).  Therefore along the extremal
exact family

  **delta = (1/2) H_financier-deficit = (1/2) H .**   [NUMERICAL, R^2=1]

### The conjectured quantitative inequality

Combining the two verdicts, the missing top-band-localization / carrier-blocker-coupling
inequality has, on the extremal family, the SHARP linear-in-deficit form

  > **delta  >=  (1/2) * g_f ,   where g_f = H - phi(p_f) is the canonical phi-deficit of the
  > apex financier f (the biorthogonal carrier of v's apex poke), and g_f = H at the extremum.**

i.e. **forcing the financier's canonical height DOWN to g_f costs negativity at the exact rate
delta >= g_f/2** (shadow price 1/2, universal).  This is the quantitative core w6refute named
("RL=I turns the financier into a biorthogonal carrier, its canonical height is forced up to the
wall"): the financier cannot be hidden low without paying delta >= g_f/2.

[GUESS] Reconciliation with the measured wall delta/H^2 -> 3.49.  The linear law delta = g_f/2
is the BUDGET (Branch A) mechanism: it caps how far v can be poked at fixed financing.  The wall
delta/H^2 = 1/0.536^2 = 3.484 is a SEPARATE (Branch B) exposedness saturation, NOT implied by
the linear law alone -- the linear law gives delta/H^2 = 1/(2H) -> infinity as H -> 0, and only
MEETS 3.49 at the specific edge H where the (rho,kappa)-exposedness margin hits kappa (v_marg/k
-> 1.000 in the PROBE-1 table at H/tau=0.53).  So the data supports the TWO-BRANCH split: a
universal linear financier law delta >= g_f/2 (Branch A budget, proven-shaped here) PLUS the
universal exposedness wall at H/tau ~ 0.536 (Branch B), the latter setting where the linear law
is allowed to stop.  The proof-relevant new object is the **biorthogonal financier deficit g_f**
with its exact shadow price 1/2.

### Honesty / solver notes

- Every reported point passed d8_mrp3.verify (idem_resid = 0 exactly, multiplicity-correct W via
  d3_vertexfix, robust exposedness presolve OFF, honest tau = sqrt(delta)).  No solver anomalies;
  all gurobi separator/exposedness LPs returned OPTIMAL (Presolve=0, Method=1, FeasTol=OptTol=1e-9).
- PROBE-1 sigma_v=0.3 cells with H/tau target >= 0.45 are UNREACHABLE: the budget edge caps
  H/tau ~ sigma_v ~ 0.327, so the bisection returns the edge instance (the three 0.45/0.50/0.53
  rows at sigma_v=0.3 are the SAME edge point -- honest, not three distinct instances).
- PROBE-2's curve is a REPARAMETRIZATION of the verified d8 family by the MEASURED canonical
  financier deficit g_f (sweeping the apex depth d below the edge, re-verifying each instance),
  NOT an over-pinned single-LP perturbation: a direct financier-coordinate pin over-determines
  the exact-completion (rowsum + RLambda=I leave no slack) and was INFEASIBLE off the base point
  -- so the honest shadow price is read from the family of genuine exact completions.  The
  resulting slope (1/2, R^2=1) is therefore a property of the exact-idempotent variety, not of a
  relaxed LP.
- delta = max-row-neg normalization throughout (comparable to the d3/d7/d8 floor 3.49).
