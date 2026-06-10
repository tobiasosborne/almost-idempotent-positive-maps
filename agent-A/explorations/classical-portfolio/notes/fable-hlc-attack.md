# Fable-5 HLC attack (highest-scrutiny pass)

**Date:** 2026-06-10 · **Agent:** Fable 5 (1M), exploration lane only.
**Target (HLC):** ∃ universal A, a > 0: for exact P (P1=1, P²=P, max_i neg(p_i) ≤ δ ≤ δ₀, τ=√δ,
ρ=4τ, κ=τ/4, W = (ρ,κ)-well-exposed row vertices, C=conv W, H=max_i dist₁(p_i,C)):
H ≥ Aρ ⇒ max_i neg(p_i) ≥ a·H² (any exponent p ≤ 2 acceptable). OR refute (exact family, H/τ→∞).

**File protocol:** appended incrementally; each stage lands before the next begins.

---

## Stage 0 — Setup digestion (what I take as given, what I distrust)

Read: ORCHESTRATION.md, W2d (grand assembly + minimal DAG), W2b (hull-chase gap), X1 (one-mode
wall), X3 (equal-input conditional), X4 (KKT countermodel), A1/A2/A4/A7/N1/F1 (wave-1 audits),
d3 (envelope), d4 (MCC reductions), d7 (FTI-2 decider).

**Audited arsenal I will rely on (re-derived where load-bearing, below):**
- (D0) diam₁(K) ≤ 2+4δ; ‖P‖_{∞→∞} = 1+2·max_i neg(p_i). Both elementary (rowsum 1 + neg ≤ δ).
- (L1) lone-far-row: dist₁(v, conv(rows∖{v})) ≥ ρ ⇒ v is (ρ, ρ/(2+4δ))-exposed; ρ-ball exempt.
  Note ρ/(2+4δ) = 4τ/(2+4δ) ≥ τ (δ ≤ 1/2) ≫ κ = τ/4. Margin headroom factor ≥ 4. [A1, verified]
- (L2) some row at height H ⇒ some row VERTEX at height ≥ H (convexity of dist₁(·,C)). [A2(i)]
- (L2′) hidden vertex v ⇒ dist₁(v, conv(rows∖{v})) < ρ (contrapositive of L1). [d4]
- (L4) frame-clipping: λ a signed coefficient vector over points f_a ∈ conv W with Σλ=1 ⇒
  dist₁(Σλ_a f_a, conv W) ≤ (2+4δ)·neg(λ). [A4(i)]
- (L5′) at a GLOBAL height maximizer i*: normalized positive mass on rows of height ≤ H/2 is
  ≤ 2(2+4δ)δ/H. FALSE for non-maximizers. [A4 corrected]
- (F1-id) mutual-shadow elimination: v₁ = μ₁v₂+(1−μ₁)L₁+e₁, v₂ = μ₂v₁+(1−μ₂)L₂+e₂, L_j∈C,
  ‖e_j‖₁ ≤ ρ ⇒ (1−μ₁μ₂)·dist₁(v₁,C) ≤ (1+μ₁)ρ. So at height H: 1−μ₁μ₂ ≤ 2ρ/H = 8τ/H. [A7]
- (X1) one-mode wall: exact shell p_i = q + t_i r with nonconstant t forces r·t=1, r·1=0 ⇒
  Δt·‖r‖₁ ≥ 2 ⇒ diam₁{p_i} ≥ 2. (Will re-derive; it is the seed of my main thrust.)
- (B–S) exact stochastic idempotents = absorbing equal-input blocks + proportional transient rows
  (refs/baake-sumner-2007.11433).
- Numerics: 43k+ exact configs, floor δ/H² ≈ 3.49 at the H ~ τ boundary; deep-hidden region costs
  δ/H² ∈ [280, 26000]; hard wall dist/τ ≤ 0.536; hull-chase law; R duals inert once rows pinned.

**Dead routes (will not re-walk):** averaging/quasi-stationary; height tests for norm excess
(Px ∈ [0,1] kills it); raw circuits; unlocalized dual descent; maximal-skeleton sans localization;
stochastic-complement rank induction; KKT localization energy; pure shadow composition (vacuous as
μ₁μ₂→1).

**Known single obstruction (all faces of one gap):** high, ρ-far HELPER/CARRIER rows on the high
zero-face. L5′ controls high→low leakage only at the maximizer; nothing proved controls
high→high off-chain mass, and the C10 dual's α-mass can sit on a high zero-face. Every failed
route reduces to exactly this.

**My read of the geometry (orienting picture, not a claim):** rank r ⇒ P = ΛR, RΛ = I_r; rows
p_i = Λ_i R live in an (r−1)-dim affine flat V = {x : x1=1} ∩ rowspace. K = conv(rows) ⊂ V.
Heights h_i = dist₁(p_i, conv W) are intrinsic to the row set. The fixed-point identity
p_i = Σ_j P_ij p_j (each row is a SIGNED affine combination of all rows, with neg coefficient
mass = neg(p_i) ≤ δ) is the entire content of P² = P at row level. THIS identity — rows are
δ-almost-convex combinations of rows — plus "rows live in the flat" is what every argument
actually uses. I will treat it as the master identity (MI).

**Plan of attack (ordered):**
- T1 (main): multi-mode biorthogonality made quantitative — replace "k modes" bookkeeping by a
  single scalar height functional obtained from the optimal exposer of the TOP vertex, and run
  the MI through it with the F1 near-coincidence + L5′ at the maximizer. Goal: a self-improving
  inequality h ≤ (something)·h + Cδ/H·diam where the contraction factor is bounded away from 1
  by exactness (the X1 mechanism: a shell cannot reproduce its own height functional internally
  without an Ω(1)-diameter dual carrier, which the ρ-ball cannot contain).
