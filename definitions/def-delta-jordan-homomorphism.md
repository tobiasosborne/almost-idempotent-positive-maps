---
id: def-delta-jordan-homomorphism
term: δ-Jordan-homomorphism
aliases: delta-Jordan-homomorphism; δ-isomorphism; delta-isomorphism; approximate Jordan isomorphism
kind: consensus
status: locked
source: internal
locus: report sec:epsjb (def:eps-jb-iso); agent-a-findings §5
sha256: -
consensus: A+B; Jordan transcription of Kitaev's δ-hom/iso (B correction: not an order-iso unless added)
---

**Statement.** Let $A,B$ be [[def-eps-jb-algebra|ε-JB algebras]] and $\delta\ge0$. A
*$\delta$-Jordan-homomorphism* is a linear $v:A\to B$ with
$$\lVert v(\mathbf 1)-\mathbf 1\rVert\le\delta,\qquad \lVert v(a\circ b)-v(a)\circ v(b)\rVert\le\delta\,\lVert a\rVert\lVert b\rVert.$$
A *$\delta$-isomorphism* is a bijective $\delta$-Jordan-homomorphism that is an approximate isometry,
$(1-\delta)\lVert a\rVert\le\lVert v(a)\rVert\le(1+\delta)\lVert a\rVert$.

**Notes / provenance.** Consensus definition (report sec:epsjb def:eps-jb-iso; `agent-a-findings §5`); the
Jordan/commutative-product transcription of Kitaev's $\delta$-homomorphism/isomorphism. **Agent B
correction:** this is an algebraic+normed notion; it does *not* by itself guarantee that $v$ or
$v^{-1}$ approximately preserves the positive cone — order control is a *separate* requirement in the
factorization problem. The target of the open Layer-1 structure theorem (registry op-jordan-structure):
every ε-JB algebra is $C\varepsilon$-Jordan-isomorphic to a genuine JB-algebra.
