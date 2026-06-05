---
id: lem-square-hole-almost-positive
kind: lemma
contract: For r in A the square hole q_r = P(r^2)-r^2 in Ker P satisfies q_r >= -C eta ||r||^2 1, ||P(q_r^2)|| <= C eta ||r||^4, and ||q_r||_omega <= C sqrt(eta) ||r||^2.
defs: def-square-hole; def-spectral-idempotent; def-near-fixed-algebra
deps: lem-P-properties
status: proved
af: none
provenance: theorem-B-algebraic-bridge.md:301-372; report lem:bridge-squarehole
owner: B
workspace: proofs/lem-square-hole-almost-positive
---

The crux fact: square holes are almost-positive null. The O(eta) (not O(eta^2)) rate is sharp (32/27,
registry rem-bridge-numerics). Report `lem:bridge-squarehole`.
