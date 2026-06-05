---
id: lem-exposed-circuit
kind: lemma
contract: For a signed affine retraction with neg mass <= delta: (i) a (rho,kappa)-exposed row vertex v concentrates, ||v-pi_v||_1 <= C(delta/kappa+delta) for a probability pi_v supported on U_v={j:||p_j-v||_1<rho}; (ii) for pairwise-separated (rho,kappa)-exposed vertices v_a, ||sum c_a v_a||_1 >= (1-C(delta/kappa+delta)) sum|c_a|; both RHS are 1-O(sqrt delta) when kappa >= c sqrt(delta).
defs: def-exposed
deps: lem-leakage
status: proved
af: none
provenance: B-EXC (concentration + circuit cancellation); report lem:exposed-circuit
owner: B
workspace: proofs/lem-exposed-circuit
---

At an exposed vertex the positive mass concentrates near the vertex and signed mass cancels around ell^1
circuits, with dimension-free constants. Uses [[def-exposed]]; builds on lem-leakage. Report
`lem:exposed-circuit` (status proved). Theory: agent-B/notes/exposed-circuit-cancellation.md (B-EXC).
