---
id: prop-rounding-fails
kind: obstruction
contract: Generic O(eps) positivity rounding is false: for each m>=1 (eps=1/(2m)) the spin-factor target J=R⊕R^m carries an eps-positive unital map T on l_infty^{2m} with ||T-S||>=sqrt(eps) for every positive unital map S (Rademacher lower bound; free maps, no retraction constraint).
defs: def-spin-factor; def-positive-unital-map; def-eps-jb-algebra
deps:
status: proved
af: none
provenance: B-ROUND §§2-4; subagent-positivity-rounding.md; report prop:rounding-fails
owner: B
workspace: proofs/prop-rounding-fails
---

No dimension-free black-box repair of an eps-positive map to a genuine [[def-positive-unital-map]]
exists: on a [[def-spin-factor]] one loses at least a square root. Motivates restricting to idempotents
(op-npps), whose retraction constraint blocks the sign-spreading construction. Commutative-commutative
case is exempt (positive within 2 eps). Report `prop:rounding-fails`; theory:
report/sections/07-exact-factorization.tex (prop:rounding-fails).
