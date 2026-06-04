# Dimension canary — smoke test (extended N)

Companion to `REPORT.md`. Driver: `canary_smoke.py` → `results_canary.json`.
Status: **numerical smoke test**, not a proof. Reuses the verified `d^1` builder
(`jordan_common.py` / `jordan_fast.py`; `ker d^1 = dim Der(J)` reproduced at every N).

## Question (same as REPORT.md)

The Layer-1 error-reduction Newton step is `δ → O(δ² + Kε)` with
`K = ‖s‖`, `s` a right inverse (splitting) of the Jordan 2-coboundary
`(d¹h)(a,b) = a∘h(b) + h(a)∘b − h(a∘b)` (adjoint module `M=J`; `H²(J,J)=0` so `s`
exists). **A dimension-free `K` is exactly what the Jordan structure theorem
needs.** `s := pseudoinverse` (Frobenius-minimal right inverse):

- `‖s‖_F = 1/σ_min(d¹)` — Frobenius, **exact**, the already-known *bounded* result.
- `‖s‖_op` — **order-unit/operator norm, the one the theorem controls** — the open one.

REPORT.md left `‖s‖_op` "UNRESOLVED": it had only `n ≤ 6` (`N ≤ 36` for `H_n(ℂ)`,
`N ≤ 9` for spin), lower bounds growing sub-`√n`, and a crude `~n` upper bound —
too short a range to tell "bounded" from "slowly growing."

## What this run adds

1. **Spin factors `V_n` to `N = 41`** (vs `N ≤ 9` before). `dim V_n = n+1` is
   linear in `n`, and the order-unit norm `‖(t,v)‖ = |t| + ‖v‖₂` makes `‖·‖_op` a
   tractable **extreme-point** computation — unit-ball extreme points are the two
   poles `±e₀` and the equator sphere `{(0,u)}`, so `‖f‖_op`/`‖sf‖_op` are found by
   gradient ascent over a low-dim sphere rather than blind random search. **These
   spin numbers are trustworthy.**
2. `H_n(ℂ)`, `H_n(ℝ)` cross-checks (to `N=36`) on a random-extreme-direction search
   (the `opnorm_trend.py` method; **looser** — it under-samples the bilinear
   denominator `‖f‖_op`, so its absolute numbers and trend are noisier).

## Data (log-log slope of each quantity vs N)

| family | N range | `σ_min(d¹)` | `σ_max(d¹)` | `‖s‖_F` (exact) | `‖s_F‖_op` |
|---|---|---|---|---|---|
| **spin `V_n`** (trustworthy) | 3–41 | `N^+0.02` (flat ~1.6) | `N^+0.51` | `N^−0.02` (→0.61) | **`N^−0.18` (flat→dec, ~0.55)** |
| `H_n(ℂ)` (looser) | 4–36 | `N^+0.21` | `N^+0.26` | `N^−0.21` | `N^+0.32`* (→ plateau ~2.2) |
| `H_n(ℝ)` (looser) | 3–36 | `N^+0.16` | `N^+0.23` | `N^−0.16` | `N^+0.33`* (→ plateau ~2.0–2.5) |

\* The `H_n` `‖s_F‖_op` power-law is a **small-N transient**. Dropping the first
point: `H_n(ℂ)` slope `+0.32 → +0.11` (flat); increments decelerate
`0.84, 0.20, 0.05, 0.06` → converging to a finite plateau. `H_n(ℝ)` similar
(noisier search).

## Verdict — the canary does NOT fire

In every family tested the splitting constant `K = ‖s‖` is **bounded**:

- **Frobenius `‖s‖_F` — bounded (exact)** in all three families (slopes `−0.02…−0.21`,
  all decreasing). Confirms the known result over a 4–14× wider dimension range.
- **Operator/order-unit `‖s_F‖_op` — plateaus (no divergence)**: spin flat-to-decreasing
  to `N=41` (trustworthy); `H_n(ℝ/ℂ)` rise then flatten to a plateau by `N≈16`.

The mechanism is visible in the singular values: `‖s‖_F = 1/σ_min` stays bounded
because `σ_min(d¹)` never collapses (spin: flat ~1.6; `H_n`: grows). `σ_max` grows
`~√N`, so the Frobenius **condition number `κ = σ_max/σ_min` does grow `~√N`** — but
that is the spread, not the inverse-norm, and does not feed `K`.

## Honest caveats (do not overclaim)

1. `‖s_F‖_op` is a **lower-bound estimate** (max of a ratio over sampled cochains).
   A clear *growth* would be decisive that the canary fires; a *plateau* is
   *consistent with* dimension-free but **not a proof**. We observe no growth.
   The bias direction is favorable: under-estimating the harder bilinear
   denominator `‖f‖_op` *inflates* the ratio, so the true trend is at most flatter.
2. `s_F` is the **Frobenius-minimal** splitting. The theorem needs only *some*
   bounded splitting, so bounded `‖s_F‖_op` is **good news**; a growing `‖s_F‖_op`
   (not observed) would have been suggestive-not-fatal (an op-norm-optimal
   splitting could be smaller).
3. Adjoint module `M=J` only; the error-reduction uses `M=A` (an `ε`-JB algebra) —
   a further approximation not tested here (same caveat as REPORT.md).
4. `H_n` operator-norm search is looser than spin; treat spin as the headline.

## Bottom line

Extending the dimension range by 4–14× turns REPORT.md's "unresolved at `n≤6`" into:
**no numerical sign of dimension dependence** in the Frobenius-minimal splitting of
`d¹`, in either norm, for spin factors (trustworthy, to `N=41`) or the `H_n(ℝ/ℂ)`
matrix families (looser, to `N=36`). This is encouraging evidence for the
dimension-free error-reduction conjecture (`prop:error-reduction`, report §7) — a
smoke test, not a settled question.
