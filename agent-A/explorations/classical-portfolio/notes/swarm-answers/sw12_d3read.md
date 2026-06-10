1. VERDICT: PARTIAL

I did not prove existential DMF. I did reconstruct the d3/d7/d8 floor evidence and the small-δ prediction is sharp:

The claimed small-δ flat floor is not verified in the saved d3/d7 data. The verified flat-floor rows live at corner scale, roughly δ≈0.06–0.08, not δ<0.01. Prediction for d13: outcome (c) for any alleged small-δ H≈0.536√δ floor instance in this geometry. It either fails the hidden-top verification or collapses to H=O(δ). If d13 profiles the collapsed corner-family instances, the witness is deep with m*=1, not shallow.

2. Proof / Post-Mortem / Construction

The reliable d3 row-level data is `d3_clean_scaling.npy`: max H/τ=0.535613 occurs at

\[
\tau=0.287873725,\quad \delta=0.082871281,\quad H=0.154189049,\quad \delta/H^2=3.486.
\]

For “floor-like” rows H/τ≥0.5, the smallest δ I found is

\[
\tau=0.250082344,\quad \delta=0.062541179.
\]

For δ<0.01, the best row-level d3 entry is only

\[
\tau=0.098424783,\quad \delta=0.009687438,\quad H=0.019374876,\quad H/\tau=0.19685.
\]

So no saved d3 row-level flat-floor sample below δ=0.01.

The verified d7 `d7_hunt.json` entries are all ring-shell deep-collapse cases:

\[
\delta\in[0.179548,0.2505],\quad \delta/H^2\ge 303.38
\]

in `d7_hunt` itself, with the smallest H as low as 0.0003047. These are not small-δ floor instances.

The d8/d12 financed-wiggle family is the actual witness-profiled construction. Its passing rows all satisfy

\[
H=2\delta,\quad \tilde\sigma_v=0,\quad m_{\rm obs}=1,\quad \text{shallow fraction}=0.
\]

Even the smallest passing d12 row is

\[
\delta=0.007,\quad H=0.014,\quad H/\tau=0.167,\quad \delta/H^2=35.714.
\]

That is corner/collapsed scale, not flat floor.

By hand, the corner separator is the negative-anchor separator. If the hidden row has one negative anchor coefficient \(-\delta\), take

\[
\phi(x)=-2x_0,\qquad \sup_{\operatorname{conv} W}\phi=0,\qquad \phi(p_v)=2\delta=H.
\]

Then

\[
g(x)=H-\phi(x)=2\delta+2x_0.
\]

Rows in W used by the RW witness have \(x_0=0\), hence \(g=H\). The top hidden row has \(x_0=-\delta\), hence \(g_v=0\). Since the positive far carriers of \(p_v\) are W rows in the d12 geometry, the optimal RW witness is deep.

3. New Sub-Lemmas

σ̃-zero floor exclusion. If \(\tilde\sigma_v=0\), then by σ̃-height-collapse

\[
H\le \delta R\le \delta(2+4\delta).
\]

Thus a flat floor \(H\approx 0.536\sqrt{\delta}\) requires roughly \(\sqrt{\delta}\gtrsim0.268\), i.e. \(\delta\gtrsim0.0718\). It cannot persist to small δ.

Corner RW witness depth. In the barycentric corner/financed-wiggle geometry, the row-identity RW dual has μ supported on W rows. Since every W row is deep, the witness has deep mass exactly 1.

d7 ring-shell non-floor status. Verified d7 ring-shell entries enter the non-exposed distinct-vertex hypothesis only by collapsing H, giving huge δ/H². They do not instantiate the small-δ all-shallow web.

4. Calibration

P(existential DMF true): 0.70.

P(this forensic prediction survives audit): 0.84.

5. Sharpest Structural Insight

The apparent floor and the witness anatomy came from different regimes. The only profiled construction is σ̃=0, so height-collapse forces H=O(δ); its RW witness is necessarily deep. A genuine small-δ flat floor with H≈c√δ must have \(\tilde\sigma_v\to1\), so it cannot be the d12 corner mechanism. The saved d3/d7 data does not currently contain such a verified small-δ web.