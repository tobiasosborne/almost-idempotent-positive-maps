VERDICT: DIED-AT: the large-σ shadow reduces Branch B to a sharper carrier-blocker coupling inequality, but does not prove it. This is the same wave-5 wall in a more precise form: the missing step is no longer “there is a top-band far blocker,” but “the far blocker must be coupled to v’s sharp-shadow carrier measure.”

**Post-Mortem**
Let `A={j≠v:P_vj>0}`, `σ=Σ_A P_vj=σ_v`, and `ν=Σ_{j≠v}P_vj^-≤δ`. Define the normalized positive carrier average

```text
q_v = (1/σ) Σ_{j∈A} P_vj p_j .
```

From the row identity,

```text
σ(q_v - p_v) = ν(r_v - p_v)
```

for some convex average `r_v` of negative off-site rows. Hence

```text
||q_v-p_v||₁ ≤ (2+4δ)ν/σ ≤ 2(2+4δ)δ      since σ≥1/2.
```

Also, since `g=Pg`, `g_v=0`, and `g≥0`,

```text
Σ_{j∈A} P_vj g_j = Σ_{j≠v} P_vj^- g_j ≤ δR,
```

so

```text
(1/σ)Σ_{j∈A}P_vj g_j ≤ δR/σ ≤ 2δR.
```

Thus v’s positive off-site carriers form a convex measure which is both geometrically `O(δ)` from `p_v` and almost entirely in the ultra-top band. In particular,

```text
λ{g ≥ κR} ≤ δ/(σκ) ≤ 8τ,
```

where `λ_j=P_vj/σ` on positive carriers.

This is strong, but it still does not close Branch B. The height-functional wall says Branch B would follow if every `ρ`-far row had `g≥κR`. Failed exposedness gives a `ρ`-far top-band blocker through the C10 dual witness. The sharp-shadow measure gives top-band carriers for v. I do not see any audited fact forcing those two objects to overlap.

The remaining inequality is:

```text
λ({j : ||p_j-p_v||₁ ≥ ρ and g_j < κR}) ≥ c
```

or a substitute proving that if this λ-mass is zero, then the ρ-ball cluster of v is already `(ρ,κ)`-exposed.

Current tools do not give that. C10 controls a dual blocker measure `μ` and slack `α`, not v’s row coefficients. F-GB gives top-band mass but not far-vs-near localization. F-E would close only if some row is forced to put positive mass on high-energy blocker sites; present facts still allow top-band blockers to be positive-mass orphans. F-WR/F-BC need side conditions that are exactly the missing carrier/blocker linkage.

**New Sub-Lemmas**
1. Positive-carrier sharp shadow: proved above. It strengthens B3’s signed shadow by showing v’s actual positive off-site row coefficients average to `O(δ)` from `p_v` and have mean deficit `≤δR/σ_v`.

2. Carrier dichotomy: either a positive fraction of v’s sharp-shadow carriers are `ρ`-far top-band rows, or v has an `O(δ+τ)` convex shadow supported inside its `ρ`-ball. The second case is exactly the ρ-ball exemption and does not contradict hiddenness without a cluster-exposure lemma.

**Calibration**
`P(Branch B true) ≈ 0.80`.

`P(this died-at diagnosis survives audit) ≈ 0.87`; the positive-carrier shadow lemma itself is high-confidence, about `0.93`.

**Best Closing Suggestion**
Run or prove a targeted carrier-blocker coupling lemma: in the canonical-W hidden-top setup with `σ_v≥1/2`, a C10 far top-band blocker must receive nontrivial mass from v’s positive carrier system, or from rows positively fed by that system. This is the exact place to apply `P²=P` to the blocker/financing row rather than to v alone.