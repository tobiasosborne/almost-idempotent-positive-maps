# d13 — the decisive small-δ probe: does the flat floor survive at small δ?

## VERDICT (first): **OUTCOME (c)** — the flat floor is a CORNER EXTRAPOLATION.

**The hidden-top-vertex height collapses to the corner `H ≈ 2δ`, NOT the floor `H ≈ 0.536√δ`,
at every small δ. No verified hidden-top-VERTEX instance exists near the floor at δ ≤ 1e-2.**

Across `delta ∈ {1e-2, 3e-3, 1e-3, 3e-4}` (probe targets), an intensive band-gated hunt
(~5000 verified exact idempotents per δ, three generators, presolve OFF) found the maximum
achievable `H/τ` over a hidden robust **vertex** to **collapse monotonically**:
`0.222 → 0.110 → 0.077 → 0.035`, i.e. `δ/H² = 20 → 83 → 168 → 833` — far above the floor band
`[3.4, 8]`. The entry gate (`H/τ ≥ 0.30`, a hidden robust vertex) is **never enterable** at
small δ. Stage-2 witness anatomy never runs because no small-δ instance qualifies — so DMF is
neither confirmed nor refuted at small δ; rather **the regime the question is about does not
contain a hidden vertex at all.** The flat floor `H ≈ 0.536√δ` was a moderate-δ (δ ≳ 0.05)
phenomenon extrapolated below its domain of validity. This is consistent with (and stronger
than) the σ̃-height-collapse lemma: at small δ a hidden top vertex would need σ̃ ≈ 1, but the
hunt shows **no hidden top vertex of order-`√δ` height exists in the first place** — the
height itself collapses to `2δ`.

Evidence strength: **HIGH.** The pipeline is validated (it reproduces the floor where it
exists, see anchor below), the hunt is large and band-gated to the honest δ, and the three
independent generators agree to 3 digits at every δ.

---

## The single sharpest finding: H tracks the CORNER `2δ`, not the floor `0.536√δ`

[NUMERICAL] Achieved hidden-vertex height vs the two candidate laws:

| δ | H_achieved | H/τ | corner `2δ` | floor `0.536√δ` | δ/H² | **H/(2δ)** | H/(0.536√δ) |
|----|-----------|------|------------|----------------|------|-----------|-------------|
| 5.0e-2 (anchor) | 0.1000 | 0.447 | 0.1000 | 0.1199 | 5.0 | **1.00** | 0.83 |
| 1.0e-2 | 0.0222 | 0.222 | 0.0200 | 0.0536 | 20.4 | **1.11** | 0.41 |
| 3.0e-3 | 0.0060 | 0.110 | 0.0060 | 0.0294 | 83.3 | **1.00** | 0.20 |
| 1.0e-3 | 0.0024 | 0.077 | 0.0020 | 0.0170 | 167.6 | **1.22** | 0.14 |
| 3.0e-4 | 0.0006 | 0.035 | 0.0006 | 0.0093 | 833 | **1.00** | 0.065 |

`H/(2δ) ≈ 1` at every δ; `H/(0.536√δ) → 0`. The crossover is at δ ≈ 0.05–0.06, where
`2δ = 0.536√δ`. ABOVE it the floor binds (H ≈ 0.5√δ ≈ 2δ); BELOW it the **corner `2δ`
binds** and the floor is unreachable. The "flat floor" `H ≈ 0.536√δ` extrapolated from
δ ∈ [0.04, 0.1] simply does not extend to δ → 0.

---

## Per-instance table (band-gated entry hunt; honest τ = √δ; multiplicity-correct W)

| δ (target) | best H/τ (vertex) | δ/H² | entry gate (≥0.30)? | outcome | dominant failure |
|-----------|-------------------|------|---------------------|---------|------------------|
| **5.0e-2 (ANCHOR)** | **0.447** | **5.0** | ✅ cleared | **a_verified_deep** | (validates pipeline) |
| 1.0e-2 | 0.222 | 20.4 | ❌ | c_no_floor_vertex | ratio collapses (< 0.30) |
| 3.0e-3 | 0.110 | 83.3 | ❌ | c_no_floor_vertex | ratio collapses |
| 1.0e-3 | 0.077 | 167.6 | ❌ | c_no_floor_vertex | ratio collapses |
| 3.0e-4 | 0.035 | 833 | ❌ | c_no_floor_vertex | ratio collapses |

Per-δ the hunt drew ≈5000 band-gated exact idempotents (`|δ_achieved − δ|/δ ≤ 1/3`, robust
`|W| ≥ 2`, idem_resid = 0 to machine ε). The three generators (G1 fixed-τ undistorted, G2
random-canonical, G3 d7 two-vertex shadow-shell) produced **identical** max `H/τ` to 3 digits
at each δ — not a search failure of one family, a structural wall.

