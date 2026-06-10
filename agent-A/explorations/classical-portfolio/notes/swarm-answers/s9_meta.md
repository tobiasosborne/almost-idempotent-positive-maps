VERDICT: PARTIAL; the framing is mostly sound, but the `σ̃` branch dies at the exact gap
\[
\text{RW deep dual-feasible witness} \;\not\Rightarrow\; \text{deep optimal witness}.
\]

**Proof / Post-Mortem**
Canonical `σ̃` should be geometric, self-excluded, and halo-stable:
\[
C_W=\operatorname{conv}\{p_w:w\in W\},\quad d_W(j)=\operatorname{dist}_1(p_j,C_W),
\]
\[
\widetilde\sigma_x(\varepsilon)=\sum_{j\ne x}P_{xj}^+\,1_{\{d_W(j)>\varepsilon\}}.
\]
Use `ε=0` only for exact statements. Boundary rows count inside. If \(d_W(j)\le\varepsilon\), then for the canonical separator
\[
\phi(p_j)\le \varepsilon,\qquad g_j=H-\phi(p_j)\ge H-\varepsilon,
\]
so halo ambiguity is automatically absorbed as depth slack.

What d12 actually proves: its code computed positive mass on indices `k not in W`, not an LP test for \(d_W(k)>0\). Since it got `0`, the result is still strong for those instances: all positive off-self carriers are W-indices, hence geometrically in \(C_W\). But future nonzero `σ̃` readings need the `dist1_to_conv` test; index-not-in-W is not the canonical definition.

Existential DMF really is sufficient. Pick a maximal-height geometric row vertex \(v\). If \(H>0\), then \(v\notin W\), hence hidden; topness gives \(g\ge0\), and \(R=\operatorname{osc}(g)\le2+4\delta\). For one optimal witness with deep mass \(m_*\) at depth \(H-E\),
\[
m_*(H-E)\le\sum\mu_jg_j
\le \sum\mu_jg_j+\sum\alpha_kg_k
=\sum\beta_kg_k
\le t^*R<\kappa R.
\]
Thus
\[
H\le E+\frac{\tau(2+4\delta)}{4m_*}.
\]
If \(E=C_D\delta/\tau=C_D\tau\), the asymptotic HLC constant is
\[
a=\left(C_D+\frac{1}{2m_*}\right)^{-2},
\]
not \(4m_*^2\) unless \(E=o(\tau)\). The \(t^*=0\) case is fine: the exchange forces \(\sum\mu g=0\), so DMF gives \(H\le E\).

The RW issue: RW is dual-feasible with cost
\[
B_{\rm RW}=\frac{\nu_v}{\theta_{\rm far}(1+\nu_v-P_{vv})},
\]
so \(t^*\le B_{\rm RW}\). For any feasible witness the exchange gives only
\[
\sum\mu g+\sum\alpha g\le B_{\rm witness}R,
\]
not \(t^*R\). RW being deep is enough for HLC only if one also proves \(B_{\rm RW}<\kappa\). It is not enough for existential DMF unless RW is optimal, or one proves an optimal-face transfer preserving deep mass.

**New Sub-Lemmas**
1. Geometric `σ̃` lemma: rows within an \(\varepsilon\)-halo of \(C_W\) are \(H-\varepsilon\)-deep. Proved above.
2. Existential-DMF chain lemma: one deep optimal witness suffices, including \(t^*=0\). Proved above, with corrected constant.
3. Feasible-vs-optimal witness lemma: exchange uses the witness’s own \(B\); replacing it by \(t^*\) is valid only on the optimal face. Proved above.
4. Top-vertex reduction: HLC may choose a maximal-distance geometric vertex because distance to a convex set is convex and maximizes on row vertices. Multiplicity must be geometric, not index-naive.
5. σ̃-small ⇒ deep optimal witness: still open. Current proof only gives “RW deep when RW is active and its carriers lie in \(C_W\).”

**Gap List**
Unproved in POST-d12 sharpening:
- `σ̃≤s ⇒ ∃ optimal witness with deep mass ≥1−f(s)`.
- RW witness lies on, or transfers to, the optimal dual face.
- `σ̃-large` is equivalent to a mutual-shadow hidden web.
- ρ-separated hidden top-band vertices cannot mutually carry each other.
- “All-shallow requires `σ̃>0`” for arbitrary optimal witnesses; true only for the row-identity/RW witness unless optimal-face transfer is proved.
- The d7/X1 exposure mechanism as a quantitative theorem, not just numerical/nonrealization evidence.

**Probabilities**
\(P(\)existential DMF true as stated with some universal \(m_*>0,E=O(\tau)\)\()=0.70\).
\(P(\)this audit survives hostile review\()=0.88\).

**Structural Insight**
The post-d12 frame should separate three objects: geometric carrier mass outside \(C_W\), separator-shallow mass, and the optimal dual face. d12 strongly supports the RW/deep-carrier story for the financed-wiggle family, but the campaign’s remaining obstruction is not “does v have deep row carriers?” It is whether optimization can abandon that deep feasible witness and move to an all-shallow top-band witness.