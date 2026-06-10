<!--
ROLE: d12 numerics worker -- the DECISIVE DMF falsification probe (test DMF off the d8 family).
Agent: numerics worker (exploration lane). Date: 2026-06-10/11.
Inputs: wave8-fable-closer.md (DMF = SC2, the single open core; the exact dual (diamond);
  witness-anatomy methodology Stage 2b/N1-N6), d8_mrp3.py (the financed-wiggle STACKING family),
  d8_opt.py (optimizer that drives it to the floor), d1_infra.py / d3_vertexfix.py (validated gates).
Script: experiments/d12_dmfprobe.py.  Data: out/d12_dmfprobe.json + out/d12_logs/*.json.
Tags: [NUMERICAL] (LP-extracted, gated, machine-precision residuals).
-->

# d12 -- DMF depth profiles OFF the d8 family

## VERDICT (first, as mandated)

**DMF SUPPORTED.** Across **12 verified hidden-top-vertex instances OFF the d8 wall-edge**
family (d8_mrp3 financed-wiggle STACKING construction, optimizer-driven to the floor, with
VARIED off-edge parameters: sigma_v in {0.5, 0.7}, ell in {0.65, 0.72, 0.75}, ma in {2, 3},
k_groups in {2, 3}), spanning **delta/H^2 in [3.57, 35.7]** (delta in [0.007, 0.070], the
floor region [3.4, 6] AND the mid-envelope), every OPTIMAL exposedness-dual witness is
**100% deep**:

  **min observed m* = 0.99999... (= 1.0 to machine precision) across all 12 instances,
  all deep-mass = 1.0000 at deficit g = H exactly (g/H = 1.000 for every mu-carrying row);
  zero shallow mass (shallow_fraction = 0.0000 everywhere).**

No all-shallow witness was found. DMF is **exactly saturated (m* = 1, E = 0)** off the d8
family exactly as it was ON the edge (w8_witness_check N2). The wave8 row-witness mechanism
(RW: the optimal witness IS v's own row identity, mu = gamma*P^+_v, all carriers are
W-vertices at deficit H) **reproduces verbatim off-family**. [NUMERICAL, gated; all LP
identity/mass-balance residuals <= 3e-16; presolve OFF on every exposedness/distance LP;
multiplicity-correct robust W; honest tau = sqrt(delta) per instance.]

## The sigma_tilde-vs-sigma_v finding (N3, decisive)

On EVERY passing instance: **sigma_v (off-own-site positive mass) = 1.007 .. 1.070, but
sigma-tilde (v's positive coeff mass on rows OUTSIDE conv W) = 0.0000 EXACTLY.** v's positive
carriers are precisely the W-vertices; v draws NO positive mass from outside conv W. This is
the wave8 N3 catch confirmed off-family: the formal off-own-site sigma_v ~ 1 throughout (these
v's have P_vv = 0, a private/anchor own-site), so the "branch split sigma_v <=/>= 1/2" is
**vacuous in sigma_v** (always Branch B) and the robust branch variable is sigma-tilde = 0
here. Any sigma_v-resolved statement MUST be re-read as sigma-tilde before banking. The
witness depth has nothing to do with sigma_v: it is forced by the row identity (RW), and the
carriers are W-rows (deep by construction, g = H).

## Per-instance table

| label | d_poke | delta | tau | H | H/tau | delta/H^2 | t*/kappa | sigma_v | sigma~ | m*_obs | shallow | classes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| floor_d100sv70 | 0.100 | 0.0700 | 0.2646 | 0.1400 | 0.529 | **3.571** | 0.989 | 1.070 | 0.000 | 1.000 | 0.000 | W:1.0 |
| floor_kg3      | 0.135 | 0.0675 | 0.2598 | 0.1350 | 0.520 | **3.704** | 0.990 | 1.067 | 0.000 | 1.000 | 0.000 | W:1.0 |
| floor_ma3      | 0.130 | 0.0650 | 0.2550 | 0.1300 | 0.510 | **3.846** | 0.991 | 1.065 | 0.000 | 1.000 | 0.000 | W:1.0 |
| floor_d120     | 0.120 | 0.0600 | 0.2449 | 0.1200 | 0.490 | 4.167 | 0.992 | 1.060 | 0.000 | 1.000 | 0.000 | W:1.0 |
| floor_d110     | 0.110 | 0.0550 | 0.2345 | 0.1100 | 0.469 | 4.545 | 0.994 | 1.055 | 0.000 | 1.000 | 0.000 | W:1.0 |
| mid_d090       | 0.090 | 0.0450 | 0.2121 | 0.0900 | 0.424 | 5.556 | 0.996 | 1.045 | 0.000 | 1.000 | 0.000 | W:1.0 |
| mid_d070       | 0.070 | 0.0350 | 0.1871 | 0.0700 | 0.374 | 7.143 | 0.998 | 1.035 | 0.000 | 1.000 | 0.000 | W:1.0 |
| mid_d050ma3    | 0.050 | 0.0250 | 0.1581 | 0.0500 | 0.316 | 10.00 | 1.000* | 1.025 | 0.000 | 1.000 | 0.000 | W:1.0 |
| small_d050sv35 | 0.050 | 0.0175 | 0.1323 | 0.0350 | 0.265 | 14.29 | 1.000* | 1.018 | 0.000 | 1.000 | 0.000 | W:1.0 |
| small_d030kg3  | 0.030 | 0.0150 | 0.1225 | 0.0300 | 0.245 | 16.67 | 1.000* | 1.015 | 0.000 | 1.000 | 0.000 | W:1.0 |
| small_d020     | 0.020 | 0.0100 | 0.1000 | 0.0200 | 0.200 | 25.00 | 1.000* | 1.010 | 0.000 | 1.000 | 0.000 | W:1.0 |
| small_d010sv70 | 0.010 | 0.0070 | 0.0837 | 0.0140 | 0.167 | 35.71 | 1.000* | 1.007 | 0.000 | 1.000 | 0.000 | W:1.0 |

