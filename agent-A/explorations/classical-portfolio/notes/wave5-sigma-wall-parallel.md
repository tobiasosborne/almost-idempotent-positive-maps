<!--
ROLE: incremental harvest of the wave-5 parallel σ_v-wall attack (8 codex provers, diverse
mandated strategies + 1 opus dual-certificate decider). Crash-safe: appended as results land.
Date: 2026-06-10/11. Orchestrator: Agent A (fable main loop).
Raw answers: /tmp/codex-sigma-wall/<worker>/answer.md (events.jsonl alongside).
-->

# Wave 5 — parallel σ_v-wall attack (harvest)

Fleet: codex A/A2/A3 (Branch A: general / LP-duality / spectral-kernel), codex B/B2/B3
(Branch B: general / explicit-functional / UNSTEERED CONTROL), codex ψ/ψ2 (prove-bias /
refute-bias), opus d9 (dual-certificate decider rerun → notes/d9-dual-certificates.md).

## Convergence table (filled as workers return)

| worker | verdict | died-at / key object | P(true) | P(survives audit) |
|---|---|---|---|---|
| A (general) | STUCK — reduced | supplier-deficit lower bound A_v ≥ c₀H_v²/σ_v² | 0.70 | 0.82 |
| A2 (LP dual) | DIED-AT | α-localization: C10 exchange Σμg+Σαg = Σβg ≤ κR available; α-carrier control needed | 0.75 | 0.10 (as proof) |
| A3 (spectral) | DIED-AT | point-energy Γ_v ≳ (H/σ_v)² needed; energy route caps at H ≲ √σ_v·τ (√σ_v short) | 0.72 | 0.80 (as diagnosis) |
| B (general) | STUCK — reduced | top-slab localization: ρ-far ⇒ g ≥ κD (T_far = ∅) | 0.78 | 0.85 |
| B2 (functional) | DIED-AT | top-band blocker bound: ρ-far ⇒ g ≥ κR; derives B_B ≈ 1/2 analytically (≈ measured 0.536) | 0.75 | 0.15 (as proof) |
| B3 (control) | DIED-AT | chose wall-functional route (= B2, convergent); NEW proved: large-σ sharp shadow + top-band concentration | 0.78 | 0.88 (as diagnosis) |
| ψ (prove) | REFUTED (literal stmt) | exact-rational cex: ψ trade x(S) vs λφ; gap 3s/16 < κZ = s/4 | 0.01 | 0.90 |
| ψ2 (refute) | AMBIGUOUS + cex | 2nd independent bare-lemma cex; its OWN cex dies under canonical-W ⇒ names the minimal fix | 0.55 (canonical variant) | — |

## codex A (Branch A, unsteered) — STUCK, valuable reduction

**Reduction.** With the distance separator φ (dual ℓ∞-norm ≤ 1, sup_{conv W} φ = 0,
φ(p_v) = H_v) and deficit g = H_v − φ(p) (so g ≥ 0 if v is a top vertex, g_v = 0, Pg = g):
Branch A follows with B_A = √(3/c₀) from ONE missing inequality, the
**supplier-deficit lower bound**:
  A_v := Σ_{s∈S_v} P⁺_{vs} g_s ≥ c₀ · H_v²/σ_v².
Available from the audited belt is only the OPPOSITE side (F-GB at g_v = 0): A_v ≤ δR ≤ 3δ.

**Stress test (important):** the audited inequalities ALONE permit the two-level evasion at
scaling τ=ε, δ=ε², σ_v=√ε, ℓ=ε^{3/2}, H_v=ε (F-GB exactly saturated, Branch A violated).
NOT a counterexample matrix — but it proves the belt is insufficient: any proof of Branch A
must extract MORE from exactness P²=P than F-GB/F-WR/F-BC currently encode. [codex,
unverified by second family yet]

**Hiddenness use:** non-exposedness of v gives only: some ρ-far row b has g_b < κR ≤ 3τ/4
(a blocker, not a contradiction). The v→v″ max-selection route needs the unproved ψ-gap.

**Cross-check hook for the d9 duals:** the missing inequality predicts that at the collapse
edge the binding structure should price the supplier deficits — check whether the d9 dual
multipliers on supplier rows scale like H²/σ_v² (would confirm A_v is the right object).

## codex B (Branch B, unsteered) — STUCK, valuable reduction

