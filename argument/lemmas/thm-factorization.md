---
id: thm-factorization
kind: theorem
contract: Conditional on op-npps, an almost-idempotent unital positive Phi (||Phi^2-Phi||<=eta<=eta_0) factorizes through a finite-dimensional special JB-algebra J by unital positive maps Delta=inclusion, Upsilon=E with Upsilon Delta=id_J, ||Delta Upsilon - Phi||<=C sqrt(eta), and Upsilon(Delta(x)∘Delta(y))=x•y.
defs: def-near-positive-projection; def-jc-algebra; def-positive-unital-map
deps: op-npps; thm-effros-stormer; thm-bridge
status: proved
af: none
provenance: TH-C (theorem-C-conditional-factorization.md; full proof, conditional on op-npps); report thm:factorization
owner: B
workspace: proofs/thm-factorization
---

Theorem C: granting op-npps, get a unital positive idempotent E with ||E-P||<=C sqrt(eta); its range
J=E(B(H)_sa) is a special [[def-jc-algebra]] (Effros-Stormer, thm-effros-stormer) under x•y=E(x∘y), and
Delta,Upsilon are [[def-positive-unital-map]]s. The implication is proved; only op-npps (the
[[def-near-positive-projection]] stability) is open. Report `thm:factorization`; theory:
agent-B/theory/theorem-C-conditional-factorization.md.
