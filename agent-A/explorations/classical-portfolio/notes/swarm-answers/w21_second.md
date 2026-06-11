# w21_second — DIED-AT (no counterexample): the sharp cases are boundary recoding events (codex, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w21_second/brief.md. Long form: experiments/out/w21_second/proof.md.

DIED-AT, not proved and no counterexample found.

I saved the long-form verdict to [proof.md](/tmp/codex-sigma-wall/w21_second/proof.md). The numerical artifacts are also saved:

- [second_order_decider.py](/tmp/codex-sigma-wall/w21_second/second_order_decider.py)
- [filter_second_order_results.py](/tmp/codex-sigma-wall/w21_second/filter_second_order_results.py)
- [second_order_fixed_window_summary.txt](/tmp/codex-sigma-wall/w21_second/second_order_fixed_window_summary.txt)
- [second_order_full_records_summary.txt](/tmp/codex-sigma-wall/w21_second/second_order_full_records_summary.txt)
- [second_order_filtered_summary.txt](/tmp/codex-sigma-wall/w21_second/second_order_filtered_summary.txt)

Key result: sampled dangerous directions had `dot_delta` and frozen first-order `D` at numerical zero, and no `q_delta = 0 < q_H` seed appeared. Raw `H/delta = 2.00000000004` was reproduced, but the top cases are finite-scale boundary recoding events above tiny positive entry scales, not clean fixed-base second-order limits. In the filtered fixed-base window, the resolvable samples had `max_local_ratio = 0`.

The remaining failed estimate is still the finite-jet/quadratic normal projection bound:
`\|(C,D)_{\perp M}\|^2 <= L_n * delta(P(C,D))`.
`python3 -m py_compile second_order_decider.py filter_second_order_results.py` passed.
---
## Appendix: proof.md (verbatim)

# VERDICT: DIED-AT

I did not prove the second-order tangent-cone lemma, and I did not find a
counterexample direction.

The run produced useful negative evidence: every sampled dangerous direction
had `dot_delta` and frozen first-order height `D` at numerical zero, and no
sample produced a `q_delta = 0 < q_H` seed.  The raw ratio `H/delta = 2` is
reproduced, but in the saved runs it is attained in finite-scale boundary
recoding windows where `t` is larger than a tiny positive H-M entry.  After
filtering to the fixed-base window `t < 0.1 * min_positive_entry(P0)`, the
resolvable samples had zero measured second-order height.

The exact failed estimate is still the quadratic/finite-jet normal bound:
\[
  \|(C,D)_{\perp\mathcal M}\|^2 \le L_n\,\delta(P(C,D)),
\]
or, equivalently on a dangerous first jet, a finite-order statement saying
that every nonnegative second jet can be re-based onto the H-M locus with
normal error controlled by the first nonzero negative active entry.  I can
verify the first dangerous-cone cancellation, but I cannot close the
second-order iteration without an external finite-determinacy or
Lojasiewicz-type projection theorem.

## 1. Decomposition At An H-M Base Point

Let \(P_0\) be an H-M stochastic idempotent with recurrent blocks
\(C_1,\ldots,C_k\), transient set \(T\), recurrent laws \(\pi_s\), and transient
coefficients \(\alpha_i\).  A variety tangent \(A\) satisfies
\[
  P_0A+AP_0=A,\qquad A\mathbf 1=0.
\]
The first-order normal cost is
\[
  \dot\delta_{P_0}(A)
  =\max_i\sum_{j:P_{0,ij}=0}(-A_{ij})_+ .
\]

There are three cases.

1.  **Stratum tangent.**  \(A\) is tangent to the fixed H-M parameter stratum.
    Rebase along the H-M family.  This is harmless, but only after tracking
    boundary changes of recurrent support and transient coefficient support.

2.  **Linear normal.**  \(\dot\delta(A)>0\).  The audited w19 lemma gives
    \[
      \dot H^+(A)\le 2\dot\delta(A).
    \]
    Together with w20 visibility, this controls exact arcs at a fixed H-M base
    point, with a radius depending on \(n\), the minimum positive recurrent
    mass, and the active transient face depths.

