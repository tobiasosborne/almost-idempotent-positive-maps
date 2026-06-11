# w28_face — DIED-AT: reduced to the representative displacement lemma (codex, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w28_face/brief.md. Long form: experiments/out/w28_face/proof.md.

VERDICT: DIED-AT.

I did not prove the estimate, and I did not find a counterexample. The long-form artifact is in [proof.md](/tmp/codex-sigma-wall/w28_face/proof.md). The exact failed subestimate is the stronger representative displacement lemma:

\[
\sum_j (P_{u_sj})_+ \|p_j-p_{u_s}\|_1 \le C_D\delta
\]

If that lemma is proved, the target follows immediately by Markov’s inequality over rows outside \(M_s\). Numerics strongly support it, but I could not derive it from the audited row-reproduction/coordinate tools.

Artifacts saved:

- [w28_face_numerics.py](/tmp/codex-sigma-wall/w28_face/w28_face_numerics.py)
- [w28_face_numeric_results.json](/tmp/codex-sigma-wall/w28_face/w28_face_numeric_results.json)
- [w28_face_numeric_summary.txt](/tmp/codex-sigma-wall/w28_face/w28_face_numeric_summary.txt)
- [progress.md](/tmp/codex-sigma-wall/w28_face/progress.md)
- [proof.md](/tmp/codex-sigma-wall/w28_face/proof.md)

Verification passed:

```text
python3 -m py_compile w28_face_numerics.py
python3 w28_face_numerics.py
```

No `answer.md` was created. Since the estimate was not proved, I did not assemble the global W-free theorem.
---
## Appendix: proof.md (verbatim)

# VERDICT: DIED-AT

I did not prove the requested representative off-cluster estimate

\[
L_\eta:=\max_s\sum_{j\notin M_s}|P_{u_sj}|
\le C\left(\eta+{\delta\over\eta}\right).
\tag{T}
\]

I also did not find a counterexample to (T).  The requested numerical suite
supports the conjectured shape: the known w27 rank-2 family saturates the
\(\sqrt\delta\) scale, the split-block family is harmless after the max-volume
merge, random small-\(\delta\) exact-variety samples are far below the bound,
and the certified w16/w17 instances sit near ratio \(0.5\) despite being above
the small-\(\delta\) corner.

The exact failed subestimate is the following stronger representative-only
displacement lemma:

\[
\boxed{
D_s:=\sum_j (P_{u_sj})_+\,\|p_j-p_{u_s}\|_1
\stackrel{?}{\le} C_D\delta .
}
\tag{D}
\]

If (D) is proved, then (T) follows immediately, since every
\(j\notin M_s\) has \(\|p_j-p_{u_s}\|_1>\eta\):

\[
\sum_{\substack{j\notin M_s\\P_{u_sj}>0}}P_{u_sj}
\le {D_s\over\eta}
\le {C_D\delta\over\eta},
\qquad
\sum_{\substack{j\notin M_s\\P_{u_sj}<0}}|P_{u_sj}|\le\delta.
\]

For \(0<\eta\le1\), this gives \(L_\eta\le (C_D+1)\delta/\eta\), hence the
requested \(C(\eta+\delta/\eta)\).  Numerically, (D) is very stable for the
max-volume representative rows: it is \(2\delta+o(\delta)\) on the sharp
rank-2 and split-block families, \(4\delta/3+o(\delta)\) on w19 leftcone, and
about \(2.43\delta\) on the above-corner certified instances.

But I do not have a proof of (D).  The audited row-reproduction modulus gives
only

\[
\operatorname{dist}\bigl(p_{u_s},
\operatorname{conv}\{p_j:P_{u_sj}>0\}\bigr)
\le (2+4\delta)\nu_{u_s},
\]

or equivalently a bound on the norm of the positive weighted average after
normalization.  It does not bound the positive weighted average of the norms.
The missing signed affine-face configuration is exactly the case where
positive far rows can cancel each other transversely while preserving all
scalar coordinate identities.

Calibration:

\[
P(\text{this DIED-AT survives audit})=0.76,
\qquad
P(\text{estimate (T) is true})=0.68,
\qquad
P(\text{lemma (D) is the right missing lemma})=0.57.
\]

No `answer.md` was created.

## Setup

Use the w26 audited max-volume chart.  Let

\[
P^2=P,\qquad P{\bf 1}={\bf 1},\qquad
\nu_i=\sum_j(-P_{ij})_+,\qquad \delta=\max_i\nu_i,
\qquad R=1+2\delta .
\]

Choose actual rows \(r_s=p_{u_s}\), \(s=1,\ldots,k\), maximizing volume among
row bases.  Write

\[
p_i=\sum_s\beta_s(i)r_s,\qquad P\beta_s=\beta_s,\qquad
\sum_s\beta_s(i)=1,
\]

with the audited dimension-free bounds

\[
|\beta_s(i)|\le1,\qquad
\|\beta_s\|_{(V,\|\cdot\|_1)^*}\le1.
\]

For \(0<\eta\le1/4\),

\[
M_s=\{i:\|p_i-r_s\|_1\le\eta\},\qquad
B_\eta=[n]\setminus\bigcup_sM_s .
\]

The imported w27 estimates remain valid:

\[
\|p_i-\widehat r_s\|_1\le \eta+2\delta,\qquad i\in M_s,
\]

and

\[
\sum_{j\in\cup_{t\ne s}M_t}|P_{u_sj}|
\le {2\delta\over1-\eta}+\delta .
\tag{1}
\]

