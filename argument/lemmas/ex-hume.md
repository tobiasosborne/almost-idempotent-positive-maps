---
id: ex-hume
kind: obstruction
contract: The explicit 3x3 family P_s=I-u_s v_s^T (v_s=(1,-1+s,-s), u_s=(1-s+s^2,-s,0)^T) is a signed affine retraction with neg mass delta=s^2 whose distance to every stochastic idempotent is 2s-2s^2+2s^3 = 2 sqrt(delta)+O(delta): no bound C delta^beta with beta>1/2 holds, so the exponent 1/2 in op-classical/op-npps is sharp.
defs: def-stochastic
deps:
status: proved
af: none
provenance: rank-one-classical-stability.md; experiment explicit_sqrt_family; report ex:hume
owner: B
workspace: proofs/ex-hume
---

Hume's explicit family realises the sqrt(delta) lower bound, certifying that the 1/2 exponent in op-classical
is optimal. Uses [[def-stochastic]]. Report `ex:hume` (status proved; sharpness). Theory:
agent-B/notes/rank-one-classical-stability.md; experiment agent-B/experiments/classical-projection-stability/explicit_sqrt_family.
