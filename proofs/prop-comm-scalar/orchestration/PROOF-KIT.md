# PROOF KIT — `prop-comm-scalar` (groundability scout deliverable)

> READ-ONLY scout output. Ground truth = `refs/`. Build artifact, not canonical. Every "verbatim" string below is `grep -F` byte-exact; the prover MUST re-extract from the cited file/locus, never retype from memory.
>
> ⚠️ **OVER BUDGET — MUST FACTOR BEFORE BUILDING. See §6 flag #1 and beads `aipm-0wn`.** A single faithful workspace is ~14 nodes / depth 6, which blows the linker brittleness budget (≤12 nodes, depth ≤3). Register sub-lemma shards via Recipe A first, then build each, then assemble.

## 0. CONTRACT (af root — byte-verbatim from `argument/lemmas/prop-comm-scalar.md` line 4)

```
Every finite-dim unital Jordan R^m-module splits into one-dim scalar modules with action l(x)=x_k (coordinate) or l(x)=(x_p+x_q)/2 (Peirce-1/2 half-sum); in the max-sector norm the support-unit formula Sf(x)=f(x,s) (s=e_k resp. e_p+e_q) is a norm-one right inverse of d^1, Pi=d^1 S is a projection onto im d^1 with ||Pi||<=3, and the next-arrow estimate dist(theta,im d^1)<=12||J theta|| holds (sharpened to <=2 for coordinate modules).
```

`deps:` empty in registry — genuinely self-contained (the prose derives even the module classification from first principles).

---

## 1. PROOF OUTLINE

Four claims over `B = R^m` (coordinatewise product, `||x||_∞`). `M` = finite-dim unital Jordan `B`-module; `l(x)` = scalar action on a 1-dim module; `d^1 h(x,y)=l(x)h(y)+l(y)h(x)-h(xy)`; `Jθ` = project defect operator (def-jordan-coboundary: written `Jθ`, NOT a separate `d²`).

**(A) Algebraic module classification** — *the load-bearing structural claim*. Form the split square-zero extension `B ⊕ M` (`M²=0`); Jordan identity ⇒ module operator identity (JMod) `L_{a²b}+2L_aL_bL_a=L_{a²}L_b+2L_{ab}L_a` and `[L_a,L_{a²}]=0`. With `T_i = L_{e_i}`:
- `a=b=e_i` ⇒ `2T_i³−3T_i²+T_i=0` ⇒ `T_i(T_i−1)(2T_i−1)=0` ⇒ spectrum ⊆ `{0,½,1}`.
- `[L_a,L_{a²}]=0` ⇒ `T_i` commute ⇒ simultaneously diagonalizable.
- `i≠j` ⇒ `2T_iT_jT_i=T_iT_j` ⇒ on a joint eigenvector `λ_iλ_j(2λ_i−1)=0`; unitality `Σλ_i=1` ⇒ each joint eigenspace is `λ_k=1` (coordinate) or `λ_p=λ_q=½` (half-sum). Hence `M=(⊕_i M_i)⊕(⊕_{p<q}M_{pq})`.
- *Scalar cross-check (1-dim)*: `(x_j−x_k)(x_j+x_k−2l(x))=0` forces `l(x)=(x_j+x_k)/2`, support ≤ 2.

**(B) Support-unit right inverse, norm one.** `s=e_k` (coord) resp. `s=e_p+e_q` (half-sum). `(Sf)(x)=f(x,s)`. For `f=d^1h`: coordinate `f(x,s)=h(x)`; half-sum `f(x,s)` reproduces the canonical symmetrized representative (antisymmetric part in `ker d^1`). So `d^1 S f=f` on `im d^1`. Norm one because `||s||_∞=1`.

**(C) Projection `||Π||≤3`.** Max-sector action contractive `||x·m||≤||x||_∞||m||` ⇒ `||d^1h||≤3||h||` (three-term coboundary). `Π=d^1S`: `Π²=Π`, `ran Π=im d^1`, `||Π||≤||d^1||·||S||≤3·1=3`.

