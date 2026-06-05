# Lean/Mathlib coverage study for the almost-idempotent-positive-maps project

**Date:** 2026-06-05. **Method:** 6 parallel subagents each grepped a *local* Mathlib
source tree — `cft-anyons-deprecated/.lake/packages/mathlib/Mathlib`, commit
`d6dab93` (**2026-05-14**), Lean `v4.30.0-rc2`, 8054 `.lean` files — cross-checked
against the online docs. Every "EXISTS" below cites a declaration + file actually
found; every "ABSENT" lists the patterns grepped. This is ground truth as of that
commit, not memory.

**Bottom line.** The fear ("the gap is huge; most of Jordan algebra + its spectral
theory is missing") is **correct for the Jordan-specific and structure-theory
layers**, but with two large mitigations that change the practical picture:

1. The **analytic C\*/convex/cohomology infrastructure is far more mature than
   expected.** Full continuous functional calculus, the finite-dim spectral
   theorem, `CFC.sqrt`/operator-monotone `rpow`, positive maps, *completely
   positive maps*, Birkhoff–von Neumann, simplices, exposed faces, group
   cohomology, Haar measure, Schur/Maschke are all present.
2. The missing "spectral theory" is **Jordan** spectral theory. Our objects are
   *special* Jordan algebras (self-adjoint parts of C\*-algebras), so we can
   **borrow the C\* functional calculus** instead of rebuilding Jordan spectral
   theory — for the bridge and the channel application this sidesteps the largest
   abstract gap.

Consequently the realistic formalisation order is: **(0) definitions + statements
of the conjectures** (achievable, the user's stated minimal goal), **(1) the
commutative/classical section and the bridge theorem** (serious but finite — they
sit on the well-covered parts), **(2) Theorem C / Effros–Størmer**, and far out,
**(3) Layer-1 structure theory and the JNW classification / Albert algebra**
(open-ended, comparable to multi-year Mathlib efforts).

---

## 1. Coverage map by layer

Legend: ✅ reusable as-is · 🟡 partial (ingredients present, glue/result missing) ·
❌ absent (build from scratch). Effort buckets: **S** = days, **M** = weeks,
**L** = months, **R** = research-scale / open-ended. (Line counts are unreliable;
treat as orders of magnitude.)

### 1a. Operator-algebra analytic core (underpins §2,4,6 of the report)
| Need | Status | Evidence / gap |
|---|---|---|
| C\*-algebra, `B(H)`, `Mₙ(ℂ)` | ✅ | `CStarAlgebra` (`CStarAlgebra/Classes.lean`); `B(H)` instance (`ContinuousLinearMap.lean`); `Matrix.instCStarRing` |
| `selfAdjoint`, order, positive cone | ✅ | `selfAdjoint` (`Algebra/Star/SelfAdjoint.lean`); `StarOrderedRing` |
| spectrum, spectral radius | ✅ | `spectrum`, `spectralRadius`; `IsSelfAdjoint.spectralRadius_eq_nnnorm` |
| continuous functional calculus `cfc`/`cfcₙ` | ✅ | `CFC/Unital.lean`, `Instances.lean`; `cfc_mono`, `cfc_pow`, `cfc_comp` |
| `CFC.sqrt`, `rpow`, operator-monotone `t^p` (p∈[0,1]), `abs`, `posPart` | ✅ | `SpecialFunctions/CFC/Rpow/*`, `CFC.monotone_rpow` |
| finite-dim spectral theorem (Hermitian matrices) | ✅ | `Matrix.IsHermitian.spectral_theorem`, `eigenvalues`, CFC instance |
| norm monotonicity `0≤a≤b⇒‖a‖≤‖b‖`; sandwich `−‖a‖≤a≤‖a‖` | ✅ | `CStarAlgebra.norm_le_norm_of_nonneg_of_le`; `IsSelfAdjoint.le_algebraMap_norm_self` |
| `0≤y≤c ⇒ y²≤cy` (bridge Lemma 3) | 🟡 S | derivable in ~5 lines via `cfc_mono`; not named |
| order-unit norm = operator norm (as a named fact) | 🟡 S | sandwich present; no `order_unit_norm_eq` lemma |
| `‖a‖ = sup_ρ |ρ(a)|` over states (bridge "norm via states") | ❌ M | NOT FOUND (`norm_eq_iSup_state` etc.); GNS present so a proof is reachable, or route via spectral radius |
| **spectral idempotent `P=θ(2Φ−1)`** (Riesz projector / sign of the *map* `2Φ−1`) | ❌ S–M | no holomorphic FC / Riesz projector / `spectralProjection`; but `sgn(S)=S(S²)^{-1/2}` is a convergent binomial series in the Banach algebra `End(B(H)_sa)` — constructible from analytic tools, needs the `(1+x)^{-1/2}` series lemma |

### 1b. Positive / CP maps and the operator inequalities (hypotheses + exponent §10)
| Need | Status | Evidence / gap |
|---|---|---|
| positive linear maps `→ₚ`, boundedness, star-preservation | ✅ | `PositiveLinearMap` (`CStarAlgebra/PositiveLinearMap.lean`): `exists_norm_apply_le`, `map_isSelfAdjoint`, `StarHomClass` |
| completely positive maps `→CP` | ✅(thin) | `CompletelyPositiveMap`, CP⟹positive, star-homs are CP |
| unital positive ⇒ contraction `‖Φ(a)‖≤‖a‖` | 🟡 S | `norm_apply_le_of_nonneg` + `‖Φ(1)‖=1`; not bundled |
| **Kadison `Φ(a)²≤Φ(a²)`** | ❌ S | NOT FOUND; supporting order API present, ~1–3 days |
| Kadison–Schwarz `Φ(a)*Φ(a)≤Φ(a*a)` (2-positive) | ❌ M | NOT FOUND; 2-positivity not even defined |
| **Jordan–Schwarz `{Φa*,Φa}≤Φ{a*,a}`** (Størmer) | ❌ M | NOT FOUND; the single largest hypothesis-level gap |
| Choi / Stinespring / Kraus | ❌ M–L | all NOT FOUND |
| decomposable = CP+coCP; transpose as positive map | ❌ M | NOT FOUND; `CStarMatrix.transpose` exists but not as a positive map |
| completely bounded norm `‖·‖_cb` | ❌ M | NOT FOUND |
| Tomiyama conditional expectations; multiplicative domain | ❌ M | NOT FOUND (operator-algebraic sense) |

### 1c. Jordan algebra (algebraic) core (report §3)
| Need | Status | Evidence / gap |
|---|---|---|
| Jordan algebra def (commutative + Jordan identity) | ✅ | `IsCommJordan`, `IsJordan` (`Algebra/Jordan/Basic.lean`, 237 lines) |
| symmetrised product `½(ab+ba)`, special Jordan algebra | ✅ | `SymAlg` (`Algebra/Symmetrized.lean`, 327 lines), `IsCommJordan αˢʸᵐ` |
| power-associativity for Jordan algebras | 🟡 M | `NatPowAssoc` mixin exists; `IsCommJordan→NatPowAssoc` theorem ABSENT |
| multiplication operator `Lₐ` | ✅ | `LinearMap.mulLeft`, `AddMonoid.End.mulLeft` |
| multiplication algebra `M(J)=⟨Lₐ,1⟩` | ❌ M | not defined as a subalgebra of `End(J)` |
| derivations `Der(J)` of a Jordan algebra | ❌ M | `Derivation` requires `CommSemiring` (associative); no Jordan/non-assoc derivations |
| automorphisms `Aut(J)` as a group | ❌ M | `AlgEquiv` forces associativity; `NonUnitalAlgEquiv` is a Mathlib TODO |
| Peirce decomposition, Jordan frame, idempotents | ❌ L | entirely absent ("Peirce" only = Peirce's law in logic) |
| quadratic rep `U_a`, triple product `{a,b,c}` | ❌ M | absent (only a doc comment) |

The total Jordan development in Mathlib is **two files (~564 lines)** — the axioms
and `SymAlg`. By contrast the Lie-algebra development is 52 files.

### 1d. JB-algebras, classification, concrete factors (report §3, §9 targets)
| Need | Status | Evidence / gap |
|---|---|---|
| JB-algebra (Jordan Banach + the 3 norm axioms) | ❌ L | NOT FOUND anywhere; only a JB\*-triple *comment* in `MStructure.lean` |
| formally real / Euclidean Jordan algebra | 🟡 M | `IsFormallyReal` is **ring-level only** (`Algebra/Ring/IsFormallyReal.lean`), no Jordan/cone/trace-form tie-in |
| JC/JW-algebras | ❌ M–L | absent |
| **JNW classification** | ❌ R | absent; scope comparable to Cartan–Killing (which Mathlib itself hasn't finished) |
| spin factor (as Jordan algebra) + its cone/norm | ❌ S–M | absent; Clifford-algebra infra exists to build on |
| `Hₙ(K)` as a Jordan algebra | 🟡 M | `IsHermitian` + `SymAlg` exist but **not connected** |
| quaternions ℍ | ✅ | `Algebra/Quaternion.lean` (rich) |
| **octonions 𝕆 / Cayley–Dickson** | ❌ M | entirely absent (only doc comments) |
| **Albert algebra `H₃(𝕆)`** | ❌ L | absent; needs octonions first |
| special/exceptional/reversible, Glennie s-identity | ❌ M–R | absent |
| Effros–Størmer (positive projection ⇒ JC range) | ❌ M–L | absent; needs JB/JC theory first |

### 1e. Order-unit spaces (the report's *central* definition) + convex/stochastic toolkit (§5, §8)
| Need | Status | Evidence / gap |
|---|---|---|
| **order-unit space + order-unit norm** | ❌ M | NOT FOUND (`OrderUnit`/`orderUnitNorm` absent); `gauge` exists to build the norm; ~300–500 lines |
| convex cones (`ConvexCone`, `PointedCone`, `ProperCone`, dual) | ✅ | `Analysis/Convex/Cone/*`; `innerDual_innerDual` |
| self-dual cone predicate | ❌ S | absent (double-dual thm present, not packaged) |
| state space of an order-unit space; Kadison–Krein duality | ❌ M | absent |
| convex hull, Carathéodory, `stdSimplex`, barycentric coords | ✅ | `convexHull`, `Caratheodory.lean`, `stdSimplex`, `AffineBasis.barycentricCoord` |
| extreme points, exposed points/faces, Krein–Milman | ✅ | `Set.extremePoints`, `IsExposed`, `KreinMilman.lean` |
| row/doubly-stochastic matrices, **Birkhoff–von Neumann** | ✅ | `rowStochastic`, `doublyStochastic`, `Birkhoff.lean` (with explicit coeffs + extreme points = permutation matrices) |
| ℓ¹/ℓ∞ on ℝⁿ, matrix `∞→∞` operator norm, Hausdorff dist | ✅ | `PiLp`, `Matrix.linfty_opNorm_*`, `hausdorffDist`, `ConvexBody` |
| **idempotent stochastic matrices** (faces as fixpoint simplices) | ❌ S–M | absent; the key object of the commutative section, ~100–200 lines |
| Minkowski–Carathéodory (fin-dim) | ❌ S | flagged absent in `KreinMilman.lean` comment; workaroundable via Birkhoff |

### 1f. Cohomology / Haar / representation toolkit (Layer-1 error reduction, §9)
| Need | Status | Evidence / gap |
|---|---|---|
| general homological algebra: complexes, `Ext`, derived cat | ✅ | `Algebra/Homology/*`, `DerivedCategory/Ext/*` |
| group cohomology `Hⁿ(G,A)`, explicit `H¹,H²` cocycle/coboundary API | ✅ | `RepresentationTheory/Homological/GroupCohomology/*` |
| Schur's lemma, Maschke, `IsSemisimpleModule`, isotypic, Wedderburn–Artin | ✅ | `RepresentationTheory/Irreducible.lean`, `Maschke.lean`; `RingTheory/SimpleModule/*` |
| Haar measure (loc. compact); average `⨍` | ✅ | `Measure/Haar/Basic.lean`, `MeasureTheory.average` |
| Banach fixed point `ContractingWith`; Newton (quadratic) | 🟡 | `ContractingWith` (linear rate); `Polynomial.newtonMap` quadratic *divisibility* only — no normed `δ↦O(δ²+ε)` |
| Lie-algebra cohomology / Whitehead `H¹=H²=0` | ❌ M | only low-degree *cochains* (`Algebra/Lie/Cochain.lean`); no cohomology groups, no Whitehead |
| Hochschild cohomology | ❌ M | absent (TODO comment only) |
| **Jordan (Penico) cohomology, Jordan 2-cocycles/coboundaries, `H²=0`** | ❌ R | entirely absent — the deepest Layer-1 gap |
| continuous-group Reynolds operator `v↦∫_G ρ(g)v dg` (Weyl trick) | ❌ M | finite-group `Representation.averageMap` exists; compact-group version absent |
| compactness of `O(n)`/`U(n)`; `Aut(J)` compact | ❌ M | `orthogonalGroup` defined; no `CompactSpace` instance |
| separability idempotent / Casimir | ❌ M | absent (the `IsSeparable` in Mathlib is field-extension separability) |
| projective/injective tensor norms, nuclear norm, Schur multipliers | ❌ M–L | all absent |

---

## 2. Answering the question: how big is the gap?

**For the project as a whole (full proofs of everything): enormous — `R` (research-scale).**
The structure theorem (Layer 1) needs Jordan cohomology + compact-group Haar
averaging + `Aut(J)` compactness + (for the matrix benchmark) Schur-multiplier
machinery, none of which exist; the classification / Albert algebra needs octonions
+ a Cartan–Killing-scale classification. These are multi-year formalisations on
their own, and several are *research-grade even to formalise the statement of the
proof*.

**But the gap is highly non-uniform, and the project's "front half" is reachable.**

- **Definitions + conjecture statements (the user's minimal goal): achievable, `M`.**
  Needs: order-unit space + order-unit norm (`❌ M`, ~300–500 lines, `gauge` helps);
  the ε-JB axioms (`S`, trivial once order-unit is in place); a JB-algebra def
  (`M`, formally-real Jordan + norm); the channel setup with `P` either defined via
  the binomial series for `sgn(2Φ−1)` (`S–M`) or *axiomatised* as a unital
  `δ`-positive idempotent close to `Φ`; then the bridge, Theorem C, near-positive
  projection stability, the classical conjecture, and the structure-theorem
  conjecture as `theorem … := sorry` statements. The commutative statements ride
  directly on existing `rowStochastic`/Birkhoff/simplex API. **This is a clean,
  bounded milestone and a real achievement.**

- **The commutative / classical section (§8) proofs: the most tractable, `M`.**
  The convex-geometry toolkit (Birkhoff, simplices, extreme/exposed points, ℓ∞ row
  norm, Hausdorff distance) is essentially complete. Hume's sharp example, rank-one
  and simplex stability, the leakage and exposed-circuit lemmas are elementary
  convex geometry. Main missing primitive: idempotent stochastic matrices as
  simplex retractions (`S–M`). A genuinely formalisable sub-project that would
  prove real theorems.

- **The bridge theorem (§6) proof: self-contained and `M`-scale.** It uses no CP,
  no classification, no cohomology — only Kadison (`❌ S`), Jordan–Schwarz
  (`❌ M`, or just its self-adjoint Kadison case which is `S`), the `cfc`
  inequalities (mostly `✅`/`S`), `‖a‖=sup_ρ|ρ(a)|` (`❌ M`, or replace by spectral
  radius), and the spectral idempotent (`S–M`). Plausibly the **first** real
  theorem of the project to formalise. The order/norm being *exact* (our design
  choice) is a real advantage here: it avoids the order-unit-space generality and
  works directly in `B(H)_sa` where `cfc` is available.

- **Theorem C / Effros–Størmer (§7): `L`.** Effros–Størmer needs JC-algebra theory
  (a unital positive projection's range as a Jordan algebra) which is absent;
  building it is a medium-large development on top of a JB-algebra definition.

- **Layer 1 (§9) and classification/factors (§3 targets): `R`.** Defer.

---

## 3. Recommended staging (if we pursue this)

1. **Milestone 0 — statements.** Order-unit space + order-unit norm; ε-JB algebra;
   JB-algebra; channel setup; state the bridge / Theorem C / NPPS / classical /
   structure-theorem as `sorry`-ed theorems. *Deliverable: the whole theory
   typechecks as a statement-level skeleton.*
2. **Milestone 1 — the bridge.** Kadison (self-adjoint), the `cfc` inequalities,
   `P` via the binomial `sgn` series, `‖·‖`-via-spectral-radius; prove
   `thm:bridge` at `O(√η)` in `B(H)_sa`.
3. **Milestone 2 — classical section.** Idempotent stochastic matrices; Hume's
   example; rank-one + simplex stability; leakage + exposed-circuit lemmas.
4. **Later — Effros–Størmer + Theorem C; then Layer-1 / classification** (each its
   own project).

Two reusable wins to upstream regardless: a clean **order-unit space / order-unit
norm** library, and **Kadison's inequality** — both are natural Mathlib
contributions independent of this project.

---

## 4. Caveats
- Grounded at Mathlib `d6dab93` (2026-05-14); Mathlib moves fast — re-check before
  committing. (CP maps and `IsFormallyReal`, e.g., are recent.)
- Effort buckets are rough; "absent" means "no reusable declaration found", not
  "impossible" — Mathlib's adjacent infrastructure often shortens the work.
- Full per-area evidence with declaration names and file paths is in the 6 subagent
  reports summarised here (run 2026-06-05).
