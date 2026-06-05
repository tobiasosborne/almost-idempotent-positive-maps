---
id: prop-parallelogram
kind: proposition
contract: If rows r_1..r_k have distinct binary codewords realised by affine s_1..s_m:K->[0,1] (s_l(r_a) in {0,1}), then for all c_a, ||sum_a c_a r_a||_1 >= (1-C m sqrt delta) sum|c_a|; so for m sqrt(delta) small the rows are affinely independent and bounded-complexity product-of-simplices geometries (e.g. an exact parallelogram) cannot occur; the constant degrades with the number m of coordinate bits.
defs: def-stochastic
deps:
status: proved
af: none
provenance: parallelogram-classical-stability.md; report prop:parallelogram
owner: B
workspace: proofs/prop-parallelogram
---

Bounded binary-coordinate affine dependencies force an m sqrt(delta) lower bound, ruling them out at small
delta (the parallelogram obstruction); does not settle geometries needing unboundedly many witnesses. Uses
[[def-stochastic]]. Report `prop:parallelogram` (status proved). Theory:
agent-B/notes/parallelogram-classical-stability.md.
