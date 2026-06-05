---
id: def-self-adjoint-part
term: self-adjoint part
aliases: B(H)_sa; Bsa; state; self-adjoint operators
kind: cited
status: locked
source: hos
locus: joa-m.md:374 (states); cf. Idel 2013 idel-2013.md:333 (positive-semidefinite order)
sha256: 28740e73d547dd46
consensus: transcribed report sec:prelim (def:operators); A-verified
---

**Statement.** Let $\mathcal H$ be a finite-dimensional complex Hilbert space and $B(\mathcal H)$ the
operators on it, with operator norm $\lVert x\rVert=\sup_{\lVert\xi\rVert\le1}\lVert x\xi\rVert$. The
*self-adjoint part* is $B(\mathcal H)_{\mathrm{sa}}=\{x\in B(\mathcal H):x=x^*\}$, a real vector space.
For $a\in B(\mathcal H)_{\mathrm{sa}}$ write $a\ge0$ iff every eigenvalue of $a$ is $\ge0$; this is the
order with unit $\mathbf 1$. A *state* is a positive ($\omega(a)\ge0$ for $a\ge0$) unital
($\omega(\mathbf 1)=1$) linear functional $\omega:B(\mathcal H)\to\mathbb C$.

**Notes / provenance.** States as positive unital functionals: HOS `refs/hos/joa-m.md:374`; the
positive-semidefinite order on self-adjoint matrices: Idel `refs/idel-2013/idel-2013.md:333`. The whole
project lives in $B(\mathcal H)_{\mathrm{sa}}$ with only this order and the operator norm. Underlies
[[def-order-unit-space]], [[def-positive-unital-map]].