Thus the only uncontrolled part of \(L_\eta\) is representative mass on
\(B_\eta\).

## What Still Proves

The scalar coordinate telescope controls all rows with a visible loss in the
\(s\)-coordinate.  From

\[
0=\sum_jP_{u_sj}(1-\beta_s(j))
\]

and \(0\le 1-\beta_s(j)\le2\), one has, for every \(\rho>0\),

\[
\sum_{\substack{P_{u_sj}>0\\ \beta_s(j)\le1-\rho}}P_{u_sj}
\le {2\delta\over\rho}.
\tag{2}
\]

Consequently, convex \(B_\eta\)-rows are controlled: if \(\beta(j)\) is in the
simplex and \(j\notin M_s\), then

\[
\eta<\|p_j-r_s\|_1
\le 2R(1-\beta_s(j)),
\]

so (2) gives the usual \(O(\delta/\eta)\) bound.

The remaining rows satisfy \(\beta_s(j)\approx1\) but are far from \(r_s\)
because the other coordinates cancel in plus/minus pairs:

\[
\sum_{t\ne s}\beta_t(j)\approx0,\qquad
\sum_{t\ne s}|\beta_t(j)|\gtrsim\eta .
\]

Equivalently their coefficient negative mass

\[
\mu_j=\sum_t(-\beta_t(j))_+
\]

is at least a constant multiple of \(\eta\) after the scalar-deficit part is
removed.  Bounding the representative's positive mass on this set would follow
from a dimension-free estimate of the form

\[
\sum_j(P_{u_sj})_+\mu_j\le C\delta .
\tag{M}
\]

I could not derive (M) from the audited tools.  The fixed-coordinate identities
only give scalar cancellation; they do not prevent positive mass from being
split between opposite signed-face directions.  The row-reproduction convex
hull modulus sees the average of those directions, not their total variation.

Lemma (D) is a row-space version of (M) and is the cleanest failed subestimate:
it exactly forbids such transverse positive cancellation at representative
rows.

## Numerics

Artifacts:

- `w28_face_numerics.py`
- `w28_face_numeric_results.json`
- `w28_face_numeric_summary.txt`
- `progress.md`

Verification:

```text
python3 -m py_compile w28_face_numerics.py
python3 w28_face_numerics.py
```

Both passed.

Summary of the target ratio

\[
{ \max_s\sum_{j\notin M_s}|P_{u_sj}|
\over
\eta+\delta/\eta}
\]

with \(\eta=\sqrt\delta\):

```text
w27 rank-2 leakage: ratios 0.55, 0.515811, 0.505, 0.501581, 0.5005
split block: ratios 0.05, 0.0158114, 0.005, 0.00158114
w19 leftcone: ratios 0.0833333, 0.0263523, 0.00833333, 0.00263523
w16 best rational above corner: ratio 0.489732
w17 main rational above corner: ratio 0.492049
w17 robust rational above corner: ratio 0.493795
random small-delta conjugations: 36 samples, max ratio 0.100086
```

The w27 rank-2 family has

\[
P_{13}=\sqrt\delta,\qquad P_{12}=-\delta,
\]

so its total off-cluster \(\ell^1\) mass is

\[
\sqrt\delta+\delta,
\]

and its \(B_\eta\)-mass alone is exactly \(\sqrt\delta\).  This confirms the
known saturation: no \(O(\delta)\) representative support estimate is possible.

The diagnostic ratio for (D),

\[
{D_s\over\delta}
=
{1\over\delta}\sum_j(P_{u_sj})_+\|p_j-p_{u_s}\|_1,
\]

was:

```text
w27 rank-2 leakage: tends to 2
split block: tends to 2
w19 leftcone: tends to 4/3
w16/w17 above corner: between 2.37 and 2.43
```

This is strong evidence for (D), but not a proof.

## Conditional Assembly Status

Since (T) is not proved here, I did not assemble a new global theorem.

The w27 conditional assembly remains exactly as stated: if

\[
L_\eta\le C_L\left(\eta+{\delta\over\eta}\right)=:L,\qquad L\le {1\over8},
\]

then the H-M construction obtained by normalizing the representative laws on
the clusters, clipping \(B_\eta\)-row coefficients to the simplex, and zeroing
transient columns satisfies

\[
\|P-Q\|_{\infty,1}\le \eta+12L+24\delta.
\]

With \(\eta=\sqrt\delta\), this would give

\[
\|P-Q\|_{\infty,1}
\le (1+12C_L)\sqrt\delta+(12C_L+24)\delta .
\]

This theorem is still conditional on the missing representative leakage
estimate.  The present run does not license the W-free global statement.

## Final Failure Point

The campaign is reduced further than w27 in one useful way:

\[
\boxed{
\text{Prove (D), or equivalently a dimension-free positive transverse
variation bound for representative rows.}
}
\]

Everything else in the bridge is already banked:

1. in-class concentration is \(\eta+2\delta\);
2. cross-cluster representative leakage is \(O(\delta)\);
3. scalar coefficient-deficit rows in \(B_\eta\) are \(O(\delta/\eta)\);
4. the rank-2 family shows the \(\sqrt\delta\) scale is sharp;
5. the L4 H-M construction is explicit once (T) is supplied.

The unproved point is precisely the signed affine-face cancellation:
positive representative mass can, in principle, sit on far rows whose
\(\beta_s\)-coordinate is nearly \(1\) and whose other coordinates cancel in
pairs.  Numerics says this cancellation still costs \(O(\delta)\) transverse
positive displacement at max-volume representatives, but the audited toolkit
does not yet prove it.
