# w15_audit — hostile derive-first audit of the w14 H-M autopsy (codex, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w15_audit/brief.md

**Overall Verdict**

The autopsy mostly survives at the row level, but not as written. I found two material defects: row 12 has a bad H-M locus label, and the synthesis overstates the component-finisher attachment. `positive SCC + path product` is not enough; w12 needs a closed primitive positive component inside a positively closed shallow band, plus constants strong enough to force the collapse radius below the exposure threshold.

**Step-Table Verdicts**

| row | verdict | audit result |
|---|---|---|
| 10 | CONFIRMED | H-M Theorem 2.2 says an idempotent probability measure has closed completely simple support and product form `mu1 * Haar * mu3`; proof is positivity/probability based. Signed support does not inherit this. |
| 11 | CONFIRMED | Rees/Suschkewitsch and finite kernel loci are real. Algebra is exact-semigroup algebra; it does not perturb through signed coefficients without a replacement carrier object. |
| 12 | CORRECTED | The math is right, but the locus is not H-M `.txt` lines 55-65/81-82; those lines are front matter. The cited setup is [kernel-conjecture.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex:55). |
| 13 | CONFIRMED | H-M Theorem 1.11 and the deferred proof use nonnegative zero/positive pattern structure. Signed replacement by visible vertices/clusters is heuristic but correctly motivated. |
| 14 | CONFIRMED | Positive diagonal is positivity-rigid. Signed counterexample: `P=1π`, `π1=-ε`, `sum π=1`, gives `P^2=P`, row negativity `ε`, and `P11<0`. |
| 15 | CONFIRMED | The zero-sum closures at H-M lines 3112-3114 and 3141-3148 really use nonnegative terms. Signed cancellations kill the inference. |
| 16 | CONFIRMED | Zero-pattern symmetry/block partition is positivity-rigid. Example: `P=I-u v^T`, `v=(1,0,-1)`, `u=(1,-ε,0)` gives `P1=1`, `P^2=P`, row negativity `ε`, but `P12=0`, `P21=ε>0`. |
| 17 | CONFIRMED | H-M exact positive block rank-one proof is rigid; w12 repair modulus checks out, conditional on its hypotheses. |
| 18 | CONFIRMED | H-M stochastic specialization really says proportional recurrent-block rows become equal because row sums are 1. Perturbative use is conditional after collapse. |
| 19 | CONFIRMED with locus split | H-M gives transient proportional mixtures. The small-invisible-mass bound is campaign math, stated in [kernel-conjecture.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex:176), not H-M. |
| 20 | CORRECTED | Component finisher is conditional, but “positive SCC path products beat error” is underspecified. Needs w12’s closed/primitive/component and radius hypotheses. |
| 21 | CONFIRMED | The missing step is genuinely open: path-product floor/thin-chain exclusion. H-M does not supply it. |

**Checked Inequalities**

Exact row reproduction is correct under row negative mass. Let

\[
\nu_i=\sum_j(P_{ij})_- ,\qquad s_i=\sum_j(P_{ij})_+=1+\nu_i .
\]

With

\[
q_i=\frac1{s_i}\sum_{P_{ij}>0}P_{ij}p_j\in \operatorname{conv}\{p_j:P_{ij}>0\},
\]

the row identity gives

\[
p_i-q_i=\nu_i(q_i-r_i),
\]

where `r_i` is a convex average of negatively weighted rows. Since row diameter is at most `2+4δ`,

\[
\operatorname{dist}\bigl(p_i,\operatorname{conv}\{p_j:P_{ij}>0\}\bigr)
\le (2+4\delta)\nu_i
\le (2+4\delta)\delta .
\]

Rank-one-block repair also checks, but only with w12 hypotheses. The finisher needs

\[
\theta_C>0,\qquad
\varepsilon\le 7\delta+6\delta^2,
\]

and yields

\[
\operatorname{diam}_1\{p_i:i\in C\}
\le
\frac{2(1+\delta)\varepsilon}{\theta_C}+4\delta .
\]

For exposure-grade collapse it is not enough that `θ_C>0`; one needs

\[
\frac{2(1+\delta)\varepsilon}{\theta_C}+4\delta < r_*,
\]

with `r_*=0.85τ` in the audited consumer.

Small invisible mass branch checks. Splitting the signed coefficient vector against `C_W`, one can choose a probability vector on `C_W` so that the residual signed measure has positive and negative mass both bounded by `max(σ̃_v,ν_v)`. Therefore

\[
\operatorname{dist}(p_v,C_W)
\le (2+4\delta)\max\{\widetilde\sigma_v,\nu_v\}
=
2(1+2\delta)\max\{\widetilde\sigma_v,\nu_v\}.
\]

If `σ̃_v≤√δ`, `ν_v≤δ`, and `δ≤1/4`, then

\[
\operatorname{dist}(p_v,C_W)\le 3\sqrt\delta .
\]

**Synthesis Attack**

The synthesis is too loose. w12 licenses attachment only under these extra hypotheses:

\[
P^+_{S,S^c}=0,
\]

a primitive closed positive component, not an arbitrary carrier SCC;

\[
K_C=D^{-1}A_C
\]

must be a genuine almost-idempotent stochastic self-map; and the path-product lower bound must beat the full signed/idempotence error enough to make `R_C<r_*`, not merely make paths positive. Kernel-conjecture itself flags periodic components and analytic band-closure as open caveats at lines 261-264.

`delta` convention: campaign convention is row negative mass, explicitly [kernel-conjecture.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex:62). The entrywise caveat is mathematically real but moot for this campaign.

\[
P(\text{autopsy survives as written})=0.70
\]

\[
P(\text{signed-surrogate frame is the right next attack})=0.74
\]