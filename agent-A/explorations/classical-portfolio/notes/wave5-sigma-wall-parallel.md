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

---

# d11 — scale disambiguation + M-minimization (COMPLETE; 9/9 cells verified)

Report: notes/d11-scale-disambiguation.md; data: out/d11_scalesweep.json.

**TASK A (the degeneracy resolved):** the d8 family RIGIDLY lives on the budget line
g_f = H = 2δ — all three ratios 1.0000 to all digits across 7 verified collapse edges
spanning δ ∈ [0.00063, 0.0718] (2.06 decades); slope ½ and R² = 1.0000 at EVERY scale. No
crossover exists; the orchestrator's contradiction worry is vacuous for THIS family (it
never populates the flat floor — δ/H² = 1/(4δ) → ∞ along the budget line; the flat-floor
instances live in the d3/d7 stacking constructions). Sharpened statement: **g_f = H is a
financier/separator identity (the biorthogonal apex financier's canonical deficit equals the
full separation); δ = g_f/2 is the budget shadow price.** Resolving column: g_f/(κ·osc)
climbs 0.10 → 1.000, hitting EXACTLY 1 at the wall edge — the financier reaches the
top-band threshold precisely at the exposedness wall. [NUMERICAL, scale-swept]

**TASK B (the decisive LP): min M ≥ c·τ — the coupling lemma is NOT refuted, and the
certificate is in hand.** M/τ = 1.075 (wall, σ_v = 0.5), 3.02 (σ_v = 0.3); realization
freedom only RAISES it (the edge binds), c ≈ 1.07 at the wall. **76–94% of M is the
financier's SELF-coupling: the binding term is μ_f·λ_f·P⁺_ff — the financier is
simultaneously v's top carrier (λ_f) and the top C10 blocker (μ_f).** The reciprocal-carrier
mechanism is now measured, not just named. [NUMERICAL]

**The proof target in its final form (for the closer):** prove from exactness that the
binding far top-band blocker's self-coupling μ_f λ_f P⁺_ff ≳ τ (column exactness at the
DIAGONAL: P_ff = Σ_k P_fk P_kf is the natural untapped identity), then chain:
self-coupling ⇒ financier cannot sit low (budget shadow price δ = g_f/2 side) ⇒ hiding
caps H at the wall. All scaffolding (C10-exchange, column-shadow, carrier propagation,
conditioned F-ψ, large-σ shadow, height-functional wall) is proved and audited.

---

# WAVE 8 — fable closer + 2-family audits + DMF descent attack