3.  **Dangerous cone.**  \(\dot\delta(A)=0\).  Then \(A_{ij}\ge0\) at every
    active zero.  The audited fact is that the frozen first-order height also
    vanishes:
    \[
      D(A)=2\max_i\sum_{q\notin S_i}(-\Gamma_q(A_i))_+=0.
    \]
    Thus both \(H\) and \(\delta\) restart at second order.

## 2. Exact Chart And The Second-Order Object

Use the w18 chart in the splitting
\[
  \mathbb R^n=E\oplus F,\qquad E=\operatorname{im}P_0,\quad F=\ker P_0:
\]
\[
P(C,D)=
\begin{pmatrix}
(I+CD)^{-1} & (I+CD)^{-1}C\\
D(I+CD)^{-1} & D(I+CD)^{-1}C
\end{pmatrix},
\qquad D\mathbf1=0.
\]
For \(C=tC_1+t^2C_2+\cdots\), \(D=tD_1+t^2D_2+\cdots\),
\[
  P(t)=P_0+tA+t^2B+O(t^3),
\]
where the diagonal second fundamental form contains
\[
  B_{EE}=-C_1D_1+\cdots,\qquad B_{FF}=D_1C_1+\cdots .
\]
Equivalently, for the conjugation arc used numerically,
\[
  P(t)=\exp(tY)P_0\exp(-tY),
\]
the script computes the exact coefficient
\[
  B={1\over2}(Y^2P_0+P_0Y^2-2YP_0Y).
\]

For a dangerous first jet, the fixed-base second-order delta coefficient is
\[
  q_\delta(A,B)
  =
  \max_i\sum_{\substack{j:P_{0,ij}=0\\ A_{ij}=0}}(-B_{ij})_+ .
\]
Entries with \(A_{ij}>0\) are not fixed-base second-order costs; they open a
new nonnegative face and must be re-based before measuring the next normal
component.  This is exactly where the iteration begins.

The desired second-order lemma would be:
\[
  q_H(A,B)\le C_2\,q_\delta(A,B)
\]
after quotienting out all second-order H-M rebasings, and if
\(q_\delta(A,B)=0\), the same statement must restart at the next nonzero jet.

## 3. Where The Proof Dies

The first-order proof uses only the row coefficient identity
\[
  A_i=\sum_s\alpha_{is}B_s+\sum_q\Gamma_q(A_i)\pi_q
\]
and the inequality
\[
  \sum_{q\notin S_i}(-\Gamma_q(A_i))_+
  \le
  \sum_{j:P_{0,ij}=0}(-A_{ij})_+ .
\]
On the dangerous cone the right-hand side is zero, hence the first-order
height vanishes.

At second order, the same argument would need a replacement coefficient
identity for the first non-H-M jet after all allowed H-M rebasings.  The
missing estimate is:
\[
  \operatorname{dist}\bigl(J^2(P),J^2(\mathcal M)\bigr)
  \le L_n\,q_\delta(A,B)
\]
in a norm strong enough to bound visible-hull height, with the evident
iteration if \(q_\delta(A,B)=0\).  I do not have this.

The failure occurs at iteration depth 2.  If \(q_\delta>0\), the numerics
support the same sharp ratio \(2\).  If \(q_\delta=0\), the second jet remains
inside the nonnegative cone and may correspond to moving onto an adjacent
H-M stratum.  To continue, one must prove that after finitely many such
rebasings the first genuinely normal jet is controlled by the first negative
active entry, with constants depending only on the fixed local data.  I have
not proved this finite-determinacy statement.

## 4. Numerical Decider

Saved code:

- `second_order_decider.py`
- `filter_second_order_results.py`

The decider reuses the audited w19 implementation for H-M strata, tangent
equations, \(\dot\delta\), frozen \(D\), and visible height.  It samples two
classes of dangerous directions:

- one-sided LP extreme points with \(A_{ij}\ge0\) at active zeros;
- the equality slice \(A_{ij}=0\) at active zeros, where genuine fixed-base
  second-order \(\delta\) can first appear.

It integrates exact idempotent arcs and records `H/delta`, `delta/t^2`,
`H/t^2`, the analytic chart coefficient `q_delta_B`, and visibility data.

Verification:

```text
python3 -m py_compile second_order_decider.py filter_second_order_results.py
```

passed.

### Main Runs

