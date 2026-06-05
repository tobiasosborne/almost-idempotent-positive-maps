---
id: lem-bridge-onehole
kind: lemma
contract: For a range-product hole h=h_{r,s}=r∘s-P(r∘s) and t,u in A, the one-hole insertion contexts ||P((h∘t)∘u)|| <= C sqrt(eta)||r||||s||||t||||u|| (5.1) and ||P(h∘(t∘u))|| <= C sqrt(eta)||r||||s||||t||||u|| (5.2).
defs: def-square-hole; def-near-fixed-algebra
deps: lem-first-insertion; lem-bridge-polar
status: proved
af: none
provenance: theorem-B-algebraic-bridge.md:453-487; report lem:bridge-onehole
owner: B
workspace: proofs/lem-bridge-onehole
---

The two one-hole contexts (5.1),(5.2) of the Jordan-identity expansion are each O(sqrt eta), obtained
by splitting on range/kernel and applying (HZ), (HH), and first-insertion (FI). Uses
[[def-square-hole]], [[def-near-fixed-algebra]]. Report `lem:bridge-onehole`; theory theory/bridge/
(theorem-B-algebraic-bridge.md Lemma 5).
