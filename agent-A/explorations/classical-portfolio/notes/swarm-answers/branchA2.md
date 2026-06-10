VERDICT: DIED-AT. No unconditional Branch A proof. The LP-duality route dies exactly at the missing α-localization inequality.

I granted the favorable case where `v` is a top vertex for the distance-dual functional. Let `φ` be the ℓ¹-distance dual, normalized by `max_{w in W} φ(w)=0`, `φ(p_v)=H_v`, and set

```text
g_i := H_v - φ(p_i),      R := osc(g).
```

Then exactness gives `g = Pg`, `g_v=0`. The audited F-GB gives only

```text
sum_k P^+_{vk} g_k <= δ R,
so positive mass σ_v can sit at average level <= δR/σ_v.
```

For failed exposedness, the C10 dual witness is

```text
μ in Prob(F), α,β >= 0,  sum β_i < κ,
sum_{j in F} μ_j (p_j-v) = sum_i (β_i-α_i)(p_i-v).
```

Pairing with `φ` gives the exchange identity

```text
sum_{j in F} μ_j g_j + sum_i α_i g_i = sum_i β_i g_i <= κ R.        (available)
```

This controls only **height in the one affine coordinate `g`**. It does not control α-mass, α-radius, or high zero-face geometry. The needed step is something like

```text
sum_i α_i dist_1(p_i,p_v) <= C σ_v τ (1 + sum_i α_i)                (needed)
```

or an analogous statement forcing the α-carriers, or the μ-blockers they absorb, into an `O(σ_v τ)` neighborhood or into a supplier structure priced by `σ_v`. I do not see a derivation of this from `P²=P`, row-negativity, F-GB, F-E, F-SS, F-ND, F-WR, or F-BC. Exactness binds actual row coefficients of `P`; C10’s `α` is a dual slack variable and is not tied to the row `v`’s external coefficient mass.

**Post-mortem.** The route proves a useful reduction: any counterexample to Branch A must have low-`g` far blockers or α-carriers on a high zero-face. This matches the recorded crux in [fable-hlc-attack.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/fable-hlc-attack.md:219) and the audited residual in [endgame-sigma-wall-residual.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/endgame-sigma-wall-residual.md:4). The measured σ-law in [mrp-decider-report.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/mrp-decider-report.md:42) is still strong evidence, but it is not supplied by this LP exchange alone.

**New sub-lemmas from this attempt.**

1. Distance-dual fixed-deficit lemma: for top `v`, the dual profile is fixed by `P`, hence F-GB applies to `g`.
2. C10 exchange identity: every failed-exposedness dual satisfies  
   `Σ μ g + Σ α g = Σ β g <= κR`.
3. Conditional close: Branch A would follow from an α-localization or supplier-pricing lemma tying C10 slack mass to `σ_v`. That is exactly the unproved step.

**Calibration.** `P(Branch A true) ≈ 0.75`, mainly from d8/d9 numerics. `P(this LP-duality/exchange proof survives audit without a new localization lemma) ≈ 0.10`.

What I learned: the budget binds through the **supplier system**, not through `φ` directly exposing `v`. F-GB says `v` can spend only `δR` of deficit budget through its positive external mass, but C10 can hide the exposedness obstruction in low-`g` high-zero-face rows. The missing theorem must prove those rows are not free: they must either be close to `v`, become well-exposed themselves, or force a row-negativity cost of order `H_v²/σ_v²`.