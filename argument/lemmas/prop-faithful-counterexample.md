---
id: prop-faithful-counterexample
kind: obstruction
contract: The family T_a=(1-a)P_0+aJ (0<a<1/2, J=(1/3)ones) gives unital positive Phi_a, each with a FAITHFUL invariant state pi_a and eta_a=||T_a^2-T_a||=(10/9)a(1-a)->0, yet the ambient hole ||(Id-P_a)(r^2)|| -> 2/9 stays bounded away from 0 (floor lambda=pi_{a,3}=a/3=Theta(eta_a), eta_a/lambda->10/3=Theta(1)): a faithful invariant state ALONE does not give an O(eta) defect, so the lambda-dependence is necessary.
defs: def-positive-unital-map
deps: thm-faithful-approx
status: proved
af: none
provenance: report/sections/06b-faithful-invariant.tex prop:faithful-counterexample (L152-177); B-FIT (T_a family); A-FIT §3, verified in agent-A/experiments/faithful-invariant-transfer/
owner: A
workspace: proofs/prop-faithful-counterexample
---

Sharpness of thm-faithful-approx: a single explicit [[def-positive-unital-map]] family, faithful for every
a>0 with eta_a->0, whose ambient-product hole does not vanish because its conditioning lambda degrades in
exact step with eta. So the bound C(eta/lambda) is correctly vacuous, and the bare hypothesis "admits a
faithful invariant state" does NOT transfer; the projected Effros--Stoermer product stays necessary.
Report `prop:faithful-counterexample`; source report/sections/06b-faithful-invariant.tex; experiment
agent-A/experiments/faithful-invariant-transfer/REPORT.md §3 (projector matches Riesz to machine precision).
