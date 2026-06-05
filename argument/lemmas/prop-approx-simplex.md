---
id: prop-approx-simplex
kind: proposition
contract: If the rows of P admit gamma-approximate simplex coordinates (representatives r^a, affine lambda_a with sum lambda_a=1, lambda_a(r^b)=delta_ab, ||p_i-sum_a lambda_a(p_i) r^a||_1<=gamma) with the lambda_a nonnegative or of coefficient negative mass O(delta), then there is a stochastic idempotent E with ||P-E||_{inf->inf}<=C(sqrt delta+gamma); hence op-classical reduces to producing gamma=O(sqrt delta) approximate simplex coordinates with O(delta) coefficient negative mass.
defs: def-stochastic
deps: lem-classical-equiv
status: proved
af: none
provenance: approximate-simplexity-reduction.md; robust-approximate-simplexity-reduction.md; report prop:approx-simplex
owner: B
workspace: proofs/prop-approx-simplex
---

Reduces op-classical to a coordinate hypothesis: approximate simplex coordinates with O(delta) coefficient
negative mass (the O(delta) bound is the genuine target; O(sqrt delta) would only give O(delta^{1/4})). Uses
[[def-stochastic]]; via lem-classical-equiv. Report `prop:approx-simplex` (status proved; reduction). Theory:
agent-B/notes/approximate-simplexity-reduction.md, robust-approximate-simplexity-reduction.md.
