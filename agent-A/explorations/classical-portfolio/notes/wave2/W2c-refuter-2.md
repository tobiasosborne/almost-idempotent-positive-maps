**Verdict:** no refutation found. The best exact combined escape I can honestly point to is still the d7 ring shell: `δ/H² = 280.123955...` from [experiments/out/d7_tradeoff.json](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/experiments/out/d7_tradeoff.json:505). The formal shadow-only construction can make `δ/H² -> 0`, but it is not an exact idempotent.

**Constructed attack family:** set `H = Dτ`, spacing `s = αρ < ρ`, chain length `m ≈ H/s = D/(4α)`, and split each high level into distinct near-coincident pairs with separation `ε` satisfying `τ² << ε < ρ`. Add same-height carrier rows just outside the `ρ` ball to block exposers, and let carriers cycle to re-inject height. Ignoring `P²=P`, choosing `D -> ∞` gives the fake refuter scale `δ/H² = 1/D² -> 0`.

**Wall hit:** exactness forces reciprocal carriers. In the rank-2/single-mode model this is **PROVED**: if rows are `p_i = q + t_i r`, row-stochastic idempotence gives
`Σ q_i t_i = 0`, `Σ r_i = 0`, `Σ r_i t_i = 1`, hence
`diam₁(rows) = (max t-min t)||r||₁ ≥ 2`.
So a nonconstant exact mode cannot live inside a sub-`ρ` near-coincident cluster. The missing mass reappears as a `ρ`-far carrier; if that carrier exposes, it joins `W` and collapses `H`; if it is hidden, the same demand recurses.

**Best scaling achieved:** for exact families, only `δ/H² = Ω(1)`; I did not get an `o(1)` construction. Canonical frames give the stronger `δ ≥ H/2`; the adversarial helper-ring exact search enters the target geometry only after `H` collapses, with floor `≈280`.

**Lemma name:** `lem-high-carrier-localization`:
an exact high ρ-connected hidden carrier system either produces a well-exposed high carrier that enters `W`, or pays `max neg ≥ cH²`. This is the precise wall; it packages the remaining dual-localization/no-staircase gap.