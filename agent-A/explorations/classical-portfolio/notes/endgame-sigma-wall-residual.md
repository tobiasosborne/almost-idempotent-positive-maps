I can’t honestly mark HLC as PROVED from the audited arsenal.

**Branch A: SKETCH, not proved.**  
What is proved is the audited g-budget: for deficit `g`, a row `j` placing positive mass `σ` on levels `≥ ell` satisfies `σ ell <= g_j + δ R`, with `R=osc(g)`; for the top vertex `g_v=0`, this gives only `ell <= δR/σ_v`. See [audit-summary.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave4/audit-summary.md:7) and [fable-hlc-attack.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/fable-hlc-attack.md:260).  
The missing analytic step is exactly the measured law `H <= B_A σ_v τ`. If that were proved, then for `σ_v <= 1/2`:
`δ = τ² >= 4 H² / B_A²`.

**Branch B: SKETCH/GUESS, not proved.**  
The desired margin-pinning statement is: if `σ_v >= 1/2` and `H > B_B τ`, then the hidden cluster is actually `(ρ,κ)`-exposed. The numerics strongly show `B_B ≈ 0.536`, with margin hitting `κ` at the wall; see [mrp-decider-report.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/mrp-decider-report.md:39).  
But the audited facts do not prove this. In particular, `F-ψ` is explicitly not confirmed; the missing uniform ψ-gap is recorded in [audit-summary.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave4/audit-summary.md:9). Even granting ψ-gap, I still do not see a derivation of the exposedness wall from F-WR/F-BC/F-GB alone.

**Glue: conditional only.**  
If the σ-wall lemma is added:

`H <= B_A σ_v τ` for `σ_v <= 1/2`, and  
`σ_v >= 1/2, H > B_B τ => exposed`,

then HLC follows with

`a = min(4/B_A², 1/B_B²)`.

Using the measured constants gives the numerical floor `a ≈ 3.48`; using a conservative conjectural pair `B_A=2, B_B=1` would give `a=1`. But those constants are not proved analytically here.

Single residual: the analytic σ_v-wall lemma. The ψ-gap is a sub-residual if the proof routes through the `v″` max-selection branch. No files were changed; this environment is read-only.