# Theory 01 — The Jordan error-reduction lemma (Theorem 1 crux, Task 3)

Agent A. This is the Jordan analogue of Kitaev's `lem_approx`/`cor_improvement` — the step that wins **dimension-free** constants. Goal:

**Lemma ER (target).** ∃ universal `δ₀,ε₀,C` (dim-free) s.t. for `ε<ε₀`: if `ℬ` is a genuine finite-dim JB-algebra and `v:ℬ→A` is a `δ`-Jordan-homomorphism into an `ε`-JB-algebra `A` with `δ<δ₀`, then there is a `Cε`-Jordan-homomorphism `ṽ:ℬ→A` with `‖ṽ−v‖≤C'δ`. (And `v` a `δ`-inclusion ⇒ `ṽ` a `Cε`-inclusion; bijectivity preserved.)

Newton iteration `δ ↦ O(δ²+ε)` then drives any small enough `δ` down to `O(ε)`; with `ε=0` it yields an exact Jordan homomorphism (rigidity).

## 1. The cochain setup (now precise — from Chu–Russo / Penico / Jacobson)

Module action of `ℬ` on `A` via `v`: `a·m := v(a)∘m` (`a∈ℬ`, `m∈A`). [In the iteration `M=A`; for the exact-rigidity ε=0 case `M=ℬ` adjoint module.]

- **1-cochain**: linear `h:ℬ→A`. **2-cochain**: symmetric bilinear `f:ℬ×ℬ→A`.
- **Coboundary** `(d¹h)(a,b) = v(a)∘h(b) + h(a)∘v(b) − h(a∘b)`  [signs verified, two sources].
- **Multiplicativity defect** `g(a,b) := v(a∘b) − v(a)∘v(b)` (symmetric, `‖g‖≤δ`). This is our 2-cochain to kill.
- **Approximate 2-cocycle equation** (linearized Jordan identity; the load-bearing identity, verbatim from Chu–Russo Thm 1.2, with `L_x m = v(x)∘m`):
  ```
  g(a², a∘b) + L_{a²}g(a,b) + L_{a∘b}g(a,a)
     = g(a²∘b, a) + L_a g(a², b) + L_a L_b g(a,a)   + O(ε)·‖a‖³‖b‖.
  ```
  The `O(ε)` error comes from: ℬ satisfies the Jordan identity EXACTLY; A satisfies it only up to ε (JB4); v is bounded (`‖v‖≤1+O(δ)`); replacing genuine products by `g` at each slot accrues the JB4 defect of A. [Derivation: apply v to the exact Jordan identity in ℬ, expand each `v(x∘y)=v(x)∘v(y)+g(x,y)`, and use JB4 in A to collapse the v(·)∘v(·)∘… terms. To be written out fully — finite bookkeeping.]

So `d²g = O(ε)` in the precise sense above: `g` is an **ε-approximate Jordan 2-cocycle**.

## 2. The splitting and the correction (mirroring Kitaev)

If we have a **bounded splitting operator** `s: Z² → C¹` with `d¹(s f) = f` for exact cocycles `f`, and `‖s‖ ≤ K` (the crux: K dimension-free), set
  `h := s g`,  `ṽ := v − h`  (then symmetrize / unitize as Kitaev does).
The new defect:
  `g̃(a,b) = ṽ(a∘b) − ṽ(a)∘ṽ(b) = g(a,b) − (d¹h)(a,b) + O(δ²)·‖a‖‖b‖`
         `= g(a,b) − g_exact-part + O(δ²+Kε)`.
Because `d²g = O(ε)`, `g` differs from an exact cocycle `g₀∈Z²` by `O(ε)` (need: a bounded "cocycle projection"; provided by the same homotopy: `g₀ = g − d²-correction`, or directly `d¹(sg) = g + O(Kε)` if `s` is a homotopy inverse on the ε-approximate complex). Then `g̃ = O(δ² + Kε)`. **Newton:** `δ_{n+1}=O(δ_n² + Kε)` ⇒ `δ_∞ = O(Kε)`. With `K=O(1)` (dim-free) this is `O(ε)`. ∎ (modulo the homotopy/norm lemmas).

