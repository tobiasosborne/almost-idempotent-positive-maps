VERDICT: PARTIAL: F-ND and F-BC survive; F-ψ is not airtight as stated.

F-ND: confirmed with the factor-2 downgrade. If `u` maximizes site `i` with value `M`, then for any `rho`-far row `q`,
`rho <= ||u-q||_1 <= 2(M-q_i) + 2t + 4δ`.
So the max-selection exposer `h(y)=(M-y_i)/Z`, `Z<=1+2δ`, has far-row margin at least
`(rho-2t-4δ)/(2Z)`. This matches the note’s Stage-5 correction in [notes/fable-hlc-attack.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/fable-hlc-attack.md:423). To put the original near-delta row into the exposed cluster, I would use the stronger conservative threshold giving
`c = (rho - 2κ(1+2δ) - O(δ))/(4τ) = 7/8 - o(1)`, so `c≈0.85` is a safe advertised constant.

F-BC: confirmed, actually slightly stronger under the signed-mass reading. If `x(S)>=1-κ` and total negative mass is `<=δ`, then positive external coefficient mass is `<=κ+δ`; the claimed `κ+2δ` is safe.

F-ψ: not confirmed. The `v -> v″` repair is directionally right, and exact-zero normalization at `v″` is fine by max-selection: use `ψ(v″)-ψ`, or shift by the row-sum affine constant. Also `ψ(v″)>=ψ(v)` gives `g(v″)<=2σ_v+O(δ)` for the usual `λ=1/2` choice. But I do not see the missing uniform gap: a `rho`-far non-`S`-full row can trade `S`-mass deficit against the `λφ` term and remain nearly ψ-maximal. The notes assert this in the table, but §5.7 only repairs localization, not this gap. So record F-ψ as conditional/open pending a lemma: “every rho-far non-`S`-full row has ψ-gap ≥ κZ.”