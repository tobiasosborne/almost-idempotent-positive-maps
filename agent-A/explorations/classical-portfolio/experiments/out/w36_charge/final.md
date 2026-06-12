VERDICT: PARTIAL.

I did not prove (CHARGE), and I did not find a selected-chart counterexample to the dimension-free contract. Long form is in [proof.md](/tmp/codex-sigma-wall/w36_charge/proof.md:1). No `answer.md` was created.

Key outcome: all mandatory exact checks pass, but the no-center path-tie variant shows the selected-chart constant cannot realistically be `C=1`: exact ratios are `59999/40000` at `k=6` and `149999/90000` at `k=8`, with the float scan increasing toward `2`.

Saved artifacts include:

- [progress.md](/tmp/codex-sigma-wall/w36_charge/progress.md:1)
- [stress_checks.py](/tmp/codex-sigma-wall/w36_charge/stress_checks.py:1) and `stress_checks_summary.txt`
- [path_tie_exact.py](/tmp/codex-sigma-wall/w36_charge/path_tie_exact.py:1) and `path_tie_exact_summary.txt`
- [selected_family_scan.py](/tmp/codex-sigma-wall/w36_charge/selected_family_scan.py:1) and `selected_family_scan_summary.txt`

The precise died-at step is the multi-swap shear-decay / dual-flow lemma displayed in `proof.md` as `(DECAY)` / `(TREE)`.