VERDICT: PARTIAL.

I wrote the long-form artifact to [proof.md](/tmp/codex-sigma-wall/w35_charge/proof.md). The proof does not close even for the cleaner cap `delta_0 = 1/4`; the exact wall is the missing dual-flow charge inequality `(CHARGE)` for the min-max max-volume tie chart.

I also saved exact rational stress checks in [stress_checks.py](/tmp/codex-sigma-wall/w35_charge/stress_checks.py), with outputs in [stress_checks_summary.txt](/tmp/codex-sigma-wall/w35_charge/stress_checks_summary.txt) and [stress_checks.json](/tmp/codex-sigma-wall/w35_charge/stress_checks.json). All requested stress families have a favorable max-volume tie chart with max SF ratio `1`.

Verification run:
`python3 -m py_compile stress_checks.py && python3 stress_checks.py`

Progress log is in [progress.md](/tmp/codex-sigma-wall/w35_charge/progress.md). No `answer.md` was created.