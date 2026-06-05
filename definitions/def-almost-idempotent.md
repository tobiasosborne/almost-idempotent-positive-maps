---
id: def-almost-idempotent
term: almost idempotent
aliases: η-idempotent; eta-idempotent; non-idempotence
kind: consensus
status: locked
source: internal
locus: report sec:spectral (eq:eta-hypothesis); contrast rem:cb-norm
sha256: -
consensus: A+B; operator-norm formulation adopted (vs Kitaev's cb-norm), report rem:cb-norm
---

**Statement.** A [[def-positive-unital-map]] $\Phi:B(\mathcal H)_{\mathrm{sa}}\to
B(\mathcal H)_{\mathrm{sa}}$ is *almost idempotent* (with defect $\eta$) if
$$\lVert\Phi^2-\Phi\rVert\le\eta,\qquad \eta\in[0,\tfrac14),$$
where $\lVert\cdot\rVert$ is the **operator norm of the map** on $B(\mathcal H)_{\mathrm{sa}}$ (with the
order-unit norm on $B(\mathcal H)_{\mathrm{sa}}$ itself). The range $\eta<\tfrac14$ is what makes the
binomial series of [[def-spectral-idempotent]] converge.

**Notes / provenance.** Project hypothesis (consensus). Kitaev measures non-idempotence in the
**cb-norm** $\lVert\Phi^2-\Phi\rVert_{\mathrm{cb}}\le\eta$; we deliberately use the **operator norm**
because mere positivity is not stable under amplification ($\mathrm{id}_n\otimes\Phi$ need not be
positive) — see report rem:cb-norm. This weaker control is exactly why the bridge exponent is
$\sqrt\eta$ rather than $\eta$. Distinguish: $\eta$ (this defect) vs $\delta=\lVert P-\Phi\rVert\le C\eta$
(spectral closeness) vs $\varepsilon\le C\sqrt\eta$ (the JB-axiom defect of [[def-eps-jb-algebra]]).