**Same frame as codex A** (independently chosen: distance dual φ, deficit g = H − φ(p), g_v = 0,
g = Pg, D = diam₁ ≤ 2+4δ — the two general provers CONVERGED on the deficit-function frame).

**Mechanism identified (the linear margin growth):** h = g/D is an admissible exposer with
h(v) = 0; if every ρ-far row has g ≥ κD then v is exposed with margin H/D — exposure at
H ≥ (1/2+δ)τ, matching the measured wall ≈ 0.536τ to first order. F-GB at g_v = 0 gives
P⁺_v({g ≥ κD}) ≤ δ/κ = 4τ, so for σ_v ≥ 1/2 at least σ_v − 4τ ≥ 1/2 − 4τ of v's external
mass is forced INTO the top slab {g < κD} — large external mass pulls suppliers near the top.

**Reduction (the missing inequality), top-slab localization:**
  T_far := { j : ‖p_j − p_v‖₁ ≥ ρ and g_j < κD } = ∅  (under σ_v ≥ 1/2, H > B_B τ).
Available: only mass accounting on T_far ∪ T_near with nothing separating far from ρ-near
exempt rows. This is EXACTLY the C10 α-mass crux in new clothes: the failed-exposedness dual
can park uncontrolled α on the high zero-face/top slab. F-WR/F-BC don't close it at σ_v = O(1)
(external-mass cost affordable).

**Stress note:** the crude vertical bound gives wall (κD)/τ = 0.57+ vs measured 0.5357 — a
pure-H/D proof overshoots; the true wall uses lateral cluster structure (the d8 edge instance
sits hidden at margin 0.9997κ just below the crude threshold).

**Sub-lemmas filed:** (1) top-slab localization [open]; (2) C10 α-control on the high zero-face
[open]; (3) strengthened ψ-gap would imply (1) but F-ψ as stated is not enough.

## Orchestrator synthesis after A + B (preliminary)

The two INDEPENDENT general provers converged on the same frame (top-vertex deficit g with
g = Pg, g_v = 0) and reduced both branches to dual localization statements about the same
geometry — who is allowed to sit in the top slab {g small} at distance ≥ ρ from v:
- Branch A residual: suppliers in the slab must CARRY deficit (A_v ≥ c₀H²/σ_v²).
- Branch B residual: ρ-far rows may NOT be in the slab at all (T_far = ∅).
Both are "the C10 α-mass control" in different quantifiers. The σ_v-wall lemma is therefore ONE
localization principle: **exactness P²=P forbids ρ-far rows from loitering in the top slab of
an invariant deficit function without paying ~H²-level negativity.** This is precisely what the
d9 dual certificates should display — the binding blockers at the collapse edge ARE the
would-be top-slab loiterers. [orchestrator synthesis, to verify against A2/A3/B2/B3 + d9]

## codex ψ (prove-bias) — REFUTED the ψ-gap lemma as literally recorded

**Counterexample family (exact-rational, every m ≥ 8):** s = 1/m, δ = s², a = 3s/8.
P = diag(B, H) (7×7): B = 4×4 stochastic idempotent with row 4 = (0, 1−a, a, 0);
H = I − uvᵀ, u = (1−s+s², −s, 0)ᵀ, v = (1, −1+s, −s)ᵀ (vᵀu = 1, vᵀ1 = 0 ⇒ H² = H, H1 = 1;
single negative entry −s² = −δ). With S = {1,2}, φ = x₃, ψ = x(S) + ½φ, v″ = p₁ (ψ-max, Z = 1),
q = p₄ = (0, 1−a, a, 0; 0,0,0): q is ρ-far (‖q−v″‖₁ = 2), non-S-full (1−a < 1−κ), but
ψ(v″) − ψ(q) = a/2 = 3s/16 < κZ = s/4. **The failure mode: the λφ term refunds part of the
lost S-mass.** [ORCHESTRATOR-VERIFIED: I re-derived H²=H, H1=1, neg = δ, row sums, the
ψ-arithmetic and the ρ-far/non-S-full gates by hand — all correct. Claude-family check of
codex algebra ⇒ 2-family on the arithmetic; the FORMALIZATION fidelity vs fable-hlc-attack.md
§ψ still rides on ψ2 + a planned opus read.]