- T2: the "top-cluster trap": apply MI not to one row but to the ENTIRE set S = {h_i > H/2},
  using the convexity of height + L5′-type leakage AT THE MAXIMIZER ONLY, and ask what the
  positive mass on S∖(ρ-ball of i*) does. Combine with F1 to collapse S near the top into one
  ρ-cluster, then apply L1 to the cluster as a single pseudo-row (cluster version of lone-far-row:
  if the whole top cluster is ρ-far from conv(other rows), some member exposes). The missing
  piece becomes: positive mass from i* into the mid-band (H/2, H−ρ·gap) — try to kill it with a
  second-moment/variance functional rather than a height test (dead route only covers ℓ∞ height
  tests bounded in [0,1]; a QUADRATIC functional of an affine map is not subject to Px∈[0,1]).
- T3 (refutation lane, run in parallel mentally): try to beat the numerics with a structured
  family the searches could not see: log-staircase with k ~ log(1/δ) layers where each layer's
  dual carrier is the next layer (the X1 wall says the carrier needs Δt·‖r‖₁ ≥ 2 — try paying
  it across layers, diameter 2 is AVAILABLE since diam(K) ≈ 2). Key question: does the ℓ¹ row
  budget 1+2δ allow mode coefficients t_i^{(m)} with the needed biorthogonal pairing at all
  scales simultaneously?
- T4: if T1–T3 all partial: extract the sharpest PROVED structural fact + minimal residual
  conjecture, with the honest dependency DAG.

Self-scrutiny pass is mandatory at the end; every PROVED claim gets re-derived from scratch there.

---

## Stage 1 — Reframings and first new structural facts

### 1.1 The transpose frame (conceptual, orients everything)

Q := Pᵀ is a projection on ℓ₁ⁿ with ‖Q‖₁→₁ = ‖P‖∞→∞ = 1 + 2max_i neg(p_i) ≤ 1+2δ, and Q is
mass-preserving (1ᵀQ = 1ᵀ ⇔ P1 = 1). The rows are the images of the standard basis: **p_i = Q e_i**.
HLC is therefore exactly a quantitative stability statement for near-contractive mass-preserving
projections on ℓ₁ⁿ (Douglas–Ando rigidity, quantitative — consistent with the campaign framing).
At δ=0 the Baake–Sumner normal form = the classical contractive-projection structure (disjointly
supported class distributions + proportional transient rows).

### 1.2 Affine profiles are EXACT fixed vectors; the deficit identity

For any affine φ on the row flat, the profile γ = (φ(p_i))_i satisfies γ = Pγ EXACTLY (P1=1,
P²=P). Take φ the optimal ℓ¹-separator of the top vertex v from C = conv W: ‖∇φ‖_∞ ≤ 1,
sup_C φ = 0, φ(v) = H. Then γ_i = φ(p_i) ≤ h_i ≤ H ∀i, γ at v's index = H. The **deficit**
g := H·1 − γ satisfies (P1=1):

  g = Pg,  g ≥ 0,  g(v) = 0,  g_j ≥ H − h_j  (so g ≥ H/2 on all rows of height < H/2),
  ‖g‖_∞ ≤ H + diam₁(K) ≤ H + 2 + 4δ.

At the top row: 0 = Σ_k P⁺_{vk}g_k − Σ_k P⁻_{vk}g_k, hence **Σ_k P⁺_{vk} g_k = Σ_k P⁻_{vk}g_k
≤ δ‖g‖_∞ ≤ δ(H+2+4δ)** — recovers/sharpens L5′ with φ-level sets: the top row's positive mass on
{g ≥ s} is ≤ δ(H+2+4δ)/s. At a general row j: Σ_k P⁺_{jk}g_k ≤ g_j + δ‖g‖_∞ — the φ-sub-level
sets are GRADED almost-invariant sets of P⁺. This reproduces the band/staircase escape hatch
(mass can drift one band down per step) — consistent with N1; no new wall from flow alone. [Re-derivation
of known material in sharper coordinates; nothing here contradicts the dead-route map.]

**Max-principle reading (the right abstract home for HLC):** at δ=0, fixed vectors of a stochastic
idempotent attain their max on recurrent classes (= W at δ=0); γ ≤ 0 on W-rows forces γ ≤ 0
everywhere. HLC = the QUANTITATIVE max principle: a P-fixed vector which is ≤ 0 on W-rows and
1-Lipschitz w.r.t. row geometry can overshoot to +H only if δ ≥ aH². Per-row overshoot above the
max of the positive support is ≤ ε_i·(γ-spread) ≤ 2.2δ — so any tower needs ≥ H/(2.2δ) ~ 1/τ
rows: dimension-dependent escape only; the numerics (n ≲ 12) could NOT have seen long towers.
This sharpens where a counterexample MUST live if it exists: n ≳ H/δ.

### 1.3 NEW Lemma SS (sharp shadow — shadows live at scale δ, not ρ)

**Claim.** For any row i with P_ii < 1: dist₁(p_i, conv(rows∖{p_i})) ≤ (2+4δ)·m_i where
m_i = neg of the normalized off-self coefficients ≤ δ/(1−P_ii) (for P_ii ∈ [0,1); ≤ δ if P_ii ≤ 0).

