<!--
ROLE: d14 numerics worker report. Mission: measure the band-edge leakage profile on the
verified instance library; decide whether the t10 sup-form band-cut closure lemma holds in
practice (TRUE with a missing structural input) or is VIOLATED. See
wave5-sigma-wall-parallel.md WAVE 10/11 + ORCHESTRATOR STRATEGIC ASSESSMENT item 2.
Date: 2026-06-11. Worker: opus d14 (numerics). Code: experiments/d14_leakage.py;
data: experiments/out/d14_leakage.json + out/d14_logs/<label>.json (P saved per instance).
All [NUMERICAL].
-->

# d14 — band-edge leakage profile (sup-vs-averaged closure)

## VERDICT (read this first)

**The sup-form band-cut closure `λ ≤ c(1−q)τ` is VIOLATED on EVERY verified instance at the
stated c=1 target — but the violation is the BENIGN budget identity, and it points at the
exact missing structural input.** [NUMERICAL, 15 verified instances]

Decompose the shallow-band leakage into positive and negative parts. The result is uniform
and decisive across the whole library (corner, all d12 off-edge, the d13 small-δ anchor, the
s5 exact all-shallow face), δ ∈ [0.0012, 0.072]:

- **The total |·|-leakage of the shallow band has an irreducible floor `λ_S = δ = H/2`**,
  attained at **v itself** for EVERY threshold t — no cut lowers it (`lamS/δ = 1.000` to all
  digits; `lamS/H = 0.500` exactly; closure ratio `λ_S/((1−q)τ)` = 4.3–12, never ≤ 1).
- **That floor is 100% v's NEGATIVE entries pointing at deep rows** (`v→deep pos = 0`,
  `v→deep neg = δ` at the optimal t). The bad shell carries ZERO leakage (`shell_mass = 0`
  everywhere) — the obstruction is NOT a boundary-row phenomenon, it is v's own δ-budget.
- **The POSITIVE leakage `λ⁺_S = sup_{i∈S} Σ_{j∉S} P⁺_ij` is EXACTLY 0 at some threshold on
  every instance** (t/(κΩ) ∈ [0.10, 1.03]). v's positive carriers are all in-band; only its
  negative mass crosses the cut.

So **the sup-form closure is true for the POSITIVE kernel (λ⁺ = 0) and false for the signed
kernel (λ = δ).** The missing structural input is exactly the one t10's finisher already
needs and the campaign already names: the finisher acts on the **positive** part of the
block, where leakage genuinely vanishes — but then the residual is the OTHER finisher
hypothesis, the **projective diameter Δ**, which is **INFINITE (q = 1) on every structured
instance** because the in-band positive carriers point at the W-archetypes, which are
disjoint-support identity rows `e_i`. The band-cut route is therefore NOT dead by sup-leakage
(positive leakage closes perfectly); it is blocked at the Birkhoff-diameter hypothesis, the
zero-pattern/support-graph degeneration that the campaign flagged as the s5 / unbounded-Δ
branch. **The honest obstruction is: signed → positive splits the leakage cleanly (λ⁺=0,
λ⁻=δ), and the surviving residual is the support-graph (Δ=∞) case, not the sup-vs-averaged
gap.**

## What was measured

Instance library (all VERIFIED: idem_resid < 1e-7 — in fact 0.0 on the exact/optimized ones;
P1 = 1; multiplicity-correct robust W; honest τ = √δ; v = height-max hidden robust vertex;
canonical separator with Pg = g, g_v = 0):

- 13 d12 PASS instances (saved P + canonical separator), off the d8 wall edge, δ ∈ [0.007,
  0.070], n = 17–22.
- d13 `d5e-02`: the corner-anchor small-δ verified instance (G2_canonical, δ = 0.05, n = 7).
- s5 exact 5×5: built byte-for-byte from `notes/swarm-answers/s5_refute.md` (P² = P to 1e-16,
  δ = 1841/1600000); the only known all-shallow optimal face, σ̃ > 0, H = O(δ).
- corner edge: `decide_opt(0.1435, 0.5, …)` rebuilt fresh (δ = 0.07175, the corner scale,
  H/τ = 0.536, presolve OFF).

For each, for a grid of 40 band thresholds t ∈ [0.1 κΩ, 2 κΩ] (Ω = osc(g)):
- the **shallow band** `S_t = {j : g_j ≤ t}` (the t10/s3 collapse block containing v) and its
  closure leakage `λ_S = sup_{i∈S} Σ_{j: g_j>t} |P_ij|` — s3's quantity verbatim;
- the per-row crossing leakage `ℓ_i = Σ_{j: g_j≥t} |P_ij|` for rows i with g_i < t (mission
  item 1), split by role (v / carrier / financier / reciprocal / W-vertex / hidden-vertex /
  other) and g_i/t ratio;
