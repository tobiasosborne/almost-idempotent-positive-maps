---
id: prop-diag-next-arrow
kind: proposition
contract: For the fixed diagonal-frame action of D=R^n on M=H_n(F) (x·m=x•m), every unit-normalized symmetric 2-cochain theta satisfies dist(theta,im d^1)<=C||J theta||_inj and ||theta-Pi_n theta||_inj<=C'||J theta||_inj, where Pi_n=d^1 S_n is the bounded Rademacher projection onto coboundaries; the off-diagonal residual is reconstructed by endpoint/one-tail/tail-tail Walsh pieces (two-density sparse-sign identity). This closes only the fixed-frame DxD source block, not the full (moving-frame) matrix next-arrow.
defs: def-jordan-coboundary
deps:
status: proved
af: none
provenance: B-DNEXT (diagonal-frame-matrix-next-arrow-walsh-target.md); B-NEWTON (next-arrow-to-newton-error-reduction.md); report prop:diag-next-arrow
owner: B
workspace: proofs/prop-diag-next-arrow
---

The next-arrow (approximate-cocycle) estimate for the fixed diagonal-frame matrix module: a
dimension-free bounded Walsh/Rademacher projection of the [[def-jordan-coboundary]] reconstructing the
A, B, U, and W off-diagonal modes from the linearized Jordan defect by global diagonal-sign averages.
This settles the DxD source block of the high-rank matrix next-arrow; the DxE and ExE blocks
(moving-frame) remain open. Report `prop:diag-next-arrow`; theory:
agent-B/notes/diagonal-frame-matrix-next-arrow-walsh-target.md.
