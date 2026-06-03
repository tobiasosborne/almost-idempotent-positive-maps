# Faithful-invariant-state transfer — does the exact "ordinary-Jordan-product" theorem survive perturbation?

**Agent A, sidequest 2026-06-03. Colleague's question, assessed at strict rigour, with numerics.**

## 0. The question

> If `P` is an idempotent unital positive map on `L(H)` admitting a **faithful
> invariant state**, then its range is *even* a Jordan algebra under the
> **ordinary** Jordan product `a∘b = ½(ab+ba)` of `L(H)` (not merely under the
> projected Choi–Effros product `a•b = P(a∘b)`). **Does this transfer to the
> approximate setting** (`Φ` unital positive, `‖Φ²−Φ‖≤η`)?

Throughout, `dim H < ∞`, all elements self-adjoint, `P=θ(2Φ−𝟏)` the spectral
idempotent of the bridge, `A=Im P`. For `a,b∈A` define the **product hole**
`h_{a,b}=a∘b−P(a∘b)∈Ker P` and the **square hole** `q_a=P(a²)−a²=−h_{a,a}`.

**Answer (one line) — corrected after Agent B's pushback (v0.11).** **No, not from
faithfulness alone.** The colleague's hypothesis is *existential* ("admits a
faithful invariant state"); to that question the answer is NO. What controls the
transfer is the *quantitative, dimension-free* conditioning `λ` (least eigenvalue
of the invariant state's density), and bare existence does not bound `λ` away
from `0`:
- **conditional positive** — *if additionally* `λ=Ω(1)` (dimension-free):
  `‖a∘b−P(a∘b)‖≤C(η/λ)‖a‖‖b‖ = O(η)`, products agree to `O(η)`, and the bridge's
  Jordan defect upgrades `√η→η`. But `λ=Ω(1)` is strong (`λ≤1/dim H`) and is NOT
  implied by the hypothesis — so this is a narrow special case, not a general
  mechanism;
- **the general case fails** — `λ≲η`: the range is not even approximately closed
  under `∘` (holes `Θ(1)`); only the *projected* product survives (Agent B's
  bridge, `O(√η)`). **Agent B's family below is faithful for every `a>0` with
  `η→0`, yet holes `→2/9`** — a definitive NO to the bare hypothesis.

**Headline correction.** An earlier draft (v0.10) headlined this "YES". That was
the wrong emphasis: it answered a *refined* question (faithful state *with a
dimension-free modulus*), not the colleague's literal one. Agent B's explicit
family forced the correction. The two of us **agree on the theorem** (identical
bound, B's `μ`=my `λ`); we now also agree the headline answer is **NO in
general**, conditional YES only with a dimension-free `λ`.

---

## 1. The exact statement (proof, and why faithfulness is essential)

**Theorem (exact).** Let `P:L(H)→L(H)` be unital, positive, idempotent
(`P²=P`), `*`-preserving, admitting a faithful state `ω` with `ω∘P=ω`. Then
`A=Im P` is closed under the ordinary Jordan product `∘`; equivalently
`P(a∘b)=a∘b` for all `a,b∈A`, so `•` and `∘` coincide on `A` and `A` is a unital
Jordan subalgebra of `(L(H)_sa,∘)`.

*Proof.* For `a∈A`, `P(a)=a`. Kadison's inequality for the positive unital `P`
on self-adjoint `a` gives `P(a)²≤P(a²)`, i.e. `a²≤P(a²)`, so
`q_a:=P(a²)−a²≥0`. Invariance: `ω(q_a)=ω(P(a²))−ω(a²)=ω(a²)−ω(a²)=0`. A faithful
state is faithful on the positive cone (`x≥0, ω(x)=0 ⇒ x=0`), so `q_a=0`, i.e.
`a²∈A`. Polarising, `a∘b=½((a+b)²−a²−b²)∈A`. ∎

**Faithfulness is essential — an exact counter-witness.** Take the classical
(commutative) positive unital idempotent on `ℝ³`
```
P0 = [[1,0,0],[0,1,0],[1/3,2/3,0]]   (row-stochastic, P0²=P0)
```
Its only invariant state is `π=(1,0,0)` — **not faithful** (`λ=0`); state 3 is
transient. `Im P0 = {v : v₃=(v₁+2v₂)/3}`. For `a=(−1,1,⅓)∈Im P0` (`‖a‖_∞=1`):
`a²=(1,1,1/9)`, `P0(a²)=(1,1,1)`, so
```
q_a = P0(a²) − a² = (0,0,8/9),   ‖q_a‖ = 8/9.
```
The range is *not* closed under the ordinary product; the hole is `Θ(1)`. (This
is exactly why Effros–Størmer must use the *projected* product `•`.) So the
faithful-invariant-state hypothesis is not decorative: it is what collapses
`•` onto `∘`.

---

## 2. The approximate transfer (proof of the upper bound)

**Theorem (approximate transfer).** Let `Φ:L(H)→L(H)` be unital, positive,
`*`-preserving, `‖Φ²−Φ‖≤η<η₀`, `P=θ(2Φ−𝟏)`, `A=Im P`. Suppose `Φ` admits a
faithful state `ω` with `‖ω∘Φ−ω‖≤η` (e.g. exactly invariant) and density
`ρ_ω≥λ·𝟏`, `λ>0`. Then for all `a,b∈A`
```
‖a∘b − P(a∘b)‖ ≤ C (η/λ) ‖a‖‖b‖,
```
`C` absolute (dimension-free). In particular `•` and `∘` agree on `A` to
`O(η/λ)`; when `λ=Ω(1)` this is `O(η)`.

*Proof.* Three steps on the square hole `q_a=P(a²)−a²`.

1. **Almost-positivity (unconditional; Agent B's bridge, Lemma 3).** Kadison for
   `Φ` plus `‖P−Φ‖≤Cη` and `P(a)=a` give `q_a ≥ −Cη‖a‖²·𝟏`. Hence, writing
   `q_a=q⁺−q⁻` (orthogonal parts), `‖q⁻‖≤Cη‖a‖²`.
2. **Small overlap (invariance).** `ω(q_a)=ω(P(a²))−ω(a²)`. Since
   `‖P−Φ‖≤Cη` and `‖ω∘Φ−ω‖≤η`, `ω(P(a²))=ω(a²)+O(η)‖a‖²`, so
   `|ω(q_a)|≤Cη‖a‖²`. Therefore `ω(q⁺)=ω(q_a)+ω(q⁻)≤|ω(q_a)|+‖q⁻‖≤Cη‖a‖²`.
3. **Operator-norm upgrade (faithfulness).** For `x≥0`,
   `ω(x)=Tr(ρ_ω x)≥λTr(x)≥λ‖x‖`. Apply to `x=q⁺`:
   `‖q⁺‖≤ω(q⁺)/λ≤C(η/λ)‖a‖²`. Combining, `‖q_a‖=max(‖q⁺‖,‖q⁻‖)≤C(η/λ)‖a‖²`.

Polarisation of the symmetric bilinear map `(a,b)↦h_{a,b}` (with diagonal
`h_{a,a}=−q_a`) gives `‖h_{a,b}‖≤C(η/λ)‖a‖‖b‖`. ∎

**Corollary (exponent upgrade — the payoff for the project).** If `λ=Ω(1)`,
then on `A` we have `‖x•y−x∘y‖≤O(η)‖x‖‖y‖`. Since the ordinary `∘` satisfies the
Jordan identity *exactly* in `L(H)_sa`, replacing each `•` by `∘` in the
defect `((a•a)•b)•a−(a•a)•(b•a)` (finitely many `O(η)` substitutions, bounded
factors) gives a Jordan-identity defect of `O(η)`. **A well-conditioned faithful
invariant state upgrades the bridge from `O(√η)` to `O(η)` — a sufficient
condition for Kitaev-strength `η`, distinct from and complementary to the
decomposable/dilation route (findings §8–§9).** Conceptually the faithful
invariant state supplies the second-moment ("variance"/GNS) control that
complete positivity would otherwise provide via a dilation.

---

## 3. Numerics (classical model; the proof is non-commutative and general)

`Φ=`row-stochastic `T` on `(ℝⁿ,‖·‖_∞)`; Jordan product = pointwise; `P=θ(2T−𝟏)`
the Riesz spectral projector onto `Re μ>½`; `λ=min_i π_i`. Scripts:
`hole_scaling.py`, `crossover.py`; raw JSON alongside. `max‖q_a‖` is maximised
over `a∈Im P`, `‖a‖_∞=1` (dense angular grid; `dim Im P=2`).

**(i) No faithful state (Agent B's family B, `λ=0`).** `T_a=(1−a)P0+aS`, state 1
absorbing. As `η→0`:
| η | ‖q_a‖ | ‖q_a‖/√η | ‖P(q_a²)‖ |
|---|---|---|---|
| 6.6e-3 | 0.880 | 10.8 | 7.9e-3 |
| 6.7e-5 | 0.888 | 108.8 | 7.9e-5 |

`‖q_a‖→8/9`, **log-log slope ≈ 0.00 → `Θ(1)`**. The operator-norm hole does
*not* vanish. Only the *projected* hole `‖P(q_a²)‖` vanishes, **slope 1.001 →
`Θ(η)`** — this reproduces Agent B's `‖P(h²)‖/η→32/27` exactly. So B's `Θ(η)`
finding and my `Θ(1)` finding are about *different objects* (projected vs
operator-norm hole) and are fully consistent.

**(ii) Well-conditioned faithful state (family C, two recurrent classes,
`λ≈0.198`).** Perturb the block idempotent `[[p,1−p,0],[p,1−p,0],[0,0,1]]`:
| η | ‖q_a‖ | ‖q_a‖/η |
|---|---|---|
| 1.37e-2 | 3.2e-3 | 0.236 |
| 1.39e-4 | 3.2e-5 | 0.234 |

**Slope 1.002 → `‖q_a‖=Θ(η)`** (two independent seeds: `q/η→0.23`, `0.68`).
Exactly the predicted `O(η)`. The bridge upgrades to `η` here.

**(iii) Is `1/λ` real? Crossover family E (faithful→transient).** Add a leak `ρ`
from the absorbing state back into the transient one; `λ→0` as `ρ→0`. At fixed
`a` (so `η~const`), sweeping `ρ`:
- The faithfulness step is **saturated**: the measured `ω(q⁺)/λ` equals `‖q_a‖`
  to 4 digits — so the operator-norm upgrade in §2 step 3 is tight, not slack.
- But here `ω(q⁺)∝λ` (not `∝η`), giving `‖q_a‖=ω(q⁺)/λ=Θ(1)` even though the
  chain is *faithful* (`λ>0`). Family E lives in the regime `λ≲η`, where the
  bound `η/λ` is correctly **vacuous**.
- Near `λ~η` (`ρ=3e-4`: `λ=5.6e-4`, `η=6.7e-4`) the bound is **tight up to a
  constant**: `‖q_a‖·λ/η ≈ 0.75`.

**Conclusion on `1/λ`.** It is a genuine feature of the worst case, not a proof
artifact: as `λ` falls to `~η`, the operator-norm hole genuinely degrades to
`Θ(1)`. What matters is `λ` *relative to* `η`:
```
‖a∘b−P(a∘b)‖  ≈  C (η/λ)        when λ ≫ η  (meaningful, → O(η) for λ=Θ(1));
              =  Θ(1)            when λ ≲ η  (transfer fails).
```
Whether, in the intermediate band `η<λ<1`, the *true* worst case follows `η/λ`
all the way (family E suggests yes near the crossover) or stays `O(η)` until a
sharp jump (family C/D suggest the latter for their geometry) is an open
quantitative question — but it does **not** affect the headline dichotomy.

**(iv) Qubit degeneracy (B's probe).** In the triangular Bloch form on `C²`,
`h_{r,s}=0` identically (range exactly `∘`-closed) — a degenerate case, not a
counterexample. A non-commutative numerical check of the *Jordan-defect* upgrade
(iii→`O(η)` when `λ=Θ(1)`) is the natural follow-up; the §2 corollary is the
analytic argument and is fully non-commutative.

---

## 4. Honest status ledger

| Claim | Status |
|---|---|
| **Colleague's literal question (faithfulness ⇒ approx `∘`-closure)** | **NO** — Agent B's family: faithful ∀`a>0`, `η→0`, holes `→2/9` (verified) |
| Exact: faithful invariant state ⇒ range `∘`-closed (`•=∘`) | **proved** (§1), faithfulness essential (8/9 witness) |
| Approx upper bound `‖h_{a,b}‖≤C(η/λ)‖a‖‖b‖` | **proved** (§2); A and B agree (B's `μ`=`λ`) |
| Conditional: `λ=Ω(1)` dimension-free ⇒ holes `Θ(η)` | **proved + numerically confirmed** (slope 1, §3ii) — *narrow special case* |
| Conditional: `λ=Ω(1)` ⇒ bridge Jordan-defect `O(η)` | **proved** (§2 corollary); does NOT help the general theorem (`λ=Ω(1)` fails for large/general systems) |
| No/ill-conditioned (`λ≲η`) ⇒ transfer fails, holes `Θ(1)` | **established**: B's closed-form family (`λ=a/3=Θ(η)`, holes→2/9) + my family E; 8/9 exact witness |
| `1/λ` tight up to constant near `λ~η` | **numerically established** (both families saturate `‖h‖≈cη/λ`) |
| Exact worst-case law in band `η<λ<1` | **open** (both families suggest `η/λ` is the true law) |

**Caveat (no overclaim).** `λ≤1/dim H`, so for the maximally-mixed invariant
state `λ=1/d` and the rate is `O(ηd)` — dimension-dependent. Bare existence of a
faithful invariant state does **not** bound `λ` away from `0` (Agent B's family:
`λ=a/3→0` while staying faithful). So the colleague's hypothesis as literally
stated does **not** transfer; the projected Effros–Størmer product `P(x∘y)`
remains necessary. The `O(η)` statement is a *conditional* requiring a
dimension-free spectral floor on the invariant state, a clean but narrow
sufficient condition — not a general mechanism and not a route to `α=1` for the
project's main (general positive `Φ`) theorem.