`‖h‖=‖sg‖≤Kδ ⇒ ‖ṽ−v‖≤O(Kδ)`; for K=O(1), `‖ṽ−v‖=O(δ)`, preserving inclusions/bijectivity for δ small. ✔

## 3. THE crux: a DIMENSION-FREE bounded splitting `s` (literature gap)

Established (extraction, cited):
- `M(ℬ)` = multiplication algebra `⟨L_a, 1⟩ ⊆ End(ℬ)` is a **semisimple associative algebra** (Jacobson, Ann. Math. 50 (1949) Thm 1) for semisimple/Euclidean ℬ. ⇒ every ℬ-module is completely reducible ⇒ `H¹=H²=0` (Jacobson 1951; Penico 1951) ⇒ a bounded splitting `s` EXISTS (finite dim).
- The generic trace form `τ(a,b)=tr(L_{a∘b})` is **positive-definite** for Euclidean ℬ (McCrimmon), `Aut(ℬ)`-invariant; `Aut(ℬ)` is **compact** (closed in `O(ℬ,τ)`).
- A `Aut(ℬ)`-invariant Casimir `D=Σ e_i⊗e^i` (τ-dual bases) exists — the analogue of Kitaev's `D=∫_{U(ℬ)}U†⊗U`.

**RESOLUTION of the dimension-free obstruction (key advance, 2026-06-02).** B and the literature note correctly that the naive trace-form Casimir `D=Σe_i⊗e^i` has projective norm `≍ dim ℬ`. But this is the WRONG representation. The relevant norm is the **projective tensor norm `‖·‖_∧`**, which is an *infimum over representations*. The dimension-freeness in Kitaev comes NOT from a probability normalization of the Casimir but from the **group-averaged representation**:

- For ℬ=M_n: the diagonal `D=∫_{U(n)} U†⊗U dU` equals `(1/n)·SWAP = (1/n)Σ_{ij} e_{ij}⊗e_{ji}`. The naive sum-representation gives `‖D‖_∧ ≤ (1/n)·n²·1 = n`. But the **averaging representation** gives `‖D‖_∧ ≤ ∫‖U†‖_op‖U‖_op dU = ∫1 dU = 1`. SAME element, dimension-free norm — because `‖·‖_∧` takes the inf over representations and the Haar average is the good one.
- **The Casimir and the Haar diagonal are the same element; only the averaging representation reveals the O(1) projective norm.** This is the whole secret of Kitaev's dimension-freeness, and it is NOT cb-norm-specific — it is pure projective-tensor-norm + compact-group averaging.

**Jordan version.** The contracting homotopy for Jordan cohomology is built from the **separability idempotent `e=Σ u_i⊗u_i' ∈ M(ℬ)⊗M(ℬ)^op`** of the semisimple associative multiplication algebra `M(ℬ)` (NOT from ℬ⊗ℬ directly — the extraction confirms the separability lives in `M(ℬ)`). The unit/unitary group `U(M(ℬ))` is COMPACT (M(ℬ) ≅ ⊕ matrix algebras, semisimple). Represent `e` as the Haar average
  `e = ∫_{U(M(ℬ))} u†⊗u du`   (or the Aut(ℬ)-conjugation average),
whose projective norm is `≤ ∫‖u†‖‖u‖ du = 1`, **dimension-free**, by the same mechanism. The homotopy `s` (contraction of a 2-cocycle against `e` through `v`) then has `‖s‖ = O(1)`.

So the **dimension-free obstruction is resolved in principle**: the bounded homotopy comes from the compact-group-averaged separability idempotent of `M(ℬ)`, with `‖·‖_∧ ≤ 1`. What remains is to (i) write the explicit Jordan contraction `h = s·g` and verify `d¹h = g + O(ε)`, (ii) check the averaging representation satisfies the Jordan cohomological identities, (iii) handle approximate cocycles / approximate-module errors, (iv) direct sums (blockwise; `‖·‖` is a max over ideal-blocks for the order-unit norm). This replaces the previous "Lemma ER-norm (to prove)" — the norm bound is now understood; the remaining work is the explicit contraction identity.

