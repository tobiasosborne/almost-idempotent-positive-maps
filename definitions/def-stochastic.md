---
id: def-stochastic
term: stochastic idempotent
aliases: row-stochastic map; signed affine retraction; negative mass; row polytope
kind: consensus
status: locked
source: internal
locus: report sec:classical (def:stochastic); markov-affine-retraction-formulation.md
sha256: -
consensus: A+B; B's classical formulation, in report sec:classical (A leads report)
---

**Statement (commutative vocabulary).** A *unital positive map* of $\ell^\infty_n=\mathbb R^n$ is a
*row-stochastic matrix* $Q$ ($Q\ge0$ entrywise, $Q\mathbf 1=\mathbf 1$) — an affine self-map of the
probability simplex $\Delta_n$. A *stochastic idempotent* $E$ is a row-stochastic $E$ with $E^2=E$ (an
affine retraction of $\Delta_n$ onto a sub-polytope). A *signed affine retraction* is $P$ with
$P\mathbf 1=\mathbf 1$ and $P^2=P$ exactly, whose rows are signed measures of total mass $1$; its
*negative mass* is $\delta=\max_i\sum_j\max(-P_{ij},0)$, and its *row polytope* is $K=\mathrm{conv}\{$rows$\}$.

**Notes / provenance.** Project formulation (B's `markov-affine-retraction-formulation.md`; report
sec:classical `def:stochastic`). The signed form is the working object because $P^2=P$ holds *exactly*
(non-positivity quarantined in $\delta$). This is the commutative specialization of
[[def-near-positive-projection]]; the open classical stability problem is `op:classical` (registry).
Uses [[def-exposed]].
