VERDICT: DIED-AT the missing shallow-cluster mass cap.

I cannot prove `σ̃_v = O(δ/τ)`. The exact identities give the opposite pressure unless `v` is nearly self-supported. Let `C = conv W`, `U = {j != v : p_j notin C, P_vj > 0}`, `s = σ̃_v = Σ_U P_vj`, and `b = Σ_{j != v, p_j in C} P_vj^+`. Then

```text
Σ_{j in U} P_vj^+ g_j <= δR
H <= (P_vv^+ + s)H + δR
bH <= δR
```

So if `s` is large, the outside carriers are merely forced to be shallow on average:

```text
(1/s) Σ_{j in U} P_vj^+ g_j <= δR/s.
```

That is exactly the all-shallow hidden-web obstruction, not a contradiction. If `P_vv^+` is not close to `1`, the separator accounting even forces `s` to be large up to `O(δ/H)`.

Post-mortem: the mandated chase dies when trying to turn “outside carrier, shallow, and close on average to `v`” into exposure or non-vertexhood. L2/L2′ allow hidden vertices to have a `ρ`-shadow; the sharp carrier shadow only improves the scale of the average shadow; F-ND/ND′ only exposes concentrated rows; W-locality only controls rows already in `W`. A spread shallow hidden carrier in the `ρ`-ball of `v` survives all of these. The needed missing inequality is:

```text
Σ_{j in U, j shallow hidden in the rho-cluster of v} P_vj^+ <= C τ.
```

That is just quantitative Baake-Sumner stability / the 2-cycle exclusion in σ̃ language.

New sub-lemmas:
1. Proven: positive mass from `v` into `conv W` is deep-priced:
   `b <= δR/H`.
2. Proven: outside positive carriers have mean deficit at most `δR/s`.
3. Open: shallow hidden ρ-clusters carry only `O(τ)` positive mass. This is the real s2 gap.

Calibrated probabilities: `P(existential DMF true) = 0.72`; `P(this s2 diagnosis survives audit) = 0.84`. I would put `P(direct σ̃_v <= Cτ true as stated) = 0.40` unless the statement excludes the self-heavy/near-delta window very carefully.

Sharpest structural insight: σ̃ is not a harmless nuisance variable. For `H >> δ`, separator accounting says a hidden top vertex must pay for its height either by self-mass or by positive mass on rows outside `conv W`; positive mass on `W` is too expensive because W-rows are deep. Thus bounding σ̃ directly is essentially the whole hidden-web theorem, not a shortcut around it.