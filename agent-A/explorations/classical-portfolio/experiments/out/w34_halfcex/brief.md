# w34_halfcex: the half-delta staircase — closed form, CHART RECOMPUTATION (the critical audit), and the delta* threshold

You are a codex (gpt-5.5) BUILDER/AUDITOR. The orchestrator's local LP probe
found an apparent phase transition for the signed-face excess (SF) on the dense
transverse-pair family — including LINEAR-IN-RANK growth at delta = 1/2 — but
the headline claim is UNVERIFIED in the one way that has already killed a
previous "blow-up" (the w25 split-block): the max-volume chart was FIXED, not
recomputed. Your job: settle it.

Repo root: /home/tobias/Projects/almost-idempotent-positive-maps (readable).
Workdir (writable): /tmp/codex-sigma-wall/w34_halfcex.
PROGRESS PROTOCOL: one short line per stage to progress.md (eager flush).
ARTIFACT RULE: long form to proof.md, NEVER answer.md. Save all code+outputs.
TOOLING: SciPy/HiGHS + sympy (exact rationals). gurobi is BROKEN inside this
sandbox (HostID license mismatch) — do not waste time on it.

## INPUTS (read first, under agent-A/explorations/classical-portfolio/)
1. experiments/out/w34_scaling/NOTES.md — the finding + the caveat (READ THE
   CAVEAT TWICE). Scripts dense_scaling.py + JSON results in the same dir.
2. notes/swarm-answers/w33_sf_geom.md — the dense-pair family definition
   (sec 5), the exact k=7 ratio-17/8 instance, the named fixed-support theorem.
3. notes/swarm-answers/w33_cex.md — sec 5: HOW the split-block blow-up died
   under max-volume recomputation (the failure mode you must rule out or
   confirm); the exact-rational auditor sf_exact.py in
   experiments/out/w33_cex/ (REUSE IT — it recomputes the max-volume basis by
   exact Gram determinants and evaluates SF in the recomputed chart).

## THE FAMILY (orchestrator's extracted m=3, cap=1/2, a=1/2 solution)
k = 2m+1 representatives; L rows: e_0..e_{2m}, x_pm = e_0 pm a(sum_{1..m} e_t
- sum_{m+1..2m} e_t); d = 2m+3. The m=3 LP solution (residuals 1e-16):
B_0 = (0,...,0,1/2,1/2); odd-index foreign rows have diagonal 5/6,
off-diagonals pm 1/6, pair entries pm 1/6; even-index rows are exact unit
vectors e_{2t}; P's nonzero row negative masses all EXACTLY 1/2; SF (intended
chart) = m*a*(1/2+1/2) = m/2, ratio = m at cap = 1/2.

## TASKS (in order; the chart audit is the deliverable that matters)
1. CLOSED FORM: rationalize the family for general m (sympy): write B(m) and
   P(m) = L B(m) explicitly; verify EXACTLY: P^2 = P, BL = I, row sums 1, all
   row negative masses <= 1/2 (and record the exact value).
2. **CHART RECOMPUTATION (CRITICAL)**: for each m in {2,3,5,8}, run the exact
   max-volume audit (w33_cex sf_exact.py conventions: recompute the max-volume
   ACTUAL-ROW basis by exact Gram/minor maximization, recompute coefficients,
   re-evaluate SF as stated for EVERY representative s, take the max). Report
   SF_recomputed/delta vs m. THREE possible outcomes — say which:
   (a) ratio still ~ m -> genuine rank-unbounded excess at delta_0 = 1/2:
       SF as stated is FALSE at delta_0 = 1/2 (dimension-free C impossible
       there). State it as a theorem with the exact family.
   (b) ratio collapses (chart artifact, like split-block) -> name the
       mechanism precisely (which rows enter the recomputed basis, why the
       excess vanishes).
   (c) intermediate -> quantify.
   NOTE the instances contain exact unit rows (P_{2t} = e_{2t}) and duplicate/
   degenerate structure — handle max-volume TIES the way w33_cex sec 7 did
   (scan tie bases, report the WORST/BEST over ties, since SF quantifies over
   "the" max-volume basis — if ties give different answers, flag that as a
   statement-level ambiguity for the registry).
3. THRESHOLD MAP: with the recomputed-chart auditor, trace max ratio vs cap on
   [0.30, 0.50] (step 0.025, m up to ~12, amplitude adaptively chosen): locate
   delta* = sup{delta_0 : ratio bounded in m}. Conjecture the form of
   C(delta_0) (e.g. ~ 1/(1-2*delta_0)?) from the data. Even rough is fine —
   say what is data vs conjecture.
4. SMALL-DELTA SUPPORT: confirm (recomputed chart) that for cap <= 0.3 this
   family's ratio stays ~1 — i.e. SF with C(delta_0) ~ 1-2 for delta_0 <= 0.3
   is consistent with all evidence.

## DELIVERABLE (verdict-first; long form to proof.md)
VERDICT: CHART-CONFIRMED BLOW-UP AT delta=1/2 (+ closed-form family, exact
verification, delta* estimate, C(delta_0) conjecture) / CHART ARTIFACT (+ the
collapse mechanism, stated precisely as a candidate lemma — that mechanism
would be a PROOF INGREDIENT for SF) / MIXED (quantified). Calibrated
P(survives audit) per claim. All code + exact outputs saved.
