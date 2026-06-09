# PROOF KIT — `prop-spin-splitting`

**Target shard:** `argument/lemmas/prop-spin-splitting.md`
**Contract (af root, byte-for-byte):**
> For a spin factor V=R1+H the exact-adjoint Jordan coboundary d^1 has an O(H)-equivariant right inverse S with ||Sf||_F<=2||f||_inj, hence (by the rank-2 norm comparison) order-unit constant ||S||_{op->op}<=4 sqrt2, independent of dim H; and a normalized adjoint 2-cochain theta with theta(1,z)=0 obeys dist(theta,im d^1)<=(2 sqrt2+2)||J theta|| (next-arrow estimate).

**Bottom line:** GROUNDABLE (verdict **G**). Every external spin-factor structural fact byte-matches HOS verbatim. All constants (2, 4√2, 2√2+2) are DERIVED in the prose and reproduced exactly. Both agents derived it independently; the existing audit's only reservation ("prove the explicit injective-norm contraction rather than invoking HS/Schur") is satisfied by B's committed proof. Fits one af workspace within budget (11 nodes, depth 3). Prover MUST re-grep every external before pasting.

---

## 1. PROOF OUTLINE

**Half A — the O(H)-equivariant right inverse S (constant 2 in Frobenius, 4√2 in order-unit).**
1. *Setup.* V = R1 ⊕ H, product `(α1+x)(β1+y) = (αβ+⟨x,y⟩)1 + αy + βx`. Euclidean norm `||(α,x)||_2 = (α²+||x||²)^{1/2}`. Injective Euclidean cochain norms `||h||_Fop = sup_{||z||_2≤1}||h(z)||_2`, `||f||_Fop = sup_{||z||_2,||w||_2≤1}||f(z,w)||_2`. Adjoint coboundary `(d^1 h)(a,b)=a·h(b)+h(a)·b−h(ab)`.
2. *Parametrize a 1-cochain* `h:V→V`: `h(1)=p1+a`, `h(x)=⟨u,x⟩1+Ax` (`p∈R`, `a,u∈H`, `A∈End(H)`). Direct multiplication gives the three blocks of `d^1 h` (values at (1,1),(1,x),(x,y)). The skew part of A drops out — `ker d^1 = Der(V) = so(H)` — so the canonical complement is `A=A*` self-adjoint.
3. *Define S.* Given `f∈im d^1`, read off the data: `f(1,1)=p1+a`; self-adjoint `S_f` from `2⟨x,S_f y⟩ = B_f(x,y)+p⟨x,y⟩` (`B_f` = scalar part of `f(x,y)`); vector `u_f` from exactness `P_H f(x,y)+a⟨x,y⟩ = ⟨u_f,y⟩x+⟨u_f,x⟩y` (uniqueness by `y=x`). Set `(Sf)(1)=p1+a`, `(Sf)(x)=⟨u_f,x⟩1+S_f x`. Then `d^1 S f = f`; linearity and O(H)-equivariance are intrinsic.
4. *Norm bound* `||Sf||_Fop ≤ 2||f||_Fop`. With `N=||f||_Fop`: `|p|,||a||≤N` (from `f(1,1)`); `||S_f||≤(||B_f||+|p|)/2≤N`; `||u_f||≤N` (from `||U_f(x,x)||≤2N` and `U_f(x,x)=2⟨u_f,x⟩x`). For unit `z=α1+x`: scalar part `|pα+⟨u_f,x⟩|≤√2 N`, vector part `||aα+S_f x||≤N(|α|+||x||)≤√2 N`; combining the two slots gives `||(Sf)(z)||_2≤2N`.
5. *Rank-2 norm comparison → order-unit constant 4√2.* On the rank-2 algebra V the order-unit norm `||·||_ou` and the Hilbert norm `||·||_2` satisfy `||x||_2 ≤ ||x||_ou ≤ √2 ||x||_2` (HOS 6.1.7, byte-grounded below). Propagating through one input slot (1-cochains) and two input slots (2-cochains) costs at most √2 each side, so `||S||_{ou→ou} ≤ 2√2 · ||S||_{Fop→Fop} ≤ 2√2·2 = 4√2`. **This step — not the rank-r gap — is the entire reason spin is dimension-free** (`prop-rank-gap` instantiated at r=2). The constant is independent of dim H.

