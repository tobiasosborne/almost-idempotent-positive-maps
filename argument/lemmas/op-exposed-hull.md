---
id: op-exposed-hull
kind: open-problem
contract: (OPEN) Global exposed-hull lemma: there are universal c,C>0 such that for every near-positive signed affine retraction with neg mass <= delta, taking rho=C sqrt(delta) and W_{rho,kappa}={vertices v: e_v(rho)>=kappa} with kappa=c sqrt(delta), every row is within C sqrt(delta) of conv W_{rho,kappa}; by thm-classical-factorization (global form) this implies op-classical.
defs: def-exposed; def-stochastic
deps:
status: open
af: none
provenance: simultaneous-skeleton-reduction.md; exposed-redundant-dichotomy-target.md; report op:exposed-hull
owner: B
workspace: proofs/op-exposed-hull
---

The remaining classical obstruction: a simultaneous (not pointwise) skeleton reduction over all exposed
vertices; implies op-classical and the unconditional exact factorization. A pointwise exposed/redundant
dichotomy is insufficient (redundancy can be circular). Uses [[def-exposed]], [[def-stochastic]]. Report
`op:exposed-hull` (status open). Theory: agent-B/notes/simultaneous-skeleton-reduction.md,
exposed-redundant-dichotomy-target.md.
