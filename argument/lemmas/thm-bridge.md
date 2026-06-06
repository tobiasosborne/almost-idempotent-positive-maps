---
id: thm-bridge
kind: theorem
contract: For unital positive Phi on B(H)_sa with ||Phi^2-Phi|| <= eta <= eta_0, the near-fixed algebra (A=Im P, •, 1, A∩B(H)_+) is an eps-JB algebra with eps <= C sqrt(eta), with universal dimension-free constants and no use of complete positivity.
defs: def-eps-jb-algebra; def-near-fixed-algebra; def-spectral-idempotent; def-almost-idempotent
deps: lem-P-properties; lem-first-insertion; lem-square-hole-almost-positive; prop-bridge-jordan; lem-bridge-easy; lem-bridge-orderunit
status: proved
af: validated
provenance: theorem-B-algebraic-bridge.md:7-50; report thm:bridge (A-verified line-by-line v0.5 §10)
owner: B
workspace: proofs/thm-bridge
---

**Layer-2 bridge theorem — the project's proved centerpiece.** Combines the easy axioms (JB1-JB3,
O(eta)) with the approximate Jordan identity (JB4, O(sqrt eta), prop-bridge-jordan). Dimension-free,
CP-free. Report `thm:bridge`; B's proof, A-verified. This is the first target for af formalization
(Phase 3) and the eventual fresh Lean proof (Phase 5).
