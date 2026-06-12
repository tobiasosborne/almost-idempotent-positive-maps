# w35_charge: prove exists-chart SF at small delta_0 — the dual-flow charging argument

You are a codex (gpt-5.5) PROVER. Target: the EXISTS-chart form of the
signed-face excess at small delta_0, with explicit dimension-free constant.
Everything points at it being true with C ~ 2 for delta_0 <= 0.3: the w34
hostile audit confirmed the dual-flow mechanism ("duplication splits the flow
but cannot raise row-0 mass"); every known bad instance collapses to ratio ~1
in a favorable quasi-max-volume chart; the threshold data says trouble only
starts around delta_0 ~ 0.35-0.5 (envelope conjecture C ~ 1/(1-2delta)).

Repo root: /home/tobias/Projects/almost-idempotent-positive-maps (readable).
Workdir (writable): /tmp/codex-sigma-wall/w35_charge.
PROGRESS PROTOCOL: one short line per stage to progress.md.
ARTIFACT RULE: long form to proof.md, NEVER answer.md. sympy/HiGHS available;
gurobi BROKEN in sandbox.

## THE TARGET (exists-chart SF, small delta_0)
P real d x d, P^2 = P, P1 = 1, all row negative masses <= delta <= delta_0
(take delta_0 = 1/4 or 0.3 — choose what makes the proof clean and SAY SO).
Prove: there EXISTS a set of actual rows u_1..u_k forming a basis of the row
space with volume >= theta * (max actual-row volume) (theta a universal
constant; theta = 1 i.e. an exact max-volume tie is fine if your construction
achieves it), such that in its chart p_j = sum_t a_t(j) p_{u_t}:
  sum_j (P_{u_s j})_+ ( sum_{t != s} (-a_t(j))_+ - (1 - a_s(j)) )_+
     <= C * delta   for every s,   C universal (delta_0, theta dependence OK).

## TOOLS ALREADY PROVED/CONFIRMED (cite, do not re-derive)
- Deficit bound: sum_j (P_{u_s j})_+ (1 - a_s(j)) <= 2 delta for ANY chart
  with |a_t| <= 1 (w31 sec 2 — uses only Pa_s = a_s and the box bound).
- The P = LB, BL = I frame (w34_audit A7: rank conditions, minor-scan
  equivalence det(P_U P_U^T) = det(L_U)^2 det(B B^T)).
- Sum rules sum_j P_{u_s j} a_t(j) = delta_st; coefficients are P-harmonic
  (P a_t = a_t).
- Duplicate/stacking invariance mechanism (w34_audit A2): BL = I sees only
  aggregate +/- mass over identical coefficient columns.
- Fixed-support tight certificates (w33_sf_geom sec 4 + w34_audit A4):
  pair 1+4a^2, k=4 cycle 1+3a^2.
- The collapse mechanism (w34_halfcex sec 2): swapping exact unit rows INTO
  the basis removes the split-mass row from the representative role; the
  remaining displayed excess is bounded by the negativity actually paid.

## SUGGESTED ROUTE (the charging argument; deviate if you find better)
1. CHART SELECTION: among quasi-max-volume actual-row bases, choose one
   minimizing a potential (candidates: total excess sum_s SF_s; or the number
   of rows with E_s(j) > 0 weighted by mass; or prefer-minimal-support
   greedy). The selection must be shown well-defined and to achieve theta.
2. CHARGING: in the chosen chart, show every unit of weighted excess
   sum_j (B_sj)_+ E_s(j) is injectively charged to row negative mass
   SOMEWHERE in P (not only row u_s — the staircase shows the cost can sit in
   FOREIGN representative rows: there, each foreign row pays exactly 1/2).
   The dual-flow form: E_s(j) > 0 means the coefficient row j carries
   net-negative foreign flow; BL = I forces compensating positive flow
   through columns whose rows then either (a) pay negativity, or (b) are
   swap-eligible (near-unit rows) — and case (b) is excluded by the chart
   selection (a swap would increase the potential's volume/decrease excess,
   contradicting minimality). Make this precise.
3. VERIFY on the three exact stress families (transverse pair, dense pair
   k=7, staircase m=2,3): your chosen chart must yield SF <= C delta with
   your claimed C — exact rational checks, scripts saved.
4. If the full proof does not close: prove the best PARTIAL (e.g. SF bounded
   by C delta + C' delta * max_j E_s(j), or rank <= 4, or delta_0 smaller) and
   state the exact missing inequality in display math (died-at protocol).

## DELIVERABLE (verdict-first; long form to proof.md)
VERDICT: PROVED (statement + C + theta + delta_0, full proof, stress-family
checks) / PARTIAL (what is proved + the exact missing step) / DIED-AT (the
precise wall). Calibrated P(survives hostile audit). All code saved.
