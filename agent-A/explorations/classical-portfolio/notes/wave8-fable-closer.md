<!--
ROLE: wave-8 CLOSER pass on the sigma_v-wall lemma (the single terminal open of HLC).
Agent: Fable 5 (1M), exploration lane only. Date: 2026-06-10/11.
PROTOCOL: written incrementally, section by section, each stage lands before the next begins.
Inputs: wave5-sigma-wall-parallel.md (dossier, waves 5-7 + d10/d11), d11-scale-disambiguation.md,
d10-certificate-mining.md, d9-dual-certificates.md, wave4/audit-summary.md, fable-hlc-attack.md,
mrp-decider-report.md, endgame-sigma-wall-residual.md, experiments/d1_infra.py (the LP definitions).
Tags: [PROVED] (full proof in this file) / [PROVED-mod] (proof modulo named routine step) /
[CONDITIONAL] / [NUMERICAL] / [GUESS] / [DEAD].
-->

# Wave 8 — closer pass on the σ_v-wall lemma

## Stage 0 — Assembled state (my understanding of the mechanism, ≤1 page)

**Frame (canonical, from the dossier + d1_infra.py).** P n×n real, P1 = 1, P² = P exact,
neg(p_i) ≤ δ per row, τ = √δ, ρ = 4τ, κ = τ/4. Rows are self-indexed coefficient vectors:
p_i = Σ_k P_ik p_k with coefficient-of-row-k = entry-at-site-k. (ρ,κ)-exposedness of row i
(d1_infra.exposed_margin, the project's operative definition): ∃ affine h with **0 ≤ h ≤ 1 on
all rows**, h(p_i) = 0, and h ≥ κ on every row ρ-far from p_i; W = exposed row VERTICES
(require_vertex=True). H = max_i dist₁(p_i, conv W); v hidden top vertex; φ = canonical
separator (‖∇φ‖_∞ ≤ 1, sup_{conv W} φ = 0, φ(p_v) = H); deficit g = H − φ(p), g = Pg, g ≥ 0,
g_v = 0, R = osc(g) ≤ H + 2 + 4δ. σ_v = Σ_{k≠v} P⁺_vk (off-own-site positive mass);
carriers A = {k ≠ v : P_vk > 0}, λ_k = P_vk/σ_v.

**What 14 provers established.** Both branches reduce to ONE localization residual: no ρ-far
row may loiter in the top band {g < κR} without paying ~H² negativity (H²-qualified form; the
literal T_far = ∅ is FALSE by d10 PROBE 1). The belt alone is insufficient (saturation stress
test); row exactness at the blocker is insufficient (no-gain lemma); the canonical-g energy
route is provably capped (anti-lemma); raw-Λ arguments are gauge-garbage. The d11 measurement:
at the collapse edge the binding C10 blocker is the financier f which is simultaneously v's top
carrier, with self-coupling μ_f λ_f P⁺_ff ≳ τ and min aggregate coupling M ≥ 1.07τ; on the d8
family g_f = H = 2δ identically (budget line), and g_f/(κ·osc) hits 1.000 exactly at the wall.

**My read of the mechanism (formed during Stage 0, to be tested below).** Three observations
organize everything:

1. **The financier identity g_f = H is F-ND in disguise.** The measured d8 financier has
   P_ff ≈ 1.04 ≥ 1 (off-own-site ℓ¹ mass ≈ 1.4δ): it is an extreme near-delta row at a
   PRIVATE site. A near-delta row's site-max relative is forced into W (no ρ-far row can match
   a concentrated site pattern — the F-ND margin computation), so a near-delta row sits within
   O(t+δ) of conv W, hence its deficit is ≥ H − O(t+δ). That is the analytic origin of the
   "financier/separator identity": deep-ness is forced by site-privacy + concentration, NOT by
   a new exactness identity. (Formalized + proved as ND′ in Stage 2; numerically tested in
   Stage 2b.)
2. **The exposedness dual is an EXACT affine identity, and pairing it with coordinate masses
   forces supply.** With the project's [0,1]-normalized exposer class the failed-exposedness
   witness is Σ_F μ_b p_b + Σ_k α_k p_k = Σ_k β_k p_k + γ p_v, Σμ = 1, Σβ = B < κ,
   γ = 1 + A − B (A = Σα), with complementary slackness putting α inside v's ρ-ball (when the
   margin t* > 0) and β on the h* = 1 face. Pairing with φ gives the C10-exchange
   (witness g-cost ≤ BR < κR); pairing with 1_S for S = supp⁺(p_v) forces the far witness rows
   to be S-full up to a leak of A·δ — the α-loophole reappears as a SINGLE scalar leak term.
3. **The shallow half of the measured witness rides on δ-thin / non-vertex far top-band rows**
   (the d8 frame-group dirs ≈ midpoints of supplier pairs). These owe nothing to W
   (require_vertex) and cost nothing in the exchange (g ≈ 0). THIS — not the financier — is
   the load-bearing loophole: depth can be forced (via ND′) only on concentrated rows at
   private sites; mixture-like rows at shared sites escape every site argument. Whether
   exactness P² = P globally forbids an ALL-shallow witness (all witness mass on such rows)
   is, I believe, the irreducible core. Stage 2 attacks exactly this; Stage 2b measures the
   witness anatomy on a rebuilt verified d8 edge instance.

**Plan.** Stage 1: formalize the LP/dual and the self-coupling lemma candidate with explicit
quantifiers. Stage 2: prove the new facts (witness identity + exchange + supply-forcing +
return-flow + ND′ + far-row coefficient cap + the coupling), assemble, and locate the exact
failing inequality. Stage 2b: numerics on a rebuilt d8 edge instance (small checks only).
Stage 3: conditional assembly with explicit constants + the definitive obstruction map.
Stage 4: adversarial self-review.

---
## Stage 1 — Formalization: the LP, its exact dual, and the lemma candidates

### 1.1 The exposedness LP and its dual (the project's operative definition, d1_infra.exposed_margin)

For a row index v with far set F := {j ≠ v : ‖p_j − p_v‖₁ ≥ ρ} (F ≠ ∅, else exposed vacuously):

  t*(v) := max { t : h affine, 0 ≤ h(p_k) ≤ 1 ∀k, h(p_v) = 0, h(p_j) ≥ t ∀j ∈ F }.

v is (ρ,κ)-exposed iff t* ≥ κ; **hidden ⟺ t* < κ**; t* ∈ [0,1] (h ≡ 0 feasible). LP duality
(finite LP, both sides feasible-bounded, strong duality exact) gives multipliers
μ_j ≥ 0 (j ∈ F), α_k ≥ 0, β_k ≥ 0 (k = 1..n), γ ∈ ℝ with

  (♦)  Σ_{j∈F} μ_j p_j + Σ_k α_k p_k  =  Σ_k β_k p_k + γ p_v        (vector identity),
  (♦m) Σμ = 1,  1 + A − B = γ   where A := Σα, B := Σβ,
  (♦o) t* = B  at the dual optimum.

