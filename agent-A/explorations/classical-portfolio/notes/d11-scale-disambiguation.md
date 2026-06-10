# d11 -- Scale disambiguation of the d10 financier law + wave-7 M-minimization

**Date:** 2026-06-10/11 - **Scope:** exploration only
(`agent-A/explorations/classical-portfolio/experiments/`), NOT committed to canonical layers.
**Agent:** numerics worker (d11), exploration lane.

Mission: resolve the d10 PROBE-2 scale degeneracy (it probed only the default scale where the
collapse edge has delta ~ 0.0718 and H = 2*delta EXACTLY, so "g_f = H" and "g_f = 2*delta" were
indistinguishable) by sweeping the collapse edge across >= 2 decades of delta; and run the
wave-7 aggregate-coupling minimization M = sum_b mu_b sum_{j in A_v} lambda_j P+_{jb}.

VERIFICATION GATE (every reported point): d8_mrp3.verify -- idem_resid<1e-7, multiplicity-correct
W (d3_vertexfix), robust exposedness (presolve OFF), honest tau=sqrt(delta).  gurobi separator/
exposedness LPs: Presolve=0, Method=1 (dual simplex), FeasTol=OptTol=1e-9.  Tags: [NUMERICAL]/[GUESS].

---

## SURVIVED READING (stated plainly)

**[NUMERICAL] Neither reading survives as a *distinguishing* statement inside the d8 two-level
family, because that family RIGIDLY ENFORCES the identity `g_f = H = 2*delta`.**  Across the full
collapse-edge ladder -- 7 verified scales spanning **delta in [0.00063, 0.07175], 2.06 decades** --
every single edge has `g_f/H = 1.0000`, `g_f/(2 delta) = 1.0000`, and `H/(2 delta) = 1.0000` to all
printed digits, and the financier-law slope is `ddelta_min/dg_f = 0.5000, R^2 = 1.0000` at EVERY
scale (not just the default one d10 probed).  So the d10 "law" `delta_min = (1/2) g_f` is the BUDGET
IDENTITY `delta = H/2`, and "g_f = H" is a SEPARATE identity of the same family -- the three
quantities are the SAME line, never disambiguable here.  The slope 1/2 does NOT scale; it is exactly
universal.  **There is no crossover scale within the d8 family: H = 2 delta is structural, holding
even at delta ~ 6e-4.**

**Consequence for the closer (the honest resolution of the orchestrator catch).**  Because the d8
family lives ON the line `H = 2 delta`, it CANNOT reach the flat floor `delta/H^2 -> 3.49`
(`H = 0.536 sqrt(delta)`) at small delta: its `delta/H^2 = 1/(4 delta)` BLOWS UP as delta -> 0
(500 at delta=6e-4 in the table), and it only TOUCHES 3.49 at its single wall edge (sigma_v=0.5,
delta=0.0718), exactly where the two lines `H = 2 delta` and `H = 0.536 sqrt(delta)` cross.  So this
family is a BUDGET-line carrier, not a flat-floor carrier.  The reading that "g_f ~ H persists across
delta would force delta >= H/2 and contradict the flat floor" is therefore VACUOUS as a worry: the
d8 family never claims to populate the flat floor at small delta -- the flat-floor instances live in
a DIFFERENT construction (d3/d7 stacking).  The correct math statement the data supports is the
SECOND d10 reading, sharpened: **`g_f = H` is a separator/financier identity (the canonical apex
deficit of the biorthogonal financier EQUALS the full separation H), and `delta = g_f/2` is the
budget shadow price (height costs negativity at rate 1/2).**  The real open question is unchanged and
correctly posed: why the (rho,kappa)-exposedness EDGE forces `H/tau` up to ~0.536 (Branch B wall),
which on the `H = 2 delta` line lands at delta ~ 0.0718 -- i.e. why hiding pushes the financier to
the band edge ONLY at the wall.  The new resolving column is `g_f/(kappa*osc)`: it climbs
monotonically 0.0999 -> 0.9997 along the ladder and hits 1.000 EXACTLY at the wall edge, confirming
that `g_f` reaches the top-band threshold `kappa*osc` precisely at the exposedness wall, not before.

