# w18_variety — the tangent-cone/normal-cone program; exact charts; dimension counts (codex research, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w18_variety/brief.md.

**Verdict**
Top pick: attack the **linear law as a normal-cone statement on the idempotent variety**, not as another hiddenness LP argument. The current dossier shows hiddenness keeps pulling proofs back into the exposedness LP frame; the variety lens gives a way to avoid that.

| rank | attack plan | first lemma to prove | P(new proved lemma in one wave) |
|---:|---|---|---:|
| 1 | **Curve-selection / normal-cone proof of the linear law** | \[
\dot H_{P_0}(A)\le C\,\dot\delta_{P_0}(A)
\] for every H-M stratum point \(P_0\) and tangent \(A\in T_{P_0}\mathcal I^1_{n,k}\), with \(\dot\delta_{P_0}(A)=\max_i\sum_{j:P_{0,ij}=0}(-A_{ij})_+\). | 0.68 |
| 2 | **Riccati-corner local model around H-M normal forms** | \[
H(P(C,D))\le C\,\delta(P(C,D))+O(\|(C,D)\|^2)
\] in the exact idempotent chart, uniformly over partition strata. | 0.58 |
| 3 | **Quotient anti-splitting from exact idempotence** | \[
A_v(S_t\setminus C_W)\ge c\tau\quad\Longrightarrow\quad \exists\text{ closed quotient SCC }\mathcal C:\ A_v(\mathcal C)\ge c'\tau
\] unless \(H\le C\delta\). | 0.36 |

Calibrated \(P\)(at least one plan produces a genuinely new proved lemma within one wave): **0.82**.  
Calibrated \(P\)(one of these closes the full linear law without a new external idea): **0.27**.

**Dead-End Evasion**
| plan | LP-frame collapse | anti-splitting | clone-invariance |
|---|---|---|---|
| 1 | Avoids hiddenness as an input; starts from \(\delta=0\) normal geometry. | Converts splitting into a leading analytic arc; if splitting is real, it appears in the tangent cone. | Uses row geometry, not atom path-products. |
| 2 | Uses exact \(P^2=P\) coordinates before any exposedness LP. | Measures whether many shallow classes are tangent or normal to the H-M locus. | Exact row-class quotient/cluster version fits naturally. |
| 3 | Still touches hiddenness, but only after quotienting and using \(Q^2=Q\). | Directly targets the recorded w16 died-at. | Built on the quotient carrier graph, so exact cloning is neutralized. |

**Structure**
Let
\[
\mathcal I^1_{n,k}=\{P\in\mathbb R^{n\times n}:P^2=P,\ P\mathbf1=\mathbf1,\ \operatorname{rank}P=k\}.
\]
All rank-\(k\) idempotents are similar to \(\operatorname{diag}(I_k,0)\). With \(P\mathbf1=\mathbf1\), the acting group is
\[
G_{\mathbf1}=\{S\in GL_n:S\mathbf1=\mathbf1\}.
\]
It acts transitively on \(\mathcal I^1_{n,k}\). If \(E=\operatorname{im}P\), \(F=\ker P\), \(\mathbf1\in E\), then the stabilizer is \(GL(E)_{\mathbf1}\times GL(F)\). Hence
\[
\dim \mathcal I^1_{n,k}
=(n^2-n)-((k^2-k)+(n-k)^2)
=(n-k)(2k-1).
\]

Differentiating \(P^2=P\) gives
\[
PA+AP=A.
\]
In \(V=E\oplus F\), with \(P=\begin{pmatrix}I&0\\0&0\end{pmatrix}\),
\[
A=\begin{pmatrix}0&C\\D&0\end{pmatrix}.
\]
The row-stochastic slice adds \(A\mathbf1=0\), i.e. \(D\mathbf1=0\). Thus
\[
T_P\mathcal I^1_{n,k}=P\,X(I-P)+(I-P)YP,\qquad (I-P)YP\mathbf1=0.
\]

