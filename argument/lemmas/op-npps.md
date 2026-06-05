---
id: op-npps
kind: open-problem
contract: (OPEN, sharp exponent 1/2) Near-positive projection stability: there are dimension-free delta_0,K so that any linear R on B(H)_sa with R^2=R, R(1)=1, ||R||<=1+delta and R(x)>=-delta 1 for 0<=x<=1 (delta<=delta_0) has a unital positive idempotent E with ||E-R||<=K sqrt(delta).
defs: def-near-positive-projection; def-spectral-idempotent
deps:
status: open
af: none
provenance: B-NPPS (near-positive-projection-stability-program.md); TS3 (Theorem 3 hypothesis); report op:npps
owner: B
workspace: proofs/op-npps
---

The single unproved input of the factorization route: round a delta-positive unital idempotent to a
genuine [[def-near-positive-projection]] (unital positive idempotent) at the sharp sqrt(delta) rate,
dimension-free. The spectral idempotent [[def-spectral-idempotent]] P=theta(2Phi-I) is the target R.
Open in general; commutative reduction and special cases in Sec. classical. Report `op:npps`;
theory: agent-B/notes/near-positive-projection-stability-program.md.
