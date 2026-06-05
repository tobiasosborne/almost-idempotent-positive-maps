---
id: prop-kadison-js
kind: proposition
contract: A unital positive map T satisfies the Jordan-Schwarz inequality {Ta*, Ta} <= T{a*,a} for all a (where {x,y}=x∘y); its self-adjoint case a=a* is Kadison's inequality Phi(a)^2 <= Phi(a^2), and a merely positive unital map need NOT satisfy the (2-positive) Schwarz inequality Phi(a)*Phi(a) <= Phi(a*a).
defs: def-positive-unital-map; def-jordan-product
deps:
status: cited
af: none
provenance: refs/vlw-2604.08380/paper.tex:555-560 (lem:JS-inequality, Stormer 1963 Lem 7.3); Kadison1952; report prop:kadison-js
owner: A
workspace: proofs/prop-kadison-js
---

The single positivity inequality available for merely positive unital maps: Stormer's Jordan-Schwarz
inequality, with Kadison's inequality as the self-adjoint special case. Uses [[def-positive-unital-map]]
and the [[def-jordan-product]]. Cited background; report `prop:kadison-js` (02-preliminaries.tex; VLW
Lem 7.3 / Stormer 1963, Kadison 1952).
