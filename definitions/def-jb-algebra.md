---
id: def-jb-algebra
term: JB-algebra
aliases: Jordan Banach algebra; JB algebra
kind: cited
status: locked
source: hos
locus: joa-m.md:2308-2316 (3.1.3-3.1.4)
sha256: 28740e73d547dd46
consensus: transcribed report sec:jordan (def:jb-algebra)
---

**Statement.** A *Jordan Banach algebra* is a real [[def-jordan-algebra]] $A$ with a complete norm
satisfying $\lVert a\circ b\rVert\le\lVert a\rVert\lVert b\rVert$. A *JB-algebra* is a Jordan Banach
algebra whose norm additionally satisfies, for all $a,b\in A$:
$$\lVert a^2\rVert=\lVert a\rVert^2, \qquad \lVert a^2\rVert\le\lVert a^2+b^2\rVert.$$
The first is the Jordan analogue of the C\*-identity; the second forces sums of squares to dominate
their summands (so positivity = being a square is well-behaved). $B(\mathcal H)_{\mathrm{sa}}$ is the
motivating JB-algebra under [[def-jordan-product]] and the operator norm.

**Notes / provenance.** HOS 3.1.3-3.1.4 `refs/hos/joa-m.md:2308-2316`. These two norm axioms are exactly
what JB1+JB2 (square norm) and JB3 (square positivity) of [[def-eps-jb-algebra]] relax to order
$\varepsilon$. See [[def-jc-algebra]] (the special, Hilbert-space-representable ones).