**Half B — the normalized next-arrow estimate `dist(θ,im d^1) ≤ (2√2+2)||Jθ||`.**
1. *Normalization.* `θ(1,z)=0`, so for `x,y∈H`: `θ(x,y)=c(x,y)1 + D(x,y)`, `c` symmetric scalar bilinear, `D:H×H→H` symmetric bilinear.
2. *Scalar part is an exact coboundary.* `A=A*` with `2⟨x,Ay⟩=c(x,y)`, `h_A(1)=0, h_A(x)=Ax` gives `(d^1 h_A)(x,y)=c(x,y)1`, `||A||≤½||c||`. So the whole problem is in `D`.
3. *Vector coboundary subspace.* `h_u(1)=0, h_u(x)=⟨u,x⟩1` ⇒ `(d^1 h_u)(x,y)=⟨u,y⟩x+⟨u,x⟩y =: D_u(x,y)`.
4. *Linearized Jordan defect.* Using `a²=||a||²1`, `ab=⟨a,b⟩1` for pure vectors and `θ(1,·)=0`, the scalar part of `Jθ` drops and `J_D(a,b)=⟨a,b⟩D(a,a)−⟨b,D(a,a)⟩a`; hence `||J_D|| = sup_{||a||=1}||P_{a⊥}D(a,a)||`.
5. *Hilbert-space stability lemma (the crux of Half B).* For symmetric bilinear `D`, `Q(x)=D(x,x)`, `T=sup_{||x||=1}||P_{x⊥}Q(x)||`: there is `u∈H` (Riesz vector of `c(x)=Tr(y↦D(x,y))` scaled by `1/(n+1)`) with `||Q(x)−2⟨u,x⟩x||≤(2√2+2)T`; polarization (`||x±y||² summing to 4`) then gives `||(D−D_u)(x,y)||≤(2√2+2)T`. The (n+1) and (n−1) factors cancel exactly, giving the dimension-free constant.
6. *Assemble.* `D_u=d^1 h_u`, so `dist(θ,im d^1) ≤ ||D−D_u|| ≤ (2√2+2)||J_D|| = (2√2+2)||Jθ||`.

---

## 2. EXTERNALS TABLE

All "GROUNDED" rows below verified with `grep -Fc` returning exactly 1 against `refs/hos/joa-m.md`. **Bytes pasted from the file, not memory.** Source id `hos` = Hanche-Olsen & Størmer, *Jordan Operator Algebras*; manifest entry `refs/hos/joa-m.md`. **Prover MUST re-grep.**

