# w17_antecedent — ANTECEDENT REALIZED (first sigma>tau AND H>0.1tau instance) [pending w17_cert_audit — hiddenness margin 1.2e-4]
# Brief: /tmp/codex-sigma-wall/w17_antecedent/brief.md. Artifacts: experiments/out/w17_antecedent/.

**VERDICT: ANTECEDENT REALIZED.**

Found a verified `(n,k)=(10,5)` instance with hidden top vertex `v=5`:

- `delta = 0.23293352400054423`
- `tau = 0.4826318721350096`
- `H/tau = 0.10019261004117462`
- `sigma_tilde/tau = 1.546673312722326`
- `delta <= 0.25`, `sigma_tilde > tau`, `H > 0.1*tau`

Primary artifacts:
- [certificate](/tmp/codex-sigma-wall/w17_antecedent/targeted_best/fine_best_certificate.json)
- [factorization](/tmp/codex-sigma-wall/w17_antecedent/targeted_best/fine_best_factorization.json)
- [final frontier summary](/tmp/codex-sigma-wall/w17_antecedent/w17_final_pareto_front.json)
- [verdict note](/tmp/codex-sigma-wall/w17_antecedent/verdict.md)
- [decider script](/tmp/codex-sigma-wall/w17_antecedent/w17_decider.py)

Verification:
- Independent w15 verifier cross-check: `PASS`, same `delta`, `H/tau`, `sigma_tilde/tau`.
- Factor residuals: `R Lambda - I = 2.22e-16`, row sums `1.11e-16`, idempotence `1.11e-16`.
- Hiddenness LP: `t*/kappa = 0.9998773692789819`, so hidden but very near the active wall.
- A companion certificate with more hiddenness slack is saved at [robust_certificate.json](/tmp/codex-sigma-wall/w17_antecedent/targeted_robust/robust_certificate.json): `H/tau = 0.10000254724475997`, `sigma_tilde/tau = 1.5521010289492778`, `t*/kappa = 0.9977747381613477`.

Quotient carrier test:
- Coincident-row classes are all singleton, so quotient carrier equals raw carrier.
- Main quotient component: `[1, 2, 3, 5, 6, 7]`, `L=2`.
- `Pi = 0.00012007604435309809`, `Pi/tau = 0.00024879427009641934`.
- No clone pathology. The quotient path product is extremely thin; this is a genuine test object for the quotient floor, not a proof of it.

Calibrated `P(the antecedent regime is empty) = 0.001`, only for floating-point / interval-certification caution.

Single most informative next experiment: interval/rational certify this active-set point, then continue the exact active equations in `(eps, scale)` to maximize `min(H/tau - 0.1, kappa - t*)` while lowering `delta`.
---
## Appendix: verdict.md (worker long-form, verbatim)

VERDICT: ANTECEDENT REALIZED.

Primary certificate:
- File: /tmp/codex-sigma-wall/w17_antecedent/targeted_best/fine_best_certificate.json
- Factorization: /tmp/codex-sigma-wall/w17_antecedent/targeted_best/fine_best_factorization.json
- n = 10, k = 5, v = 5, W = [0, 1, 2, 3, 4]
- delta = 0.23293352400054423
- tau = 0.4826318721350096
- H/tau = 0.10019261004117462
- sigma_tilde/tau = 1.546673312722326
- sigma_tilde = 0.7464738365004333
- P_vv = 0.7274084488610099
- nu_v = 0.022359756530588203
- factor residuals: R Lambda - I = 2.22e-16, row sums = 1.11e-16, idempotence = 1.11e-16
- independent w15 verifier cross-check: PASS with the same delta, H/tau, sigma_tilde/tau.

Hiddenness:
- rho = 1.9305274885400383
- kappa = 0.1206579680337524
- t* = 0.12064317166013583
- t*/kappa = 0.9998773692789819
- far rows for v: [0, 1, 3, 4]
- active exposedness constraints: h(row 0) <= 1, h(row 2) >= 0, h(row 4) <= 1, t <= h(row 1), t <= h(row 3).

Robustness companion:
- File: /tmp/codex-sigma-wall/w17_antecedent/targeted_robust/robust_certificate.json
- H/tau = 0.10000254724475997
- sigma_tilde/tau = 1.5521010289492778
- t*/kappa = 0.9977747381613477

Quotient carrier:
- All coincident-row classes are singleton, so the quotient carrier equals the raw carrier.
- At t/(kappa Omega) = 0.5, the mass-carrying quotient component is [1, 2, 3, 5, 6, 7].
- For the primary certificate, quotient Pi = 0.00012007604435309809, L = 2, Pi/tau = 0.00024879427009641934.
- This is not a clone artifact. It is a thin quotient-carrier test object; any non-vacuous quotient floor with c of order 1 and C' not large enough to swamp c tau fails on the measured path product, but the constants in the conjecture are unspecified.

Frontier files:
- /tmp/codex-sigma-wall/w17_antecedent/w17_final_pareto_front.json
- /tmp/codex-sigma-wall/w17_antecedent/run2/w17_pareto_front.json
- /tmp/codex-sigma-wall/w17_antecedent/run2/w17_points.json
- /tmp/codex-sigma-wall/w17_antecedent/targeted_best/fine_points.json

Calibration:
- P(the antecedent regime is empty) = 0.001, reserved only for floating-point/interval-certification caution.

Single most informative next experiment:
- Interval/rational certify the active-set continuation point, then continue the exact active-set equations in eps/scale to maximize min(H/tau - 0.1, kappa - t*) and lower delta.
