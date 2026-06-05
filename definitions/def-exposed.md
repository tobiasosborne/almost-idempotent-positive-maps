---
id: def-exposed
term: exposed vertex
aliases: exposedness modulus; (ρ,κ)-exposed; well-exposed
kind: consensus
status: locked
source: internal
locus: report sec:classical (def:exposed); exposed-redundant-dichotomy-target.md
sha256: -
consensus: A+B; B's exposed-circuit machinery, in report sec:classical
---

**Statement.** For a [[def-stochastic|signed affine retraction]] with row polytope $K$, a row vertex $v$
is *$(\rho,\kappa)$-exposed* if there is an affine $h\colon K\to[0,1]$ with $h(v)=0$ and $h(p_i)\ge\kappa$
for every row $p_i$ with $\lVert p_i-v\rVert_1\ge\rho$ (measured on the row *set*, not all of $K$). The
*exposedness modulus* is $e_v(\rho)=\sup_h\min_{\,\lVert p_i-v\rVert_1\ge\rho} h(p_i)$ over such $h$. A
vertex is *well-exposed* (at $\sqrt{}$ scale) if $e_v(\rho)\ge c\sqrt\delta$ for some $\rho=O(\sqrt\delta)$,
where $\delta$ is the negative mass.

**Notes / provenance.** Project definition (B's `exposed-redundant-dichotomy-target.md`; report
sec:classical `def:exposed`). Central to the proved classical special cases (well-exposed ⇒ simplex) and
to the open *global exposed-hull lemma* `op:exposed-hull` (the remaining classical obstruction). Pointwise
exposed-or-redundant dichotomy is provably *insufficient* (dense regular polygons) — the gap must be stated globally.
