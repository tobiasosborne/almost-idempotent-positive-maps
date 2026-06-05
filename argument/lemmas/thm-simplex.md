---
id: thm-simplex
kind: theorem
contract: There are universal delta_0,C>0 such that every signed affine retraction P with neg mass <= delta <= delta_0 whose row polytope K is (i) of affine dimension <=1 (point/segment) or (ii) a simplex with vertices among the rows admits a stochastic idempotent E with ||P-E||_{inf->inf} <= C sqrt(delta), constant C independent of the number of vertices m and of n.
defs: def-stochastic
deps: lem-classical-equiv
status: proved
af: none
provenance: B-SIMP; line-segment-classical-stability.md; report thm:simplex
owner: B
workspace: proofs/thm-simplex
---

Line-segment and simplex retractions are O(sqrt delta)-stable with a vertex-count-free constant (no factor in
m or n, since the barycentric decomposition is convex). Uses [[def-stochastic]]; via lem-classical-equiv.
Report `thm:simplex` (status proved). Theory: agent-B/notes/line-segment-classical-stability.md,
simplex-classical-stability.md (B-SIMP).
