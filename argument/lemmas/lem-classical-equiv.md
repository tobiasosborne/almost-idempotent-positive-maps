---
id: lem-classical-equiv
kind: lemma
contract: The signed-idempotent and stochastic-idempotent formulations of classical stability are equivalent up to universal constants: Q row-stochastic with ||Q^2-Q|| <= eta gives P=theta(2Q-1) signed affine retraction with ||P-Q|| <= C eta and neg mass delta <= C eta, and conversely row-normalising p_i^+ gives Q with ||P-Q|| <= 2 delta, ||Q^2-Q|| <= 6 delta+4 delta^2.
defs: def-stochastic
deps:
status: proved
af: none
provenance: subagent-classical-sqrt-stability-proof.md; classical-affine-face-lemmas.md (Lemma 3); report lem:classical-equiv
owner: B
workspace: proofs/lem-classical-equiv
---

The two formulations imply one another with universal constants, so op-classical may be attacked through the
exactly-idempotent signed form P^2=P with non-positivity quarantined in delta. Uses [[def-stochastic]].
Report `lem:classical-equiv` (status proved). Theory: agent-B/notes/subagent-classical-sqrt-stability-proof.md,
classical-affine-face-lemmas.md (Lemma 3).
