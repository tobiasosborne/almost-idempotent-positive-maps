---
id: prop-decomposable-norm
kind: proposition
contract: The Haagerup-Wittstock decomposable norm is not 1 for every unital positive decomposable map (the transpose tau_n on M_n has ||tau_n||_dec=||tau_n||_cb=n); the correct boundedness input is instead the per-summand cb component bound ||Phi_0||_cb,||Psi_0||_cb <= 1 forced by unitality Phi_0(1)+Psi_0(1)=1.
defs: def-decomposable-map
deps:
status: proved
af: none
provenance: subagent-decomposable-norm.md; report prop:decomposable-norm
owner: B
workspace: proofs/prop-decomposable-norm
---

Fixes the right hypothesis for an O(eta) decomposable theorem: not the (unbounded) decomposable norm but
an explicit CP+coCP decomposition with per-summand cb budget 1. Uses [[def-decomposable-map]]. Report
`prop:decomposable-norm`; source report/sections/10-exponent.tex.
