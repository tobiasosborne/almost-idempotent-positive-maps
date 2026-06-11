# w19_boundary — DIED-AT: the boundary charge is an upper budget; height cancels (codex, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w19_boundary/brief.md. Artifacts: experiments/out/w19_boundary/.

VERDICT: DIED-AT.

The exact quotient identities are banked, but they do not force the requested boundary-product dichotomy. The failed inequality is:

\[
\|(EC)_{\alpha,*}\|_1 \ge c''\tau
\quad\text{or even}\quad
\|EC\|_{\infty\to1}\ge c''\tau
\]

for a shallow row/component carrying the high-hidden mass.

What the identities do give, clone-invariantly:

\[
B^2-B=-EC,\qquad
B^m-B=-\sum_{r=0}^{m-2}B^rEC,\qquad
\operatorname{tr}B-\operatorname{tr}B^2=\operatorname{tr}(EC).
\]

The charge lands only in the already-known \(v\)-row negative budget:

\[
(Q^+)_{vT}t\le (Q^-)_v g\le \delta\Omega,
\qquad
(Q^+)_{vT}\le 4\tau/\lambda
\]

for \(t=\lambda\kappa\Omega\). This is an upper budget, not a lower bound, and it does not imply \(H\le C\delta\). The height cancels.

Numerics:

| instance | \(H/\tau\) | \(\widetilde\sigma/\tau\) | best \(\Pi/\tau\) | \(m=2\|EC\|_{\infty\to1}/\tau\) |
|---|---:|---:|---:|---:|
| w16_best | 0.01583 | 1.62555 | 9.04e-5 | 0.00297 |
| w17_targeted_best | 0.10019 | 1.54667 | 2.49e-4 | 0.02094 |
| w17_targeted_robust | 0.10000 | 1.55210 | 2.52e-4 | 0.02104 |

No first-horn component attaches: components leak to deep rows and the audited finite-\(\delta\) denominator \(0.85\tau>4\delta\) fails in these certified cases.

Saved artifacts:

- [verdict.md](/tmp/codex-sigma-wall/w19_boundary/verdict.md)
- [boundary_dichotomy.py](/tmp/codex-sigma-wall/w19_boundary/boundary_dichotomy.py)
- [boundary_measurements.json](/tmp/codex-sigma-wall/w19_boundary/boundary_measurements.json)
- [extra_certified_measurements.json](/tmp/codex-sigma-wall/w19_boundary/extra_certified_measurements.json)
- [both_horns_fail_candidate.json](/tmp/codex-sigma-wall/w19_boundary/both_horns_fail_candidate.json)
- [progress.md](/tmp/codex-sigma-wall/w19_boundary/progress.md)

I also ran `python3 -m py_compile boundary_dichotomy.py`.

Calibration after this run:

\[
P(\text{boundary-product dichotomy as stated})\approx0.18,\qquad
P(\text{this closes anti-splitting})\approx0.07.
\]
---
## Appendix: verdict.md (worker long-form, verbatim)

# w19_boundary verdict

VERDICT: DIED-AT.

The quotient semigroup identities are exact and clone-invariant, but they do not
prove the requested dichotomy. The failed step is the lower bound
\[
\|(EC)_{\alpha,*}\|_1\ge c''\tau
\quad\text{or even}\quad
\|EC\|_{\infty\to 1}\ge c''\tau
\]
for a shallow row/component carrying the high-hidden mass. In the certified
antecedent instances, the first horn is unavailable and the \(m=2\) boundary
product is only \(0.003\tau\) to \(0.021\tau\) in max-row \(\ell^1\).

