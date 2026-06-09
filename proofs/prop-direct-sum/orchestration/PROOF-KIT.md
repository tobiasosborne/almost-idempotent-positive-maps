# PROOF KIT — `prop-direct-sum` (groundability scout deliverable)

> Scratch/BUILD artifact for the prover subagent. Ground truth remains `refs/`. All `grep -F`-confirmed bytes below were re-extracted from `refs/hos/joa-m.md` during this scout; the prover MUST re-confirm (re-grep) before pasting into externals.

## Contract (af root — byte-verbatim from `argument/lemmas/prop-direct-sum.md` line 4)

```
If B=⊕_r B_r (order-unit norm = max_r) and each factor has an exact-adjoint coboundary splitting with constant K_r, then B has one with constant max_r K_r + 1, independent of the number of summands (off-block components recovered by P_r f(e_r,·), with no sum over r); valid for adjoint/block-respecting modules.
```

`deps:` is EMPTY in the registry shard — confirmed correct: the proof takes "each factor has a splitting with constant `K_r`" as a **hypothesis**, it does NOT import `thm-matrix-splitting`/`prop-spin-splitting` (those are the *consumers* of this proposition, via `cor-adjoint-benchmark`). No hidden lemma dependency.

---

## 1. PROOF OUTLINE

Setup (all from the prose note `adjoint-direct-sum-reduction.md` + report `prop:direct-sum`):
- `B = ⊕_{r=1}^m B_r`, finite direct sum of unital JB-algebras, coordinatewise Jordan product, order-unit norm `||x|| = max_r ||x_r||` (**a hypothesis of the statement**).
- `e_r` = unit of ideal `B_r` embedded in `B` (a central idempotent of `B`); `P_r : B → B_r` coordinate projection. Adjoint module: action is left Jordan multiplication; `(d^1 h)(a,b) = a∘h(b) + h(a)∘b − h(a∘b)`.
- Each factor has an exact adjoint right inverse `S_r : im(d^1_{B_r}) → C^1(B_r,B_r)` with `d^1_{B_r} S_r g = g` and `||S_r g|| ≤ K_r ||g||`. Set `K = max_r K_r`.

Skeleton:
1. **Same-factor restriction.** For an exact adjoint coboundary `f = d^1 h` on `B`, define `f^r(a,b) = P_r f(a,b)` for `a,b ∈ B_r`. This is an exact adjoint coboundary on `B_r` (the coboundary of `P_r h|_{B_r}`). [pure unfolding of `d^1` + that `B_r` is a subalgebra/ideal]
2. **Block-projection construction.** Define `Sf : B → B` coordinatewise:
   `(Sf)_r(x) = (S_r f^r)(x_r) + P_r f(e_r, x_{≠r})`, where `x_{≠r} = x − x_r`. Linear in `f`. The second summand is the off-block recovery term — **evaluated at the central unit `e_r`, no sum over `r`.**
