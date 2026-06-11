# w15_periodic — w12 finisher primitivity gap CLOSED (codex, 2026-06-11) [pending w15_periodic_audit]
# Brief: /tmp/codex-sigma-wall/w15_periodic/brief.md

VERDICT: GAP CLOSED.

The periodic gap is vacuous under the actual w12 component hypotheses. No \(d\)-power/Cesaro bookkeeping is needed; exact idempotence already kills nontrivial period by a two-step argument.

**Patch Statement**

Let \(P\mathbf 1=\mathbf 1\), \(P^2=P\), and \(\delta(P)=\delta<1/4\). In the w12/d14 band write

\[
B=P_{SS}=A-N,\qquad A=B^+,\quad N=B^-,
\]

with

\[
\|N\|\le\delta,\qquad \|A\|\le 1+\delta,\qquad
\zeta:=\|B^2-B\|\le \delta(1+2\delta).
\]

Let \(C\) be a w12 positive component, meaning positive mass from rows of \(C\) stays in \(C\), so

\[
d_i:=\sum_{j\in C}A_{ij}\in[1,1+\delta].
\]

If \(C\) is strongly connected, then \(C\) has period \(1\). Hence every w12 component is aperiodic/primitive in the small-\(\delta\) regime, and the existing primitive finisher applies unchanged.

With

\[
\varepsilon=\zeta+6\delta+4\delta^2,
\]

and

\[
E_L(\delta,\zeta)
=
L\delta(1+2\delta)^{L-1}
+\zeta\sum_{r=0}^{L-2}(1+2\delta)^r,
\]

the patched finisher is:

\[
R_C
=
4\delta+\frac{2(1+\delta)\varepsilon}{\theta_C}.
\]

If \(R_C<r_*=0.85\sqrt\delta\), the component collapses to a near equal-input cluster and is exposed by the audited consumer. Otherwise,

\[
\Pi_C
\le
E_L(\delta,\zeta)
+
\frac{2(1+\delta)\varepsilon}{r_*-4\delta}.
\]

So the only survivor is still the w12 long-thin inequality. There is no additional periodic survivor class.

**Periodic Exclusion Proof**

Assume for contradiction that \(C\) has period \(d\ge2\), with cyclic classes

\[
C_0,\dots,C_{d-1},
\]

and positive edges only \(C_r\to C_{r+1}\). Fix \(i\in C_r\) and set \(T=C_{r+2}\) modulo \(d\). Since \(d\ge2\), direct positive edges \(C_r\to T\) are forbidden, so

\[
A_{iT}=0,\qquad B_{iT}\le0.
\]

But two positive steps from \(i\) land in \(T\). Thus

\[
\sum_{j\in T}(A^2)_{ij}
=
\sum_{k\in C_{r+1}} A_{ik}\sum_{j\in T}A_{kj}
=
\sum_{k\in C_{r+1}} A_{ik}d_k
\ge
\sum_{k\in C_{r+1}}A_{ik}
=d_i
\ge1.
\]

Since \(B=A-N\),

\[
\sum_{j\in T}(B^2)_{ij}
\ge
1-2\delta(1+\delta).
\]

On the other hand, \(\|B^2-B\|\le\zeta\) and \(B_{iT}\le0\), so

\[
\sum_{j\in T}(B^2)_{ij}
\le
\sum_{j\in T}B_{ij}+\zeta
\le
\zeta.
\]

Therefore

\[
1\le 2\delta(1+\delta)+\zeta
\le 2\delta(1+\delta)+\delta(1+2\delta)
=3\delta+4\delta^2.
\]

This contradicts \(\delta<1/4\). Hence no nontrivial periodic w12 component exists.

The signed carrier can only evade this by not being a closed w12 component, i.e. by putting substantial positive mass outside the cyclic block. That is exactly the refuter’s observed dichotomy, not a new finisher gap.

Calibrated \(P(\)patch survives hostile audit\()\): **0.92**.