**(D) Next-arrow.** Residual `R=θ−Πθ`; `J_R=J_θ`, `dist(θ,im d^1)≤||R||`.
- *Coordinate (constant 2):* sign-vector 3-test identity ⇒ `||R||≤2||Jθ||`.
- *Half-sum (constant 12):* residual decomposes `R=AΔ_xΔ_y+B(x_1y_1−x_2y_2)+Δ_xU(y_0)+Δ_yU(x_0)+W(x_0,y_0)`; coefficients recovered from finite defect evaluations (`A=¼J_θ(u,u)`, `B=½J_θ(u,s)`, `U(z)=½J_θ(u,z)`, `W` via polarization); bounds `|A|≤M/4,|B|≤M/2,||U||≤M/2,||W||≤8M` ⇒ `||R||≤4|A|+2|B|+4||U||+||W||≤12M`.

Each constant (1, 3, 12, 2) is explicitly computed in the prose — none asserted.

---

## 2. EXTERNALS TABLE

Decisive finding: **`refs/hos/joa-m.md` contains the word "module" ZERO times** (`grep -c -i module` = 0), and zero `cochain`/`cocycle`/`coboundary`. The entire cohomological/module apparatus is INTERNAL project vocabulary (`def-jordan-coboundary`, `def-injective-cochain-norm`, both `source: internal`). **This proposition has NO externally-cited mathematical fact in the GROUNDED sense** — every external-looking input is an INTERNAL definition or a DERIVED consequence the prose proves from the Jordan identity via the split null extension.

The two HOS facts that *resemble* the structural inputs are below with TRUE bytes — but with an **arena gap**: HOS states them for the algebra's own multiplication operators `T_a`, NOT for module operators `L_a` on `B⊕M`. The prose does NOT cite them; it re-derives the module versions. Optional context only.

| name | claim | status | source · file · locus · BYTE-EXACT |
|---|---|---|---|
| **MOD-CLASSIFICATION** | finite-dim unital Jordan `R^m`-module splits into 1-dim coord/half-sum modules | **DERIVED** | proven in prose from split-null-extension Jordan identity. NOT in HOS. |
| **JMod** | `L_{a²b}+2L_aL_bL_a=L_{a²}L_b+2L_{ab}L_a` and `[L_a,L_{a²}]=0` on `B⊕M` | **DERIVED** | `grep -F "L_{a^2 b}"`/`"T_{a^2 b}"` on joa-m.md → NOT FOUND. Derive by linearizing the square-zero extension Jordan identity. |
| HOS-LIN-JORDAN *(context only)* | linearized Jordan axiom (2.33) | GROUNDED *(algebra T_·, not module)* | hos · `refs/hos/joa-m.md:995` · `$$[T_a, T_{b \circ c}] + [T_b, T_{c \circ a}] + [T_c, T_{a \circ b}] = 0.$$` (operator form 2.35 @1010). **ARENA GAP.** |
| HOS-PEIRCE-EIG *(context only)* | Peirce eigenvalues `{1,½,0}` of `T_p` | GROUNDED *(algebra T_p)* | hos · `refs/hos/joa-m.md:1487` · `... we must conclude that  $T_p$  has eigenvalues 1,  $\frac{1}{2}$  and 0, and that we have the following vector space decomposition:` (sha `28740e73d547dd46`). The module cubic `T_i(T_i−1)(2T_i−1)=0` re-derives the same spectrum. |

**Externals verdict:** nothing to ACQUIRE, nothing must be passed off as cited. Build like `lem-classical-equiv`: all "external-looking" inputs are DERIVED nodes; the only true imports are def shards. If the prover wants a `refs/` external for HOS-LIN-JORDAN/HOS-PEIRCE-EIG as scaffolding, the bytes above are exact — but flag **arena-gap (algebra→module)** so the verifier checks the prose RE-DERIVES the module form rather than transporting the algebra statement.

---

## 3. INTERNAL IMPORTS

