---
id: lem-intertwine-spectral-idempotent
kind: lemma
contract: For elements F, Phi of unital Banach algebras with ||F^2-F|| < 1/4 and ||Phi^2-Phi|| < 1/4, and a bounded unital linear intertwiner j (j(I)=I) with Fj=jPhi, the Kitaev spectral idempotents intertwine: theta(2F-1) j = j theta(2Phi-1).
defs: def-spectral-idempotent
deps:
status: proved
af: validated
provenance: agent-B/notes/decomposable-dilation-compatible-theorem.md (intertwining step); report thm:dilation-compatible
owner: B
workspace: proofs/lem-intertwine-spectral-idempotent
---

The functional-calculus intertwining behind the dilation reduction: a bounded unital intertwiner of two
almost-idempotent elements also intertwines their spectral idempotents `theta(2X-1)`
([[def-spectral-idempotent]]). Proof skeleton: `Fj=jPhi` gives `S_F j = j S_Phi` (`S_X=2X-I`, using
`j(I)=I`), hence `S_F^n j = j S_Phi^n` by induction; `theta(2X-1)` is a *single fixed* power series `g`
(binomial `R=(S^2)^{-1/2}`, then `sgn=SR`), so each partial sum intertwines and the limit passes through the
bounded `j` (operator-norm convergence from Kitaev's Taylor-calculus bound,
`refs/kitaev-2405.02434/approximate_algebras.tex:503-516`; `sgn`/`prop_P` at `:518-533`). The series converge
under the `<1/4` threshold in each algebra's own norm (op-norm on `End(B(H)_sa)`, cb-norm on the lift); the
intertwining identity is stated in op-norm, so the cb→op passage is harmless (`||.||_op <= ||.||_cb`). Used
by `thm-dilation-compatible` to get `theta(2F-1) j = j P`.

**Note (proof scope, 2026-06-06).** The contract advertises a *unital* intertwiner `j(I)=I`, which the
consumer (`thm-dilation-compatible`) does provide; but the af proof shows unitality is **not load-bearing**.
Nodes 1.1–1.6 use only that `I_A, I_B` are multiplicative units acting as the identity operator
(`I_A·j(b)=j(b)`, `j(I_B·b)=j(b)`) — i.e. `I_A j = j = j I_B` — never `j(I_B)=I_A`. The proof therefore
establishes the stronger `j(I)=I`-free intertwining; `unital j` is kept in the contract because the consumer
supplies it, not because the argument needs it.
