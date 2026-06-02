# Theory overview — Kitaev's theorem for positive maps / Jordan algebras (Agent A)

Goal: generalize Kitaev (arXiv:2405.02434) from UCP maps / C\*-algebras to **unital positive maps / JB-algebras**. Setting: van Luijk–Wilming (arXiv:2604.08380).

## The two theorems

**Theorem 1 (abstract structure).** ∃ universal `ε₀,C>0` (dimension-free) s.t. every finite-dim **ε-JB-algebra** (`ε<ε₀`) is `Cε`-Jordan-isomorphic to a genuine finite-dim JB-algebra.

**Theorem 2 (channel factorization).** Φ:B(H)→B(H) unital positive \*-preserving, dim H<∞, `‖Φ²−Φ‖≤η`. Then ∃ a finite-dim **special** JB-algebra (JC-algebra) B and **unital positive** maps Δ:B→B(H)_sa, Υ:B(H)_sa→B with `‖ΔΥ−Φ‖≤O(√η)`, `‖ΥΔ−1_B‖≤O(√η)`. [Exponent α=1/2 unconditional; α=1 only under a decomposable+dilation hypothesis. Exact UP factor maps require near-positive projection stability (generic O(ε) positivity-rounding is FALSE — spin-factor counterexample, B). Reversibility/decomposability of B are NOT automatic.]

## ε-JB-algebra (order-unit form) — working definition

Finite-dim real order-unit space `(A,1,≤)`, order-unit norm `‖·‖`, with commutative bilinear `∘` (commutativity & unit `1∘a=a` EXACT) s.t.
- (JB1) `‖a∘b‖≤(1+ε)‖a‖‖b‖`
- (JB2) `‖a∘a‖≥(1−ε)‖a‖²`
- (JB3) `a∘a ≥ −ε‖a‖²·1`  (approx. positivity of squares)
- (JB4) `‖((a∘a)∘b)∘a − (a∘a)∘(b∘a)‖ ≤ ε‖a‖³‖b‖`  (approx. Jordan identity)

Why order-unit (vs Kitaev's fully-approximate normed structure): when A=Im(P)⊆B(H)_sa for P=θ(2Φ−1), the order-unit structure (order + norm) is inherited **exactly**; only `∘=P(·∘·)` is approximate. This is strictly cleaner than the ε-C\* setting.

## Proof map (Agent A pieces in bold)

| Kitaev (assoc/C\*) | Jordan analogue | status |
|---|---|---|
| approx unitary group (impl. fn thm) | approx automorphism orbit / Jordan symmetries | TODO |
| **nontrivial approx projection (Lefschetz–Hopf, H-space)** | **nontrivial approx Jordan idempotent** (Task 4) | started — assoc-free core ports |
| subspaces 𝒮_{P,Q}, Hilbert structure | **approx Peirce decomposition** A₁⊕A_{1/2}⊕A₀ (Task 5) | TODO |
| matrix units E_jk via Ha operator | **approx Jacobson coordinatization** (rank≥3); spin (rank2); H_3(𝕆) (rank3) | TODO |
| **error reduction `lem_approx` (diagonal D=∫U†⊗U, kill 2-cocycle)** | **Jordan error reduction via Aut(ℬ)-averaging + H²=0** (Task 3, THE crux) | in progress |
| merge/extend, assemble | merge/extend Euclidean Jordan ideals | TODO |
| (Layer 2) `th_almost_idemp`: Φ̃(XY) is ε-C\* | (Layer 2) P(a∘b) is ε-JB (ε=O(√η)) | **DONE** (B's proof, A verified; `agent-B/theory/theorem-B-algebraic-bridge.md`) |
| (Layer 2) UCP rounding via 1-design | UP rounding via Jordan-frame/Aut averaging | TODO (Task 6) |

## Key inputs from literature (see ../refs/lit/, ../notes/ingestion-results-2026-06-01.json)
- Effros–Størmer 1979: positive unital projection P ⇒ Im(P) reversible JC-algebra under P(a∘b); always special (H_3(𝕆) excluded by concreteness).
- Jordan–Schwarz (Størmer): `{Ta*,Ta}≤T{a*,a}`; MD(idempotent UP)=Fix=Range.
- H¹=H²=0 for f.d. semisimple Jordan algebras (Jacobson; Penico). Wedderburn principal thm. Rigidity.
- Aut(Euclidean Jordan algebra) compact ⊂ O(V) ⇒ Haar averaging. Peirce, frames, spectral thm (Faraut–Korányi).
- GAP: no quantitative/dimension-free "approximately-JB ⇒ JB" in literature. We prove it.

## The Layer-2 crux, reduced (Agent A contribution)
Approx. Jordan identity for `a•b=P(a∘b)` ⟸ single estimate
  (★) `‖P(P(x)∘b) − P(x∘b)‖ ≤ O(η)‖x‖‖b‖`, b∈Im(P),
because the ambient Jordan identity in B(H)_sa is EXACT (peel inner P's, surviving args coincide ⇒ P(0)=0). (★) is the analogue of Kitaev's Phi_assoc1/2; needs a CP-free GNS/variance + Jordan–Schwarz proof. Details: 02-layer2-bridge.md.