Def shards (`defs:` lists only the first; the rest are vocabulary to `af def-add`):
- **`def-jordan-coboundary`** (declared) — `d^1 h(a,b)=v(a)∘h(b)+h(a)∘v(b)−h(a∘b)`, `im d^1`, `ker d^1`, the defect operator `Jθ`, `dist(h,Der)`. internal/consensus/locked.
- **`def-injective-cochain-norm`** — `||θ||_inj`; the "max-sector norm" arena. (√rank caveat irrelevant here: sectors are 1-dim.)
- **`def-peirce-decomposition`** (HOS-cited, for "Peirce-1/2" terminology) + **`def-jordan-algebra`** (Jordan identity, HOS 2.4.1 @963-967) — vocabulary.

**Prior validated lemmas: NONE.** `deps:` empty is correct (traced; imports no earlier registry result). No hidden dependency.

Note: first af workspace in the Layer-1 next-arrow track — no in-track precedent; clone format from `proofs/lem-classical-equiv`.

---

## 4. NODE PLAN (single workspace = ~14 nodes / depth 6 — OVER BUDGET; see §6)

Honest full plan (tags: grounded-leaf | derived | assembly):

```
N1  Split null extension B⊕M (M²=0) ⇒ module identity (JMod) + [L_a,L_{a²}]=0.  deps: (def-jordan-algebra)   [derived]
N2  T_i=L_{e_i}: cubic ⇒ T_i(T_i−1)(2T_i−1)=0, spec⊆{0,½,1}; commute ⇒ simultaneously diag.  deps: N1   [derived]
N3  i≠j ⇒ λ_iλ_j(2λ_i−1)=0; Σλ_i=1 ⇒ coordinate or half-sum: M=(⊕M_i)⊕(⊕M_{pq}).  deps: N2   [derived]
N4  Coordinate right inverse s=e_k, (Sf)(x)=f(x,s)=h(x), d^1Sf=f, ||S||≤1.  deps: N3   [derived]
N5  Half-sum right inverse s=e_p+e_q, d^1Sf=f, ||S||≤1.  deps: N3   [derived]
N6  Norm-one right inverse S on every 1-dim sector (max-sector).  deps: N4,N5   [assembly]
N7  Contractive action ⇒ ||d^1h||≤3||h|| ⇒ ||d^1||≤3.  deps: N3   [derived]
N8  Π=d^1S: Π²=Π, ran Π=im d^1, ||Π||≤3.  deps: N6,N7   [assembly]
N9  COORD next-arrow: sign-vector 3-test ⇒ ||R||≤2||Jθ||.  deps: N4,N8   [derived]
N10 HALF-SUM residual form R=AΔΔ+B(...)+ΔU+ΔU+W, J_R=J_θ.  deps: N5,N8   [derived]
N11 Coefficient recoveries + bounds |A|≤M/4,|B|≤M/2,||U||≤M/2,||W||≤8M.  deps: N10   [derived]
N12 HALF-SUM assembly ⇒ ||R||≤12M ⇒ dist≤12||Jθ||.  deps: N11   [derived]
ROOT  contract (N3 classification + N6 + N8 + N9&N12).  deps: N3,N6,N8,N9,N12   [assembly]
```
Node count 13+ROOT = **14**; longest chain N1→N2→N3→N10→N11→N12→ROOT = **depth 6**. **Both budgets blown** → factor.

---

## 5. GROUNDABILITY VERDICT

**G — Groundable (build may proceed), but MUST be factored into sub-lemmas.** No fact is both un-quotable AND un-derivable — nothing to acquire (the "structural" inputs are derived from the Jordan identity inside the workspace; the framework is internal vocabulary). The only `refs/`-citable items (HOS 2.33, Peirce eigenvalues) are optional context with an arena gap and are re-derived anyway. Constants 1/3/12/2 all explicitly computed. The single obstruction is **node budget** — a factoring instruction, not a groundability failure. **Caveat the verifier must enforce:** the module classification is DERIVED — do NOT let it be smuggled in as "by HOS/standard rep theory"; HOS has no module theory.