**Scope honesty:** refutes the standalone uniform ψ-gap input ONLY. No hidden-top
configuration in the example — a conditioned variant (ψ-gap restricted to hidden-top
instances, or with the trade-correction inequality λ(φ(q)−φ(v″)) ≤ v″(S) − q(S) − κZ as the
target) is untouched. Branch B routes: avoid the v″ max-selection, or sharpen the lemma.
P(literal lemma true) ≈ 0.01; P(refutation survives audit) ≈ 0.90.

## opus d9 — dual-certificate decider rerun (COMPLETE, all 8 σ_v cells OPTIMAL)

Full table: experiments/out/d9_duals.json; blueprint: notes/d9-dual-certificates.md.
All cells gurobi OPTIMAL (presolve OFF, dual simplex, FeasTol=OptTol=1e-9), idem_resid = 0,
honest τ. [NUMERICAL]

**The blueprint findings:**
1. **ONE functional, both regimes.** The exposedness separating functional is the SAME object
   across the whole σ_v sweep: a level functional with anchors at h = 1, hidden v at h = 0,
   suppliers at h ≈ 0.66–0.74; only the achieved margin changes. ⇒ Branches A and B need one
   construction + one height bound, not two proofs.
2. **The binding blocker is the FINANCING row** (the direction paying for the apex poke;
   secondary: frame-group) — NOT the suppliers. Its height equals the margin t* and rises
   LINEARLY in σ_v: t*/κ = σ_v/0.5, saturating at κ exactly at σ_v = 0.5.
3. **Regime fingerprint:** just past the collapse edge, v enters W with post-edge margin
   2.00κ (budget regime) vs 1.00κ (wall regime) — corroborates the two-branch split.
4. **v″ blocks supplier exposedness** — the ψ-gap object appears with explicit multipliers
   (note: the LITERAL ψ-gap lemma is refuted, see above; the d9 multipliers show what the
   CONDITIONED variant must say).
5. (Λ,R) min-neg duals: only pin/neg/epi rows carry duals (RL/Lsum zero) — "R inert" confirmed
   from the dual side.

