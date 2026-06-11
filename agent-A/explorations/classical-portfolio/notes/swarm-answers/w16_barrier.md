# w16_barrier — DIED-AT the quotient pinning / anti-splitting step (codex, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w16_barrier/brief.md

VERDICT: DIED-AT.

I used the high-height branch `H > B tau`; the `H <= B tau` branch is already covered by the proved belt. The progress log is updated at [progress.md](/tmp/codex-sigma-wall/w16_barrier/progress.md).

What is proved clone-invariantly:

\[
S_t=\{i:g_i<t\},\qquad t=\kappa\Omega_g,\qquad \Omega_g\le 2+4\delta.
\]

From \(Pg=g\), \(g_v=0\), and row negative mass \(\nu_v\le\delta\),

\[
A_v(S_t^c)\le \frac{\delta\Omega_g}{t}=4\tau .
\]

The small-\(\widetilde\sigma\) height cap gives, for \(\delta\le1/4\),

\[
H>B\tau \quad\Longrightarrow\quad
\widetilde\sigma_v\ge \frac{H}{2(1+2\delta)}>\frac{B}{3}\tau .
\]

Therefore

\[
A_v(S_t\setminus C_W)
\ge \left(\frac B3-4\right)\tau .
\]

So high hidden height forces aggregate shallow off-\(C_W\) positive carrier mass at scale \(\tau\). This is the strongest clean output of the route.

The failed inequality is the needed quotient pinning step:

\[
\boxed{
\max_{\mathcal C\subset S_t\setminus C_W}
A_v(\mathcal C)\ \ge\ c_B\,\tau
}
\]

for a closed quotient positive component \(\mathcal C\), strong enough to attach the w12 finisher. Equivalently, one needs a dimension-free bound

\[
\#\{\text{geometrically distinct shallow quotient components hit by }P_v^+\}
\le N_B .
\]

I cannot derive this from the audited tools. Pure \(\ell^1\) geometry has no dimension-free packing bound, exact cloning only removes coincident rows, and near-distinct shallow classes can still split the aggregate mass. Row reproduction gives only distance to the positive-successor hull; hiddenness gives a far-row LP shadow; the missing coupling is still

\[
\sum_{b\in F_v\cap S_t}\mu_b\,P^+_{vb}\ge c\tau .
\]

Natural repairs fail for the recorded reasons: atom path-products are killed by cloning, aggregate mass does not imply w12 closed-component radius, threshold/coarea arguments give averaged not sup closure, and diagonal return-flow can spread over arbitrarily many quotient classes.

This suggests a numerical decider target: a high-dimensional shallow fan/thin web where row \(v\) spreads \(O(\tau)\) positive mass over many noncoincident quotient classes while the hiddenness LP blocker is supported on a far top-band average.

Calibrated probabilities: \(P(\)barrier true\()\approx 0.74\). \(P(\)this quotient/LP route closes without a new facial-modulus theorem\()\approx 0.22\).