---

## 6. RISK FLAGS

1. **NODE BUDGET — will not fit one workspace (highest-priority).** Honest full plan = 14 nodes, depth 6. **Recommended 4 atomic sub-lemma workspaces** (each ≤~5 nodes/depth≤3) + a thin assembly:
   - `prop-comm-scalar-classification` (N1–N3): module decomposition. *Load-bearing; own validated workspace.*
   - `prop-comm-scalar-rightinv` (N4–N8): norm-one `S` and `||Π||≤3`.
   - `prop-comm-scalar-coord-nextarrow` (N9): coordinate `dist≤2||Jθ||`.
   - `prop-comm-scalar-halfsum-nextarrow` (N10–N12): half-sum `dist≤12||Jθ||` (deepest chain; on its own exactly depth-3).
   Requires registering new sub-lemma shards (Recipe A) with `prop-comm-scalar` depending on them, BEFORE building. **Reviewer ≠ author on the registry change. Tracked as beads `aipm-0wn`.**
2. **Mixed Peirce-1/2 case — contract claims handled; VERIFIED it is** (half-sum module IS the intrinsic mixed Peirce-1/2 component; covered by N3 `M_{pq}` + N10–N12 const 12). Not hand-waved.
3. **Constants 3/12/2 — all PROVEN.** 3 = three-term coboundary × norm-one S; 2 = sign-vector 3-test; 12 = explicit `4·¼+2·½+4·½+8`. The half-sum `||W||≤8M` (from `sup|W(z,z)|≤4M` via polarization) is the least-obviously-tight step — verifier should re-derive `W(x_0,y_0)=Q((x_0+y_0)/2)−Q((x_0−y_0)/2)` and `||W||≤8M` carefully (factor-2 risk).
4. **Arena gap (algebra `T_a` → module `L_a`) — do NOT cite HOS for JMod.** `grep -F "L_{a^2 b}"`/`"T_{a^2 b}"` both NOT FOUND. The prover must DERIVE (JMod) by linearizing the square-zero-extension Jordan identity (N1), not import it. If the verifier sees `refs/hos` used to close N1/N2/N3 directly, REJECT it (fabrication-style arena error).
5. **`max-sector norm` contractivity is the linchpin of `||Π||≤3` and `K_dec=1`.** Immediate in the max-sector norm. The contract is specifically the max-sector norm — prover should fix that arena, NOT attempt the general-`K_dec` statement (out of scope). Verifier: confirm the workspace proves the max-sector version.
6. **`Jθ` definition must match `def-jordan-coboundary`.** The prose's explicit 6-term `Jθ(a,b)=θ(a²,ab)+l(a²)θ(a,b)+l(ab)θ(a,a)−θ(a²b,a)−l(a)θ(a²,b)−l(a)l(b)θ(a,a)` is the project defect operator. State it as a definition-in-workspace consistent with the split-square-zero-extension first-order coefficient (N1). Verifier should check the coordinate/half-sum specializations are the same operator specialized.

### Key file paths (absolute)
- Shard: `argument/lemmas/prop-comm-scalar.md`
- Prose: `agent-B/notes/commutative-scalar-module-splitting.md` (classification + right-inverse + Π), `commutative-scalar-cocycle-projection-theorem.md` (half-sum next-arrow, const 12), `commutative-coordinate-cocycle-projection.md` (coord next-arrow, const 2)
- Report: `report/sections/09-structure-programme.tex:238-251`
- Defs: `definitions/{def-jordan-coboundary,def-injective-cochain-norm,def-peirce-decomposition,def-jordan-algebra}.md`
- Ground truth: `refs/hos/joa-m.md` (sha `28740e73d547dd46…`) — lines 995 (2.33), 1010 (2.35), 1487 (Peirce eigenvalues)
- Format precedent: `proofs/lem-classical-equiv/orchestration/PROOF-KIT.md`, `.../externals/*.json`; smallest workspace `proofs/lem-bridge-orderunit/`
