# w18_similarity — the cohomological route: BLOCKED at first-order diagonal displacement (codex, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w18_similarity/brief.md. Artifacts: experiments/out/w18_similarity/ (Newton traces).
# NOTE: the worker's detailed lemma write-up was lost to final-message-only capture; the diagnosis below + traces are the record.

VERDICT: ROUTE BLOCKED in the naive Newton/projection form.

I saved the full write-up at [answer.md](/tmp/codex-sigma-wall/w18_similarity/answer.md), with the corner-splitting lemma, similarity lemma, obstruction, numerical tables, unverified leads, and calibrated probabilities.

Artifacts saved:

- [similarity_newton.py](/tmp/codex-sigma-wall/w18_similarity/similarity_newton.py)
- [out_1000/summary.json](/tmp/codex-sigma-wall/w18_similarity/out_1000/summary.json)
- `out_1000/*.csv` traces and final matrices
- [progress.md](/tmp/codex-sigma-wall/w18_similarity/progress.md)

Key result: the exact Peirce retraction works algebraically, but the positivity projection creates an order-\(\delta\) \(E_{11}\oplus E_{00}\) displacement. The retraction’s diagonal correction is only quadratic in the off-diagonal tangent blocks, so it does not remove that first-order diagonal error. Numerically, the certified w16 instance can reduce negativity only by drifting order-one along the idempotent variety, not by producing an \(O(\delta)\)-close H-M cleanup.

Calibration recorded:

\[
P(\text{proved contraction lemma in one wave}) \approx 0.18
\]

\[
P(\text{route eventually proves the linear law}) \approx 0.32
\]