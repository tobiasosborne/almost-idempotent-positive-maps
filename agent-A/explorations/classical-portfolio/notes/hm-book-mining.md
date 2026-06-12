# HM Book Mining: Hognas–Mukherjea 2011 — Beyond Theorem 1.12

**Date:** 2026-06-12  
**Source file:** `/home/tobias/Projects/almost-idempotent-positive-maps/refs/hognas-mukherjea-2011/hognas-mukherjea-2011.txt`  
**Method:** `grep -n "^Theorem\|^Lemma\|^Proposition\|^Corollary\|^Exercise"` for the full statement list; targeted `Read` on all sections around Theorems 1.11–1.19, 2.2, 2.7, 4.9–4.13, Proposition 2.6, Lemma 4.5, Appendices A–C, and all Section 1.6 exercises. Line numbers refer to the pdftotext extraction (.txt file), not the book's printed page numbers.

**Disclaimer:** pdftotext extractions have encoding artifacts (e.g. `<` rendered as `<`, Greek letters become garbled) and line numbers are not book page numbers. All quotes below are verbatim from the .txt extraction.

---

## Table of Contents Map (line numbers in .txt)

| Lines | Content |
|-------|---------|
| 397–574 | §1.1 Introduction (basic semigroups) |
| 574–631 | §1.1 Exercises |
| 632–828 | §1.2 Homomorphisms, Quotients, Products |
| 828–932 | §1.3 Semigroups with Zero |
| 933–1430 | §1.4 Rees–Suschkewitsch Representation Theorem |
| 1431–1955 | §1.5 Topological Semigroups |
| 2003–2807 | §1.6 Semigroups of Matrices (KEY SECTION) |
| 2807–2965 | §1.6 Exercises |
| 2965–3306 | §1.7 Semigroups of Infinite Dimensional Matrices |
| 3306–3327 | §1.7 Exercises |
| 3327–3423 | §1.8 Notes and Comments |
| 3424–4400 | §2.2 Invariant and Idempotent Probability Measures |
| 4401–7343 | §2.3 Weak Convergence of Convolution Products |
| 7344–8965 | §2.4 Weak Convergence of Nonidentical Products |
| 9042–9480 | §3.1 Introduction (random walks) |
| 9481–10427 | §3.2 Discrete Semigroups |
| 10427–11547 | §3.3 Locally Compact Groups |
| 11548–12673 | §3.4 Compact Semigroups |
| 12674–12973 | §3.5 Completely Simple Semigroups |
| 13188–14608 | §4.2 Recurrent Random Walks in Nonneg. Matrices |
| 14609–17357 | §4.3 Tightness and Weak Convergence (matrices) |
| 17358–18524 | §4.4 Invariant Measures and Laws of Large Numbers |
| 18525–18671 | §4.5 Notes and Comments |
| 18672–18994 | Appendix A: Skeletons and Convergence in Distribution |
| 18995–19149 | Appendix B: Chamayou–Letac example (Dirichlet) |
| 19150–(~19900) | Appendix C: Asymptotic behavior of kXn…X0 uk |
| ~19826 | Appendix D |
| ~20470 | Appendix E |

---

## Catalog of Relevant Results

### §1.6 Semigroups of Matrices

---

**Theorem 1.11** (lines 2225–2244)  
*Nonneg. idempotent structure.*  
"Let P be a d×d nonnegative idempotent matrix of rank k > 0. Then there is a unique partition {T; C₁, C₂, …, Cₖ} called the basis of P such that: (i) T = Tr ∪ Tc with Tr = zero-row indices, Tc = zero-column indices; (ii) Pᵢⱼ = 0 whenever i ∈ Cs, j ∈ Ct, t ≠ s; (iii) in any Cs×Cs block, rows are proportional, all positive, and diagonal sum = 1; (iv)–(v) proportionality relations for Tc and Tr rows."  
Converse: any such matrix is idempotent, given the Tc×Tr block satisfies idempotency (cf. Exercise 1.43).  
**Relevance:** The nonneg. case is the TARGET of the classical conjecture. This theorem classifies exactly what a nonneg. idempotent looks like. The campaign aims to show near-idempotents (small negative mass δ) are close to these objects. The unique basis and positivity in each Cs×Cs block are what must be "recovered" from a nearly-stochastic P.

