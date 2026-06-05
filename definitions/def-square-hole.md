---
id: def-square-hole
term: square hole
aliases: q_r; null-square element
kind: original
status: locked
source: internal
locus: report sec:bridge (lem:bridge-squarehole); theorem-B-algebraic-bridge.md:301-372
sha256: -
consensus: A+B; B introduced in the bridge proof, A-verified v0.5 §10
---

**Statement.** Let $P$ be the [[def-spectral-idempotent]] and $A=\operatorname{Im}P$ the
[[def-near-fixed-algebra]]. For $r\in A$, the *square hole* is
$$q_r := P(r^2)-r^2 \in \operatorname{Ker}P,$$
the failure of $A$ to be closed under the *ambient* squaring. More generally the *product hole* of
$r,s\in A$ is $h_{r,s}:=r\circ s-P(r\circ s)\in\operatorname{Ker}P$ (so $q_r=-h_{r,r}$).

**Why it matters.** Square holes are *almost-positive null* elements: $q_r\ge -C\eta\lVert r\rVert^2\mathbf 1$
(Kadison) and $\lVert P(q_r^2)\rVert\le C\eta\lVert r\rVert^4$. This is the crux fact of the bridge — it is
what makes one-hole insertions $O(\sqrt\eta)$ and two-hole insertions $O(\eta)$ in the state seminorm.
The $O(\eta)$ (not $O(\eta^2)$) rate is sharp ($\lVert P(q_r^2)\rVert/\eta\to 32/27$ numerically).

**Notes / provenance.** Project-original notation/object, introduced by B in the bridge proof
(`theorem-B-algebraic-bridge.md:301-372`, registry `lem-square-hole-almost-positive`), A-verified
(`agent-a-findings v0.5 §10`). The bounds themselves are registry lemmas, not part of this definition.
