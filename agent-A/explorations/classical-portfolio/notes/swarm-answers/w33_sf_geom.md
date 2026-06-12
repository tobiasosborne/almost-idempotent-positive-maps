# w33_sf_geom — LP-CERTIFICATE AT SMALL k; general-k gap precise; dense-pair family kills universal C<=2 at moderate delta (codex, 2026-06-12)
# Brief: notes/briefs/w33_sf_geom.md. Long form: experiments/out/w33_sf_geom/proof.md.
# Orchestrator review (Claude, 2026-06-12):
#   (1) The section-6 "convexity estimate" Sum (B_sj)+ F(L_j) <= nu_{u_s} max F is FALSE — refuted
#       by the worker's OWN k=7 exact instance (B_0 = (0,..,0,1/2,1/2) has nu_{u_0} = 0 while
#       LHS = 3/4; with global delta = 6/17 instead, RHS = 9/34 < 3/4 still fails). E_0 IS convex
#       with E_0(e_0)=0, so the instance is a direct counterexample to that route. Do NOT build on
#       section 6. The rest (LP certificates, dense-pair instance) is unaffected.
#   (2) The k=7 ratio-17/8 instance is exactly-rationally verified by the worker
#       (dense_pair_k7_verify.txt: P^2=P, BL=I, row sums, max minor 1, delta=6/17, SF=3/4).
#       Independent Claude-family re-verification queued for wave 34.

VERDICT: LP-CERTIFICATE AT SMALL k; GENERAL-k GAP NOT CLOSED.
- BREAKTHROUGH vs w32: the geometry-included structural LP (P = LB, BL = I, full-row negativity)
  REMOVES the delta=0 obstruction. Fixed-support certificates: k=3 pair support ratio = 1+4a^2 <= 2
  (max-volume endpoint a <= 1/2); k=4 cycle/all-pairs ratio = 1+3a^2 <= 7/4.
- DENSE TRANSVERSE PAIRS (new stress family, x_pm = e_0 +- a*v, v with m foreign +1s and m -1s):
  k=7, a=1/4: EXACT RATIONAL instance with delta = 6/17, SF = 3/4, ratio = 17/8 = 2.125;
  k=9, a=0.2: ratio 2.164. So universal C_sf <= 2 is FALSE for delta_0 >= 6/17. NOT a counterexample
  to SF as stated (C may depend on delta_0) — but the sparse-support dual cannot be rank-free.
- THE NAMED MISSING THEOREM (clean fixed-support form): for every k, every coefficient support L
  (rows sum 1, first k rows e_t, max-volume minors <= 1) and every left inverse B with all row
  negative masses of LB <= delta: Sum_j (B_sj)+ E_s(L_j) <= C(delta_0) * delta.
- DECISIVE OPEN EXPERIMENT (orchestrator): m -> infinity scaling of the dense-pair ratio at FIXED
  small delta-cap (0.05/0.1/0.2). Unbounded => dimension-free SF false at fixed delta_0;
  saturating => fit C(delta_0). Pure LP — runs locally without network (resilience protocol).
- Calibration: P(diagnosis survives audit) = 0.82; P(SF true with C = C(delta_0)) = 0.58.
- INFRA: same in-sandbox gurobi HostID failure as w33_cex (gurobi_status.txt); HiGHS used;
  the nonconvex QCP script geom_qcp_search.py is written and ready to run OUTSIDE the sandbox.
---
## Appendix: proof.md (verbatim)

# VERDICT: LP-CERTIFICATE AT SMALL k; GENERAL-k GAP NOT CLOSED

I did not prove the signed-face excess (SF), and I did not find a
dimension-free counterexample.  The useful output of this pass is a
geometry-included LP certificate loop based on the exact H-M converse
parametrization, plus a new dense transverse-pair stress family showing exactly
why the sparse rank-three certificate does not yet globalize.

The strongest finite certificate is:

\[
\sum_j (P_{u_sj})_+ E_s(j)\le C_{\rm supp}\,\delta
\]

for each audited fixed support \(L=(a(j))\) tested, where the LP optimizes over
the full matrix \(P=L B\), not merely over coefficient weights.  The sparse
transverse supports give:

- \(k=3\), signed pair \(e_s\pm a(e_t-e_r)\): ratio \(1+4a^2\), hence at most
  \(2\) under the max-volume endpoint \(a\le 1/2\).
- \(k=4\), cycle/all-pairs supports: ratio \(1+3a^2\), hence at most \(7/4\)
  at \(a=1/2\).

The general-k gap is precise: I do not have a support-independent dual
certificate proving that every max-volume coefficient support \(L\) has a
dimension-free constant depending only on \(\delta_0\).  Dense transverse pairs
already defeat the naive \(C_{\rm sf}\le2\) guess at moderate \(\delta\).

Calibration:

\[
P(\text{this LP-certificate/gap diagnosis survives audit})=0.82,
\qquad
P(\text{SF is true with }C_{\rm sf}=C(\delta_0))=0.58.
\]

No `answer.md` was created.

## 1. Exact Parametrization Used

The Hognas-Mukherjea reference is

