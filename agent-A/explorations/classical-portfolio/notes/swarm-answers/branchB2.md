VERDICT: DIED-AT, not proved.

The explicit functional I would use is the ℓ∞ dual height certificate. Let `C=conv W`, choose a dual `γ` with `||γ||_∞<=1`, `γ(p_v)=H`, `γ<=0` on `C`, and set

```text
g_i := H - γ(p_i),   R := max_i g_i <= H + 2 + 4δ,
h_0(p_i) := g_i / R.
```

For a global height maximizer this gives `0<=h_0<=1`, `h_0(v)=0`, and every `W` row has margin at least `H/R`. If all `ρ`-far rows satisfied

```text
g_i >= κR,                                            (NEEDED)
```

then `h_0` would expose `v`. Since `κ=τ/4`, `R≈2`, the wall is linear:

```text
H/R >= κ  roughly means  H >= τ/2.
```

That is exactly why the numerical wall lands near `H/τ=0.536`.

Where it dies is the missing top-band blocker bound:

```text
needed:   inf{g_j : ||p_j-p_v||_1 >= ρ} >= κR
available from exactness at v:
          P_v^+({g_j >= ell}) <= δR/ell.
```

With `ell=κR`, this only gives

```text
P_v^+({g_j >= κR}) <= δ/κ = 4τ.
```

So when `σ_v>=1/2`, almost all external supplier mass is forced into the bad band `g_j<κR`; it does not prove those rows are within the exempt `ρ`-ball or separable by a coordinate tie-breaker. This is the same missing `ψ`-gap recorded in [audit-summary.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave4/audit-summary.md:9) and the residual note [endgame-sigma-wall-residual.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/endgame-sigma-wall-residual.md:9).

New sub-lemmas from this attempt:

1. Height-functional wall lemma: if the dual deficit satisfies `g_j>=κR` on all `ρ`-far rows, then `v` is exposed. Asymptotic threshold: `B_B>1/2`.
2. Supplier top-band lemma: if `σ_v>=1/2`, then at least `σ_v-4τ` external positive mass from `v` lands in `g<κR`.

The coordinate/supplier-site functional also dies at the same point: far supplier or financing rows can keep nearly the same combined height/site score. The capped deficit `max(g-cap,0)` is useful diagnostically but is not affine, so it is not an exposedness functional.

Calibrated probabilities: `P(Branch B true) ≈ 0.75` from the d8/d9 numerical certificates; `P(this explicit construction survives audit as a proof) ≈ 0.15` without a new ψ-gap/top-band localization lemma.

Why the margin grows linearly in `H`: the height certificate lifts `W` rows by `H`, while the normalization range is bounded by the row-diameter `2+4δ` plus `H`. Thus the candidate margin is `~H/2`; comparing to `κ=τ/4` gives a linear wall at `H/τ≈1/2`.