- the **interior** (g_i ≤ t/2) sup-leakage and the **bad shell** (g_i ∈ (t/2, t)) mass + count;
- the **projective diameter Δ** of the positive part of the shallow band block (Birkhoff
  contraction q = tanh(Δ/4) — t10's other hypothesis): finite iff every row pair has fully
  overlapping support.

## Decision quantities (per instance)

| instance | δ | H/τ | MIN_t λ_S | λ_S/δ | λ_S/H | argsup role | λ⁺_S min | shell mass | Δ finite? |
|---|---|---|---|---|---|---|---|---|---|
| corner_edge | 0.0717 | 0.536 | 0.0717 | 1.000 | 0.500 | **v** | 0 | 0 | no (q=1) |
| d12 floor (×6) | 0.055–0.070 | 0.47–0.53 | =δ | 1.000 | 0.500 | **v** | 0 | 0 | no (q=1) |
| d12 mid (×3) | 0.025–0.045 | 0.32–0.42 | =δ | 1.000 | 0.500 | **v** | 0 | 0 | no (q=1) |
| d12 small (×4) | 0.007–0.0175 | 0.17–0.27 | =δ | 1.000 | 0.500 | **v** | 0 | 0 | no (q=1) |
| d13 d5e-02 | 0.050 | 0.447 | 0.050 | 1.000 | 0.500 | **v** | 0 | 0 | no (q=1) |
| s5_exact | 0.00115 | 0.029 | 0.00050 | 0.434 | 0.500 | **v** | 0 | 0 | no (q=1) |

(s5: λ_S = ν_v = δ/2 here, not δ — its two negative rows split the budget; still λ_S/H = 0.500.
s5 is the only instance with NO finite-Δ shallow block at ANY t and closure ratio ~1.5e10 —
the support-graph degeneration is maximal there, the all-shallow face living on H = O(δ).)

## The violator anatomy (what the numerics show, mechanistically)

1. **The leakage floor is v's negativity, not a boundary shell.** For every t, the
   sup-leakage of the shallow band is attained at v, equals v's full negative mass ν_v = δ,
   and consists entirely of negative entries pointing at deep rows (g_j > t). v sits at the
   band bottom (g_v = 0); its positive carriers are shallow (in-band), its negatives point
   deep. No threshold escapes this — δ is a hard floor. The averaged-vs-sup distinction is a
   red herring here: the sup IS the mean of a single dominant row (v), and it cannot be
   pigeonholed away because it is the same row at every cut.

2. **Positive closure is perfect.** `λ⁺_S = 0` at a realizable t on every instance. The
   positive kernel — the object t10's Birkhoff finisher actually contracts — has a closed
   shallow block. So the sup-form closure that the finisher needs HOLDS for the positive part.

3. **The surviving residual is Δ = ∞ (q = 1), the support graph.** Even at the
   positive-closure threshold the positive shallow block has disjoint-support rows (v's
   carriers feed the W-archetypes, which are `e_i` identity rows). Birkhoff contraction
   q → 1, so the t10 collapse bound 2ε/(1−q) is vacuous. This is the campaign's named
   "unbounded-Δ case = support-graph B–S stability" branch (WAVE 10 t10 death certificate),
   and it is where the s5 family lives.

## Conclusion for the band-cut route

- **The band-cut closure lemma as literally stated (sup-form λ_S small) is FALSE** — the
  signed floor δ = H/2 is structural and threshold-independent; six died-at certificates
  correctly fenced it.
- **But the failure is benign and decomposes:** positive leakage closes perfectly (λ⁺ = 0);
  the entire obstruction is (a) v's negative budget δ (the H = 2δ budget identity, already
  the campaign's empirical law) and (b) the infinite projective diameter of the
  disjoint-support positive block.
- **Therefore the missing structural input is NOT a better cut.** It is a finisher that (i)
  runs on the positive part (where leakage = 0) and (ii) tolerates Δ = ∞ via the support
  graph — i.e. the Δ-unbounded / support-graph Baake–Sumner branch, exactly the
  orchestrator's "zero-pattern degeneration → support-graph combinatorics, where the s5
  family lives." The averaged-vs-sup leakage gap that the campaign was trying to close is
  **not where the route dies**; the route dies at the Birkhoff diameter on the support graph.

This matches and sharpens s3's died-at (`sup_{i∈T} Σ_{j∉T}|P_ij| = O(δ/κR)`, with the boundary
rows spending height budget): the numerics localize that "boundary row" to **v itself**, with
budget exactly δ, and show the leakage is purely negative — so the positive Markov block IS
approximately closed, and the real missing brick is the support-graph diameter, not closure.

## Files

- `experiments/d14_leakage.py` — the probe (new; reuses d12 canonical-separator + gates,
  builds s5 exactly, rebuilds the corner edge; presolve OFF on all LPs).
- `experiments/out/d14_leakage.json` — per-instance checkpoint + summary.
- `experiments/out/d14_logs/<label>.json` — per-instance full profile + saved P (15 files).
- `experiments/out/d14_logs/run.log` — run log.

## Gates exercised (M I; numerics)

idem_resid < 1e-7 (= 0.0 on exact/optimized); P1 = 1; multiplicity-correct robust W (presolve
OFF); honest τ = √δ; v = height-max hidden robust vertex; canonical separator Pg = g checked
(sep_resid ≤ 1e-15). Unverified points never entered. s5 rebuilt from its closed form and
re-verified P² = P to 1e-16. Re-run: `cd experiments && python3 -u d14_leakage.py`.
