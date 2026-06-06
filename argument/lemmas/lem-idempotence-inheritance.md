---
id: lem-idempotence-inheritance
kind: lemma
contract: For a unital order-isometric Jordan embedding j (so ||jM||=||M|| and ||j||_op=1) and a unital positive C, with Phi=Cj and F=jC, the operator-norm idempotency defects satisfy ||Phi^2-Phi|| <= ||F^2-F||; hence ||F^2-F|| <= eta < 1/4 forces ||Phi^2-Phi|| <= eta < 1/4, so P=theta(2Phi-1) is well-defined.
defs: def-positive-unital-map; def-spectral-idempotent
deps:
status: proved
af: validated
provenance: docs/LEARNINGS.md (R7); algebra Phi^2-Phi=(Phi-I)Cj, F^2-F=j(Phi-I)C with j order-isometric; report thm:dilation-compatible
owner: A
workspace: proofs/lem-idempotence-inheritance
---

The almost-idempotence of `Phi=Cj` is **inherited** from that of the UCP lift `F=jC`, with the *same*
constant — closing the gap a fresh verifier mistakenly flagged as a "false premise" (the counterexample
cannot exist under the order-isometric hypothesis; see `docs/LEARNINGS.md` R7). Proof: `Phi^2-Phi=(Phi-I)Cj`
and `F^2-F=j(Phi-I)C` (pure algebra from `Phi=Cj`, `F=jC`); since `j` is order-isometric (`||jM||=||M||`,
`||j||_op=1`), `||Phi^2-Phi||=||(Phi-I)Cj|| <= ||(Phi-I)C|| = ||j(Phi-I)C|| = ||F^2-F||`. The operator-norm
submultiplicativity leaf is grounded in `refs/kitaev-2405.02434/approximate_algebras.tex` (bounded operators
form a Banach algebra). Independently confirmed by a 7,008,000-sample numerical sweep (zero violations).
Guarantees `P=theta(2Phi-1)` ([[def-spectral-idempotent]]) is well-defined under the dilation hypothesis.
Used by `thm-dilation-compatible`.
