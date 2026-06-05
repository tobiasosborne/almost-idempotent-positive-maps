---
id: def-eps-jb-algebra
term: ε-JB algebra
aliases: epsilon-JB algebra; approximate JB algebra; eps-JB
kind: consensus
status: locked
source: internal
locus: report sec:epsjb (def:eps-jb); agent-a-findings §5; theorem-B-algebraic-bridge.md:36-50,86
sha256: -
consensus: A+B agreed (A-FIND §5 LOCKED; realised at ε≤C√η by the bridge, A-verified v0.5 §10)
---

**Statement.** Let $\varepsilon\ge 0$. An *ε-JB algebra* (order-unit form) is a finite-dimensional real
order-unit space $(A,\mathbf 1,\le)$ with order-unit norm $\lVert\cdot\rVert$, together with a commutative
bilinear product $\circ\colon A\times A\to A$ for which **commutativity** $a\circ b=b\circ a$ and the
**unit law** $\mathbf 1\circ a=a$ hold *exactly*, and such that for all $a,b\in A$:

- **(JB1)** $\lVert a\circ b\rVert \le (1+\varepsilon)\,\lVert a\rVert\,\lVert b\rVert$ — approximate submultiplicativity;
- **(JB2)** $\lVert a\circ a\rVert \ge (1-\varepsilon)\,\lVert a\rVert^2$ — lower square-norm bound;
- **(JB3)** $a\circ a \ge -\varepsilon\,\lVert a\rVert^2\,\mathbf 1$ — approximate positivity of squares;
- **(JB4)** $\lVert((a\circ a)\circ b)\circ a-(a\circ a)\circ(b\circ a)\rVert \le \varepsilon\,\lVert a\rVert^3\,\lVert b\rVert$ — approximate Jordan identity.

**Key design point (consensus).** The order, unit, and norm are **exact**; only the *product* carries
the defect. At $\varepsilon=0$ the four axioms degenerate exactly to the JB-algebra axioms
([[def-jb-algebra]]): JB1→submultiplicativity, JB1+JB2→$\lVert a^2\rVert=\lVert a\rVert^2$, JB3→squares
positive (formal reality), JB4→the exact Jordan identity. This is strictly cleaner than Kitaev's
ε-C\*-algebras, where the norm itself is only approximately multiplicative.

**Notes / provenance.** Project-internal *consensus* definition (no single external source): proposed by A
(`agent-a-findings §5`), the exact axiom list B proves realised with $\varepsilon\le C\sqrt\eta$
(`theorem-B-algebraic-bridge.md:36-50,86`), A-verified line-by-line (v0.5 §10). That it is *realised* by
[[def-spectral-idempotent]] + [[def-near-fixed-algebra]] is the separate **proved** content of the bridge
theorem (registry `thm-bridge`), not part of this definition. A definition is never `(proved)`; this is
`(consensus)`.
