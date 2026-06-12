VERDICT: REDUCTION REFUTED-AT-A3.

I wrote the long-form audit to [proof.md](/tmp/codex-sigma-wall/w38_sb/proof.md). The fatal issue is that `(R)` is correct, but `(SIG)` is false at `theta=1/2`: when `lambda < 0`, `E = sigma + 2|lambda| > sigma`.

Exact selected-chart witness from perturbed staircase `m=5, eps=1/1000`:

```text
lambda = -1/999
SF_s   = 5003/2000000
S+_s   = 5001/2000000
SF-S+  = 1/1000000
```

So proving the stated `(SB)` would not imply the SF/registry contract as written. A corrected target needs the missing negative-deficit term, e.g. `S+ + 2 sum beta_+ (-lambda)_+`.

Saved artifacts:

- [verify_reduction.py](/tmp/codex-sigma-wall/w38_sb/verify_reduction.py), [verify_reduction.out](/tmp/codex-sigma-wall/w38_sb/verify_reduction.out)
- [single_swap_check.py](/tmp/codex-sigma-wall/w38_sb/single_swap_check.py), [single_swap_check.out](/tmp/codex-sigma-wall/w38_sb/single_swap_check.out)
- [progress.md](/tmp/codex-sigma-wall/w38_sb/progress.md)

Verification: both local scripts compile with `python3 -m py_compile`; `answer.md` is absent.