---
id: thm-cluster
kind: theorem
contract: There are universal delta_0,C>0 such that a signed affine retraction P with neg mass <= delta <= delta_0 having representatives r^1..r^m pairwise 2rho-separated, each (rho,kappa)-exposed (disjoint clusters U_a), with every off-cluster row within gamma of conv{r^a}, admits a stochastic idempotent E with ||P-E||_{inf->inf} <= C(rho+gamma+delta/kappa+delta); so rho,gamma=O(sqrt delta), kappa>=c sqrt(delta) give O(sqrt delta), C independent of m, n, and the number of transient rows.
defs: def-exposed; def-stochastic
deps: lem-exposed-circuit
status: proved
af: none
provenance: CL-FAC; cluster-representative-classical-stability.md; report thm:cluster
owner: B
workspace: proofs/thm-cluster
---

Cluster-representative stability: well-separated exposed clusters reconstruct a stochastic idempotent with no
accumulation over representatives or transient rows. Uses [[def-exposed]], [[def-stochastic]]; via
lem-exposed-circuit. Report `thm:cluster` (status proved). Theory:
agent-B/notes/cluster-representative-classical-stability.md (CL-FAC).
