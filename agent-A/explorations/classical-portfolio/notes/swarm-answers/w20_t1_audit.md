# w20_t1_audit — T1 HOLDS WITH REPAIR: fixed-mass ambient version banked; recoding step INVALID as written (codex hostile audit, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w20_t1_audit/brief.md. Long form: experiments/out/w20_t1_audit/audit_report.md.

Done. Long-form audit is in [audit_report.md](/tmp/codex-sigma-wall/w20_t1_audit/audit_report.md), not `answer.md`.

Verdict: **T1 HOLDS WITH REPAIR**. Fixed-mass visibility survives with the `eta` support-margin and target-scale hypotheses, but the claimed uniform radius/recode package is not valid as written. Independent numerics reproduced the `1e-6` active-entry stress and found no fixed-mass condition-implies-visible violations, while recoding stress cases fail the fixed-mass hypotheses by factors `62.7` to `314`.

Artifacts written:
- [progress.md](/tmp/codex-sigma-wall/w20_t1_audit/progress.md)
- [independent_visibility_audit.py](/tmp/codex-sigma-wall/w20_t1_audit/independent_visibility_audit.py)
- [independent_visibility_summary.txt](/tmp/codex-sigma-wall/w20_t1_audit/independent_visibility_summary.txt)
- [independent_visibility_results.json](/tmp/codex-sigma-wall/w20_t1_audit/independent_visibility_results.json)

Verification run passed: `python3 -m py_compile independent_visibility_audit.py` and the numerical sweep completed.
---
## Appendix: audit_report.md (verbatim)

# VERDICT: T1 HOLDS WITH REPAIR

The fixed-positive-mass visibility argument is basically correct, but the
claimed uniformity repair is not.  The fixed lemma needs the extra LP support
margin `eta` and a target-scale condition involving `tau(P)`.  Those are real
dependencies, not cosmetics.  The `mu -> 0` recoding paragraph is not a valid
"apply the same argument" step as written: after dropping several small
recurrent coordinates, the recoded H-M point can be order `n theta` away while
its surviving minimum recurrent mass is only order `theta`, so the fixed-mass
hypotheses can fail by factors 60-300 in tiny examples.

Repaired statement: for a fixed H-M base point `P0`, in max-row-`l1` distance
`epsilon=max_i ||p_i-p_i^0||_1`, every recurrent-cluster row vertex `v` with
LP support margin `eta>0` against the rows where the shifted block exposer is
negative is visible whenever

```text
epsilon <= min{ mu(P0)/8, tau/64, eta*tau/64, 1/64 }
```

in the small-delta regime.  This fixed statement is ambient: it uses only
row-wise `l1` proximity and the support-margin LP, not idempotence or the
variety, except when estimating `epsilon` along a variety arc.  The boundary
version must be restated in terms of the total mass actually removed from each
block, not just the threshold `theta`; transient mixture faces whose
coefficients `alpha_is` degenerate must also be recoded.

Calibration: `P(this repaired verdict survives further audit) = 0.74`.

## Visibility Margin Re-Derivation

For an H-M point with recurrent blocks `C_s`, laws `pi_s`, transient rows
`sum_s alpha_is pi_s`, set

```text
Gamma_s(x) = sum_{j in C_s} x_j + sum_{ell in T} x_ell alpha_{ell s}
g_s(x) = 1 - Gamma_s(x).
```

The operator norm of `Gamma_s` from row `l1` to `R` is at most `1`, since its
coordinate weights are in `[0,1]`.  For a base-row mixture
`y=sum_q alpha_q pi_q`,

```text
g_s(y) = 1 - alpha_s = (1/2) ||y - pi_s||_1,
```

using disjoint recurrent supports.  Thus the H-M exposer has exact LP margin
`rho/2` against rows at `l1` distance at least `rho` from `pi_s`.

If `P` is `epsilon`-close to `P0` in max-row-`l1`, and `v in C_s`, then

```text
|[g_s(p_i)-g_s(p_v)] - [g_s(p_i^0)-g_s(pi_s)]| <= 2 epsilon.
```

For any row with `||p_i-p_v||_1 >= rho=4 tau`,

```text
g_s(p_i)-g_s(p_v) >= rho/2 - 3 epsilon = 2 tau - 3 epsilon.
```

The only possible problem is nonnegativity on rows where this shifted exposer
goes slightly negative.  If a support functional `ell_v` satisfies
`ell_v(p_v)=0`, `0 <= ell_v(p_i) <= 1`, and `ell_v >= eta` on those negative
rows, then

```text
f = (g_s - g_s(p_v)) + (2 epsilon/eta) ell_v
```

is nonnegative on all rows and vanishes at `v`.  After normalization by
`1+2epsilon+2epsilon/eta`, far rows still have margin above `kappa=tau/4` under
the displayed sufficient condition.  The constants are conservative but safe
for `tau <= 1`.

Important correction: the proof note's arc "radius"

```text
r(P0,eta,M) = (1/(4 n M)) min{ mu/8, tau(t)/64, eta*tau(t)/64, 1/64 }
```

is not a radius depending only on the base data; it contains `tau(t)`, a
quantity of the target point.  Along
`P(t)=exp(tY)P0 exp(-tY)` with `Y 1=0`, the row-`l1` operator norm gives the
clean ambient estimate

```text
epsilon(t) <= 2 M exp(2 M t) t
```