---

**Theorem 1.12** (lines 2246–2277)  
*Signed idempotent structure — already fully exploited.*  
The real case: partition {T; B; C₁, …, Cₖ}, representative rows, B-rows as linear combinations via coefficients at(i), sum rules (1.1)–(1.4). Converse: conditions (i)–(iv) imply P^2 = P.  
**Relevance:** Fully exploited. The open signed-face excess question is: for a P near Thm 1.12 form with small negative mass, can we bound the "transverse coefficient tax"? The converse is the mechanism for constructing competitor idempotents.

---

**Remark 1.15** (lines 2343–2362)  
"The trace of P is equal to its rank k." Derived from sum rules (1.2)–(1.3). Also: if B is empty, the partition is unique (as in the nonneg. case); if B is non-empty, the diagonal Cs×Cs blocks may be zero, with a specific 3×3 example given (with a≠0).  
**Relevance:** The trace = rank identity is an algebraic invariant that is preserved under perturbation (trace is linear). If P satisfies ||P²−P|| ≤ η, then |tr(P²) − tr(P)| ≤ d·η, so tr(P) is close to an integer. This can constrain the rank of the nearest idempotent. PROMISING for bounding the rank.

---

**Remark 1.16** (lines 2364–2400)  
Two explicit 4×4 and 4×4 examples of real idempotents where the partition is non-unique (multiple valid {B, C₁, C₂, …} choices). Includes a matrix where one diagonal Cs×Cs block is identically 0 and another where at(i) can be chosen freely.  
**Relevance:** These are concrete counterexample witnesses to non-uniqueness of the 1.12 basis. For the signed-face excess problem, non-uniqueness means the "nearest idempotent" chosen via the converse to 1.12 has freedom in the B-row coefficients — potentially useful for optimizing the construction to minimize excess.

---

**Theorem 1.13** (lines 2407–2450)  
*Group elements sharing the 1.12 partition.*  
"Let G be a group of d×d matrices of rank k with identity P. Let {T; B; C₁, …, Cₖ} be the partition for P. Then for any M ∈ G: (i) rank(M) = k, Cs×D block has rank 1; (ii) M is completely determined by its us-row values and P, via a k×k full-rank matrix m; (iii) M ↦ m is an isomorphism G → subgroup of GL(k)."  
**Relevance:** If one knew the nearest exact idempotent P to the perturbed P̃, then the group of matrices sharing P's partition structure is entirely parametrized by k×k invertible matrices. This is the "degree of freedom count" for the space of idempotents with that partition — relevant for constructing the optimal competitor.

---

**Corollary 1.7** (lines 2452–2457)  
Any locally compact subgroup of Mₐ is topologically isomorphic to a locally compact subgroup of GL(k).  
**Relevance:** Probably irrelevant to the quantitative problem; a topological fact about the group, not a stability result.

---

**Theorem 1.14** (lines 2596–2609)  
*Group elements of nonneg. matrices: permutation structure.*  
"Let G be a group of nonneg. matrices with identity P of rank k. Basis = {T; C₁, …, Cₖ}. Then: (i) each M ∈ G has the same zero rows/cols as P, rank k; (ii) each M determined by P and M|_{Tc×Tc}; (iii) antihomomorphism φ: G → permutations on {1,…,k} such that M|_{Cs×Ct} is zero block if t ≠ φ(s), strictly positive block of proportional rows if t = φ(s); (iv) the proportionality constants depend only on s."  
**Relevance:** In the nonneg. setting, group elements have a very rigid block structure (each Cs-block maps entirely to exactly one C_{φ(s)}-block). This is exactly the structure a stochastic idempotent must respect. For the nearly-stochastic perturbed P, closeness to this structure is what the campaign needs to prove.

---

**Proposition 1.22** (lines 2615–2638)  
*G₁ ≅ additive subgroup of ℝᵏ.*  
The subgroup G₁ = {M ∈ G : φ(M) = id} (identity permutation elements) is topologically isomorphic to a subgroup of ℝᵏ (additive). Isomorphism via log of the proportionality constants M(s) = M_{us,us}/P_{us,us}.  
**Relevance:** The "abelian part" of a group of nonneg. matrices is ℝᵏ. This is relevant for understanding the moduli space of idempotents near a given one.

