---
id: lem-leakage
kind: lemma
contract: Affine-face leakage: for row-stochastic Q with ||Q^2-Q|| <= eta and affine h:Delta_n->[0,1], m=max_j h(q_j), d_i=m-h(q_i), one has q_i({j:h(q_j)<=m-gamma}) <= (d_i+eta)/gamma; so a maximiser row leaks at most sqrt(eta) of its mass below level m-sqrt(eta) and no O(eta) closure is possible.
defs: def-stochastic; def-exposed
deps:
status: proved
af: none
provenance: classical-affine-face-lemmas.md (Lemma 1, Cor 2); report lem:leakage
owner: B
workspace: proofs/lem-leakage
---

Right-fixity forces the row mass to stay within sqrt(eta) of any maximised affine face: exposed faces are
almost closed at the square-root scale. Uses [[def-stochastic]], [[def-exposed]]. Report `lem:leakage`
(status proved). Theory: agent-B/notes/classical-affine-face-lemmas.md (Lemma 1, Corollary 2).
