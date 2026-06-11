# VERDICT: DIED-AT FOR THE MAX-VOLUME REPRESENTATIVE LEMMA

There is a simple counterexample to the **general-row** version, even at
`delta=0`.  Thus the lemma cannot be stated for an arbitrary row.  I did not
find a counterexample to the intended max-volume representative version, but I
also did not prove it.

Calibration:

\[
P(\text{general-row counterexample survives audit})=0.99,
\qquad
P(\text{this representative DIED-AT survives audit})=0.78,
\qquad
P(\text{representative lemma is true})=0.62.
\]

No `answer.md` was created.

## 1. The General-Row Version Is False

Take the exact stochastic idempotent

\[
P=
\begin{pmatrix}
1&0&0\\
0&1&0\\
1/2&1/2&0
\end{pmatrix}.
\]

Then \(P^2=P\), \(P{\bf 1}={\bf 1}\), and every row has negative mass \(0\).
For the transient row \(u=3\),

\[
p_u=\frac12 p_1+\frac12 p_2,
\qquad
\|p_1-p_u\|_1=\|p_2-p_u\|_1=1.
\]

Hence

\[
\sum_j (P_{uj})_+\,\|p_j-p_u\|_1=1
\]

while \(\delta=0\).  This does not refute the application, because the
maximum-volume representatives are rows \(1\) and \(2\), and their transport
cost is \(0\).

The numerical audit also shows why the representative hypothesis is essential:
in the w27 rank-2 family the pivot ratio tends to \(2\), but a non-pivot row has
\(T/\delta\) growing like a negative power of \(\delta\).

## 2. Free Identity

For every row \(u\), idempotence and row sums give

\[
\sum_j P_{uj}p_j=(P^2)_{u\cdot}=p_u,\qquad \sum_jP_{uj}=1.
\]

Therefore

\[
\sum_jP_{uj}(p_j-p_u)=0.
\]

Writing \(P_{uj}=a_j-b_j\), with \(a_j=(P_{uj})_+\) and
\(b_j=(P_{uj})_-\), this is

\[
\sum_j a_j(p_j-p_u)=\sum_j b_j(p_j-p_u).
\]

Since every row has \(\ell^1\)-norm at most \(1+2\delta\),

\[
\|p_j-p_u\|_1\le 2+4\delta,
\]

and hence

\[
\left\|\sum_j a_j(p_j-p_u)\right\|_1
\le (2+4\delta)\nu_u
\le (2+4\delta)\delta.
\]

The vector estimate is exact and dimension-free.  It does not control

\[
T_u:=\sum_j a_j\|p_j-p_u\|_1,
\]

because the positive vector displacements may cancel.

## 3. Representative Setup

For the intended application, choose actual rows

\[
r_s=p_{u_s},\qquad s=1,\ldots,k,
\]

forming a maximum-volume row basis.  The audited w26 chart gives exact
coordinates

\[
p_i=\sum_s\beta_s(i)r_s,\qquad P\beta_s=\beta_s,\qquad
\sum_s\beta_s(i)=1,
\]

with

\[
|\beta_s(i)|\le 1,\qquad
\|\beta_s\|_{(V,\|\cdot\|_1)^*}\le 1.
\]

For a pivot \(u_s\), the fixed-coordinate identity gives

\[
\sum_j P_{u_sj}\bigl(1-\beta_s(j)\bigr)=0,
\]

and, because \(0\le 1-\beta_s(j)\le 2\),

\[
\sum_{P_{u_sj}>0}P_{u_sj}\bigl(1-\beta_s(j)\bigr)\le 2\delta.
\tag{3.1}
\]

This controls all positive successor rows that lose visible \(s\)-coordinate.
The remaining obstruction is the signed face

\[
\beta_s(j)\approx 1,\qquad
\sum_{t\ne s}\beta_t(j)\approx 0,
\]

where \(p_j-p_{u_s}\) is produced by transverse \(+/-\) coordinates.

Equivalently, the missing estimate is

\[
\sum_j(P_{u_sj})_+\,
\mu_j
\le C\delta,
\qquad
\mu_j:=\sum_t(-\beta_t(j))_+.
\tag{3.2}
\]

If (3.2) were known, the displacement lemma would follow from clipping the
coefficient vector to the simplex and using the row norm bound
\(\|r_s\|_1\le 1+2\delta\).  I could not derive (3.2).

## 4. Route R1: Iterated Identity Fails At The Contraction Step

Let

\[
f_i=\|p_i-p_u\|_1,\qquad a_i=(P_{ui})_+.
\]

For every row \(i\),

\[
p_i-p_u=\sum_lP_{il}(p_l-p_u).
\]

With \(D:=2+4\delta\) this gives the localized inequality

\[
f_i\le \sum_l(P_{il})_+f_l + D\nu_i.
\tag{4.1}
\]

Multiplying by \(a_i\) and summing,

\[
T_u
\le
\sum_l\left(\sum_i a_i(P_{il})_+\right)f_l
+D\sum_i a_i\nu_i.
\tag{4.2}
\]

The two-step positive-positive coefficient is

\[
c_l:=\sum_i a_i(P_{il})_+.
\]

Idempotence only says that the signed two-step coefficient returns to
\(P_{ul}\):

\[
P_{ul}=\sum_iP_{ui}P_{il}.
\]

After expanding into positive and negative parts, (4.2) gives only

\[
T_u\le T_u+O(\delta).
\]

There is no self-improving inequality \(T_u\le aT_u+b\delta\) with
\(a<1\).  The rank-2 saturating family explains the obstruction: the positive
two-step mass can reproduce the one-step positive transport at full first
order.