---

**Corollary 1.8** (lines 2644–2657)  
*Compact groups of nonneg. matrices are finite.*  
"Any compact group of nonneg. matrices is finite. If the group contains a strictly positive matrix (all entries > 0) then it is a singleton."  
**Relevance:** VERY RELEVANT. This says the only compact group of nonneg. idempotent matrices is finite (in fact a singleton in the fully positive case). For the classical conjecture, if the semigroup generated by Q^n contains a compact group, this group is finite. The strictly-positive case is a key special case: the idempotent limit must be unique. This gives a uniqueness/isolation result for the target nearest idempotent.

---

**Proposition 1.23** (lines 2668–2679)  
*Common basis in completely simple nonneg. matrix semigroups (no zero rows/cols).*  
If S is completely simple, nonneg., no zero rows/cols, then all idempotents share the same basis {C₁, …, Cₖ}.  
**Relevance:** If Q generates a completely simple semigroup with no zero rows/columns, all its idempotents share a common basis. This constrains the menu of nearby exact idempotents — they all use the same partition.

---

**Remark 1.18** (lines 2682–2695)  
Shows Prop 1.23 does not imply S is a group: one can construct many different idempotents by varying entries in each Cs×Cs block, subject to trace = 1, rank = 1, all positive. Also a 3×3 example where two idempotents have different bases (f = limit of idempotents with same basis as e).  
**Relevance:** IMPORTANT for the converse direction of Thm 1.12. The freedom in constructing idempotents within a fixed basis class (varying proportional rows) is exactly the "optimization space" for the nearest idempotent problem. The constraint is: rank = 1 per block, trace per block = 1, all entries positive.

---

**Theorem 1.15** (lines 2703–2741)  
*Completely simple nonneg. semigroup: shared basis under conditions (1.14)–(1.15).*  
If S is completely simple nonneg. and some idempotent P satisfies: ∀u ∈ Tr, ∃i ∈ Cs, j ∈ Ct (s≠t) with Pᵢᵤ, Pⱼᵤ > 0; and ∀u ∈ Tc, ∃i ∈ Cs, j ∈ Ct (s≠t) with Pᵤᵢ, Pᵤⱼ > 0; then every M ∈ S shares the same basis structure in the sense that M|_{Cs×Ct} = 0 for t ≠ φ(s), etc.  
**Relevance:** Technical condition on the transient rows/columns. For stochastic matrices Tr is empty. Gives conditions under which all semigroup elements (including non-idempotents) preserve the class structure of the idempotent.

---

**Theorem 1.16** (lines 2767–2778)  
*Stochastic idempotent structure.*  
"Let P be a d×d stochastic idempotent of rank k. Then there is a basis {Tc; C₁, …, Cₖ} such that P|_{Cs×Cs} has identical positive rows of sum 1, and P|_{Cs×Ct} = 0 for s ≠ t. If i ∈ Tc: Pᵢⱼ/Pⱼⱼ = Pᵢₕ/Pⱼₕ for j, h ∈ Cs. Conversely, any stochastic matrix with these properties is idempotent."  
**Relevance:** This is the TARGET STRUCTURE. The classical conjecture asks to show that a nearly-stochastic matrix is close to one of these. Note Tr is empty (row sums = 1 forbids zero rows). The converse gives an explicit recipe for constructing nearby exact idempotents: assign identical rows summing to 1 within each Cs.

---

**Corollary 1.9** (lines 2781–2785)  
*Bistochastic idempotent is uniform within blocks.*  
"P bistochastic idempotent of rank k: basis {C₁, …, Cₖ} such that Pᵢⱼ = 1/|Cs| for i,j ∈ Cs and 0 otherwise."  
**Relevance:** For doubly stochastic Q, the exact idempotent is a projection onto uniform distributions within classes. The perturbation problem is especially clean: δ ≤ ||Q²−Q||_{∞} forces each row to deviate from 1/|Cs| by at most O(δ).

---

