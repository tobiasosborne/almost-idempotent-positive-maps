# w15_refuter — NOT-REFUTED; the delta/sigma_tilde^2 < 1 barrier (codex, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w15_refuter/brief.md. Scripts/outputs: experiments/out/w15_refuter/.

VERDICT: NOT-REFUTED.

I built and ran the numerical refuter stack in `/tmp/codex-sigma-wall/w15_refuter`:

- [w15_refuter_search.py](/tmp/codex-sigma-wall/w15_refuter/w15_refuter_search.py)
- [w15_template_audit.py](/tmp/codex-sigma-wall/w15_refuter/w15_template_audit.py)
- [w15_verdict.md](/tmp/codex-sigma-wall/w15_refuter/w15_verdict.md)
- [w15_summary.json](/tmp/codex-sigma-wall/w15_refuter/w15_summary.json)
- [w15_template_audit.json](/tmp/codex-sigma-wall/w15_refuter/w15_template_audit.json)
- [w15_best_regime_matrix.txt](/tmp/codex-sigma-wall/w15_refuter/w15_best_regime_matrix.txt)

Closest in-regime record:

```text
delta = 0.060906010420960506
tau = 0.24679143101201975
H = 0.007114228160152251
H/tau = 0.028826884835421045
sigma_tilde = 0.2001
sigma_tilde/tau = 0.810806109350913
P_vv = 0.2
Pi_C/tau = 5.928525894001441e-06
```

So it has a very thin shallow SCC, but misses the load-bearing gate: `sigma_tilde < tau`, and height is tiny.

Audit summary:

```text
LP-financed s5/cycles: 272 verified in regime, 0 branch hits
positive diagonal/self-mass: 45 verified in regime, 0 branch hits
stochastic conjugations: 3 verified in regime, 0 branch hits
```

Main quantified obstruction: the best self-mass attempt got

```text
delta / sigma_tilde^2 = 1.5211287514903344
```

so it still fails the required `sigma_tilde > sqrt(delta)` inequality.

Updated calibration:

```text
P(path-product floor / thin-chain exclusion true in small-delta regime) = 0.84
```

Most promising remaining degree of freedom: end-to-end nonlinear optimization over `(L, B)` with W-aware loss, instead of fixing `B` and LP-completing `Q`. The concrete barrier to beat is now `delta / sigma_tilde^2 < 1` while keeping the top vertex hidden.
---
## Appendix: w15_verdict.md (worker's long-form verdict, verbatim)

VERDICT: NOT-REFUTED.

I did not build a delta <= 0.25 exact signed idempotent with a hidden top vertex satisfying
sigma_tilde > tau.  All matrices were built as exact projections either by
P = Lambda R, R Lambda = I, or by P = A P0 A^{-1}, A1 = 1, and then verified from P itself
with multiplicity-correct W, LP exposedness, LP l1 distance to conv(W), sigma_tilde including
the self term, and shallow SCC path products.

Closest in-regime record from the broad run:

delta = 0.060906010420960506
tau = 0.24679143101201975
H = 0.007114228160152251
H/tau = 0.028826884835421045
H/delta = 0.11680666835639467
sigma_tilde = 0.2001
sigma_tilde/tau = 0.810806109350913
delta/sigma_tilde^2 = 1.5211287514903344
P_vv = 0.2
nu_v = 0.0028184331717057477
best shallow SCC: C = {1,2,3,4,5,6}, L = 2,
Pi_C = 1.4631093891724293e-06, Pi_C/tau = 5.928525894001441e-06.

This has a very thin shallow component, but it misses the load-bearing gate:
sigma_tilde < tau and H/tau is tiny.

Failure map:

1. LP-financed s5/cycle frames.  For fixed hidden geometry L and requested hidden block B,
Q was chosen by LP to minimize max row negative mass, so this is the best completion inside
the frame, not a min-norm left-inverse artifact.  Audit: 1760 cases, 352 LP completions,
272 verified in delta <= 0.25, 0 branch hits.  Best H/tau = 0.0894516290 occurred at
delta = 0.0019996 but sigma_tilde/tau = 0.00447258.  Smallest Pi_C/tau was
1.97e-11, but sigma_tilde = 0.  Obstruction:

    thin path products are easy, but only in the sigma_tilde <= tau branch.

2. Positive-diagonal/self-mass probes.  This was the main autopsy-driven loophole.
Broad best reached sigma_tilde/tau = 0.810806, still below 1.  Targeted audit:
275 cases, 233 LP completions, 45 verified in regime, 0 branch hits.  Best audit
delta/sigma_tilde^2 = 2.55157; broad best improved that to 1.52113, still above 1.
Obstruction:

    delta >= 1.52 sigma_tilde^2

on the best found self-mass instance, so sigma_tilde > sqrt(delta) never fired.

3. Stochastic-idempotent conjugations P = A P0 A^{-1}.  Audit: 120 cases, 3 verified
in regime, 0 branch hits.  Best sigma_tilde/tau = 0.0306383, best H/tau = 0.0329668.
Obstruction:

    conjugation perturbations produce only O(delta) hidden height and O(delta)
    invisible/self mass, hence sigma_tilde/tau collapses as delta decreases.

4. Large-delta artifacts.  sigma_tilde > tau did appear in the first broad run only at
delta = 7.4013, with tau = 2.7205.  This is outside the small-delta conjectural regime
and was excluded from the in-regime scoring.

Updated calibration:

P(path-product floor / thin-chain exclusion is true in the small-delta regime) = 0.84.

Most promising remaining degree of freedom:

End-to-end nonlinear optimization over (L, B) with W-aware loss, rather than fixing B and
LP-completing Q.  The remaining plausible loophole is a periodic carrier with positive
self-mass and tuned negative return-flow that reduces delta/sigma_tilde^2 below 1 while
keeping the top vertex hidden.  The present LP-completed templates got as low as 1.52,
so that is the concrete barrier to beat.
