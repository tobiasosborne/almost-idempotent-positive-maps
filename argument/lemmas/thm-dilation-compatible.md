---
id: thm-dilation-compatible
kind: theorem
contract: If there are a finite-dimensional Hilbert space K, a unital order-isometric Jordan embedding j:B(H)_sa->B(K)_sa, and a unital positive C:B(K)_sa->B(H)_sa with Phi=Cj whose lift F=jC extends to a UCP map B(K)->B(K) with ||F^2-F||_cb <= eta, then with P=theta(2Phi-1), A=Im P, a•b=P(a∘b), the algebra A is an O(eta)-eps-JB order-unit algebra (by reduction to Kitaev's CP theorem for F).
defs: def-spectral-idempotent; def-near-fixed-algebra; def-eps-jb-algebra
deps: lem-cstar-sa-to-epsjb; lem-intertwine-spectral-idempotent; lem-idempotence-inheritance; lem-P-properties
status: proved
af: validated
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
[[lem-P-properties]]. The dilation space is a **full matrix algebra B(K)** (K finite-dimensional) — the
natural Stinespring dilation target — so [[lem-cstar-sa-to-epsjb]] (UCP on B(H), with H:=K) applies
**verbatim** to F on B(K). (The general finite-dim C*-algebra D=⊕_j B(L_j) case is deferred, `aipm-q8i`:
⊕B(L_j) is a *proper* subalgebra of B(K), and Kitaev's two-hole estimate uses a Stinespring stack
instantiated only over full B(H_n), so general D needs a bridge lemma re-deriving that stack at
finite-dim-C* generality.) (def-decomposable-map
was a non-load-bearing import, removed; the registry dep on thm-bridge was structural-not-logical, replaced
by the actual imports.) Report `thm:dilation-compatible`; source report/sections/10-exponent.tex.