**Cross-check vs codex A's prediction:** A predicted supplier-row duals scaling like H²/σ_v²;
d9 shows the binding object is the FINANCING row's height, not supplier deficit mass. The
top-slab loiterer (B's T_far) is the financing direction. ⇒ the localization principle should
be aimed at FINANCING rows: exactness forces whoever finances the apex poke to sit at height
≥ t* ~ (H/τ)·κ/0.5; hiding requires t* < κ ⇒ H/τ < min(2σ_v·…, 0.536-ish). [synthesis hook
for the closer]

## codex A2 (Branch A, LP-duality angle) — DIED-AT α-localization

Granted top-vertex v: same deficit frame (g = Pg, g_v = 0). NEW exchange identity (clean and
reusable): pairing the C10 failed-exposedness dual witness (μ ∈ Prob(F), α,β ≥ 0, Σβ < κ,
Σ_F μ_j(p_j−v) = Σ_i(β_i−α_i)(p_i−v)) with φ gives
  **Σ_F μ_j g_j + Σ_i α_i g_i = Σ_i β_i g_i ≤ κR.**  [C10-exchange]
This controls heights in the single coordinate g but says NOTHING about α-mass/α-radius.
Needed (the死 point): α-carriers (or their absorbed μ-blockers) localized to an O(σ_v τ)-ball
of v or priced by σ_v. Key structural observation: exactness binds ROW COEFFICIENTS of P;
C10's α is a DUAL SLACK — nothing ties it to v's row. Any counterexample to Branch A must
park low-g far blockers / α-carriers on a high zero-face. P(route as proof) = 0.10.

## codex A3 (Branch A, spectral/kernel-energy angle) — DIED-AT point-energy; route PROVABLY capped

Two genuinely new facts:
- **Self-starvation lemma:** P⁺_vv ≥ 1 − σ_v − O(δ) ≥ 1/2 − O(δ), so if Γ^f_v ≥ E for any
  f = Pf then E ≲ δ·osc(f)² (F-E starvation at v itself).
- **Height-energy ANTI-lemma:** for the canonical deficit g, F-GB bounds the local positive
  quadratic energy: Σ_k P⁺_vk g_k² ≤ R·Σ_k P⁺_vk g_k ≤ δR². ⇒ THE CANONICAL-g ENERGY ROUTE
  CANNOT prove Branch A (its own bound evades F-E starvation).
Died-at: need a profile f = Pf, osc ≤ 1, with point-energy Γ^f_v ≳ (H/σ_v)²; the natural
variance heuristic gives only AVERAGED H²/σ_v ⇒ H ≲ √σ_v·τ — exactly a √σ_v factor short.
Learning: "the budget binds geometrically, not energetically."

## codex B2 (Branch B, explicit-functional angle) — DIED-AT; B_B ≈ 1/2 DERIVED

Same height-certificate h₀ = g/R. **Analytic origin of the measured constant:** margin of the
candidate exposer is ~H/R with R ≈ 2 (+H); requiring margin ≥ κ = τ/4 gives the wall at
H ≈ τ/2, i.e. **B_B ≈ 1/2 — matching the measured 0.536 to first order, now explained.**
Conditional lemma banked: [height-functional wall] if g_j ≥ κR for all ρ-far rows j, then v
is exposed once H > B_B τ, B_B ≳ 1/2. Supplier top-band lemma: σ_v ≥ 1/2 ⇒ at least σ_v − 4τ
of v's external mass lands in {g < κR}. Died-at: the same top-band blocker bound. Notes the
capped deficit max(g−cap, 0) is NOT affine ⇒ not an exposer (diagnostic only).

## codex B3 (Branch B, UNSTEERED CONTROL) — chose the same wall-functional route (convergence signal); 2 NEW proved facts

Strategy choice (independent): exposedness-LP dual / wall-functional — i.e., the control
landed on B2's mandated angle, strengthening confidence that this is THE natural route.
NEW proved facts (audit-grade candidates for the belt):
- **Large-σ sharp shadow:** σ_v ≥ 1/2 ⇒ dist₁(p_v, conv{p_j : j ≠ v}) ≤ (2+4δ)δ/(σ_v−δ) ≤ 12δ
  (δ ≤ 1/4). The hidden top vertex is ℓ¹-CLOSE to the hull of the other rows — its
  vertex-ness is δ-thin in the large-σ_v regime.
- **Top-band concentration:** ≥ 1/4 of v's off-site positive mass sits in {g ≤ 4δR}.
Died-at: the uniform wall-functional inequality t*_v ≥ κ (the exposedness LP value). Both
facts push the obstruction into a TINY top band; nothing yet forbids a ρ-far blocker there.

## codex ψ2 (refute-bias) — STATEMENT-AMBIGUOUS + second independent counterexample + THE MINIMAL FIX

- Formalization fidelity finding: fable-hlc-attack.md pins ψ = x(S) + λφ and S-full
  (x(S) ≥ 1−κ) but NOT Z, φ-admissibility, or whether q may lie in W (FA3-audit.md:11).
- Second bare-lemma counterexample (6×6, exact rationals, δ = 1/16): ψ-gap 3/32 < κZ = 33/256.
  INDEPENDENT of ψ's counterexample (different mechanism class, same λφ-refund loophole).
- **The gold nugget — its own counterexample self-destructs under the canonical-W reading:**
  the offending row q is itself well-exposed (explicit exposer h given, far-values ≥ 2/5 ≫ κ),
  so q ∈ W and φ = −2x₄ is not the canonical separator. ⇒ MINIMAL FIX identified: require
  (i) φ = the canonical normalized top separator AFTER computing W, and (ii) the high
  zero-face rows of that separator S-full. P(canonical conditioned F-ψ true) ≈ 0.55.

# GRAND SYNTHESIS (orchestrator, post-wave-5)

**1. Six independent provers, three disjoint proof technologies, ONE wall.** Every A/B worker
independently adopted the same deficit frame (g = H − φ(p), g = Pg, g_v = 0, F-GB top-band
accounting) and died at the SAME point. The σ_v-wall residual is now ONE precisely-specified
lemma:

> **TOP-BAND LOCALIZATION (the single remaining inequality).** Let v be a hidden top vertex
> with canonical separator φ and deficit g = H − φ(p). Then no row j with ‖p_j − p_v‖₁ ≥ ρ
> may satisfy g_j < κR — unless it (or the cluster) exposes, or pays ~H²-level negativity.
> Equivalently: C10's α-mass cannot sit on the ρ-far part of the high zero-face {g < κR}.

Branch A = this with the budget bookkeeping (then B_A = √(3/c₀) via codex-A's reduction);
Branch B = this directly (then B_B ≈ 1/2 via codex-B2's wall constant, matching measured
0.536). The d9 duals say the numerical occupant of the top band at the edge is the FINANCING
row, whose height obeys t*/κ = σ_v/0.5 — the linear law the lemma must reproduce.

**2. Routes now PROVABLY closed (do not re-walk):** canonical-g kernel-energy (A3's
anti-lemma: its own energy is ≤ δR², too small); pure-H/D vertical functional (B's stress
note: overshoots the wall); literal ψ-gap as input (refuted twice, independently).

**3. New belt candidates harvested (to audit + bank):** C10-exchange identity (A2);
self-starvation lemma (A3); large-σ sharp shadow — hidden top vertex is 12δ-close to the
other rows' hull (B3); top-band concentration (B3); supplier top-band lemma (B2);
height-functional wall lemma (B2, conditional); the two ψ counterexample families (ψ, ψ2);
the canonical-W conditioned F-ψ reformulation (ψ2).

**4. What the closer must do:** prove top-band localization using exactness BEYOND the belt
(the belt is provably insufficient — codex A's saturation stress test). The d9 blueprint
suggests the mechanism: whoever finances the apex poke must itself sit at height ≈ margin;
exactness P² = P applied to the financing row's own budget is the untapped constraint. The
large-σ sharp shadow (v is 12δ-close to conv of the others when σ_v ≥ 1/2) is brand-new
leverage for Branch B: v's separating data lives almost entirely in the other rows.

**5. Honest count:** 8/8 codex verdicts are STUCK/DIED-AT/REFUTED — no branch proved. The
deliverable of this wave is the compression 2 branches + 1 sub-residual → 1 named inequality
+ 1 refutation + ~6 new auditable belt facts + the analytic origin of both measured constants
(0.5 from B2's margin arithmetic; linear σ_v-law from d9 duals).

---

# WAVE 6 (post-synthesis, 4 codex on the sharpened residual)

| worker | verdict | key output | P(target true) |
|---|---|---|---|
| w6fin (financing route) | DIED-AT (same wall) | financing-row no-gain lemma: exactness at f alone is H- and σ_v-free | 0.65 (H²-form) / 0.35 (literal T_far=∅) |
| w6shadow (sharp shadow) | DIED-AT (sharper) | positive-carrier sharp shadow [proved]; residual = carrier-blocker COUPLING | 0.80 (Branch B) |
| w6psifix (conditioned F-ψ) | **PROVED (conditioned)** | the corrected F-ψ input, short clean proof, excludes both wave-5 cex, fits consumer | 0.99 (variant) |
| w6refute (refuter) | NOT-REFUTED | 6-template failure map; **reciprocal-carrier mechanism named**; floor 3.484 re-found independently | **0.83** (raised) |

## w6psifix — PROVED: the canonical-W conditioned ψ-gap (F-ψ replacement)

Statement (self-contained in /tmp/codex-sigma-wall/w6psifix/answer.md, to be banked): with φ
the CANONICAL top separator (sup_{conv W} φ = 0, φ(p_v) = H, dual-norm ≤ 1), ψ = x(S) + φ/2,
v″ the ψ-max row vertex with s_{v″} ≥ 1−κ, and the high-danger band
𝒵_hi = {i : ρ-far from v″, g_i ≤ g_{v″} + 2κZ}: IF every row of 𝒵_hi is S-full, THEN every
ρ-far non-S-full q has ψ-gap ≥ κZ. Plus the height bound g_{v″} ≤ 2σ_v + 2δ (clean 4-line
proofs). Explicit exclusion checks on BOTH wave-5 counterexamples (each had a non-canonical φ:
sup_C φ = 0 violated). Consumer fit verified against fable-hlc-attack.md:479 with O(δ) = 2δ.
HONEST: the 𝒵_hi/S-full condition is itself ~top-band localization — this lemma RE-ROUTES
F-ψ through the single residual rather than adding a second one. [codex, P=0.99/0.82 —
needs Claude-family audit before banking]

## w6fin — financing route dies at the SAME wall; useful no-gain lemma

Exactness applied to the financier f's own row gives only Σ_k P⁺_fk g_k ≤ g_f + δR — an
inequality containing NEITHER H nor σ_v ⇒ cannot by itself give A_v ≥ cH²/σ_v² or T_far = ∅.
[financing-row no-gain lemma, proved]. Also: positive-support shadow (recovers B3's shadow
via the row identity). NOTE the calibration split: P(H²-qualified form) = 0.65 vs P(literal
T_far = ∅) = 0.35 — the literal form may be FALSE while the qualified form holds; the closer
should target the qualified form. Concrete closer suggestion: JOINT LP certificate search
(variables P, g, φ, C10 witness; objective max far top-band α-mass s.t. P² = P) → extract the
rational dual = the missing inequality. [→ d10 decider]

## w6shadow — carrier-blocker coupling is the sharpened residual

NEW proved (strengthens B3): **positive-carrier sharp shadow** — v's positive off-site
carrier measure q_v = (1/σ)Σ_A P_vj p_j satisfies ‖q_v − p_v‖₁ ≤ (2+4δ)ν/σ ≤ 2(2+4δ)δ AND
mean deficit (1/σ)Σ_A P_vj g_j ≤ δR/σ ≤ 2δR; carrier mass in {g ≥ κR} ≤ 8τ. Carrier
dichotomy: either a positive fraction of carriers are ρ-far top-band rows, or v has an
O(δ+τ) shadow inside its ρ-ball (the exemption case, needs a cluster-exposure lemma).
Death point — the COUPLING inequality: nothing forces the C10 dual blocker (a far top-band
row) to RECEIVE mass from v's carrier system. Suggestion: apply P² = P to the BLOCKER row,
not to v. [consistent with w6fin's death + w6refute's mechanism]

## w6refute — NOT-REFUTED after 6 adversarial templates; THE mechanism named

Templates → kills: belt-insufficiency scaling realizations collapse to the wall (financier
height pinned at g = H); optimized financed-wiggle grid best 3.571, refined known cell 3.484
(re-found INDEPENDENTLY, scipy reimplementation — cross-validates d8/d9 without gurobi);
multi-group financing duplicates the blocker, doesn't lower the wall; canonical frame killed
HARDER (dist ≤ 2·neg, linear); staircase dies by X1; 1220 random exact projections best 176.
**Sharpest insight (the analytic seed for the closer):** "The belt lets the financier be a
free low-g far row. Exactness does not. RΛ = I turns the financier into a biorthogonal
carrier, and its canonical height is forced up to the wall. Every attempt to make that row
hidden recursively creates the same reciprocal-carrier obstruction." P(localization true)
raised to 0.83.

# POST-WAVE-6 STATE

The single residual, now in its sharpest form (three independent formulations that coincide):
> **Carrier-blocker coupling / reciprocal-carrier lemma.** Apply exactness to the BLOCKER
> (financier) row: since P = ΛR with RΛ = I (any rank factorization of an exact idempotent),
> the financier is a biorthogonal carrier of v's representation; prove its canonical height
> g_f is forced ≥ ~κR (equivalently: a C10 far top-band blocker must receive carrier mass).
The proof must use the BIORTHOGONALITY (column/dual-frame structure), not row budgets alone
(w6fin's no-gain lemma shows row-side exactness at f is insufficient).

Status of the chain: σ_v-wall ⟸ top-band localization (H²-qualified form, P ≈ 0.65–0.83)
⟸ carrier-blocker coupling. F-ψ correctly re-routed (w6psifix, conditioned, PROVED mod
audit). Next: d10 joint-LP dual mining (w6fin's recipe) + provers on the reciprocal-carrier
lemma; then the fable closer decision.

---

# WAVE 7 (2 codex: reciprocal-carrier via RΛ=I; carrier-blocker coupling via C10)

| worker | verdict | key output | P |
|---|---|---|---|
| w7carrier | DIED-AT (same wall, sharpened) | column-carrier propagation [proved]; GAUGE WARNING; binding-height = LP complementarity (demystified) | 0.72 quantitative / 0.40 literal |
| w7coupling | DIED-AT (same wall, sharpened) | column-shadow lemma [proved]; coupling ⟸ aggregate pinning Σ_b μ_b P_vb ≥ cτ | 0.65 aggregate form |

**w7carrier:** column idempotence at f: P_vf = Σ_k P_vk P_kf gives [column-carrier
propagation] Σ_{k∈A} P_vk P⁺_kf ≥ m − δ² for direct carrier mass m = P_vf — propagation is
proportional to the OVERLAP m; nothing forces m large ⇒ no H, no σ_v. **Gauge warning
(important for all future provers):** raw-Λ-row arguments are not invariant under Λ → ΛS,
R → S⁻¹R; the invariant content of the factorization is exactly row exactness g = Pg +
column exactness P² = P — "RΛ = I" per se adds nothing beyond these. **Binding-height
identity demystified:** d9's "height = margin" is exposedness-LP complementary slackness
(active far-row constraint ⇒ h(f) = t*), NOT a hidden exactness identity. So the
reciprocal-carrier "mechanism" needs a QUANTITATIVE carrier-overlap lower bound, which is
the open content.

**w7coupling:** [column-shadow lemma] v's carrier system reproduces every column of p_v to
O(δ/σ_v): Σ_{j∈A_v} λ_j P_jb = P_vb + O(δ/σ_v). [coupling reduction] carrier-blocker
coupling ⟸ the aggregate pinning inequality **Σ_{b∈B} μ_b P_vb ≥ cτ** (μ = the C10 witness
measure on far blockers). C10-exchange controls only HEIGHT; α still carries all the
radius/column information (same uncontrolled high-zero-face term).

**CONVERGENT NEXT EXPERIMENT (both workers, independently, = w6fin's recipe refined):**
joint LP/alternating search under exact P² = P + C10 witness + σ_v ≥ 1/2 + far top-band
blocker constraints, with objective MINIMIZING the aggregate coupling
M := Σ_b μ_b Σ_{j∈A_v} λ_j P⁺_jb (equivalently sweep a floor θ₀ on the carrier-overlap
θ_f and watch when the 3.48 wall appears). **Decision value: optimum M = 0 ⇒ the coupling
lemma is FALSE as stated (counterexample direction); M ≥ cτ ⇒ extract the rational dual =
the missing proof certificate.** d10 (running) covers the neighbourhood of this; a d11
with the M-objective directly is queued if d10 doesn't settle it.

---

# d10 — certificate mining (COMPLETE, clean) + AN ORCHESTRATOR CATCH

Report: notes/d10-certificate-mining.md; data: out/d10_certmine.json (16 PROBE-1 + 3 PROBE-2
cells, all verified, gurobi OPTIMAL throughout, zero anomalies).

**PROBE 1 [NUMERICAL]:** far top-band positive feed M_far stays BOUNDED (≈ 2.0–2.14,
σ_v-independent, ≈ 2 + 0.27·H/τ) as H → wall; 1-step and 2-step feeds EQUAL to machine
precision. ⇒ literal T_far = ∅ is FALSE (the far top band is robustly occupied at bounded
mass); the H²-qualified form is the right target — confirms w6fin's 0.65/0.35 split.

**PROBE 2 [NUMERICAL, the headline]:** at every probed collapse edge the binding financier
is the SAME row; the forced-height cost curve is EXACTLY linear with universal slope:
**δ_min = ½·g_f, intercept 0, R² = 1.000, σ_v-independent**; and at the natural edge
g_f = H to all digits. Conjectured shape: "forcing the biorthogonal financier to height t
costs negativity t/2"; the δ/H² → 3.49 wall is a SEPARATE exposedness saturation
(margin/κ → 1.000 at H/τ = 0.53). Supports the two-branch split: linear financier law
(Branch A side) + exposedness wall (Branch B side).

**⚠ ORCHESTRATOR CATCH — scale degeneracy in "g_f = H" [must resolve before the closer]:**
PROBE 2 ran only at the default family scale, where the collapse edge sits at δ ≈ 0.0718 —
and there H = 2δ EXACTLY (the d8 floor identity δ/H² = 1/(4d)). So the measurements
"g_f = H" and "g_f = 2δ" are INDISTINGUISHABLE at the probed scale. The two readings have
wildly different consequences:
- If g_f ≈ H persists across δ scales: δ ≥ H/2 for hidden tops — but this CONTRADICTS the
  established d3/d7/d8 record (flat floor δ/H² ≈ 3.49 as δ → 0 means instances exist with
  H ≈ 0.536√δ ≫ 2δ at small δ). So this reading is almost certainly WRONG at small δ.
- If g_f ≈ 2δ (financier sits at height ~2δ, deep inside the top band at small δ): the law
  δ_min = g_f/2 is the TAUTOLOGY-like budget identity "financier height = 2·negativity",
  consistent with the H² envelope, and the real question becomes why the EDGE forces
  g_f up to ~H (i.e., why hiding pushes the financier to the band edge ONLY near the wall).
⇒ d11 MUST sweep PROBE 2 across δ scales (≥ 2 decades) tracking g_f vs H vs 2δ separately,
plus run the w7 M-minimization. Without this, the "linear law" risks being a confident,
plausible, WRONG claim — the exact failure mode this project guards against.
