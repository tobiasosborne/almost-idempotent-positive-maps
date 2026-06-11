# w30_telescope — DIED-AT: no contraction (coefficient exactly 1); the negative-coefficient interface fact named (codex, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w30_telescope/brief.md. Long form: experiments/out/w30_telescope/proof.md.

VERDICT: DIED-AT.

The telescoping route does not produce a contraction. I wrote the long-form artifact to [proof.md](/tmp/codex-sigma-wall/w30_telescope/proof.md:1), with the exact leak:

\[
aP^+ = P_{u\cdot}+aP^-+bP^+-bP^-,
\]

so the two-step positive expansion returns \(T\) with coefficient \(1\), giving only \(T \le T + O(\delta)\).

The minimal missing max-volume interface is:

\[
\sum_j (P_{u_sj})_+\sum_{t\ne s}(-\beta_t(j))_+ \le C_\mu\delta.
\]

If that lands, the lemma follows with \(C_D=2(1+2\delta_0)(2+C_\mu)\).

Artifacts:
- [proof.md](/tmp/codex-sigma-wall/w30_telescope/proof.md:1)
- [progress.md](/tmp/codex-sigma-wall/w30_telescope/progress.md:1)
- [telescope_audit.py](/tmp/codex-sigma-wall/w30_telescope/telescope_audit.py:1)
- [telescope_numeric_summary.txt](/tmp/codex-sigma-wall/w30_telescope/telescope_numeric_summary.txt:1)

Verification passed:
`python3 -m py_compile telescope_audit.py`
`python3 telescope_audit.py`

No `answer.md` was created.
---
## Appendix: proof.md (verbatim)

# VERDICT: DIED-AT

The representative displacement lemma is still numerically consistent, but the
requested telescoping route R1 does not prove it.  The exact failure is the
two-step positive kernel:

\[
(P_{u\cdot})\,P^+ \quad\text{has no contraction on}\quad
f_j=\|p_j-p_u\|_1.
\]

Idempotence returns the signed two-step kernel to the one-step row, but after
positive/negative decomposition the one-step transport \(T\) reappears with
coefficient exactly \(1\).  The remaining terms are only \(O(\delta)\).  Thus
the route gives

\[
T \le T + O(\delta),
\]

not

\[
T \le aT + O(\delta),\qquad a<1.
\]

Long-form conclusion:

\[
\boxed{\text{R1 DIED-AT: no contraction from the iterated identity alone.}}
\]

Calibration:

\[
P(\text{this DIED-AT survives audit})=0.84,
\qquad
P(\text{the max-volume representative lemma is true})=0.66.
\]

The minimal missing max-volume interface is the coordinate-negative-mass
estimate

\[
\boxed{
\sum_j (P_{u_sj})_+
\sum_{t\ne s}(-\beta_t(j))_+
\le C_\mu \delta
}
\tag{MV-face}
\]

for every maximum-volume pivot \(u_s\), with dimension-free \(C_\mu\).  If
(MV-face) is supplied, the target follows immediately with

\[
C_D=2(1+2\delta_0)(2+C_\mu).
\]

No `answer.md` was created.

## 1. Setup And Imported Audited Facts

Assume

\[
P^2=P,\qquad P{\bf 1}={\bf 1},\qquad
\nu_i:=\sum_j(-P_{ij})_+\le\delta\le\delta_0.
\]

Put

\[
R:=1+2\delta,\qquad D:=2R=2+4\delta.
\]

Then every row \(p_i\) satisfies

\[
\|p_i\|_1\le R,
\qquad
\|p_i-p_j\|_1\le D.
\]

Choose the audited maximum-volume actual-row basis

\[
r_s=p_{u_s},\qquad s=1,\ldots,k.
\]

The w26 audit gives coordinates

\[
p_i=\sum_s\beta_s(i)r_s,\qquad
P\beta_s=\beta_s,\qquad
\sum_s\beta_s(i)=1,
\]

with

\[
|\beta_s(i)|\le1,\qquad
\|\beta_s\|_{(V,\|\cdot\|_1)^*}\le1.
\]

Fix a representative row \(u=u_s\).  Write

\[
f_i:=\|p_i-p_u\|_1,\qquad
a_i:=(P_{ui})_+,\qquad
b_i:=(-P_{ui})_+.
\]

The target is

\[
T:=\sum_i a_i f_i \le C_D\delta.
\]

The free vector identity is exact:

\[
\sum_i P_{ui}(p_i-p_u)=0.
\]

Therefore

\[
\left\|\sum_i a_i(p_i-p_u)\right\|_1
=
\left\|\sum_i b_i(p_i-p_u)\right\|_1
\le D\nu_u
\le D\delta.
\]

This is sharp but vector-valued.  It does not control the sum of norms \(T\),
because positive displacements can cancel.

## 2. The Almost-Subharmonicity Is Correct

For any row \(i\),

\[
p_i-p_u=\sum_l P_{il}(p_l-p_u),
\]