`/home/tobias/Projects/almost-idempotent-positive-maps/refs/hognas-mukherjea-2011/hognas-mukherjea-2011.txt`.

The relevant byte checks are saved in `hm112_grep_anchors.txt`:

```text
2246:Theorem 1.12. Let P be a d  d idempotent matrix of rank k. Then there is a
2276:    Conversely any real matrix P with a partition fT; B; C1 ; C2 ; : : : Ck g such that
(i), (ii), (iii), and (iv) hold is idempotent of rank k.
2337:   Conversely, conditions (1.1)–(1.4) imply that P is idempotent.
```

The OCR text uses a control glyph for `x` in line 2246 and an en dash in
`(1.1)–(1.4)`, so the older ASCII quote from w25 is not literally byte-present.

For the row-stochastic campaign objects, the exact parametrization is:

\[
P=L B,\qquad B L=I_k.
\]

Here \(L_{j\cdot}=a(j)\) is the coefficient row of index \(j\), the first \(k\)
rows are the basis vectors \(e_1,\ldots,e_k\), and \(B\) is the matrix of the
representative rows.  If every row of \(L\) sums to \(1\) and every row of \(B\)
sums to \(1\), then \(P{\bf 1}={\bf 1}\).  The identity \(BL=I_k\) gives

\[
P^2=L B L B=L B=P,
\]

so idempotence is structural, exactly as in the H-M converse.  The row negative
constraints are imposed on the full rows

\[
\nu_i=\sum_j(-P_{ij})_+\le\delta.
\]

This is the geometry that the coefficient-only relaxation did not include.

## 2. Tooling Note

I wrote `geom_qcp_search.py` for the mandated Gurobi nonconvex QCP over
variable \(L,B,P\), with \(P=LB\), \(BL=I\), row negativity, and sign-chamber
objectives for the signed-face excess.  Model creation is blocked in this
container by the Gurobi license, despite the installation being present.  The
saved check in `gurobi_status.txt` says:

```text
Gurobi Optimizer version 13.0.1 build v13.0.1rc0 (linux64 - "Linux Mint 22.3")
gurobipy (13, 0, 1)
model creation: GurobiError HostID mismatch (licensed to a690fcd, hostid is 0)
```

I therefore used SciPy/HiGHS for the exact fixed-support structural LPs.  These
LPs are not coefficient-only: for each support \(L\) they optimize over all
representative rows \(B\), construct \(P=LB\), enforce \(BL=I\), and constrain
negative mass of every full row.

## 3. LP Form

For a fixed coefficient support \(L\), the variables are:

- \(B_{rj}\), the representative rows;
- \(z_{ij}\ge0\), epigraph variables for \((-P_{ij})_+\);
- \(\delta\).

The constraints are:

\[
\sum_jB_{rj}=1,\qquad
\sum_jB_{rj}L_{jt}=\delta_{rt},
\]

\[
z_{ij}\ge -(LB)_{ij},\qquad
\sum_j z_{ij}\le\delta.
\]

For a fixed sign pattern of \(B_{sj}\), the objective

\[
\sum_{j:B_{sj}\ge0} B_{sj}E_s(j)-C\delta
\]

is linear.  Enumerating the sign pattern gives a global LP certificate for that
support and constant \(C\).

The main implementation is `fixed_support_geom_lp.py`; targeted summaries are
in `fixed_support_smoke.txt`, `targeted_geom_lp_summary.txt`, and
`dense_pair_C2_summary.txt`.

## 4. Sparse Supports: Geometry Cuts the Delta-Zero Obstruction

For the old transverse-pair support

\[
L=\{e_1,e_2,e_3,e_1+a(e_2-e_3),e_1-a(e_2-e_3)\},
\]

the coefficient-only relaxation has a \(\delta=0\) obstruction.  The structural
LP does not: it forces full-row negativity in the non-\(s\) rows and in the pair
rows.

Representative data from `fixed_support_smoke.txt`:

```text
pair_k3_a0.05: upper_C=1.0099998
pair_k3_a0.2:  upper_C=1.1599999
pair_k3_a0.5:  upper_C=2
```

The active exact row has \(B_s=(0,0,0,1/2,1/2)\).  At \(a=0.2\),

\[
\text{target}=0.2,\qquad
\delta=0.1724137931,\qquad
\text{ratio}=1.16.
\]

The exact idempotence and \(BL=I\) residuals are at roundoff
(\(\le 10^{-16}\)).  The observed formula on this support is

\[
\frac{\sum_j(P_{u_sj})_+E_s(j)}{\delta}=1+4a^2\le2.
\]

For \(k=4\), both the cycle and all-pairs supports satisfy the support
certificate

\[
\text{ratio}=1+3a^2\le 7/4
\]

on the tested amplitudes.  See `targeted_geom_lp_summary.txt`.

## 5. Dense Transverse Pair: The General-k Gap

The sparse active set does not globalize by inspection.  Consider

\[
L=\{e_0,e_1,\ldots,e_{2m},
e_0+a v,\ e_0-a v\},
\]

