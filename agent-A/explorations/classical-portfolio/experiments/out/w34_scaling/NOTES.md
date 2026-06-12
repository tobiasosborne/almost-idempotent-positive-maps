# w34_scaling — orchestrator local probe (2026-06-12, network-resilience fallback)

Dense transverse-pair family (w33_sf_geom sec 5) scaled in m at fixed delta-cap.
Structural LP over B (fixed support L, BL=I, full-row negativity <= cap, B_0 >= 0
restriction => reported ratios are LOWER bounds). Scripts: dense_scaling.py;
data: dense_scaling_results.json (coarse), dense_scaling_fine_results.json (adaptive).

## Phase structure of max SF/delta over amplitude a (LOWER bounds, fixed intended chart)
- cap <= 0.3: ratio == 1.000 for ALL tested m (2..25; feasible amplitude scales ~ cap/m).
- cap = 0.4:  plateau at ratio 2.0 for m = 5..25.
- cap = 0.45: peak 8.9 (m=8, a=1/2), falls back to 2.0 at larger m on the tested grid.
- cap = 0.5:  ratio = m EXACTLY on the grid (m = 2..25, a = 1/2) — LINEAR GROWTH, unbounded in rank.

## m=3, cap=1/2, a=1/2 extracted solution (residuals ~1e-16; visibly rational)
B_0 = (0,...,0, 1/2, 1/2); foreign rows have entries in {5/6, ±1/6, 0, 1};
P's nonzero row negative masses all EXACTLY 1/2. Clean closed form evidently exists.

## CRITICAL CAVEAT (why this is NOT yet a banked claim)
The LP fixes the chart L and representative set. SF quantifies over the recomputed
MAX-VOLUME basis of the actual P. The cap=1/2 instances contain exact unit rows
(P_2 = e_2, P_4 = e_4, ...) and the recomputed chart may differ — exactly the
mechanism by which the w25 split-block "blow-up" died (w33_cex sec 5). The linear
growth claim is UNVERIFIED until the chart is recomputed per instance => w34_halfcex.
