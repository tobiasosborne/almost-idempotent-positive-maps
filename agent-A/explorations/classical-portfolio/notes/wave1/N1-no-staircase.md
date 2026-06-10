Honest verdict: **not proved as stated**. The spectral route stalls at a precise missing localization inequality.

**PROVED conditional algebra.** Grant a single affine height `h` with `h|conv W=0`, `0≤h≤D≤2+4δ`, and `h(v_j)≥H-jρ`. Let `S` be the first `M≈H/(2ρ)` chain rows, so `h≥H/2` on `S`. Write `P=P⁺-P⁻`, `U={h≥H/2}`, `L={h<H/2}`. Since `h=Ph`,

```text
h_S - P⁺_{S,S} h_S
= P⁺_{S,U\S} h_{U\S} + P⁺_{S,L}h_L - P⁻_{S,*}h_* .      (1)
```

If `P⁺_{S,S}` is strictly triangular, then it is nilpotent and

```text
h_S = (I + N + ... + N^{M-1}) RHS.
```

Using L5, `P⁺_{S,L}h_L = O(δ)`, and `P⁻_{S,*}h_* = O(δ)`. Therefore nilpotence forces

```text
max_j P⁺_{v_j,U\S} h  ≥  cρ - O(δ).                     (2)
```

So the spectral argument proves only this: **an acyclic chain forces substantial positive transition to off-chain high rows**, unless negativity is already much larger than the current regime.

**Failing inequality.** To finish the desired `δ ≥ aH²`, one would need something like

```text
P⁺_{v_j,U\S} h  ≤  Cδ
```

or a theorem saying that such off-chain high carriers either form a usable same-shell cycle or themselves cost `Ω(H²)`. L5 does not give this. It controls high-to-low leakage, not high-to-high support outside the selected chain. This is the same localization gap recorded in [notes/d6-codex-frame-transfer.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/d6-codex-frame-transfer.md).

**Minimal test configuration.** Test a two-lane staircase:

```text
low anchors A ⊂ W at height 0
chain vertices v_j at heights H-jρ
carrier rows u_j at the same heights as v_j, with ||u_j-v_j||₁<ρ
shadow edges v_j -> v_{j+1}, acyclic
positive exactness mass P⁺_{v_j,u_j} ≈ 1
carriers u_j either self-return or cycle among carriers
```

Then the chain submatrix is nilpotent, low leakage is negligible, but height is reproduced through `u_j`. The decider should minimize `δ/H²` over exact `P=ΛR`, `RΛ=I`, while recomputing `W`. Existing nearby helper-shell tests support the conjecture, but they do not prove this localization step; see [experiments/out/d7_tradeoff.json](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/experiments/out/d7_tradeoff.json).