# d8 — Numerically DECIDING the MRP regime (the LAST open parameter region of HLC)

**Date:** 2026-06-10 · **Scope:** exploration only (`agent-A/explorations/classical-portfolio/experiments/`,
NOT committed to canonical layers). **Agent:** Fable 5 (1M), exploration lane.

**Question (MRP — middle-regime pinch, `fable-hlc-attack.md` §6.2).** The fable HLC pass proved every
*other* counterexample architecture collapses and compressed the open set to ONE explicit two-level
parameter regime: a top vertex `v` at deficit `g≈0`, height `H` above `conv W`, with external (off-own-site)
coefficient mass `σ_v ∈ (≈3δ, τ/2)` drawn from supplier groups at level `ℓ≈2.2δ/σ_v`; a `ψ`-max vertex
`v″` at level `≤2σ_v` with forced external mass `σ_{v″}≈ρ/2.2≈1.8τ`; `k_groups` supplier groups, pairwise
`≥ρ`-separated or coincident. **CLAIM (MRP):** exactness forces `max-neg ≥ a·H²` in this regime too.
**Decider:** minimize `δ/H²` over EXACT completions `P=ΛR` (`RΛ=I_r`, `P1=1`, `P²=P`, `neg ≤ δ`,
`τ=√δ`, `ρ=4τ`, `κ=τ/4`) of the two-level family over a `σ_v × k_groups × δ × r × n` grid, robustly
recomputing `W` post-hoc.

## TL;DR — VERDICT: **MRP HOLDS / HLC SUPPORTED in the middle regime** (no refutation) [NUMERICAL, strong]

| quantity | value | tag |
|---|---|---|
| **Global min verified `δ/H²`** | **≈ 3.484** (max-neg units), at `H/τ = 0.536` | NUMERICAL |
| where it lives | the universal `(ρ,κ)`-exposedness wall `H/τ ≈ 0.536` (`σ_v ≳ 0.5`) | NUMERICAL |
| **the σ_v law (candidate middle-regime lemma)** | **wall `H/τ ≈ min(σ_v, 0.536)` ⇒ floor `δ/H² ≈ max(1/σ_v², 3.49)`** | NUMERICAL |
| MRP regime itself (`σ_v ≲ τ/2 ≪ 0.5`) | `δ/H² ≈ 1/σ_v² ≫ 3.49` — the **SAFEST** region for HLC | NUMERICAL |
| `k_groups` effect | **NONE** (1, 2, 3 identical to 4 digits) | NUMERICAL |
| refutation candidate (`δ/H² < 3`) | **NONE** found; the floor is bounded below by ≈ 3.48 | NUMERICAL |

**Normalization:** `δ = max_i neg(p_i)` (max-neg units), identical to the d3 envelope and d7 FTI-2 decider.
Our floor `δ/H² ≈ 3.49` **re-finds the same d3/d7 floor** through the MRP-specific two-level construction +
an optimizer over `(Λ,R)`, and finds nothing below it.

---

## The decisive structural fact (why MRP holds): the σ_v–wall

The MRP family is realizable as an exact idempotent (verified, `idem_resid = 0`), enters the hypothesis
(`v` a genuine vertex, far from `conv W`, failing `(ρ,κ)`-exposedness, with the supplier cluster also
hidden), and its floor is governed by ONE relation, found cleanly across the grid:

> **The hidden cluster (`v` + suppliers) fails `(ρ,κ)`-exposedness only while its exposedness margin stays
> below `κ`. Pushing `v` out (raising `H/τ`) raises that margin LINEARLY; at the ceiling the margin reaches
> `κ` and the ENTIRE cluster exposes at once, joins `W`, and `H` collapses to 0.** The ceiling is
> `H/τ ≈ min(σ_v·(1+o(1)), 0.536)`.