**[NUMERICAL] TASK B verdict: min M >= c*tau, the coupling lemma is NOT refuted.**  The aggregate
coupling `M = sum_b mu_b sum_{j in A_v} lambda_j P+_{jb}` is bounded AWAY from 0 at every verified
instance: `M/tau = 1.075` at the wall edge (sigma_v=0.5) and `M/tau = 3.02` at the small scale
(sigma_v=0.3, delta=0.0266); minimizing over the family's realization freedom (sweeping d down from
the edge) only RAISES M/tau (1.075 -> 1.673 as d shrinks; 3.02 -> 4.819), so the edge is the
minimizer and `min M/tau = 1.075` (wall) is the binding value.  **c >= 1.07 at the wall.**  ~80% of M
is the financier's OWN self-coupling: `frame-financing#6` is simultaneously v's dominant positive
carrier (`lambda = 0.47`) AND the dominant C10 top-band blocker (`mu = 0.47`), so the binding term is
`mu_f * lambda_f * P+_{ff}` -- the RECIPROCAL-CARRIER structure w6refute/w7 named, now measured: the
financier receives its own carrier mass, and that self-overlap is what keeps M >= c*tau.

---

## TASK A -- delta-scale sweep of the financier law (the disambiguation)

Collapse edge swept over a sigma_v ladder (budget regime: lower sigma_v collapses earlier, so the edge delta spans decades AND H/tau varies, breaking the H=2delta degeneracy *if* the family allows it).

| sigma_v | d_edge | delta | H | 2delta | H/tau | kappa*osc | g_f | g_f/H | g_f/2delta | g_f/(k*osc) | H/2delta | slope | R^2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.05 | 0.01250 | 0.00063 | 0.00125 | 0.00125 | 0.0500 | 0.01251 | 0.00125 | 1.0000 | 1.0000 | 0.0999 | 1.0000 | 0.5000 | 1.0000 |
| 0.10 | 0.02600 | 0.00260 | 0.00520 | 0.00520 | 0.1020 | 0.02556 | 0.00520 | 1.0000 | 1.0000 | 0.2034 | 1.0000 | 0.5000 | 1.0000 |
| 0.15 | 0.04050 | 0.00608 | 0.01215 | 0.01215 | 0.1559 | 0.03921 | 0.01215 | 1.0000 | 1.0000 | 0.3099 | 1.0000 | 0.5000 | 1.0000 |
| 0.20 | 0.05550 | 0.01110 | 0.02220 | 0.02220 | 0.2107 | 0.05326 | 0.02220 | 1.0000 | 1.0000 | 0.4168 | 1.0000 | 0.5000 | 1.0000 |
| 0.30 | 0.08850 | 0.02655 | 0.05310 | 0.05310 | 0.3259 | 0.08363 | 0.05310 | 1.0000 | 1.0000 | 0.6349 | 1.0000 | 0.5000 | 1.0000 |
| 0.40 | 0.12700 | 0.05080 | 0.10160 | 0.10160 | 0.4508 | 0.11842 | 0.10160 | 1.0000 | 1.0000 | 0.8580 | 1.0000 | 0.5000 | 1.0000 |
| 0.50 | 0.14350 | 0.07175 | 0.14350 | 0.14350 | 0.5357 | 0.14354 | 0.14350 | 1.0000 | 1.0000 | 0.9997 | 1.0000 | 0.5000 | 1.0000 |


### sigma_v = 0.05  forced-height curve (edge d=0.0125, financier=frame-financing#6)