(*) t*/kappa ~ 1 at small delta: v sits just barely hidden (the row-witness bound
t* = nu_v/(1+nu_v) approaches kappa = tau/4 from below; v is exposed exactly when
nu_v/(1+nu_v) >= tau/4, i.e. tau >= 2-sqrt(3), the wave8 N4 corner). Two intended floor
cells (sv35, sv70 at d~0.143) had v ALREADY EXPOSED (v in W) -- the optimizer fully exposed v
at those exact params -- and were correctly REJECTED by the gate (FAIL_v_in_W), not counted.

Depth profile is IDENTICAL for all 12: cumulative mu-mass at deficit >= H - E equals 1.0000
for E/H in {0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0} -- i.e. ALL the mu-mass sits at the maximal
deficit g = H. m*_observed (mu-mass at g >= H - 5 delta/tau) = 1.0000.

## What this means for DMF / the sigma_v-wall residual

1. **DMF is not falsified.** The decisive numeric (a single verified all-shallow witness OFF
   the corner) did NOT appear. On the entire reachable off-d8 floor the optimal witness is
   v's own row identity (RW, wave8 2c.1): mu = gamma*P^+_v on W-vertices, every carrier at
   g = H. This is the SAME object as on the edge (w8_witness_check N1/N2), now confirmed
   across delta/H^2 in [3.57, 35.7] and across distinct (sigma_v, ell, ma, k_groups). The
   exchange is saturated everywhere: Sum mu*g = t*R to machine precision (e.g. floor_d100sv70:
   0.14000 = 0.14000), within 1.1% of kappa*R.