So: **hidden ⟺ ∃ witness (♦) with B < κ.** WLOG α_v = 0 (absorb into γ). Complementary
slackness at the optimum, with h* the optimal exposer:
  α_k > 0 ⇒ h*(p_k) = 0;  β_k > 0 ⇒ h*(p_k) = 1;  μ_j > 0 ⇒ h*(p_j) = t*.
**α-localization:** if t* > 0 then h*(p_j) ≥ t* > 0 on F, so α_j = 0 for j ∈ F: α lives on
the open ρ-ball of v. (Flag: the degenerate edge t* = 0 must be carried as a separate case;
there α may sit on far rows.)

Since every p_x is itself an affine combination of the p_k (rows of the flat), any AFFINE ψ
pairs exactly with (♦)+(♦m):

  (E)  Σ_{j∈F} μ_j ψ(p_j) + Σ_k α_k ψ(p_k) = Σ_k β_k ψ(p_k) + γ ψ(p_v).

Three instances used below: ψ = g (the canonical deficit, affine: g(x) = H − φ(x));
ψ = x(S) := Σ_{w∈S} x_w (site-set masses); ψ = x_w (single coordinates).

### 1.2 Standing constants

τ = √δ, ρ = 4τ, κ = τ/4, diam₁ ≤ 2+4δ, R = osc(g) = max g ≤ H + 2 + 4δ (g ≥ 0, g_v = 0),
entries of any row lie in [−δ, 1+δ], ‖p_i‖₁ ≤ 1+2δ, σ_v = Σ_{k≠v}P⁺_vk, ν_i = neg(p_i) ≤ δ,
o_x := ‖p_x‖₁ − P_xx = off-own-site ℓ¹ mass (= σ_x + ν_x when P_xx ≥ 0), carriers
A_v = {k≠v : P_vk > 0}, λ_k = P_vk/σ_v. Small-parameter regime δ ≤ δ₀, τ ≤ τ₀ (explicit
where load-bearing; think δ → 0, H ∈ [cτ, ρ]).

### 1.3 The self-coupling lemma candidate, made precise

The d11 measurement (M ≥ 1.07τ, 76–94% from μ_f λ_f P⁺_ff) and the d10/d11 financier law
(g_f = H on the family; δ = g_f/2) must be split into the parts that are THEOREMS about every
exact P and the parts that are family geometry. The precise candidates:

> **(SC1, transpose-coupling — PROVABLE, §2.6).** For a hidden v with witness (♦) and
> S := supp⁺(p_v): the far witness rows lean on v's carrier system,
> Σ_{j∈F} μ_j Σ_{k∈A_v∪{v}} P_jk ≥ s_min − (leak), s_min := ρ/(2+4δ) − 2δ ≈ 1.9τ,
> conditional on the A-dichotomy (leak = A₀δ + κ(1+2δ) + θ-slack, §2.5).

> **(SC2, deep-witness mass forcing = DMF — THE CORE, open).** ∃ universal m* ∈ (0,1],
> C_D, δ₀: for every exact P with δ ≤ δ₀ and every hidden top vertex v, every optimal
> witness satisfies Σ{μ_j : g_j ≥ H − C_D·max(δ/σ_v, δR)·(1/1) − [slack]} ≥ m*. (Operative
> slack target: depth H − E with E = O(τ²/σ_v + σ_v·0); see §3 for what each branch needs.)

> **(SC3, the financier identity g_f = H — NOT a general theorem).** It is the conjunction
> of: f near-delta at a private site (family design) + ND′ (§2.4, new, proved). The general
> content is ND′; "g_f = H" itself must NOT be targeted (the d11 warning stands).

What must be shown about (μ_f, λ_f, P_ff): nothing about the PRODUCT is both provable and
sufficient (the product bound M ≥ cτ follows from SC1-type supply but provably cannot lift
g_f — §2.7); the load-bearing content is the DEPTH of the rows carrying μ-mass (SC2), and
depth is exactly what the diagonal identity at f does NOT control (§2.7: the no-gain
phenomenon survives the diagonal identity). This is established rigorously below.

### 1.4 Targets restated (what Stage 3 will assemble)

Branch A (σ_v ≤ 1/2): H ≤ B_A σ_v τ. Branch B (σ_v ≥ 1/2, H > B_B τ ⇒ exposed/cluster).
Glue (endgame note): a = min(4/B_A², 1/B_B²). The H²-qualified intermediate: far top-band
occupancy costs ~H² negativity.

---
## Stage 2 — New facts, with proofs

Throughout: v hidden top vertex, witness (♦) with B = t* < κ, S := supp⁺(p_v) (sites of v's
positive entries; i_v ∈ S iff P_vv > 0 — assume P_vv ≥ 0, else σ_v > 1 and v is in the
extreme Branch-B regime where P_vv plays no role; the proofs below never divide by P_vv).

### 2.1 [PROVED] W2 — the sharp exchange

> Σ_{j∈F} μ_j g_j + Σ_k α_k g_k = Σ_k β_k g_k ≤ B·R = t*·R < κR.

Proof. (E) with ψ = g, using γ g_v = 0 and 0 ≤ g ≤ R. ∎
All three terms on the left are ≥ 0; in particular the μ-average of g over the witness's far
rows is < κR, and α-mass on {g ≥ s} is < κR/s. (This recovers A2's C10-exchange in the
project's exact dual normalization; the bound is B·R with B = t*, which is SHARPER than κR
when the hiding is comfortable, t* ≪ κ. This sharpening is load-bearing in §3.)

### 2.2 [PROVED] W3 — witness residual identities (recorded for future provers)

Let c ∈ ℝⁿ be the signed index measure of (♦): c := Σ_j μ_j e_j + Σ_k α_k e_k − Σ_k β_k e_k
− γ e_v, so cᵀP_rows := Σ_x c_x p_x = 0 and cᵀ1 = 0. Then c′ := Pᵀc also satisfies both
(Σ_x c′_x p_x = Σ_x c_x (Σ_k P_xk p_k) = Σ_x c_x p_x = 0; 1ᵀc′ = (P1)ᵀc = 1ᵀc = 0): the
witness can be PUSHED THROUGH P, at the cost of losing sign structure (entries of Pᵀc are
signed). Any future "substitute the blockers by their own representations" argument lives
here; the sign loss is why it has never closed (recorded as a warning, not a result).

### 2.3 [PROVED] RF — the return-flow lemma (diagonal exactness at v)

> Σ_{k≠v} P⁺_vk P⁺_kv ≥ P_vv(1−P_vv) − (1+δ)δ − σ_v δ ≥ σ_v(1−σ_v) − 3.1δ  (δ ≤ 0.1).

