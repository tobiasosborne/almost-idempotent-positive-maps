---
id: prop-rank-gap
kind: proposition
contract: On a simple Euclidean Jordan factor of rank r, the order-unit and Frobenius norms satisfy ||a||_op <= ||a||_2 <= sqrt(r) ||a||_op, with the upper ratio sqrt(r) attained at a=1; so the coboundary's order-vs-Frobenius gap is exactly sqrt(r) (r=2 spin, r=n for H_n, r=3 Albert).
defs: def-injective-cochain-norm; def-jordan-coboundary; def-spin-factor
deps:
status: proved
af: none
provenance: A-SPIN §1 (agent-A/theory/02-spin-splitting.md); agent-B/notes/cochain-norm-conversion-caveat.md; report prop:rank-gap
owner: A
workspace: proofs/prop-rank-gap
---

The single quantitative obstruction to converting a dimension-free Frobenius splitting of the
[[def-jordan-coboundary]] into an order-unit ([[def-injective-cochain-norm]]) one: the two element
norms are exactly sqrt(rank)-equivalent, sharp at the identity. Dimension-free for [[def-spin-factor]]s
(rank 2) but growing as sqrt(n) for the matrix families H_n. Report `prop:rank-gap`; theory:
agent-A/theory/02-spin-splitting.md §1.