## 5. Route R2: Functional Split Stops At Sign Variation

For any fixed \(\phi\in[-1,1]^n\),

\[
\left|\sum_j(P_{uj})_+\langle\phi,p_j-p_u\rangle\right|
\le (2+4\delta)\delta
\]

by the free identity.  The desired scalar quantity is instead

\[
\sum_j(P_{uj})_+\sup_{\phi_j\in[-1,1]^n}
\langle\phi_j,p_j-p_u\rangle,
\]

where the optimizing sign vector may vary with \(j\).

The maximum-volume chart reduces this to a low-dimensional coordinate problem,
but the fixed coordinate identities still allow transverse pairs of the form

\[
\beta(j_\pm)=e_s\pm a(e_t-e_r).
\]

Their coordinate average is exactly \(e_s\), while their absolute coordinate
variation is \(2a\).  The missing input is not dimension-counting; it is a
dimension-free way to charge the average negative coordinate mass to row
negative mass.  I did not find such a charge.

## 6. Route R3: Second Moments Are The Wrong Scale By Themselves

The Cauchy-Schwarz route gives

\[
T_u^2\le \left(\sum_j(P_{uj})_+\right)
\left(\sum_j(P_{uj})_+f_j^2\right).
\]

To prove \(T_u=O(\delta)\) from this alone one would need a second moment of
order \(O(\delta^2)\).  The examples do not have that scale uniformly.

Measured pivot values:

```text
w27 rank-2:       T/delta -> 2,     M2/delta -> 0
split block:      T/delta -> 2,     M2/delta -> 0
w19 leftcone:     T/delta -> 4/3,   M2/delta -> 8/3
transverse pair:  T/delta ~ 2.08 at delta~0.02, M2/delta ~ 4.17
w16/w17:          T/delta ~ 2.37--2.43, M2/delta ~ 5.65--5.81
```

Thus second moments are useful diagnostics, but the plain Cauchy route gives
only a \(\sqrt{\delta}\)-type estimate in the cases where \(M_2=O(\delta)\).

## 7. Transverse-Pair Stress Family

The most direct attempted conspiracy uses exact \(P=LB\), \(BL=I\), with
coordinate rows

\[
e_0,\ e_1,\ e_2,\ e_0+a(e_1-e_2),\ e_0-a(e_1-e_2).
\]

For \(m\in(0,1)\) and

\[
c=\frac{a}{1+4a^2},
\]

take

\[
B_0=(1-m,0,0,m/2,m/2),
\]
\[
B_1=(0,1-2ac,2ac,c,-c),
\qquad
B_2=(0,2ac,1-2ac,-c,c).
\]

Then \(P=LB\) is exactly idempotent and row-stochastic.  The representative
row \(0\) sends positive mass \(m/2,m/2\) to the two transverse rows, whose
vector displacements cancel.  For small \(a\), however, the maximum row
negative mass is \(\delta\sim a\), and the representative transport is only
\(\sim 2m\delta\).  Numerically, with \(m=0.99\):

```text
a=0.02: delta=0.0199681, pivot T/delta=2.08307
a=0.05: delta=0.0495050, pivot T/delta=2.21782
a=0.10: delta=0.0961538, pivot T/delta=2.46154
a=0.20: delta=0.172414,  pivot T/delta=2.96552
```

The same model can reach ratios above \(5\) only at large negative mass
around \(\delta=0.2\), outside the small-corner regime relevant to the bridge.

## 8. Numerical Audit

Artifacts in this workdir:

```text
displacement_audit.py
displacement_numeric_results.json
displacement_numeric_summary.txt
progress.md
proof.md
```

Verification:

```text
python3 -m py_compile displacement_audit.py
python3 displacement_audit.py
```

Both commands completed cleanly.

Summary of representative pivot ratios:

```text
general-row delta=0 transient: pivot ratio 0, non-pivot row ratio infinite
w27 rank-2 leakage:            pivot T/delta -> 2
split block:                   pivot T/delta -> 2
w19 leftcone:                  pivot T/delta -> 4/3
transverse-pair stress:         pivot T/delta 2.08 at delta~0.02
w16/w17 certified instances:    pivot T/delta 2.37--2.43
random small-delta similarities:
  samples=36
  median pivot T/delta=2.03808
  p90 pivot T/delta=2.884
  max pivot T/delta=3.56927
```

No tested max-volume representative violates an \(O(\delta)\) law.  Arbitrary
non-representative rows violate it strongly.

## 9. Conditional Handoff To w28

If the max-volume representative displacement lemma is later proved with
constant \(C_D\), then the w28 Markov step follows immediately.  For

\[
M_s=\{j:\|p_j-p_{u_s}\|_1\le\eta\},
\]

every \(j\notin M_s\) has displacement \(>\eta\), so

\[
\sum_{\substack{j\notin M_s\\P_{u_sj}>0}}P_{u_sj}
\le
\frac{1}{\eta}
\sum_j(P_{u_sj})_+\|p_j-p_{u_s}\|_1
\le
\frac{C_D\delta}{\eta}.
\]

The negative part contributes at most \(\delta\).  Hence the full off-cluster
\(\ell^1\)-mass obeys

\[
\sum_{j\notin M_s}|P_{u_sj}|
\le
\frac{C_D\delta}{\eta}+\delta
\le
(C_D+1)\left(\eta+\frac{\delta}{\eta}\right)
\]

for \(0<\eta\le1\).  If \(C_D\) is reserved only for the positive part, the
full-face constant is \(C_D+1\); if the lemma's constant is enlarged by one,
this is the advertised w28 face estimate with the same displayed constant.

I did not assemble the global theorem.