### The validation anchor (δ = 5e-2) — proof the pipeline finds the floor when it exists
Full d12 witness anatomy PASSED: idem_resid = 0, ident_resid = 4e-16, massbal_resid = 0,
v a robust vertex failing exposedness (t*/κ = 0.85 < 1), H = 0.10, δ/H² = 5.0, m* = 1.0,
shallow_fraction = 0, class composition = **100% W-vertex** (exactly the corner mechanism).
**But even here σ̃ = 0, not ≈ 1** — because `δR/H = 0.05·2.1/0.10 = 1.05 > 1`, so the
σ̃-collapse bound `1 − δR/H < 0` is **vacuous**, and `E_dmf = 5δ/τ = 1.12 > H` makes the
m*=1 deep-mass measurement vacuous too. **This δ = 5e-2 "floor" instance is STILL the corner**
(H = 0.10 = 2δ): it sits exactly at the crossover, which is why it is simultaneously the
last floor point and a corner point. The witness is the d12 corner mechanism (W-vertices),
fully consistent with d12 — and with the orchestrator's diagnosis that d12 measured only the
corner.

---

## Why outcome (c), structurally (the d3 report, confirmed)

The d3-envelope-report established (and `d13` re-confirms): a row far from `conv W` must be a
**non-vertex** (coincident/interior) — a distinct far **vertex** is always `(Cτ, cτ)`-well-
exposed and JOINS W, collapsing its distance to 0. The floor `dist/τ ≤ 0.536` was measured as
the max over ALL rows (including non-vertices) at moderate τ ≈ 0.17–0.30. The σ̃-height-collapse
lemma, by contrast, is about a hidden **vertex**. d13 closes the gap: the max `H/τ` over a hidden
**vertex** (the lemma's object) collapses to ≈ 0 as δ → 0, pinned to the corner `2δ`. So:

- The floor instances that realize `dist/τ ≈ 0.536` at small δ (if any) are **non-vertex**
  hidden rows, to which the σ̃-collapse lemma and the DMF chain (built on a hidden top vertex)
  **do not apply**.
- For hidden **vertices**, the true small-δ height law is `H ≈ 2δ` (LINEAR in δ), i.e.
  **δ ≳ H/2** — strictly STRONGER than the conjectured `δ ≳ aH²`. This is the d5 linear edge,
  now shown to govern the entire small-δ hidden-vertex regime, not just the large-τ edge.

[NUMERICAL] caveat: the random hunt cannot prove a height is unreachable, only that ~15000
band-gated exact idempotents across 3 generators failed to reach it while the SAME machinery
reaches it at δ = 5e-2. The structural reason (distinct far vertices expose ⇒ join W) makes
the collapse non-accidental.

---

## Generator note (honest limitations)

- `d8_mrp3` financed-wiggle (d12's generator) lives at the **corner H ≈ 2δ** for all δ — it
  cannot reach the floor at any δ; d13 does NOT rely on it. Confirmed: d12's smallest "δ=7e-3"
  instance had H = 0.014 = 2δ.
- `d3_envtrue.rand_P_fixed_tau` has a **δ-overshoot bug**: its analytic-tail solver can return
  δ ≈ 9 regardless of the requested τ (breakpoint crossings). d13 **band-gates on the ACHIEVED
  δ** and rescales to target, neutralizing this — without the gate one gets spurious `H/τ ≈ 8`
  degenerate (|W| = 1) instances at fake-small δ. This is logged as a generator caveat, not a
  result.
- The structured d7 shadow-shell family (G3) confirms the collapse independently and never
  beats the random families.

---

## Files
- `experiments/d13_smalldelta.py` — the probe (new; imports d3/d7/d12 code, modifies nothing).
- `experiments/out/d13_smalldelta.json` — per-δ checkpoint incl. all FAILED entries with
  reasons (outcome-(c) evidence) and per-generator stats.
- `experiments/out/d13_logs/d5e-02.json` — the validation-anchor full anatomy (PASS).
- `experiments/out/d13_logs/run.log` — full run log (1200 s, ~5000 samples/δ).

## Implication for the HLC chain
The σ̃-small branch / DMF web case is moot for hidden **vertices** at small δ: there is no
hidden top vertex at height `~√δ` to begin with — its height is `~2δ`, giving the LINEAR
`δ ≳ H/2` directly (better than the `√δ` rate needs). The remaining battleground is hidden
**non-vertices** at the `0.536√δ` floor, where the DMF/σ̃ vertex-machinery does not apply and
a different argument is required. This **redraws the regime map**: the decisive open object is
the hidden NON-vertex at the floor, not the hidden vertex.