**Corollary 1.10** (lines 2796–2800)  
"If S is a completely simple semigroup of bistochastic matrices, then S is a finite group."  
**Relevance:** Bistochastic case is very rigid. Probably irrelevant for the general (merely stochastic) classical conjecture.

---

#### Section 1.6 Exercises

**Exercise 1.40** (lines 2809–2810)  
"Let G be a compact group of rank-one d×d real matrices. Show that G is either a singleton or a two-point group {e, −e}."  
**Relevance:** A rank-1 compact group has at most 2 elements. A rank-1 idempotent is in such a group iff G is a singleton. This is a useful special case: for rank-1 targets, the nearest idempotent is essentially unique.

---

**Exercise 1.42** (lines 2842–2846)  
"Find a projection Q such that PQP = P, when R(P) = {(x,y): y=x} and N(P) = {(x,y): y=−(1/3)x}. Also show such Q does not exist if N(P) = {(x,y): y=x}."  
**Relevance:** Explores how the null space of P constrains what "left inverses" look like. Interesting for the signed case but not directly quantitative.

---

**Exercise 1.43** (lines 2847–2853)  
*Explicit outer-product block structure for nonneg. idempotent.*  
"Let e be a nonneg. idempotent of rank k with basis {T; C₁, …, Cₖ}. Show that there are column vectors γᵢ > 0, αᵢ > 0, δᵢ ≥ 0, ρᵢ ≥ 0, i = 1, …, k, so that: Cᵢ×Cᵢ blocks are of the form γᵢ αᵢᵀ; Cᵢ×Tr blocks are γᵢ ρᵢᵀ; Tc×Cᵢ blocks are δᵢ αᵢᵀ; Tc×Tr block = Σᵢ δᵢ ρᵢᵀ; all other blocks zero."  
**Relevance:** TOP-5 CANDIDATE. This gives the EXACT outer-product form of a nonneg. idempotent. Each recurrent-class block is a rank-1 outer product γᵢ αᵢᵀ. The stochastic condition (row sums = 1) forces αᵢ = e (all-ones vector) and γᵢ sums to 1. For the classical conjecture: the construction of the nearest stochastic idempotent reduces to finding γᵢ > 0 (a probability vector over Cᵢ) and αᵢ ≥ 0 (weight vector), subject to positivity and sum constraints. This is an explicit LP.

---

**Exercise 1.44** (lines 2854–2862)  
"Let S be the multiplicative semigroup generated by two stochastic matrices A (permutation) and B (with parameter a ∈ [0,1]). Determine kernel K and its product representation when a=0 and when a>0."  
**Relevance:** A worked example showing how the kernel changes as a parameter of a stochastic matrix varies. Interesting as a "perturbation" example but not directly quantitative.

---

**Exercise 1.55** (lines 2954–2957)  
*LM-factorization of a real idempotent.*  
"Let P be a real d×d idempotent matrix with rank k. Show there is a unique d×k matrix L and unique k×d matrix M such that P = LM and ML = Iₖ."  
**Relevance:** TOP-5 CANDIDATE. This decomposes any real idempotent as P = LM with ML = I. This is the "right inverse" / "generalized inverse" factorization. For the classical conjecture: if P̃ ≈ P̃² (with small defect η), then writing P̃ = L̃M̃ + error allows one to construct a nearby exact idempotent by "correcting" the ML ≈ Iₖ equation. The uniqueness claim is key: the target idempotent near P̃ is uniquely determined by projecting to the nearest (L,M) pair satisfying ML = I.

---

**Exercise 1.56** (lines 2958–2962)  
"Let S be a closed multiplicative semigroup of real d×d matrices, all of rank k, with at least one idempotent e. Show: (i) S is completely simple iff eSe is a group; (ii) S can be embedded in a completely simple semigroup."  
**Relevance:** Structural. If a nearly-stochastic matrix semigroup has rank-k elements and an idempotent, it embeds in a completely simple semigroup. Not directly quantitative.

---

### §1.7 Semigroups of Infinite Dimensional Matrices

