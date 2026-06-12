VERDICT: MIXED / max-volume tie ambiguity.

The half-delta staircase does survive recomputation in the best-tie sense: at `delta=1/2`, the intended identity chart is still max-volume and gives `SF/delta = m` for `m=2,3,5,8`. But it is tied with other max-volume charts where row `0` drops out and the ratio collapses to `1`.

Required exact chart audit:

```text
m=2: best=2, worst=1, ties=7
m=3: best=3, worst=1, ties=9
m=5: best=5, worst=1, ties=13
m=8: best=8, worst=1, ties=19
```

So SF is false at `delta_0=1/2` if the statement must hold for every/arbitrary max-volume tie choice. If the statement allows choosing a favorable tied chart, this family does not refute it.

Long-form writeup is in [proof.md](/tmp/codex-sigma-wall/w34_halfcex/proof.md). Code and outputs are saved, including [w34_halfcex_audit.py](/tmp/codex-sigma-wall/w34_halfcex/w34_halfcex_audit.py), `chart_recompute_audit.json`, `threshold_audit.json`, and `final_checks.txt`. No `answer.md` was created. Gurobi was not used.

Threshold sweep result: best-tie data supports `delta_* = 1/2` as a supremum, not included; conjectured envelope near the threshold is `C(delta) ~ 1/(1-2 delta)`. For cap `<= 0.3`, this family stayed bounded in the `~1..2` range.