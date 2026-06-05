---
id: def-jordan-product
term: Jordan product
aliases: ∘; symmetrized product; jp
kind: cited
status: locked
source: hos
locus: joa-m.md:812 (eq. 2.17)
sha256: 28740e73d547dd46
consensus: transcribed in report sec:jordan (def:jordan-algebra), notation harmonised to ∘
---

**Statement.** For elements $a,b$ of an associative algebra, the *Jordan product* is
$$a \circ b = \tfrac12(ab+ba).$$
For $a,b$ self-adjoint, $a\circ b$ is self-adjoint, so $\circ$ keeps us inside $B(\mathcal H)_{\mathrm{sa}}$
where the associative product $ab$ does not. We write $a^2 := a\circ a$.

**Notes / provenance.** Byte-matched to Hanche-Olsen–Størmer, *Jordan Operator Algebras*, eq. (2.17)
(`refs/hos/joa-m.md:812`). Notation harmonised: HOS write $a\circ b$; Kitaev `½(XY+YX)`; van Luijk–Wilming
`{a,b}=½(ab+ba)`. The ambient $\circ$ on $B(\mathcal H)_{\mathrm{sa}}$ satisfies the Jordan identity
*exactly* — this exactness is the cancellation engine of the bridge theorem.
Underlies [[def-jordan-algebra]], [[def-near-fixed-algebra]], [[def-square-hole]].
