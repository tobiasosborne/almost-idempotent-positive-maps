---
id: thm-well-exposed
kind: theorem
contract: There are universal delta_0,c,C>0 such that if a signed affine retraction P with neg mass <= delta <= delta_0 has every row-polytope vertex pairwise separated and (rho,kappa)-exposed with rho <= C sqrt(delta), kappa >= c sqrt(delta), then the vertices are affinely independent (K is a simplex) and thm-simplex gives a stochastic idempotent within C sqrt(delta).
defs: def-exposed; def-stochastic
deps: thm-simplex; lem-exposed-circuit
status: proved
af: none
provenance: well-exposed-classical-stability.md; report thm:well-exposed
owner: B
workspace: proofs/thm-well-exposed
---

Well-exposed, separated vertices cannot support a nontrivial affine dependence (by circuit cancellation), so
the polytope is a simplex and the simplex theorem applies. Uses [[def-exposed]], [[def-stochastic]]; via
thm-simplex and lem-exposed-circuit. Report `thm:well-exposed` (status proved). Theory:
agent-B/notes/well-exposed-classical-stability.md.
