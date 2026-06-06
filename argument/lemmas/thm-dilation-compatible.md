---
id: thm-dilation-compatible
kind: theorem
contract: If there is a unital order-isometric Jordan embedding j:B(H)_sa->D_sa and a unital positive C:D_sa->B(H)_sa with Phi=Cj whose lift F=jC extends to a UCP map D->D with ||F^2-F||_cb <= eta, then with P=theta(2Phi-1), A=Im P, a•b=P(a∘b), the algebra A is an O(eta)-eps-JB order-unit algebra (by reduction to Kitaev's CP theorem for F).
defs: def-spectral-idempotent; def-near-fixed-algebra; def-eps-jb-algebra
deps: lem-cstar-sa-to-epsjb; lem-intertwine-spectral-idempotent; lem-idempotence-inheritance; lem-P-properties
status: proved
af: none
provenance: agent-B/notes/decomposable-dilation-compatible-theorem.md; report thm:dilation-compatible (report/sections/10-exponent.tex)
owner: B
workspace: proofs/thm-dilation-compatible
---

The clean conditional Kitaev-strength result: a lifted-UCP (dilation-compatibility) hypothesis ||F^2-F||_cb
<= eta supplies the missing two-hole structure, and j embeds A isometrically into the O(eta) eps-JB algebra
of F. Reduces to three factored sub-lemmas: the lift's structure is O(eta)-eps-JB by
[[lem-cstar-sa-to-epsjb]] (the C*->JB symmetrisation, the O(eta) crux); the spectral idempotents intertwine
(theta(2F-1)j=jP) by [[lem-intertwine-spectral-idempotent]]; P=theta(2Phi-1) is well-defined because Phi
inherits almost-idempotence by [[lem-idempotence-inheritance]]; and P's properties on B(H)_sa are
[[lem-P-properties]]. (def-decomposable-map was a non-load-bearing import, removed; the registry dep on
thm-bridge was structural-not-logical, replaced by the actual imports.) Report `thm:dilation-compatible`;
source report/sections/10-exponent.tex.
