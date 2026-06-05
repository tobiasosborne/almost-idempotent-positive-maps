# Theory 02 — The operator-norm splitting, the rank obstruction, and the spin case

Agent A, 2026-06-05. This note isolates *why* the dimension-free **operator-norm**
splitting of the Jordan coboundary `d¹` is hard, reduces the difficulty to a single
quantitative phenomenon (rank growth), and shows the **spin family is structurally
easy** for a clean reason. It refines `01-error-reduction.md §3` and the canary.

Throughout: `ℬ` a finite-dim Euclidean (formally real) Jordan algebra; we want a
right inverse `s` of `d¹: C¹(ℬ,M)→C²(ℬ,M)` (`d¹s=id` on `B²=im d¹`, valid since
`H²=0`) with `‖s‖` **dimension-free in the order-unit (operator) norm**. The
already-known fact (`01-…`, canary) is that the Frobenius/Hilbert–Schmidt
splitting `s_F = d¹⁺` (pseudoinverse) has `‖s_F‖_{HS} = 1/σ_min(d¹) = O(1)`,
dimension-free. The gap is everything between HS and operator norm.

## 1. The obstruction is exactly a factor √(rank)

For a simple Euclidean Jordan algebra `ℬ` of rank `r`, every element `a` has a
spectral resolution `a = Σ_{i=1}^r λ_i c_i` (Jordan frame `c_i`), and
- **order-unit norm** `‖a‖_op = max_i |λ_i|` (spectral radius);
- **Frobenius/trace norm** `‖a‖_2 = (Σ_i λ_i²)^{1/2}` (up to a fixed normalisation).

Hence, *dimension-freely in the embedding dimension but with the rank*,
```
        ‖a‖_2 ≤ √r · ‖a‖_op,        ‖a‖_op ≤ ‖a‖_2.
```
(Equivalently `‖a‖_op ≤ ‖a‖_2 ≤ √r‖a‖_op`.) So the two norms are
`√r`-equivalent and **no better**: the ratio `√r` is attained at `a = 𝟏`
(all `λ_i=1`: `‖𝟏‖_op=1`, `‖𝟏‖_2=√r`).

- spin `V_n`: rank `r = 2` ⟹ constant `√2`, **independent of `n`**.
- `H_n(ℝ/ℂ/ℍ)`: rank `r = n` ⟹ `√n`, **grows**.
- Albert `H_3(𝕆)`: rank 3, single algebra.

**This is the whole story of the operator-norm gap.** The Frobenius splitting is
dimension-free; converting it to operator norm costs at worst `√(rank)`; for the
families whose rank grows (`H_n`) that worst case, if attained, would make the
operator-norm splitting grow like `√n`. The open question is precisely whether the
worst case is attained on the cochains that actually occur in `im d¹`.

## 2. Spin factors: the gap is absent (clean dimension-free reduction)

For spin `V_n = ℝ⊕ℝⁿ`, `‖(t,v)‖_op = |t|+‖v‖₂` and `‖(t,v)‖_2 = √(t²+‖v‖₂²)`,
so for ALL `n`
```
        ‖x‖_2 ≤ ‖x‖_op ≤ √2 · ‖x‖_2.            (rank-2 equivalence)
```
Propagating this through the cochain operator norms (one slot for 1-cochains, two
input slots for 2-cochains; `‖·‖_{Fop}` = the **injective/operator** norm with
*Euclidean* inputs, `sup_{‖·‖_2≤1}`), one gets dimension-free equivalences
```
   (1/√2)‖h‖_{C¹,Fop} ≤ ‖h‖_{C¹,op} ≤ √2‖h‖_{C¹,Fop},
   (1/2)‖f‖_{C²,Fop}  ≤ ‖f‖_{C²,op}  ≤ √2‖f‖_{C²,Fop},
```
and therefore, for any splitting `s`,
```
   ‖s‖_{op→op} ≤ 2√2 · ‖s‖_{Fop→Fop}.        (spin: op-bound ⟸ Euclidean-injective bound)
```
**Consequence.** For spin the order-unit-norm splitting bound is dimension-free
*equivalent* to the **Euclidean-injective-norm** splitting bound `‖s‖_{Fop→Fop}`.
The op-vs-Frobenius difficulty that defeats the global averaging argument
(`01-… §3`: `U(M(ℬ))` are Frobenius- but not order-isometries) **does not arise for
spin**, because on a rank-2 algebra Frobenius and order norms are already
`√2`-equivalent. The remaining spin task is purely Euclidean and `O(n)`-equivariant
(`Aut(V_n)=O(n)`): show `‖s‖_{Fop→Fop}` is dimension-free.

> **Caveat (do not over-read the canary here).** `‖s_F‖_{Fop→Fop}` is NOT implied by
> `‖s_F‖_{HS}=1/σ_min` being bounded: a cochain can have small injective(`Fop`) norm
> but large `HS` norm, so `Fop→Fop` boundedness needs the *direct* operator-norm
> search, not `σ_min`. The canary's **spin op-norm search** (closed-form
> extreme-point, trustworthy to `N=41`, flat→decreasing) measures exactly
> `‖s_F‖_{op→op} ≈ ‖s_F‖_{Fop→Fop}` (by the equivalence above) — so for spin that
> search is `2√2`-faithful to the structural quantity, and its flatness is genuine
> evidence. (The HS/`σ_min` result is a separate, weaker statement.)

