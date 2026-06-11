# w18_semigroup — fixed-space duality + boundary-product identities (codex research, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w18_semigroup/brief.md. Wave-18 idempotence-exploitation round, worker 5/5.

**Verdict**

Best current attack is not “more spectral facts”; it is a clone-invariant left/right fixed-space formulation that feeds the quotient anti-splitting problem. Exact semigroup data is real, but raw path products and raw factorisations are already known to be non-invariant.

**Top 3 Attack Plans**

1. **Fixed-Space Duality / Recurrent Classes Without Positivity**  
First lemma:
\[
\{g:Pg=g\}\ \cong\ \operatorname{Aff}(\{p_i\}),\qquad g_i=\phi_g(p_i),
\]
and dually every row \(p_i=e_i^TP\) lies in the left fixed space \(\{\ell:\ell P=\ell\}\). More explicitly, for any biorthogonal fixed bases \(Pu_s=u_s\), \(\ell_s^TP=\ell_s^T\), \(\ell_s^Tu_t=\delta_{st}\),
\[
P=\sum_{s=1}^k u_s\ell_s^T,\qquad p_i=\sum_{s=1}^k u_s(i)\ell_s^T .
\]
Dead-end evasion: gauge-invariant if stated as fixed spaces/row classes, not raw \(R\Lambda=I\); clone-invariant because duplicate rows have identical values under every \(Pg=g\).  
What it buys: a clean replacement for “recurrent classes”: extreme/quasi-positive points of the left fixed slice. Hiddenness and \(H\) become statements inside the exact affine duality between left fixed rows and right fixed functions.  
Calibration: \(P(\)useful new reduction\()=0.78\), \(P(\)closes linear law alone\()=0.32\).

2. **Quotient Semigroup Boundary Product**  
First lemma:
\[
B^m-B=-\sum_{r=0}^{m-2}B^rEC
\]
for every block split \(P=\begin{pmatrix}B&E\\ C&D\end{pmatrix}\). This is the full \(P^k=P\) family localized to a band.  
Dead-end evasion: use quotient row classes \(Q_{\alpha\beta}=\sum_{j\in\beta}P_{ij}\), not raw indices; this avoids the cloning obstruction. It also differs from t2 because it uses all lengths and boundary-return terms, not one uncontrolled one-step coupling.  
What it buys: turns the thin-chain problem into: either a quotient component has a fat path product, or the boundary product \(\sum B^rEC\) is large and must be charged to deep/visible mass. This is the most direct route to the w12 finisher.  
Calibration: \(P(\)quotient statement true\()=0.60\), \(P(\)provable with current belt plus one new lemma\()=0.38\).

3. **Trace / Resolvent As A Boundary-Tax Detector**  
First lemma:
\[
\operatorname{tr}P=k,\qquad 
\operatorname{tr}B-\operatorname{tr}(B^2)=\operatorname{tr}(EC),
\qquad
\operatorname{tr}B-\operatorname{tr}(B^m)=
\operatorname{tr}\sum_{r=0}^{m-2}B^rEC .
\]
Dead-end evasion: trace is clone-invariant and basis-free; use it only on quotient/cluster blocks. Do not try to prove the theorem from integer trace alone: s7 already died at the boundary-product localization.  
What it buys: an aggregate “spectral tax” for shallow components. It can certify that forbidden alternating/periodic modes are paid for by \(EC\), and may provide the missing lower bound that the semigroup boundary-product plan needs.  
Calibration: \(P(\)useful supporting lemma\()=0.55\), \(P(\)standalone proof\()=0.15\).

**Supporting Derivations**

For \(A=P^+\), \(N=P^-\), \(\|N\|_{\infty\to\infty}\le\delta\),
\[
\left\|A^m-P^m\right\|_{\infty\to\infty}
\le (1+2\delta)^m-(1+\delta)^m
\le m\delta(1+2\delta)^{m-1}.
\]
So \(P^m=P\) controls aggregate positive path sums up to signed error. It does not control atom path-products; cloning kills those.

For a right fixed deficit \(g=Pg\),
\[
g_i=p_i g .
\]
Thus every canonical separator/deficit already is a right fixed coordinate function on the row polytope. Conversely, if rows \(p_i=p_j\), then \(g_i=g_j\) for every \(Pg=g\); this is exactly why quotienting by row equality is canonical.

For the certified \(n=7,k=4\) instance: \(\delta=0.22840025\), \(\tau=0.47791239\), \(H/\tau=0.0158336\), \(\widetilde\sigma/\tau=1.62555\). It crosses the sigma gate but has tiny height. Also the semigroup signed-error scale is large there:
\[
\epsilon_2=2\delta+3\delta^2\approx 0.613,
\]
so this instance is not in the asymptotic regime where a path-product finisher can bite.

**Unverified Leads**

- **Quasi-positive left fixed cone.** Prove: every extreme point of  
  \[
  K_\delta=\{\ell:\ell P=\ell,\ \ell\mathbf1=1,\ \neg(\ell)\le C\delta\}
  \]
  is \(O(\delta)\)-near a visible row, unless the known small-\(\widetilde\sigma\) branch applies. Internal theorem; no external source expected.

- **Clustered quotient floor.** Exact quotienting is not robust under small similarities. Need a clustered quotient at scale \(\eta_{\rm cl}\lesssim\delta\), with \(Q^2=Q+O(\delta)\) and finisher error still \(O(\delta)\). Internal, but should be banked separately.

- **Projection perturbation/subspace angle.** If a candidate nonnegative idempotent \(Q\) is constructed, exact resolvent
  \[
  (zI-P)^{-1}=z^{-1}(I-P)+(z-1)^{-1}P
  \]
  gives immediate range/kernel angle bounds. Source acquisition needed before banking: Kato or Stewart-Sun style projection perturbation references.

- **Projective contraction provenance.** The Birkhoff-Hilbert finisher is central; before canonical use, acquire byte-grounded sources for the contraction theorem if not already in `refs/`.

**Overall Calibration**

Most promising path: Plan 1 feeding Plan 2.  
\(P(\)linear law true\()\approx 0.78\).  
\(P(\)this semigroup/two-sided lens yields the missing proof without a new facial-modulus theorem\()\approx 0.34\).