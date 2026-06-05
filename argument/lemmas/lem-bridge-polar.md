---
id: lem-bridge-polar
kind: lemma
contract: Polarised holes q_{r,s}=P(r∘s)-r∘s obey, in the state seminorm ||x||_omega^2=omega(x^2), ||q_{r,s}||_omega <= C sqrt(eta)||r||||s|| (4.1) and ||q_{r,s}|| <= C||r||||s||; hence ||P(q_{r,s}∘q_{u,v})|| <= C eta ||r||||s||||u||||v|| (HH) and ||P(q_{r,s}∘z)|| <= C sqrt(eta)||r||||s||||z|| for z in V (HZ).
defs: def-square-hole; def-near-fixed-algebra
deps: lem-first-insertion; lem-square-hole-almost-positive
status: proved
af: none
provenance: theorem-B-algebraic-bridge.md:374-451; report lem:bridge-polar
owner: B
workspace: proofs/lem-bridge-polar
---

Polarising the square-hole estimate gives the seminorm bound (4.1); Cauchy-Schwarz for rho∘Phi then
yields the two-hole (HH) bound O(eta) and the one-hole (HZ) bound O(sqrt eta), the replacement of Phi
by P being absorbed into C. Uses [[def-square-hole]], [[def-near-fixed-algebra]]. Report
`lem:bridge-polar`; theory theory/bridge/ (theorem-B-algebraic-bridge.md Lemma 4).
