---
id: lem-cstar-sa-to-epsjb
kind: lemma
contract: If F is a unital eta-idempotent UCP map on B(H) (||F^2-F||_cb <= eta < 1/4), Ftilde=theta(2F-1), and B=Im Ftilde carries the Choi-Effros product X*Y=Ftilde(XY) (Kitaev's extended O(eta)-C*-algebra), then B_sa with the symmetrized product X∘Y=(1/2)(X*Y+Y*X) is an O(eta)-eps-JB order-unit algebra with universal dimension-free constants.
defs: def-eps-cstar-algebra; def-eps-jb-algebra; def-self-adjoint-part; def-jordan-product
deps:
status: proved
af: validated
provenance: agent-B/notes/decomposable-dilation-compatible-theorem.md:67-82; report sec:exponent (thm:dilation-compatible)
owner: B
workspace: proofs/lem-cstar-sa-to-epsjb
---

The C\*→JB symmetrisation — **the heart of the dilation theorem's O(η) strength**. Given Kitaev's extended
`O(eta)`-C\*-algebra `B=Im Ftilde` ([[def-eps-cstar-algebra]], `th_almost_idemp`,
`refs/kitaev-2405.02434/approximate_algebras.tex:2192-2194`), its self-adjoint part under the symmetrised
product ([[def-jordan-product]], [[def-self-adjoint-part]]) satisfies the four
[[def-eps-jb-algebra]] axioms: **JB1/JB2** from ax\_prodnorm/ax\_C\* (`:407-440`); **JB4** (the Jordan
identity at `O(eta)`) from Kitaev's **`O(eta)`-associativity** of `*` (`:2228-2231`) plus the *exact* ambient
Jordan identity (HOS eq. 2.18, `refs/hos/joa-m.md:825`) — this is the route that beats the bridge's `O(√η)`;
**JB3** (positivity of squares `X∘X >= -C eta ||X||^2 1`) from `Ftilde` being **UCP** with `X^2>=0`
(`:2233-2235`) — *not* derivable from the abstract ε-C\* axioms (ax\_C\* is only a norm bound), which is why
the contract is the concrete `B=Im Ftilde` realisation. The order-unit norm equals the operator norm on
`B_sa ⊆ B(H)_sa`. Used by `thm-dilation-compatible`.