Proof. Diagonal of P² = P at v: P_vv = Σ_k P_vk P_kv ⇒ P_vv(1−P_vv) = Σ_{k≠v} P_vk P_kv.
Split the RHS by signs. Terms with P_vk < 0: their total magnitude is ≤ ν_v·max_k|P_kv| ≤
δ(1+δ) (entries ≤ 1+δ in absolute value: a negative entry is ≥ −δ, a positive one ≤ 1+δ).
Terms with P_vk > 0, P_kv < 0: each |P_kv| ≤ δ (single negative entry of row k), total ≤
σ_v δ. Hence Σ_{k≠v}P⁺_vk P⁺_kv ≥ P_vv(1−P_vv) − δ(1+δ) − σ_v δ. With P_vv = 1 − σ_v + ν_v
and ν_v ∈ [0,δ]: P_vv(1−P_vv) = (1−σ_v+ν)(σ_v−ν) ≥ σ_v(1−σ_v) − δ (check both signs of the
ν-derivative; |∂/∂ν| ≤ 1 on the range). Total slack ≤ δ(2+δ+σ_v) ≤ 3.1δ for σ_v ≤ 1+δ,
δ ≤ 0.1. ∎

In λ-terms: Σ_{k∈A_v} λ_k P⁺_kv ≥ (1−σ_v) − 3.1δ/σ_v. **The carriers collectively return
≈ (1−σ_v) of positive column mass to v.** This is the reciprocal-carrier structure as a
THEOREM — but note what it does and does not say: it forces the carriers to LEAN ON v
(coefficient on row v), and leaning on v is FREE in the g-budget (g_v = 0). It contributes
no depth. (Its real use: Branch-A site-supply accounting, §2.8.)

### 2.4 [PROVED] ND′ — near-delta depth (the analytic content of the financier identity)

> Let x be any row with own-site entry a_x := P_xx ≥ 1 − t where t ≤ t₀ := ρ/2 − κ(1+2δ) − 2δ
> (= 2τ − τ/4 − O(τδ) ≥ 1.7τ for δ ≤ 0.05). Then there is a W-vertex w with
> ‖p_x − p_w‖₁ ≤ 3t + 5δ; consequently dist₁(p_x, conv W) ≤ 3t + 5δ and
>   **g_x ≥ H − 3t − 5δ.**
> Equivalently, via a_x ≥ 1 − o_x: every row with off-own-site ℓ¹ mass o_x ≤ t₀ has
> g_x ≥ H − 3o_x − 5δ. Contrapositive (top-band spread-out forcing): a top-band row
> (g < κR) has o > (H − κR − 5δ)/3 — top-band rows must be SPREAD at scale (H−κR)/3.

Proof. Let i = x's site, M := max_k P_ki ≥ a_x ≥ 1−t, attained on the nonempty face
F_M := (conv rows) ∩ {y_i = M} (a face since y_i ≤ M on all rows). F_M is compact, so it has
an extreme point w; an extreme point of a face is extreme in conv(rows), and extreme points
of conv(rows) are rows; hence w is a ROW VERTEX with P_wi = M.
 w is (ρ,κ)-exposed: take h(y) := (M − y_i)/Z, Z := M + δ ≤ 1 + 2δ. Then h is affine;
h(p_k) = (M − P_ki)/Z ∈ [0, (M+δ)/Z] = [0,1] for all k (entries ≥ −δ); h(p_w) = 0. For q
ρ-far from w: if P_qi < 0 then h(q) ≥ M/Z ≥ (1−t)/(1+2δ) ≫ κ. If P_qi ≥ 0:
ρ ≤ ‖p_q − p_w‖₁ ≤ (M − P_qi) + offmass(q) + offmass(w) ≤ (M−P_qi) + (1+2δ−P_qi) + (1+2δ−M)
= 2(M−P_qi) + 2(1−M) + 4δ ≤ 2(M−P_qi) + 2t + 4δ, using offmass(y) = ‖p_y‖₁ − y_i ≤ 1+2δ−y_i
and 1−M ≤ t. So h(q) = (M−P_qi)/Z ≥ (ρ − 2t − 4δ)/(2Z) ≥ κ by the definition of t₀. Hence
w ∈ W (an exposed row vertex).
 Distance: ‖p_x − p_w‖₁ ≤ (M − a_x) + offmass(x) + offmass(w) ≤ (t+δ) + (t+2δ) + (t+2δ)
= 3t + 5δ (M ≤ 1+δ ⇒ M − a_x ≤ t+δ; offmass(x) ≤ 1+2δ−a_x ≤ t+2δ; offmass(w) ≤ 1+2δ−M ≤
t+2δ). Finally φ(p_x) ≤ φ(p_w) + ‖p_x−p_w‖₁ ≤ 0 + 3t+5δ (φ 1-Lipschitz-ℓ¹, ≤ 0 on conv W),
so g_x = H − φ(p_x) ≥ H − 3t − 5δ. ∎

Two corollaries.
 **(ND′-a, weak Branch A — unconditional.)** Apply to x = v (g_v = 0): either
 o_v > t₀ (so σ_v ≥ t₀ − δ ≈ 1.7τ), or H ≤ 3o_v + 5δ ≤ 3σ_v + 8δ. In particular
 **σ_v < 1.7τ ⇒ H ≤ 3σ_v + 8δ.** (Same content class as audited F-ND, σ_v-form, with my
 constants; F-ND's audited version remains the bankable one — this is a consistency check
 that also fixes the constants used downstream.)
 **(ND′-b, the financier explained.)** The measured d8 financier (P_ff ≈ 1.04, o_f ≈ 1.4δ)
 satisfies g_f ≥ H − 3o_f − 5δ = H − O(δ), and f ∈ (3o_f+5δ)-neighborhood of W. The
 "financier/separator identity g_f = H" [d10/d11, NUMERICAL] is therefore ND′ + the family's
 site-privacy, NOT a new exactness identity. SC3 settled.
 **Vacuity warning (honest):** on the d8 budget line H = 2δ, the slack 5δ exceeds H: ND′ is
 VACUOUS exactly on the extremal family at finite δ. It bites only in the small-δ regime
 H ≍ τ ≫ δ — which is the regime the σ_v-wall lemma actually needs (H > B·τ ≫ δ). All
 chains below are therefore asymptotic statements (δ ≤ δ₀), as the targets permit.

### 2.5 [PROVED] SF — supply-forcing with the A-dichotomy (the α-loophole as one scalar)

> Pairing (E) with ψ = x(S), S = supp⁺(p_v), p_v(S) = 1 + ν_v, and −δ ≤ p_k(S) ≤ 1+δ ∀k:
>  **Σ_{j∈F} μ_j p_j(S) ≥ 1 − Aδ − B(1+2δ) > 1 − Aδ − κ(1+2δ).**
> Hence (Markov, p_j(S) ≤ 1+δ): for θ > 0, the μ-mass on far rows with p_j(S) ≤ 1−θ is
> ≤ (Aδ + κ(1+2δ) + δ)/θ.
> **A-dichotomy:** for any A₀ > 0, either A ≤ A₀ (and the leak is ≤ A₀δ), or A > A₀ and
>  dist₁(p_v, conv{p_k : α_k > 0}) ≤ (1+κ)(2+4δ)/A ≤ 2.4/A₀,
> where (t* > 0) the α-support lies in the open ρ-ball of v: **either supply-forcing holds
> with leak A₀δ, or v has a (2.4/A₀)-shadow inside its own ρ-ball.**

