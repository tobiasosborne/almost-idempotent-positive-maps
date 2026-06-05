---
id: def-injective-cochain-norm
term: injective cochain norm
aliases: ‖·‖_inj; injective multilinear norm; order-unit cochain norm
kind: consensus
status: locked
source: internal
locus: report sec:programme; next-arrow-to-newton-error-reduction.md; cochain-norm-conversion-caveat.md
sha256: -
consensus: A+B; B's cochain-norm conventions (report sec:programme), A's rank-gap caveat
---

**Statement.** For a $k$-linear Jordan cochain $\theta$, the *injective (order-unit) cochain norm* is
$$\lVert\theta\rVert_{\mathrm{inj}}=\sup_{\lVert x_1\rVert\le1,\dots,\lVert x_k\rVert\le1}\lVert\theta(x_1,\dots,x_k)\rVert,$$
all norms being the order-unit norm of the [[def-eps-jb-algebra|algebra]]. This is the norm the Layer-1
structure theorem must control — **distinct** from the Frobenius/Hilbert–Schmidt tensor norm.

**Notes / provenance.** Project convention (B's `next-arrow-to-newton-error-reduction.md`; report
sec:programme). **Crucial caveat** (`cochain-norm-conversion-caveat.md`; A's `prop:rank-gap`): the
order-vs-Frobenius gap on a rank-$r$ simple factor is exactly $\sqrt r$; a cochain can have injective norm
$1$ yet HS-tensor norm $\sqrt n$ (e.g. $(x,y)\mapsto\langle x,y\rangle$ on $\mathbb R^n$). So the
[[def-jordan-coboundary|coboundary]] splitting must be bounded *directly* in this norm — the Frobenius
bound (which IS dimension-free) does not transfer. This is the heart of the open Layer-1 problem.
