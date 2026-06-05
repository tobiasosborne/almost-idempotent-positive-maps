---
id: def-spin-factor
term: spin factor
aliases: spin cone; V_n; R·1 ⊕ H
kind: cited
status: locked
source: hos
locus: joa-m.md:2264 (2.9.7)
sha256: 28740e73d547dd46
consensus: transcribed report sec:jordan (thm:jnw) + sec:factorization (def:spin-cone); cone computed inline
---

**Statement.** A *spin factor* is $V = \mathbb R\mathbf 1\oplus H$, where $H$ is a real inner-product
space of dimension $\ge2$, with Jordan product determined by $(s,v)\circ(t,w)=(st+\langle v,w\rangle,\,
sw+tv)$. It is the rank-2 simple [[def-formally-real]] Jordan algebra (two minimal projections summing to
$\mathbf 1$). The element $(s,v)$ has square $(s^2+\lVert v\rVert_2^2,\,2sv)$ and spectrum
$\{s\pm\lVert v\rVert_2\}$, so the *positive cone* is $V_+=\{(s,v):s\ge\lVert v\rVert_2\}$ and the
order-unit norm is $\lVert(s,v)\rVert=\lvert s\rvert+\lVert v\rVert_2$.

**Notes / provenance.** HOS 2.9.7 `refs/hos/joa-m.md:2264`; cone/norm computed inline in report
sec:factorization. **Project-relevant:** spin is the rank-2 ("bounded rank") family where the Layer-1
order-vs-Frobenius $\sqrt{\mathrm{rank}}$ gap is absent (constant $4\sqrt2$); it also hosts the
positivity-rounding obstruction (registry prop-rounding-fails). $V_4$ and $V_{\ge6}$ are irreversible.
