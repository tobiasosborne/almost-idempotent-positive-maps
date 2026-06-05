---
id: thm-classical-factorization
kind: theorem
contract: There are universal eta_0,C>0 such that if Q is row-stochastic with eta=||Q^2-Q||_{inf->inf}<=eta_0 and the rows of P=theta(2Q-1) satisfy the thm-cluster geometry (rho,gamma=O(sqrt eta), kappa>=c sqrt eta), then there exist a finite-dim commutative special JB-algebra J and unital positive maps Delta:J->ell^inf_n, Upsilon:ell^inf_n->J with Upsilon Delta=id_J, ||Delta Upsilon-Q||_{inf->inf}<=C sqrt(eta), and Upsilon(Delta x . Delta y)=x*y.
defs: def-stochastic; def-positive-unital-map
deps: thm-cluster; op-exposed-hull
status: proved
af: none
provenance: CL-FAC (incl. global exposed-hull corollary); report thm:classical-factorization
owner: B
workspace: proofs/thm-classical-factorization
---

Under the cluster-geometry hypothesis (or its global exposed-hull form, op-exposed-hull) an almost-idempotent
commutative positive map admits an exact commutative unital-positive JB-factorization. Uses [[def-stochastic]],
[[def-positive-unital-map]]; via thm-cluster and op-exposed-hull. Report `thm:classical-factorization`
(status proved, conditional on the cluster geometry). Theory: agent-B/theory/classical-cluster-factorization-theorem.md (CL-FAC).