because \(P^2=P\) and row sums are \(1\).  Splitting the row into positive and
negative parts gives

\[
f_i
\le
\sum_l (P_{il})_+ f_l
+
\sum_l (-P_{il})_+ f_l.
\]

Since \(f_l\le D\),

\[
\boxed{
f_i\le \sum_l (P_{il})_+ f_l+D\nu_i.
}
\tag{2.1}
\]

Multiplying (2.1) by \(a_i\) and summing over \(i\),

\[
T
\le
\sum_l\left(\sum_i a_i(P_{il})_+\right)f_l
+
D\sum_i a_i\nu_i.
\tag{2.2}
\]

Since \(\sum_i a_i=1+\nu_u\le1+\delta\),

\[
D\sum_i a_i\nu_i\le D(1+\delta)\delta.
\tag{2.3}
\]

Thus the only possible source of contraction is the two-step positive kernel

\[
c_l:=\sum_i a_i(P_{il})_+.
\]

## 3. Exact Two-Step Decomposition

Let

\[
P^+:=((P_{ij})_+),\qquad P^-:=((-P_{ij})_+).
\]

For the representative row,

\[
P_{u\cdot}=a-b.
\]

Idempotence says

\[
(a-b)(P^+-P^-)=P_{u\cdot}=a-b.
\]

Hence

\[
\boxed{
aP^+
=
P_{u\cdot}
+aP^-
+bP^+
-bP^-.
}
\tag{3.1}
\]

Pairing (3.1) with \(f\) gives

\[
\sum_l c_l f_l
=
T-\sum_l b_l f_l
+\sum_{i,l}a_i(P_{il})_-f_l
+\sum_{i,l}b_i(P_{il})_+f_l
-\sum_{i,l}b_i(P_{il})_-f_l.
\tag{3.2}
\]

The desired \(T\) appears on the right with coefficient exactly \(1\).  The
two negative terms in (3.2) are useful only if they capture a definite fraction
of \(T\).  They do not do so uniformly.  In particular, a representative row
may have \(\nu_u=0\) and still have \(T>0\), because the cancellation is
performed by positive mass on signed-face successor rows whose own rows carry
the negative mass.

Dropping the negative terms in (3.2) gives only

\[
\sum_l c_l f_l
\le
T
+D(1+\delta)\delta
+D\delta(1+\delta).
\tag{3.3}
\]

Combining (2.2), (2.3), and (3.3),

\[
\boxed{
T\le T+3D(1+\delta)\delta.
}
\tag{3.4}
\]

This is the exact leak.  The signed identity is doing all it can; after taking
positive parts, it returns \(T\) rather than a strict fraction of \(T\).

## 4. Why Iterating Does Not Repair It

Iterating (2.1) with \(A=P^+\) gives, for every fixed \(m\),

\[
T
\le
aA^m f
+
D\sum_{r=0}^{m-1} aA^r\nu.
\tag{4.1}
\]

The signed kernel satisfies \(P^m=P\), but \(A^m\) is not controlled by this in
a contractive way.  The positive row sums are \(1+\nu_i\), so \(A^m\) may
preserve or increase the \(f\)-mass before the signed cancellations are
reintroduced.

For fixed \(m\), expanding \(A^m\) into signed and negative-part terms again
returns \(T+O_m(\delta)\), not \(aT+O_m(\delta)\).  Taking large \(m\) only
increases the accumulated error in (4.1), unless one already has an independent
return-to-class or signed-face estimate.  That independent estimate is exactly
what R1 was supposed to produce.

The cluster split also does not close the argument.  With

\[
M_s(\eta)=\{j:\|p_j-p_u\|_1\le\eta\},
\]

Markov gives only

\[
\sum_{j\notin M_s(\eta)}a_j\le {T\over\eta}.
\]

The w27 leakage family has positive off-cluster mass \(\delta/\eta\), and at
\(\eta=\sqrt\delta\) this is \(\sqrt\delta\).  This is compatible with
\(T=O(\delta)\), but it prevents a proof based on \(O(\delta)\) support
concentration.  Feeding \(M\le T/\eta\) into a term \(O(\eta M)\) gives back
an \(O(T)\) term, with no strict coefficient.

## 5. The Coordinate Reduction And The Minimal Missing Fact

The max-volume chart does give a clean reduction of the target to one missing
dimension-free face estimate.

Fix \(u=u_s\) and define

\[
\lambda_j:=1-\beta_s(j),
\qquad
\mu_j:=\sum_{t\ne s}(-\beta_t(j))_+.
\]

Because \(|\beta_s(j)|\le1\), we have

\[
0\le\lambda_j\le2.
\]

The scalar fixed-coordinate identity gives

\[
\sum_jP_{uj}\lambda_j=0.
\]

Therefore

\[
\sum_j a_j\lambda_j
=
\sum_j b_j\lambda_j
\le
2\nu_u
\le2\delta.
\tag{5.1}
\]

Also,

