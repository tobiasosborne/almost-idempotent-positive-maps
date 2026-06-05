---
id: def-jordan-coboundary
term: Jordan coboundary
aliases: d¹; Jordan 2-cocycle; derivation; multiplicativity defect; coboundary
kind: consensus
status: locked
source: internal
locus: report sec:programme; next-arrow-to-newton-error-reduction.md (B-NEWTON conventions)
sha256: -
consensus: A+B; B's cochain/Newton conventions, used in report sec:programme (Layer-1)
---

**Statement (Layer-1 cohomology).** Let $v\colon B\to A$ map a genuine JB-algebra $B$ into an
[[def-eps-jb-algebra]] $A$, with module action $a\cdot m:=v(a)\circ m$. The *multiplicativity defect*
$g(a,b)=v(a\circ b)-v(a)\circ v(b)$ is a (symmetric) Jordan 2-cochain. The *Jordan coboundary* of a
1-cochain $h$ is
$$(d^1 h)(a,b)=v(a)\circ h(b)+h(a)\circ v(b)-h(a\circ b).$$
A *derivation* is an element of $\ker d^1$. Killing $g$ by a coboundary $d^1 h$ (Newton-iterating
$\delta\mapsto C(\varepsilon+\delta^2)$) is the error-reduction step; it needs a **bounded right inverse
$s$ of $d^1$ in the order-unit norm** — the open Layer-1 obstruction.

**Notes / provenance.** Project conventions (B's `next-arrow-to-newton-error-reduction.md`; report
sec:programme). The linearized Jordan-identity defect operator is written $J\theta$, *not* a separate
$d^2$. The splitting/derivation distinction matters: the right test is $\mathrm{dist}(h,\mathrm{Der})$,
not $\lVert h\rVert$. Norms are [[def-injective-cochain-norm|injective order-unit]] norms.