**The OLD framing (superseded):** the *naive* Casimir has `‖D‖ ≍ dim ℬ` … [kept for context; the projective-norm/averaging resolution above supersedes it]. Kitaev's associative `∫U†⊗U` is dimension-free because Haar is a **probability** measure (built-in `1/dim` normalization). **We must prove a normalized version:**

**Lemma ER-norm (to prove).** For each finite-dim Euclidean Jordan algebra ℬ, the splitting `s` built from the **Haar-probability Reynolds operator** `R(φ)=∫_{Aut(ℬ)} g·φ·g⁻¹ dμ(g)` on `Aut(ℬ)` together with the **normalized** trace-form Casimir satisfies `‖s‖ ≤ K` with `K` independent of `dim ℬ`.

Two routes to ER-norm, to develop:
- **(R1) Per-simple-factor + normalization.** Any finite-dim Euclidean ℬ = ⊕_k ℬ_k (simple). For each simple factor, `τ_k = c_k · (Frobenius/operator inner product)` with an explicit scalar `c_k` (e.g. `τ=2n·tr` on `H_n(ℂ)`); dividing it out gives a normalized Casimir whose homotopy norm is `O(1)` *per factor*, with the cross-factor structure handled by orthogonality of the decomposition. Need: verify `K` doesn't grow with the NUMBER of factors (it shouldn't — the splitting is block-diagonal across ideals, and `‖·‖` is a max over blocks for the order-unit norm).
- **(R2) Incremental, à la Kitaev.** Don't apply ER-norm to a large ℬ at once; apply it only inside the *incrementally built* model algebra at each merge/extend step, where ℬ has controlled (bounded-rank-increment) structure, so `K` is uniformly bounded. This is exactly how Kitaev keeps constants dim-free (he never uses the global diagonal on `A`; only on the honest ℬ being built). **This is likely the safest route** and aligns the error-reduction with the incremental assembly (Task 5).

**Working hypothesis:** R1 gives a clean dim-free `K` because (a) the simple Euclidean factors have trace forms that are *fixed scalar multiples* of the operator inner product, so the normalized Casimir is the "operator-space" Casimir whose Reynolds-averaged homotopy is `O(1)` (independent of matrix size — this is the Jordan analogue of the C\* fact that `∫U†⊗U` is norm-1 for every matrix size); (b) direct sums are handled blockwise. I will attempt R1 first; fall back to R2 (incremental) if the number-of-factors or rank dependence bites.

## 4. Subtlety: the module is `A` (an ε-JB-algebra), not a genuine module

The cocycle/coboundary calculus above is for genuine ℬ-modules. Here the "module" is `A` with action `a·m=v(a)∘m`, which is only an *approximate* module (associativity of the action holds up to ε, since A is only ε-JB and v only δ-multiplicative). The homotopy `s` is built from ℬ-data (Casimir of ℬ, Aut(ℬ)) and applied to `A`-valued cochains; the approximate-module errors are absorbed into the `O(ε)` of `d²g` and the `O(δ²)` of the Newton step. This matches Kitaev exactly: his diagonal `D` lives in the honest ℬ; `v,g` are evaluated into the approximate `A`. **Key structural point to preserve: all averaging/Casimir lives in the genuine ℬ; A only receives the contracted cochains.**

## 5. Status / next steps
- [ ] Write out the derivation of the approximate 2-cocycle equation (§1) fully, tracking the `O(ε)` constant.
- [ ] Construct `s` explicitly from the M(ℬ)-separability idempotent / Aut(ℬ)-Reynolds + normalized Casimir; prove `d¹s=id+O(ε)` on ε-approximate cocycles.
- [ ] Prove **Lemma ER-norm** (dim-free `K`) via R1 (per-factor normalization), fallback R2 (incremental). THIS is the literature gap.
- [ ] Newton iteration bookkeeping (constants, basin `δ₀`).
- [ ] Reconcile with Task 5 (incremental assembly) so ER is applied at each step.

Refs: extraction note (this session); Chu–Russo `../refs/lit/chu-russo-1512.03347.pdf`; Jacobson Ann.Math.50(1949); Penico TransAMS70(1951); McCrimmon *A Taste of Jordan Algebras*; Kitaev `lem_approx` (lines 1224–1319), `D=∫U†⊗U` (1246–1254).