**Proof.** MI: p_i = Σ_j P_ij p_j ⇒ (1−P_ii)p_i = Σ_{j≠i}P_ij p_j ⇒ p_i = Σ_{j≠i} c_j p_j with
c_j = P_ij/(1−P_ii), Σ_{j≠i}c_j = 1, neg(c) =: m_i ≤ δ/(1−P_ii). Split c = c⁺ − c⁻ and normalize:
p_i = (1+m_i)q − m_i r with q,r ∈ conv(rows∖i); ‖p_i − q‖₁ = m_i‖q−r‖₁ ≤ m_i·diam₁(K). ∎

Consequence: a hidden top vertex with P_vv ≤ 7/8 has an O(δ)-shadow — 17δ, vastly tighter than
the ρ = 4τ shadow from L2′. All recursion/F1 machinery can be re-run at shadow scale δ.

### 1.4 NEW Lemma DJ (delta jaw — self-mass forces exposure unless the site is fed)

**Claim.** If row i has P_ii ≥ 1−η and every other row j has P_ji ≤ η′, with 2η+2η′+2δ ≤ 2−ρ,
then dist₁(p_i, conv(rows∖i)) ≥ 2−2η−2η′−2δ ≥ ρ, so p_i is (ρ,κ)-well-exposed by L1 — height 0.

**Proof.** Any q̄ ∈ conv(rows∖i) has q̄_i ≤ η′ and Σ_{j≠i}q̄_j ≥ 1−η′ (signed: total sum is 1 and
i-entry ≤ η′; ℓ¹ off-i mass ≥ |sum off-i| = 1−q̄_i ≥ 1−η′). Row i has (p_i)_i ≥ 1−η and off-i ℓ¹
mass ≤ (1+2δ)−(1−η) = η+2δ. So ‖p_i−q̄‖₁ ≥ ((1−η)−η′) + ((1−η′)−(η+2δ)) = 2−2η−2η′−2δ. L1 gives
margin ≥ ρ/(2+4δ) ≥ κ·4-ish ≥ κ. ∎

**Dichotomy (DJ+SS):** every HIDDEN row vertex v (at site i) satisfies either
 (a) P_ii < 1−η (then SS: an O(δ/η)-shadow in conv of the other rows), or
 (b) some OTHER row feeds v's site: ∃j≠i, P_ji > η′.
(η,η′ = 1/8 say.) This is the precise matrix-level form of the two jaws: a hidden vertex is
either nearly-affinely generated by the others at scale δ (not ρ!), or its site receives Ω(1)
mass from another row (the "self-feeding shell" — now visible as a COLUMN property).

### 1.5 The self-coefficient rigidity (why naive towers die — mined from the failed construction)

A tower x_m = (1+δ)x_{m−1} − δπ (coefficients on the layer below + negative on a far anchor)
forces, by entries=coefficients, x_m = (1+δ)e_{site(m−1)} − δe_{site(π)} as a VECTOR; consistency
then forces x_{m−1} ≈ e_{site(m−1)}: delta-like rows ⇒ P_ii ≈ 1, unfed ⇒ DJ ⇒ EXPOSED, tower
collapses (each layer joins W; height never accumulates). This is the exact mechanism behind the
numerics' "hull-chase". A non-collapsing shell must SPREAD its coefficient mass across other
shell rows ⇒ mutual-shadow web ⇒ X1-type biorthogonality territory. The two jaws are now both
matrix-explicit; the open middle is the spread-mass multi-mode shell (next stage).


---

## Stage 2 — New algebraic objects: the energy vector in ker P, and site-budget rigidity

### 2.1 NEW: the energy vector Γ and the kernel identity PΓ = 0

Let g = Pg be any exact fixed vector (e.g. the deficit of §1.2). Define the **local energy**

  Γ_j := Σ_k P_jk (g_k − g_j)²  (signed; the negative part is ≥ −δ·osc(g)², osc(g) := max g − min g).

**Fact E1 (exact).** P(g²) − g² = Γ componentwise, where (g²)_j := (g_j)². Proof: (P g²)_j − g_j²
= Σ_k P_jk(g_k² − g_j²) = Σ_k P_jk(g_k−g_j)² + 2g_j Σ_k P_jk(g_k − g_j) and the last sum is
(Pg)_j − g_j = 0. ∎

**Fact E2 (exact).** PΓ = 0 — the energy vector lies in ker P. Proof: P(g²) is exactly fixed
(P² = P), so P(g² + Γ) = P(g²) = g² + Γ and P(g²) = g² + Γ gives PΓ = P(g²+Γ) − P(g²) = 0. ∎

**Fact E3 (energy starvation).** Γ_j ≥ −δ·osc(g)² for all j, and for EVERY row j:
  Σ_k P⁺_jk Γ_k = Σ_k P⁻_jk Γ_k ≤ δ‖Γ‖_∞ ≤ δ(1+2δ)osc(g)².
Hence with osc(g) ≤ H + 2 + 4δ ≤ 2.2+H ≤ 3 (small H): Σ_k P⁺_jk (Γ_k + δ·9) ≤ 9δ + 9δ(1+2δ),
so **positive mass on {Γ ≥ E} is ≤ 19δ/E for every row** (δ ≤ 1/4). High-energy rows are shunned
by ALL positive mass — including their own self-mass: P⁺_kk ≤ 19δ/Γ_k. [Quantitative form of the
δ=0 fact: transient sites receive zero column mass.]

**Fact E4 (localization from low energy).** If Γ_j ≤ E₀ then row j's positive mass on
{k : |g_k − g_j| ≥ Δ} is ≤ (E₀ + 9δ)/Δ². So low-energy rows are g-LOCALIZED — and in particular
FEEDING across a g-gap costs energy: a row with positive mass m₀ at g-level ℓ₁ and m₁ at level ℓ₂
has Γ ≥ (m₀∧m₁)·(ℓ₂−ℓ₁)²/4 − 9δ (its own g sits at the weighted mean; both sides contribute).

