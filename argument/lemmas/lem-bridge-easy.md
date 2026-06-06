---
id: lem-bridge-easy
kind: lemma
contract: The projected product a•b=P(a∘b) on A satisfies the easy axioms with O(eta): unit 1•a=a and commutativity a•b=b•a are exact, ||a•b|| <= (1+C eta)||a||||b||, a•a >= -C eta ||a||^2 1, and ||a•a|| >= (1-C eta)||a||^2.
defs: def-eps-jb-algebra; def-jordan-product; def-near-fixed-algebra
deps: lem-P-properties; lem-square-hole-almost-positive; prop-kadison-js
status: proved
af: validated
provenance: theorem-B-algebraic-bridge.md:188-218; report lem:bridge-easy
owner: B
workspace: proofs/lem-bridge-easy
---

All epsilon-JB axioms except the Jordan identity, with the unit law and commutativity exact and the
remaining bounds O(eta); the norm lower bound uses Jordan-Schwarz on Phi. Uses
[[def-eps-jb-algebra]], [[def-jordan-product]], [[def-near-fixed-algebra]]. Report `lem:bridge-easy`;
theory theory/bridge/ (theorem-B-algebraic-bridge.md Lemma 1).