2. **The depth is a structural consequence of RW, not a delicate inequality.** Because v's
   positive carriers are W-rows (sigma-tilde = 0) and W-rows have g = H (they lie on the
   separator's zero level), the witness is forced deep by construction. The "all-shallow
   witness" of wave8 3.4 would require v to draw positive mass from OUTSIDE conv W
   (sigma-tilde > 0) onto top-band non-W rows -- which the d8_mrp3 STACKING family never
   realizes at the verified floor (the suppliers are hidden NON-vertices that the optimizer
   keeps off the witness; v's witness picks only the W anchors/private pillar).

3. **HONEST LIMITATION (the genuinely off-family blind spot remains).** This probe reaches the
   off-d8 floor via the d8_mrp3 STACKING construction (different parametrization, but the
   same financed-wiggle architecture). The FTI-2 distinct-vertex MUTUAL-SHADOW construction
   (d7_fti2 / d7_drive: two vertices v1,v2 each shadowing the other, the structure wave8 3.4
   names as where an all-shallow web could hide) could NOT be VERIFIED at small delta -- the
   alternating-LP search returns either no hidden config or degenerate huge-delta/tiny-H
   instances (delta/H^2 in the thousands, not the floor), confirming d7_hunt's verdict that
   distinct far vertices ALWAYS expose at (4tau, tau/4) on the canonical frame. So the
   all-shallow web, IF it exists, is NOT realized by any verified instance reachable here; it
   remains the open object, but no numerics support its existence. P(DMF true with m* ~ 1)
   is RAISED by this probe (the off-family floor saturates DMF exactly), consistent with the
   wave8 calibration P ~ 0.75.

4. **Corner confirmation (bonus).** The verified floor lands exactly on the wave8 N4 law
   H = 2*delta, delta/H^2 = 1/(4*delta): floor_d100sv70 at delta = 0.070 gives
   delta/H^2 = 3.571 = 1/(4*0.070), approaching the corner value (7+4sqrt3)/4 = 3.482 at
   delta* = (2-sqrt3)^2 = 0.0718. H/tau maxes at 0.529 (-> 2(2-sqrt3) = 0.536 at the corner).
   The mission's "H ~ 0.536 sqrt(delta) >> 2delta" premise is the CORNER, not small delta: at
   small delta these hidden instances have H = 2delta << sqrt(delta) (H/tau = 2tau -> 0), as
   wave8 N4 established. The floor delta/H^2 ~ 3.5 is reached only by pushing delta UP to the
   corner -- which is exactly where the table tops out (floor_d100sv70).

## Methodology / reproducibility

- Instances: d8_mrp3.build + d8_opt.decide_opt(load_bearing pins, 4 starts, 14 rounds),
  Gurobi alternating (Lambda,R) LP minimizing max-row-neg; the d8 wall-edge
  (d=0.1435, sigma_v=0.5, ell=0.65, ma=2, k_groups=2) is EXCLUDED; all 12 use off-edge params.
- Gate (each instance, reject on fail): idem_resid < 1e-7 (all ~1e-16); multiplicity-correct
  robust W (d3_vertexfix.well_exposed_set_robust); v a robust vertex; H = dist1(p_v, conv W)
  > 0; v genuinely the max-height hidden vertex (scanned all non-W vertices); v fails
  (4tau, tau/4)-exposedness (t* < kappa).
- Witness: exposedness LP for v solved with scipy HiGHS, **presolve OFF**; optimal dual
  (mu, alpha, beta, gamma) read from ineqlin/eqlin marginals (the w8_witness_check pattern);
  identity residual of (diamond) <= 3e-16, |1+A-B-gamma| <= 3e-16, |B - t*| <= 7e-17 -- the
  witness identity holds to machine precision on every instance.
- Separator: canonical phi via LP (||grad||_inf <= 1, sup_{conv W} phi <= 0, max phi(p_v));
  g = H - phi, ||Pg - g||_inf checked (~1e-16, g is P-stationary affine), R = osc(g).
- Outputs: experiments/d12_dmfprobe.py; out/d12_dmfprobe.json (checkpoint per instance);
  out/d12_logs/<tag>.json (full anatomy + P per instance); out/d12_logs/run.log.
  No d12_DMF_witness_candidate.json was written (no all-shallow witness found).

## Solver anomalies (honest)

None. All LPs solved at first method (HiGHS, presolve OFF), status 0. The only "failures" were
the two intended floor cells where the optimizer EXPOSED v (v joined W) so there was no hidden
top vertex to test -- a correct geometric outcome, gated out, not a solver fault.
