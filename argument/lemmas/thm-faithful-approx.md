---
id: thm-faithful-approx
kind: theorem
contract: For unital positive Phi with ||Phi^2-Phi|| <= eta <= eta_0, P=theta(2Phi-1), A=Im P, if Phi admits a faithful state omega with ||omega∘Phi-omega|| <= eta and density rho_omega >= lambda 1 (lambda>0), then for all a,b in A the ambient product hole satisfies ||a∘b-P(a∘b)|| = ||h_{a,b}|| <= C (eta/lambda) ||a|| ||b||, with universal dimension-free C.
defs: def-square-hole; def-positive-unital-map
deps: lem-square-hole-almost-positive; lem-P-properties
status: proved
af: validated
provenance: report/sections/06b-faithful-invariant.tex thm:faithful-approx (L83-133); A-FIT §2 (reuses lem:bridge-squarehole); re-derived by B (B's mu = lambda)
owner: A
workspace: proofs/thm-faithful-approx
---

The quantitative version of prop-faithful-exact: the square-hole [[def-square-hole]] estimate
q_a >= -C eta ||a||^2 1 (from lem-square-hole-almost-positive) and the spectral-estimate
delta=||P-Phi||<=C eta (from lem-P-properties, used in the expectation bound) plus approximate
invariance bound omega(q^+), and faithfulness upgrades small expectation to small operator norm at the
cost of 1/lambda (the conditioning of omega). Polarisation gives the bilinear hole bound for the
[[def-positive-unital-map]] Phi. Report `thm:faithful-approx`; source report/sections/06b-faithful-invariant.tex.

af: validated (10 nodes, depth 3; prover prover-faithful, fresh single-node verifiers per node;
node 1.4 had a dependencies challenge — missing direct 1.1 edge — resolved via amend + the transitive
1.1->1.3->1.4 recording, re-verified clean).