\[
p_j-r_s
=
(\beta_s(j)-1)r_s+\sum_{t\ne s}\beta_t(j)r_t.
\]

Since \(\sum_t\beta_t(j)=1\), the off-\(s\) positive coordinate mass is
\(\lambda_j+\mu_j\), and the off-\(s\) total variation is
\(\lambda_j+2\mu_j\).  Hence

\[
\|p_j-r_s\|_1
\le
R\left(\lambda_j+\lambda_j+2\mu_j\right)
=
2R(\lambda_j+\mu_j).
\tag{5.2}
\]

Multiplying (5.2) by \(a_j\) and summing,

\[
T
\le
2R\sum_j a_j\lambda_j
+
2R\sum_j a_j\mu_j
\le
4R\delta
+
2R\sum_j a_j\mu_j.
\tag{5.3}
\]

Thus the representative displacement lemma follows immediately from

\[
\sum_j a_j\mu_j\le C_\mu\delta.
\tag{MV-face}
\]

Indeed, for \(\delta\le\delta_0\),

\[
T
\le
2(1+2\delta_0)(2+C_\mu)\delta.
\]

This is the precise interface fact that the sibling max-volume route would
need to supply.  It is also the exact signed-face gap already visible in w27
and w29: the scalar coordinate loss \(\lambda_j\) controls rows that leave the
representative coordinate, but it is blind to rows with

\[
\beta_s(j)\approx1,\qquad
\sum_{t\ne s}\beta_t(j)\approx0,
\qquad
\mu_j>0.
\]

Those rows can be far from \(r_s\) by transverse \(+/-\) coordinates while
keeping the \(s\)-coordinate fixed.

## 6. Numerical Audit

Artifacts produced here:

```text
telescope_audit.py
telescope_numeric_results.json
telescope_numeric_summary.txt
telescope_run.log
progress.md
proof.md
```

Verification commands:

```text
python3 -m py_compile telescope_audit.py
python3 telescope_audit.py
```

Both completed cleanly.

The script checks the w27 rank-2 leakage family, split-block family, w19
leftcone family, transverse-pair signed-face family, certified w16/w17
instances, and 36 random small-\(\delta\) exact similarities.

Numerical facts:

```text
max two-step decomposition residual: 2.220446049250313e-16
subharmonic max violation: 0 up to roundoff in all reported families
```

Representative pivot transport remained linear in all tested cases:

```text
w27 rank-2, delta=1e-5:       T/delta=2.00002
split block, eps=1e-5:        T/delta=2.00002
w19 leftcone, eps=1e-5:       T/delta=1.33335
transverse pair, a=0.02:      T/delta=2.0592 for the signed-face pivot
w16/w17 certified instances:  T/delta=2.37--2.43 above the small corner
random small-delta samples:   max T/delta=3.1529, median T/delta=1.97314
```

But the positive iterates did not contract:

```text
w27 rank-2, delta=1e-5:       S2/T=1.99685, (P^+)^8 ratio=8.97478
split block, eps=1e-5:        S2/T=1.5,     (P^+)^8 ratio=5
w19 leftcone, eps=1e-5:       S2/T=2,       (P^+)^8 ratio=9.00018
transverse pair, a=0.02:      S2/T=1.96154, (P^+)^8 ratio=8.72474
random small-delta samples:   max S2/T=2.00304, median S2/T=1.64143
```

The transverse-pair family isolates the signed-face leak.  For \(a=0.02\) and
\(m=0.99\), the max-volume pivot \(u=0\) has

```text
T/delta = 2.0592
lambda positive average / delta = -5.6e-15
mu positive average / delta = 0.991584
S2/T = 1.961538
(P^+)^8 ratio = 8.724743
```

Thus the displacement is generated almost entirely by coordinate negative
mass \(\mu\), while the visible representative-coordinate loss \(\lambda\) is
zero at numerical precision.  This is not a counterexample to the lemma.  It is
the minimal obstruction to the telescoping proof.

## 7. Final Status

What R1 proves:

\[
f_i\le\sum_l(P_{il})_+f_l+D\nu_i,
\]

\[
T\le T+3D(1+\delta)\delta,
\]

and the conditional reduction

\[
\left[
\sum_j (P_{u_sj})_+
\sum_{t\ne s}(-\beta_t(j))_+
\le C_\mu\delta
\right]
\Longrightarrow
\left[
T\le 2(1+2\delta_0)(2+C_\mu)\delta
\right].
\]

What R1 does not prove:

\[
T\le aT+b\delta,\qquad a<1.
\]

Exact leak:

\[
aP^+=P_{u\cdot}+aP^-+bP^+-bP^-,
\]

so the two-step positive expansion returns \(T\) with coefficient \(1\).
Neither class concentration nor finite iteration changes that without an
extra signed-face/max-volume input.

Minimal interface to continue:

\[
\sum_j (P_{u_sj})_+
\sum_{t\ne s}(-\beta_t(j))_+
\le C_\mu\delta
\]

dimension-free for maximum-volume pivots.
