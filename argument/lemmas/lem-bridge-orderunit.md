---
id: lem-bridge-orderunit
kind: lemma
contract: The near-fixed algebra A=Im P, with unit 1 and inherited cone A_+ = A cap B(H)_+, is an order-unit space, and its order-unit norm ||a||_ou = inf{t>0: -t1<=a<=t1} coincides exactly with the operator norm on A.
defs: def-near-fixed-algebra; def-order-unit-space; def-spectral-idempotent
deps: lem-P-properties
status: proved
af: none
provenance: theorem-B-algebraic-bridge.md:121-152; report lem:bridge-orderunit
owner: B
workspace: proofs/lem-bridge-orderunit
---

The order-unit part of the structure on A is exact (no approximate norm/order is introduced): since
P(1)=1 the range A=Im P contains 1, and with the inherited Archimedean cone (V_+ closed) it is an
order-unit space whose order-unit norm is the ambient operator norm. Uses [[def-near-fixed-algebra]],
[[def-order-unit-space]], [[def-spectral-idempotent]]. Report `lem:bridge-orderunit`; theory
theory/bridge/ (theorem-B-algebraic-bridge.md Lemma 0).
