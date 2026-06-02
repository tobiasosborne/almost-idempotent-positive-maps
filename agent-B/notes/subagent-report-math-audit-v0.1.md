# Subagent Report: Math Audit Of Report Sections 04--08

Date: 2026-06-02.

Scope audited:

- `report/sections/04-spectral-idempotent.tex`
- `report/sections/05-epsilon-jb.tex`
- `report/sections/06-bridge-theorem.tex`
- `report/sections/07-structure-programme.tex`
- `report/sections/08-discussion.tex`

Consensus baseline used:

- `agent-B/notes/compaction-checkpoint.md`
- `agent-b-findings`
- `agent-a-findings`
- `agent-B/theory/theorem-B-algebraic-bridge.md`
- `agent-B/theory/theorem-C-conditional-factorization.md`
- `agent-B/notes/theorem-stack-v0.3.md`
- `agent-B/notes/stochastic-stoquastic-special-cases.md`
- supporting Agent B notes for Layer 1 output and decomposable `O(eta)`.

High-level verdict: the local estimates transcribed in Section 06 match the
current theorem-B proof draft/proof object. I did not find a local algebraic
mistake in Lemmas 0--5 or the Jordan-identity bookkeeping. The main issues are
status/hypothesis overclaims and a few wording errors that could make open or
conditional material look proved.

## Findings

### 1. Bridge theorem status is stronger than Agent B's current status labels

Location:

- `report/sections/06-bridge-theorem.tex:6-7`
- `report/sections/06-bridge-theorem.tex:27-56`
- `report/sections/06-bridge-theorem.tex:86-97`, `139-151`, `187-202`,
  `268-276`, `320-332`, `380-392`, `426-433`
- `report/sections/08-discussion.tex:136-138`

Issue:

The report labels the algebraic bridge and all internal lemmas/propositions as
`\textsc{(proved)}` and says the proof is "verified". Current Agent B durable
files still label the arbitrary-UP bridge as a proof candidate/proof draft
pending Agent A review:

- `agent-B/notes/compaction-checkpoint.md:33`
- `agent-B/notes/theorem-stack-v0.3.md:70-81`
- `agent-b-findings:659-661`

There is a conflict because current `agent-a-findings` v0.5 says Agent A
verified theorem B. If the report is meant to follow Agent B consensus files,
Section 06 is ahead of the durable Agent B status.

Suggested correction language:

```tex
This section records Agent B's theorem-B proof draft/proof candidate. Agent A's
current findings report a line-by-line verification, but Agent B's theorem stack
has not yet been promoted from proof-candidate status.
```

Then replace the theorem and lemma status tags by something like
`\textsc{(proof candidate; Agent A verified)}` until Agent B promotes the status
in `theorem-stack-v0.3.md` / `agent-b-findings`. If the intention is instead to
promote it to proved, update the Agent B consensus files first.

### 2. Spectral estimate states uniform `O(eta)` up to `eta<1/4`, which is false as written

Location:

- `report/sections/04-spectral-idempotent.tex:47-58`
- proof especially `report/sections/04-spectral-idempotent.tex:80-91`

Issue:

`lem:P-properties` says there is a universal constant `C` for all
`eta<1/4`, including `||R-I||<=C eta`. But the proof gives
`2 eta/(1-4 eta)`, which is not bounded by a universal multiple of `eta` as
`eta -> 1/4`. The theorem-B source only uses this after decreasing a small
threshold `eta0`.

Suggested correction language:

```tex
There are universal constants $\eta_0<1/4$ and $C$ such that, whenever
$0\le\eta\le\eta_0$, ...
```

or keep the explicit bound:

```tex
\|R-\Id\|\le \frac{2\eta}{1-4\eta},
```

and only later specialize to `eta<=eta0` to obtain `O(eta)`.

### 3. The `delta`-isomorphism definition incorrectly equates norm control with order control

Location:

- `report/sections/05-epsilon-jb.tex:67-90`
- especially `report/sections/05-epsilon-jb.tex:86-87`
- provenance comment `report/sections/05-epsilon-jb.tex:12`

Issue:

The definition requires unit control, approximate multiplicativity, and a
two-sided norm estimate. It does not require positivity, approximate positivity,
or order preservation. The sentence

```tex
Equivalently, a $\delta$-isomorphism is an approximate order-isomorphism ...
```

is therefore not justified. This matters because Agent B's current Layer 1
consensus explicitly says algebraic/normed stability is not enough for exact UP
factorization; Layer 1 must also output positivity/concrete comparison data
(`agent-B/notes/layer1-output-requirements.md:1-33`,
`agent-B/notes/theorem-stack-v0.3.md:42-51`).

The provenance comment also says theorem B proves "the delta-isomorphism"; it
does not.

Suggested correction language:

```tex
This is an algebraic/normed notion of approximate Jordan isomorphism. It does
not by itself encode positivity or order preservation; those are additional
requirements in the positive-map factorization problem.
```

If an order notion is intended, add explicit conditions such as approximate
positive-cone preservation for both `v` and `v^{-1}`.

### 4. Layer 1 frame paragraph suggests the spectral idempotent supplies element idempotents

Location:

- `report/sections/07-structure-programme.tex:60-69`

Issue:

The paragraph discusses approximate idempotent elements / Jordan frames, then
says "the spectral idempotent `P` ... already supplies the analytic device."
`P` is an idempotent linear map, not an approximate idempotent element of the
epsilon-JB algebra. Current consensus keeps Layer 1 idempotent/frame
construction open.

Suggested correction language:

```tex
The spectral-idempotent construction is the map-level analogue that produced
the epsilon-JB product; it does not by itself produce the approximate Jordan
frame elements needed for Layer 1.
```

### 5. Section 07's "resolution" paragraph overstates the averaging route in the order-unit norm

Location:

- `report/sections/07-structure-programme.tex:193-225`
- `report/sections/07-structure-programme.tex:227-236`
- `report/sections/07-structure-programme.tex:257-280`

Issue:

The later numerical paragraph correctly says the order-unit/operator-norm
bounded homotopy remains unresolved. But the preceding paragraph is headed "The
resolution" and says the Jordan analogue "carries this over", that the
separability idempotent has an averaging representation with projective norm
`<=1`, and that contracting against it "yields" `K=O(1)`.

This is too strong relative to Agent B consensus. The larger unitary group of
the multiplication algebra is compatible with trace/Frobenius norms, not the
order-unit norm required by the theorem. Agent B's current obligation note says
Haar/Reynolds averaging is only a norm-one projection, not a right inverse to
the Jordan coboundary, and the non-invariant components are exactly where
dimension/rank dependence can enter
(`agent-B/notes/layer1-quantitative-obligations-v0.2.md:79-95`).

Suggested correction language:

```tex
\paragraph{Candidate averaging mechanism.}
The multiplication-algebra Haar average gives a dimension-free-looking
separability-idempotent representation in trace/Frobenius norms. It is not yet
a dimension-free order-unit-norm contracting homotopy. The open problem is to
replace this by an Aut(J)-compatible order-unit construction, or to avoid the
global homotopy by an incremental argument.
```

Also avoid saying it "yields a homotopy `s` with `K=O(1)`" before the open
operator-norm estimate is proved.

### 6. `O(eta)` exponent discussion misses the precise UCP/cb and dilation-compatible hypotheses

Location:

- `report/sections/08-discussion.tex:18-21`
- `report/sections/08-discussion.tex:24-49`
- status row `report/sections/08-discussion.tex:139-141`

Issue:

The text says the Kitaev-strength exponent is "available for completely positive
maps" and "conjectural for positive maps." Current Agent B consensus is more
specific:

- Kitaev's `O(eta)` result is under UCP/cb-style hypotheses, not merely an
  operator-norm almost-idempotent CP hypothesis.
- A proved `O(eta)` bridge exists under the stronger dilation-compatible
  lifted-UCP hypothesis (`agent-B/notes/theorem-stack-v0.3.md:240-262`).
- General decomposable `O(eta)` is conjectural and requires controlled CP+coCP
  data or a direct two-hole proof; the naive doubled route fails
  (`agent-B/notes/theorem-stack-v0.3.md:271-296`).

Suggested correction language:

```tex
Kitaev's $O(\eta)$ exponent is available in the UCP/cb setting, and Agent B has
a valid $O(\eta)$ bridge under the stronger dilation-compatible lifted-UCP
hypothesis. For arbitrary unital positive maps the proved/candidate bridge is
only $O(\sqrt\eta)$. A decomposable $O(\eta)$ bridge remains conjectural unless
one assumes such a compatible lifted-UCP model or proves an intrinsic CP/coCP
two-hole cancellation.
```

The decomposable formula at `08-discussion.tex:45-49` should also include the
component-control hypothesis:

```tex
\Phi=\Phi_0+\Psi_0\circ\tau,\qquad
\Phi_0,\Psi_0 \text{ CP},\qquad \Phi_0(1)+\Psi_0(1)=1.
```

Do not phrase this in terms of the standard decomposable norm.

### 7. Macro/notation typos in the exponent paragraph obscure the mathematics

Location:

- `report/sections/08-discussion.tex:30`
- `report/sections/08-discussion.tex:43`
- `report/sections/08-discussion.tex:46`

Issue:

These are not just cosmetic: they use report macros with the wrong meaning.

- `\omega=\rho\jp\Phimap` should be composition, not Jordan product.
- `uses \Img\,\mathrm{id}_n\otimes\Phimap` should not use the image macro.
- `\Psi_0\jp\tau` should be composition with transpose/opposite leg, not
  Jordan product.