A useful exact chart near \(P_0\) is obtained by taking the new image as \(\operatorname{graph}D:E\to F\) and the new kernel as \(\operatorname{graph}(-C):F\to E\):
\[
P(C,D)=
\begin{pmatrix}
(I+CD)^{-1} & (I+CD)^{-1}C\\
D(I+CD)^{-1} & D(I+CD)^{-1}C
\end{pmatrix},
\qquad D\mathbf1=0.
\]
The off-diagonal blocks are first order; the diagonal deviations are quadratic:
\[
P_{EE}-I=-CD+O(3),\qquad P_{FF}=DC+O(3).
\]
This is the exact place where the unused quadratic constraint \(P^2=P\) lives.

The \(\delta=0\) locus is the H-M stochastic-idempotent normal form. For a partition into recurrent blocks \(C_1,\dots,C_k\) and transient set \(T\),
\[
p_i=\pi_s\quad(i\in C_s),\qquad
p_i=\sum_s\alpha_{is}\pi_s\quad(i\in T),
\]
where \(\pi_s\) is a probability row supported on \(C_s\), \(\alpha_i\in\Delta_{k-1}\), and transient columns vanish. This gives a finite semialgebraic stratification by partition data. For a fixed stratum with \(t=|T|\), the parameter dimension is
\[
\sum_s(|C_s|-1)+t(k-1)=n-k+t(k-2).
\]

Normal geometry: at such a \(P_0\),
\[
\delta(P_0+tA+O(t^2))
=t\max_i\sum_{j:P_{0,ij}=0}(-A_{ij})_+ + O(t^2).
\]
So directions that create negative mass at active zero entries pay linearly. The linear law \(H\le C\delta\) is exactly the claim that every first-order direction producing visible-hull height also pays this normal cost. If a counterexample exists, semialgebraic curve selection should give an analytic arc with \(\delta=o(H)\); its leading term must be a tangent-cone direction with \(\dot\delta=0\) but \(\dot H>0\). That is the cleanest target.

**Small Cases**
Rank 1, any \(n\): \(P=\mathbf1\pi^T\), \(\pi^T\mathbf1=1\). All rows coincide, \(P^2=P\), and \(H=0\) even if \(\pi\) has negative entries.

\(n=2,k=2\): only \(P=I\). No deformation, no hidden geometry.

\(n=3,k=2\): every rank-two point can be written
\[
P=I-uv^T,\qquad v^T u=1,\quad v^T\mathbf1=0.
\]
This is a 3-dimensional row-stochastic idempotent variety; the nonnegative normal-form strata are 1-dimensional. Thus the first nontrivial normal directions already appear here, and they are exactly the directions the tangent-cone lemma should detect.

**Certified Instance Check**
The w16 rational instance is in the pivot chart \(P=\Lambda B\), \(B\Lambda=I\), with \(n=7,k=4\). It has \(W=\{0,1,2,3\}\), hidden top \(v=4\),
\[
\delta=0.2284002679,\quad \tau=0.4779124,\quad H/\tau=0.015833,\quad \widetilde\sigma_v/\tau=1.62555.
\]
So high invisible mass can live almost tangent to the \(H=0\) locus. This kills height-free sigma barriers and supports focusing on \(H\) as the normal displacement. All rows are distinct, so exact quotienting does nothing here; cloning this instance would preserve \(H,\delta,\widetilde\sigma\) while destroying raw atom path-products, confirming that any path-product plan must be quotient or clustered.

**UNVERIFIED-LEADS**
1. Semialgebraic curve selection and uniform Łojasiewicz-type reductions: standard real algebraic geometry, but not repo-grounded. Acquire a local byte-matched source before binding.
2. Full converse derivation of the H-M normal form: the dossier has extraction-level H-M loci; for af-grade work, either byte-pin the PDF/source or derive the finite Markov-chain proof internally.
3. Robust clustered quotient under \(SPS^{-1}\) near-duplicate smearing: plausible from w16, but still a lead until constants are derived.