Closer deliverable: **notes/wave8-fable-closer.md** (641 lines; the full state). Headlines:
corner theorem (exact constants τ* = 2−√3, wall 2(2−√3), floor (7+4√3)/4); d11
reciprocal-carrier demystified (witness = v's own row identity, verified 1e−16); 9 new
lemmas; residual compressed to **DMF** (optimal witnesses carry m* mass at deficit
≥ H − O(δ/τ)) ⇒ HLC with a → 4m*²; σ̃-vs-σ_v catch (N3). Verifier:
experiments/w8_witness_check.py (independently reproduces d11's M/τ = 1.0754).

## Audit 1 (codex, hostile derive-first on the 9 lemmas)
4 SOUND (W2 exchange, RW, plus dual-core of §1.1, WL-statement), 5 SOUND-WITH-FIX, 1 BROKEN:
- **NG′ DOWNGRADED** from proved lemma to analysis/dead-end guidance (its "consistency at
  any H" claim was template/numerics-supported, not derived) — keep only its algebraic
  identities.
- Fixes to apply before banking: ND′ threshold is t₀/τ = 7/4 − 2τ − δ/2 (the advertised
  "≥ 1.7τ for δ ≤ 0.05" is FALSE — it is ≈ 1.278τ at δ = 0.05); RF needs the hypothesis
  P_vv ≥ 0 (else ν_v includes the self-entry) and its 3.1δ constant re-proved; CPL wording
  split on sign(P_vv); WL gets a cleaner direct exposer proof (κΣ_far P⁺_wk ≤ ν_w);
  EVERY α-localization use carries the t* > 0 hypothesis (t* = 0 admits far α).
P(suite survives af-formalization): 0.45 as written, **0.78 with fixes + NG′ downgraded**.

## Audit 2 (codex, corner forms + 3.2′ chain)
- **Corner closed forms CONFIRMED by independent derivation** (τ²−4τ+1 > 0 ⇔ τ < 2−√3;
  all five numbers re-derived; d9 bracket check passes; raw-κ vs κR normalization verified
  against d1_infra). Now 2-family. P(exactly right) = 0.90.
- Sharp exchange ≤ t*R: CONFIRMED.
- **3.2′ chain: SOUND asymptotically AFTER a fix, BROKEN as finite-corner calibration.**
  The R-handling bug: R ≤ 2+4δ universally (g_i ≤ diam; the closer's R = 2+4δ+H is wrong
  as a universal bound — it is the FAMILY identity R = 2+H that recovers the corner value).
  Corrected chain (CLEANER): m*(H − C_Dδ/τ) ≤ t*R < κR ≤ (τ/4)(2+4δ) ⇒
  H ≤ τ[(2+4δ)/(4m*) + C_Dτ] ⇒ **δ ≥ aH², a → 4m*²; B_B → 1/2 asymptotically** (the 0.536
  is the finite-corner value, exact AT the corner only). RETRACT the closer's "DMF(m*=1)
  reproduces the entire measured envelope" finite-δ calibration (its finite formula
  evaluates to 2.36, not 3.4). P(corrected chain survives af): 0.80.

## DMF descent attack (codex w8dmf) — DIED-AT hidden-vertex recursion; minimal obstruction found
- VALID: non-vertex Krein–Milman descent (face dimension strictly drops, stays in
  F_v ∩ T_E); W-rows are automatically DEEP (g_w ≥ H — confirmed); the δ = 0 Baake–Sumner
  anchor (byte-pinned: equal-fin.tex:1060 normal form kills the shallow web exactly).
- INVALID: recursing through a hidden vertex's own witness — (♦) solved for p_x is SIGNED
  (the −β term); no preserved probability measure; no decreasing invariant.
- **Minimal obstruction (the irreducible object): a 2-cycle of shallow hidden vertices
  a → b → a, each all-shallow-witnessed by the other.** Every candidate decreasing quantity
  stalls on it. Baake–Sumner forbids it at δ = 0; the missing theorem is its quantitative
  δ > 0 exclusion.
- Reduction banked: **DMF ⟸ "every closed class in the shallow hidden-witness graph has
  universal escape mass to the deep set"** — i.e. exactly quantitative Baake–Sumner
  stability. P(DMF as stated) ≈ 0.55; P(pruned/extreme-witness weakening) ≈ 0.70.

## POST-WAVE-8 STATE (the campaign's terminal form)
HLC ⟸ DMF (corrected 3-line chain, 2-family-audited, a → 4m*²) ⟸ quantitative
Baake–Sumner stability of the shallow hidden-witness graph (the 2-cycle exclusion).
In flight: opus d12 witness-depth probe on d3/d7 stacking instances — directly searches
for shallow hidden webs in verified instances; either supports DMF (m* large observed
off-family) or finds the refutation candidate.

---

# d12 — DMF off-family probe (COMPLETE): SUPPORTED, m* = 1 exactly; σ̃ finding decisive

Report: notes/d12-dmf-depth-profiles.md; data: out/d12_dmfprobe.json. 12 verified
hidden-top instances OFF the wall edge (varied σ_v/ℓ/ma/k_groups; δ/H² ∈ [3.57, 35.7]
covering the floor region + mid-envelope). All gates green (residuals ≤ 3e-16, presolve
OFF, multiplicity-correct W). [NUMERICAL]

- **min m*_observed = 1.0 to machine precision (median 1.0); shallow fraction 0.0000
  everywhere; every μ-row at deficit g = H exactly.** DMF exactly saturated off-family,
  identical to the edge; the wave-8 row-witness mechanism (μ = γP⁺_v on W-vertices,
  exchange saturated Σμg = t*R) reproduces verbatim.
- **N3 resolved (decisive):** every instance has formal σ_v ≈ 1.01–1.07 but **σ̃ = 0
  exactly** (v's positive mass outside conv W is ZERO — v's positive carriers ARE
  W-vertices; hiddenness comes from negativity alone, the corner mechanism). ⇒ all
  σ_v-resolved statements must be restated in σ̃. **The all-shallow witness requires
  σ̃ > 0 — never realized in ANY reachable verified instance.**
- The FTI-2 distinct-vertex mutual-shadow construction (the only named home of the
  all-shallow web) could not be verified at small δ — alternating-LP search yields only
  degenerate instances, re-confirming d7's verdict that distinct far vertices always
  expose. The all-shallow detector was red→green tested; the negative is trustworthy.

## POST-d12 SHARPENING (orchestrator)
The chain in 3.2′ needs only EXISTENTIAL DMF (one optimal witness with deep mass m* —
the exchange Σμg + Σαg = Σβg ≤ t*R holds for every optimal witness, and the lower bound
m*(H−E) ≤ Σμg needs just one deep witness). Existential DMF ⟸:
 (i) σ̃-small case: if σ̃ ≈ 0, the RW row-witness is deep by construction (carriers in
     conv W are deep: g_w ≥ H) — candidate lemma "σ̃ ≤ s ⇒ ∃ optimal witness with deep
     mass ≥ 1 − f(s)";
 (ii) σ̃-large case: v draws positive mass onto non-W top-band rows = the mutual-shadow
     web = exactly what d7/X1 say exposes — candidate lemma "ρ-separated hidden top-band
     vertices cannot mutually carry each other" (the 2-cycle exclusion, now with a σ̃
     dichotomy to attack it through).
Wave 9 targets: (a) verify existential-DMF suffices in the corrected 3.2′ chain (logic
check); (b) prove (i); (c) attack (ii) via L1/L2/F-ND/X1 + the corner mechanism.

---

# WAVE 9+ — results (rolling)

## w9chain (codex): EXISTENTIAL-SUFFICIENT CONFIRMED + final clean theorem [P(af) = 0.92]
- The chain needs ONE optimal witness with deep mass (the exchange Σμg ≤ Σβg ≤ t*R holds
  for every optimal witness; only the lower bound m*(H−E) ≤ Σμg uses the deep one).
- **Final theorem (conditional on existential DMF):** H ≤ τ(2+4δ)/(4m*) + E(δ), hence
  δ ≥ aH² with **a = (1/(2m*) + e)⁻² where e = lim E(δ)/τ** — REFINEMENT vs fable: only
  E = o(τ) gives a → 4m*²; E = C_D·δ/τ = C_D·τ gives a = (1/(2m*) + C_D)⁻². The deep-band
  width matters at first order; provers of DMF should minimize E, not just m*.
- **t* = 0 case CLOSED:** exchange gives Σμg ≤ 0, so DMF forces H ≤ E — the chain survives
  with NO α-localization needed (removes the standing t* > 0 caveat from the CHAIN; it
  still rides on the σ̃-small branch's tools).
- Top-vertex WLOG settled: pick a height-maximizing row vertex; it is hidden if H > 0 and
  g ≥ 0 holds for it (non-top v is NOT WLOG — g ≥ 0 can fail; HLC only needs the top one).
- W-rows-deep one-liner recorded (φ(p_w) ≤ 0 ⇒ g_w ≥ H).

## w9deep (codex): σ̃-small branch PROVED — by HEIGHT COLLAPSE [orchestrator-verified]
**Lemma (σ̃-height-collapse):** hidden top vertex v with σ̃_v ≤ s < 1 ⇒ H ≤ δR/(1−s).
Proof (4 lines, verified by orchestrator): 0 = g_v = Σ_k P_vk g_k; positive part
Σ(P_vk)₊g_k = Σ(−P_vk)₊g_k ≤ ν_vR ≤ δR; conv-W rows are deep (g ≥ H) and carry positive
mass M_C = 1 + ν_v − σ̃_v; so (1+ν−σ̃)H ≤ δR. Sub-lemmas banked: top-separator-nonnegative
(g_i ≥ 0 for ALL rows when v is the height-max vertex); optimal-witness-vacuous-depth.
With m(s) = 1, E_s = δR/(1−s): in this branch EVERY optimal witness is (vacuously) deep.
σ̃ convention pinned: includes the self-row if p_v ∉ conv W and P_vv > 0.

## w9cycle (codex): PARTIAL — 3 new exclusion sub-lemmas; skinny regime survives
[direct-two-site] P_ab, P_ba ≥ c ⇒ c² ≤ 1/4 + 2δ(1+δ) (diagonal exactness at a) — direct
mutual carrying with coefficient > 1/2 + O(δ) impossible. [disjoint-two-ball] return mass
ε ≥ mn − mr − O(δ) — closed disjoint order-one 2-block cycles impossible. [non-skinny
payment] μν ≤ 1−θ ⇒ δ ≥ (θ²/64)H². Survivor: the SKINNY spread-mass regime
(μν = 1 − O(ρ/H), mass spread across the partner's ρ-ball). P(full exclusion from banked
tools) = 0.20 — quantitative B–S stability still the named missing input.

# ⚠ ORCHESTRATOR SYNTHESIS post-w9deep — d12's conclusion DOWNGRADED; the regime map redrawn
The CONTRAPOSITIVE of σ̃-height-collapse: **M_C ≤ δR/H, i.e. σ̃_v ≥ 1 − δR/H ALWAYS.**
Consequences (each verified by direct computation):
1. d12's σ̃ = 0 measurement is a CORNER-SCALE ARTIFACT: at H ≈ 2δ, δR/H ≥ 1 and the bound
   is vacuous — σ̃ = 0 is possible there and only there. d12's "DMF SUPPORTED" verdict is
   hereby DOWNGRADED to corner-regime-only; the "all-shallow web requires σ̃ > 0, never
   realized" framing was sound for the instances probed but says NOTHING about small δ.
2. At small δ (H ~ τ/2 ≫ δ): σ̃ → 1 PROVABLY — every hidden top vertex is a web; v's
   positive carriers are (almost all) outside conv W and SHALLOW-leaning (v's deep-mass
   ≤ δR/H → 0). The corner witness mechanism (μ = γP⁺_v on W-vertices) CANNOT operate
   there: a deep optimal witness, if it exists, is a structurally different object.
3. THE DECISIVE UNMEASURED DATUM: no verified small-δ floor instance (d3/d7 stacking,
   H ≈ 0.536√δ) has ever had its witness depth-profiled — d12's generator degenerated
   before that regime. If those instances verify and their witnesses are deep ⇒ DMF stands
   with an unknown mechanism to find; if shallow ⇒ DMF refuted, recalibrate (m*, E);
   if the instances themselves fail verification at small δ ⇒ the flat floor is itself a
   corner extrapolation and the true small-δ law may be LINEAR (δ ≥ cH — stronger than
   HLC). All three outcomes are major. → d13.
4. The HLC chain simplifies regardless: for the height-max vertex, EITHER σ̃ ≤ s (then
   δ ≥ (1−s)H/R — LINEAR, better than needed) OR σ̃ > s (the web case = the only
   remaining battlefield, now by PROOF not heuristic).

---

# sw10/sw11/sw12 — the analytic triangulators: THE FLAT FLOOR WAS NEVER REAL

## sw12 (d3/d7 forensics) — the record audited, with receipts
- **No saved d3/d7 entry verifies the flat floor below δ ≈ 0.06.** d3_clean_scaling.npy:
  max H/τ = 0.5356 at δ = 0.0829 (corner); floor-like rows (H/τ ≥ 0.5) bottom out at
  δ = 0.0625; the best δ < 0.01 entry has H/τ = 0.197 ≈ budget-line. d7_hunt entries are
  ring-shell deep-collapse (δ/H² ≥ 303) — not floor instances. d12's smallest passing row:
  H = 2δ, δ/H² = 35.7.
- **[σ̃-zero floor exclusion, proved]:** σ̃ = 0 ⇒ H ≤ δR (height collapse) ⇒ a flat floor
  H ≈ 0.536√δ requires δ ≳ 0.0718 = the corner. It CANNOT persist to small δ with the
  measured (σ̃ = 0) mechanism.
- Hand-derived the corner separator (φ = −2x₀ negative-anchor form, g = 2δ + 2x₀): the
  RW witness is deep with m* = 1 — predicts d13 outcome (c) + deep witnesses on whatever
  collapsed instances it profiles. P(forensic prediction survives) = 0.84.

## sw11 (linear law) — DIED-AT the web exclusion, but with the record correction
Cross-checked d13's IN-PROGRESS output (d13_smalldelta.json): verified small-δ search
collapses to **H/τ = 0.2000, 0.1095, 0.0632, 0.0346 at δ targets 1e-2 … 3e-4 — exactly
H ≈ 2δ**, not c√δ; the "all-shallow" artifacts in d13_logs have δ = 10.5, 6.9 (INVALID,
not small-δ evidence). Died at: the web-exclusion inequality M_C ≥ c₀ (= excluding σ̃→1
webs) — same nucleus. P(existential DMF) = 0.62.

## sw10 (web anatomy) — the surviving blueprint, sharply drawn
New proved bits: sigma-web balance; corrected carrier shadow (it is BARYCENTRIC only —
"σ̃ ≈ 1 web" does NOT mean visible clustering; the real failure mode is a facial-angle
failure: top-band non-W rows averaging back near v while avoiding W); shallow recursion
(shallow carriers finance from shallow non-W rows: the web is self-similar); multiplicity
convention (duplicates cannot fake non-vertexhood); F-ND forces every web node to have
nontrivial off-own-site spread; the cycle caps (direct ≤ 1/2, disjoint-balls, non-skinny
pays) force any closed shallow class to be SKINNY (μν = 1 − o(1)) and spread. **Missing
lemma named: a uniform facial/exposedness modulus for hidden top-band webs.**

# ORCHESTRATOR SYNTHESIS #2 (post sw10/11/12): THE LINEAR LAW IS THE TRUE TARGET
The ENTIRE verified record — every scale, every family, 67k+ instances + d12 + d13-partial
— satisfies **H ≤ ~2δ** (the budget line). The "wall H/τ = 0.536" and "floor δ/H² = 3.48"
are the linear law re-expressed AT the corner (2δ = 0.536τ ⟺ δ = δ*). The √δ-scaling
was never observed at small δ; it was conjectured from corner data. Consequences:
1. **The true conjecture is the LINEAR LAW (= X3's hull-distance half, day-1!):** every
   exact signed affine retraction has every row within Cδ of conv W (numerics: C ≈ 2).
   LINEAR ⇒ existential DMF (vacuous depth) ⇒ HLC with room to spare.
2. The σ_v-wall/HLC's √δ-form was always SAFE but the campaign was trying to prove a
   statement weaker than the truth while calibrating against corner-only data.
3. The single open is UNCHANGED in identity but upgraded in prize: exclude σ̃ → 1 shallow
   webs (uniform facial modulus / quantitative B–S stability). If excluded ⇒ LINEAR law
   ⇒ everything. If a web exists ⇒ it is the first H ≫ δ instance ever seen and the real
   geometry of the problem.
4. d13's final verdict (outcome (c) expected) is the remaining empirical confirmation.

---

# THE 9-AGENT DMF SWARM (s1–s9) — full verdicts in notes/swarm-answers/ (all 32 campaign
# answers archived there)

| agent | verdict | death point / key yield |
|---|---|---|
| s1 LP-face | DIED-AT | basicness gives only support ≤ d+1 — no depth control |
| s2 σ̃-bound | DIED-AT | σ̃ = O(δ/τ) NOT provable — "exact identities give the opposite pressure" (consistent with s5!) |
| s3 block-stability | DIED-AT | the leakage estimate ‖B²−B‖ = O(δ/κR) for the top-band block is not derivable from the belt |
| s4 closed-class | DIED-AT | μ-to-P closure / α-slack inequality |
| s5 REFUTER | **PARTIAL — exact all-shallow face CONSTRUCTED** | see below |
| s6 compactness | DIED-AT | the scale-collapse inequality (W jumps in limits) |
| s7 trace/spectral | DIED-AT | boundary-product bound |
| s8 control | **PARTIAL — σ̃ ≤ τ branch PROVED** | see below |
| s9 meta-auditor | PARTIAL | framing corrections + the gap list — see below |

## s5 — ALL-SHALLOW OPTIMAL FACES EXIST (exact 5×5 rational certificate)
P = ΛR (RΛ = I, P² = P exact), δ = 1841/1600000, W = {0,1,2}, hidden vertices 3,4 with
σ̃ = 1/2000 > 0; for v = 3: H = 1/1000, the far shallow row 4 (g₄ = 0) carries the ENTIRE
optimal witness (μ = δ₄ forced by complementary slackness; exact primal/dual certificates,
t* = 1/200 < κ). **BUT the family lives on H = O(δ) (H/τ ≈ 0.03), and its scaling keeps
H/τ → 0** — so DMF-with-E-slack survives vacuously. THE LESSON: all-shallow faces are real
once σ̃ > 0; existence is NOT the obstruction — HEIGHT is. Any final statement must exclude
shallow webs only at height ~τ, not absolutely. [exact-rational, P(survives audit) = 0.88]

## s8 — the σ̃ ≤ τ branch of DMF is PROVED (explicit constants)
[σ̃ height cap] H ≤ 2(1+2δ)·max(σ̃_v, neg(p_v)) (barycenter split; cleaner than w9deep's
collapse). ⇒ σ̃ ≤ τ, δ ≤ 1/4 ⇒ H ≤ 3τ ⇒ (with C_D = 3) the DMF threshold is ≤ 0 and EVERY
witness is deep: **existential DMF holds on the σ̃ ≤ τ branch with m* = 1, C_D = 3.**
NOTE (orchestrator): this branch gives HLC DIRECTLY (H ≤ 3τ ⇒ δ ≥ H²/9) with no witness
machinery at all. [pushed-witness death certificate] LP support-cleanup can NEVER finish
the other branch: pushing shallow witness rows through P costs (B+N)/M_F with M_F ≤ 1+N,
so optimality needs M_F ≥ 1 + N/B — impossible for any negative leakage N > 0 (B < κ < 1).
"The remaining problem is genuinely quantitative B–S stability for a SIGNED shallow web,
not another exposedness-dual algebra trick."

## s9 — meta-audit: framing corrections (adopt these conventions)
- **Canonical σ̃ = geometric + halo:** σ̃_x(ε) = positive mass on rows with dist₁ to
  C_W > ε; halo rows are automatically (H−ε)-deep (φ ≤ ε) — halo ambiguity becomes depth
  slack. d12 measured INDEX-not-in-W, not the geometric test (still strong for those
  instances; convention change required going forward).
- Existential sufficiency independently re-derived (matches w9chain; a = (C_D + 1/(2m*))⁻²).
- **The feasible-vs-optimal gap:** the exchange bounds a FEASIBLE witness by its own B·R,
  not t*R — RW-deep helps only if B_RW < κ is also proved. (w9deep's height-collapse branch
  is unaffected — it never used RW.) Gap list recorded for the next wave.

# GRAND STATE after the swarm (the campaign's sharpest-ever form)
**HLC ⟺ excluding hidden top vertices with σ̃ > τ at height H > Bτ** (the σ̃ ≤ τ branch is
proved + gives HLC directly; the s5 construction shows low-height σ̃ > 0 webs exist, so the
exclusion is genuinely height-conditional). Everything else — the chain, both edge cases,
the corner, the σ̃ ≤ τ branch — is proved (much of it 2-family). The single open is now a
SIGNED quantitative Baake–Sumner stability statement, with: the δ = 0 anchor byte-pinned,
the pushed-witness lemma certifying that LP methods cannot close it, s3's died-at marking
the leakage estimate as the missing technical step, and the s5 family as the sharpening
test case. Empirically: ZERO verified instances at H ≫ δ exist (the linear law H ≤ ~2δ
fits the entire record); d13 final verdict pending.

---

# d13 — FINAL VERDICT: OUTCOME (c), HIGH STRENGTH. The flat floor is a corner extrapolation;
# the LINEAR LAW is the empirical truth.

Report: notes/d13-smalldelta-witnesses.md (NOTE: written under experiments/notes/ — move on
commit); data: out/d13_smalldelta.json. ~5000 verified exact idempotents PER δ (idem_resid
= 0, honest τ, multiplicity-correct W, presolve OFF), THREE independent generators (d3
fixed-τ, d3 random-canonical, d7 shadow-shell). [NUMERICAL, high strength]

- Max H/τ over hidden robust VERTICES collapses monotonically: δ = 1e-2 → 0.222,
  3e-3 → 0.110, 1e-3 → 0.077, 3e-4 → 0.035 (δ/H² = 20 → 833 ≫ the floor band [3.4, 8]).
  **No verified hidden-top-vertex instance exists near the floor for δ ≤ 1e-2.**
- Achieved H tracks 2δ at every δ (H/(2δ) ≈ 1.0–1.2); H/(0.536√δ) → 0.065. Crossover at
  δ ≈ 0.05–0.06 where 2δ = 0.536√δ — exactly the corner.
- Pipeline control: the δ = 5e-2 anchor PASSES full d12 anatomy (m* = 1, 100% W-vertex
  witness) — the machinery finds the floor where it exists; below the corner there is
  nothing to find.
- Generator caveats logged honestly (d8_mrp3 corner-only; a d3 rand_P_fixed_tau δ-overshoot
  bug, neutralized by band-gating).
- The worker's "hidden NON-vertex remains the open object" caveat is VACUOUS by the
  top-vertex reduction (w9chain + s9 #4, independently proved: dist₁(·, conv W) is convex ⇒
  the row-max is attained at a row vertex; no hidden vertex above 2δ ⇒ no row above 2δ).
  [orchestrator]

**EMPIRICAL CLOSURE:** every verified instance ever produced by this campaign — 67k+ day-1,
d8–d13, all scales, all families — satisfies the LINEAR LAW δ ≳ H/2 (with the corner δ*
= (2−√3)² as the unique extremal scale, where the linear and exposedness walls meet). The
conjectured √δ floor NEVER existed below the corner. The proof target is now unambiguous:
**the linear law (δ ≥ cH for exact signed idempotents, equivalently the height-conditional
σ̃ > τ web exclusion)**, which implies HLC, op-exposed-hull, and op-classical with room to
spare. d13 = the campaign's decisive numeric.

---

# WAVE 10 — the 10-strategy-kind swarm (answers: notes/swarm-answers/, t1–t10)

| kind | verdict | death point (native language) |
|---|---|---|
| t1 induction-on-n | DIED-AT | W-stability under state deletion (named missing lemma) |
| t2 probabilistic | DIED-AT / (a) COLLAPSE | (b) signed coupling defect uncontrolled |
| t3 rank-complement | DIED-AT (native) | quantitative (δ,H,W)-complementation algebra |
| t4 extremal-KKT | **COLLAPSE** | "the normal cone of the hiddenness constraint IS the exposedness-LP dual cone" |
| t5 SOS | **COLLAPSE** | quadratic module lacks any generator beyond C10-exchange on each stratum |
| t6 discharging | DIED-AT | conservation g = Pg yields no forbidden local configuration |
| t7 Lyapunov | DIED-AT (native) | the designed-Φ inequality unobtainable |
| t8 minimax | **COLLAPSE** | instance space non-convex; lifted game trivializes or re-enters LP |
| t9 homotopy | **COLLAPSE** | the wall where the path creates/destroys hidden vertices is an exposedness-LP wall |
| t10 Birkhoff | DIED-AT (native) — **with the FINISHER proved** | see below |

## META-FINDING (the wave's discovery): hiddenness IS the LP frame
Five independent strategy kinds collapsed into the exposedness-LP basin at exactly the
moment they used "v hidden" as a hypothesis — t4's formulation is definitive: the normal
cone of the hiddenness constraint is the LP dual cone. ⇒ Any proof EITHER works inside the
LP frame (where the pushed-witness certificate blocks cleanup) OR must avoid hiddenness as
a hypothesis — i.e. needs a W-FREE surrogate formulation (→ formulation-hunter).

## t10 — THE FINISHER, PROVED (conditional): projective idempotent-collapse lemma
For a nonneg kernel K with Hilbert projective row-diameter Δ (Birkhoff contraction
q ≤ tanh(Δ/4) — NO spectral gap) and ‖K²−K‖_{∞→1} ≤ ε: diam₁{rows} ≤ 2ε/(1−q). ⇒ a
closed, bounded-diameter shallow top block collapses to an EQUAL-INPUT cluster; collapse
radius < ρ ⇒ g/Ω_g exposes the top row ⇒ contradiction. **The ONLY missing input: top-band
closure** — λ_T := sup_{i∈T} Σ_{j∉T}|P_ij| small. The harmonic bound P⁺_i(T^c) ≤
(g_i + δΩ)/(κΩ) is order-1 ONLY for rows with g_i near the band edge. [death certificate:
λ_T = O(1) possible at the boundary; unbounded-Δ case = support-graph B–S stability]

## POST-WAVE-10 TARGET (the next inward burn): THE BAND-CUT CLOSURE LEMMA
Choose the band threshold t ADAPTIVELY (pigeonhole over dyadic levels of g in [κΩ/2, κΩ]
or a weighted average over t): since total crossing mass is budgeted (g = Pg + the
harmonic bound, summed/integrated over levels), SOME cut level has small boundary leakage
in the relevant weighting ⇒ T_t is a closed almost-stochastic almost-idempotent positive
block ⇒ t10's finisher fires ⇒ equal-input collapse ⇒ exposure. Sub-questions: the right
weighting (carrier mass? μ-mass? row count?); the Δ-bounded vs Δ-unbounded dichotomy
(zero-pattern degeneration → support-graph combinatorics, where the s5 family lives).
This is the first time the campaign has a PROVED finisher waiting on a single localization
input of classical type (good-cut/coarea pigeonhole).

---

# WAVE 10.5 + report v2 reviews (answers archived in notes/swarm-answers/ as w105_*, review2_*)

- **bandcut: DIED-AT the uniform cut-leakage estimate.** The pigeonhole/coarea cut gives
  AVERAGED leakage; t10's finisher (as stated) needs the SUP-form λ_T ≤ c(1−q)τ. The
  residual is now: either strengthen the cut (sup-control via a two-scale cut / removing
  few bad rows) or weaken the finisher to tolerate weighted leakage (re-derive Birkhoff
  contraction under L¹-leakage). BOTH are concrete, classical-type questions — the
  sharpest the residual has ever been.
- **wfree: RECOMMENDED W-free form = Baake–Sumner NORMAL-FORM DISTANCE** (dist of P to the
  exact nonnegative idempotents, after the B–S structure): kills the hiddenness quantifier
  (the collapse driver), makes the finisher hypothesis natural, δ=0 case is B–S verbatim.
  Full statement + equivalence losses in the archived answer.
- **bsautopsy: SOURCE FACT — Baake–Sumner do NOT prove the classification** (stated as a
  reformulation of Högnäs–Mukherjea; no written proof in the byte-pinned file). The audit
  reconstructs the proof and flags a NORM LANDMINE: entrywise ≥ −δ only gives block
  negative mass ≤ mδ (m = block size) — dimension-free control needs the ROW-mass
  convention throughout. Step table in the archived answer. ⇒ refs acquisition task:
  byte-pin Högnäs–Mukherjea (L1: TIB).
- **Report v2 reviews:** overclaim P = 0.86 (passing; no banned resurrection; small fixes
  listed); readability 0.25 → 0.35 (22 concrete defects; the structural one: the
  self-containment CLAIM must be qualified to "self-contained modulo two declared
  black-box imports" or the imports fully stated). v3 fixer launched.

## NEXT (the inward burn continues)
1. v3 fix round (22 defects + overclaim list) → re-review → ship to user.
2. Band-cut residual pair: (a) sup-form cut via bad-row removal; (b) weighted-leakage
   Birkhoff finisher. [the #1 math target]
3. W-free reformulation: 2-family audit of wfree's equivalence theorem, then adopt as the
   canonical statement of the open core.
4. Byte-pin Högnäs–Mukherjea; re-run bsautopsy on the REAL proof.

---

# WAVE 11 (answers archived as w11_*) — the band-cut pincer dies; the gap is now atomic

- **bc_supcut DIED-AT the excision-to-sup tradeoff:** the Markov threshold argument cannot
  reach η* = c(1−q)τ — excising enough rows to force sup-leakage ≤ η* removes a constant
  fraction of the band per round; the CZ-recursion's re-closure cost (mass the excised rows
  carried into the kept block) regenerates leakage at the same order. Full display in the
  archived answer.
- **bc_weighted PARTIAL:** weighted Dobrushin contraction IS provable (a real new lemma),
  but the t10 EXPOSURE step (collapse radius < ρ ⇒ g/Ω exposes v) irreducibly needs
  sup-control on the rows within the collapse radius — the weighted bound cannot see which
  rows those are. The band-interior observation (g ≤ t/2 rows have automatic sup-leakage
  ≤ 1/2 + ε) gives a 1/2-contraction, but iterating against K^m ≈ K pays the leakage m
  times (derived honestly — the hoped-for free iteration fails).
- **wfree_audit PARTIAL:** B–S normal-form distance is the right CANONICAL TARGET (clean,
  W-free, δ=0 anchored) but w105_wfree's equivalences need extra hypotheses + unspecified
  constants; the partition search is "essentially the classical stability problem itself"
  — not cosmetic, not a shortcut. Adopt as the statement, not as a route.

# ORCHESTRATOR STRATEGIC ASSESSMENT (post-wave-11)
The residual is now ATOMIC: **sup-vs-averaged leakage control at the band edge of a signed
almost-idempotent block** — six independent died-at certificates surround this single point
(s3 leakage, bandcut averaged, supcut excision, weighted exposure-step, plus the t10 and
s8 death certificates fencing the approaches). Every named classical upgrade (pigeonhole,
CZ excision, weighted norms, iteration) has been tried and its failure quantified. The
remaining unwalked paths:
1. **The real Högnäs–Mukherjea proof** (bead filed) — the δ=0 argument's actual mechanism
   is UNKNOWN to the campaign (B–S cite it without proof); its structure may dictate the
   correct δ > 0 surrogate (this is how the corner mechanism was found: read the object,
   not the wish).
2. **d14 (numerics): measure the actual band-edge leakage profile** on the corner, s5, and
   d13 instances — if verified instances ALWAYS satisfy sup-leakage ≤ η* (the lemma being
   TRUE with a structural input the belt lacks), the certificate shapes say what that
   input is; if they violate it, the band-cut route is dead for a reason and the honest
   obstruction map closes there.
3. The honest-stall write-up (PRD-sanctioned): conditional theorem (linear law ⟸ band
   closure) + corner theorem + s8 branch + finisher + atomic residual = a complete,
   publishable obstruction map. The report (v3, delivered) already carries most of it.

---

# d14 — leakage profiling (COMPLETE, 15/15 verified): THE LEAKAGE QUESTION DISSOLVES

Report: notes/d14-leakage-profiles.md; data: out/d14_leakage.json. [NUMERICAL, all gates]
- Sup-leakage is VIOLATED everywhere but BENIGNLY: the floor is exactly δ = H/2, carried
  100% by v's own NEGATIVE entries pointing at deep rows; the bad shell carries ZERO
  leakage. Sup-vs-averaged was a red herring — the sup is one row (v), purely negative,
  budgeted by δ.
- **POSITIVE leakage λ⁺ = 0 at a realizable threshold on EVERY instance** — the t10
  finisher's closure hypothesis HOLDS for the positive kernel B⁺.
- **The TRUE residual is the finisher's OTHER hypothesis: projective diameter Δ = ∞
  (q = 1) on every structured instance** — in-band carriers feed disjoint-support
  W-archetype rows. The band-cut route dies at the SUPPORT-GRAPH / unbounded-Δ branch
  (exactly where t10 placed it; s5 is the family with no finite-Δ block at any t).
  This sharpens s3's died-at: the "boundary row" is v, budget δ, purely negative.

# POST-d14 TARGET (wave 12): the SUPPORT-GRAPH COMPONENT FINISHER
Δ = ∞ comes from zero entries — i.e. the support graph of B⁺ is disconnected/thin. But
disjoint supports at δ = 0 are EXACTLY the B–S normal form's block structure: infinite Δ
is intrinsic to the ANSWER, not an obstruction — the contraction must run PER COMPONENT.
Programme: (1) within a support-component, bootstrap positivity from idempotence
(K^m ≈ K for all m + primitivity ⇒ effective entrywise positivity at scale path-product
vs defect — the dimension-free tension is the work); (2) per-component collapse (finisher)
⇒ equal-input clusters ⇒ expose (F-ND/coincidence machinery); (3) cross-component: B⁺
components do not interact positively BY DEFINITION; the only couplings are v's δ-budget
negatives — assemble. Refuter target: a band component that is an arbitrarily long thin
chain (path products ε^L vs defect — the dimension-free killer candidate).

---

# WAVE 12 (archived as w12_*) — the component finisher PROVED for fat components; the
# survivor is the THIN-CHAIN class; the refuter could not realize it

- **comp_finisher PARTIAL (a real theorem):** the support-component finisher holds with
  explicit constants for every PRIMITIVE component whose minimum path-product Π_C beats
  the signed/idempotence error: the survivor class is exactly
  Π_C ≤ E_L(δ,ζ) + 2(1+δ)ε/(r*−4δ), r* = 0.85τ (F-ND consumer) — i.e. edge-floor a gives
  a^L ≲ Cτ + O(Lδ). Equal-input collapse + exposure runs end-to-end on every fat
  component. **The open core is now: exclude long-thin chains (vanishing path products)
  in the σ̃ > τ band.**
- **chain_refuter NOT-CONSTRUCTED:** every exact-rational thin-chain template snapped on
  the gates; the s5 seed remains the only living web and it sits at σ̃ < τ — INSIDE the
  already-proved branch. No verified instance has EVER entered the σ̃ > τ, H > Bτ regime.

# POST-WAVE-12 STATE — the kernel
The entire campaign now rests on one statement: **thin-chain exclusion** — an exact signed
idempotent cannot support a σ̃ > τ hidden top vertex whose band component is a long thin
chain (path products below the finisher's floor). Status: no analytic proof, no
counterexample, no verified instance anywhere near the regime; the refuter's failure map
+ the comp_finisher's explicit inequality bracket it from both sides. Everything else in
the chain (linear law ⟸ component finisher + thin-chain exclusion ⟸ ... ⟸ op-classical)
is proved or proved-mod-audit.

---

# WAVE 13 (archived as w13_*) — SYMMETRIC STALEMATE AT THE KERNEL

- **chain_excl DIED-AT the path-product lower bound:** the needed-and-unproved inequality
  is Π_C ≳ τ − O(Lδ) (or any substitute beating the wave-12 survivor inequality). Best
  honest yield: the recursive high-web reduction (every shallow component node is itself
  far from conv W with large geometric σ̃) — the budget recursion holds but does not force
  the path-product floor.
- **chain_refuter2 NOT-CONSTRUCTED, including the priority PERIODIC template:** the
  period-two attack (aimed at the finisher's primitivity hypothesis) fails the gates in an
  instructive dichotomy — either the period-two mass stays below τ (inside the proved s8
  branch) or raising the height exposes the candidate rows (they enter W). Trees, frame-
  chains, parallel bundles: all snapped; failure map recorded.

# FINAL STATE OF THE CAMPAIGN (2026-06-11, after 13 waves, 10 strategy kinds, ~55 workers)
**Prover and refuter are jammed against the SAME inequality from opposite sides:**
  Π_C ≳ τ − O(Lδ)   for the band component of any σ̃ > τ hidden top vertex.
- TRUE ⇒ thin-chain exclusion ⇒ (with the proved component finisher + s8 branch) the
  LINEAR LAW ⇒ HLC ⇒ op-exposed-hull ⇒ op-classical. ALL other links proved or
  proved-mod-audit, constants explicit.
- FALSE ⇒ a realizable thin-chain web ⇒ the first H ≫ δ instance ever ⇒ likely
  refutation geometry for the linear law (HLC itself would survive unless H/τ
  exceeds ~0.5 — the corner theorem caps what a counterexample can do).
- No verified instance has ever entered the regime; both directions have quantified
  failure maps; every classical technique and ten strategy kinds have measured death
  certificates. Remaining unwalked: the real Hognas–Mukherjea proof (bead), an
  SOS/certificate search SPECIALIZED to the chain inequality (small n, the reduced
  problem — distinct from the collapsed full-problem SOS of wave 10), and the
  PRD-sanctioned obstruction write-up (report v3 already carries the structure).

# WAVE 14 — the REAL Hognas-Mukherjea autopsy (codex, landed 2026-06-11) [pending w15 audit]
Full verdict: notes/swarm-answers/w14_autopsy.md. The delta=0 proof (H-M Thm 2.2 / 1.11 /
1.16) does NOT perturb directly: SIGN-RIGID at zero-sum closure ("0 = sum of nonnegatives
=> each term 0" — THE main failure), zero-pattern symmetry/block partition, and positive
diagonal (fails already for rank-one signed P = 1*pi with pi_i < 0). SIGN-ROBUST: exact
row reproduction — P^2 = P exact gives
  dist(p_i, conv{p_j : P_ij > 0}) <= (2+4*delta)*nu_i <= (2+4*delta)*delta,
and the post-collapse equal-input specialization. The rank-one-block step is quantitatively
repairable: entry floor theta_C on a component gives row diameter <= 2(1+delta)*eps/theta_C
+ 4*delta (eps <= 7*delta + 6*delta^2) — O(sqrt(delta)) at theta_C ~ sqrt(delta).
SYNTHESIS: the signed analogue of the kernel/minimal-ideal mechanism is: visible exposed
vertices = recurrent classes; hidden top vertices generate a shallow positive carrier
graph; a positive SCC with path-product mass above signed error = the "approximate minimal
ideal", to which the proved w12 component finisher attaches. H-M therefore POINTS AT
Conjecture 2 (the path-product floor) as the right surrogate — it identifies the missing
step, it does not supply it. P(mechanism yields conjecture) = 0.63; P(reading survives
audit) = 0.86. CAVEAT: read delta as ROW negative mass (matches kernel-conjecture.tex);
entrywise reading would void the moduli.

# WAVE 15 — launched 2026-06-11 (6 codex, parallel; briefs at /tmp/codex-sigma-wall/w15_*)
- w15_audit: hostile derive-first audit of the w14 autopsy (loci + moduli + synthesis).
- w15_prover: Conjecture 2 via the H-M signed-surrogate frame (exact idempotence free,
  P^k = P amplification vs O(L*delta) signed loss).
- w15_refuter: counterexample design AT the sign-rigid steps (cancellation where the
  proof needs positivity; periodic-carrier degree of freedom; must dodge prior failure maps).
- w15_sos: chain-specialized SOS/LP certificate search, reduced inequality, L = 2..5,
  rational rounding (the last unwalked computational route).
- w15_periodic: close the w12 finisher's primitivity gap (try: exact P^d = P excludes
  nontrivial periodic carrier?).
- w15_hmloci: byte-pin the H-M loci for the kernel-conjecture.tex §5 anchor caveat
  (extraction-level; grep -F-verified quotes).

## w15_audit (codex) — the w14 autopsy SURVIVES MOD 2 CORRECTIONS [audit of the audit chain done]
Full table: notes/swarm-answers/w15_audit.md. All sign-rigid/sign-robust row verdicts
CONFIRMED; the exact-row-reproduction modulus, the rank-one-block repair, and the
small-invisible-mass branch all INDEPENDENTLY RE-DERIVED (p_i - q_i = nu_i (q_i - r_i)
identity; dist <= (2+4*delta)*nu_i; dist(p_v, C_W) <= 2(1+2*delta)*max(sigma_tilde_v, nu_v)
<= 3*sqrt(delta) on the sigma_tilde_v <= sqrt(delta) branch). CORRECTIONS:
(1) w14 row "exact row reproduction" cited H-M txt lines 55-65/81-82 — front matter; the
real locus is kernel-conjecture.tex:55ff (campaign setup). (2) THE SYNTHESIS IS TOO LOOSE:
"positive SCC with path-product mass = approximate minimal ideal" UNDERSPECIFIES the w12
finisher's hypotheses — attachment needs (a) a CLOSED positive component (P^+_{S,S^c} = 0),
(b) PRIMITIVE (the periodic gap — w15_periodic in flight), (c) the collapse radius beating
the exposure threshold: 2(1+delta)*eps/theta_C + 4*delta < r_* with r_* = 0.85*tau in the
audited consumer — NOT merely Pi_C > 0. delta-convention caveat MOOT (campaign = row
negative mass, kernel-conjecture.tex:62). P(autopsy survives as written) = 0.70;
P(signed-surrogate frame is the right next attack) = 0.74. ORCHESTRATOR NOTE: the
dossier's WAVE 14 section above stands with correction (2) — read "approximate minimal
ideal" as "closed primitive positive component with radius < r_*".

## w15_hmloci (codex) — the delta=0 anchor is PINNED; kernel-conjecture.tex §5 DISCHARGED
Full table: notes/swarm-answers/w15_hmloci.md. H-M Thm 1.16 (txt:2767-2777) covers the
finite stochastic-idempotent case DIRECTLY (no compact-semigroup specialization needed);
proof source = Thm 1.11 (:2225-2244) via Thm 1.18 (:3079-3210). Orchestrator grep -F
spot-checked both key excerpts. Honest mismatch notes: H-M states ratio/proportionality —
the convex-mixture + visible-vertex sentences are easy campaign consequences (columns in
T_c vanish + rows sum to 1), recorded as such. kernel-conjecture.tex §5 anchor item
REPLACED (caveat discharged at extraction-level provenance tier) + recompiled clean.

## w15_sos (codex) — NO CHAIN-LOCAL CERTIFICATE EXISTS: the scalar shadow is FALSE
Full answer + formalization: notes/swarm-answers/w15_sos.md; script + outputs:
experiments/out/w15_sos/. Verdict: FORMALIZATION BLOCKED for L = 2..5 — the notes contain
no complete polynomial reduction in (edge weights, delta, sigma_tilde, tau) alone; w13's
thin-chain scale is the OBSTRUCTION, not an exact construction. STRONGER: the best
justifiable scalar shadow has EXACT RATIONAL witnesses (tau = 1/100, delta = 1/10000,
sigma_tilde = 1/50, a_i = d_i = 1/100) satisfying all scalar constraints while violating
Pi_L + L*delta - tau >= 0 for EVERY L in {2,3,4,5} — hence NO LP/SOS certificate at ANY
degree for the scalar shadow. READING: the path-product floor, if true, is NOT chain-local;
any proof MUST consume a matrix/hiddenness row-realization constraint (consistent with the
w13 symmetric stalemate). The scalar witnesses are NOT counterexamples to Conjecture 2 —
realizability by an exactly-idempotent matrix with a hidden top vertex is exactly the open
content. NEXT-WAVE TARGET: realize the scalar witness as an actual instance (refuter side)
or prove unrealizability from hiddenness (prover side) — the kernel in its sharpest form yet.

## w15_prover (codex) — DIED-AT, but discovers THE CLONING OBSTRUCTION [audit in flight]
Full answer: notes/swarm-answers/w15_prover.md. The H-M surrogate DOES generate shallow
positive carrier mass (A_v(S_t \ C_W) >= (B/3 - 4)*tau, derived) and the exact-idempotence
shortcut works (P_ij >= (A^k)_ij - k*delta*(1+2*delta)^{k-1}). DIED-AT (display-boxed):
(A_C^k)_ij >= c*tau + O(k*delta), equivalently Pi_C >= c*tau - C'*L*delta. THE DISCOVERY:
index-cloning P_hat_{ab} = alpha_b * P_{pi(a),pi(b)} preserves exact idempotence (orchestrator
re-derived: (P_hat^2)_ab = alpha_b (P^2)_{pi(a)pi(b)}), row sums, delta, and the ENTIRE row
geometry (l1-isometry on row differences: vertices, W, H, g, sigma_tilde, hiddenness), yet
Pi_hat_C <= (1+delta)/M -> 0. Conjecture 2's carrier graph is RAW-INDEX (kernel-conjecture.tex
~:230-241 — only def:vertex is multiplicity-correct), so the floor AS WRITTEN appears
false-or-vacuous; Conjecture 1 (a distance statement) is untouched. Repairs that fail at index
level: P^k=P controls sums not atoms; mass survives cloning but the finisher eats atoms;
degree bounds can't be dimension-free; thresholds blind to fibers. The viable repair is the
QUOTIENT (multiplicity-correct carrier graph) — "a different theorem" (prover's repair 5).
P(index-level floor true) ~ 0.30 (mostly vacuity); P(H-M route closes without redefining
the floor) ~ 0.18. FOLLOW-ONS LAUNCHED: w15_clone_audit (hostile check incl. the vacuity/
seed-instance logic + whether exposing functionals lift to the split column space),
w16_quotient (state Conjecture 2', prove clone-invariance + finisher lumpability, attack).

## w15_periodic_audit (codex) — the periodicity patch HOLDS; constants verified
Full answer: notes/swarm-answers/w15_periodic_audit.md. Verdict: PATCH HOLDS for CLOSED w12
positive components (d_i >= 1) in the campaign's max-row-sum norm; N^2 >= 0 so the mixed-term
bookkeeping is safe; exact threshold 3*delta + 4*delta^2 < 1 iff delta < 1/4; d = 2 is NOT a
surviving case (C_{r+2} = C_r still forbids self-loops under period 2). Approximate-closure
tolerance derived: leakage eta < 1 - sqrt(3*delta + 4*delta^2) (or the worsened-zeta variant).
The finisher display needs delta < (0.85/4)^2 ~ 0.0452 for the denominator. NOT discharged:
the separate analytic band-closure caveat (already recorded in kernel-conjecture.tex
:261-264); the patch applies to closed components, not arbitrary carrier SCCs. STATUS: the
"periodic components" open sub-issue riding with conj:floor is CLOSED for closed components
(prover w15_periodic + independent hostile audit, P = 0.92/0.87). Doc edit deferred until the
cloning question settles (conj:floor may be restated as 2').

## w15_refuter (codex) — NOT-REFUTED; the new quantified barrier: delta/sigma_tilde^2 >= 1.52
Full answer + long-form verdict: notes/swarm-answers/w15_refuter.md; full stack (search +
template audit + best instances): experiments/out/w15_refuter/. Three template families
(LP-financed s5/cycles: 272 in-regime verified; positive-diagonal/self-mass: 45;
stochastic conjugations: 3) — 1368 verified exactly-idempotent matrices total, ZERO
in-regime branch hits. Closest record: delta = 0.0609, sigma_tilde/tau = 0.811,
H/tau = 0.029, Pi_C/tau ~ 6e-6 — a genuinely thin shallow SCC exists, but the
LOAD-BEARING GATE sigma_tilde > tau is never crossed (best self-mass attempt:
delta/sigma_tilde^2 = 1.52 > 1). Updated P(floor true in small-delta regime) = 0.84.
Most promising remaining DOF: end-to-end nonlinear optimization over (L,B) with W-aware
loss instead of LP-completing Q; the concrete barrier to beat is delta/sigma_tilde^2 < 1
while keeping the top vertex hidden.

## ORCHESTRATOR SYNTHESIS (post w15_prover + w15_refuter, pending w15_clone_audit)
The cloning obstruction + the refuter's empty in-regime record CLOSE A LOGICAL LOOP:
cloning maps any antecedent-realizing seed to a floor-violating instance (geometry
preserved, Pi -> 0), hence the RAW-INDEX floor is true IFF the antecedent regime
(hidden v, sigma_tilde > tau, H > B*tau) is EMPTY — i.e. Conjecture 2 as written is
either FALSE or exactly EQUIVALENT to the hard case of Conjecture 1 (no intermediate
content). The refuter's barrier (delta/sigma_tilde^2 never < 1.52, 67k+ + 1368 instances,
zero antecedent hits ever) is evidence FOR emptiness — i.e. for the kernel itself. The
only viable INTERMEDIATE working form is the quotient floor 2' (w16_quotient in flight).
Equivalently: the sharpest new attack target is the BARRIER INEQUALITY itself — prove
"hidden top vertex => sigma_tilde_v <= C0 * sqrt(delta)" directly (if true with any
universal C0, the s8 + height-collapse branches finish via the proved belt: that IS the
kernel conjecture in its leanest form yet, now with a measured constant 1.52 to beat).

## w16_quotient (codex) — 2' FORMULATED + BRIDGE SECURED; clone-invariance PROVED; died at ANTI-SPLITTING
Full answer (LaTeX-ready statements): notes/swarm-answers/w16_quotient.md. DELIVERED:
(1) Conjecture 2' — the floor on the QUOTIENT carrier graph (classes = exactly coincident
rows; Q_{alpha beta} = aggregated mass; well-definedness proved). (2) CLONE-INVARIANCE
PROVED: quotient objects of any duplicate split are canonically isomorphic with equal Q —
the w15 obstruction is neutralized BY CONSTRUCTION. (3) LUMPING LEMMA (the bridge): Q1 = 1,
Q^2 = Q, delta(Q) <= delta(P), g descends Q-harmonically, band closure descends,
||(B')^2 - B'|| <= ||B^2 - B||, and the w12 finisher applied to Q gives class collapse
= index collapse (identical rows). Finisher-calibrated form: theta_C >= 20*tau suffices at
delta_0 <= 1e-4. (4) NEW CAVEAT — exact quotienting is NOT ROBUST: similarity conjugation
P_eta = S P_hat S^{-1}, S = I + O(eta), keeps exact idempotence + row sums while smearing
duplicates into an eta-cloud (path weights O(1/M) + O(eta)); the honest target is the
eta_cl-CLUSTERED quotient with eta_cl <~ delta (cost: zeta -> zeta + O(eta_cl)).
(5) DIED-AT (boxed): Pi'_C >= c*tau - C'*L*delta — current identities control AGGREGATE
path sums, not a best single path product; mass can split over many nearly coincident
quotient classes; the missing piece is an ANTI-SPLITTING principle from hiddenness/
realization. The quotient H-M surrogate survives: (Q^+)_{[v]}(S_t \ C_W) >= (B/3-5)*tau,
Q^k = Q. P(2' true exact) ~ 0.48, provable-in-frame ~ 0.22; CLUSTERED variant: ~ 0.66 /
0.38. ORCHESTRATOR: the campaign's kernel is now the pair {anti-splitting principle for
the clustered quotient, the barrier inequality sigma_tilde <= C0*sqrt(delta)} — these are
dual faces: anti-splitting concentrates shallow mass into one fat quotient component
(finisher exposes => contradiction => barrier); splitting forever IS the thin-web geometry.

## w16_barrier (codex) — DIED-AT quotient pinning; CONVERGENT with w16_quotient's anti-splitting
Full answer: notes/swarm-answers/w16_barrier.md. On the H > B*tau branch (the H <= B*tau
branch is the proved belt), PROVED clone-invariantly: A_v(S_t^c) <= 4*tau and
A_v(S_t \ C_W) >= (B/3 - 4)*tau — high hidden height forces aggregate shallow off-C_W
carrier mass at scale tau. DIED-AT (boxed): max over closed quotient components C of
A_v(C) >= c_B*tau — equivalently a dimension-free bound N_B on the number of geometrically
distinct shallow quotient components hit by P_v^+. No audited tool gives it: l1 geometry
has no dimension-free packing bound; cloning removal only kills COINCIDENT rows;
return-flow can spread over arbitrarily many classes; coarea gives averaged not sup
closure. TWO INDEPENDENT PROVERS (w16_quotient, w16_barrier) NOW DIE AT THE SAME MISSING
PRINCIPLE: anti-splitting / quotient pinning. Named decider target: a SHALLOW FAN — v
spreads O(tau) positive mass over many noncoincident quotient classes while the hiddenness
LP blocker sits on a far top-band average (if constructible: barrier route as framed dies
and likely a 2'-counterexample geometry; if obstructed: the obstruction IS the
anti-splitting principle). P(barrier true) ~ 0.74; P(closes without a new facial-modulus
theorem) ~ 0.22.

## w15_clone_audit (codex) — OBSTRUCTION REAL BUT CONDITIONAL; quotient repair endorsed
Full answer: notes/swarm-answers/w15_clone_audit.md. ALL hostile checks pass: algebra
re-derived; the splitting is an l1-isometry on rows; EXPOSERS LIFT AND DESCEND (the
subtle check — via the fiber-summing map R with ||R||_{1->1} <= 1), so W, H, g,
sigma_tilde, hiddenness, and the high-hidden antecedent are all invariant; clone diameter
<= 2L independent of M; no path avoids the divided edges. LOGICAL STATUS RESOLVED: the
raw-index floor is FALSE if any antecedent-realizing seed exists, else VACUOUSLY TRUE —
no record instance qualifies (67k+; kernel-conjecture.tex item 1), so conj:floor as
written carries no content beyond conj:kernel. Quotient repair endorsed (matches
w16_quotient's 2'; for cloning, quotient weights = the ORIGINAL edge weights exactly).
Residual flagged for af-grade work: the finisher for arbitrary coincident-row quotients
with internal signed cancellation inside a class. Coherent with w15_sos. P(verdict
survives) = 0.88. DOC UPDATED: kernel-conjecture.tex now carries the periodicity closure,
the cloning status-correction paragraph, Conjecture conj:quotient-floor (multiplicity-
correct floor), and ledger item 6 (wave-15/16 constraints); recompiled clean, 6pp.

## w16_nlopt (codex) — SIGMA-BARRIER CROSSED (first sigma_tilde > tau hidden vertex ever) [pending w16_cert_audit]
Full answer + long-form: notes/swarm-answers/w16_nlopt.md; instance + frontier + scripts:
experiments/out/w16_nlopt/. End-to-end nonlinear optimization over exactly-idempotent
factorizations P = LB, BL = I (the w15 refuter's named DOF) at (n,k) = (7,4):
delta = 0.2284, tau = 0.4779, hidden v = 4 (HiGHS-optimal hiddenness LP, t*/kappa = 0.162),
sigma_tilde = 0.7769, sigma_tilde/tau = 1.626, delta/sigma_tilde^2 = 0.378 (old measured
barrier 1.52 SHATTERED), idempotence/rowsum residuals 2.2e-16. ORCHESTRATOR READING
(critical): H/tau = 0.0158 — NEGLIGIBLE HEIGHT, and delta = 0.228 is large. So this does
NOT enter the floor conjectures' antecedent (sigma_tilde > tau AND H > B*tau) and does NOT
contradict the doc's record item (no instance with sigma_tilde > tau AND H > 0.1*tau —
still true). What it KILLS: the height-free barrier formulation "hidden => sigma_tilde <=
C0*sqrt(delta)" (w16_barrier's target as posed — FALSE at least at large delta; worker's
P(C0=1 barrier true) = 0.01); and it resets the measured sigma-frontier. The campaign's
empirical question is now the TRADEOFF: can sigma_tilde > tau coexist with H > 0.1*tau?
FOLLOW-ONS LAUNCHED: w16_cert_audit (independent verifier, claimant's code banned;
rationalization/interval hardening; context coherence vs height-collapse + corner) and
w17_antecedent (homotopy from the instance: maximize H/tau subject to hidden +
sigma_tilde > tau; couplings with the corner family; fixed-H sigma-frontier sweeps; if
realized — test the QUOTIENT floor on it; if not — fit + conjecture the boundary law).

## w16_cert_audit (codex, independent verifier) — the crossing is CERTIFIED (EXACT RATIONAL)
Full table: notes/swarm-answers/w16_cert_audit.md; verifier + rational instance + report:
experiments/out/w16_cert_audit/. Fresh verifier written from the definitions (claimant's
code banned): every claimed number reproduced to the last digit; all 7 rows geometrically
distinct row vertices; hiddenness LP primal=dual to 3e-16, the t >= kappa LP INFEASIBLE
(a dual certificate of hiddenness). RATIONAL HARDENING: continued-fraction rationalization
(denominators <= 1e4) with EXACT BL = I, P^2 = P, P1 = 1; exact delta = 0.22840027,
exact sigma_tilde = 0.77687284; margins (sigma - tau = 0.299, hidden gap 0.100, outside
distance 0.0064) dwarf the 5.2e-7 drift. Second saved instance verifies float-only but is
threshold-fragile (4.6e-9 margin) — use the main one. CONTEXT: coherent with
height-collapse + corner; H/tau = 0.0158 so no contradiction with the recorded joint
(sigma > tau AND H > 0.1*tau) emptiness. BONUS: Q-rescaling continuation crosses at
delta <= 0.1 (sigma/tau = 1.028 at delta = 0.0914) — NOT a large-delta artifact.
P(genuine) = 0.999. STATUS CHANGES: (1) height-free barrier formulation DEAD (recorded);
(2) doc ledger 6(c) REWRITTEN (the sigma gate is crossable; the open question is the
sigma-H TRADEOFF); (3) the w15_refuter "1.52 barrier" superseded. w17_antecedent (the
tradeoff decider) is the live worker.

## w17_antecedent (codex) — ANTECEDENT REALIZED (claimed) [pending w17_cert_audit]
Full answer: notes/swarm-answers/w17_antecedent.md; instances + Pareto front + decider:
experiments/out/w17_antecedent/. Claimed FIRST EVER instance with the floor conjectures'
joint antecedent: (n,k) = (10,5), hidden v = 5, delta = 0.23293, sigma_tilde/tau = 1.5467,
H/tau = 0.10019 (cross-checked vs the independent w15 verifier; idempotence residuals
1.1e-16). CAUTION FLAGS (orchestrator): (1) hiddenness margin RAZOR-THIN — t*/kappa =
0.99988 (1.2e-4 relative; robust companion 0.99777) — certification audit launched before
any record correction; (2) delta = 0.233 is ABOVE the corner scale delta* ~ 0.0718: the
SMALL-delta regime of the conjectures is untouched; the linear law is NOT violated
(H = 0.048 <= 2*delta); what would be falsified is the ledger item-1 claim AS STATED
("no instance with sigma>tau AND H>0.1tau", asserted over all scales including large).
QUOTIENT-FLOOR TEST OBJECT: all rows distinct (quotient = raw); main quotient component
[1,2,3,5,6,7], L = 2, Pi/tau = 2.5e-4 — extremely thin; at this delta the floor RHS
c*tau - C'*L*delta can be vacuous, so NOT yet a small-delta refutation, but the first
genuine test object + via CLONING an outright raw-floor refutation for delta0 >= 0.233.
IF CERTIFIED: ledger item 1 must be re-scoped to below-corner scales; the decisive
remaining empirical question becomes whether the antecedent persists BELOW the corner
(d13 says max H/tau collapses ~ 2*delta/tau there — the conjectures' real regime).

# WAVE 18 — the idempotence-exploitation research round (user-directed, 2026-06-11; 5 codex)
Charge: P^2 = P has not been exploited to its fullest; the reformulations retreat to
convex-hull information. Lenses: variety geometry / SOS-mod-ideal / quadratic-matrix
literature / cohomological-similarity (never run in this lane) / semigroup-two-sided.
Answers land below as harvested; bead aipm-(wave18).

## w18_semigroup (codex) — TOP PLAN: fixed-space duality; NEW exact boundary-product identity
Full answer: notes/swarm-answers/w18_semigroup.md. Plan 1 (P_useful = 0.78): the EXACT
spectral form P = sum_s u_s l_s^T (biorthogonal fixed bases) puts every row INSIDE the
k-dim left fixed space — hiddenness/H become statements in the exact affine duality
between left fixed rows and right fixed functions ({g : Pg = g} ~ Aff({p_i}), g_i =
phi_g(p_i)); clone-invariant by construction; candidate replacement for "recurrent
classes" = extreme points of the quasi-positive left-fixed cone K_delta. Plan 2 (P_true
= 0.60): the boundary-product family B^m - B = - sum_{r<=m-2} B^r E C for every band
split — all lengths at once, on the QUOTIENT; dichotomy: fat quotient path product OR
large boundary product charged to deep/visible mass — the most direct route to the w12
finisher. Plan 3 (P_supporting = 0.55): trace tax tr B - tr B^2 = tr(EC), integer total
trace; clone-invariant; candidate sign-robust replacement for the dead positive-diagonal
step (per-component trace >= 1 - O(delta)?). Honest note: the certified n=7 crossing
instance has epsilon_2 ~ 0.61 — at delta ~ 0.23 NO path-product finisher can bite; the
asymptotic regime is where these plans live. Leads to bank: the quasi-positive left-fixed
cone lemma (internal); the clustered quotient floor (internal); Kato/Stewart-Sun
projection-perturbation + Birkhoff-Hilbert contraction sources (ACQUIRE before canonical
use). Synthesis deferred until all 5 land.

## w18_quadlit (codex) — 10 ranked literature leads; the Douglas-Ando reframing
Full table: notes/swarm-answers/w18_quadlit.md (every item UNVERIFIED-LEAD until byte-
pinned). HEADLINES: (#2, conf 0.85) Douglas 1965 / Ando 1966 — norm-one projections on
l1/l-infty have averaging/conditional-expectation normal forms = the H-M family; our P has
||P||_{infty->infty} = 1 + 2*delta, so THE LINEAR LAW IS EXACTLY a quantitative stability
statement for contractive projections on l_infty^n ("hidden height forces projection-norm
excess >= c*H") — the cleanest W-free reframing yet. (#1, conf 0.75) Luo-Pang 1994 /
Hoffman / metric-subregularity error bounds: dist(x, S) <= C||F(x)||^theta on compact
semialgebraic sets; theta = 1 under linear regularity => the FIXED-n linear law may be
nearly free; the singular strata where theta < 1 would be exactly the interesting
geometry; n-dependence of C is the named risk. (#4, conf 0.75) Markov chain tree theorem
(Freidlin-Wentzell): stationary weights = spanning-tree products — a candidate mechanism
to convert aggregate shallow mass into tree products (anti-splitting), with the honest
risk that tree products decay exponentially in component size (the thin-chain obstruction
reborn). Also: Kato similarity (conf 0.95) for the clustered-quotient robustness; Meyer
stochastic complementation (0.90) for cluster aggregation; Stewart-Sun Riccati sep-bounds;
Putinar/Lasserre for hiddenness-aware fixed-n SOS. One suspicious citation flagged by the
orchestrator: an attribution to "Hume" (impossibility of raw O(delta) distance) — likely
garbled; verify before any use. Acquisition shopping list filed as a bead.

## w18_sos_ideal (codex) — smallest hidden geometry at (n,k) = (4,3); the hiddenness-lifting wall again
Full answer: notes/swarm-answers/w18_sos_ideal.md; probe + rank-chart outputs:
experiments/out/w18_sos_ideal/. (3,2): hidden branch EMPTY (H = 0; delta - cH = tau^2 is
trivially SOS). Smallest hidden geometry: (4,3), exact rational rank-chart witness saved
(hidden but low height — no threat to the linear law). Degree-2/4 SOS modulo the ideal at
(4,3): FORMULATION OBSTRUCTION, not a no-certificate verdict — the wall is lifting W /
far-sets / vertex status / dist(., C_W) through global KKT-binary-quotient variables.
CONSISTENT with t5's collapse + the meta-finding: even ON the variety, hiddenness IS the
hard structure to encode polynomially. Useful byproduct: the explicit (3,2) rank-chart
symbolic parametrization (idempotence residual identically 0) — reusable for small-case
symbolic work.

## w18_similarity (codex) — the cohomological route is BLOCKED at a PRECISE point (first-order diagonal displacement)
Full answer: notes/swarm-answers/w18_similarity.md; Newton traces (certified instance +
randoms): experiments/out/w18_similarity/. The Peirce corner retraction works
ALGEBRAICALLY (tangent = E_10 + E_01; diagonal corners quadratically determined). THE
BLOCK: the positivity projection (rounding negative entries away) creates an order-delta
displacement in E_11 + E_00 — a FIRST-ORDER diagonal error the retraction only repairs
QUADRATICALLY in the off-diagonal blocks. Numerics: on the certified w16 instance the
loop reduces negativity only by drifting ORDER-ONE along the variety — no O(delta)-close
H-M cleanup. P(contraction lemma in one wave) = 0.18; P(route eventually proves linear
law) = 0.32. ORCHESTRATOR NOTE — CROSS-LANE CONVERGENCE: this is the classical twin of
op-layer1-gap's "positivity-capable output" obstruction (the main lane's cohomological
error-reduction has the same missing ingredient: a splitting/projection compatible with
the order structure). REPAIR DIRECTIONS for synthesis: (a) positivity projection
constrained to the tangent corners (project the negativity onto E_10 + E_01 moves only);
(b) co-optimize the base point + gauge (the H-M family + similarity simultaneously);
(c) the Douglas-Ando norm-excess functional as the Lyapunov function for the loop instead
of raw negativity.

## w18_variety (codex) — THE TANGENT-CONE PROGRAM (the round's sharpest plan, P = 0.68)
Full answer: notes/swarm-answers/w18_variety.md. STRUCTURE DELIVERED: I^1_{n,k} = {P^2=P,
P1=1, rank k} is a homogeneous space of G_1 = {S: S1=1}, dim = (n-k)(2k-1); tangent
PA + AP = A => pure off-diagonal corners (D1 = 0 on the stochastic slice); EXACT chart
P(C,D) with (I+CD)^{-1} blocks — off-diagonal first-order, diagonal deviations QUADRATIC
(-CD, DC + O(3)): "exactly where the unused quadratic constraint lives". H-M locus =
finite semialgebraic stratification by partition data, stratum dim n - k + t(k-2).
NORMAL GEOMETRY: delta(P_0 + tA) = t * max_i sum_{j: P_{0,ij}=0} (-A_ij)_+ + O(t^2) —
crossing the nonneg boundary pays LINEARLY at active zeros. PLAN 1 (P = 0.68): the linear
law IS the tangent-cone inequality dH/dt <= C * ddelta/dt at every stratum point; the
counterexample side reduces by CURVE SELECTION to an analytic arc whose leading direction
has ddelta = 0 but dH > 0 — the cleanest target in the campaign. Testable at n=3, k=2:
P = I - u v^T (v^T u = 1, v^T 1 = 0), 3-dim variety vs 1-dim normal-form strata. PLAN 2
(0.58): Riccati-corner local model H <= C*delta + O(||(C,D)||^2) uniformly over strata.
PLAN 3 (0.36): quotient anti-splitting from exact idempotence. Certified-instance check
coherent ("high invisible mass can live almost tangent to the H = 0 locus" — exactly why
height-free barriers died). P(at least one plan -> new proved lemma in one wave) = 0.82.

# WAVE 18 SYNTHESIS (orchestrator; all 5 research answers harvested)
The round confirms the user's diagnosis: the quadratic constraint was being consumed only
through weak corollaries (row reproduction, P^k = P sums). What it actually provides:
(1) an exact finite-dim HOMOGENEOUS-SPACE geometry with quadratically-determined diagonal
corners (variety); (2) an exact k-dim spectral/fixed-space coordinate system for all rows
(semigroup); (3) exact all-length boundary-product identities (semigroup); (4) at delta=0,
the Douglas-Ando contractive-projection normal form, making the linear law a PROJECTION-
NORM-EXCESS stability statement (quadlit). CONVERGENCES: [A] variety plan 1 + semigroup
plan 1 + quadlit #2 are three coordinatizations of ONE attack: a clone-invariant,
hiddenness-free, k-dimensional normal-displacement inequality — this is the wave-19 core.
[B] The cohomological Newton loop (similarity) fails EXACTLY at first-order diagonal
displacement from positivity projection — the tangent-cone lemma is its correct
infinitesimal form (prove the inequality BEFORE iterating; cross-lane twin of
op-layer1-gap's positivity-capable output). [C] SOS-mod-ideal re-confirms: hiddenness is
the only structure that resists polynomial lifting (meta-finding upheld on the variety).
WAVE 19 (launching): w19_tangent (the tangent-cone lemma; n=3 model first + numerical
tangent-cone decider), w19_leftcone (the quasi-positive left-fixed-cone extreme-point
lemma), w19_boundary (the boundary-product dichotomy at the w12-finisher interface).
Deferred pending acquisitions (bead): the Douglas-Ando and Luo-Pang formalizations.

## w17_cert_audit (codex, independent verifier) — BOTH ANTECEDENT INSTANCES CERTIFIED EXACT
Full report: notes/swarm-answers/w17_cert_audit.md; verifier + exact rational instances:
experiments/out/w17_cert_audit/. MAIN (delta = 0.23293, H/tau = 0.10019) and ROBUST
(delta = 0.23459, H/tau = 0.10000) both hardened to EXACT rational (B = [I; X],
L = [I - QX, Q] gives LB = I, P^2 = P, P1 = 1 exactly); hiddenness decided NOT-float-only
(exact drifts ~1.3e-11 vs flip radii 6.6e-6 / 8.5e-5); sigma_tilde > tau certified via the
self-coefficient P_55 = 0.727 > tau; 9 Pareto points re-checked, no systematic bias.
W = {0,1,2,3,4} (k = 5 visible), hidden {5,6,7}, nonvertices {8,9}. CONSEQUENCES RECORDED:
(1) ledger item 1 falsified AS STATED -> doc re-scoped (the emptiness question lives
BELOW the corner delta* = 0.0718; both instances satisfy the linear law H <= 2*delta);
(2) via cloning, the RAW-INDEX FLOOR IS REFUTED OUTRIGHT for delta_0 >= 0.233 (doc
status-correction paragraph updated); (3) the quotient floor's first genuine test objects
(quotient Pi/tau ~ 2.5e-4 — thin, but at this delta the floor RHS is vacuous-ish; the
small-delta question is untouched). P(exact antecedent instance exists at delta <= 0.25)
> 0.999999. kernel-conjecture.tex updated + recompiled clean.

# WAVE 19 — launched 2026-06-11 (3 codex provers on the wave-18 synthesis targets)
- w19_tangent: the tangent-cone lemma dH <= C * ddelta at H-M stratum points (n=3 model
  explicit first; numerical tangent-cone decider over sampled strata; curve-selection
  counterexample side). The round's sharpest target (w18 P = 0.68).
- w19_leftcone: the quasi-positive left-fixed-cone extreme-point lemma (extreme points of
  {l : lP = l, l1 = 1, neg(l) <= C*delta} near visible rows) + the duality implication
  chain; vertex-enumeration test on the certified n=7 instance.
- w19_boundary: the boundary-product dichotomy on the quotient (B^m - B = -sum B^r E C'
  exact; fat component OR charged boundary mass) at the anti-splitting frontier; horn
  measurements on the certified antecedent instances.

## w19_boundary (codex) — DIED-AT: the boundary-product dichotomy fails as stated (height cancels)
Full answer: notes/swarm-answers/w19_boundary.md; measurements + both-horns-fail candidate:
experiments/out/w19_boundary/. BANKED (exact, clone-invariant, quotient): B^2 - B = -EC;
B^m - B = -sum_{r<=m-2} B^r EC; tr B - tr B^2 = tr(EC). DIED-AT (boxed): ||(EC)_{alpha,*}||_1
>= c''*tau (or ||EC||_{infty->1} >= c''*tau) for shallow rows carrying high-hidden mass —
the identities only yield the UPPER budget (Q^+)_{vT} <= 4*tau/lambda from v's own negative
budget; it is not a lower bound and H CANCELS from it. Horn measurements on the certified
instances: Pi/tau ~ 1e-4..2.5e-4 AND ||EC||/tau ~ 0.003..0.021 — both horns fail there.
ORCHESTRATOR CAVEAT: those instances are ABOVE-CORNER (delta ~ 0.23), where 4*delta = 0.93
> 0.85*tau = 0.41 — the finisher horn is arithmetically dead at that scale regardless; the
dichotomy's live habitat (small delta) is untested by these objects. Still, "the charge is
a budget, not a bound" is a genuine structural death certificate for the m-identity route
ALONE. P(dichotomy as stated) = 0.18; P(closes anti-splitting) = 0.07. The anti-splitting
frontier now rests on w19_tangent / w19_leftcone (in flight).

## w19_leftcone (codex) — REFUTED AS STATED (exact n=4 family); weak replacement proved
Full answer: notes/swarm-answers/w19_leftcone.md; counterexample + w16 vertex enumeration:
experiments/out/w19_leftcone/. The quasi-positive left-fixed-cone extreme-point lemma is
FALSE: an exact n=4, rank-3 idempotent family with delta = eps has a K_C extreme point
-> (1/2, 1/2, 0, 0) at l1-distance -> 2/3 from the ROW SET (-> 1 from the visible rows) as
eps -> 0. No O(delta) row-proximity holds for left-fixed quasi-positive extreme points.
PROVED replacement (clone-invariant but too weak for the height payoff):
dist_1(l, conv{p_i}) <= (2+4*delta)*neg(l). The w16 n=7 vertex enumeration is consistent
(many K_C vertices far from visible rows). READING: the k-dim fixed-space coordinate
system stands as GEOMETRY (rows still live in it exactly) but supplies no proximity
principle — the left/right duality is NOT where hiddenness pays. Wave-19 scoreboard so
far: boundary DIED-AT (budgets-not-bounds), leftcone REFUTED; the tangent-cone lemma
(w19_tangent, in flight) carries the round.

## w19_tangent (codex) — THE TANGENT-CONE LEMMA: PROVED (claimed), C = 2 DIMENSION-FREE [pending w19_tangent_audit]
Full statement + RECOVERED FULL PROOF NOTE: notes/swarm-answers/w19_tangent.md; decider +
outputs: experiments/out/w19_tangent/. CLAIM: for every H-M normal-form point P_0 and
every variety tangent A (P_0 A + A P_0 = A, A1 = 0), along any exact C^1 arc:
  dot-H+(A) <= 2 * dot-delta(A),   dot-delta(A) = max_i sum_{j: P0_ij=0} (-A_ij)_+,
with C = 2 independent of n, k, partition, mixtures, and minimal block mass — THE
INFINITESIMAL FORM OF THE LINEAR LAW, dimension-free, hiddenness-free, clone-invariant.
Sharp at the recurrent-hull derivative; visible-set changes claimed to only lower
first-order height (the semicontinuity step — the audit's prime target). Decider: 246
strata, zero dangerous-cone (dot-delta = 0) directions, budget-1 max = 2.0 exactly
(matches sharpness). Remaining gap (honest): second-order/curve-selection upgrade through
the exact chart + stratum-boundary handling => the LOCAL linear law near the H-M locus.
P(local route works) = 0.74; P(global all-strata-uniform) = 0.52. AUDIT LAUNCHED
(w19_tangent_audit: re-derivation, the semicontinuity attack, independent decider with
extreme strata, arc-level integration spot check).
ORCHESTRATION LESSON (logged): codex `-o answer.md` OVERWRITES a worker-authored
answer.md in the same workdir — the proof note had to be recovered from the transcript.
Future briefs: instruct workers to write long artifacts to proof.md/verdict.md, never
answer.md.

## w19_tangent_audit (codex, hostile) — THE TANGENT-CONE LEMMA HOLDS WITH REPAIR: BANKED
Full report: notes/swarm-answers/w19_tangent_audit.md + experiments/out/w19_tangent_audit/
(incl. audit_report.md). Independent re-derivation + independent decider re-implementation:
209 strata (incl. extreme tiny-mass geometries), zero dangerous-cone directions,
budget1_max = 2.000000000000002; EXACT ARC integration along the worst LP direction stays
below 2*dot-delta (idempotence residual 1e-16); the w19_leftcone refutation family does
NOT attack this lemma (at its H-M anchor: dot-delta = 1, frozen D = 0). REPAIRS:
(1) SHARPNESS only for the FROZEN recurrent-hull derivative — the n=3 endpoint direction
has frozen D = 2 but ACTUAL H/t = 0 (actual-height sharpness unconfirmed; the lemma's
inequality is what matters). (2) The semicontinuity step: pointwise Dini fine, but NO
uniform local radius over tiny recurrent masses — an explicit TWO-SCALE VISIBILITY LEMMA
is required (made concrete by a finite-scale stress: H/t ~ 2 above a 1e-6 active-entry
scale on a tiny-mass stratum; tail below that scale = 0, so no Dini failure).
P(repaired verdict survives) = 0.82. STATUS: the repaired lemma is PROVED + HOSTILE-
AUDITED at exploration level — the first new proved result of the idempotence-
exploitation programme. WAVE 20 LAUNCHED: w20_curve — T1 the two-scale visibility lemma
(the audit's named gap), T2 the LOCAL linear law near the H-M locus (fixed n; explicit
radius; must explicitly disarm the recorded "naive compactness / W-jump" dead route),
T3 the honest dimension-dependence list + the standing global gap (B-S normal-form
distance — every small-delta idempotent near the locus — NOT claimed).

## w20_curve (codex) — T1 PROVED (two-scale visibility); T2 dies at ONE quadratic estimate [T1 audit in flight]
Full answer + proof note: notes/swarm-answers/w20_curve.md; numerics:
experiments/out/w20_curve/. T1 (the audit-demanded uniformity repair) PROVED: explicit
visibility radius for recurrent masses >= mu; mu -> 0 handled by recoding to the boundary
H-M stratum (two-scale split). T2 (the local linear law) NOT proved — the exact failed
estimate: ||(C,D)_{perp M}||^2 <= L_n * delta (the quadratic normal bound); the chart
gives H <= 2*delta + O(||(C,D)||^2) and nothing kills the quadratic term. NUMERICS
SIGNATURE: worst stable LOCAL ratio H/delta = 2.000000000013 — the local law empirically
holds with EXACTLY the lemma's constant 2 (sharp); the tiny-mass finite-scale transition
at mu ~ 1e-6 reproduced. ORCHESTRATOR DECOMPOSITION (for w21): on the dangerous cone
(dot-delta = 0; audited fact: frozen first-order height D = 0 there) BOTH H and delta are
second-order — the race restarts one order down; the T2 gap IS the second-order
tangent-cone inequality q_H <= C_2 * q_delta (+ finite-jet iteration for doubly-degenerate
directions). LAUNCHED: w20_t1_audit (hostile audit of T1: the recoding step under mixed-
rate degenerations is the prime target; plus the W-jump disarmament assessment) and
w21_second (the second-order lemma + assembly to the local law; decider-first).

## w20_t1_audit (codex, hostile) — T1 HOLDS WITH REPAIR; the recoding step is INVALID as written
Full report: notes/swarm-answers/w20_t1_audit.md + experiments/out/w20_t1_audit/.
BANKED (repaired, AMBIENT — stronger than claimed): fixed-mass visibility — for an H-M
base P0, every recurrent-cluster vertex with LP support margin eta > 0 stays visible
whenever the max-row-l1 distance eps <= min{ mu(P0)/8, tau/64, eta*tau/64, 1/64 }
(uses only row proximity + the support-margin LP; the H-M exposer has exact margin rho/2
via disjoint supports; nonneg repaired by f = (g_s - g_s(p_v)) + (2eps/eta) l_v).
INVALID AS WRITTEN: (a) the mu -> 0 RECODING — dropping several small recurrent
coordinates can put the recoded H-M point ~ n*theta away while surviving min mass is
~ theta: the fixed-mass hypotheses then FAIL by factors 62.7-314 (independent stress
numerics); must be restated via TOTAL MASS REMOVED per block + recode degenerate
transient faces (alpha_is -> 0) too. (b) the claimed arc radius involved tau(t) — a
TARGET-point quantity, not base data; the clean ambient estimate is eps(t) <=
2M e^{2Mt} t (M = row-sum norm of the generator) + a separate lower scale estimate for
tau along the arc. Fixed-mass independent numerics: zero condition-implies-visible
violations (incl. the 1e-6 stress family). P(repaired verdict survives) = 0.74.
STATE: tangent-cone lemma BANKED; T1-fixed-mass BANKED (repaired); OPEN SUB-TASKS:
the mass-removed recoding lemma + the arc-scale estimate; w21_second (the decisive
second-order lemma) still in flight.

## w21_second (codex) — DIED-AT, NO COUNTEREXAMPLE; the frontier converges on BOUNDARY RECODING
Full answer + long form: notes/swarm-answers/w21_second.md; decider stack:
experiments/out/w21_second/. No dangerous-cone direction with q_delta = 0 < q_H exists in
the sampling (no local-law counterexample seed); in the clean fixed-base second-order
window the resolvable samples had max_local_ratio = 0 — the second-order race at a FIXED
H-M base is EMPTY-OR-BENIGN. The raw sharp cases (H/delta = 2.00000000004) are
FINITE-SCALE BOUNDARY RECODING EVENTS (arcs crossing tiny-positive-entry scales), not
fixed-base limits. The failed estimate is unchanged (the quadratic normal projection
bound). CONVERGENT FRONTIER (orchestrator): w20_t1_audit's invalid recoding step and
w21_second's sharp-case localization point at the SAME missing object — a mass-removed
boundary-recoding theory: when an arc kills tiny positive entries (mass theta removed
from a block), recode to the boundary stratum with bookkeeping in TOTAL MASS REMOVED
(not the threshold), tracking how H, delta, tau, and visibility margins transform.
That single lemma would (a) repair T1's mu -> 0 case, (b) resolve the sharp boundary
events in the second-order race, and plausibly (c) close the local linear law by
induction on strata (each recoding strictly reduces the support pattern — finitely many
steps). LAUNCHING: w21_recode.

## w21_recode (codex) — L1+L2 PROVED: the mass-removed recoding lemma [audit in flight]
Full answer + proof note: notes/swarm-answers/w21_recode.md; checks:
experiments/out/w21_recode/. L1: recoded boundary H-M point with ||P0 - P0'||_{infty,1}
<= 2*(sum_s q_s + q') (A = 2; bounds in REMOVED MASS, never the threshold), survivor mass
>= min surviving original mass, survivor shift exactly q_s, face-drop shift 2*r_i. L2: the
honest two-scale uniform visibility assembly (iterate recoding, support pattern strictly
shrinks, <= n steps; ambient fixed-mass lemma at each base; w19 lemma applies at every
recoded base). EVIDENCE: the w20_t1_audit stress family that killed the naive version
(62.7-313x) now PASSES under the removed-mass bounds (eps/(2Q) < 1); 12/12 mixed-rate
degenerations clean; the w21_second sharp boundary events localized to t >> min-entry
windows with fixed-base ratio 0. L3 (the local linear law) NOT assembled — the one
remaining estimate is the finite-jet normal projection bound after all rebasings.
P(L1+L2 survive audit) = 0.78; P(L3 assembles from present ingredients) = 0.34.
AUDIT LAUNCHED (w21_recode_audit: exactness of P0', compounding over iterations
(telescoping vs n-factor), oscillating-arc stopping condition, independent stress re-run).

## w21_recode_audit (codex, hostile) — L1 BANKED; L2 repaired to the FINAL-PROFILE one-shot form
Full report: notes/swarm-answers/w21_recode_audit.md + experiments/out/w21_recode_audit/.
L1 SURVIVES in full: P0' is an EXACT H-M idempotent (re-derived: pi_s' P' = pi_s' via
survivor support; every transient mixture follows); ||P0 - P0'||_{infty,1} <= 2(sum q_s
+ q') CONFIRMED with q' = max_i r_i (max-row norm); validity needs only K_s nonempty,
q_s < 1, r_i < 1 (perturbative reading needs them small); the w20 stress family passes.
L2 BROKEN as a literal stepwise iteration — THE OLD TRAP ONE LEVEL UP: relative removed
masses measured after each renormalization can sum to O(n) while the ORIGINAL removed
mass is O(1) (explicit sequential family overcharges 10.8x at 12 drops). REPAIRED L2
(audited): choose the FINAL boundary profile, measure ALL removed recurrent + transient-
face mass in the ORIGINAL profile (collapse the chain), recompute (mu_m, eta_m, Lambda_m)
at that final stratum, apply the fixed-mass visibility lemma ONCE. No radius depending
only on n or a threshold is justified — the radius depends on the final profile's
surviving data (honest). THE AUDITED CHAIN IS NOW: tangent-cone lemma + ambient
fixed-mass visibility + L1 recoding + L2 (final-profile). ONE estimate remains for the
LOCAL LINEAR LAW: the finite-jet normal projection bound ||(C,D)_{perp M}||^2 <= L *
delta after final-profile rebasing (+ the arc-scale tau(t) estimate where needed).
LAUNCHING w22_jet.

## w22_jet (codex) — J1 REFUTED AS STATED: support-addition arcs; the repair is the STRATIFIED bound
Full answer + long form: notes/swarm-answers/w22_jet.md; counterexample code:
experiments/out/w22_jet/. THE COUNTEREXAMPLE: exact nonnegative H-M SUPPORT-ADDITION arcs
(moving from a boundary stratum into a larger stratum, staying exactly H-M) have delta = 0
to ALL orders but first jet NOT tangent to the fixed stratum — so ||(C,D)_{perp M}||^2 <=
L*delta is FALSE for ANY finite L, already at n = 2, k = 1 (mu = 1, no small masses, no
eta involved, arbitrarily small radius): a dimension-free fixed-stratum estimate is not
unproved but FALSE. HARMLESS FOR THE LAW: along such arcs H = 0 too (they stay in the H-M
family); they break the CHOSEN COORDINATES only. THE REPAIR (worker's option 3 = the
orchestrator's reading): the stratified error bound
  dist_chart((C,D), M_HM)^2 <= L * delta,
distance to the LOCAL delta = 0 LOCUS (finite union of strata through the base), not one
stratum — a Lojasiewicz-type error bound on the variety (re-connecting the w18_quadlit
Luo-Pang lead #1; the numerics' sharp H/delta = 2 says exponent 2 is the truth).
P(local law true after the repair) = 0.78; P(repaired assembly survives audit) = 0.55.
LAUNCHING w23_loj (the stratified bound: prove no third-order-flat transverse direction
exists via the chart second-order algebra; support-addition directions are now INSIDE
the locus and harmless).

## w23_loj (codex) — J1' PROVED + J2' ASSEMBLED: THE LOCAL LINEAR LAW (claimed) [AUDIT IN FLIGHT]
Full answer + proof note: notes/swarm-answers/w23_loj.md; probes:
experiments/out/w23_loj/. CLAIMS: J1' — the stratified bound dist_chart((C,D), M_HM)^2 <=
L * delta against the WHOLE local delta=0 locus (support-addition arcs now give dist = 0;
max sampled dist^2/delta = 0.196; the explicit second-order rigidity jet confirmed
delta/t^2 -> a > 0 for promotion+forbidden-mixing directions). J2' — the LOCAL LINEAR LAW
H <= C_loc * delta, C_loc = 2 + K_vis * L, fixed-n constants, explicit neighborhood of
the H-M locus; assembled from the audited chain (final-profile recode -> fixed-mass
visibility -> tangent-cone lemma + J1' kills the quadratic error). NOT THE GLOBAL LAW:
the B-S normal-form distance gap (is every small-delta idempotent in the neighborhood?)
STANDS. Assembly stress: fixed-base windows max H/delta = 0; ratio-2 cases remain
boundary-transition events (handled by the recode). P(J1') = 0.74; P(J2' survives audit)
= 0.60. AUDIT LAUNCHED (w23_loj_audit; prime targets: the promotable-zeros enumeration
completeness, mixed 2-jets, and the assembly's integration step — a pointwise derivative
bound at one endpoint must not be silently integrated along the arc).

## w23_loj_audit (codex, hostile) — J1' BANKED (mod clarification); THE ASSEMBLY (J2') BROKEN
Full report: notes/swarm-answers/w23_loj_audit.md + experiments/out/w23_loj_audit/.
J1' (the stratified distance-to-locus bound) HOLDS WITH REPAIR/CLARIFICATION: support
additions and mixed promotion/face 2-jets did NOT break it; the promotable-zero
enumeration must explicitly include the INDUCED TRANSIENT-ROW entries. J2' (the local
linear law as assembled) BROKEN: not numerically refuted, but the step H <= 2*delta +
K_vis*r^2 is NOT LICENSED by w19+w20+w21+J1' — the w20 visibility hypotheses FAIL on a
concrete nearest-branch test by factors 12.8 and 128 (the eps-condition does not hold at
the chosen recoded base for the nearest locus point). PROTOCOL NOTE: the hostile audit
caught an invalid landmark claim before it entered the record — the audited chain stands
at: tangent-cone + ambient fixed-mass visibility + L1/L2 recoding + J1' stratified bound;
THE LOCAL-LAW ASSEMBLY IS THE OPEN PIECE (an arc/base-choice construction whose
visibility hypotheses actually hold — possibly choosing the recode profile from the
NEAREST BRANCH rather than the final profile, or a visibility statement at the nearest
locus point itself). The GLOBAL gap (B-S normal-form distance) stands behind it.

# CONSOLIDATION (2026-06-11): OVERVIEW.md + the Theorem 1.12 discovery + merge to main
- **OVERVIEW.md written** (the bird's-eye onboarding doc, this directory): plain-language
  conjectures (formal Kernel Conjecture vs the stronger linear-law working target kept
  explicitly apart), all definitions self-contained (scale-dependent visibility,
  sigma-tilde incl. self-coefficient), the full strategy map 4.1-4.9 with statuses and
  pointers, the frontier box, the do-not-retry list. REVIEWED by two independent codex
  workers: w24_freshread (FAILS-as-drafted: the kernel-vs-linear-law conflation, the
  visibility definition, the O(delta) exponent on op-exposed-hull — ALL FIXED) and
  w24_factcheck (15 findings: 4 ERROR incl. the W-free O(delta) target being REFUTED by
  registry lemma ex-hume — which also explains w18_quadlit's mysterious "Hume" citation;
  3 OVERCLAIM; 4 STALE; 4 NIT — ALL APPLIED). Archived: notes/swarm-answers/w24_*.md.
- **USER DISCOVERY: H-M THEOREM 1.12** (txt ~:2245) — the theorem directly after the
  nonnegative classification is an EXACT structure theorem for arbitrary REAL (signed)
  idempotent matrices with a converse: proportional-row classes C_s (rank-one
  restrictions) + B-rows as linear combinations + exact signed sum rules (1.2)/(1.3)
  (in-class = 1, cross-class = 0) — the signed analogues of the sign-rigid zero-sum
  closures. The campaign NEVER READ IT (autopsies targeted 1.11/1.16/2.2 only).
  w25_hm112 launched: restate, autopsy the proof, derive what near-positivity forces,
  constructive nearest-H-M-point test on the certified instances, bridge to the GLOBAL
  gap. OVERVIEW §4.9 records the lead.
- **Branch merged to main** (fast-forward; main was 0 ahead): the classical-portfolio
  work is now part of the main project per user direction.

## w25_hm112 (codex) — Thm 1.12: THE RIGHT GLOBAL COORDINATES, mod ONE merge/conditioning lemma
Full answer + long form: notes/swarm-answers/w25_hm112.md; numerics:
experiments/out/w25_hm112/. VERDICT: PARTIALLY — P(1.12 route reaches the global W-free
statement) = 0.48, the HIGHEST credence yet on the global gap. Thm 1.12 (txt ~:2245;
restated + loci quoted in the long form) gives an exact global signed parametrization:
proportional classes C_s + B-rows as combinations + the exact sum rules. CANDIDATE
LEMMA CHAIN: L1 stochastic 1.12 coordinates -> L2 CLUSTERED CONDITIONING (merge
near-proportional classes at scale eta — THE missing step) -> L3 signed concentration
from bounded coordinates -> L4 constructive H-M projection (normalize + clip). THE
OBSTRUCTION (explicit small-delta split-block family): exact proportional classes can
SPLIT a limiting recurrent block — B coefficients ~ 1/delta, direct nearest-point stays
at distance 2 while the MERGED H-M point is 2*delta-close. CONVERGENCE: this is the same
nearest-branch/merging phenomenon that broke the w23 assembly — the synthesis is
1.12 global coordinates + the audited recoding/merging theory choosing the stratum +
clip/normalize. Instance checks: w19 leftcone family harmless here (2*delta direct);
w16/w17 (above-corner) warn only about singleton-representative choice (their B
coefficients are already near-convex). P(reading survives audit) = 0.83.
NEXT: the clustered-conditioning lemma (L2) is the single named missing step.

## w26_cluster (codex) — L2 PARTIAL: the rank-conditioned clustered chart [audit in flight]
Full answer + proof note: notes/swarm-answers/w26_cluster.md; verification:
experiments/out/w26_cluster/. LANDED: a clustered 1.12 chart with explicit constants —
clustering scale eta = sqrt(delta), proportionality error F = eta, coefficient bound
A = R(1+R)^{k-1} (R = 1 + 2*delta, k = rank). VERIFIED: kills the split-block 1/delta
blow-up (old coefficient negative mass 500/5000 -> merged max coefficient 1.0, merged
H-M distance 2*delta); leftcone + certified instances behave. HONEST DEFECT: A is
RANK-DEPENDENT (~2^{k-1} at small delta) — the classical twin of the parent project's
Frobenius-vs-order-unit /prop-rank-gap disease; NOT yet the dimension-free L2 the global
route needs. L3 stated precisely in the proof note; remaining gap = a dimension-free
support-margin/concentration estimate. AUDIT LAUNCHED (w26_cluster_audit) with the
DECISIVE EXPERIMENT specified: adversarial chains of k near-proportional classes at
pairwise scale eta to measure whether the (1+R)^{k-1} cascade SATURATES (rank-dependence
real) or stays O(1) (bound loose — improvable to polynomial/constant).

## w26_cluster_audit (codex, hostile) — L2 UPGRADED TO DIMENSION-FREE: A = 1 (max-volume basis)
Full report: notes/swarm-answers/w26_cluster_audit.md + experiments/out/w26_cluster_audit/.
The greedy chart's rank-dependence (A = R(1+R)^{k-1}) was an ARTIFACT: choosing the
representative basis as a MAXIMUM-VOLUME set of actual rows gives A = 1, Lambda <= 1,
E <= R*eta — DIMENSION-FREE. (The classical prop-rank-gap scare dissolves at this step.)
L2 is now proved + audited in the form the global route needs. THE SINGLE REMAINING GAP
of the 1.12 bridge: L3 — the support-concentration estimate (bounded merged coordinates
+ exact sum rules + entries >= -delta => mass outside the eta-pivot clusters is small /
each merged class is near an equal-input block, with dimension-free moduli). L4
(constructive projection) is expected mechanical once L3 exists. LAUNCHING w27_concentration.

## w27_concentration (codex) — L3 DIED-AT, productively: the scale is sqrt(delta), ONE estimate remains
Full answer + proof note: notes/swarm-answers/w27_concentration.md; numerics:
experiments/out/w27_concentration/. PROVED: (a) in-class concentration G1 = eta + 2*delta;
(b) cross-cluster representative leakage <= 2*delta/(1-eta) (+delta in l1). REFUTED:
O(delta) support-concentration — an explicit rank-2 family has representative mass
sqrt(delta) on B_eta at eta = sqrt(delta); the TRUE scale is sqrt(delta) (consistent with
ex-hume and the audited B-S-distance target — the bridge was always going to land at
O(sqrt(delta)) in full distance). THE LAST NAMED ESTIMATE (the whole 1.12 bridge now
hangs on it): max_s sum_{j not in M_s} |P_{u_s j}| <= C*(eta + delta/eta) in the signed
affine-face case (= C*sqrt(delta) at eta = sqrt(delta)). IF IT LANDS: the conditional L4
assembly in the proof note gives the GLOBAL W-free O(sqrt(delta)) H-M distance in
||.||_{infty,1} — the campaign landmark feeding op-exposed-hull -> op-classical.
LAUNCHING w28_face on it.

## w28_face (codex) — DIED-AT: the bridge reduces to the REPRESENTATIVE DISPLACEMENT LEMMA
Full answer + proof note: notes/swarm-answers/w28_face.md; numerics:
experiments/out/w28_face/. Neither proved nor refuted; the named reduction: prove
  sum_j (P_{u_s j})_+ * ||p_j - p_{u_s}||_1 <= C_D * delta
(the representative's positive mass, transport-weighted, is O(delta)); then the face
estimate (and hence the conditional L4 assembly = the GLOBAL W-free O(sqrt(delta))
theorem) follows by Markov over rows outside M_s. Numerics strongly support the lemma.
ORCHESTRATOR IDENTITY (hand to the prover): the VECTOR version is exact and free —
idempotence + row sums give sum_j P_{u j}(p_j - p_u) = (P^2)_u - p_u = 0, so the signed
displacement sum VANISHES IDENTICALLY and ||sum_j (P_{uj})_+ (p_j - p_u)||_1 =
||sum_j (P_{uj})_- (p_j - p_u)||_1 <= nu_u * (2 + 4delta) <= 2delta(1+2delta). The whole
difficulty: upgrade the vector cancellation to the SCALAR (no-cancellation) sum — i.e.
exclude a conspiracy where O(sqrt(delta)) positive mass sits at O(1) displacement in
mutually-cancelling directions. The w27 rank-2 saturator (mass sqrt(delta) at
displacement sqrt(delta), scalar sum = delta) is consistent. LAUNCHING w29_displacement.

## w29_displacement (codex) — the displacement lemma: scope delimited; THE CAMPAIGN'S NAMED KERNEL
Full answer + proof note: notes/swarm-answers/w29_displacement.md; numerics:
experiments/out/w29_displacement/. GENERAL-ROW version REFUTED (clean counterexample at
delta = 0 — P(survives audit) = 0.99): the max-volume property of the representative is
LOAD-BEARING. MAX-VOLUME version: DIED-AT (not derivable from the audited tools yet) but
likely TRUE (P = 0.62; 36-sample sweep: T/delta median 2.04, p90 2.88, max 3.57 — bounded).
The Markov handoff is written out: lemma with constant C_D => the w28 face estimate with
C_D + 1 => the w27 conditional L4 assembly => THE GLOBAL W-FREE O(sqrt(delta)) THEOREM.
STATUS: the representative displacement lemma (max-volume form) is the single named open
statement of the classical campaign's best route. WAVE 30 LAUNCHED: w30_telescope (route
R1 — iterated identity / self-improvement T <= a*T + b*delta) and w30_maxvol (mine the
max-volume property directly: Cramer-type coefficient bounds — what does max-volume
FORBID about positive mass at large displacement; the delta=0 counterexample shows
exactly the failure mode the property must exclude — use it as the guide).

## w30_telescope (codex) — DIED-AT: idempotence alone gives NO contraction; the interface fact is named
Full answer + proof note: notes/swarm-answers/w30_telescope.md; numerics:
experiments/out/w30_telescope/. THE EXACT LEAK: in the two-step positive expansion the
identity a*P^+ = P_{u.} + a*P^- + b*P^+ - b*P^- returns T with coefficient EXACTLY 1 —
T <= T + O(delta), no contraction from idempotence alone (a clean structural fact: the
displacement lemma genuinely needs the max-volume input). THE MINIMAL INTERFACE FACT
(precisely posed): sum_j (P_{u_s j})_+ * sum_{t != s} (-beta_t(j))_+ <= C_mu * delta —
the representative's positive mass weighted by the target rows' NEGATIVE coefficient
mass. If it lands: C_D = 2(1+2*delta_0)(2 + C_mu) and the displacement lemma follows.
This is exactly w30_maxvol's territory (negative coefficients vs maximality) — awaiting
its verdict; if its died-at dovetails, the combined prover takes the interface fact as
the single target.
