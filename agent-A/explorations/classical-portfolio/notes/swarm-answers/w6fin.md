VERDICT: DIED-AT.

Precise death inequality:
\[
\sum_{k:g_k\ge \kappa R} P^+_{fk}
\le {g_f+\delta R\over \kappa R},\qquad
\sum_k P^+_{fk}g_k \le g_f+\delta R.
\]
For a financing/top-band row `f` with `g_f < kappa R`, this gives only `<= (kappa+delta)R` weighted budget control. It contains no `H` and no `sigma_v`, so it cannot imply either `A_v >= c H^2/sigma_v^2` or `T_far = empty`.

This is the same wave-5 wall, not a new one: C10/top-band alpha localization is still missing. The financing-row mechanism identifies the right blocker numerically, but does not yet supply the analytic selection lemma tying that blocker’s row budget to `v`’s positive-support geometry.

Post-mortem:

For any invariant deficit `g = Pg`, row exactness gives
\[
g_i=\sum_k P^+_{ik}g_k-\sum_kP^-_{ik}g_k.
\]
With `neg(p_i)<=delta` and `osc(g)=R`,
\[
\sum_k P^+_{ik}g_k \le g_i+\delta R.
\]
Applying this to `v` gives the known upper bound
\[
A_v:=\sum_k P^+_{vk}g_k\le \delta R,
\]
whereas Branch A needs a lower bound `A_v >= c H^2/sigma_v^2`.

Applying it to the alleged financier `f` gives the displayed death inequality. If `g_f` is just below `kappa R`, the estimate is essentially vacuous. If `g_f` is tiny, it proves only that `f` maps mostly inside the tiny top band; it still does not force height, exposure, or `H^2` negativity.

New sub-lemmas:

1. Positive-support shadow, proved:
If `S` is the positive off-site support of `v`, mass `sigma_v`, and negative mass `nu_v<=delta`, then the positive barycenter `q=sum_{s in S}P^+_{vs}p_s/sigma_v` satisfies
\[
\|q-p_v\|_1\le D\nu_v/\sigma_v,\quad D\le 2+4\delta.
\]
This recovers the large-sigma shadow, but only gives top-band concentration.

2. Financing-row no-gain lemma, proved:
Exactness of the financier row gives only its own F-GB inequality above. Column exactness `P_{vf}=(P^2)_{vf}` does not introduce a height lower bound for `g_f`.

3. Missing lemma, open:
A selection/localization theorem identifying the C10 alpha/top-band blocker with a row whose exact budget must see `H` or `sigma_v`.

Calibration:
`P(top-band localization true)`: 0.65 for the H²-negativity qualified form; 0.35 for literal `T_far=empty`.
`P(this diagnosis survives audit)`: 0.85.

Best concrete closer:
Run a joint LP certificate search whose variables include `P,g,phi` and a C10 failed-exposedness witness, with objective maximizing far top-band alpha mass under `P^2=P`. The needed output is a rational dual for an inequality of the form “far top-band alpha mass is controlled by `v`’s positive support plus `H^2` negativity.”