| g_f | delta_min | H | 2delta | H/tau |
|---|---|---|---|---|
| 0.00038 | 0.00019 | 0.00037 | 0.00038 | 0.0274 |
| 0.00050 | 0.00025 | 0.00050 | 0.00050 | 0.0316 |
| 0.00062 | 0.00031 | 0.00062 | 0.00063 | 0.0354 |
| 0.00075 | 0.00038 | 0.00075 | 0.00075 | 0.0387 |
| 0.00087 | 0.00044 | 0.00087 | 0.00088 | 0.0418 |
| 0.00100 | 0.00050 | 0.00100 | 0.00100 | 0.0447 |
| 0.00113 | 0.00056 | 0.00112 | 0.00112 | 0.0474 |
| 0.00125 | 0.00063 | 0.00125 | 0.00125 | 0.0500 |

- fit: delta_min = 0.49999999999999173 * g_f + 2.3602778652241592e-17  (R^2=1.0)

### sigma_v = 0.10  forced-height curve (edge d=0.0260, financier=frame-financing#6)

| g_f | delta_min | H | 2delta | H/tau |
|---|---|---|---|---|
| 0.00156 | 0.00078 | 0.00156 | 0.00156 | 0.0559 |
| 0.00208 | 0.00104 | 0.00208 | 0.00208 | 0.0645 |
| 0.00260 | 0.00130 | 0.00260 | 0.00260 | 0.0721 |
| 0.00312 | 0.00156 | 0.00312 | 0.00312 | 0.0790 |
| 0.00364 | 0.00182 | 0.00364 | 0.00364 | 0.0853 |
| 0.00416 | 0.00208 | 0.00416 | 0.00416 | 0.0912 |
| 0.00468 | 0.00234 | 0.00468 | 0.00468 | 0.0967 |
| 0.00520 | 0.00260 | 0.00520 | 0.00520 | 0.1020 |

- fit: delta_min = 0.4999999999999957 * g_f + 3.8410312777313354e-18  (R^2=1.0)

### sigma_v = 0.15  forced-height curve (edge d=0.0405, financier=frame-financing#6)

| g_f | delta_min | H | 2delta | H/tau |
|---|---|---|---|---|
| 0.00364 | 0.00182 | 0.00364 | 0.00365 | 0.0854 |
| 0.00486 | 0.00243 | 0.00486 | 0.00486 | 0.0986 |
| 0.00608 | 0.00304 | 0.00607 | 0.00608 | 0.1102 |
| 0.00729 | 0.00365 | 0.00729 | 0.00729 | 0.1207 |
| 0.00850 | 0.00425 | 0.00850 | 0.00851 | 0.1304 |
| 0.00972 | 0.00486 | 0.00972 | 0.00972 | 0.1394 |
| 0.01093 | 0.00547 | 0.01093 | 0.01094 | 0.1479 |
| 0.01215 | 0.00608 | 0.01215 | 0.01215 | 0.1559 |

- fit: delta_min = 0.49999999999999345 * g_f + 6.75384383581292e-17  (R^2=1.0)

### sigma_v = 0.20  forced-height curve (edge d=0.0555, financier=frame-financing#6)

| g_f | delta_min | H | 2delta | H/tau |
|---|---|---|---|---|
| 0.00666 | 0.00333 | 0.00666 | 0.00666 | 0.1154 |
| 0.00888 | 0.00444 | 0.00888 | 0.00888 | 0.1333 |
| 0.01110 | 0.00555 | 0.01110 | 0.01110 | 0.1490 |
| 0.01332 | 0.00666 | 0.01332 | 0.01332 | 0.1632 |
| 0.01554 | 0.00777 | 0.01554 | 0.01554 | 0.1763 |
| 0.01776 | 0.00888 | 0.01776 | 0.01776 | 0.1885 |
| 0.01998 | 0.00999 | 0.01998 | 0.01998 | 0.1999 |
| 0.02220 | 0.01110 | 0.02220 | 0.02220 | 0.2107 |

- fit: delta_min = 0.5000000000000016 * g_f + -4.1149385254259133e-17  (R^2=1.0)

### sigma_v = 0.30  forced-height curve (edge d=0.0885, financier=frame-financing#6)

