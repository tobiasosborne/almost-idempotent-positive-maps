VERDICT: EXISTENTIAL-SUFFICIENT, provided the existential witness is an **optimal** dual witness.

The universal quantifier over every optimal witness is stronger than needed. For the selected optimal witness with deep mass:

1. DMF lower bound uses only that witness:
   `Σ μ_j g_j >= m*(H - E)`.

2. Exchange holds for every optimal witness:
   from `(♦)` paired with `g`, using `g_v=0`,
   `Σ μ_j g_j + Σ α_k g_k = Σ β_k g_k`.
   Since `α_k >= 0`, `g_k >= 0`, and `0 <= g_k <= R`,
   `Σ μ_j g_j <= Σ β_k g_k <= B R = t* R`.

3. Hiddenness and diameter are witness-free:
   `t* < κ = τ/4`, and the corrected bound is `R <= 2+4δ`.

So the chain closes with one deep optimal witness:
`m*(H - E) <= Σ μ_j g_j <= t*R < κR <= (τ/4)(2+4δ)`.

**Clean Theorem**
Assume existential DMF: for every exact `P` in the canonical frame with `δ <= δ0`, every hidden top vertex `v` admits an optimal exposedness-dual witness `(μ,α,β,γ)` such that
`μ{j : g_j >= H - E(δ)} >= m*`.

Then
`H <= τ(2+4δ)/(4m*) + E(δ)`
or equivalently
`H <= τ[(2+4δ)/(4m*) + E(δ)/τ]`.

Proof: choose a global height-maximizing hidden vertex `v`. Apply existential DMF to get the selected optimal witness. The deep mass gives `Σ μg >= m*(H-E)`. The exchange gives `Σ μg <= t*R`, and hiddenness gives `t*R < κR`. With `κ=τ/4` and `R <= 2+4δ`, divide by `m*`.

Important normalization: the displayed bound has `+E`, not `+E/m*`, because the chain is `m*(H-E)`. A `+E/m*` term would correspond to a different hypothesis `Σ μg >= m*H - E`.

Thus
`δ >= H^2 / [(2+4δ)/(4m*) + E(δ)/τ]^2`.
If `E(δ)/τ -> e`, the asymptotic constant is
`a = (1/(2m*) + e)^(-2)`.
Only when `E=o(τ)` do we get `a -> 4m*^2`. If `E=C_D δ/τ=C_D τ`, then `e=C_D`, so the constant is `(1/(2m*)+C_D)^(-2)`.

**Edge Cases**
`t*=0`: exchange still holds and gives `Σ μg <= 0`; with `g>=0`, the chain forces `H<=E` under DMF. No α-localization is needed.

`H<=E`: theorem is vacuous but valid. Any useful `δ >= aH²` then depends on controlling `E/τ`.

Non-top `v`: not WLOG for the exchange, because `g>=0` can fail. For HLC choose a row vertex maximizing `dist(p_i,conv W)`; by convexity such a vertex exists, and if `H>0` it is not in `W`, hence hidden. For this top choice, `g>=0`.

W-rows are deep: if `w in W`, then `p_w in conv W`, so `φ(p_w) <= sup_{conv W} φ = 0`; hence `g_w = H - φ(p_w) >= H`.

P(this survives af-formalization): `0.92`, excluding the truth of DMF itself.