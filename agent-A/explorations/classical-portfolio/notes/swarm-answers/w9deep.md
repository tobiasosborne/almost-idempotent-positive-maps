VERDICT: PROVED, with one caveat: this proves the formal σ̃-small branch by height collapse, not by proving RW itself is optimal.

For `0 <= s < 1`, take

`m(s) = 1`,  
`E_s = δ R / (1 - s)`.

In the requested template, since `δ = τ^2` and `R <= 2 + 4δ <= 3` for `δ <= 1/4`,

`E_s <= (3 / (1 - s)) · (δ/τ + sR)`,

so one valid explicit choice is

`f(s) = 3 / (1 - s)`.

**Proof**

Use the literal σ̃ convention:

`σ̃_v = sum_{p_k notin conv W} (P_vk)_+`

including the self row if `p_v notin conv W` and `P_vv > 0`. If future code excludes self, replace σ̃ by `σ̃ + (P_vv)_+`.

Let

`C = { k : p_k in conv W }`,  
`O = { k : p_k notin conv W }`,  
`ν_v = sum_k (−P_vk)_+ <= δ`.

Since `v` is the top row for the canonical separator, `φ(p_i) <= H` for every row `i`; otherwise that row would have distance to `conv W` larger than `H`. Hence

`g_i = H - φ(p_i) >= 0`, `g_v = 0`, and `0 <= g_i <= R`.

Also `g = Pg`, so the `v` row gives

`0 = g_v = sum_k P_vk g_k`.

Split into positive and negative parts:

`sum_k (P_vk)_+ g_k = sum_k (−P_vk)_+ g_k <= ν_v R`.

For every `k in C`, `φ(p_k) <= 0`, so `g_k >= H`. The positive mass on `C` is

`M_C = sum_{k in C} (P_vk)_+ = 1 + ν_v - σ̃_v`.

Therefore

`(1 + ν_v - σ̃_v) H <= sum_{k in C} (P_vk)_+ g_k <= ν_v R`.

If `σ̃_v <= s < 1`, then

`H <= ν_v R / (1 + ν_v - σ̃_v) <= δ R / (1 - s) = E_s`.

Now take any optimal exposedness-dual witness `(μ, α, β)`. The dual normalization gives `sum μ = 1`, and all row deficits satisfy `g_i >= 0`. Since `H - E_s <= 0`,

`μ{ g >= H - E_s } = 1`.

So an optimal witness exists with deep mass at least `m(s)=1`.

**New Sub-Lemmas**

1. `top-separator-nonnegative`: for the canonical top separator, `g_i >= 0` on every row.
2. `sigma-tilde-height-collapse`: if `σ̃_v <= s < 1`, then `H <= δR/(1-s)`.
3. `optimal-witness-vacuous-depth`: if `H <= E`, every optimal witness has `μ{g >= H-E}=1`.

RW remains useful as a non-optimal feasible witness: when `H >= ρ`, its carrier witness has deep feasible mass at least roughly `1-s`. But RW optimality beyond the measured d8/d12 families is still not proved.

`P(true) = 0.90`  
`P(survives audit) = 0.80`, with the main audit risks being the exact σ̃ convention and the “top” hypothesis needed for `g >= 0`.