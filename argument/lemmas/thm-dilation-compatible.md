---
id: thm-dilation-compatible
kind: theorem
contract: If there is a unital order-isometric Jordan embedding j:B(H)_sa->D_sa and a unital positive C:D_sa->B(H)_sa with Phi=Cj whose lift F=jC extends to a UCP map D->D with ||F^2-F||_cb <= eta, then with P=theta(2Phi-1), A=Im P, a•b=P(a∘b), the algebra A is an O(eta)-eps-JB order-unit algebra (by reduction to Kitaev's CP theorem for F).
defs: def-decomposable-map
deps: thm-bridge
status: proved
af: none
provenance: B-DECDIL; decomposable-dilation-compatible-theorem.md; report thm:dilation-compatible
owner: B
workspace: proofs/thm-dilation-compatible
---

The clean conditional Kitaev-strength result: a lifted-UCP (dilation-compatibility) hypothesis ||F^2-F||_cb
<= eta supplies the missing two-hole structure, and j embeds A isometrically into the O(eta) eps-JB algebra
of F. Uses [[def-decomposable-map]]. Report `thm:dilation-compatible`; source report/sections/10-exponent.tex.
