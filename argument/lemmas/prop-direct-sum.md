---
id: prop-direct-sum
kind: proposition
contract: If B=⊕_r B_r (order-unit norm = max_r) and each factor has an exact-adjoint coboundary splitting with constant K_r, then B has one with constant max_r K_r + 1, independent of the number of summands (off-block components recovered by P_r f(e_r,·), with no sum over r); valid for adjoint/block-respecting modules.
defs: def-jordan-coboundary; def-jb-algebra
deps:
status: proved
af: validated
provenance: agent-B/notes/adjoint-direct-sum-reduction.md; agent-B/notes/spin-direct-sum-adjoint-corollary.md; report prop:direct-sum
owner: B
workspace: proofs/prop-direct-sum
---

The summand-count-free direct-sum reduction for the exact-adjoint [[def-jordan-coboundary]] splitting:
over a direct sum of [[def-jb-algebra]]s the splitting constant gains only a universal +1, with no
dependence on the number of summands, because off-block primitive components are read off the coboundary
by evaluating at the central units e_r. Adjoint/block-respecting modules only (arbitrary modules can
carry mixed Peirce-1/2 components). Report `prop:direct-sum`; theory:
agent-B/notes/adjoint-direct-sum-reduction.md.
