---
id: def-spectral-idempotent
term: spectral idempotent
aliases: P; θ(2Φ−1); Kitaev idempotent
kind: cited
status: locked
source: kitaev-2405.02434
locus: approximate_algebras.tex:2171-2182 (eq. tilde_Phi, Prop. P)
sha256: e7eb512a2ec2438d
consensus: transcribed in report sec:spectral (def:spectral-idempotent); restricted to B(H)_sa
---

**Statement.** Let $\Phi\colon B(\mathcal H)_{\mathrm{sa}}\to B(\mathcal H)_{\mathrm{sa}}$ be unital
positive and almost idempotent (see [[def-almost-idempotent]]). Set $S=2\Phi-\mathbf 1\in\mathrm{End}(B(\mathcal H)_{\mathrm{sa}})$,
define $R=(S^2)^{-1/2}$ by the binomial series for $(\mathbf 1-(\mathbf 1-S^2))^{-1/2}$ (convergent since
$\lVert S^2-\mathbf 1\rVert=4\lVert\Phi^2-\Phi\rVert\le4\eta<1$ for $\eta<\tfrac14$), set $\operatorname{sgn}(S)=SR$, and put
$$P=\theta(2\Phi-\mathbf 1)=\tfrac12\bigl(\mathbf 1+\operatorname{sgn}(S)\bigr)
   =\tfrac12\Bigl(\mathbf 1+(2\Phi-\mathbf 1)\bigl(\mathbf 1-4(\Phi-\Phi^2)\bigr)^{-1/2}\Bigr).$$
This is the spectral idempotent of $\Phi$ for the spectral cluster near $1$. Its key properties
(idempotent, unital, $\lVert P-\Phi\rVert\le C\eta$, $\delta$-positive) are the registry lemma
`lem-P-properties`, **not** part of this definition.

**Notes / provenance.** Construction from Kitaev, eq. (tilde_Φ) / Prop. P
(`refs/kitaev-2405.02434/approximate_algebras.tex:2171-2182`). Kitaev states it for unital CP maps in the
cb-norm; here it is restricted to the real space $B(\mathcal H)_{\mathrm{sa}}$ with the operator-norm
hypothesis [[def-almost-idempotent]], which is all the bridge needs. Notation $\theta(2\Phi-\mathbf 1)$ per
the harmonisation table. Feeds [[def-near-fixed-algebra]].