Proof. From (E): Σμ_j p_j(S) = γ(1+ν_v) + Σβ_k p_k(S) − Σα_k p_k(S) ≥ (1+A−B)(1+ν_v) − Bδ
− A(1+δ) = (1+ν_v) + A(ν_v−δ) − B(1+ν_v+δ) ≥ 1 − Aδ − B(1+2δ). Markov as stated. For the
dichotomy: let c := Σα_k p_k / A ∈ conv(α-rows). From (♦), γ(p_v − c) = Σμ_j(p_j − c)
− Σβ_k(p_k − c) (using γ − A = 1 − B), so γ‖p_v − c‖₁ ≤ (1 + B)·diam₁ ≤ (1+κ)(2+4δ), and
γ = 1 + A − B ≥ A. α-rows are in the ρ-ball by §1.1 (t* > 0). ∎

Remark (why this matters): this converts the C10 "uncontrolled α on the high zero-face" —
the death point of A2, B, PC, and w7 — into a SINGLE scalar dichotomy. The price: the two
branches do not currently MEET (supply needs A₀ ≲ κ/δ = 1/τ; a ρ/2-shadow needs A₀ ≳ 1.2/τ;
the window A ∈ (κ/δ·…, 1.2/τ) is uncovered at the constants' face value — see the honest
accounting in §3.3). At δ → 0 with H ≍ τ the gap is a factor ≈ 5 in A₀, i.e. a constants
battle, not a scaling battle.

### 2.6 [PROVED, conditional on the SF branch] FC + CPL — far-row coefficient cap and the transpose-coupling

> **(FC)** Every ρ-far row j satisfies P_j,v ≤ 1 − s_min with s_min := ρ/(2+4δ) − 2δ
> (≥ 1.9τ − O(τδ+δ)): a far row's coefficient on row v is capped; equivalently its off-v
> coefficient mass s_j := 1 − P_jv ≥ s_min.

Proof. p_j − p_v = Σ_k P_jk(p_k − p_v) (subtract p_v = (Σ_k P_jk)p_v from the row identity);
the k=v term vanishes, so ρ ≤ ‖p_j − p_v‖₁ ≤ Σ_{k≠v}|P_jk|·diam₁ ≤ (s_j + 2ν_j)(2+4δ),
where Σ_{k≠v}|P_jk| = s_j + 2(off-v negative mass) ≤ s_j + 2δ. Rearrange. ∎

> **(CPL, transpose-coupling = SC1)** If a far row j has p_j(S) ≥ 1 − θ then its coefficient
> mass on the CARRIERS is p_j(A_v) ≥ s_min − θ. Combined with SF (branch A ≤ A₀):
>  Σ_{j∈F} μ_j p_j(A_v) ≥ s_min − A₀δ − κ(1+2δ) − δ ≈ 1.9τ − leak.

Proof. p_j(S) = P_j,iv + p_j(A_v) ≤ (1 − s_min) + p_j(A_v) by FC (note P_j,iv ≤ P_jv-entry
= coefficient on row v... here i_v is v's own site, and the entry at i_v IS the coefficient
on row v by self-indexing). Then μ-average via SF. ∎