Suggested correction language:

```tex
\omega=\rho\circ\Phimap
```

```tex
uses the amplification $\mathrm{id}_n\otimes\Phimap$
```

```tex
\Phi=\Phi_0+\Psi_0\circ\tau
```

### 8. "Approximate factor maps" is too strong unless qualified as non-positive/algebraic

Location:

- `report/sections/08-discussion.tex:52-58`

Issue:

The bridge gives an approximate JB algebra and an algebraic linear
factorization through `A=Im P` using inclusion and `P`, but `P` need not be
positive. Current consensus says exact UP factor maps require projection
stability or positivity-capable/concrete Layer 1 output
(`agent-B/theory/theorem-B-algebraic-bridge.md:3-5`,
`agent-B/theory/theorem-C-conditional-factorization.md:1-5`,
`agent-B/notes/layer1-output-requirements.md:21-33`).

Suggested correction language:

```tex
The bridge yields an approximate Jordan algebra and a linear algebraic
factorization of the nearby idempotent $P$ through $A=\operatorname{Im}P$.
These maps are not known to be positive. Producing exact unital-positive factor
maps requires more...
```

### 9. Classical projection-stability wording suggests more is known than is known

Location:

- `report/sections/08-discussion.tex:91-97`

Issue:

The text says projection stability "is known classically only at the
square-root scale." The current Agent B state is that the full dimension-free
classical Markov/stochastic theorem is open; several special cases are proved
at square-root scale, and Hume's family shows linear stability is false if the
full theorem is true. See
`agent-B/notes/stochastic-stoquastic-special-cases.md:11-30`,
`agent-B/notes/stochastic-stoquastic-special-cases.md:166-192`.

Suggested correction language:

```tex
In the classical setting, linear stability is false and the proved special
cases occur at the sharp square-root scale. The full dimension-free stochastic
projection-stability theorem remains open.
```

### 10. Exceptional/special target language conflates Layer 1 with the channel factorization target

Location:

- `report/sections/08-discussion.tex:120-122`
- `report/sections/08-discussion.tex:148-150`
- compare `report/sections/07-structure-programme.tex:33-45`

Issue:

Section 07 states an abstract Layer 1 target into a genuine finite-dimensional
JB algebra, which may include exceptional summands unless one proves a special
output theorem. Section 08 then says "Exceptional algebras excluded (target is
special)" and that "the bridge target inherits this." This is true only for the
channel/exact-factorization target obtained from a concrete positive projection
or nearby JC subalgebra. It is not true of the abstract Layer 1 theorem as
stated.

Suggested correction language:

```tex
Exceptional JB factors are excluded from the concrete channel/factorization
target, because Effros--Stormer produces a special JB/JC algebra. The abstract
Layer 1 stability theorem, as stated in Section 7, is a theorem about finite
dimensional JB algebras in general and should not be described as excluding
the Albert algebra unless the target is explicitly restricted to special JB
algebras.
```

Also add the Agent B consensus warning:

```tex
The special target need not be reversible; decomposable factor maps require
reversible/universally reversible structure or separate hypotheses.
```

### 11. Status ledger undercounts the open problems

Location:

- `report/sections/08-discussion.tex:125-167`

Issue:

The table correctly lists Layer 1 as open, exact factorization as open, and
decomposable `eta` as open. But the prose immediately after the table says
"The two genuinely open problems are independent" and then treats Layer 1 as a
"third" reason. This is confusing and understates the current Agent B theorem
stack, which has three separate open/conditional components:

1. abstract Layer 1 dimension-free stability;
2. exact UP factorization via projection stability or positivity-aware Layer 1;
3. decomposable/general `O(eta)` strengthening.

Suggested correction language:

```tex
There are three separate unresolved components: the decomposable/lifted
$O(\eta)$ exponent, exact UP factorization via projection stability or
positivity-aware Layer 1 output, and the abstract Layer 1 dimension-free
stability theorem.
```

### 12. Reversible/decomposable warning should be explicit in the report status

Location:

- `report/sections/08-discussion.tex:100-123`
- `report/sections/08-discussion.tex:125-155`

Issue:

The report says the target is special, but does not explicitly record the Agent
B consensus that arbitrary positive-map targets are not reversible in general
and decomposable factor maps require reversible/universally reversible targets
or extra hypotheses (`agent-B/notes/theorem-stack-v0.3.md:236-238`,
`agent-b-findings:207-210`).

Suggested correction language:

```tex
Special/concrete does not imply reversible. Therefore the baseline
positive-map factorization should promise unital positive maps only.
Decomposable factor maps are a separate corollary under reversible or
universally reversible target hypotheses, or under explicit dilation-compatible
assumptions.
```