3. **Norm bound (the "+1").** For `||x|| ≤ 1`: the diagonal term gives `||(S_r f^r)(x_r)|| ≤ K_r ||f^r|| ≤ K ||f||`; the off-block term gives `||P_r f(e_r, x_{≠r})|| ≤ ||f||` (using `||e_r|| ≤ 1`, `||x_{≠r}|| ≤ ||x|| ≤ 1`, and `P_r` norm-1). Sum: `||(Sf)_r(x)|| ≤ (K+1)||f||` for every `r`; max over `r` gives `||Sf|| ≤ (K+1)||f||`. **Summand-count-free because the max over `r` of a per-`r` bound `(K+1)` is again `(K+1)` — there is no sum over the `m` summands anywhere.**
4. **Right-inverse check (`d^1 Sf = f`).** Write `h_{rs}(x) = P_r h(x)` (the primitive's blocks). Two homogeneous-input cases exhaust `B×B` by bilinearity:
   - (a) `a,b ∈ B_r`: output-block `B_r` correct since `d^1_{B_r} S_r f^r = f^r`; output-block `B_j` (`j≠r`) reduces to `−(Sf)_j(a∘b) = −h_{jr}(a∘b) = P_j f(a,b)`.
   - (b) `a ∈ B_r`, `b ∈ B_s`, `r≠s`: `a∘b = 0`; output-block `B_r` is `a∘(Sf)_r(b) = a∘h_{rs}(b) = P_r f(a,b)`; symmetrically `B_s`; all other output ideals get 0 on both sides. Key off-block identity: `P_r f(e_r, x) = e_r∘h_{rs}(x) = h_{rs}(x)` since `e_r` is the unit on output ideal `B_r` and all cross terms vanish.

**Where "+1" arises:** the off-block primitive components `h_{rs}` (`r≠s`) are *read off the coboundary itself* by `f(e_r, x)` — they cost exactly one application of `f` (one extra `||f||` factor), independent of the factor data `K_r`. So the construction never feeds off-block data through the (potentially worse) `S_r`; it pays a flat `+1`.

**Why summand-count independence:** the only aggregation across summands is `||x|| = max_r ||x_r||` and `||Sf|| = max_r ||(Sf)_r||` — both **max**, never **sum**. No term scales with `m`. (Contrast the failed rank-one route in report `remark` lines 180–186: summing rank-one primitives loses `√dim`.)

---

## 2. EXTERNALS TABLE

The argument is overwhelmingly DERIVED (pure cochain algebra over the def shards). The genuinely EXTERNAL (refs-grounded) structural facts are about the order-unit norm and the central units. **All byte-confirmed below via `grep -F` against `refs/hos/joa-m.md`. Prover MUST re-grep before pasting.**

| # | name | precise claim | classification | grounding |
|---|------|---------------|----------------|-----------|
| E1 | `GT-orderunit-norm-formula` | On an order unit space `A` with order unit `e`, the order norm is `||a|| = inf{λ>0 : −λe ≤ a ≤ λe}`. | **GROUNDED** | hos · `refs/hos/joa-m.md:370` (§1.2.1) |
| E2 | `GT-jb-unit-norm-one` | In a unital JB-algebra, `||1|| = 1`. | **GROUNDED** | hos · `refs/hos/joa-m.md:2318` (§3.1.4) |
| E3 | `GT-jb-is-order-unit-space` | A unital JB-algebra is a complete order unit space with order unit `1` and order norm = the given norm. | **GROUNDED** | hos · `refs/hos/joa-m.md:2552` (§3.3.10) |
| E4 | `GT-central-idempotent-summand` | If `e` is a central idempotent in a unital Jordan algebra `A`, then `U_e A` is a direct summand and an ideal in `A`. | **GROUNDED** (optional) | hos · `refs/hos/joa-m.md:1473` (§2.5.7) |
| E5 | `||x|| = max_r ||x_r||` for `B = ⊕_r B_r` | order-unit norm of the direct sum equals the max of factor norms | **HYPOTHESIS** (NOT to ground) | stated in the contract's parenthetical "(order-unit norm = max_r)". Confirmed NOT a general theorem in HOS. `skip_noquote` assumption. |
| E6 | "each factor has an exact-adjoint splitting with constant `K_r`" | per-factor right inverse `S_r`, `d^1_{B_r}S_r=id`, `||S_r||≤K_r` | **HYPOTHESIS** | the antecedent of the implication; an assumption node, not grounded. |

**BYTE-EXACT verbatim quotes (re-confirmed via `grep -F` — prover must re-extract, do NOT retype from memory):**

**E1** — `refs/hos/joa-m.md:370`:
```
$$||a|| = \inf\{\lambda > 0: -\lambda e \le a \le \lambda e\}.$$
```
(Context, `:368`: "An element  $e \in A^+$  is called an order unit for A if for all  $a \in A$  there is  $\lambda > 0$  such that  $-\lambda e \le a \le \lambda e$ .")

**E2** — `refs/hos/joa-m.md:2318`:
```
If A is unital we denote the identity by 1. Then it is clear from (i) that ||1|| = 1.
```

**E3** — `refs/hos/joa-m.md:2552`:
```
**3.3.10. Proposition.** If A is a unital JB algebra, then A is a complete order unit space with the ordering induced by  $A_+$  and order unit the identity 1. The order norm is the given one, and  $a \in A$  satisfies  $-1 \le a \le 1$  implies  $0 \le a^2 \le 1$ .
```

**E4** — `refs/hos/joa-m.md:1473`:
```
- **2.5.7.** From the above proof it is clear that, if e is a central idempotent in a unital Jordan algebra A, then  $U_eA$  is a direct summand and, in particular, an ideal in A. Conversely, if e is an idempotent in A such that  $U_eA$  is an ideal, then e is central. For then, if  $a \in A$ , we must have  $e \circ a \in U_eA$ , i.e.  $U_e(e \circ a) = e \circ a$ . By (2.62), however, this implies  $U_ea = T_ea$ . Hence by 2.5.5, e is central.
```

Note on E4: the proof uses only that `e_r` is the unit/idempotent of the ideal `B_r` and acts as identity on output-block `B_r` (`e_r∘y = y` for `y ∈ B_r`) and annihilates other blocks. The prover may either cite E4 to license "the central units `e_r` are the idempotent units of the ideal summands," or fold it into the setup hypothesis.

**No NEEDS-ACQUISITION facts.** Nothing must be acquired.

---

## 3. INTERNAL IMPORTS

Def shards (used as vocabulary via `af def-add`):
- `def-jordan-coboundary` — `(d^1 h)(a,b) = a∘h(b) + h(a)∘b − h(a∘b)`, "exact-adjoint splitting / right inverse `S`", derivation `= ker d^1`.
- `def-jb-algebra` — what each `B_r` is.
- `def-injective-cochain-norm` — the cochain norm `||θ||_inj = sup_{||x_i||≤1} ||θ(x_1,…,x_k)||` (order-unit norm) that the bound uses. Registry `defs:` lists only the first two, but `def-jordan-coboundary` links this transitively. Prover SHOULD `af def-add` it.

Prior validated registry lemmas to import: **NONE.** `deps:` empty is correct.

---

## 4. NODE PLAN  (8 nodes, depth 3 — within the ≤12 / depth-≤3 budget)

Root `==` the registry contract (byte-verbatim).

- **ROOT** — the contract. depends_on: N5, N7. [assembly]
- **N1** — *Setup / hypotheses as a frame.* `B = ⊕_{r=1}^m B_r` unital JB-algebras, coordinatewise product, order-unit norm `||x|| = max_r ||x_r||` (E5, hyp); `e_r` central unit of ideal `B_r` (E2/E3/E4), `P_r` coordinate projection; adjoint module `d^1` from `def-jordan-coboundary`; per-factor `S_r` with `d^1_{B_r}S_r=id`, `||S_r||≤K_r`, `K=max_r K_r` (E6, hyp). depends_on: E1,E2,E3,(E4),E5,E6, `def-jordan-coboundary`, `def-jb-algebra`, `def-injective-cochain-norm`. [grounded-leaf + hypothesis frame]
- **N2** — *Block restriction is a coboundary.* For `f = d^1 h` on `B`, `f^r := P_r f|_{B_r×B_r}` equals `d^1_{B_r}(P_r h|_{B_r})`, an exact adjoint coboundary on `B_r`. depends_on: N1. [derived]
- **N3** — *Construction.* Define `(Sf)_r(x) = (S_r f^r)(x_r) + P_r f(e_r, x_{≠r})`, `x_{≠r}=x−x_r`; linear in `f`. depends_on: N1, N2. [derived]
- **N4** — *Coordinate maps are norm-nonincreasing in the max-norm.* From `||x||=max_r||x_r||` (E5) and order norm (E1): `||x_r||≤||x||`, `||x_{≠r}||≤||x||`, `||P_r y||≤||y||`, and `||e_r||=1` (E2). depends_on: N1. [derived, leans on E1/E2/E5]
- **N5** — *Norm bound `||Sf|| ≤ (K+1)||f||`.* For `||x||≤1`: `||(S_r f^r)(x_r)|| ≤ K_r||f^r|| ≤ K||f||` (N2,N3, `||f^r||≤||f||` from N4) and `||P_r f(e_r,x_{≠r})|| ≤ ||f||` (N4); sum `≤(K+1)||f||` per `r`; max over `r` ⇒ `||Sf||≤(K+1)||f||`. **No `m`-dependence (max, not sum).** depends_on: N3, N4. [derived — the "+1" + summand-count-freeness]
- **N6** — *Off-block recovery identity.* For `r≠s`, `x∈B_s`: `P_r f(e_r,x) = e_r∘h_{rs}(x) = h_{rs}(x)` (`e_r` unit on output `B_r`, cross terms vanish; uses E2/E4 + `d^1` unfolding). depends_on: N1, N3. [derived]
- **N7** — *Right-inverse `d^1 Sf = f`.* Case (a) `a,b∈B_r`; case (b) `a∈B_r,b∈B_s,r≠s` (`a∘b=0`, outputs `a∘h_{rs}(b)=P_r f` via N6, symmetric in `s`); bilinearity exhausts `B×B`. depends_on: N3, N6, N2. [assembly]

Depth check: ROOT→N5→N4→N1 (depth 3) and ROOT→N7→N6→N1 (depth 3). Width 7 internal nodes. **Within budget.** If N7's two cases balloon, split into N7a (same-factor) / N7b (cross-factor) — still ≤9 nodes, depth 3.

---

## 5. GROUNDABILITY VERDICT

**G — fully groundable with present refs.** Every external structural fact (E1–E4) is byte-present and `grep -F`-confirmed in `refs/hos/joa-m.md`. The two "external-looking" inputs (E5 max-norm, E6 per-factor splittings) are hypotheses written into the contract itself, so `skip_noquote` assumption nodes, not facts requiring acquisition. The entire core is pure cochain/Jordan algebra → DERIVED nodes. Nothing is NEEDS-ACQUISITION; nothing is un-groundable.

---

## 6. RISK FLAGS

- **R1 (max-norm E5) — RESOLVED but frame it right.** "(order-unit norm = max_r)" is a defining hypothesis, NOT a fact to prove. HOS has no general "direct-sum norm = max" theorem. Introduce `||x||=max_r||x_r||` as a `skip_noquote` hypothesis; do not let the verifier demand a refs byte for E5.
- **R2 (contract "no sum over r" / "max_r K_r + 1") — prose DOES prove exactly this** (`adjoint-direct-sum-reduction.md` lines 99–115). ✓
- **R3 (`max_r K_r + 1` vs note's `K+1`).** Identical; keep `K := max_r K_r` as a definition node so the root reads `max_r K_r + 1` verbatim.
- **R4 (adjoint/block-respecting restriction).** Essential. For arbitrary modules a central idempotent can act with Peirce eigenvalue `½`, so off-block recovery `P_r f(e_r,·)` fails. Encode "adjoint module" (action = left Jordan multiplication, `e_r` acts as identity on its block) as a hypothesis. **Do NOT silently generalize to arbitrary modules** — that's the project's signature failure (the `½`-Peirce caveat).
- **R5 (`e_r∘h_{rs}(x) = h_{rs}(x)`, N6).** Output-block index bookkeeping: `h_{rs}: B_s → B_r`, relevant unit is `e_r` (OUTPUT side). Verifier must check `r` vs `s` is not flipped.
- **R6 (no ballooning expected).** If N7 grows, split same-factor vs cross-factor (N7a/N7b). Still ≤9 nodes/depth 3.
- **R7 (`def-injective-cochain-norm` not in registry `defs:`).** Reachable transitively (not a drift error), but prover SHOULD `af def-add` it. The bound is in the ORDER-UNIT cochain norm (not Frobenius); harmless here because the construction never converts norms (only `max` + per-factor `K_r`, already order-unit constants).