| g_f | delta_min | H | 2delta | H/tau |
|---|---|---|---|---|
| 0.01593 | 0.00797 | 0.01593 | 0.01593 | 0.1785 |
| 0.02124 | 0.01062 | 0.02124 | 0.02124 | 0.2061 |
| 0.02655 | 0.01328 | 0.02655 | 0.02655 | 0.2304 |
| 0.03186 | 0.01593 | 0.03186 | 0.03186 | 0.2524 |
| 0.03717 | 0.01859 | 0.03717 | 0.03717 | 0.2727 |
| 0.04248 | 0.02124 | 0.04248 | 0.04248 | 0.2915 |
| 0.04779 | 0.02390 | 0.04779 | 0.04779 | 0.3092 |
| 0.05310 | 0.02655 | 0.05310 | 0.05310 | 0.3259 |

- fit: delta_min = 0.5000000000000004 * g_f + 8.322572149783598e-18  (R^2=1.0)

### sigma_v = 0.40  forced-height curve (edge d=0.1270, financier=frame-financing#6)

| g_f | delta_min | H | 2delta | H/tau |
|---|---|---|---|---|
| 0.03048 | 0.01524 | 0.03048 | 0.03048 | 0.2469 |
| 0.04064 | 0.02032 | 0.04064 | 0.04064 | 0.2851 |
| 0.05080 | 0.02540 | 0.05080 | 0.05080 | 0.3187 |
| 0.06096 | 0.03048 | 0.06096 | 0.06096 | 0.3492 |
| 0.07112 | 0.03556 | 0.07112 | 0.07112 | 0.3771 |
| 0.08128 | 0.04064 | 0.08128 | 0.08128 | 0.4032 |
| 0.09144 | 0.04572 | 0.09144 | 0.09144 | 0.4276 |
| 0.10160 | 0.05080 | 0.10160 | 0.10160 | 0.4508 |

- fit: delta_min = 0.5000000000000008 * g_f + -6.776370833129477e-17  (R^2=1.0)

### sigma_v = 0.50  forced-height curve (edge d=0.1435, financier=frame-financing#6)

| g_f | delta_min | H | 2delta | H/tau |
|---|---|---|---|---|
| 0.04305 | 0.02153 | 0.04305 | 0.04305 | 0.2934 |
| 0.05740 | 0.02870 | 0.05740 | 0.05740 | 0.3388 |
| 0.07175 | 0.03588 | 0.07175 | 0.07175 | 0.3788 |
| 0.08610 | 0.04305 | 0.08610 | 0.08610 | 0.4150 |
| 0.10045 | 0.05023 | 0.10045 | 0.10045 | 0.4482 |
| 0.11480 | 0.05740 | 0.11480 | 0.11480 | 0.4792 |
| 0.12915 | 0.06458 | 0.12915 | 0.12915 | 0.5082 |
| 0.14350 | 0.07175 | 0.14350 | 0.14350 | 0.5357 |

- fit: delta_min = 0.49999999999999906 * g_f + 9.544805168276839e-17  (R^2=1.0)

## TASK B -- wave-7 aggregate-coupling minimization M

M := sum_b mu_b sum_{j in A_v} lambda_j P+_{jb};  lambda = v's normalized positive carrier measure, mu = C10 exposedness-dual witness on rho-far TOP-BAND blockers (normalized).

| sigma_v | delta_edge | M (edge) | M/tau (edge) | min M/tau (sweep) | #topband blockers | mu blocker roles |
|---|---|---|---|---|---|---|
| 0.50 | 0.07175 | 0.28806 | 1.0754 | 1.0754 | 7 | frame-financing#6:0.47, frame-group#0:0.21, frame-financing#2:0.09, frame-financing#3:0.09, frame-group#1:0.08, frame-financing#0:0.03, frame-financing#1:0.03 |
| 0.30 | 0.02655 | 0.49211 | 3.0202 | 3.0202 | 7 | frame-financing#6:0.68, frame-group#0:0.14, frame-financing#2:0.05, frame-financing#3:0.05, frame-group#1:0.05, frame-financing#0:0.01, frame-financing#1:0.01 |