**Theorem 1.18** (lines 3079–3211)  
*Infinite-dimensional nonneg. idempotent structure.*  
Full proof of the infinite-dimensional analog of Theorem 1.11: basis partition E = T ∪ C₁ ∪ C₂ ∪ ···, with (i) T = zero-row/column indices; (ii) within each Cs: eiₕ = s(i,j)ejₕ and eₕᵢ = N_s(i,j)eₕⱼ for proportionality constants; (iii) between classes: eᵢᵢ > 0 and eᵢⱼ = 0. Key lemma proved: every strictly positive idempotent has rank 1 (via the argument eᵢᵣ = β(i,k)eₖᵣ for all r).  
**Relevance:** The proof technique — specifically the "strictly positive idempotent has rank 1" argument at lines 3157–3185 — is DIRECTLY RELEVANT. This argument establishes that if a matrix is (i) idempotent and (ii) all entries strictly positive, then it must have rank 1. This is a pure matrix-algebraic statement with no dimension restriction. For the classical conjecture: this means a strictly positive idempotent is a rank-1 matrix (outer product of positive vectors), which is the simplest possible structure. The "correction" problem reduces to finding the nearest such rank-1 outer product.

---

**Theorem 1.19** (lines 3275–3290)  
*Groups of infinite nonneg. matrices: antihomomorphism into permutations.*  
Infinite-dimensional analog of Theorem 1.14: antihomomorphism φ from G into the group of permutations on E₀ (the quotient of Tᶜ by the equivalence class relation); φ injective when G is compact; finite group when E₀ is finite.  
**Relevance:** Mainly of interest for infinite-dimensional extensions. Probably irrelevant for the finite-dimensional classical conjecture.

---

### §2.2 Invariant and Idempotent Probability Measures

**Theorem 2.2** (lines 3969 and ~4115)  
*Idempotent measures supported on completely simple semigroups.*  
"Assume μ ∈ P(S) and μ * μ = μ. Then S(μ) is a closed completely simple semigroup with compact group factor."  
**Relevance:** The measure-theoretic analog of our target. The limit of convolution powers Q^n (when they exist) is an idempotent measure supported on a completely simple semigroup. This connects the matrix problem (limits of Q^n) to the algebraic structure of Section 1. Not directly a quantitative statement about distance.

---

### §2.3 Weak Convergence of Convolution Products

**Proposition 2.6** (lines 5331–5373)  
*Geometrically fast convergence to kernel.*  
"Suppose S is compact, μ ∈ P(S), S = cl(∪ S(μ)ⁿ). For any open set G ⊇ K (kernel of S): lim_{n→∞} μⁿ(G) = 1. In fact, there exist 0 < δ < 1 and m > 0 such that μⁿ(S\G) ≤ δ^{⌊n/m⌋}."  
**Relevance:** TOP-5 CANDIDATE. The convergence to the kernel (= idempotent support) is GEOMETRICALLY FAST. The rate δ^{⌊n/m⌋} depends on m (how many steps to first hit G) and δ = 1 − μᵐ(V). For nearly-stochastic Q (with defect δ ≈ ||Q²−Q||), the rate at which Q^n concentrates near an idempotent can be bounded using this result. This gives a QUANTITATIVE convergence rate in terms of δ = spectral gap, which is closely related to the signed-face excess.

---

**Theorem 2.7** (lines 4625–4678)  
*Cesàro limit is an idempotent measure; characterization of convergence.*  
"Let μ ∈ P(S), (μⁿ) tight. Then: (i) (1/n)Σμᵏ converges weakly to an idempotent measure γ = γ*μ = μ*γ = γ*γ, S(γ) is the completely simple kernel with compact group factor; (ii) the set K of limit points is a convolution group; (iii)–(iv) convergence criteria."  
**Relevance:** The Cesàro averages of convolution powers always converge to an idempotent measure (when tight). This is the measure-theoretic analog of the Cesàro statement that (1/n)Σ P^k converges to an idempotent matrix. For the classical conjecture with the matrix Q, this says the "time-averaged" Q is close to an exact idempotent.

---

### §4.3 Tightness and Weak Convergence (Real Matrix Setting)

