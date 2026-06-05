---
id: thm-rank-one
kind: theorem
contract: There are universal delta_0,C>0 such that every rank-one signed affine retraction P=I-u v^T (sum_j v_j=0, v^T u=1) with neg mass <= delta <= delta_0 is within ||P-E||_{inf->inf} <= C sqrt(delta) of a stochastic idempotent E; this class contains Hume's sharp family (ex-hume).
defs: def-stochastic
deps: lem-classical-equiv
status: proved
af: none
provenance: rank-one-classical-stability.md; report thm:rank-one
owner: B
workspace: proofs/thm-rank-one
---

Rank-one retractions are O(sqrt delta)-stable; this is the special case containing the sharp Hume example.
Uses [[def-stochastic]]; via lem-classical-equiv. Report `thm:rank-one` (status proved). Theory:
agent-B/notes/rank-one-classical-stability.md.
