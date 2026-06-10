VERDICT: CONSTANT-DOWNGRADE: the identities and mechanisms are real, but `19δ/E` and `+2.2δ` are not justified under the broader `osc(g) ≤ H+2+4δ` normalization as written.

Let `R = osc(g)`, and write a row as `p = q - n`, with `|n|_1 ≤ δ`, `|q|_1 = 1+|n|_1`. Since `Pg=g`,

```text
Γ_i = P(g²)_i - g_i² = Σ_k P_ik (g_k - g_i)².
```

So `PΓ = P²(g²) - P(g²) = 0`. Also
`-δR² ≤ Γ_i ≤ (1+δ)R²`, and `||Γ||∞ ≤ (1+2δ)R²`.

For starvation, for row `j` and `S={k: Γ_k ≥ E}`:

```text
E q(S) ≤ Σ_S q_k Γ_k
       ≤ Σ n_k Γ_k - Σ_{S^c} q_k Γ_k
       ≤ δ(1+δ)R² + δR²(1+δ)
       = 2δ(1+δ)R².
```

Thus the clean derived bound is

```text
positive mass on {Γ ≥ E} ≤ 2(1+δ)R² · δ/E.
```

If `R≤3`, `δ≤1/4`, this gives `22.5δ/E`, not `19δ/E`. The note’s arithmetic in [notes/fable-hlc-attack.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/fable-hlc-attack.md:176) and Stage-5 line 430 needs a stronger `R`/small-`δ` hypothesis.

Low-energy localization survives with the same caveat:

```text
q{|g_k-g_j|≥Δ} ≤ (Γ_j + δR²)/Δ²,
```

so `(E0+9δ)/Δ²` follows if `R≤3`.

For the g-budget, from `g_j=Σqg-Σng` and `g≥0`,

```text
σℓ ≤ g_j + δ sup(g) = g_j + δR.
```

The advertised `g_j+2.2δ` is valid only if `R≤2.2` is separately available; §1.2/Stage-5 instead cite `R≤H+2+4δ`.