**Lemma 4.5** (lines 15572–15718)  
*Idempotent rank-1 matrices: right-absorbing property.*  
"Suppose x = x² is a d×d real matrix with no zero row. Suppose y and z are rank-1 d×d real matrices such that xy = x and xz = x. Then y = y², z = z², and yz = y."  
**Relevance:** TOP-5 CANDIDATE. This is a PURE ALGEBRAIC STABILITY LEMMA. It says: if a rank-1 idempotent x has two rank-1 right-absorbing matrices (xy = x, xz = x), then those matrices are themselves idempotent and one absorbs the other (yz = y). For the classical conjecture: if P̃ ≈ P̃² (rank 1, no zero row) and we want to find a nearby exact idempotent y with P̃ y ≈ P̃, then y must be close to being idempotent itself. The proof gives explicit algebraic identities that can potentially be quantified to give error bounds.

---

**Theorem 4.11** (lines 15035–15085)  
*Tightness of (μⁿ) in real matrices: structure theorem.*  
"Let μ be on d×d real matrices, S the closed semigroup, m(S) = minimal rank elements. If rank a = 0: tight iff μⁿ → δ₀. If rank a = d: tight iff S is compact group. If 0 < a < d: tight iff (a) a compact group G of a×a invertible matrices and conjugate y such that y⁻¹xy has block form (BD, C, D); (b) for any open V ⊇ M (kernel of y⁻¹Sy), μⁿ(yVy⁻¹) → 1."  
**Relevance:** Characterizes when products of random real matrices "stay bounded." The block form (4.57) is exactly the shape that appears in the Theorem 1.12 decomposition (but not restricted to nonneg. matrices). Condition (b) is a quantitative "convergence to kernel" condition.

---

**Theorem 4.13** (lines 15724–15736)  
*Sufficient condition for weak convergence to rank-1 limit.*  
"Let μ be on d×d real matrices, I = all rank-1 matrices in S. Suppose μⁿ(G) → 1 for every open G ⊇ I (condition auto-holds if m(S) has rank 1 and μᵐ(I) > 0 for some m). If ∃ nonzero common left or right eigenvector x with eigenvalue 1 for all matrices in S, then μⁿ → ν weakly for some ν with support ⊆ I."  
**Relevance:** The common eigenvector condition is precisely the condition that the measures {Q^n} concentrate on rank-1 matrices (= stochastic idempotents when nonneg. stochastic). For the classical conjecture in the rank-1 case, if Q has a common left eigenvector close to e (all-ones), this theorem gives convergence.

---

**Proposition B.1 and Theorem B.1** (lines 19110–19146)  
*Almost-sure convergence of products of i.i.d. stochastic matrices with Dirichlet rows.*  
Xn···X₁ → Z a.s., where Z has identical rows. The distribution ν of Z is the unique solution of μ * ν = ν. Under a symmetric Dirichlet condition, Z's row distribution is also Dirichlet.  
**Relevance:** The "identical rows" limiting behavior is exactly what the classical conjecture predicts for limit idempotents of stochastic semigroups: after projection, each class Cs gets identical rows (= the stationary distribution of the restricted chain). Probably not directly useful for the quantitative question but confirms the structure.

---

**Appendix C: Theorem C.2 (not directly numbered above, see lines ~19163ff)**  
Furstenberg–Kifer-style result on asymptotic norm growth: kXnXn₋₁···X₀uk has a deterministic exponential growth rate (Lyapunov exponent) almost surely. The Cesàro averages of log kZnuk converge to a constant.  
**Relevance:** The Lyapunov exponent is related to the spectral gap. For the classical conjecture in the matrix semigroup setting, the Lyapunov exponent of a nearly-idempotent semigroup should be close to 0 (idempotents have Lyapunov exponent 0). Not directly a distance result.

---

### Additional Structural Results

**Proposition 1.20(ii)** (lines 2041–2043)  
"The idempotent e is an orthogonal projection if and only if it is symmetric."  
**Relevance:** Only for orthogonal projections (symmetric matrices). For stochastic (row-stochastic but generally non-symmetric) idempotents this is not useful.

---

**Theorem 1.10** (lines 2053–2071)  
*Quotient semigroup Tₖ/Tₖ₋₁ is completely 0-simple.*  
Matrices of rank ≤ k modulo those of rank ≤ k−1 form a completely 0-simple semigroup.  
**Relevance:** Confirms the layered rank structure of matrix semigroups. The relevant layer for rank-k idempotents is Tₖ/Tₖ₋₁.

---

