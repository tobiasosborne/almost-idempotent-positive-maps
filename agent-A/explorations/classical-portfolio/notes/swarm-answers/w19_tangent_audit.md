# w19_tangent_audit — LEMMA HOLDS WITH REPAIR (codex hostile audit, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w19_tangent_audit/brief.md. Artifacts: experiments/out/w19_tangent_audit/ (incl. audit_report.md).

VERDICT: LEMMA HOLDS WITH REPAIR.

The inequality survives: `dot-H+ <= 2 dot-delta` for fixed H-M base points and exact `C^1` arcs. The repair is that sharpness should be stated only for the frozen recurrent-hull derivative, not for the actual visible-set height. The semicontinuity paragraph also needs an explicit two-scale visibility lemma; the pointwise Dini statement is fine, but it does not give a uniform local radius over tiny recurrent masses.

Saved report: [audit_report.md](/tmp/codex-sigma-wall/w19_tangent_audit/audit_report.md)

Key independent results:
- Large LP sweep: `209` strata, `zero_budget_max = 0.0`, `budget1_max = 2.000000000000002`.
- Exact arc spot check: worst LP direction stayed below `2 dot_delta`; idempotence residual around `1e-16`.
- `n=3` endpoint direction has `dot_delta=1`, frozen `D=2`, but actual `H/t=0`, so actual sharpness is not confirmed.
- Left-cone refutation family does not attack this lemma: at its H-M anchor, `dot_delta=1`, frozen `D=0`.
- Zero-budget exact-arc probe found finite-scale tiny-mass stress (`H/t≈2` above a `1e-6` active-entry scale), but tail max below that scale was `0.0`, so no Dini failure.

Artifacts:
- [tangent_audit.py](/tmp/codex-sigma-wall/w19_tangent_audit/tangent_audit.py)
- [independent_decider_summary_large.txt](/tmp/codex-sigma-wall/w19_tangent_audit/independent_decider_summary_large.txt)
- [targeted_checks_summary.txt](/tmp/codex-sigma-wall/w19_tangent_audit/targeted_checks_summary.txt)
- [semicontinuity_probe_summary.txt](/tmp/codex-sigma-wall/w19_tangent_audit/semicontinuity_probe_summary.txt)
- [progress.md](/tmp/codex-sigma-wall/w19_tangent_audit/progress.md)

`python3 -m py_compile tangent_audit.py targeted_checks.py semicontinuity_probe.py` passed. P(repaired verdict survives further audit): `0.82`.