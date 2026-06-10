VERDICT: PARTIAL.

The Baake-Sumner distance formulation is a sound canonical W-free target, but `w105_wfree` does not prove a new route. Its equivalence claims are repairable only with extra hypotheses and bigger unspecified constants. The hiddenness LP is not literally smuggled back in, but the nearest-normal-form/partition search is essentially the classical stability problem itself.

Main death point if taken as written:
\[
\min_{v\in \mathrm{Vert}(\mathrm{rows}(P))}\ell_s(v)\ \text{small}
\;\not\Rightarrow\;
\|v-a^{(s)}\|_1\le 5\varepsilon
\]
without also using rowwise closeness to a nearest B-S idempotent, disjoint recurrent supports, and a Hausdorff/vertex-selection argument.

**Claim Verdicts**
- `D_BS(P)=dist(P, exact stochastic idempotents)` via B-S normal form: SOUND-WITH-FIX. Use max-row `l1` norm and row negative mass, not entrywise negativity. B-S states the HM classification; the proof is not in that source.
- Open core `D_BS(P) <= C sqrt(nu(P))`: SOUND as a statement, but COSMETIC as a route. It is basically `op-classical` in normal-form coordinates. Exponent `1/2` is sharp by `ex-hume`.
- W-form `=> D_BS`: SOUND-WITH-FIX. Needs a separated net of W-vertices before applying `thm-cluster`; losses are
  \[
  D_{BS}(P)\le C(\rho+\gamma+\delta/\kappa+\delta).
  \]
- `D_BS => W-form`: SOUND-WITH-FIX. Constants `5,6,20` are not established. A correct version is:
  \[
  D_{BS}(P)\le\varepsilon,\quad \rho\ge C\varepsilon
  \Rightarrow
  H_{\rho,c\rho}(P)\le C'\varepsilon .
  \]
- “Partition search is not hiddenness LP”: SOUND, but only formally. It avoids the exposedness dual cone, yet asks for the global B-S decomposition, which is the hard object.
- “Birkhoff becomes natural”: SOUND-WITH-FIX. It explains one local B-S block, but still needs the missing sup leakage/closure input.
- Spectral `Gamma` and fixed-simplex alternatives: SOUND as rejected alternatives; both lose transient row data.

**Tests**
`s5`: passes the W-free formulation. The explicit nearby B-S idempotent with singleton recurrent blocks `{0},{1},{2}` and transient rows
\[
(0,1/20,19/20,0,0),\quad (0,11/20,9/20,0,0)
\]
has
\[
\|P-E\|_{\infty\to\infty}=1841/800000=2\delta\approx0.00230125
=0.06784\,\tau .
\]
So the all-shallow witness is real, but low-height and B-S-close.

Corner family: also passes. Using the audited laws `H=2δ` and `t*=δ/(1+δ)`, it is a budget-line family, not a high `sqrt(δ)` web. No exact `D_BS` constant is available because the report does not give a full parametrization, but the accepted structure predicts `O(δ)` normal-form repair, hence safely `O(sqrt δ)`.

**Recommendation**
Canonical open statement going forward:

\[
\boxed{
P\mathbf1=\mathbf1,\quad P^2=P,\quad
\nu(P)=\max_i\sum_j(-P_{ij})_+\le\delta
\ \Longrightarrow\
\operatorname{dist}_{\infty\to\infty}(P,\mathcal E_n)\le C\sqrt\delta
}
\]

Keep the W/hidden-vertex machinery as a proof strategy and diagnostic layer, not as the canonical statement. The real proof target remains: produce a dimension-free stable B-S block decomposition with sup leakage/closure control.

`P(linear law true) ≈ 0.72` for hidden top vertices.  
`P(this audit survives review) ≈ 0.82`.