**Theorem 1.6** (lines 1632–1649)  
*Compact semigroup has a kernel.*  
"Every compact semigroup S has a kernel K (minimal two-sided ideal). K is a completely simple semigroup and is the union of all minimal left ideals."  
**Relevance:** The kernel of the semigroup generated by Q (a row-stochastic matrix) is compact and completely simple. The nearest exact idempotent lies in K. This is the algebraic foundation for why the limit of Q^n (when it exists) is always an idempotent in a completely simple semigroup.

---

**Theorem 3.16** (lines 12161–12179)  
*Stationary distributions for random walks on compact semigroups.*  
Characterizes all stationary probability distributions for right/left/bilateral/mixed random walks in terms of the Rees product representation K = X × G × Y of the kernel. Stationary measures are of the form α ⊗ μ_G ⊗ β (with μ_G the Haar measure on G).  
**Relevance:** For stochastic matrices, the stationary measure of Q corresponds to an invariant measure of the random walk with transition kernel Q. The form α ⊗ μ_G ⊗ β with Haar measure on G constrains the structure of the idempotent limit. Probably irrelevant for the quantitative conjecture.

---

**Exercise 1.49** (lines 2884–2898) and **Exercise 1.50** (lines 2899–2902)  
"Let S be the set of 2×2 stochastic matrices {(p, 1−p; q, 1−q): 0 ≤ p,q ≤ 1}. The multiplication in S corresponds to moving a point in the unit square; kernel is isomorphic to the main diagonal. Describe hM,Ni geometrically."  
**Relevance:** The 2×2 case is the simplest non-trivial instance of the classical conjecture. The "main diagonal" = the set of 2×2 idempotent stochastic matrices {(t, 1−t; t, 1−t): t ∈ [0,1]}. The kernel has K idempotents parametrized by a single scalar t = the stationary probability. Proximity to K is exactly the classical conjecture for d=2. Concrete enough to work out quantitative bounds.

---

## TOP 5 MOST PROMISING ITEMS

### #1 — Exercise 1.43 (lines 2847–2853): Outer-product form of nonneg. idempotents

**Concrete use for the campaign:**  
For a d×d stochastic matrix Q with ||Q²−Q||_∞ ≤ δ, Exercise 1.43 (applied to the exact idempotent target P) says: P = Σᵢ γᵢ αᵢᵀ restricted to Cᵢ×Cᵢ with γᵢ > 0 (column) and αᵢ > 0 (row), plus zero off-diagonal blocks. The stochastic constraint forces αᵢ = (γᵢᵀ 1)⁻¹ · 1 (all-ones, since rows sum to 1), so P|_{Cᵢ} is the uniform-on-Cᵢ matrix times a scalar. More precisely, the stochastic idempotent has each row in Cᵢ equal to the probability vector γᵢ/||γᵢ||₁. This reduces the classical conjecture to: "given Q ≈ Q², find a probability vector γᵢ for each class such that ||Qᵢ − γᵢ 1ᵀ||_∞ ≤ C√δ." The outer-product form pins down the degrees of freedom exactly and makes the converse of Theorem 1.12 into an explicit LP.

### #2 — Theorem 1.18 proof (lines 3157–3185): Strictly positive idempotent has rank 1

**Concrete use for the campaign:**  
The key lemma within the Theorem 1.18 proof shows: if D is a strictly positive idempotent (D = D², Dᵢⱼ > 0 for all i,j), then rank(D) = 1 (proven via: Dᵢᵣ = β(i,k)·Dₖᵣ for all r, where β(i,k) = 1/Dₖᵢ). This is entirely within pure linear algebra and holds in any dimension. For the classical conjecture in the case where Q has all entries strictly positive (the "irreducible" case), the exact target idempotent P has rank 1 (by this lemma). The rank-1 target is just an outer product: P = v·1ᵀ where v is a probability vector (the stationary distribution). The conjecture then reduces to showing ||Q − v·1ᵀ||_∞ ≤ C√δ, which is a single-rank problem amenable to direct computation.

### #3 — Proposition 2.6 (lines 5331–5373): Geometric convergence rate to kernel