| Name | Claim used | Status | Source-id : file : locus | BYTE-EXACT quote |
|---|---|---|---|---|
| **GT-spin-product** | Spin-factor Jordan product | **GROUNDED** | hos : `refs/hos/joa-m.md:2266` (2.9.7) | `$$(\xi \oplus \lambda 1) \circ (\eta \oplus \mu 1) = (\lambda \eta + \mu \xi) \oplus ((\xi, \eta) + \lambda \mu) 1.$$` |
| **GT-spin-innerprod** | `a∘b=⟨a,b⟩1` for `a,b∈H` | **GROUNDED** | hos : `refs/hos/joa-m.md:3654` (6.1.5 pf) | `inner product  $\langle \ , \ \rangle$  defined by  $a \circ b = \langle a, b \rangle 1$` |
| **GT-spin-spectrum** | `Sp(a)={−||a||,||a||}` for `a∈H`; `Sp(a+λ1)={λ−||a||,λ+||a||}` | **GROUNDED** | hos : `refs/hos/joa-m.md:3656` (6.1.6) | `if  $a \in H$  then  $\mathrm{Sp}(a) = \{-\|a\|, \|a\|\}$ , and if  $\lambda \in \mathbb{R}$ ,  $a \in H$  then  $\mathrm{Sp}(a + \lambda 1) = \{\lambda - \|a\|, \lambda + \|a\|\}$` |
| **GT-spin-cone** | Positive cone `A⁺={a+λ1 : λ≥||a||}` | **GROUNDED** | hos : `refs/hos/joa-m.md:3658` (6.1.6) | `$$A^+ = \{a + \lambda 1 : a \in H, \lambda \in \mathbb{R}, \lambda \geq ||a||\}.$$` |
| **GT-spin-frobnorm** | Hilbert (state-τ / Frobenius) norm `||a+λ1||_2² = ||a||²+|λ|²` | **GROUNDED** | hos : `refs/hos/joa-m.md:3675` (6.1.7 pf) | `$$||a + \lambda 1||_2^2 = \tau((a + \lambda 1)^2) = ||a||^2 + |\lambda|^2, \quad a \in H, \lambda \in \mathbb{R}.$$` |
| **GT-spin-normcompare** ⭐ | **Rank-2 norm comparison** `2^{-1/2}||·|| ≤ ||·||_2 ≤ ||·||`, dimension-free | **GROUNDED** | hos : `refs/hos/joa-m.md:3679` (6.1.7 pf) | `$$2^{-1/2} \| \| \le \| \|_2 \le \| \|.$$` |
| **GT-spin-system** | spin system: ≥2 symmetries ≠ ±1 with `s∘t=0` for `s≠t` | **GROUNDED** (optional) | hos : `refs/hos/joa-m.md:3620` (6.1.2) | `such that  $s \circ t = 0$  whenever  $s \neq t$  in  $\mathcal{P}$` |
| **GT-spin-rank2** | V is rank-2: `½(1±ξ)` two minimal projections summing to 1 | **GROUNDED** | hos : `refs/hos/joa-m.md:2268` (2.9.7) | `if  $\xi$  is a unit vector in H, then  $\frac{1}{2}(1+\xi)$  and  $\frac{1}{2}(1-\xi)$  are minimal projections with sum 1` |
| **DV-orderunit-norm** | Order-unit norm `||(s,v)||_ou = \|s\|+||v||_2` | **DERIVED** (not external) | from GT-spin-spectrum via `||a||_ou = max|Sp|` | NOT verbatim in HOS; derive as a one-line af step from `Sp(a+λ1)={λ±||a||}`. |
| **DV-constants** | constants 2, 4√2, 2√2+2; explicit S; Hilbert stability lemma; polarization; `||S||_{ou→ou}≤2√2·||S||_{Fop→Fop}` | **DERIVED** (proven af nodes) | — | computed in prose (B-SPINADJ + B's projection note + A §2), not externals. |
| **HYP-adjoint-module** | Module = adjoint module M=V; coboundary convention `a·h(b)+h(a)·b−h(ab)` | **HYPOTHESIS** (def import) | def-jordan-coboundary | Framework choice, not literature. |

**Notes.**
- ⭐ **GT-spin-normcompare is the load-bearing external.** HOS 6.1.7 states `2^{-1/2}||·|| ≤ ||·||_2 ≤ ||·||` with NO dimension dependence — exactly the contract's "rank-2 norm comparison." Ground the comparison HERE (self-contained in HOS) rather than importing `prop-rank-gap`.
- The `||·||_2` in HOS is the state-induced Hilbert norm (`τ`); GT-spin-frobnorm shows it equals `(||a||²+λ²)^{1/2}` = the Euclidean/Frobenius norm the prose calls `||·||_2`.
- `def-spin-factor` already cites 2.9.7 (sha `28740e73d547dd46`) and the def-gate passes clean.

---

## 3. INTERNAL IMPORTS

**Definition shards (af `def-add`):** `def-spin-factor`, `def-jordan-coboundary`, `def-injective-cochain-norm`.

**Prior validated lemmas:** **NONE strictly required.** Shard `deps:` empty; proof self-contained given the 3 def shards + HOS externals.
- ⚠️ **`prop-rank-gap` is a candidate dep but NOT necessary.** The report's proof cites `prop:rank-gap`, but (a) the comparison is byte-grounded directly in HOS 6.1.7, and (b) `prop-rank-gap` is itself `af: none`, so importing it would NOT raise validation level. **Recommend grounding via HOS, keeping `deps:` empty.**

---

## 4. NODE PLAN (≤12 nodes, depth ≤3)

Root == contract verbatim. Two independent sub-trees (A: right inverse; B: next-arrow). **11 nodes**, depth 3.

```
N0  ROOT — the full contract (both clauses). deps: N5, N10   [GOAL]

── Half A: O(H)-equivariant right inverse ─────────────────────────────
N1  Coboundary block formulas + kernel (skew part of A vanishes, ker d^1=so(H)).
    deps: GT-spin-product, GT-spin-innerprod, def-jordan-coboundary       [DERIVED]
N2  Definition + exactness of S: read off p,a,S_f,u_f; d^1 S f = f; S linear & O(H)-equivariant.
    deps: N1                                                              [DERIVED]
N3  Component bounds: |p|,||a||≤N; ||S_f||≤N; ||u_f||≤N (N=||f||_Fop).  deps: N2   [DERIVED]
N4  Frobenius right-inverse bound ||Sf||_Fop ≤ 2||f||_Fop.  deps: N3      [DERIVED]
N5  Order-unit constant ||S||_{ou→ou} ≤ 4√2, dimension-free (rank-2 comparison over 1+2 slots).
    deps: N4, GT-spin-normcompare, GT-spin-frobnorm, DV-orderunit-norm    [DERIVED]

── Half B: normalized next-arrow estimate ─────────────────────────────
N6  Normalized split θ(1,z)=0 ⇒ θ=c·1+D; scalar part exact (h_A); vector coboundary D_u.
    deps: GT-spin-product, GT-spin-innerprod, def-jordan-coboundary       [DERIVED]
N7  Linearized Jordan defect J_D(a,b)=⟨a,b⟩D(a,a)−⟨b,D(a,a)⟩a; ||J_D||=sup||P_{a⊥}D(a,a)||.
    deps: GT-spin-innerprod, def-jordan-coboundary                        [DERIVED]
N8  Hilbert stability lemma: ∃u, ||Q(x)−2⟨u,x⟩x||≤(2√2+2)T (Riesz vector of c/(n+1); (n±1) cancel).
    deps: (none external; pure Hilbert-space)                             [DERIVED]
N9  Polarization: ||(D−D_u)(x,y)|| ≤ (2√2+2)T for unit x,y.  deps: N8     [DERIVED]
N10 Next-arrow: dist(θ,im d^1) ≤ ||D−D_u|| = (2√2+2)||Jθ|| (D_u=d^1 h_u; scalar part exact via N6).
    deps: N6, N7, N9                                                      [DERIVED]
```

**Brittleness:** 11 nodes ≤ 12 ✓; depth 3 ✓. If N8 balloons, factor it into its own sub-lemma `lem-spin-hilbert-stability` and import.

---

## 5. GROUNDABILITY VERDICT

**G — GROUNDABLE NOW.** No acquisition. All seven external spin facts byte-match `refs/hos/joa-m.md` (each `grep -Fc`=1), including the load-bearing GT-spin-normcompare. Every contract constant (2, 4√2, 2√2+2) and explicit S are DERIVED in committed prose. Fits one workspace within budget.

---

## 6. RISK FLAGS

1. **Independent cross-check (positive).** `4√2` is in BOTH `agent-B/notes/adjoint-spin-splitting-theorem.md` and `agent-A/theory/02-spin-splitting.md` §2; contract/shard/report all agree. No constant discrepancy.
2. **Existing audit (`spin-splitting-audit-2026-06-05.md`) is RESOLVED.** Its residual demand — prove `||S_H f||_Fop≤2||f||_Fop` directly, NOT via HS pseudoinverse/Schur — is met by B's committed proof. **Prover must keep this discipline:** prove N3–N4 by the direct element-wise bound, never "the pseudoinverse is bounded in HS." Audit's other caveats (arbitrary modules, approx cocycles, high-rank H_n) are OUT OF SCOPE (this is the adjoint, exact, rank-2 benchmark only).
3. **Dimension-freeness crux (clean).** The √r order-vs-Frobenius gap is `√2` at r=2, independent of dim H, grounded directly in HOS 6.1.7. The √r gap is at the ELEMENT level; propagating to cochain norms costs √2 per input slot (1 slot for h, 2 for f) → the `2√2` factor. Per `def-injective-cochain-norm`'s caveat, a Frobenius/HS TENSOR-norm bound does NOT transfer to the injective norm — the spin proof sidesteps this by bounding `||Sf||` in the injective Euclidean norm from the start, then converting element-wise. **Prover must NOT convert through an HS tensor norm at any point.**
4. **Shard `deps:` empty vs report citing `prop:rank-gap` — keep deps empty, ground via HOS** (prop-rank-gap is af:none; importing adds no strength). Documentation nuance, not a math error.
5. **Two-clause contract → one workspace with two sub-trees** is the faithful match (11 nodes). Could split into `prop-spin-rightinverse` + `prop-spin-nextarrow` if reviewer wants tighter atomicity; not required.
6. **Convention pin (low risk).** B-SPINADJ uses `(d^1 h)(a,b)=a h(b)+h(a) b−h(ab)`; `def-jordan-coboundary` writes `v(a)∘h(b)+h(a)∘v(b)−h(a∘b)`. For the adjoint module `v=id` these coincide. State this identification explicitly in N1 so the af root's `d^1` matches `def-jordan-coboundary`.

**Files of record (absolute):**
- Target: `argument/lemmas/prop-spin-splitting.md`
- Prose: `agent-B/notes/adjoint-spin-splitting-theorem.md`, `agent-B/notes/spin-normalized-cocycle-projection-reduction.md`, `agent-A/theory/02-spin-splitting.md`
- Audit: `agent-B/notes/spin-splitting-audit-2026-06-05.md`
- Report: `report/sections/09-structure-programme.tex` (prop:spin-splitting, lines 200–214)
- Defs: `definitions/def-spin-factor.md`, `def-jordan-coboundary.md`, `def-injective-cochain-norm.md`
- Ground truth: `refs/hos/joa-m.md` (loci 2266, 2268, 3620, 3654, 3656, 3658, 3675, 3679)
- Format precedent: `proofs/lem-bridge-orderunit/externals/` (external JSON `"source": "HOS, refs/hos/joa-m.md:<line>, VERBATIM: \"...\""`)