where \(v\) has \(m\) foreign coordinates \(+1\), \(m\) foreign coordinates
\(-1\), and \(v_0=0\).  Every row of \(L\) sums to \(1\).  The max-volume minor
audit for the tested cases reports max minor \(1\).

The dense-pair C=2 sweep gives:

```text
dense k=5 a=0.25: target=0.5  delta=0.3000000000 ratio=1.6666666667
dense k=7 a=0.25: target=0.75 delta=0.3529411765 ratio=2.125
dense k=9 a=0.20: target=0.8  delta=0.3697478992 ratio=2.1636363636
```

Thus any proof with a universal \(C_{\rm sf}\le2\) is false once
\(\delta_0\ge6/17\).  This is not a counterexample to SF as stated, because
SF allows dependence on \(\delta_0\), but it is a real obstruction to the
sparse-support certificate.

For \(k=7,a=1/4\), the exact rational active matrix from
`dense_pair_k7_a025_C2_solution.json` has

\[
\delta=6/17,\qquad
\sum_j(P_{u_0j})_+E_0(j)=3/4,\qquad
\text{ratio}=17/8.
\]

The coefficient support is

\[
\begin{aligned}
&e_0,\ldots,e_6,\\
&x_+=e_0+\tfrac14(e_1+e_2+e_3-e_4-e_5-e_6),\\
&x_-=e_0-\tfrac14(e_1+e_2+e_3-e_4-e_5-e_6).
\end{aligned}
\]

The representative row \(B_0\) is

\[
B_0=(0,0,0,0,0,0,0,1/2,1/2).
\]

Rows \(1,2,3\) of \(B\) have diagonal \(31/34\), same-side off-diagonal
\(-3/34\), opposite-side off-diagonal \(3/34\), and pair entries
\((3/17,-3/17)\).  Rows \(4,5,6\) have the sign-reversed pattern.  The two pair
rows of \(P\) are

\[
(0,2/17,2/17,2/17,-2/17,-2/17,-2/17,13/17,4/17),
\]

\[
(0,-2/17,-2/17,-2/17,2/17,2/17,2/17,4/17,13/17).
\]

Every nonzero row negative mass is \(6/17\).  Direct verification in the JSON
gives \(P^2=P\), row sums \(1\), \(BL=I\), and max-volume minor \(1\).

## 6. What Still Needs Proof

The missing theorem is now a clean fixed-support statement:

For every rank \(k\), every coefficient support \(L\) with rows summing to
\(1\), first \(k\) rows \(e_t\), max-volume minors bounded by \(1\), and every
left inverse \(B\) such that \(P=LB\) has row negative masses \(\le\delta\),
prove

\[
\sum_j(B_{sj})_+E_s(L_j)\le C(\delta_0)\,\delta.
\]

The LP certificates prove this for the sparse supports tested.  The dense-pair
family shows the proof must use the actual size of \(\delta_0\); the active-set
dual from \(k=3\) cannot be rank-free without new inequalities controlling
dense transverse directions.

The promising but incomplete analytic route is the convexity estimate:
for any convex \(F\ge0\) with \(F(e_s)=0\),

\[
\sum_j(B_{sj})_+F(L_j)\le \nu_{u_s}\max_jF(L_j).
\]

Taking \(F=E_s\) recovers the right cancellation mechanism but leaves the
rank-dependent term \(\max E_s\).  The dense-pair numerics suggest that full-row
negativity forces \(\max E_s\) to scale with the available \(\delta_0\), not
with \(k\), but I did not convert that observation into a support-independent
proof.

## 7. Artifacts

- `geom_qcp_search.py`: Gurobi nonconvex QCP model over variable \(L,B,P\);
  blocked by license at model creation.
- `gurobi_status.txt`: saved Gurobi version/license failure.
- `hm112_grep_anchors.txt`: byte-checked H-M theorem/converse anchors.
- `fixed_support_geom_lp.py`: exact fixed-support structural LP over \(B,P\).
- `targeted_geom_lp.py`: targeted sparse-support C sweeps.
- `dense_pair_probe.py`: dense transverse-pair stress family.
- `fixed_support_smoke.json`, `fixed_support_smoke.txt`: first exact support
  certificates.
- `targeted_geom_lp_results.json`, `targeted_geom_lp_summary.txt`: sparse
  \(k=3,4\) sweeps.
- `dense_pair_C2_results.json`, `dense_pair_C2_summary.txt`: dense-pair C=2
  sweep.
- `dense_pair_k7_a025_C2_solution.json`: exact rationalizable \(k=7\) active
  solution with ratio \(17/8\).
- `dense_pair_k7_verify.txt`: exact rational verification of idempotence,
  \(BL=I\), row sums, max minor \(1\), \(\delta=6/17\), target \(3/4\).

Verification commands run:

```text
python3 -m py_compile geom_qcp_search.py
python3 -m py_compile fixed_support_geom_lp.py
python3 -m py_compile targeted_geom_lp.py
python3 -m py_compile dense_pair_probe.py
```

The broad binary-search sweep `fixed_support_geom_lp.py --ks 3 4 ...` was
abandoned as over-broad; its results are not used above.
