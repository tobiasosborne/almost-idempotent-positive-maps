# Report Review v0.2

Date: 2026-06-05.

Scope: read-only skeptical audit of Agent A's updated `report/main.tex` and
new report sections. Agent B spawned five auditors for Layer 1 mathematics,
bridge/factorization mathematics, classical stability, coverage, and
build/provenance hygiene, then checked the report locally. Gaps, errors, and
counterexamples were treated as high-value successes.

## Build And Coverage Verdict

`cd report && make` succeeds. A separate subagent build in `/tmp` also
succeeded with no unresolved references, undefined citations, duplicate labels,
or fatal errors. Remaining LaTeX warnings are typesetting only: a significant
overfull line around `09-structure-programme.tex:141`, a minor overfull line
around `04-spectral-idempotent.tex:82`, and underfull table rows in Sections 8
and 11.

Coverage is broadly good. The bridge, faithful-invariant sidequest,
near-positive projection route, classical programme, decomposable exponent
status, positivity-rounding obstruction, exact-adjoint benchmark, and open
Layer 1 status are all represented. The report is much more honest than earlier
drafts.

The report is not yet mathematically clean enough to be treated as final. The
highest-value fixes are below.

## Priority Findings

### 1. Faithful-invariant proof uses a false norm inequality

`report/sections/06b-faithful-invariant.tex:126` uses

```text
||a+tb||^2 + ||a-tb||^2 <= 2(||a||^2+t^2||b||^2).
```

This is a Hilbert/parallelogram-style inequality and is false for the
operator/order-unit norm, for example in `ell_infty^2`.

The theorem should survive with a constant change. From the displayed
polarization bound, use only

```text
||a +/- tb|| <= ||a|| + t||b||.
```

Then

```text
||h_{a,b}||
 <= C eta/(4t lambda) (||a+tb||^2+||a-tb||^2)
 <= C eta/(2t lambda) (||a||+t||b||)^2.
```

Taking `t=||a||/||b||` gives `||h_{a,b}|| <= C eta ||a||||b||/lambda` with a
new universal constant. Agent A should patch the proof line, not withdraw the
theorem.

### 2. Classical Section 8 contains two substantive precision errors

First, `report/sections/08-classical-stability.tex:122` defines exposedness by
requiring the gap for all `x in K` outside a ball. Agent B's current target in
`agent-B/notes/exposed-redundant-dichotomy-target.md` defines

```text
S_v(rho)={p_i: ||p_i-v||_1>=rho},
e_v(rho)=sup_h min_{x in S_v(rho)} h(x),
```

using outside rows, not all points of the row polytope. This is not cosmetic:
all-`K` exposedness can be stronger because convex combinations along chords can
reduce affine gaps. The report should either explicitly state it is using a
stronger sufficient target, or revert to the row-set modulus used by Agent B's
global exposed-hull notes.

Second, `08-classical-stability.tex:164` claims a nesting

```text
rank-one subset line-segment subset simplex subset (well-exposed = simplex)
```

This is false. `agent-B/notes/line-segment-classical-stability.md` explicitly
calls rank-one and line-segment complementary. A concrete rank-one positive
idempotent perturbation can have triangular row polytope, not a line segment.
Also, well-exposed separated vertices imply simplex, but not every simplex
satisfies the quantitative well-exposed hypothesis.

Moderate accompanying fix: restore small-defect thresholds in the special-case
theorems. The source notes state universal `delta0` or `eta0` hypotheses for
rank-one, simplex, well-exposed, and cluster factorization. The report often
omits them.

### 3. Layer 1 gaps are understated in the summary

`09-structure-programme.tex:49-62` correctly says approximate idempotents,
Jordan frames, Peirce decomposition, and coordinatization are separate open
steps. But `09-structure-programme.tex:284-307` summarizes the remaining gap
mostly as next-arrow/module/gauge/positivity issues. That overstates what the
exact-adjoint benchmark has bought.

Agent A should add the pre-cohomological frame/Peirce/coordinatization tasks to
`op:layer1-gap` and soften the final paragraph's "because of" language.

### 4. Exact-adjoint matrix status should match the report's own standards

The high-rank matrix exact-adjoint statement in
`09-structure-programme.tex:230-257` is marked as proved while the same section
says the final matching-reconstruction proof has not been independently
re-audited. Since `11-discussion.tex:77-80` defines proved as a complete proof
in the report or a transcribed verified proof, the cleaner status is something
like:

```text
Agent B proof claimed; exact-adjoint benchmark; independent audit pending.
```

This is a status-hygiene issue, not a discovered counterexample.

### 5. Cohomology notation and norms need definitions

The report uses `||f||_inj`, `||Sf||_{F-op}`, `J theta`, `d^2 theta`,
`dist`, and "max sector norm" without self-contained definitions. It also mixes
`d^2 theta` with the specific linearized Jordan identity operator `J theta`
used in `agent-B/notes/next-arrow-to-newton-error-reduction.md`.

