---
id: prop-doubling
kind: obstruction
contract: Naive doubling fails: for Phi=Cj one has F^2-F=j((Phi-1)C), and ||Phi^2-Phi|| controls (Phi-1) only on inputs Phi(x), not on all C(D); a commutative example (j:l^inf_2->l^inf_4, j(x1,x2)=(x1,x2,x1,x2)) has Phi=Cj exactly idempotent yet ||F^2-F||_{inf->inf}=1.
defs: def-decomposable-map
deps:
status: proved
af: none
provenance: decomposable-doubling-obstruction.md; report prop:doubling
owner: B
workspace: proofs/prop-doubling
---

Rules out proving op-decomposable by applying Kitaev's CP theorem to the doubled lift F=jC: exact
idempotence of Phi does not force approximate idempotence of F (so the dilation-compatibility hypothesis of
thm-dilation-compatible is not automatic). Uses [[def-decomposable-map]]. Report `prop:doubling`; source
report/sections/10-exponent.tex.
