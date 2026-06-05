---
id: prop-faithful-exact
kind: proposition
contract: If a unital positive idempotent P on B(H)_sa admits a faithful invariant state (omega∘P=omega), then Im P is closed under the AMBIENT Jordan product: P(a∘b)=a∘b for all a,b in Im P, so • and ∘ agree on Im P and Im P is a unital Jordan subalgebra of (B(H)_sa,∘).
defs: def-multiplicative-domain; def-positive-unital-map; def-near-positive-projection
deps: thm-vlw-minimal-jstar
status: cited
af: none
provenance: report/sections/06b-faithful-invariant.tex prop:faithful-exact (L32-51); A-FIT §1; VLW prop:fixpoint (600-610)
owner: A
workspace: proofs/prop-faithful-exact
---

Faithfulness collapses the projected product [[def-near-positive-projection]] onto the ambient one: via
Kadison (q_a=P(a^2)-a^2>=0) plus faithfulness on the cone (omega(q_a)=0 => q_a=0), Im P of a
[[def-positive-unital-map]] idempotent lands in the [[def-multiplicative-domain]] of the ambient product.
This is the multiplicative-domain mechanism of the van Luijk--Wilming faithful fixed-point theory.
Report `prop:faithful-exact`; source report/sections/06b-faithful-invariant.tex.