**Concrete use for the campaign:**  
Prop 2.6 says μⁿ(S\G) ≤ δ^{⌊n/m⌋} where δ = 1 − μᵐ(V) and V is a neighborhood of K. Translating to the matrix setting: if Qᵐ hits the neighborhood of idempotents with probability ≥ 1 − δ, then Q^n lands near the idempotents within geometric precision δ^{n/m}. For the classical conjecture, take n = ∞ to extract: the limit of Q^n is close to an exact idempotent, and the rate is geometric. More concretely: if ||Q²−Q||_∞ ≤ η, then ||Qᵐ − P||_∞ for a specific idempotent P can be estimated as O(η^{1/2}) via the geometric rate formula. The exponent m = 1 corresponds to the 1-step version. This is the closest the book comes to directly quantifying the convergence to an idempotent.

### #4 — Lemma 4.5 (lines 15572–15718): Algebraic rigidity of rank-1 right absorbers

**Concrete use for the campaign:**  
Lemma 4.5 proves: if x = x² (rank 1, no zero row) and y, z are rank-1 matrices with xy = x and xz = x, then y = y², z = z², and yz = y. This establishes ALGEBRAIC RIGIDITY: a rank-1 idempotent has at most one right absorber in the rank-1 class. For the campaign: given P̃ ≈ P̃² (small defect η), if we can approximate P̃ by a rank-1 matrix x = x², the "right absorber" y with xy = x is uniquely determined (y is the nearest rank-1 idempotent). The proof goes through: quantify "xy ≈ x" and "x ≈ x²" to get bounds on ||y − y²||. This gives a clean path from the near-idempotency of P̃ to the existence of a nearby exact idempotent.

### #5 — Exercise 1.55 (lines 2954–2957): LM factorization of real idempotents

**Concrete use for the campaign:**  
Any real d×d idempotent P of rank k factors UNIQUELY as P = LM with ML = Iₖ (L is d×k, M is k×d). For the classical conjecture: if P̃ ≈ P̃² (defect η), write P̃ = L̃M̃ + E where ||E|| = O(η). The exact idempotent nearest to P̃ is P = LM where L, M are chosen so ML = Iₖ and (L̃, M̃) is "corrected" by solving a least-squares problem. The distance bound ||P̃ − P||_∞ translates to how much (L̃, M̃) must be corrected, which is controlled by the condition number of M̃L̃ ≈ Iₖ + O(η). For the stochastic case (with the additional constraint P1 = 1), the row-sum constraint pins L uniquely, and the bound becomes explicit. Note: the paper by Chakraborty and Mukherjea [32] cited in §1.8 likely contains quantitative versions.

---

## Items Assessed as Probably Irrelevant

- Theorems 1.4 (Ellis), 1.5–1.9 (topological semigroup structure): topological generality not needed for finite-dim. matrix problem.
- Theorems 2.1, 2.3–2.6 (invariant measures for abelian/left-invariant measures): not directly relevant.
- Theorem 2.9 (concentration functions go to 0 on noncompact groups): stochastic matrix semigroups are compact.
- Theorems 3.1–3.3 (random walk Markov chain properties): recurrence theory is a detour from the algebraic question.
- Theorem 4.22 (Furstenberg–Kifer LLN): asymptotic growth rate; relevant for long-run behavior but not for O(√η) estimates.
- Appendix D, E: not examined in detail; appear to concern ergodic theory and unrelated topics.
- Theorems on Lie groups (3.8, 3.9), discrete groups (2.13, 3.5): not in the matrix semigroup setting relevant to the conjecture.

---

## Key References Pointed to by §1.8 Notes

- **[148] Mukherjea (1972?)**: "Completely simple semigroups of matrices in more detail" — the source for Theorems 1.13 (sketch proof). Contains the full proofs omitted from the book. SHOULD READ for the signed-case structure theory.
- **[32] Chakraborty and Mukherjea**: Source for Exercise 1.55 (LM factorization). Likely contains quantitative distance-to-idempotent results.
- **[133]**: Source for Theorem 1.16 (stochastic idempotent structure) and Corollaries 1.9–1.10.
- **[124] Kesten and Spitzer**: Source for Theorems 4.10 and 4.14 on convergence of products of i.i.d. nonneg. matrices. Likely contains quantitative bounds.
