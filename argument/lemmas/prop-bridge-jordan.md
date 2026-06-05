---
id: prop-bridge-jordan
kind: proposition
contract: The projected product on A=Im P satisfies the approximate Jordan identity ||((a•a)•b)•a - (a•a)•(b•a)|| <= C sqrt(eta) ||a||^3 ||b||, by exact-ambient-Jordan-identity cancellation of the leading term with O(sqrt(eta)) one-hole error terms.
defs: def-eps-jb-algebra; def-jordan-product; def-near-fixed-algebra
deps: lem-first-insertion; lem-square-hole-almost-positive; lem-bridge-polar; lem-bridge-onehole
status: proved
af: none
provenance: theorem-B-algebraic-bridge.md:489-597; report prop:bridge-jordan
owner: B
workspace: proofs/prop-bridge-jordan
---

JB4 assembly: both sides reduce to P(a^2∘(b∘a)) up to O(sqrt eta); the exact ambient Jordan identity
cancels the leading term. The sqrt(eta) is intrinsic (one-hole), not slack. Report `prop:bridge-jordan`.
