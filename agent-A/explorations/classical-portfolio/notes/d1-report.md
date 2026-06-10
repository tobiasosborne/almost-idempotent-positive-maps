# D1 report — exact-signed-retraction plateau hunt (op-exposed-hull)

**Date:** 2026-06-10  · **Branch:** agent-a/classical-portfolio · **Scope:** decide whether
`op-exposed-hull` admits a counterexample (a "τ-plateau": rows far from `conv W` by `≫ τ`,
with `τ=√δ`, in an EXACT signed affine retraction `P` with `P²=P`, `P1=1`, row-negative-mass `≤ δ`).

**Honesty tags used below:** PROVED (exact instance / exact infeasibility), NUMERICAL (solver
evidence at finite precision), GUESS (heuristic / not yet pinned).

---

## Bottom line

**No counterexample found. The evidence is strongly conjecture-consistent (NUMERICAL), and the
mechanism that would protect a plateau is shown to be self-defeating.** The one apparent
counterexample the hunt produced (a `ratio ≈ 69` spike at `δ ≈ 8.4e-4`) was traced to a **solver
artifact** — a *false-negative* in the well-exposedness LP from scipy HiGHS *simplex* returning
status 4 ("numerical difficulties") on near-coincident rows — **not** a real plateau. After
hardening the LP (interior-point + presolve-off + a margin-maximizing reformulation), the same
exact idempotent gives `max_i dist₁(pᵢ, conv W)/τ ≈ 0`. A later, more aggressive hunt produced
~20 more apparent counterexamples (reported `ratio` up to `inf`); **all were the same degenerate
near-duplicate-row artifact and collapse to `ratio ≈ 0`** under the robust test. Red→green
regression test pins both waves (`test_lp_robustness.py`).

Across all structured families and ~5000+ random EXACT idempotents the τ-scaled ratio is **bounded
by ≈ 0.12 and does NOT grow as δ→0** (it shrinks). That matches the prior 4500-sample finding of
`O(δ)` distances and is the opposite of a counterexample signature.

---

## Task 1 — infrastructure (PROVED to be correct on knowns)

`experiments/d1_infra.py`: exact idempotence check (`P²=P`, `P1=1` to machine precision),
per-row negative mass / `δ`, vertex test (LP), **well-exposedness LP** (affine `h:K→[0,1]`,
`h(v)=0`, `h(pᵢ)≥κ` on ρ-far rows), and `dist₁(pᵢ, conv W)` (LP). Headline `ratio_stats`.
Validated (`d1_validate.py`, `out/d1_validate.json`):

| instance | δ | τ | max ratio | note |
|---|---|---|---|---|
| identity (n=4) | 0 | 0 | 0 | every row a vertex |
| Baake–Sumner stochastic idempotent (absorbing + transient) | 0 | 0 | 0 | transient rows ∈ conv(absorbing); W = absorbing |
| Baake–Sumner n=6 (3 absorbing + 3 transient) | 0 | 0 | 0 | same |
| Hume rank-one `P=I−uvᵀ` (3×3) | 1 | 1 | 0 | exact retraction; plateau row self-exposes |
| random `P=ΨΦ, ΦΨ=I_r` (n=8) | ~0.34 | ~0.58 | 0 | conjecture-consistent |

The exposedness LP was independently checked to return **infeasible** on a genuinely
non-exposed configuration (a vertex = affine midpoint of two ρ-far rows) — so it is not vacuously
"always exposed".

**`P²=P` is exact by construction** via `P = Λ R` with `R Λ = I_r`, `R` rows sum 1, `Λ` rows sum 1
(then `P² = Λ(RΛ)R = ΛR = P` and `P1 = Λ(R1) = Λ1_r = 1`). PROVED algebra.

---

## Task 2 — the R Λ = I_r coupling and the binding obstruction (the load-bearing part)

### Geometry (PROVED)
All `n` rows of `P=ΛR` lie in the **(r−1)-dimensional affine flat** = affine span of the `r`
archetype rows of `R`. Via the affine iso `λ ↦ λR` the ℓ¹ geometry of the rows is the geometry of
the abstract points `λᵢ` in the simplex-plane `{Σ=1}`. `RΛ=I_r` is **biorthogonality**: the signed
measures `μ_a = R[a,:]` (each summing to 1) and the coordinate-functions `φ_b = Λ[:,b]` (summing to
1 at each row) satisfy `⟨μ_a, φ_b⟩ = δ_{ab}` — i.e. `P=ΛR` is the standard oblique rank-`r` projector.

### Obstruction #1 — signed ABSTRACT coordinates do NOT force negativity (PROVED, decisive)
`d2_plateau.py`: for EVERY abstract plateau geometry tried (push the plateau abstract point out to
`−e₁+2e₃`, r=3..5, push up to 1.0), minimizing `δ` over the archetype geometry `R` (an LP over `R`
with `RΛ=I`, rows-sum-1) returns **`δ = 0` exactly**. The optimizer re-coordinatizes: the "outside"
abstract point is realized as an honest **nonnegative vertex** `e_k`, which is then well-exposed and
joins `W`. So abstract negativity is illusory — `R` absorbs it. *This is why a naive "use signed
barycentric weights" plateau cannot exist: signs in `Λ` are free; what matters is `neg(ΛR)`.*