Two binding regimes, two certificates (read directly off the optimizer's verified instances):

- **`σ_v ≲ 0.5` (the genuine MRP regime):** the cluster collapses at `H/τ ≈ σ_v`, with cluster
  exposedness margin only `≈ σ_v/0.5 · κ < κ` at collapse — i.e. it is NOT the exposedness wall that
  binds, it is the **external-mass budget**: `v` simply runs out of supplier mass to be pushed further
  before some OTHER mechanism (the suppliers themselves leaving the hidden cone) ends the regime. Floor
  `δ/H² ≈ 1/σ_v²`, which **blows up** as `σ_v → 0`.
- **`σ_v ≳ 0.536` (outside the MRP regime):** the cluster reaches the universal `(ρ,κ)`-exposedness wall;
  at collapse the exposedness margin = `1.000 κ` EXACTLY (verified to 3 digits) and `H/τ → 0.536`. This
  is the SAME wall the d3 envelope and d7 FTI-2 decider hit. Floor `δ/H² → 1/0.536² ≈ 3.49`.

**The MRP regime is therefore the SAFEST part of parameter space for HLC, not the most dangerous.** The
fable pass's worry — that the middle regime is "borderline-infeasible, forced negativity ≈ 0.8δ, within a
factor ~2 of the budget" — does not materialize numerically: in the middle regime `σ_v ≪ 1`, the floor is
`1/σ_v² ≫ 3.49`, far ABOVE the budget. Only by leaving the MRP regime (`σ_v → O(1)`) does the architecture
approach 3.49, and there it is just the ordinary exposedness wall, not a two-level evasion.

### The σ_v-certificate (the floor table over the grid)

`δ/H²` floor and collapse-`H/τ` at each `σ_v` (kg=1; kg=2,3 IDENTICAL — `out/d8_decision.json`):

| `σ_v` | wall `H/τ` | floor `δ/H²` | `1/σ_v²` | cluster margin/`κ` at collapse |
|---|---|---|---|---|
| 0.05 | 0.050 | 400.0 | 400 | 0.10 (budget-bound, NOT wall) |
| 0.10 | 0.102 | 96.2 | 100 | 0.20 (budget-bound) |
| 0.20 | 0.211 | 22.5 | 25 | 0.42 (budget-bound) |
| 0.35 | 0.387 | 6.68 | 8.2 | 0.75 (approaching wall) |
| 0.50 | 0.536 | **3.48** | 4.0 | **1.000 (WALL)** |
| 0.70 | 0.536 | **3.48** | 2.0 | **1.000 (WALL)** |
| 1.00 | 0.535 | **3.50** | 1.0 | **1.000 (WALL)** |

The crossover is sharp at `σ_v ≈ 0.536`: below it the budget binds (`δ/H² ≈ 1/σ_v²`), at/above it the
exposedness wall binds (`δ/H² ≈ 3.49`). The MRP regime `σ_v ∈ (≈3δ, τ/2)` sits entirely in the budget-bound
branch where `δ/H²` is large.

### Scaling of the best `δ/H²` with `δ`

The family is scale-covariant in the poke depth `d`: at the floor, `δ = d`, `H = 2d`, so
**`δ/H² = 1/(4d)`, MINIMIZED at the collapse edge `d_c`** (the largest `d` that still hides). The collapse
edge sits at the `σ_v`-wall: `H/τ = 2d/√d = 2√d = 0.536 ⇒ d_c ≈ 0.0718 ⇒ δ/H² = 1/(4·0.0718) = 3.48`,
**independent of the absolute `δ` scale** once the grid resolves the edge (the `H²` form binds as
`δ ≥ 3.49 H²`, `p = 2`). A coarser `δ`-grid under-finds the edge and reports a larger floor — the SAME
sampling artifact flagged in the d3/d7 reports; the sampling-independent statement is the wall
`H/τ ≤ 0.536 ⇒ δ ≥ 3.49 H²`. No instance trends toward `δ/H² < 3` as `δ → 0`; the floor is flat at 3.49.

**Floor instance (rationalized, `idem_resid = 0`):** `n=17`, `r=11`, `δ = 0.0715`, `H = 0.143 = 2δ`,
`τ = 0.2674`, `H/τ = 0.5348`, `δ/H² = 3.497 = 1/(4δ)`. One step further (`d = 0.072`) the cluster
exposedness margin crosses from `0.998κ` to `1.001κ`, all four suppliers + `v` expose, `nW` jumps `11→16`,
`H → 0`.

---

## Methodology (replicating the d7 verified-gate decider) [METHODOLOGY]

- **Encoding (`d8_mrp3.py`).** The two-level family is built in **barycentric coordinates** over a frame
  `R0 = [I_r | 0]` (`d3_main.bary_to_P`), so rows of `P` ARE the bary-coefficient vectors and
  `neg(p_i)` is the negative part of those coefficients — directly controllable. Suppliers form `k_groups`
  `ρ`-split pairs, **each split financed POSITIVELY** by mass on low "sub-C" financing dirs (NOT by
  negativity — the wiggle-rigidity tension); they are pushed out of `conv(anchors)` by a small negative
  anchor coefficient `d` (the ONLY negativity, `⇒ δ = d`). `v` = convex combo of all suppliers (external
  mass `σ_v`) + `(1−σ_v)` on its own private frame dir + a small apex poke so `v` is a genuine VERTEX.
  `v″` is the analogous `ψ`-max vertex on a second pillar.
- **Optimizer (`d8_opt.py`).** Take the bary geometry as seed, pin the LOAD-BEARING linear data (frame
  archetypes; `v` fully, fixing the far hidden geometry ⇒ entry guaranteed; supplier group-site feed),
  and run the **exact alternating `(Λ,R)` LPs** (`d7_fti2.alternating_min`, Gurobi, `FeasTol=OptTol=1e-9`)
  minimizing max-row-neg over the remaining realization + frame freedom — the known blind spot. *(The
  optimizer confirmed `R` is INERT once the rows are pinned: load-bearing / v-only / full pins all give
  identical floors, reproducing the d3/d7 "R duals inert" finding.)*
- **Verification gate (`d8_mrp3.verify`, every reported point), all via the validated robust infra:**
  idempotence `idem_resid < 1e-7` (achieved `= 0`); `W` recomputed with the MULTIPLICITY-CORRECT vertex
  test (`d3_vertexfix`) + robust margin-maximizing exposedness LP (presolve OFF); **honest `τ = √δ` from the
  instance's OWN `δ`** (NOT the design `τ`); `dist₁(v, conv W) ≥ H` re-verified against `conv W`; `v`
  genuinely failing `(ρ,κ)`-exposedness AND a vertex; suppliers verified OUT of `W`. Unverified points
  never enter the floor. Crash-safe JSON checkpoints, `python3 -u`, flushed prints.

## Controls (`d8_controls.py`, `out/d8_controls.json`)

| control | expectation | result |
|---|---|---|
| (ii) wiggle-rigidity / lone-far collapse | a far supplier with NO surrounding web exposes → joins `W`, `dist→0` | `lone_far_exposed=True`, `collapse_ok=True` ✓ |
| (iii) F-ND (near-delta rows expose) | a row with tiny off-own-site mass is exposed | `near_delta_exposed=True` ✓; and at `σ_v ≲ 0.05` the top `v` is itself near-delta → `v_fails_exposed=False`, never enters (matches the PROVED fact F-ND) ✓ |
| (i) reproduce the 3.49 floor | the d3/d7 floor `δ/H² ≈ 3.49` | re-found by the MRP decider itself: global min `= 3.484` at `H/τ = 0.536` (a hand-built single/double poke does NOT reproduce it — the floor needs the surrounding web + optimizer, exactly as d3/d7 reported; control-i's stand-alone hand construction therefore reads `inf` and is superseded by the main decider's re-finding) |

## The candidate middle-regime lemma (described in math) [GUESS → NUMERICAL]

Let `m_cluster(H)` be the `(ρ,κ)`-exposedness margin of the hidden top cluster `{v} ∪ suppliers`. The
numerics show, across the grid:

> **(σ_v–wall, NUMERICAL).** For the MRP two-level family, the cluster stays hidden iff `H/τ ≤ W(σ_v)` with
> `W(σ_v) = min(σ_v·(1+o(1)), 0.536)`; consequently the verified floor obeys
> `δ/H² ≥ 1/W(σ_v)² = max(1/σ_v², 3.49)`. In the MRP regime `σ_v ≤ τ/2` this gives
> `δ/H² ≥ 4/τ² = 4/δ → ∞`, i.e. the middle regime is bounded FAR away from any refutation; the binding
> constraint there is the **external-mass budget** (`v` cannot be pushed past `H/τ ≈ σ_v` on `σ_v` units of
> supplier mass), not the exposedness wall.

This is the exact shape the fable pass was missing in §4.4/§6.2: the "pinch" the proof needs is the linear
growth of the cluster exposedness margin in `H/τ` capped at `κ`, AND the external-mass budget that caps
`H/τ` at `σ_v` before that. Both are `O(H²)`-favorable; neither leaves slack for a counterexample. The
fable's borderline `0.8δ` estimate assumed the regime could reach `H/τ ~ 0.5` at small `σ_v` — numerically
it cannot (it collapses at `H/τ ~ σ_v ≪ 0.5` first).

## PROVED / NUMERICAL / GUESS tags + solver anomalies

- **[NUMERICAL, strong]** MRP holds: global min verified `δ/H² ≈ 3.484 > 0` over the full `σ_v × k_groups ×
  δ × r × n` grid; no `δ/H² < 3` instance; the floor coincides with the universal exposedness wall
  `H/τ ≈ 0.536` and is reached only OUTSIDE the MRP regime (`σ_v ≳ 0.5`).
- **[NUMERICAL]** The σ_v–wall law `H/τ = min(σ_v, 0.536)`, floor `δ/H² = max(1/σ_v², 3.49)`. `k_groups`
  irrelevant (1=2=3 to 4 digits). The `H²` exponent binds (`p = 2`).
- **[NUMERICAL]** Scale-invariance of the floor at 3.49 (modulo the known grid-sampling caveat at small `δ`).
- **[PROVED, consistency]** F-ND reproduced: small-`σ_v` (near-delta) `v` is exposed and never enters —
  matches the fable's proved fact; the decider's entry gate honestly excludes those.
- **[GUESS]** Generalization to arbitrary abstract modules: the decider tests **realized-row** completions
  with explicit `(Λ,R)`, `RΛ=I` in `ℓ¹` embeddings; the Layer-1 structure theorem (`op-layer1-gap`) stays
  OPEN. The abstract-coordinate-sign loophole (d6 frame-transfer, OPEN) is not addressed by a realized-row
  decider — but it is the separate open transfer inequality, not an MRP counterexample to `neg(p_i)`.
- **Solver anomalies:** none. Gurobi 13.0.1 alternating LPs at `FeasibilityTol = OptimalityTol = 1e-9`;
  exposedness LPs presolve-OFF (`exposed_margin`); idempotence residuals `= 0` (exact frame). No HiGHS
  status-4 / Gurobi non-OPTIMAL events entered the verified set. The `(Λ,R)` optimizer reproduced "R inert
  once rows pinned" (load-bearing/v-only/full pins identical), so the cost is forced by the far geometry +
  the σ_v budget + the exposedness wall, exactly as in d7.

## Verdict

The MRP regime — the SOLE surviving open architecture from the fable HLC pass — does **NOT** refute HLC and
is in fact the **safest** region of parameter space for it. The two-level family hits the SAME `δ/H² ≈ 3.49`
floor at the SAME `H/τ ≈ 0.536` exposedness wall as every other architecture, and only when driven OUTSIDE
its defining regime (`σ_v → O(1)`); inside the regime (`σ_v ≤ τ/2`) the external-mass budget caps `δ/H²` at
`≈ 1/σ_v² ≫ 3.49`. `k_groups` provides no escape. This **closes the last open parameter region numerically
in HLC's favour** and hands the proof a concrete candidate middle-regime lemma (the σ_v–wall). HLC remains
unrefuted; calibrated `P(HLC true)` consistent with the fable pass's 0.75–0.8, now with the last regime's
floor measured and bounded away from refutation.

## Files (all under `experiments/`, reproducible; none committed)

- `d8_mrp3.py` — the financed-wiggle bary MRP family (`build`) + robust `verify` (honest τ).
- `d8_opt.py` — optimizer-backed decider: pin load-bearing data, alternating `(Λ,R)` LP min-neg, verify.
- `d8_decision.py` → `out/d8_decision.json` — the consolidated collapse-edge floor sweep over
  `(σ_v, k_groups)` with the cluster-exposedness-margin certificate. **VERDICT: HLC_SUPPORTED_floor_at_wall,
  min δ/H² = 3.484, no refutation.**
- `d8_controls.py` → `out/d8_controls.json` — controls (lone-far collapse, F-ND); control-i superseded by
  the main decider's re-finding of 3.49.
- `d8_sweep.py` → `out/d8_sweep.json` — the initial raw-geometry entry-map scan (pre-apex-fix; superseded).
- `d8_mrp.py`, `d8_mrp2.py` — earlier encoder iterations (poke-coordinate and first bary form); retained
  for provenance of the scale-mismatch diagnosis (a direct `−H` poke costs `neg = H`, not `H²` — the wall
  that forced the financed-wiggle design). No `out/d8_refutation.json` — none found.