`second_order_fixed_window_summary.txt`

- `39` strata, `352` dangerous directions.
- `dot_delta_max = 1.726e-14`.
- `frozen_D_max = 1.548e-14`.
- `counterseed_count = 0`.
- raw `max_tail_ratio = 2.000000000204834`.

The top raw samples have `q_delta_B` around machine zero but
`delta/t` of order `0.01` to `1`.  Inspection shows their
`min_positive_entry(P0)` is around `1e-7` while the tested `t` is
`1e-5` to `1e-3`.  These are not fixed-base second-order measurements; they
are boundary recoding transitions.

`second_order_full_records_summary.txt` and
`second_order_filtered_summary.txt`

- `25` strata, `172` dangerous directions with full records.
- raw `max_tail_ratio = 2.0000000000392326`.
- filtered local window `t < 0.1 * min_positive_entry(P0)`:
  `52` records had local samples and `max_local_ratio = 0`.
- finite-scale window:
  `max_transition_ratio = 2.00000000004`.

The ratio-2 samples occur when a tiny positive entry in the H-M base is crossed
at finite scale.  The visible set has one more row vertex than visible
recurrent vertices (`visible=5`, `vertices=6` in the top case), matching the
same recurrent-hull/face geometry as the first-order sharp bound.

`second_order_small_t_summary.txt`

- `21` strata, `172` directions.
- tested below the tiny-mass scale.
- `counterseed_count = 0`.
- measured tail ratios collapse to `0`, but this is also the regime where the
  \(t^2\) signal is at or below double-precision LP tolerances.

## 5. Conditional Assembly

Here is the precise conditional local statement.

Fix \(n\) and a fixed H-M base point \(P_0\).  Suppose:

1. w20 visibility holds with local radius
   \(r=r(n,\mu,\eta,M)\), where \(\mu\) is the minimum positive recurrent mass,
   \(\eta\) is the relevant transient face/visibility depth, and \(M\) bounds
   the chart norm;
2. the audited first-order lemma holds:
   \[
     \dot H^+\le 2\dot\delta;
   \]
3. for every dangerous jet, the finite-jet normal estimate holds with constant
   \(C_2(P_0)\):
   \[
     q_H\le C_2(P_0)q_\delta
   \]
   after re-basing along every H-M jet for which \(q_\delta=0\).

Then every exact idempotent row-stochastic \(P\) sufficiently close to \(P_0\)
satisfies
\[
  H(P)\le C(P_0)\,\delta(P),
\qquad
  C(P_0)=\max\{2,C_2(P_0)\}+o(1)
\]
after shrinking the neighborhood.  If the second-order/finite-jet constant is
dimension-free and equals `2`, the assembled local constant is `2` at the
Dini/arc level.

The remaining gap between this conditional statement and a neighborhood
theorem is semialgebraic curve selection with explicit control of boundary
rebasings.  Without it, the proof is only an arc-by-arc outline.

## 6. UNVERIFIED-LEADS

1. A finite-determinacy theorem for the nonnegative idempotent/H-M locus:
   every arc whose first \(m\) jets stay in the nonnegative tangent cone can be
   re-based onto an H-M arc until the first normal jet appears.

2. A local projection/retraction from the idempotent variety to the H-M locus
   with
   \[
     \operatorname{dist}(P,\mathcal M)^2\le L_n\delta(P).
   \]
   This is the original T2 estimate in geometric form.

3. A proof that the tangent cone of the H-M locus equals
   \(T\mathcal I\cap T\mathbb R_+^{n\times n}\) at every boundary H-M point,
   with constants stable under transient face-depth collapse.

4. A uniform semialgebraic Lojasiewicz inequality with exponent `1` for
   \(H\) versus \(\delta\) near the H-M locus.  Standard semialgebraic
   theory gives some exponent after compactification, but not the linear
   exponent or the sharp constant `2`.

## 7. Calibration

P(local law true with sharp local constant `C = 2`): `0.84`.

P(this tangent/finite-jet route proves it without a new external ingredient):
`0.31`.

The probability split is driven by the numerics: ratio `2` keeps reappearing
and no dangerous counterseed appears, but the proof still lacks the finite-jet
normal projection estimate that w20 identified as T2.
