Done. Long-form verdict-first audit is in [audit.md](/tmp/codex-sigma-wall/w36_audit/audit.md:1). Progress log is in [progress.md](/tmp/codex-sigma-wall/w36_audit/progress.md:1). No `answer.md` was created.

Key outcome: B6 is a real hit. I found an exact epsilon-perturbed staircase at `delta=1/2` where exact `theta=1` max-volume selection has a unique bad chart with ratio `m - 3epsilon`; the low-SF charts re-enter exactly when `theta <= 1 - epsilon`. So the exact-tie “ratio 1” collapse is fragile, and theta slack is not optional at the endpoint.

Verification run:
`stress_checks.py` rerun in a writable copy, plus an independent actual-row Gram determinant verifier in [independent_minmax_check.py](/tmp/codex-sigma-wall/w36_audit/independent_minmax_check.py:1). Outputs are saved in [independent_minmax_check.out](/tmp/codex-sigma-wall/w36_audit/independent_minmax_check.out:1) and `w35_charge/stress_checks_summary.txt`.