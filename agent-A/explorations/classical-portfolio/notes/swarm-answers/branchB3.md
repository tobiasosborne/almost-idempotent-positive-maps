VERDICT: DIED-AT the uniform wall-functional inequality.

Chosen strategy: exposedness-LP dual / wall-functional route, because Branch B is numerically a margin-pinning event: `t* = κ` at `H/τ ≈ 0.536`.

What I got:

1. **Large-σ sharp shadow.** If `σ_v >= 1/2`, then
   ```text
   dist₁(p_v, conv{p_j : j ≠ v}) ≤ (2+4δ)δ/(σ_v-δ) ≤ 12δ    (δ≤1/4).
   ```
   This follows by normalizing the off-self row identity and using F-SS / diameter `≤2+4δ`.

2. **Top-band concentration.** In the top-deficit setup, F-GB gives
   ```text
   P_v^+{g ≥ ell} ≤ δ R / ell.
   ```
   With `σ_v >= 1/2`, at least `1/4` positive off-site mass sits in `g ≤ 4δR`. So Branch B forces a real high zero-face carrier cluster, not a deep supplier.

Why it does not close: those two facts only put the obstruction into a tiny top band. They do **not** prove the exposedness LP value
```text
t_v* := max_{0≤h≤1, h(v)=0} min_{||p_j-p_v||₁≥ρ} h(p_j)
```
satisfies `t_v* ≥ κ`. The missing inequality is precisely
```text
σ_v ≥ 1/2 and H_v > B_B τ  ⇒  t_v* ≥ τ/4.
```
Equivalently, one needs a uniform high-zero-face localization/wall-functional lemma proving that the top-band carrier either contributes a `W` vertex or cannot remain a ρ-far blocker. Current audited facts do not give this: C10 still has uncontrolled `α` mass, and F-ψ is explicitly not confirmed because non-`S`-full far rows can trade `S`-deficit against the `λφ` term.

Audited facts used: F-SS, F-GB with the audited `δR` constant, F-WR/F-BC only as constraints, and F-ψ only as a named open gap. The d8/d9 certificates strongly support the wall and identify the blocker geometry, but they remain numerical blueprints, not an all-frame proof.

New sub-lemmas: the large-σ sharp shadow and the top-band concentration above.

Calibrated: `P(Branch B true) ≈ 0.78`; `P(this DIED-AT diagnosis survives audit) ≈ 0.88`.