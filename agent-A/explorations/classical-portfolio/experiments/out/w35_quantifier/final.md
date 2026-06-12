VERDICT: CHAIN-COMPATIBLE.

Long form is in [proof.md](/tmp/codex-sigma-wall/w35_quantifier/proof.md). Progress is in [progress.md](/tmp/codex-sigma-wall/w35_quantifier/progress.md). I verified `answer.md` is absent.

Core result: the chain only needs one selected actual-row chart with bounded coefficients and SF control. It does not need SF for every max-volume chart or a canonical max-volume tie choice.

Registry contract:
`exists theta-quasi-max actual-row basis U with max_s SF_s(U) <= C_sf(delta0,theta) delta(P)` for `delta0 <= 0.3`.

Quasi constants recorded:
`A=theta^{-1}`,
`C_mu = C_sf + 1 + A`,
`C_D = 4(1+2 delta0)(C_sf + 1 + A)`,
`L_eta <= C_D delta/eta + delta`,
and L4 gives `||P-Q||_{infty,1} <= eta + 12 C_D delta/eta + 36 delta` when `eta <= theta/4` and `L_eta <= 1/8`.

Recommended tie-break: minimize `max_s SF_s` over theta-quasi-max bases, then lexicographic tie-break. It collapses the staircase and the audited w33 dense/transverse examples. Minimal-support/unit-row and projected-volume rules are not registry-ready.

If someone insists on for-all/canonical max-volume SF, the half-delta staircase kills that route at `delta0 >= 1/2`; below `1/2` it is not killed by this family.