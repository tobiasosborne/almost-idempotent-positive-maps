---
id: prop-spin-splitting
kind: proposition
contract: For a spin factor V=R1+H the exact-adjoint Jordan coboundary d^1 has an O(H)-equivariant right inverse S with ||Sf||_F<=2||f||_inj, hence (by the rank-2 norm comparison) order-unit constant ||S||_{op->op}<=4 sqrt2, independent of dim H; and a normalized adjoint 2-cochain theta with theta(1,z)=0 obeys dist(theta,im d^1)<=(2 sqrt2+2)||J theta|| (next-arrow estimate).
defs: def-spin-factor; def-jordan-coboundary; def-injective-cochain-norm
deps:
status: proved
af: none
provenance: B-SPINADJ (adjoint-spin-splitting-theorem.md); agent-B/notes/spin-normalized-cocycle-projection-reduction.md; A-SPIN §2 (agent-A/theory/02-spin-splitting.md); report prop:spin-splitting
owner: B
workspace: proofs/prop-spin-splitting
---

The spin-factor case of the exact-adjoint benchmark: a dimension-free order-unit-bounded splitting of
the [[def-jordan-coboundary]] on a [[def-spin-factor]], with constant 4 sqrt2, plus the matching
next-arrow (cocycle-projection) estimate. The rank-2 structure makes the order and Frobenius
([[def-injective-cochain-norm]]) norms sqrt2-equivalent, so the rank gap (prop-rank-gap) is absent;
independently obtained by both authors. Report `prop:spin-splitting`; theory:
agent-B/notes/spin-normalized-cocycle-projection-reduction.md, agent-A/theory/02-spin-splitting.md §2.