## 3. `O(n)`-equivariant decomposition (spin), for an explicit splitting

As `O(n)`-representations (`V_n ≅ 1 ⊕ W`, `1`=trivial, `W`=vector):
```
 C¹ = End(V_n) ≅ 1 ⊕ 1 ⊕ W ⊕ W ⊕ Sym²₀(W) ⊕ Λ²(W),        dim (n+1)²
 C² = Sym²(V_n)⊗V_n ⊇ ... ⊕ Sym²₀(W) ⊕ Λ²(W) ⊕ Sym³₀ ⊕ (2,1)-hook ⊕ (mult.) 1,W
```
`ker d¹ = Der(V_n) = Λ²(W) = so(n)` (dim `n(n−1)/2`, matches the canary's
`dim ker = dim Der`). `d¹` is `O(n)`-equivariant, so by Schur it is block-diagonal
across irrep *types*; on each isotypic block it is a fixed (n-independent up to the
irrep's intrinsic scaling) linear map between multiplicity spaces. The splitting `s`
can be chosen `O(n)`-equivariant (average `s_F` over `O(n)`), hence likewise
block-diagonal. **Target:** bound `‖s‖_{Fop→Fop}` block-by-block; the multiplicity
spaces are small and `n`-independent (mult ≤ 2 for `1,W`; mult 1 for the tensor
irreps), so the only `n`-dependence is through the intrinsic injective/Euclidean
norm ratio of each fixed irrep — which for spin is controlled by §2. This is the
concrete route to a *theorem* (not just numerics) for the spin family.

## 4. The reframed open problem for `H_n` (the genuinely hard families)

> **CORRECTION / SUPERSEDED (2026-06-05).** The "rank-balance lemma" proposed
> below was critiqued by B (`agent-B/notes/spin-splitting-audit-2026-06-05.md`,
> `cochain-norm-conversion-caveat.md`) and is **withdrawn**: it points the wrong
> way. The condition `‖(sf)(a)‖_2 ≤ K‖(sf)(a)‖_op` is a *low-effective-rank*
> condition; it does NOT lower the order-norm upper bound. Worse, an
> order-bounded coboundary can force a Frobenius primitive of norm `√n`
> (`h(x)=x_11·1` on `H_n(ℝ)`), so one must NOT route through Frobenius primitives
> at all — the splitting must be estimated *directly* in the order norm.
> **Moreover the H_n exact-adjoint splitting is now PROVED directly in the order
> norm by B** (`matrix-factor-exact-adjoint-splitting-theorem.md`: diagonal gauge
> 11 + off-sector leakage globalization + sector-reconstruction), so the
> "open problem" framing of §4 is moot for the *exact-adjoint* benchmark. §1–§3
> (the `√rank` obstruction and the spin reduction) remain correct and were
> independently confirmed by B (adjoint spin constant `4√2`). What is still open
> is the *approximate-cocycle / arbitrary-module / positivity* package (report
> §9, `op:layer1-gap`). The original §4 text is kept below for the record.


For `H_n` the rank is `n`, so §2's equivalence degrades to `√n`. The canary
nonetheless sees `‖s_F‖_op` **plateauing** (looser search, to `N=36`). If true, this
says the cochains in `im d¹` are **not** worst-case for the Frobenius→operator
conversion — i.e. the splitting lands on cochains whose values are *spectrally
balanced* (low effective rank, or eigenvalues spread so `max|λ| ≈ (Σλ²/r)^{1/2}`),
avoiding the `‖𝟏‖`-type `√r` blow-up. So the precise open lemma is:

> **Rank-balance lemma (conjectural, the crux for `H_n`).** There is a splitting `s`
> of `d¹` such that for every 2-cochain `f` with `‖f‖_{C²,op}≤1`, the 1-cochain
> `s f` takes values of *dimension-free effective rank* (equivalently
> `‖(sf)(a)‖_2 ≤ K‖(sf)(a)‖_op` with `K` independent of `n`, for `a` in the op-ball).

If this holds, `‖s‖_{op→op} = O(1)` follows. This is a cleaner, checkable target
than "bound the operator norm directly," and it is exactly the structural reason the
spin proof (§2–§3) works — there `r=2` makes rank-balance automatic.

## 5. Status / next

- §1 (rank obstruction = `√(rank)`): **proved**, elementary, clarifies everything.
- §2 (spin op ⟺ Euclidean-injective, dimension-free): **proved**.
- §3 (spin equivariant block reduction): set up; the per-block `Fop` bound is the
  remaining computation to make spin a theorem. **Primary next task.**
- §4 (rank-balance lemma for `H_n`): the reframed crux; conjectural; this is the
  general Layer-1 operator-norm obstruction in its sharpest checkable form.

This supersedes the vaguer "operator norm unresolved" framing: the difficulty is
**precisely** the `√(rank)` Frobenius→operator conversion, it is **absent for spin**,
and for `H_n` it reduces to a concrete **rank-balance** property of `im d¹` that the
canary's plateau is evidence for.