if `M=||Y||_{infty->infty}` is the max row-sum norm.  The note's `2 n M`
version is only a coarser norm-conversion bound.  To turn the inequality into
a genuine explicit interval in `t`, one also needs a lower scale estimate for
`tau(t)=sqrt(delta(P(t)))`, e.g. from the first nonzero term of `delta` along
the selected arc.

## Recoding Attack

Let `D_s={j in C_s: pi_s(j)<theta}` and `q_s=sum_{D_s} pi_s(j)`.  Recoding
drops `D_s` and renormalizes the survivors:

```text
pi_s' = pi_s|_{C_s\D_s} / (1-q_s).
```

The recurrent row movement is order `2 q_s`, and the proof note's
`epsilon(P0,P0^(theta)) <= 4 n theta` is only a coarse version of
`q_s <= |D_s| theta`.  The surviving minimum mass is at least about `theta`,
but the distance to the recoded point can be many multiples of `theta`.  The
fixed-mass lemma would require, among other things,

```text
epsilon(P(t), P0^(theta)) <= mu(P0^(theta))/8.
```

This is not automatic and is false for clustered small masses near the
threshold.

Numerical recoding stress, with one survivor just above `theta`, many dropped
masses just below `theta`, and a transient mixture coefficient
`alpha_is=theta/2` degenerating simultaneously:

```text
nsmall=4  theta=1e-5  dropped=3.96e-5   eps_rec/theta=7.92   eps/(mu/8)=62.7
nsmall=8  theta=1e-5  dropped=7.92e-5   eps_rec/theta=15.8   eps/(mu/8)=125
nsmall=20 theta=1e-5  dropped=1.98e-4   eps_rec/theta=39.6   eps/(mu/8)=314
nsmall=20 theta=1e-4  dropped=1.98e-3   eps_rec/theta=39.6   eps/(mu/8)=313
```

So the recoded point is not in the fixed-mass visibility neighborhood.  The
repair is to choose boundary strata by total dropped mass gaps, requiring
`q_s << min{mu_after, eta*tau}`; if no such gap exists, the proof must use a
multi-level/Puiseux face analysis rather than one threshold.  Transient
mixture supports need the same treatment: if `alpha_is -> 0`, the tangent face
`S_i={s:alpha_is>0}` changes, and active-zero comparisons must be made after
recoding that face too.

## Quantifiers And Dependencies

The actual fixed-stratum constants depend on:

```text
mu        only to preserve the active positive entries of the chosen H-M stratum
eta       the LP support margin of the particular recurrent-cluster vertex
tau(P)    the target visibility scale sqrt(delta(P))
epsilon   max-row-l1 distance from the base point
M         arc generator norm, if converting epsilon to a t-interval
n         only through norm conversion / recoding counts / LP size
k,t       through the H-M combinatorics and LPs, not as direct margin constants
```

There is no radius depending only on `mu,k,t,n` for all recurrent-cluster
vertices.  `eta` can go to zero for sliver cluster vertices while block masses
stay fixed, and `tau(t)` can be too small unless the selected arc supplies a
lower scale coefficient.

## Independent Numerics

Artifacts:

```text
independent_visibility_audit.py
independent_visibility_summary.txt
independent_visibility_results.json
```

Verification:

```text
python3 -m py_compile independent_visibility_audit.py
python3 independent_visibility_audit.py
```

Fixed-mass pointwise check:

```text
records: 1848
condition_true: 949
formula_condition_true: 33
condition_violations: 0
```

No sampled case violated the repaired implication "fixed T1 hypotheses imply
visible."  The implicit arc formula also produced no visibility failure in the
few cases where `t < r(t)` held, but this does not rescue its quantifiers
because `r(t)` is target-dependent.

Tiny active-entry stress with `mu=9.99999000001e-07`, zero active-zero
derivative cost, and tangent residual `4.99e-11`:

```text
t=1e-04 delta/t=0.99           H/t=1.97999800001      H/delta=1.99999797981
t=3e-05 delta/t=0.966666666667 H/t=2.99666356667e-05 H/delta=3.0999967931e-05
t=1e-05 delta/t=0.9            H/t=9.899989e-06      H/delta=1.09999877778e-05
t=3e-06 delta/t=0.666666666667 H/t=2.66666266667e-06 H/delta=3.999994e-06
t=1e-06 delta/t=0              H/t=0                 H/delta=0
t=3e-07 delta/t=0              H/t=0                 H/delta=0
```

This reproduces the previous audit's warning: above the `1e-6` active-entry
scale, finite-scale behavior can show `H/t ~= 2`; below it the Dini tail
vanishes.  T1 must be genuinely two-scale; naive uniformity in `mu` is false.

## W-Jump Assessment

T1 licenses this compactness step: after selecting a fixed H-M stratum, a fixed
arc, a positive recurrent mass floor, and a positive support-margin floor for
the cluster vertices being used, the recurrent visible hull is present for the
small target scale; any newly visible vertices only enlarge the visible hull
and therefore lower height.  This is enough for the pointwise upper-Dini
argument in the tangent-cone lemma.

T1 does not license naive compactness to `delta=0` across strata.  The visible
set still jumps when recurrent masses vanish, support margins collapse, or
transient mixture faces lose support.  The current recoding paragraph does not
repair that globally.  A valid curve-selection proof still has to stratify the
arc, pick boundary faces with controlled total dropped mass, and handle
Puiseux/multi-rate degenerations explicitly.

Bottom line: fixed-mass T1 survives; the advertised uniform recoding repair
does not.
