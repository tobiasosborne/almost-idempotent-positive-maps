---
id: obs-cochain-caveats
kind: obstruction
contract: Two cheap routes to a dimension-free order-unit splitting are blocked: on H_n(R) the order-bounded 1-cochain h(x)=x_11 1 has ||d^1h||_op<=3 yet every primitive of d^1h has Frobenius norm >=sqrt(n) (an order-bounded coboundary forces a sqrt(n) Frobenius primitive); and the rank-one/nuclear-decomposition route loses dimension (Id on the traceless part of H_n(C) has operator norm 1 but nuclear norm >=dim). So the splitting must be estimated directly in the order norm.
defs: def-jordan-coboundary; def-injective-cochain-norm
deps: prop-rank-gap
status: proved
af: none
provenance: agent-B/notes/cochain-norm-conversion-caveat.md; agent-B/notes/nuclear-rank-one-route-caveat.md; report rem:cochain-caveats
owner: B
workspace: proofs/obs-cochain-caveats
---

Why a Frobenius-bounded splitting of the [[def-jordan-coboundary]] cannot be cheaply converted to the
order-unit ([[def-injective-cochain-norm]]) one: an order-bounded coboundary can force a sqrt(n)
Frobenius primitive, and summing rank-one primitive estimates pays a nuclear norm that grows with
dimension. Both no-gos sharpen prop-rank-gap and forbid routing through Frobenius/nuclear primitives;
the splitting must be estimated directly in the order norm. Report `rem:cochain-caveats`; theory:
agent-B/notes/cochain-norm-conversion-caveat.md, agent-B/notes/nuclear-rank-one-route-caveat.md.