### Obstruction #2 — a single far row SELF-EXPOSES (PROVED)
`d2_fixR.py`: pin the realized geometry (`R` = clean basis) and force one plateau row to
`(−s,0,…,1+s)` (genuine `δ=s>0`). The exact idempotent is valid, but the plateau row is an
**extreme vertex of K and is itself well-exposed** (a downward functional exposes it) — so it joins
`W` and `dist₁(·,conv W)=0`. A lone far row never escapes `W`.

### Obstruction #3 — hiding a cluster requires negativity that SCALES with height (PROVED scaling, the crux)
To be far from `conv W` and non-exposed, a row must be **hidden inside a cluster** of far rows that
mutually shadow. `d2_hide.py` shows a far circuit of `K` rows CAN make its members non-exposed —
**but only when the configuration radius `R` is comparable to the negativity it costs.** Reading the
**REAL** `τ=√δ` from the rows' own negativity (not a fake `τ=1`):

| circuit radius R | δ (real) | τ (real) | REAL max ratio |
|---|---|---|---|
| 0.5 | 0.71 | 0.84 | 0.000 |
| 1.0 | 1.91 | 1.38 | 0.000 |
| 2.0 | 4.33 | 2.08 | 0.000 |
| 4.0 | 9.16 | 3.03 | 0.774 |

The negativity grows **in lockstep** with the height/radius (the codex *height/leakage balance*
`η ~ τ`). Pushing the plateau up to escape `conv W` raises `δ`, hence `τ`, hence `ρ=Cτ`, which
**re-exposes** the cluster. This is a **self-defeating loop** — the conjecture's protective
mechanism. (The fake-`τ=1` ratio of ~19–69 vanishes once `τ` is taken honestly.)

### Pure-geometry core (PROVED at conjecture scaling)
`d2_geom.py`: at the conjecture scaling `κ = c·τ` (κ *small*), a tall "cap" of rows has all its
vertices **well-exposed regardless of height** (a "lift-everything-but-me" affine functional always
exists). Small κ makes exposedness *easy*; the residual cap distance never grows with height. The
geometry alone strongly favors the conjecture.

### So WHERE does the plateau break? (the answer to the task's key question)
The `RΛ=I_r` coupling does not break it directly; rather it leaves the negativity `δ` exactly equal
to `neg(ΛR)`, which the geometry then ties to height. The composite obstruction is:
**(far from conv W) ⇒ (must be a hidden cluster) ⇒ (cluster height costs `δ ≳ height²` i.e.
height `≲ τ`) ⇒ (re-exposed at ρ=Cτ).** Every escape route closes. No single binding *equality*
constraint kills it; the *scaling* `δ ↔ height²` does. (GUESS for the universal constant; the
numerics put `C′ ≲ 0.2`.)

---

## Task 3 — optimization hunt (NUMERICAL, conjecture-consistent)

`d3_hunt.py` / `d3_scaling.py`: exact idempotents via `P=ΛR`, `R = R_from_Lambda(Λ)` (min-norm
completion with `RΛ=I`, rows-sum-1). Headline = `max_i dist₁(pᵢ,conv W)/τ`, `τ=√(max-row-neg-mass)`.

**Structured families, ratio vs δ scaling** (`out/d3_scaling.json`, hardened LP):

| family | δ range swept | max ratio over the sweep |
|---|---|---|
| staircase heights `2⁻ᵐ·s` (r=4) | 1e-3 … 0.44 | ~1e-15 (machine zero) |
| circuit r=4, K=8 | 1e-3 … 0.54 | ~2e-15 |
| circuit r=6, K=12 | 2e-3 … 0.71 | ~3e-15 |

As `δ→0` the ratio stays at machine zero — **no growth**.

**Random hunt over exact idempotents** (1200 instances, r∈3..6, hardened LP), max ratio per δ-band:

| δ band | #instances | max ratio |
|---|---|---|
| ~0.4 | 196 | 0.021 |
| ~1e-1 | 478 | 0.114 |
| ~1e-2 | 412 | 0.0057 |
| ~1e-3 | 114 | 0.0089 |

**Aggressive small-δ hunt (2nd pass, robust margin-based exposedness).** An aggressive hunt
(`δ` pushed down to `1e-4..1e-5`, r=3..8, n up to 18) initially *appeared* to find counterexamples —
20 instances with reported `ratio = inf … 88`, all at `δ ∈ [1e-5,1e-3]`. **Every one was a
false-positive of the SAME degenerate class** (rank-3, three near-coincident row clusters forming a
triangle): the well-exposedness LP was failing on the duplicate noise rows. With the margin-based
robust exposedness test (below) **all 20 collapse to `ratio = 0.0000`** (the triangle vertices are
in fact strongly exposed, margin ≈ 1). Pinned in `test_lp_robustness.py`. Robust re-hunt (2000 exact idempotents, r=3..8, n up to 18; `out/d3_aggressive_robust.json`):
best finite `ratio = 0.086` (at `δ=0.21`, a LARGE δ), **0 instances above 0.5**, and the ratio
**decreases with δ**:

| δ band | max ratio |
|---|---|
| ~1e-3 | 0.00033 |
| ~1e-4 | 0.0000987 |

**Counterexample signature absent:** the ratio neither exceeds ~0.12 anywhere nor grows as `δ`
shrinks — it shrinks (`ratio = O(τ)` consistent with the prior `O(δ)` distance finding).

---

## The retracted "counterexample" (LEARNING — logged honestly)

A random instance produced `ratio = 69.0` at `δ = 8.40e-4` (an EXACT idempotent: idem residual
`1.1e-16`). Investigation (`spike_Lambda.npy`, saved):

- `P` is a near-stochastic idempotent with **3 clusters** of nearly-identical rows (a triangle),
  perturbed by `~3e-4` noise giving `δ=8.4e-4`. Affine dimension of the row set = `r−1 = 2` (PROVED).
- The hunt reported the third cluster's vertex (row 2) as **non-exposed**, dropping it from `W` and
  inflating the ratio. **This was wrong.** The default scipy `highs` (simplex) returned
  **status 4** ("numerical difficulties") on the badly-scaled near-coincident rows; the old code
  read `not success` as "non-exposed".
- `highs-ipm` (interior point) solves the *same* LP and finds the exposer (`margin 0.991`). Row 2 IS
  well-exposed. After the fix, `ratio = 0.0089`. **PROVED artifact, not a counterexample.**

A second, harder wave (the aggressive hunt) exposed that even a multi-solver fallback was not
enough: on the most degenerate near-duplicate clusters, **all** of `highs`, `highs-ds`, `highs-ipm`
returned status 4 *with presolve on*, and the fixed-κ feasibility LP is genuinely brittle there.

**Two-part fix in `d1_infra.py`:**
1. `robust_linprog` — tries `highs-ipm → highs → highs-ds`, trusts only `status==2` as genuine
   infeasibility (used by `is_row_vertex`, `dist1_to_conv`).
2. `exposed_margin` reformulated as **margin-maximizing** (compute
   `t* = max_h min_{k far} h(p_k)` s.t. `h(p_i)=0, 0≤h≤1`; row exposed `⇔ t* ≥ κ`), solved with
   **presolve OFF**. This turns a brittle feasible/infeasible flag into a robust numeric comparison
   and was the decisive fix (presolve was the actual culprit on duplicate rows).

Regression test `test_lp_robustness.py`: asserts (a) the spike's third-cluster vertex is exposed,
(b) the spike ratio < 0.5 (now 0.000), (c) `robust_linprog` solves where bare simplex fails, (d) the
3 worst aggressive-flagged artifacts (reported `inf`/`340`) collapse to `ratio ≈ 0`. **Red→green.**
Artifacts saved: `out/spike_Lambda.npy`, `out/flagged_artifacts.npy`.

---

## Files

- `experiments/d1_infra.py` — infrastructure (idempotence/δ/vertex/exposedness/dist LPs) + `robust_linprog`.
- `experiments/d1_validate.py`, `out/d1_validate.json` — Task-1 validation on knowns.
- `experiments/d2_coupling.py`, `d2_plateau.py`, `d2_direct.py`, `d2_fixR.py`, `d2_geom.py`, `d2_hide.py`
  + `out/d2_*.json` — Task-2 coupling analysis and the three obstructions.
- `experiments/d3_hunt.py`, `d3_scaling.py`, `out/d3_scaling.json`, `out/d3_scaling*.log`,
  `out/d3_aggressive.json` — Task-3 hunt and scaling tables.
- `experiments/out/spike_Lambda.npy` — the retracted `ratio=69` instance (kept for the regression test).
- `experiments/test_lp_robustness.py` — red→green regression for the false-negative exposedness bug.

## Honest caveats / open

- All ratio evidence is **NUMERICAL** (finite-precision LPs). The conjecture is **not proved**; what
  is proved here are the three structural *obstructions to the plateau mechanism* (negativity not
  forced by abstract signs; lone far rows self-expose; hiding costs `δ ≳ height²`) and the algebra
  of `P=ΛR, RΛ=I`.
- `R_from_Lambda` uses the **min-norm** `R` completion; a different (adversarial) `R` with the same
  `Λ` could in principle realize a worse geometry. Min-norm is a specific (favorable-to-prover)
  choice — searching over `R` completions is a follow-up, but note Obstruction #1 shows the `R`
  freedom tends to *reduce* `δ`, working against a counterexample.
- The universal constant `C′` is a GUESS; numerics put it `≲ 0.2`. n=4 rank-3 rigidity (known) is
  consistent: the (r−1)-flat is too small to hide a cluster.
