---
id: def-order-unit-space
term: order-unit space
aliases: order-unit norm; order unit; Archimedean order-unit space
kind: cited
status: locked
source: hos
locus: joa-m.md:366-372 (§1.2.1)
sha256: 28740e73d547dd46
consensus: transcribed report sec:prelim (def:order-unit); specialised to e=𝟏 on B(H)_sa
---

**Statement.** A real vector space $A$ with a proper convex cone $A^+$ (so $a\ge b\iff a-b\in A^+$) and a
distinguished $e\in A^+$ is an *order-unit space* if (i) $e$ is an *order unit*: for each $a$ there is
$\lambda>0$ with $-\lambda e\le a\le\lambda e$, and (ii) $A$ is *Archimedean*: $na\le e$ for all
$n\in\mathbb N$ implies $a\le0$. The *order-unit norm* is
$$\lVert a\rVert=\inf\{t>0:\ -t e\le a\le t e\}.$$
With $e=\mathbf 1$ and cone $A^+=\{a\in B(\mathcal H)_{\mathrm{sa}}:a\ge0\}$, $B(\mathcal H)_{\mathrm{sa}}$
is an order-unit space whose order-unit norm equals the operator norm.

**Notes / provenance.** HOS §1.2.1 `refs/hos/joa-m.md:366-372`. This is the structure that **survives**
when the associative product is dropped; in the channel setting it is inherited *exactly* by the
near-fixed algebra (only the product is approximate). Basis of [[def-eps-jb-algebra]],
[[def-near-fixed-algebra]]. Uses [[def-self-adjoint-part]].
