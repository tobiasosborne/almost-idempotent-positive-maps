VERDICT: CONFIRMED-WITH-CORRECTIONS

The repaired mechanism in [notes/fable-hlc-attack.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/fable-hlc-attack.md:371) is the right one. From `P²=P`,
`x_i = Σ_{k∈R} x_i,k x_k + ext_i`; substituting `x_k = π̄+w_k` gives, after subtracting `i,j`,

`w_i-w_j = [(s_i-s_j)π̄ + ext_i-ext_j] + Σ_{k∈R}(w_i,k-w_j,k)w_k`.

The last term is bounded by `2R_w²`. The bracket is controlled because self-indexing makes non-`R` entries the external coefficients, and the global zero-sum of wiggles ties the internal mass defect to external mass plus row-negativity. Rewriting against `π̄` and using `diam₁(K)≤2+4δ` gives the advertised `2.1(σ_i+σ_j)+4δ` scale, in the small-δ regime cited by Stage 5.

Corrections: this is not a free-standing theorem from the short claim alone. It needs the precise self-indexing/support assumptions, normalized positive `π̄`/`π̄∈K` behavior, and small-δ slack. Also the separation corollary with `8ρ²` needs the extra “`2ρ`-pattern web” bound `R_w≤2ρ`; otherwise the direct consequence is `(ρ-4δ-2R_w²)/2.1`.

So F-WR itself is confirmed under the source’s repaired hypotheses, but not as an unconditional statement stripped of those side conditions.