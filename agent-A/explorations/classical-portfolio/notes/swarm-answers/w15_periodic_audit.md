# w15_periodic_audit — the periodicity-exclusion patch HOLDS (codex hostile audit, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w15_periodic_audit/brief.md

**VERDICT: PATCH HOLDS, with caveats.** The periodic-exclusion argument is valid for a **closed w12 positive component** in the row-sum norm, and \(d=2\) is not a surviving case. The \(N^2\) term is harmless because it is nonnegative. The patch does **not** discharge the separate analytic band-closure caveat in [kernel-conjecture.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex:261).

Central derivation, with \(T=C_{r+2}\):

\[
B^2=(A-N)^2=A^2-AN-NA+N^2 .
\]

For a closed periodic component,

\[
\sum_{j\in T}(A^2)_{ij}
=
\sum_{k\in C_{r+1}}A_{ik}d_k
\ge
\sum_{k\in C_{r+1}}A_{ik}
=d_i
\ge1 .
\]

The mixed terms satisfy, in max-row-sum norm,

\[
\sum_{j\in T}(AN)_{ij}\le \delta(1+\delta),
\qquad
\sum_{j\in T}(NA)_{ij}\le \delta(1+\delta),
\]

and \(N^2\ge0\), hence

\[
\sum_{j\in T}(B^2)_{ij}
\ge
1-2\delta(1+\delta).
\]

Since \(A_{iT}=0\), also \(B_{iT}\le0\), so

\[
\sum_{j\in T}(B^2)_{ij}
\le
\sum_{j\in T}B_{ij}+\|B^2-B\|
\le \zeta .
\]

Thus

\[
1\le 2\delta(1+\delta)+\zeta
\le 2\delta(1+\delta)+\delta(1+2\delta)
=3\delta+4\delta^2 .
\]

The exact threshold from this proof is

\[
3\delta+4\delta^2<1
\iff
\delta<\frac14 .
\]

Strictness is fine: at \(\delta=1/4\) equality is possible in the bound, but the patch assumes \(\delta<1/4\).

**d=2:** not broken. For a genuine period-2 irreducible nonnegative support, the cyclic decomposition has edges only \(C_r\to C_{r+1}\). Since \(C_{r+2}=C_r\), this still forbids \(C_r\to C_r\). In particular \(A_{ii}=0\); if \(B_{ii}>0\), then \(A_{ii}>0\), giving a self-loop and period \(1\). So \(B_{iT}\le0\) still holds.

**Norms:** the proof uses the campaign’s max-row-sum / row-vector \(\ell^1\) operator norm. This matches [w12_comp_finisher.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/swarm-answers/w12_comp_finisher.md:11) and the row negative-mass convention in [kernel-conjecture.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex:55). With exact positive band closure,

\[
B^2-B=-P_{S,S^c}P_{S^c,S},
\qquad
\zeta\le \delta(1+2\delta).
\]

**Component-definition check:** the patch matches w12 only if “component” means a closed positive component with \(d_i=\sum_{j\in C}A_{ij}\in[1,1+\delta]\), as in [w12_comp_finisher.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/swarm-answers/w12_comp_finisher.md:17). It does **not** automatically apply to an arbitrary carrier SCC from [kernel-conjecture.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex:233), because analytic positive closure is still open.

The finisher display is inherited correctly, but needs the small-\(\delta\) denominator condition:

\[
R_C=4\delta+\frac{2(1+\delta)\varepsilon}{\theta_C},
\qquad
\varepsilon=\zeta+6\delta+4\delta^2.
\]

If \(R_C\ge r_*=0.85\sqrt\delta\), then

\[
\theta_C\le \frac{2(1+\delta)\varepsilon}{r_*-4\delta}
\]

only when

\[
r_*>4\delta
\iff
\delta<\left(\frac{0.85}{4}\right)^2
=\frac{289}{6400}\approx0.04516.
\]

Then

\[
\Pi_C\le E_L(\delta,\zeta)+\frac{2(1+\delta)\varepsilon}{r_*-4\delta}.
\]

For approximate positive leakage \(\eta\), the clean condition is

\[
(1-\eta)^2>2\delta(1+\delta)+\zeta .
\]

If \(\zeta\le\delta(1+2\delta)\) is still available, this is

\[
\eta<1-\sqrt{3\delta+4\delta^2}.
\]

If the same leakage also worsens band closure so that \(\zeta\le(\delta+\eta)(1+2\delta)\), a sufficient rowwise tolerance is

\[
\eta<
\frac{3+2\delta-\sqrt{5+24\delta+20\delta^2}}{2}.
\]

The refuter periodic templates are accounted for: they are not closed w12 components with \(d_i\ge1\); their period-two mass is small or leaks into the frame/archetype structure.

Calibrated \(P(\)this verdict survives further audit\()\): **0.87**.