For a quotient split
\[
Q=\begin{pmatrix}B&E\\ C&D\end{pmatrix},\qquad S=S_t,\quad T=S_t^c,
\]
exact idempotence gives
\[
B^2-B=-EC,\qquad
B^m-B=-\sum_{r=0}^{m-2}B^rEC\quad(m\ge2),
\]
and hence
\[
\operatorname{tr}B-\operatorname{tr}B^2=\operatorname{tr}(EC).
\]
Row-wise,
\[
B_{\alpha\beta}-(B^2)_{\alpha\beta}
=\sum_{a\in T}E_{\alpha a}C_{a\beta}.
\]
With \(e=E\mathbf 1_T=\mathbf 1_S-B\mathbf 1_S\),
\[
(B-B^2)\mathbf 1_S=EC\mathbf 1_S=Be.
\]
For the harmonic deficit \(Qg=g\),
\[
(I-B)g_S=Eg_T,\qquad ECg_S=(B-B^2)g_S=BEg_T.
\]

The only clean charge destination for row \(v\) is its already-known negative
budget. If \(g_v=0\), \(g\ge0\), \(g_T\ge t\), and \(t=\lambda\kappa\Omega\),
\[
(Q^+)_{vT}\,t\le (Q^-)_v g\le \delta\Omega,
\qquad
(Q^+)_{vT}\le \frac{4\tau}{\lambda}.
\]
Therefore
\[
\|(EC)_{v,*}\|_1
\le \bigl((Q^+)_{vT}+(Q^-)_{vT}\bigr)(1+2\delta)
\le \left(\frac{4\tau}{\lambda}+\delta\right)(1+2\delta).
\]
This is an upper budget, not a lower bound, and it does not imply
\(H\le C\delta\). The height \(H\) cancels out of the conservation estimate.

Numerical measurements:

| instance | \(\delta\) | \(H/\tau\) | \(\widetilde\sigma/\tau\) | best \(\Pi/\tau\) | \(m=2\ \|EC\|_{\infty\to1}/\tau\) | first horn |
|---|---:|---:|---:|---:|---:|---|
| w16_best | 0.2284002504 | 0.0158336 | 1.62555 | 9.04e-5 | 0.0029709 | no |
| w17_targeted_best | 0.2329335240 | 0.100193 | 1.54667 | 2.49e-4 | 0.0209374 | no |
| w17_targeted_robust | 0.2345924911 | 0.100003 | 1.55210 | 2.52e-4 | 0.0210356 | no |

For the targeted_best band \(S=\{1,2,3,5,6,7\}\), \(T=\{0,4,8,9\}\):
\[
\|EC\|_{\infty\to1}/\tau=0.0209374,\quad
(EC)^+_{\rm total}/\tau=0.0240170,\quad
\operatorname{tr}(EC)=-0.0066090.
\]
The best component has mass from \(v\) equal to \(1.0191\), but it leaks positive
mass \(0.02457\) to \(T\), is not a closed w12 component, and has
\(\Pi/\tau=2.49\times10^{-4}\). At these \(\delta\), the audited denominator
condition \(0.85\tau>4\delta\) also fails, so no finisher can attach.

Random H-M similarity probes:

- 160 sampled; 22 passed the verifier with \(\delta\le0.25\).
- No random probe crossed \(\widetilde\sigma>\tau\).
- The sharpest saved two-horn diagnostic geometry is
  `both_horns_fail_candidate.json` / `both_horns_fail_candidate_matrix.txt`:
  \(\delta=0.0957219\), \(H/\tau=0.29577\),
  \(\widetilde\sigma/\tau=0.00173\), and
  \(\|EC\|_{\infty\to1}/\tau=0.00173\) at \(t=0.5\kappa\Omega\).
  It is not an anti-splitting antecedent because the sigma gate is not crossed.

Saved artifacts:

- `boundary_dichotomy.py`
- `boundary_measurements.json`
- `extra_certified_measurements.json`
- `boundary_summary.txt`
- `both_horns_fail_candidate.json`
- `both_horns_fail_candidate_matrix.txt`

Calibration after this run:

\[
P(\text{boundary-product dichotomy as stated})\approx0.18,\qquad
P(\text{this closes anti-splitting without a new facial/anti-splitting lemma})
\approx0.07.
\]

What remains: a new lower-bound principle must connect high hidden shallow
mass to either positive leakage \(E^+_{S,T}\), positive return \(C^+_{T,S}\),
or one closed quotient component. The boundary identity alone only certifies
the cost after leakage exists; it does not force the leakage.
