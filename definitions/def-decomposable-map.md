---
id: def-decomposable-map
term: decomposable map
aliases: CP+coCP; decomposable positive map
kind: cited
status: draft
source: vlw-2604.08380
locus: paper.tex (decomposable = CP + coCP∘transpose); cf. subagent-decomposable-norm.md
sha256: 3395946df12f6606
consensus: report def:decomposable (status I — inline-provenanced; BYTE-CHECK PENDING against refs/vlw)
---

**Statement.** A positive map $\Phi$ is *decomposable* if $\Phi=\Phi_0+\Psi_0\circ\tau$ where
$\Phi_0,\Psi_0$ are completely positive and $\tau$ is the transpose (a Jordan automorphism) — a sum of a
CP and a co-CP map. **Correct hypothesis (not the decomposable norm):** the Haagerup–Wittstock
decomposable norm is *not* $1$ for unital positive decomposable maps ($\tau_n$ on $M_n$ has decomposable
norm $n$); the right control is the per-summand CP component bound $\lVert\Phi_0\rVert_{\mathrm{cb}},
\lVert\Psi_0\rVert_{\mathrm{cb}}\le1$ from unitality.

**Notes / provenance.** Cited from van Luijk–Wilming (`refs/vlw-2604.08380/paper.tex`); the norm caveat is
B's `subagent-decomposable-norm.md`. **status=draft: I-level provenance — the exact VLW locus/text is not
yet byte-verified in this DB (gate will WARN until upgraded).** Decomposability is the natural class for the
conjectural $O(\eta)$ (α=1) exponent (registry `op-decomposable`), where each summand carries a dilation.
