---
id: obs-exponent
kind: obstruction
contract: The general positive-map bridge attains only eps=O(sqrt eta) because a single insertion is controlled only in the state seminorm (Jordan-Schwarz, squared size O(eta)); Kitaev's O(eta) is an intrinsically bilinear two-hole Cauchy-Schwarz pairing W with ||W||=O(sqrt eta)*O(sqrt eta)=O(eta) that lives in the Stinespring dilation and needs complete positivity (cb/dilation-compatible), so the merely-decomposable case stays open (op-decomposable).
defs: def-eps-jb-algebra; def-decomposable-map
deps: thm-bridge; obs-bridge-numerics
status: proved
af: none
provenance: A-FIND §9-10; KIT 2643-2673; report rem:exponent
owner: B
workspace: proofs/obs-exponent
---

Explains the sqrt(eta)-vs-eta gap: positivity controls one hole only in the seminorm of omega=rho∘Phi
(O(sqrt eta)), whereas Kitaev's O(eta) is a bilinear pairing of two dilation-space holes needing CP. Uses
[[def-eps-jb-algebra]], [[def-decomposable-map]]. Report `rem:exponent`; source report/sections/10-exponent.tex.