This proves the wave-7 coupling target in TRANSPOSED form (blockers lean on carriers; d11's
M is carriers leaning on blockers — by w7's column-shadow lemma the λ-weighted version
Σ_j λ_j P_jb = P_vb + O(δ/σ_v) ties the two through v's direct coefficients on blockers).
Magnitude matches d11's measured M ≥ 1.07τ ≈ s_min/2.

### 2.7 [PROVED] NG′ — the no-gain phenomenon SURVIVES the diagonal identity (negative result, sharp)

The mandated "untapped resource" was column/diagonal exactness at the blocker f:
P_ff = Σ_k P_fk P_kf. I record precisely why it cannot force depth, so no future prover
re-walks it:
 (i) P_ff(1−P_ff) = Σ_{k≠f}P_fk P_kf as in §2.3. If f is near-delta (P_ff ≈ 1) BOTH sides
 ≈ 0: the identity is VACUOUS exactly in the regime where the d8 financier lives; the depth
 of a near-delta f comes from ND′ (exposedness geometry), not from the diagonal.
 (ii) If f is spread (P_ff bounded away from 0 and 1), the identity forces return flow
 Σ_{k≠f}P⁺_fkP⁺_kf ≈ P_ff(1−P_ff) — a constraint linking f's row to f's COLUMN. But both the
 row side (F-GB at f: Σ_k P⁺_fk g_k ≤ g_f + δR) and the column side (who leans on f) are
 g-cost-free when the partners are top-band rows, and partners CAN be top-band rows: leaning
 on {g ≈ 0} rows costs nothing, receiving from {g ≈ 0} rows costs nothing. The identity
 contains neither H nor σ_v nor κ. Formally: for any ε > 0 the constraint set
 {P_ff(1−P_ff) = Σ_{k≠f}P_fkP_kf, F-GB at f, g_f < ε} is consistent with the rest of the
 belt at any H (the w6refute templates already exhibit exact instances with spread top-band
 far rows at every H/τ ≤ 0.53 — d10 PROBE 1's robust far-top-band occupancy is the measured
 form). [This sharpens w6fin's no-gain lemma to cover the diagonal/column identity at f.]
 **Conclusion: depth-forcing cannot come from any single-row exactness identity at the
 blocker. It must come from the exposedness geometry (as in ND′) or from a genuinely global
 principle (§3.4).** The prompt's designated chase, taken literally, dead-ends here; what
 survives of it is ND′ (depth via concentration + site-max extraction) and RF/CPL (coupling
 without depth).

### 2.8 [PROVED] MC — margin cap from far carriers (new, small but real)

> Let θ_far := Σ{λ_k : k ∈ A_v, ‖p_k − p_v‖₁ ≥ ρ} (λ-fraction of ρ-far carriers). Then
>  t* ≤ ν_v/(σ_v θ_far) ≤ δ/(σ_v θ_far).

Proof. 0 = h*(p_v) = Σ_k P_vk h*(p_k) ≥ σ_v θ_far t* − ν_v·1, since h* ≥ 0 everywhere,
h* ≥ t* on far rows, and h* ≤ 1. ∎

Consequence shape: configurations whose carriers are substantially far (θ_far = Ω(1), as in
the d8 family where the suppliers are far) have t* = O(δ/σ_v); then the exchange (§2.1)
reads Σμ_j g_j ≤ t*R = O(δR/σ_v) — the LINEAR budget law δ ≳ σ_v·(witness depth) appears
analytically (cf. d10's measured δ_min = g_f/2). If instead θ_far ≈ 0, v's positive mass
reproduces it from inside its own ρ-ball: by the sharp shadow (split far/near carriers)
dist₁(p_v, conv(ball rows)) ≤ 2.2(θ_far + ν_v/σ_v) + (renormalization) — the cluster-shadow
case. **This is a θ-dichotomy: linear budget law vs. cluster degeneracy.** (Constants in
§3.2.)

---
## Stage 2b — Numerics: the witness anatomy on the TRUE edge instance (decisive)

Setup: rebuilt the optimizer-backed d8/d9/d11 wall-edge instance from the repo's own
infrastructure (`d8_opt.decide_opt(d=0.1435, sigma_v=0.5, k_groups=2, ell=0.65,
v_own_site=True)`, gurobi alternating LPs, `d8_mrp3.verify` gate): idem_resid = 0,
δ = 0.07175, τ = 0.26786, H = 0.14350, H/τ = 0.53572, v-margin = 0.99972κ, entry_pass —
**identical to the d9/d10/d11 edge to all printed digits.** Then: canonical separator φ via
LP (H(φ) = dist = 0.1435 ✓, ‖Pg−g‖∞ = 3e−17 ✓, R = osc g = 2.1435), the exposedness-LP dual
for v extracted from HiGHS marginals (presolve off), identity residual of (♦) = 1e−16,
B = t* to 15 digits, mass balance 1+A−B = γ ✓. Script: experiments/w8_witness_check.py (uses only
repo infra + scipy; reproducible by rerunning decide_opt as above). [NUMERICAL, gated]

**Finding N1 — the optimal witness IS v's own row identity.** At the edge: A = 0 (NO α at
all); μ is supported on exactly v's positive carriers {2,3,4,5,6,7,10} with
μ_k = P⁺_vk/(1+ν_v) to 4+ digits (e.g. μ_10 = 0.46653 = 0.5/1.07175; μ_2 = 0.21225 =
0.2275/1.07175); β = P⁻_v/(1+ν_v) on rows {1,16}; γ = 1/(1+ν_v) = 0.93305; and
  **t* = B = ν_v/(1+ν_v) = 0.07175/1.07175 = 0.0669466 (matches the LP t* to 6+ digits).**
Cross-checked against ALL d9 budget cells: ν_v = δ at each edge, and ν/(1+ν)/κ reproduces
d9's recorded v-margins to ALL PRINTED DIGITS (σ_v = 0.05: 0.0999375390381012 ≡ d9;
0.10: 0.2034318577136559 ≡; 0.20: 0.4167996737356439 ≡; 0.35: 0.7461372588698685 ≡ d9's
0.7461372588698684). The d9 "linear law t*/κ = σ_v/0.5" is the family parametrization of
the EXACT law t* = ν_v/(1+ν_v).

**Finding N2 — every witness row is a W-VERTEX at deficit exactly H.** All seven μ-rows are
vertices, all in W, all with g = 0.14350 = H exactly (they sit ON the separator's zero
level: φ = 0), all with o = 0 (frame dirs: exact delta rows), p(S) = 1, p(A_v) = 1. Deep
witness mass μ{g ≥ H − E} = 1.0000 at E = 0. **DMF holds at the extremum with m* = 1,
E = 0 — exactly saturated.** The exchange reads H·1 = Σμ_j g_j = B·R = 0.14350 vs
κR = 0.14354: saturated to 3·10⁻⁴ relative.

**Finding N3 — the "financier" demystified (and a definitional catch).** Row 10
(frame-financing#6, the d9/d11 financier, μ_f = 0.4665, λ_f ≈ 0.47) is **v's own private
pillar frame dir** (v_own_site=True): P_v,10 = 0.5 = the design's (1−σ_v^design). The d8
family's v has ZERO self-coefficient (P_vv = 0); its formal off-own-site mass is
σ_v^formal = 1.0717, NOT the design σ_v = 0.5 (the design σ_v counts only supplier mass).
The celebrated reciprocal-carrier self-coupling μ_f λ_f P⁺_ff = 0.4665·0.4665·1 = 0.2177
(75.6% of M = 0.28806, M/τ = 1.07541 — d11 reproduced exactly) is therefore just
γ·P_vf·(P_vf/σ^formal)·1 — **v's squared coefficient on its own pillar.** The d11
"measured mechanism" μ_f λ_f P_ff ≳ τ is an artifact of μ = γP⁺_v: it encodes no constraint
beyond v's row. ⚠ Consequence for the lemma statement: the Branch split "σ_v ≤ 1/2 vs
≥ 1/2" must say WHICH σ_v: on the extremal family the formal off-own-site σ_v ≈ 1 always;
the design σ_v is the supplier mass = v's positive mass on NON-W rows. The robust
branch-split variable is **σ̃_v := v's positive coefficient mass on rows outside conv W**
(σ̃_v = σ_v^design on the family). With σ_v read as off-own-site mass, the d8 family never
leaves Branch B — and the d8 "σ_v-wall law H/τ = min(σ_v, 0.536)" is about σ̃.

**Finding N4 — closed forms for ALL the measured constants [PROVED given N1/N2 shape].**
On the extremal family the hiding condition is t* = ν_v/(1+ν_v) < κ = τ/4 with ν_v = δ = τ²,
i.e. 4τ² < τ(1+τ²) ⟺ τ² − 4τ + 1 > 0 ⟺ **τ < 2−√3**. Hence:
  collapse-edge scale:  τ* = 2−√3 = 0.2679492   (measured 0.267862, grid-limited)
  edge negativity:      δ* = (2−√3)² = 0.0717968 (measured 0.07175; predicted poke
                        d* = 2δ* = 0.1435935 — d9's bisection bracket is [0.1435, 0.144] ✓)
  wall constant:        H/τ|max = 2δ*/τ* = 2(2−√3) = 0.5358984 (measured 0.535724)
  the 3.49 floor:       δ/H² = 1/(4δ*) = **(7+4√3)/4 = 3.4820508** (measured 3.4843)
using H = 2δ on the family (frame-clipping/L4 at v: H ≤ (2+4δ)ν_v; the family realizes 2ν).
**The "0.536 wall" and the "3.49 floor" are a FINITE-δ CORNER, not an asymptotic
obstruction: τ* = 2−√3 is an absolute constant.** On the budget family H/τ = 2τ → 0 as
δ → 0; the family approaches the measured wall/floor only because the minimizer drives δ UP
to the absolute corner δ* ≈ 0.0718. (This also explains why every d3/d7/d8 floor search
landed at the same δ ≈ 0.0718 regardless of design — the floor lives at one absolute point
of (δ, H)-space, namely the corner where κ(δ) overtakes the hiding resource ν = δ.)

**Finding N5 — ND′/F-ND′ honest check.** At this δ (= 0.0718), the ND′ depth bound
H − 3o − 5δ is negative for every row: ND′ is vacuous ON the corner instance, as predicted
in §2.4 (the corner has H = 2δ; all O(δ)-slack lemmas are blind exactly there). No
violations; the lemma's content is asymptotic (δ → 0, H ≍ τ).

**Finding N6 — MC is exactly tight here.** θ_far = 1 (ALL of v's positive carriers are
ρ-far: distances 1.07ρ–1.95ρ), and the MC cap δ/(σθ_far) = 0.066947 = t* exactly. The
margin cap of §2.8 is the equality case of N1.

## Stage 2c — The row-witness lemma and its consequences (new, proved)

### 2c.1 [PROVED] RW — generalized row-witness (subsumes and explains MC, §2.8)

> Let v be any row with self-coefficient a := P_vv ∈ [0,1), off-self positive mass
> σ' := 1 + ν_v − a, and far-positive fraction θ_far := (Σ{P⁺_vk : k ≠ v, ‖p_k−p_v‖₁ ≥ ρ})/σ'.
> If θ_far > 0 then
>   **t*(v) ≤ ν_v / (θ_far · σ') = ν_v / (θ_far (1 + ν_v − P_vv)).**

Proof. Rearrange the row identity: Σ_{k≠v} P⁺_vk p_k = (1−a) p_v + Σ_{k≠v} |P⁻_vk| p_k.
Divide by σ_F := θ_far σ' > 0 and split the positive part into far/near: μ_k := P⁺_vk/σ_F
for far k (μ ∈ Prob(F) ✓), α_k := P⁺_vk/σ_F for near k (α ≥ 0, on the ρ-ball ✓),
β_k := |P⁻_vk|/σ_F ≥ 0, γ := (1−a)/σ_F. This satisfies (♦) and the mass balance
1 + A − B = (σ_F + σ_N − ν)/σ_F = (σ′−ν)/σ_F = (1−a)/σ_F = γ ✓, so it is dual-feasible and
weak duality gives t* ≤ B = ν_v/σ_F. ∎

At the corner instance this is EXACT (N1/N6: the LP's optimal dual equals this witness,
t* = ν/(1+ν) with a = 0, θ_far = 1). RW is the analytic identity behind d9's entire margin
table.

### 2c.2 [PROVED] WL — W-locality (a new belt fact about W itself)

> Every w ∈ W has positive coefficient mass on ρ-far rows ≤ ν_w/κ ≤ 4τ:
>   Σ{P⁺_wk : k ≠ w, ‖p_k − p_w‖₁ ≥ ρ} ≤ ν_w/κ ≤ δ/κ = 4τ.
> **W-vertices are locally financed:** at least 1 − 4τ − 2δ of their coefficient mass
> (self + ρ-ball) is near. Conversely, any VERTEX leaning on far rows with positive mass
> > ν/κ is automatically hidden — exposure is not merely blocked but IMPOSSIBLE for
> far-leaning vertices.

Proof. w ∈ W ⇒ t*(w) ≥ κ; RW gives κ ≤ ν_w/(θσ') ⇒ θσ' ≤ ν_w/κ. (If w has no far rows at
all the far mass is 0.) ∎

Consequences worth recording: (i) hiding-by-itself is FREE for far-carrier vertices — the
hard content of the σ_v-wall lemma can never be "v's exposer succeeds"; it must be a HEIGHT
cap. (ii) The hull-chase has a one-line explanation: a climbing row either leans near
(cluster: height gain bounded by cluster analysis) or leans far (automatically hidden, but
then its position is ν-clipped INTO the far hull: frame-clipping L4 caps its height gain
over its carriers at (2+4δ)ν_v ≤ 2.2δ). **Per-generation height gain ≤ 2.2δ is therefore
unconditional for far-leaning rows** — the budget line H = 2δ of the d8 family is the
single-generation case, 87% of the clipping bound.

### 2c.3 [ANALYSIS, not proved] The ladder: what a counterexample must look like, and where it dies

Since one far-leaning generation gains ≤ 2.2δ of height and is automatically hidden (RW),
the only route to H ≍ τ (the σ_v-wall scale) is a LADDER of L ≈ H/(2.2δ) ≈ 0.25/τ
generations, each hidden, each leaning on the previous. Bookkeeping (exploratory):
generation rows must be ρ-far from the carriers they use while sitting ν-clipped inside
the carriers' hull; consecutive-pair midpoint ladders (a₁,…,a_K spaced ~2ρ; next generation
= ν-poked midpoints, K−1 of them) satisfy every POSITIONAL constraint with K bounded only
by n — positional geometry does NOT cap the ladder (folded ℓ¹ configurations keep all
pairwise distances ≥ 2ρ inside diameter 2). What kills it is SELF-INDEXING: a ladder row's
coefficient vector must EQUAL its position; positions telescope onto base sites unless
intermediate rows carry their own sites, i.e. unless intermediate generations have
self-mass (P_xx > 0) or are mutually-carried in cycles; mutual carrying at δ = 0 forces
equal-input recurrent classes = COINCIDENT rows (B–S normal form), contradicting the 2ρ
spread; self-mass ≥ 1 − t₀ triggers ND′ (deep or near W). The unresolved middle: rows with
self-mass in (≈0, 1−t₀) and partial cycles, at δ > 0 — exactly the quantitative
Baake–Sumner stability gap. At δ = 0 the ladder provably dies (B–S + the §2c.2 dichotomy);
no quantitative modulus is known. [This localizes the open core; it does not prove it.]

---

## Stage 3 — Assembly: what is now proved, what closes conditionally, the obstruction map

### 3.1 The corner theorem (unconditional content extracted from this pass)

> **[PROVED-mod: t*-optimality of RW at the corner is verified numerically to machine
> digits, not proved] The measured wall/floor constants are the finite-δ corner**
>   τ* = 2−√3, δ* = (2−√3)², H/τ ≤ 2(2−√3) = 0.53590 on the budget family,
>   δ/H² ≥ (7+4√3)/4 = 3.48205,
> realized by "v hangs on conv W by its own negativity": H = 2ν_v (frame-clipping, tight to
> 87%), hidden iff RW's bound ν/(1+ν) < κ(δ) ⟺ τ < 2−√3. The family's collapse at d* =
> 2(2−√3)² = 0.143594 lands inside d9's measured bracket [0.1435, 0.144].

Consequence: **the σ_v-wall lemma as numerically calibrated (B_B ≈ 0.536, floor 3.49) is a
statement about an absolute corner of (δ,H)-space, not an asymptotic law.** Any proof
strategy that loses O(δ) slack against H is vacuous at the corner but legitimate for the
asymptotic lemma (δ ≤ δ₀ ≪ δ*); conversely the corner constants CANNOT be recovered by any
argument with slack — they require the exact RW mechanism. This dissolves the "14 provers
died at the same wall" mystery: they were trying to prove a corner-exact constant with
slack-bearing tools.

### 3.2 The conditional assembly (both branches from ONE open inequality + one old wound)

**(DMF — deep-witness mass forcing, the single new core).** ∃ universal m* ∈ (0,1], C_D,
δ₀: for every exact P (δ ≤ δ₀), every hidden top vertex v, every optimal witness:
Σ{μ_j : g_j ≥ H − C_D δ/τ} ≥ m*. [At the corner instance: holds with m* = 1, C_D = 0,
exactly saturated. Supported, not proved.]

**(CEL — cluster-exposure lemma, the old wound, needed only on the near-carrier branch).**
If θ_far < θ₀ then v's ρ-ball cluster contains an exposed vertex or pays ν ≥ c·H².
[Open since d4/d6; both branches of every prior route need it; unchanged here.]

**Theorem (conditional).** DMF + CEL ⇒ the σ_v-wall lemma and HLC, with explicit constants:
 (i) Branch B: hidden v ⇒ m*(H − C_D δ/τ) ≤ Σμ_j g_j ≤ t*·R < κR (exchange §2.1 + DMF), so
   H ≤ κR/m* + C_D δ/τ ⇒ **B_B = R/(4m*) + o(1) → (2+H)/4m*** ; at m* = 1 this is
   B_B = 0.536 — DMF(m*=1) reproduces the measured wall constant EXACTLY (N2/N4), which is
   strong evidence that DMF with m* ≈ 1 is the true mechanism.
 (ii) Branch A (far-carrier case θ_far ≥ θ₀): RW + exchange + DMF give
   ν_v ≥ m* θ₀ σ′ (H − C_Dδ/τ)/R — the LINEAR budget law (the analytic form of d10's
   δ_min = g_f/2). Combined with ND′-a (σ′ ≥ σ_v ≥ (H − 8δ)/3 for any hidden v):
   **δ ≥ ν_v ≥ (m*θ₀/3R)·H²·(1 − o(1))** — the H² law appears unconditionally-shaped,
   a = m*θ₀/(3R) ≈ m*θ₀/6.6.
 (iii) Branch A (near-carrier case θ_far < θ₀): CEL.
Glue: a = min over branches; with m* = 1, θ₀ = 1/2: a ≥ 0.075 universal (vs the corner's
3.48 — the corner is finite-δ, compatible: for δ ≤ δ₀ small the quadratic law is the
binding statement).

### 3.3 Honest accounting of the leaks (where an auditor should push)

- SF's A-dichotomy window: supply-forcing needs A ≤ A₀ with A₀δ ≲ κ (A₀ ≈ 1/τ); the shadow
  branch needs A₀ ≳ 1/τ to give a ρ-scale shadow. The two meet only within a factor ≈ 5:
  uncovered window A ∈ (0.25/τ, 1.2/τ). At the corner instance A = 0 (no α at all), so the
  window is not exercised there; whether optimal witnesses ever need large A is unknown.
- DMF's depth slack C_D δ/τ: at the corner, witness depth is exactly H; on the budget family
  below the edge, the witness rows (W frame dirs) keep g = H exactly — the family suggests
  C_D = 0; a general proof attempt should first try "witness rows are W-rows or pay".
- The t* = 0 degenerate case (α allowed on far rows) is uncovered in §1.1's localization.
- σ̃ vs σ_v (Finding N3): all prior σ_v-statements should be re-read with σ̃ (mass outside
  conv W); the d8 family has formal σ_v ≈ 1 throughout.

### 3.4 The definitive obstruction map (if DMF is attacked next — and it should be)

**Minimal unprovable core: DMF** — equivalently, the exclusion of the ALL-SHALLOW witness:
an optimal witness with ≥ 1−m* of μ-mass on far rows at deficit g < H − E. Everything else
in both branches is now proved around it (§2.1–§2.8, 2c) or reduces to CEL.

Why each available tool fails against the all-shallow witness:
| tool | why it cannot force witness depth |
|---|---|
| F-GB / row exactness at the blocker (w6fin no-gain) | leaning on g≈0 rows is free; contains no H, σ_v |
| diagonal/column exactness at the blocker (§2.7 NG′) | vacuous for near-delta f; H-free for spread f |
| C10-exchange (§2.1) | PRICES depth, cannot CREATE it: all-shallow witnesses pay nothing |
| ND′ (§2.4) | forces depth only on concentrated rows (o ≲ H/3); spread/mixture rows escape |
| F-WR wiggle rigidity | needs a coefficient-closed common-pattern web; witness rows lean downward/outward (graded, not closed) |
| kernel energy F-E | A3's anti-lemma: canonical-g energy ≤ δR², too small |
| RW/MC/WL (§2c) | control the MARGIN and W's structure, not the witness's depth profile |
| SF/CPL (§2.5–2.6) | force S-fullness/coupling of witness rows, but S-full rows can sit at g ≈ 0 |
| substitution through P (§2.2) | sign structure lost (Pᵀc is signed); the d8 witness is already P-stationary (it IS v's row) |

What the all-shallow witness must look like (from §2c.3 + N2): its rows are far, top-band,
and either (a) non-vertices = exact mixtures of top-band rows (descend by Krein–Milman
within the band), or (b) hidden vertices with their own witnesses (recursion does not
reduce: σ̃ ≈ 1 cases recur), or (c) W-vertices — but W-rows have g ≥ H: DEEP, not shallow.
So an all-shallow witness lives entirely on (a)+(b): a self-sustaining hidden web in the
top band. At δ = 0 this web is killed by Baake–Sumner (recurrent classes are equal-input ⇒
coincident ⇒ exposed; transients are non-vertices that descend to recurrent classes ⇒ the
witness descends to W ⇒ deep — contradiction). **DMF is therefore a STABILITY statement:
quantitative Baake–Sumner for the top band: an almost-stochastic almost-idempotent block
whose rows all sit at deficit < κR must contain near-recurrent (equal-input-like) structure
within O(δ/κ) — and near-recurrent clusters expose (this last step is CEL).** The new
mathematics needed: a perturbative structure theorem for almost-idempotent almost-stochastic
matrices with modulus polynomial in δ (NOT spectral-gap-based — no gap is available), e.g.
via the idempotent semigroup/peripheral-spectrum stability literature (Douglas–Ando
quantitative, as flagged in fable §1.1) or a direct fixed-point argument on the
top-band block B = P_TT with ‖B² − B‖ = O(δ/κ) (fable §3.4). That is a self-contained,
well-posed problem — and it is the LAST one.

**Recommendation for the next wave:** (1) attack DMF directly via "optimal witnesses
descend to extreme rows": formalize the Krein–Milman descent (a) and the recursion (b) as
a finite induction over the top band's vertex poset — the only genuinely open step is a
quantitative "descent terminates in O(1) depth" bound; (2) in parallel, test DMF
numerically OFF the d8 family (d3/d7 stacking instances at small δ): measure the witness
depth profile μ{g ≥ H − E}; a single verified all-shallow witness at H ≫ δ would refute
DMF as stated and force the m* < 1 / E > 0 calibration. (3) Re-derive the d8 σ_v-law with
σ̃ and re-state the σ_v-wall lemma in σ̃ form before any af formalization (N3).

### 3.2′ — ADDENDUM (found during self-review): DMF alone implies HLC

The branch machinery is not even needed for HLC itself. Let v be a vertex at the maximal
height H (exists by L2; it is necessarily hidden, since w ∈ W ⇒ dist = 0). DMF + the
exchange (§2.1) give directly
  m*(H − C_D δ/τ) ≤ Σ_j μ_j g_j ≤ t*R < κR = (τ/4)(2+4δ+H),
hence H(1 − τ/(4m*)) ≤ τ(2+4δ)/(4m*) + C_D δ/τ, i.e. H ≤ τ·[(2+4δ)/(4m*) + C_D τ]·(1+o(1)),
and so
  **δ ≥ a·H² with a = (4m*/(2+4δ))²·(1 − o(1)) → 4m*² (as δ → 0).**
At m* = 1: a → 4, compatible with (and within 13% of) the finite-δ corner value 3.482 —
the corner sits at δ* where the o(1) corrections are ≈ maximal, and (4m*/(2+4δ*+H*))² ·
(1−τ*/4)² ≈ 3.4: **DMF(m* = 1) reproduces the entire measured envelope.** The σ_v-resolved
wall law (Branch A's H ≤ B_A σ̃ τ) and CEL are needed only for the sharper σ̃-resolved
statement, not for HLC. **The σ_v-wall residual therefore compresses, finally, to DMF — one
inequality about the depth profile of optimal exposedness-dual witnesses.**

---

## Stage 4 — Adversarial self-review (hostile re-derivation; every claim re-audited)

1. **Dual derivation (§1.1): SURVIVES.** Lagrangian re-derived sign-by-sign; numerically
   confirmed to 1e−16 (identity), 15 digits (B = t*), γ = 1+A−B ✓ on the edge instance.
   Honest gaps: (i) the t* = 0 degenerate case (α may then sit on far rows) is carried as
   an open flag — all localization-dependent results (§2.5 dichotomy's "α in the ball")
   need t* > 0; (ii) "WLOG α_v = 0" is safe: α_v multiplies (p_v − p_v)-type terms — in
   (♦) it shifts γ by α_v on both sides of the mass balance consistently.
2. **Exchange (§2.1): SURVIVES** (affine pairing is exact; 0 ≤ g ≤ R re-checked; equality
   observed numerically: 0.14350 = B·R).
3. **RF (§2.3): SURVIVES**, constants re-checked (entries ∈ [−δ, 1+δ]; the ν-derivative
   step |∂ν[(1−σ+ν)(σ−ν)]| ≤ 1 needs σ ≤ 1+ν ✓ always). Vacuous-but-true for σ_v > 1.
4. **ND′ (§2.4): SURVIVES with two flags.** (i) The face-extraction (extreme point of
   F_M is a row vertex) is standard; under the project's multiplicity-corrected vertex
   test, coincident copies of an extreme point still classify as a vertex — consistent,
   but an af-formalization should cite d3_vertexfix's convention. (ii) If P_xx < 0 the
   statement is vacuous by o_x > 1 > t₀ ✓ no gap. Margin arithmetic re-verified; the
   corner-instance scan shows no violations (and honest vacuity at δ = δ*, N5).
5. **SF (§2.5): SURVIVES as stated**; the A-window (factor ≈ 5 gap between the two
   dichotomy branches) is REAL and stated honestly — SF is NOT closed machinery, it is a
   reduction. At the corner A = 0, so no evidence the window is ever exercised.
6. **FC/CPL (§2.6): SURVIVES**; wording fix: if P_vv = 0 (corner!) then v's site ∉ S and
   p_j(S) = p_j(A_v) — the bound only improves. Verified numerically (μ·p(S) = 1.0).
7. **NG′ (§2.7): SURVIVES** — it is a negative result and matches w6fin + d10 PROBE 1.
8. **RW/WL/MC (§2c.1–2, §2.8): SURVIVE.** RW re-derived; the dual-feasibility of the row
   witness checked against (♦m) algebraically and against the LP numerically (exact at the
   corner). WL's edge case (F = ∅) noted in the proof. MC is the special case of RW.
9. **N4 closed forms: SURVIVE with the stated epistemic split.** PROVED: t* ≤ ν/(1+ν)
   (RW), H ≤ (2+4δ)ν (L4 frame-clipping at v). NUMERICAL (machine-digit, 5 independent d9
   cells + the d-bracket): equality t* = ν/(1+ν) and H = 2δ on the family. The constants
   2−√3, 2(2−√3), (7+4√3)/4 are exact CONSEQUENCES of those two family laws — they are
   "proved modulo the family's t*-optimality", which no slack-bearing tool can certify.
   The match of all four numbers to grid resolution is far beyond coincidence.
10. **Assembly order bug found and fixed:** §3.2(ii) uses σ_v ≥ (H−8δ)/3 from ND′-a, which
   only holds when o_v ≤ t₀; the complementary branch (σ_v ≥ 1.7τ) suffices only AFTER the
   σ-free height cap H ≤ κR/m* + E (3.2′) is applied first (it gives H ≤ 0.6τ/m* ≤ 5.1τ
   for m* ≥ 0.12). With 3.2′ stated, the ordering is sound; (ii) is anyway subsumed by
   3.2′ for HLC purposes.
11. **What I could NOT verify:** (i) DMF off the d8 family (the d3/d7 stacking floor
   instances were not rebuilt — flagged as the decisive next numeric); (ii) the
   t*-optimality of RW beyond the d8 family; (iii) σ̃ vs σ_v re-reading of older notes
   (N3) — wave-1..7 statements quantified over "σ_v" should be audited for which σ is
   meant before banking anything σ-dependent.
12. **Calibration.** P(DMF true, with m* ≥ 1/2, E = O(δ/τ)) ≈ 0.75 (raised from the
   dossier's 0.65–0.83 band: the corner saturates DMF at m* = 1 exactly, and the corner
   constants' closed forms remove the main "unknown mechanism" mass). P(my §2 proofs
   survive a hostile codex audit) ≈ 0.9 (they are short and elementary). P(the corner
   closed forms are exactly right) ≈ 0.95.

## Verdict (one paragraph)

The σ_v-wall lemma is NOT closed in this pass, and it is now clear why no slack-bearing
argument could have closed it at the measured constants: the measured wall H/τ = 0.536 and
floor δ/H² = 3.49 are a FINITE-δ corner with exact values 2(2−√3) and (7+4√3)/4, attained
where v hangs on conv W by its own negativity and hides by the (new, proved) row-witness
bound t* ≤ ν_v/(1+ν_v) until κ(δ) overtakes it at τ = 2−√3. The witness at the extremum is
v's own row identity; its μ-mass sits entirely on W-vertices at deficit exactly H — so the
single remaining open inequality, DMF (optimal witnesses carry m* of their mass at deficit
≥ H − O(δ/τ)), is exactly saturated there, implies all of HLC by a three-line chain
(3.2′, a → 4m*²), and reproduces every measured constant at m* = 1. Banked new and proved:
the exact dual witness identity (♦), the sharp exchange ≤ t*R, return-flow, ND′ (near-delta
depth — the financier identity g_f = H analyticized), supply-forcing with the α-loophole as
a scalar dichotomy, the far-coefficient cap + transpose-coupling (the w7 coupling lemma's
provable half), the row-witness lemma, W-locality, and the demystification of the d11
reciprocal-carrier measurement as v's squared pillar coefficient (plus the σ̃ vs σ_v
definitional catch that all future statements must respect). The obstruction map (§3.4)
shows DMF is a quantitative Baake–Sumner stability statement, true at δ = 0, with every
existing tool failing against exactly one object: the all-shallow witness supported on a
self-sustaining hidden top-band web. Next wave: attack DMF's Krein–Milman descent, and
measure witness depth profiles on the d3/d7 stacking instances at small δ.
