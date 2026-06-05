---
id: def-near-fixed-algebra
term: near-fixed algebra
aliases: A = Im P; projected Jordan product; bullet product; a•b
kind: original
status: locked
source: internal
locus: report sec:spectral (eq:projected-product); sec:epsjb; theorem-B-algebraic-bridge.md
sha256: -
consensus: A+B; the bridge's central object, A-verified v0.5 §10
---

**Statement.** Let $P$ be the [[def-spectral-idempotent]] of an [[def-almost-idempotent]]
[[def-positive-unital-map]] $\Phi$. The *near-fixed algebra* is its range
$$A=\operatorname{Im}P=\operatorname{Ker}(\mathbf 1-P)\subseteq B(\mathcal H)_{\mathrm{sa}},$$
a real subspace containing $\mathbf 1$, equipped with the **projected Jordan product**
$$a\bullet b := P(a\circ b),\qquad a,b\in A,$$
where $\circ$ is the ambient [[def-jordan-product]]. The order, unit, and order-unit norm on $A$ are
inherited **exactly** from $B(\mathcal H)_{\mathrm{sa}}$; only $\bullet$ is approximate.

**Notes / provenance.** Project-original object (the Jordan analogue of the Choi–Effros / Effros–Størmer
construction). Report sec:spectral eq:projected-product; analysed in sec:epsjb; the bridge theorem
(registry thm-bridge) proves $(A,\bullet)$ is an [[def-eps-jb-algebra]] with $\varepsilon\le C\sqrt\eta$.
The deviation of $A$ from ambient-$\circ$-closure is measured by the [[def-square-hole]].