Agent A should define these symbols before using constants, or consistently use
`J theta` for the next-arrow defect in this report.

Related precision issue: `09-structure-programme.tex:216-223` states the
commutative scalar module result as a max-sum theorem for every finite
dimensional unital `R^m`-module. The source notes are more careful: algebraic
decomposition is general, but the dimension-free norm-one/projection constants
require the chosen max-sector norm, or else a complementability constant enters.

### 6. Exact factorization wording needs tightening

`07-exact-factorization.tex:190-195` risks saying the Effros-Stormer range is a
Jordan subalgebra of `B(H)_sa` under the ambient product. It is not generally
closed under the ambient product; Effros-Stormer gives the range a JC/JB
structure with product `E(x o y)`. The theorem's factorization identity is
fine, but the wording should avoid contradicting Section 6b.

Also:

- `op:npps` assumes `0<delta`, but Theorem C applies it with `delta=C eta`.
  Handle `eta=0` separately with `E=P=Phi`, or allow `delta=0`.
- `07-exact-factorization.tex:117` says the best generic repair loses a square
  root. The spin example only proves any generic repair must lose at least a
  square root; it does not prove an `O(sqrt(eps))` generic repair exists.
- `08-classical-stability.tex:42` says "the two are equivalent" in a way that
  can be misread as full noncommutative `op:npps` being equivalent to the
  classical problem. It should say the two classical signed/stochastic
  formulations are equivalent.

### 7. Coverage expansions that would improve the report

The new diagonal-frame matrix next-arrow theorem is only summarized as
"diagonal-source `D x D` closed" at `09-structure-programme.tex:277-281`. A
labelled proposition or remark should record the actual theorem:

```text
||theta-Pi_n theta|| <= C ||Jtheta||
```

for fixed diagonal-frame matrix modules, with a clear warning that this closes
only fixed-frame `D x D`, not full matrix next-arrow. Add a provenance row for
`agent-B/notes/diagonal-frame-matrix-next-arrow-walsh-target.md`.

The full-matrix source decomposition target deserves one paragraph spelling out

```text
J = D direct_sum E,
D x D closed,
D x E leakage open,
E x E Peirce curvature/matching open.
```

The report also should explicitly say that arbitrary exact UP factorization
promises UP maps through special JB/JC targets, not decomposable factor maps;
decomposable factor maps require an added reversible/universally reversible
hypothesis.

### 8. Provenance and hygiene fixes

The build/provenance auditor found these concrete issues:

- `report/PROVENANCE.md:21`: `A-FIND` hash is stale. Current prefix is
  `22c97155f2622acb`, and `agent-a-findings` is now v0.13, not v0.11.
- `report/PROVENANCE.md:23`: `A-ER` hash is stale. Current prefix is
  `72f1492a724f21a`.
- `report/PROVENANCE.md:39`: `A-SPIN` hash is stale. Current prefix is
  `57f23abbbe80cb74`.
- `report/PROVENANCE.md:31`: `agent-B/notes/subagent-positivity-rounding.md`
  has no hash. Current prefix is `45d7f0afddcd6701`.
- `report/PROVENANCE.md:89`: "Agent B correction in Section 8" is ambiguous or
  stale after section renumbering. If it means `A-FIND Section 8`, say so.
- `09-structure-programme.tex:17` uses label `thm:jordan-structure` for an
  `openproblem`. The ledger marks it open, but the prefix is misleading.
- Several labelled, status-bearing remarks have ledger rows but no local
  `% PROV:` marker immediately above them.
- Status vocabulary drifts: the introduction defines only proved/cited/
  consensus/open, while later sections use obstruction, numerical,
  source-extracted, and benchmark.
- `07-exact-factorization.tex:226` has the typo `||a-a|| <= small`.
- `11-discussion.tex:42` says "the two genuinely open problems" but lists
  three: exponent, exact factorization/projection stability, and Layer 1.
- `11-discussion.tex:141-148` says each open problem has been reduced to a
  single sharply stated lemma. That is too strong for Layer 1, where several
  pre-cohomological and matrix next-arrow blocks remain.

## Recommended Patch Order For Agent A

1. Patch the faithful-invariant polarization proof.
2. Fix Section 8 exposedness, false nesting, and missing small-defect
   thresholds.
3. Add pre-cohomological Layer 1 gaps to `op:layer1-gap`; define cochain
   norms/operators; deconflate `d^2 theta` and `J theta`.
4. Tighten Effros-Stormer wording and small exact-factorization edge cases.
5. Update provenance hashes/status vocabulary/typos.
6. Add a labelled diagonal-frame next-arrow result and a short full-matrix
   source-decomposition paragraph.

## Subagents Used

- Nash: Layer 1/Jordan mathematical audit.
- Sartre: positive-map bridge, faithful invariant state, exact factorization.
- Pasteur: classical stability and near-positive projection coverage.
- Helmholtz: development coverage audit.
- Parfit: build/provenance/status hygiene audit.

None of these agents edited files.
