# w17_cert_audit — ANTECEDENT INSTANCES CERTIFIED EXACT (codex independent verifier, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w17_cert_audit/brief.md. Artifacts: experiments/out/w17_cert_audit/.

VERDICT: CERTIFIED EXACT for both MAIN and ROBUST.

MAIN exact rational instance: `delta = 0.2329335240003862`, hidden `v=5`, `H/tau = 0.10019261003238415`, `sigma_tilde/tau > 1` certified via `P_55 = 0.7274084488643412 > tau`, hiddenness dual objective `t*/kappa <= 0.999877369296419`.

ROBUST exact rational instance: `delta = 0.23459249106770674`, hidden `v=5`, `H/tau = 0.1000025471673097`, `sigma_tilde/tau > 1` certified via `P_55 = 0.7325554135477605 > tau`, hiddenness dual objective `t*/kappa <= 0.9977747374212589`.

I saved the verifier and artifacts here:

- [independent_verifier.py](/tmp/codex-sigma-wall/w17_cert_audit/independent_verifier.py)
- [verification_report.json](/tmp/codex-sigma-wall/w17_cert_audit/verification_report.json)
- [main_rational_instance.json](/tmp/codex-sigma-wall/w17_cert_audit/main_rational_instance.json)
- [robust_rational_instance.json](/tmp/codex-sigma-wall/w17_cert_audit/robust_rational_instance.json)
- [pareto_sample_check.json](/tmp/codex-sigma-wall/w17_cert_audit/pareto_sample_check.json)
- [audit_verdict.md](/tmp/codex-sigma-wall/w17_cert_audit/audit_verdict.md)

Key checks:

- Float recomputation matched the claimant’s reported `delta`, `W`, `H/tau`, `sigma_tilde/tau`, and hiddenness margins.
- Exact rational hardening uses `B=[I;X]`, `L=[I-QX,Q]`, so `LB=I`, `P=BL`, `P^2=P`, and `P1=1` hold exactly.
- Exact certificates verify `W={0,1,2,3,4}`, hidden vertices `{5,6,7}`, and nonvertices `{8,9}`.
- MAIN top hiddenness LP active sets: far `[0,1,3,4]`; active upper `[0,4]`, lower `[2,5]`, far `[1,3]`.
- ROBUST has the same active sets.
- MAIN quotient component `[1,2,3,5,6,7]`, `L=2`, `Pi/tau=0.00024879427009641934`.
- ROBUST quotient `Pi/tau=0.00025236363737045933`.

Sensitivity:

- MAIN `kappa - t* = 1.4796373616676739e-5`; local entrywise flip upper bound about `6.55e-6`.
- ROBUST `kappa - t* = 2.69449996533222e-4`; local entrywise flip upper bound about `8.49e-5`.
- Exact rational entry drifts are `1.25e-11` and `1.95e-11`, so the decision is not float-only.

Context:

- `delta*=(2-sqrt(3))^2 = 0.07179676972449088`; these instances are well above the corner scale, so the small-delta regime is untouched.
- Both satisfy `H <= 2*delta`.
- I rechecked nine saved candidate/certificate pairs; no systematic reporting bias showed up.

This falsifies the campaign record item saying no verified instance has `sigma_tilde > tau` together with `H > 0.1*tau`. Via the stated cloning construction, the raw-index floor is refuted for any `delta0 >= 0.2329335240003862` in particular at `delta0 >= 0.233`.

Calibrated `P(exact antecedent-realizing instance exists at delta <= 0.25)`: `> 0.999999`, with residual risk only from verifier implementation or artifact-handling error.