---
id: ex-no-faithful
kind: obstruction
contract: The R^3 row-stochastic idempotent P_0 = [[1,0,0],[0,1,0],[1/3,2/3,0]] is an exact unital positive idempotent whose invariant states (t,1-t,0) are all non-faithful (state 3 transient); for a=(-1,1,1/3) in Im P_0 the ambient square-hole is q_a=(0,0,8/9) with ||q_a||=8/9=Theta(1), so faithfulness is not free.
defs: def-positive-unital-map; def-near-positive-projection
deps:
status: proved
af: none
provenance: report/sections/06b-faithful-invariant.tex ex:no-faithful (L59-73); A-FIT §1 (8/9 witness), verified in agent-A/experiments/faithful-invariant-transfer/
owner: A
workspace: proofs/ex-no-faithful
---

Faithfulness in prop-faithful-exact is essential, not cosmetic: an exact [[def-positive-unital-map]]
idempotent [[def-near-positive-projection]] with only NON-faithful invariant states need not have a
Jordan-subalgebra range, exhibiting an ambient-product hole of size Theta(1) (8/9). This is why
Effros--Stoermer must keep the projected product •. Report `ex:no-faithful`; source
report/sections/06b-faithful-invariant.tex; experiment agent-A/experiments/faithful-invariant-transfer/REPORT.md §1.
