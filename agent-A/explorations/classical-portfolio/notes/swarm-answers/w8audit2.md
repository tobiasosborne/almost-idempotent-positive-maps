**Verdict**

Closed forms: **CONFIRMED, conditional on the two family laws** `t* = ν/(1+ν)` and `H = 2δ = 2ν`. The LP normalization in [d1_infra.py](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/experiments/d1_infra.py:118) compares raw margin `t*` to raw `κ`, not `κR`.

With `ν=δ=τ²` and `κ=τ/4`:
```text
τ²/(1+τ²) < τ/4
⇔ τ² - 4τ + 1 > 0
⇔ τ < 2 - √3
```
So:
```text
τ* = 2 - √3 = 0.2679491924
δ* = (2 - √3)^2 = 0.0717967697
d* = 2δ* = 0.1435935394
H/τ = 2τ* = 2(2 - √3) = 0.5358983849
δ/H² = 1/(4τ*²) = (7 + 4√3)/4 = 3.4820508076
```
This matches the d9 bracket `[0.1435, 0.144]` and the measured `0.536`, `3.484` figures in the notes.

3.2′ chain: **SOUND as an asymptotic DMF ⇒ HLC implication, BROKEN as a finite-corner calibration claim.**

The exchange is correct:
```text
Σ_F μ_j g_j + Σ_i α_i g_i = Σ_i β_i g_i ≤ B R = t* R < κR
```
That follows directly from the dual identity and `B=t*`; the sharp bound is `t*R`, not merely `κR`.

The bad step is the `R` handling in [wave8-fable-closer.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave8-fable-closer.md:554). From the normalized separator,
```text
g_i = φ(p_v) - φ(p_i) ≤ ||p_v - p_i||_1 ≤ diam(rows) ≤ 2 + 4δ.
```
So the clean universal cap is `R ≤ 2+4δ`, not `R = 2+4δ+H`. The looser `H+diam` bound is unnecessary and spoils the finite calibration.

Corrected asymptotic chain:
```text
m*(H - C_D δ/τ) ≤ κR ≤ (τ/4)(2+4δ)
⇒ H ≤ τ[(2+4δ)/(4m*) + C_D τ]
⇒ δ ≥ a H², with a → 4m*².
```

Constant corrections:
```text
Closer’s displayed finite formula:
(4/(2+4δ*+H*))²(1-τ*/4)² = 2.3572387152, not ≈3.4.

Using universal R≤2+4δ at δ* gives:
(4/(2+4δ*))² = 3.0585571857.

The exact corner value 3.4820508076 is recovered only from the family-specific identity R=2+H:
[2(1-τ*/4)]² = 3.4820508076.
```

Calibration check: `B_B=(2+H*)/4` at the corner is **exact**:
```text
(2+H*)/4 = 4 - 2√3 = 0.5358983849 = H*/τ*.
```
But it is a finite-corner value, not the small-δ limit. The asymptotic `m*=1` coefficient is `B_B → 1/2`.

Probabilities:
```text
P(corner closed forms exactly right): 0.90
P(3.2′ survives af-formalization as written): 0.35
P(corrected DMF⇒asymptotic-HLC chain survives): 0.80
```