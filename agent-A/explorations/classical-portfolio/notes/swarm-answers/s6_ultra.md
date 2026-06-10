VERDICT: DIED-AT the scale-collapse inequality

\[
\|p^{(k)}_{j_k}-p^{(k)}_{v_k}\|_1\ge \rho_k=4\tau_k\to0,\qquad
g^{(k)}_{j_k}\le H_k-C\tau_k,\qquad t_k^*<\kappa_k=\tau_k/4\to0.
\]

In the standard compactness limit this becomes only

\[
p^0_{j}=p^0_v,\qquad g^0_j=g^0_v=0,\qquad t^*_0=0,
\]

so the limiting object does **not** violate Baake-Sumner. It is just a recurrent equal-row block, exactly allowed by the Markov-idempotent normal form in [equal-fin.tex](/home/tobias/Projects/almost-idempotent-positive-maps/refs/baake-sumner-2007.11433/equal-fin.tex:1060).

**Proof / Post-Mortem**

The LP witness setup is solid: the exposedness dual is the finite identity `(♦)` in [wave8-fable-closer.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave8-fable-closer.md:72), and RW gives the observed deep row-witness mechanism [wave8-fable-closer.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave8-fable-closer.md:389). d12 strongly supports the sigma-tilde-small case: all measured optimal witnesses have mass `1` at `g=H`, with `sigma~ = 0` [d12-dmf-depth-profiles.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/d12-dmf-depth-profiles.md:15).

The compactness strategy fails because all bad predicates are scale-dependent. “Far” means distance at least `4τ`; “hidden” means `t* < τ/4`; “shallow” means missing depth by `O(τ)`. All three vanish as `δ=τ²→0`. Baake-Sumner kills separated exact stochastic hidden webs, but compactness only gives coincident rows in an exact recurrent class.

The W-jump is real, not cosmetic. Lower semicontinuity holds only for isolated limit vertices with fixed positive exposing margin and fixed separation. Here both margins and separations are `O(τ)`, so a row can be outside `W_k` for every `k` and become a perfectly valid `W_0`/recurrent row in the limit. Thus `conv W_k` need not converge at the scale where DMF lives.

Finite support does not rescue this. A basic optimal dual witness has support bounded by the affine dimension of the row configuration, but that dimension can grow with `n_k`; recursively adding carriers can produce ladders of length `~1/τ_k`. The ultraproduct route handles size, but it leaves an infinitesimal bad web, not a standard exact Markov-idempotent contradiction.

Conditional HLC remains clean: if qualitative existential DMF were proved with deep mass `1-ε`, the exchange line in [wave8-fable-closer.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave8-fable-closer.md:554) would give asymptotically

\[
\delta \ge (4(1-\epsilon)^2-o(1))H^2.
\]

**New Sub-Lemmas**

1. Non-collapsing compactness lemma: if `ρ_k, κ_k`, and the depth gap have positive standard lower bounds, an all-shallow limiting witness contradicts Baake-Sumner. Status: proved, but irrelevant to the `τ`-scale target.

2. W-semicontinuity lemma: isolated fixed-margin exposed vertices persist; no semicontinuity is available at `ρ,κ=O(τ)`. Status: proved/diagnostic.

3. Required replacement theorem: tangent Baake-Sumner stability for the blow-up
\[
\widehat p_i^{(k)}=(p_i^{(k)}-p_{v_k}^{(k)})/\tau_k,\qquad \widehat g_i^{(k)}=g_i^{(k)}/\tau_k.
\]
Status: open. This is the real compactness-scale theorem.

**Calibration**

P(existential DMF true): `0.72`.

P(this compactness post-mortem survives audit): `0.86`.

P(plain unscaled compactness can prove DMF without a tangent stability theorem): `0.15`.

Sharpest structural insight: DMF is not a zero-scale Baake-Sumner statement; it is a tangent-scale stability statement. The all-shallow web disappears in the standard limit because its separation, hiddenness margin, and depth defect are all `O(τ)`. The next proof has to classify infinitesimal perturbations of Markov idempotent recurrent blocks, not merely pass to an exact stochastic idempotent.