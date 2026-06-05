---
id: cor-adjoint-benchmark
kind: corollary
contract: (benchmark; modulo obs-matrix-audit) There is a universal C so that for every finite-dimensional JB-algebra B and every exact-adjoint coboundary f=d^1h in C^2(B,B) there is a derivation delta with ||h-delta||<=C||f||_inj: the exact-adjoint Jordan-coboundary inversion (an order-unit-bounded right inverse of d^1 modulo derivations) is dimension-free, uniformly over all B and all numbers of simple summands -- the master exact-adjoint benchmark.
defs: def-jordan-coboundary; def-jb-algebra; def-injective-cochain-norm
deps: prop-spin-splitting; prop-direct-sum; prop-comm-scalar; thm-matrix-splitting
status: proved
af: none
provenance: B-ADJ (finite-dimensional-adjoint-jb-splitting-corollary.md); report cor:adjoint-benchmark
owner: B
workspace: proofs/cor-adjoint-benchmark
---

The assembled exact-adjoint benchmark: combining the spin (prop-spin-splitting), direct-sum
(prop-direct-sum), commutative-scalar (prop-comm-scalar), and high-rank matrix (thm-matrix-splitting)
cases gives a dimension-free order-unit ([[def-injective-cochain-norm]]) right inverse of the
[[def-jordan-coboundary]] on every finite-dimensional [[def-jb-algebra]], modulo the matrix re-audit
(obs-matrix-audit). This is the right inverse for exact cocycles only; the next-arrow and other gaps
remain (op-layer1-gap). Report `cor:adjoint-benchmark`; theory:
agent-B/notes/finite-dimensional-adjoint-jb-splitting-corollary.md.