This is a genuinely NEW lever vs the dead-route map: it is not a height test (quadratic, not
bounded-affine — Px∈[0,1] does not apply), not flow-averaging (it is an exact one-step kernel
identity), and it converts the "high zero-face carrier" obstruction into a quantitative statement:
**level-mixing rows exist only as positive-mass orphans, at energy ≥ mixing·gap².**

Residual honesty: E3 does NOT yet make high energy COST δ globally — a super-transient orphan row
is permitted (at δ=0, transient rows have Γ > 0 freely). The question is whether the hiding
mechanism FORCES someone to pay positive mass into high-energy sites (then δ ≥ mass·E/19 — wait,
direction: E3 bounds it; a forced payment of mass m onto {Γ ≥ E} CONTRADICTS E3 unless
m ≤ 19δ/E, i.e. δ ≥ mE/19 — that IS the δ ≳ H² shape if m ~ 1 and E ~ H²). **So the whole game
is now: prove the hidden shell forces some row to put Ω(1) positive mass on Ω(H²)-energy sites.**

### 2.2 The exact 2-shell collapses to a recurrent class (instructive computation)

Try the minimal mutually-supporting top pair on private sites 1,2: rows x₁,x₂ with entries
(a,b|w₁), (c,d|w₂) (w_i on anchor sites; anchors don't touch sites 1,2). Entry-matching at sites
1,2 under MI forces b(1−a−d) = 0, c(1−a−d) = 0, a = a² + bc, d = d² + bc. Either b = c = 0
(delta rows ⇒ DJ ⇒ exposed) or a + d = 1 ∧ bc = ad — and then det[[1−a,−b],[−c,1−d]] = 0, which
forces the anchor combinations W₁, W₂ to be antiproportional nearly-positive vectors ⇒ both
O(δ) ⇒ a + b = 1 + O(δ), c + d = 1 + O(δ) ⇒ x₁ = x₂ = (a, 1−a) + O(δ): the pair is a COINCIDENT
equal-input class (B–S block) — an exposed vertex. Conclusion: an exact private-site top pair
cannot hide; it degenerates to a recurrent class. (Matches d3's "coincident clusters are the
exact-limit structure", and the hull-chase.) [PROVED at the displayed level of rigor; the O(δ)
chasing is routine.]

### 2.3 NEW Lemma PC (private-cluster exposure — the cluster delta-jaw)

Setting: v a row vertex; B = ρ-ball rows around v (exempt set); suppose the cluster's site mass
is private: v has mass M_v ≥ 1 − θ on a site set S, while every ρ-FAR row p_j has slab-site mass
F_j = ‖p_j|_S‖₁ ≤ θ′. Claim: if θ + θ′ small (θ + θ′ ≤ 1/4 say, δ ≤ δ₀), v is (ρ,κ)-exposed.

Dual proof sketch (C10): a failing dual needs Σ_j μ_j(p_j − v) = Σ_i(β_i − α_i)(p_i − v),
Σβ < κ, μ ∈ Prob(far). Restrict to S-coordinates and take the 1ᵀ(·) functional (total S-mass):
LHS: Σμ_j F_j^{signed} − M_v^{signed} ≤ θ′ − (1 − θ − δ) < −(1 − θ − θ′ − δ)·(…).
RHS: rows in B have |S-mass − M_v| ≤ ‖p_i − v‖₁ < ρ ⇒ (p_i − v) S-mass ∈ (−ρ, ρ); far rows give
S-mass(p_i − v) ≤ θ′ − M_v + … each, with coefficient (β_i − α_i): the α-part contributes
+α_i(M_v − θ′) ≥ 0 and the β-part ≥ −β_i(M_v + δ)·…; collecting: RHS ≥ −Σβ(1+…) − Σ_{i∈B}|β−α|ρ
− …. For the identity to hold one needs Σ_{i∉B}(β_i − α_i) ≈ 1 − θ − θ′, impossible since
Σβ < κ ≪ 1 and α ≥ 0 enters with the wrong sign — UNLESS the α-mass on B-rows is ~1/ρ (the
exempt rows can carry α!). B-rows have S-mass ≈ M_v: α_i on B contributes −α_i·(S-mass(p_i−v))
∈ (−α_iρ, α_iρ): bounded by ρ·|α_B| — to supply the needed ≈ −1, |α_B| ≥ (1−θ−θ′)/ρ ~ 1/ρ.
So either v is exposed, or the dual carries α-mass ≥ c/ρ on the ρ-ball rows. [PROVED modulo
careful constant-chasing EXCEPT the final loophole: large α on the exempt ball is NOT excluded
by C10 (α is uncontrolled). Stage 3 must either exploit |α| ~ 1/ρ (a near-singular dual is
itself structure: it means the ball rows' directions nearly cancel a unit S-mass deficit with
huge coefficients — quantitative affine dependence inside the ball) or route around C10.]

### 2.4 The feeder-replication tension (the sharpened crux)

Combining 2.3 with the exemption: to hide v, far rows (or the α-correction) must REPLICATE v's
private-site pattern. But a far row that replicates the pattern in full is ℓ¹-close to v —
contradiction with being far — so each far row replicates at most partially (mismatch ≥ ρ/2 in
ℓ¹ split between off-S mass and S-pattern mismatch), and the off-S/mismatch parts live at OTHER
g-levels. By E4, rows mixing the slab level (g ≈ 0) with level-ℓ mass at weight m pay
Γ ≥ ~m·ℓ². By E3 nobody may put positive mass ≥ 19δ/Γ on such rows' sites. The residual question
(THE remaining crux, now much sharper than "dual localization"):

  (RC) Does the hidden-top configuration force some row to place Ω(1) positive mass on sites of
  rows with energy Γ ≥ cH²? Equivalently: can the feeding system arrange ALL its level-mixing
  into positive-mass-orphan rows (fed only at O(δ/H²))?

If RC-yes: δ ≥ Ω(1)·cH²/19 by E3 ⇒ HLC with p = 2. If RC-arrangeable: the orphan-feeder
architecture is a concrete counterexample TEMPLATE (next stage tests it).


---

## Stage 3 — The split/blocker/budget chain (main thrust; partially successful)

Throughout: v = top vertex (height H, g(v) = 0), small-δ regime, H ≥ Aρ, ρ = 4τ, κ = τ/4;
"level" = deficit g; all rows of height < H/2 have g > H/2; rows at/below C have g ≥ H.

### 3.1 The g-budget (exact, used everywhere)

For any row j: g_j = Σ_k P⁺_jk g_k − Σ_k P⁻_jk g_k, g ≥ 0, so the positive coefficient mass that
row j places on rows at level ≥ ℓ is **≤ (g_j + δ·osc(g))/ℓ ≤ (g_j + 2.2δ)/ℓ**. A top-level row
(g_j = O(δ)) can draw coefficient mass σ from level ℓ only if σℓ ≤ g_j + 2.2δ. Conversely drawing
from BELOW one's level is free — feeding (low rows loading high sites) is NOT constrained by g.
[This is why all flow arguments stall; recorded for the record.]

### 3.2 Why a hidden top needs a SPLIT cluster (de-exposure mechanics, sharpened)

Let S = the site-support of the top cluster (the sites where v's mass ≈ 1 sits). The affine
exposer family contains h₀(x) = 1 − (S-mass of x), and more generally h_c(x) = combinations of
(1 − S-mass) and c·(x − v), c ∈ [0,1]^S. Blocking h₀ requires a ρ-far row b with S-mass ≥ 1 − κ
(else h₀ normalizes to an exposer: anchors have S-mass ≈ feed). Such a **blocker** has ≤ κ + 2δ
mass left for everything else, hence:

  **(B1) Blockers are cluster-exclusive.** A row with S_c-mass ≥ 1−κ cannot simultaneously carry
  S_{c'}-mass ≥ 1−κ for a site-disjoint cluster c′. One full-mass pattern-carrier per cluster
  minimum; they are not shareable. [PROVED — mass budget.]

  **(B2) A blocker is v + wiggle.** ‖b − v‖₁ ≥ ρ with both S-masses ≈ 1 forces the difference to
  be a zero-sum wiggle w INSIDE the S-face, ‖w‖₁ ≥ ρ − (κ + 4δ) ≥ ρ/2. Blocking the whole
  exposer family requires several blockers whose wiggles {w_j} balance (Σμ_jw_j = O(κ)): the
  "surround within the S-face". [PROVED at C10/separation level modulo constant-chasing.]

  **(B3) Wiggles need a SPLIT cluster or pay negativity.** b is a row; its coefficients = its
  entries ≈ supported on S = coefficients on the cluster rows themselves. If the cluster rows
  span internal spread ω = max‖x_i − x_j‖₁, a wiggle of size ρ needs coefficient spread ~ ρ/ω,
  hence neg(b) ≳ ρ/ω − 1. So either ω ≳ ρ/(1+δ) — the cluster is genuinely split at scale ρ —
  or δ ≥ neg(b) ≳ ρ/ω − 1. [PROVED.]

### 3.3 The split costs top-level external mass σ ≳ ρ/2 (the 2-row computation)

For a 2-row cluster x₁,x₂ with within-cluster coefficients [[a,b],[c,d]] and external
combinations W₁,W₂ (coefficient sums σ₁,σ₂): x₁ − x₂ = [σ₂W₁ − σ₁W₂]/det,
det = (1−a)σ₂ + (1−d)σ₁ − σ₁σ₂. With ‖W_i‖₁ ≤ σ_i + O(δ) this gives

  **ω = ‖x₁ − x₂‖₁ ≤ 2σ/(A+D) + O(δ),  σ := max σ_i, A+D = 2−a−d ≥ … ,**

so ω ≥ ρ forces **σ ≳ ρ/2 = 2τ** (when A+D ~ 1; degenerate A+D → 0 is the coincident-class
limit which §2.2 kills). By the g-budget (3.1) this σ must be drawn from rows at level
ℓ ≤ 2.2δ/σ ≤ **1.1τ** — i.e. from OTHER rows essentially AT THE TOP. The exact closed cluster
(σ = 0) collapses to a coincident recurrent class (§2.2) and exposes (PC). [PROVED for k=2;
the k-row version of the same computation is routine linear algebra but NOT yet done — flagged.]

### 3.4 The web: the top level is a (1/2A)-almost-closed subsystem

Let T = {rows with g ≤ cτ}. Each T-row's positive coefficient mass at levels ≥ H/2 is
≤ (cτ + 2.2δ)/(H/2) ≤ 2(c+2.2)τ/H ≤ (c+2.2)/(2A) — the top level as a whole is an
**ε-almost-closed subsystem with ε = O(1/A)**: B = P_TT satisfies ‖B² − B‖_∞ ≤ ε(1+2δ) + …
(B² = B − P_{T,T^c}P_{T^c,T}, ‖P_{T,T^c}‖_∞ ≤ ε, ‖P_{T^c,T}‖_∞ ≤ 1+2δ). The hidden-top
architecture is therefore forced to be: a self-sustaining, almost-closed, almost-stochastic,
almost-idempotent web of split clusters at the top, mutually supplying each other's σ ≳ 2τ
split-mass, each with ≥ 2 exclusive blockers (which may be cluster-mixtures, hence themselves
exempt from exposedness obligations — only vertices owe exposedness). [PROVED that the
architecture is forced INTO this form; what remains open is that this form is impossible.]

### 3.5 Where it still does not close (honest)

Two endgames both stall at a RECURSION, not at a flow gap:

(i) **Exact-closure induction.** If the web were EXACTLY closed (P_{T,T^c} = 0), B is a full
instance of the original problem on |T| < n rows (B1=1, B²=B, neg ≤ δ) — induction on n would
give δ ≥ aH_T² for ITS hidden height. Two gaps: (a) the web is only O(1/A)-almost-closed —
exactness fails precisely by the amount the budget allows; (b) sub-system exposedness does not
transfer: a W_sub vertex need not be W-exposed among ALL rows (outside rows can blockade it),
so H_T is not comparable to H without a transfer lemma. [The transfer is the OLD frame-transfer
gap, now appearing as the ONLY missing piece of an otherwise-complete induction.]

(ii) **Energy accounting (§2) almost closes it.** Blocker/surround rows and split-suppliers are
all top-level (g ≲ τ) — LOW energy — so E3 does not tax them; the level-mixing rows (feeders
from below) are orphans that nothing in the current argument forces anyone to PAY for. RC (§2.4)
remains: nothing yet forces Ω(1) positive mass onto Ω(H²)-energy sites.

### 3.6 What IS new and bankable from this stage

- (B1)–(B3) + §3.3: **a hidden top cluster cannot be skinny-and-cheap: it must be ρ-split, and
  the split must be sustained by σ ≳ 2τ of coefficient mass drawn from rows at level ≤ 1.1τ.**
  This kills, unconditionally: single coincident-class tops (collapse + expose), one-blocker
  configurations, naive towers (§1.5), and any architecture whose top draws its split-mass from
  below level ~τ — the g-budget makes deep-drawing impossible. The counterexample, if it exists,
  is CONFINED to: a top-level almost-closed web of ≥ 2 mutually-supporting ρ-split clusters with
  exclusive blocker mixtures, total external (below-top) coefficient ≤ O(1/A) per row.
- The d7 numerics' helper-ring instances (δ/H² ≥ 280) are exactly degenerate web attempts; the
  exclusivity (B1) explains the observed hull-collapse: every added full-mass blocker is itself
  top-level, near-coincident in S-mass, and drags conv W up unless ITS vertex obligations are
  met — which costs the next round of structure ("hull-chase" mechanism identified).


---

## Stage 4 — Endgames: blocker cap, wiggle rigidity, the two-level evasion, and where it truly stops

### 4.1 NEW Lemma ND (near-delta rows are exposed — unconditional)

If a row x has off-own-site ℓ¹ mass ≤ t (i.e. x_i ≥ 1 − t at its own site i, plus ≤ 2δ
negativity) with 2t + 4δ ≤ ρ − κ(1+2δ), then x belongs to an exposed cluster: take v_max = the
row maximizing site-i mass M; h(y) = (M − y_i)/Z, Z ≤ 1+2δ, is affine, ≥ 0 on K, h(v_max) = 0;
any ρ-far row q must differ from v_max by ≥ ρ, and since both are t-concentrated at site i up to
…, |q_i − M| ≥ ρ − 2t − 4δ ≥ κ(1+2δ), so h(q) ≥ κ. Hence v_max is (ρ,κ)-well-exposed, lies in W,
and x sits within 2t + O(δ) ≤ ρ of conv W. **Consequence: every row of a hidden top cluster has
self-site mass ≤ 1 − (ρ − κ)/2 + O(δ), i.e. A = 1 − a ≥ 1.8τ.** [PROVED; replaces the η,η′
bookkeeping of DJ at the right scale and removes the exact-zero-at-v nuisance via max-selection.]

### 4.2 NEW Lemma BC (blocker cap)

A blocker for cluster c (S_c-mass ≥ 1 − κ, forced in §3.2 to exist among ρ-far rows whenever the
site-indicator exposer fails) has coefficient mass outside the cluster's rows ≤ κ + 2δ. In
particular **a blocker can never supply ρ/2-scale external split-mass; in any ρ-separated pair
(v, blocker), the σ-burden of §3.3/§4.4 falls on v.** [PROVED — mass bookkeeping.]

### 4.3 Wiggle rigidity for common-pattern webs (key computation; PROVED modulo one flagged step)

Let a set R of rows share a base pattern: x_i = π̄ + w_i, ‖w_i‖₁ ≤ R_w ≪ 1, with the rows
self-indexed (coefficient on row k = entry at site k). Writing s_i = (x_i)(R-sites),
ext_i = Σ_{k∉R} P_ik p_k (external coefficient mass σ_i): MI gives exactly

  w_i = (s_i − 1)π̄ + Σ_{k∈R} π̄_k w_k + Σ_{k∈R} w_{i,k} w_k + ext_i,

where the third term is ≤ ‖w_i‖₁·max‖w_k‖₁ ≤ R_w² (QUADRATIC — because the coefficients on
R-rows are themselves π̄ + wiggle entries). Differencing two rows i,j and using the total-mass
cap (rowsums = 1, neg ≤ δ ⇒ the π̄-component difference t = s_i − s_j has |t| ≤ O(δ) + |Σ(ext
difference)|) [FLAGGED: this mass-cap step needs a careful re-derivation — see scrutiny §5]:

  ‖w_i − w_j‖₁ ≤ O(δ) + O(R_w²) + σ_i + σ_j.

**Consequence (if the flagged step holds): any two rows of a common-pattern web separated by
≥ ρ need combined external coefficient mass σ_i + σ_j ≥ ρ − O(δ + ρ²) ≈ ρ(1−o(1)) — wait, ≥
ρ/1 not ρ/2; with the worst constants ≥ ρ/2.** A fully-closed web (σ ≡ 0) is coincident to
O(δ + ρ²): the X1 wall in FULL multi-mode generality, no one-mode assumption. [This subsumes and
greatly strengthens X1; it is the single most valuable new fact if it survives scrutiny.]

### 4.4 The pinch at the top and the two-level evasion (honest status)

Chain that now stands: v hidden ⇒ (ND) cluster not delta-like ⇒ (§3.2) blockers exist, ρ-far,
S-full ⇒ (BC) blockers cannot pay ⇒ (4.3) σ_v ≥ ρ/2 − κ − O(δ) ≈ 1.75τ ⇒ (g-budget, g_v = 0)
v's suppliers sit at level ℓ ≤ 2.2δ/1.75τ ≈ 1.26τ — **the top maximizer's split-suppliers are
confined to the top 1.26τ of the deficit range.** [PROVED modulo 4.3's flagged step.]

Where it stops: the suppliers themselves sit at level g ~ τ, and at level g ~ τ the same
σ-requirement can be financed from level ℓ ≤ (τ + 2.2δ)/σ ~ O(1) — i.e. from sub-C rows (φ < 0),
which carry NO obligations and NO negativity cost: g_supplier = τ is exactly paid by σ·ℓ mass on
low rows. The pinch confines only rows with g = O(δ). A two-level architecture — v's cluster at
g ≈ 0 drawing σ ~ 2τ from supplier-groups at g ∈ [τ, 2τ], the supplier-groups' own splits and
surrounds financed by ordinary low rows — satisfies every inequality derived in this document
with max neg = O(δ). The forced negativity at v computes to neg_v ≥ σ_v·ℓ_actual/osc(g) ≈
(1.75τ)(τ)/2.2 ≈ 0.8δ: AT the budget, not above it. **The constants land within a factor ~2 of
each other: the argument as it stands neither proves δ ≥ aH² nor exhibits slack for a
counterexample — it pins the battle to the supplier level ℓ_actual and to whether τ-level
supplier-group VERTICES recursively owe their own pinch.**

The remaining alternative endgame (n-induction): if all structure retreats to g = O(δ), the web
becomes coefficient-CLOSED; a closed subsystem is an exact idempotent on < n rows (B² = B
because P_{T,T^c} = 0 kills the feedback term identically) and induction applies — but the
exposedness TRANSFER from the subsystem to the full system degrades by a factor ~ρ (mixture
blockades), which is the one unhealed wound of the whole campaign (frame-transfer in yet another
costume).


---

## Stage 5 — MANDATORY SELF-SCRUTINY (hostile re-derivation of every load-bearing step)

1. **SS (§1.3): SURVIVES.** Re-derived; the normalization Σ_{j≠i}c_j = 1 and the clipping bound
   are exact. Constant: dist ≤ (2+4δ)·δ/(1−P_ii).
2. **DJ (§1.4)/ND (§4.1): SURVIVES WITH CONSTANT DOWNGRADE.** In ND the far-row dip estimate
   loses a factor 2 that §4.1 overlooked: ρ ≤ 2(M − q_i) + 2t + 4δ, so the margin is
   (ρ − 2t − 4δ)/(2Z), and the self-mass exclusion becomes A = 1 − a ≳ 0.85τ (not 1.8τ).
   Mechanism intact; all downstream constants weaken by ≤ 2×.
3. **E1–E3 (§2.1): SURVIVE.** PΓ = 0 is trivial-but-real (Γ = P(g²) − g², P idempotent). E3's
   constant rechecked: ≤ 2δ(1+2δ)(H+2.2+2δ)² ≤ 19δ for H ≤ 0.6, δ ≤ 1/4.
4. **g-budget (§3.1): SURVIVES** (osc(g) ≤ H + 2 + 4δ since inf_K φ ≥ −diam₁(K)).
5. **§3.3 (2-row split): SURVIVES** as algebra (det and difference formulas re-derived), but it
   is only the k=2 case; §4.3 supersedes it.
6. **§4.3 wiggle rigidity: the flagged step is REPAIRED — now fully PROVED.** The cap on the
   π̄-component uses the GLOBAL zero-sum of wiggles: ν_i := w_i(R-sites) = −w_i(R^c-sites) ± 2δ
   and |w_i(R^c)| ≤ σ_i + δ (non-R-site entries ARE the external coefficients). Final form:
   for self-indexed rows x_i = π̄ + w_i, ‖w_i‖₁ ≤ R_w:
   **‖w_i − w_j‖₁ ≤ 2.1(σ_i + σ_j) + 4δ + 2R_w².**
   Hence ρ-separation within a 2ρ-pattern web forces σ_i + σ_j ≥ (ρ − 4δ − 8ρ²)/2.1 ≈ ρ/2.2
   (needs τ ≤ 1/33-ish). A fully closed web is coincident to O(δ + ρ²). This subsumes X1
   (k=1 AND all k; no coordinate-closure assumption beyond self-indexing). **This is the
   strongest bankable result of the pass.**
7. **§3.2 blocker forcing: PARTIALLY SURVIVES — important hole found.** The S-indicator exposer
   cannot be normalized to vanish at v (the exact-zero-at-v issue); max-selection repairs it but
   exposes the S-mass-maximizing VERTEX v′ (or the ψ = x(S) + λφ maximizer v″), not the height
   maximizer v. The blocker/BC/4.3 chain therefore forces σ_{v″} ≥ ρ/2.2 − κ − 2δ ≈ 1.55τ at the
   vertex v″ whose level is g(v″) ≤ 2σ_v + O(δ) — NOT at v itself.
8. **§4.4 pinch: SURVIVES AS A DICHOTOMY WITH AN EXPLICIT HOLE.**
   - If σ_v ≳ τ/2: v itself draws ≥ τ/2 from levels ≤ 4.4τ — pinched at the top. ✓
   - If σ_v = O(δ): v″ sits at g = O(δ) and is fully pinched (suppliers ≤ ~3.4τ-level). ✓
   - **MIDDLE REGIME σ_v ∈ (≈3δ, ≈τ/2): UNPINCHED.** v″'s level ≤ 2σ_v allows its forced
     σ_{v″} ≈ 1.55τ to be financed from level ≤ 1.3σ_v/τ = O(1) — i.e. from obligation-free
     sub-C rows. The two-level architecture (v-cluster at g≈0 with moderate σ_v; supplier
     groups at g ~ 4τ financed from low rows) evades every inequality in this document, with
     forced negativity ≈ σ_v·ℓ_supplier/osc ≈ 0.8δ — WITHIN the budget by a factor ~2.
9. **PC (§2.3): downgraded to PROVED-MODULO-α-LOOPHOLE** as stated there (the |α| ~ 1/ρ branch
   is real and untreated; the §3.2 site-indicator route bypasses C10 but inherits hole 7).
10. **Energy endgame (§2.4 RC): unresolved either way; no claim.** Feeders can be orphans;
    nothing forces payment. RC stands as an honest open question, NOT evidence.

Net effect of scrutiny: one major claim UPGRADED to proved (4.3), one major claim weakened
(blocker forcing localizes at v″, not v), constants degraded ~2×, and the residual hole is now a
NARROW, EXPLICIT parameter regime rather than a vague "dual localization" gap.

---

## Stage 6 — Deliverables: results, residual conjecture, verdict

### 6.1 New PROVED facts (bankable, in dependency order)

| id | statement | status |
|---|---|---|
| F-SS | every row with P_ii < 1 has an O(δ/(1−P_ii))-shadow in conv(other rows) | PROVED |
| F-ND | rows with off-own-site mass ≤ t, 2t+4δ ≤ ρ−2κ(1+2δ)·…, lie in exposed clusters (max-selection exposer); hidden cluster rows have self-mass ≤ 1 − ~0.85τ | PROVED (constants conservative) |
| F-E | Γ = P(g²)−g² satisfies PΓ = 0; energy starvation (mass on {Γ≥E} ≤ 19δ/E ∀rows); low-energy ⇒ g-localized | PROVED |
| F-GB | g-budget: positive coefficient mass σ at level ≥ ℓ obeys σℓ ≤ g_j + 2.2δ | PROVED |
| F-WR | wiggle rigidity: ‖w_i−w_j‖ ≤ 2.1(σ_i+σ_j) + 4δ + 2R_w² for self-indexed common-pattern webs; closed webs are coincident; ρ-separation costs σ ≈ ρ/2 external mass | PROVED (subsumes X1, all k) |
| F-BC | S-full blockers (S-mass ≥ 1−κ) carry ≤ κ+2δ external coefficient mass | PROVED |
| F-ψ | the ψ = x(S)+λφ max-selection forces an S-full ρ-far blocker for the vertex v″, with g(v″) ≤ 2σ_v + O(δ) | PROVED (mod routine constant-chasing) |
| F-2R | exact private 2-shells collapse to coincident equal-input classes | PROVED (private-site case) |

### 6.2 Minimal residual conjecture (the WHOLE remaining content of HLC)

**(MRP — middle-regime pinch.)** In the two-level architecture: top vertex v (g=0) with
external mass σ_v ∈ (Cδ, τ/2) drawn from supplier rows at level ℓ_v ≤ 2.2δ/σ_v; S/ψ-max vertex
v″ at level ≤ 2σ_v with forced σ_{v″} ≥ ρ/2.2 − κ financed at level ≤ 1.3σ_v/τ; supplier-group
splits financed by sub-C rows. CLAIM: exactness forces max-neg ≥ aH² in this regime too.
Everything else is proved around it. Note the forced negativity already computes to ≈ 0.8δ —
the architecture is borderline-infeasible, consistent with the empirical floor δ/H² ≈ 3.49 and
the hard wall H ≤ 0.54τ: if HLC is true it is true with a SMALL constant, and the proof must
win a factor-2 constants battle, not a scaling battle.

### 6.3 Verdict

HLC is NOT proved and NOT refuted by this pass. The pass (i) added a genuinely new exact-algebra
toolkit (kernel-energy Γ, wiggle rigidity, blocker cap, g-budget pinch), (ii) killed all cheap
counterexample architectures (closed webs, delta towers, coincident shells, one-sided
surrounds), and (iii) compressed the open set to one explicit two-level parameter regime (MRP)
where the cost lands within a factor ~2 of the budget. **Calibrated P(HLC true) ≈ 0.75–0.8**
(up from 0.7: the rigidity walls + borderline pricing of the sole surviving architecture).
**Single next action:** instantiate MRP's two-level family as a targeted exact-LP decider
(few parameters: σ_v, ℓ_supplier, group separation, k_groups) — it is now concrete enough that
either it produces δ/H² ≪ 3.4 (refutation) or its infeasibility certificates, mined across the
σ_v-sweep, ARE the missing middle-regime lemma. Estimated effort: one d7-style run.

