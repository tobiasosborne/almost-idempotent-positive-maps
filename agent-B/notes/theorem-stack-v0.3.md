# Theorem Stack v0.3

This is Agent B's current consensus candidate after:

- the `O(sqrt(eta))` algebraic bridge proof, verified by Agent A v0.5 and
  re-audited during the report review;
- the positivity-rounding obstruction;
- the classical projection-stability reduction;
- the decomposable doubled-route stress test.

Prefer this file over `theorem-stack-v0.2.md`.

## Definition: Epsilon-JB Order-Unit Algebra

A finite-dimensional real order-unit space `(A,A_+,1)` with order-unit norm and
a commutative bilinear product `*` is an `epsilon`-JB order-unit algebra if:

1. `1*a=a` exactly.
2. `||a*b|| <= (1+epsilon)||a||||b||`.
3. `||a*a|| >= (1-epsilon)||a||^2`.
4. `a*a >= -epsilon ||a||^2 1`.
5. `||((a*a)*b)*a - (a*a)*(b*a)|| <= epsilon ||a||^3 ||b||`.

The order-unit structure is exact; only the product axioms are approximate.

## Theorem 1: Abstract Algebraic Stability

Desired Layer 1 theorem:

There are universal constants `epsilon0,C` such that every finite-dimensional
`epsilon`-JB order-unit algebra with `epsilon<epsilon0` is `C epsilon`-close to
a genuine finite-dimensional JB algebra.

Status: open. Agent A's proposed cohomological error-reduction route still
needs a dimension-free bounded Jordan cohomology splitting, not just qualitative
`H^2=0`. See `agent-B/notes/layer1-agent-a-review-v0.1.md`.
A local literature check of Baak--Moslehian J*-homomorphism stability and
Chu--Russo/Penico cohomology is recorded at
`agent-B/notes/known-jstar-stability-literature-check.md`; it confirms that
these sources do not provide the required dimension-free epsilon-JB product
stability theorem.

Exact-cohomology diagnostics and partial benchmarks now proved:

The following results are **not** Theorem 1. They are exact cochain-level
benchmarks, mostly for adjoint or explicitly decomposed exact modules. They
are useful because they rule out several apparent obstructions and now close
the high-rank matrix exact-adjoint benchmark, but they do not yet provide
arbitrary module control, approximate-cocycle projection, approximate-module
error control, or a positivity/concrete output for factorization.

- **Adjoint spin factors.** For `V=R1+H`, exact adjoint coboundaries have an
  `O(H)`-equivariant Euclidean-injective right inverse with
  `||S f||<=2||f||`; using the spin rank-two norm comparison gives an
  order-unit adjoint spin constant `<=4 sqrt(2)`. See
  `agent-B/notes/adjoint-spin-splitting-theorem.md`. The normalized spin
  next-arrow estimate is also proved: if `theta(1,z)=0`, then
  `dist(theta,im d^1)<=C||Jtheta||`, by reducing the vector part to a
  dimension-free Hilbert lemma for nearly radial quadratic maps. See
  `agent-B/notes/spin-normalized-cocycle-projection-reduction.md`.
- **Adjoint direct sums.** If every simple summand `B_r` has an exact adjoint
  right inverse with constant `K_r`, then `B=direct_sum_r B_r` has one with
  constant at most `max_r K_r+1`. The off-block primitive components are
  recovered by `P_r f(e_r,x_{\ne r})`, avoiding any sum over the number of
  ideals. See `agent-B/notes/adjoint-direct-sum-reduction.md`.
- **Finite-dimensional adjoint JB algebras.** Combining the spin, matrix,
  fixed Albert, and direct-sum results gives a universal exact-adjoint
  splitting constant for every finite-dimensional JB algebra, modulo the
  derivation kernel. See
  `agent-B/notes/finite-dimensional-adjoint-jb-splitting-corollary.md`.
- **Conditional Newton bookkeeping.** If a unit-normalized product
  perturbation `x*y=x o y+theta(x,y)` has exact-complex constants
  `K_1` for inverting exact coboundaries and `K_2` for the next-arrow estimate
  `dist(theta,im d^1)<=K_2||Jtheta||`, then the coordinate change
  `T=I-h`, `d^1h` close to `theta`, improves
  `delta=||theta||` by the Newton rule
  `delta -> C(K_1,K_2)(epsilon+delta^2)`. The expansion is
  `Def_*=Jtheta+O(delta^2)`, and the transported product has
  `theta'=theta-d^1h+O(delta||h||+||h||^2)`. This is recorded in
  `agent-B/notes/next-arrow-to-newton-error-reduction.md`. It is not a
  global Layer 1 proof; it says the perturbative bookkeeping is ready once the
  relevant exact-complex estimates and approximate-module robustness are
  supplied.
- **Spin direct sums.** Combining the preceding two items, arbitrary finite
  direct sums of spin factors have exact adjoint order-unit splittings with
  constant at most `4 sqrt(2)+1`, independent of all spin dimensions and of
  the number of summands. See
  `agent-B/notes/spin-direct-sum-adjoint-corollary.md`.
- **Bounded-rank adjoint factors.** For every fixed rank cutoff `R0`, finite
  direct sums of arbitrary spin factors, matrix factors `H_n(F)` with
  `n<=R0`, and Albert factors have an exact adjoint splitting constant
  depending only on `R0`, not on spin dimensions or summand count. This uses
  finite-dimensional closed-range linear algebra for the finitely many
  bounded-rank non-spin factors, plus the adjoint direct-sum reduction. See
  `agent-B/notes/bounded-rank-adjoint-reduction.md`.
- **Exact commutative modules.** Every finite-dimensional exact unital module
  over `R^m` decomposes algebraically into coordinate sectors `x_i` and
  half-sum sectors `(x_p+x_q)/2`. In the max sector norm, the support-unit
  formula `S f(x)=f(x,s)` gives a norm-one splitting, including arbitrary
  vector-valued multiplicities, and `Pi=d^1S` is a projection onto `im(d^1)`
  with norm at most `3`. For an arbitrary module norm, the bound is controlled
  by the complementability constant of the sector projections. See
  `agent-B/notes/commutative-scalar-module-splitting.md`. The corresponding
  approximate-cocycle projection estimate is also proved for these scalar
  sectors: `dist(theta,im d^1)<=12||Jtheta||`, including the Peirce `1/2`
  half-sum modules. See
  `agent-B/notes/commutative-scalar-cocycle-projection-theorem.md`.
- **High-rank matrix caveat and resolution.** The commutative sector result does not solve
  the matrix families. In `H_n(R)`, the off-diagonal Peirce lines for the
  diagonal frame are individually half-sum scalar sectors of norm `1`, but
  their coherent sum `sum_{i<j}(E_ij+E_ji)=11^T-I` has operator norm `n-1`.
  This rules out the naive proof that splits in max sector norm and then
  includes all sectors into the ambient matrix norm. It is not a lower bound
  for exact coboundary inversion: a Rademacher/Schur-multiplier formula gives
  a dimension-free right inverse for the restriction of the adjoint
  `H_n(F)` module to a fixed diagonal `R^n` frame, and `Pi=d^1S` projects onto
  `im(d^1)` with norm at most `33`. The corresponding approximate-cocycle
  next-arrow estimate is also proved in
  `agent-B/notes/diagonal-frame-matrix-next-arrow-walsh-target.md`: after the
  support-unit residual is decomposed into `A`, `B`, `U`, and `W` modes, the
  `A/B` modes are recovered by diagonal signs, the `U` mode by sparse
  `{0,+-1}` signs, and the tail-tail `W` mode by a two-density sparse-sign
  identity
  `Q_W(y)=(64/3)T_{1/4}(y)-4T_{1/2}(y)`. Hence
  `dist(theta,im d^1)<=C||Jtheta||` and
  `||theta-Pi theta||<=C'||Jtheta||` for fixed diagonal-frame matrix modules,
  dimension-free. This fixed-frame construction transports to every Jordan
  frame with the same constants. But naive averaging over
  frames does not globalize it: the averaged diagonal pinching acts on the
  traceless part by
  `(n-1)/(dim_R H_n(F)-1)`, so reconstructing global traceless data costs a
  rank-sized factor. A separate cochain-norm caveat shows that one cannot ask
  for Frobenius-bounded primitives for order-bounded exact coboundaries:
  in `H_n(R)`, `h(x)=x_11 1` has `||h||_op=1`, `||h||_F=sqrt(n)`, and
  `||d^1h||_op<=3`; every primitive of `d^1h` has Frobenius norm at least
  `sqrt(n)`. This high-Frobenius phenomenon is harmless in order norm for the
  central-valued component: for `h_phi(x)=phi(x)1` on `H_n(F)`,
  `F=R,C,H`, the restriction of `d^1` has a norm-one inverse on its range,
  `||h_phi||<=||d^1h_phi||`, by evaluating at the spectral sign of `phi`. See
  also `agent-B/notes/multiplication-primitive-estimate.md` for the
  factor-independent estimate on multiplication primitives:
  `h(x)=c o x` satisfies `||h||<=||d^1h||<=3||h||` by evaluating at `(1,1)`.
  Consequently `agent-B/notes/unit-normalized-adjoint-reduction.md` reduces
  the full exact adjoint problem to unit-vanishing coboundaries with normalized
  primitive `h(1)=0`: remove `L_{f(1,1)}`, leaving a residual 2-cochain of norm
  at most `4||f||`. Another controlled normalized matrix subspace is recorded
  in `agent-B/notes/trace-zero-rank-one-matrix-primitive-estimate.md`:
  `h(x)=phi(x)c` with `phi(1)=0` satisfies
  `(1/2)||h||<=||d^1h||<=3||h||`, uniformly in `n` and `F=R,C,H`.
  But `agent-B/notes/nuclear-rank-one-route-caveat.md` explains why this
  cannot be naively summed over rank-one decompositions: the nuclear norm of
  `Id_{J_0}` is at least `dim J_0` while its operator norm is `1`.
  The fixed-frame Peirce reduction first gave a dimension-free pointwise
  estimate for leakage from one source off-diagonal Peirce sector into all
  other sectors after the diagonal derivation gauge. The coherent
  globalization is now proved in
  `agent-B/notes/off-sector-leakage-globalization-theorem.md`: on operators
  from the full off-diagonal Peirce space to `J`, the averaged squared
  diagonal-sign commutator
  `R(T)=E_epsilon ad_{epsilon}^2(T)` has eigenvalues
  `0,1/2,1,3/2`, with kernel exactly the sector-preserving maps. Since
  `R(h|_E)=E_epsilon ad_epsilon([L_epsilon,h|_E])` and
  `[L_epsilon,h|_E]` is bounded by the coboundary plus the controlled diagonal
  restriction, the polynomial inverse on `{1/2,1,3/2}` controls the full
  leakage operator in order norm.
  The fixed-frame sector-preserving problem asks for control of the edge maps
  `S_ij:V_ij->V_ij`, modulo frame-stabilizer derivations for `F=C,H`, from the
  full Jordan derivation defect on products `V_ij x V_jk -> V_ik`, together
  with the leakage globalization. The one-dimensional real scalar Schur
  subcase and the pure diagonal-skew matching-curvature subcase are now
  controlled; together they close the scalar Hermitian Schur/connection
  residual. A separate finite-phase extraction controls the anti-linear
  Peirce edge field in `H_n(C)`, so the fixed-frame sector-preserving
  residual for `H_n(C)` is also controlled after formal leakage removal.
  The quaternionic internal Peirce edge maps are also controlled by finite
  quaternionic coefficient extraction and row-gauge random reconstruction.
  Thus the fixed-frame matrix residual is closed after the diagonal gauge. See
  `agent-B/notes/fixed-frame-peirce-matrix-reduction.md`. In the real
  sector-preserving subcase this becomes a concrete bilinear Schur problem:
  control the Schur-multiplier norm of edge weights `m_ij` by the Jordan
  triangle-defect bilinear multiplier with coefficients
  `m_ij+m_jk-m_ik`. The full coordinate formula is
  `(d^1M_m(x,y))_ik=(1/2)sum_j(m_ij+m_jk-m_ik)(x_ij y_jk+y_ij x_jk)`, with
  diagonal square-detection terms. The middle-slice identity
  `m_ik=m_ip+m_pk-(m_ip+m_pk-m_ik)` does not settle the ordinary norm problem:
  through a fixed vertex `p`, ordinary bilinear tests see only rank-one
  products `x_ip y_pk`, not arbitrary Schur multiplier inputs. This real
  symmetric Schur problem is now solved by random matching reconstruction:
  `||M_m||<=60||d^1M_m||_inj`. See
  `agent-B/notes/sector-preserving-schur-residual.md` and
  `agent-B/notes/real-symmetric-matching-reconstruction-theorem.md`.
  In the complex skew sector, diagonal frame-stabilizer derivations are exactly
  the additive gauges `beta_ij=alpha_i-alpha_j`, and the coboundary on
  `V_ij x V_jk -> V_ik` has coefficient
  `beta_ij+beta_jk-beta_ik`; see
  `agent-B/notes/complex-skew-connection-residual.md`.
  The coefficientwise version of this target is false as a proof strategy:
  in the complex skew-connection sector, a block-embedded triangular sign
  multiplier has uniformly bounded edge weights and pointwise triangle
  curvatures, but its Hermitian Schur multiplier norm grows like the norm of
  the triangular projection, i.e. logarithmically. See
  `agent-B/notes/pointwise-schur-curvature-caveat.md`.
  A sidecar audit found that the natural Haagerup factorization route plausibly
  proves a completely bounded bilinear version of the residual estimate, but
  not the ordinary order/operator bilinear estimate needed here; extracting a
  fixed middle slice is an amplification step. See
  `agent-B/notes/subagent-schur-residual-audit-v0.1.md`.
  However, bounded matching inputs detect full Schur slices. For any Hermitian
  sector symbol `mu` and disjoint blocks `I,J,K`, testing `d^1S_mu` on an
  `I-J` block matrix and a matching `pi:J->K` controls the ordinary Schur
  multiplier with symbol
  `kappa_pi(i,j)=mu_ij+mu_{j,pi(j)}-mu_{i,pi(j)}`. The block triangular
  skew-connection example is the special case where this recovers one half of
  the arbitrary triangular sign Schur multiplier `i(sign o A)`, so that stress
  family has logarithmic ordinary bilinear defect and is not a counterexample.
  See `agent-B/notes/matching-slice-schur-detection.md`.
  The resulting standalone analytic target is the matching-curvature
  reconstruction estimate: control the Schur multiplier norm of `mu`, modulo
  diagonal gauge `i(alpha_a-alpha_b)`, by the supremum of all matching-slice
  Schur norms. Its exact kernel is right: zero triangle curvature forces a
  diagonal derivation gauge. A local tripartite version is proved: for
  disjoint equal blocks `I,J,K`, the `I-J` block is reconstructed after a
  block-local average gauge by averaging matching curvature slices over
  bijections `J->K`. The global gluing step is now also proved for pure skew
  symbols by averaging over random disjoint triples of blocks: for
  `mu=i beta`, `dist_gamma2(mu,Der_diag)` is at most a universal constant
  times the matching-slice supremum, hence at most a universal constant times
  `||d^1S_mu||`. Combining this with the real symmetric reconstruction theorem
  gives the scalar Hermitian sector estimate
  `dist(M_mu,Der_diag)<=84||d^1M_mu||_inj` for fixed-frame scalar residuals in
  `H_n(C)`. See
  `agent-B/notes/matching-curvature-reconstruction-target.md` and
  `agent-B/notes/pure-skew-matching-reconstruction-theorem.md`, and
  `agent-B/notes/hermitian-scalar-sector-reconstruction-corollary.md`.
  The anti-linear complex edge field
  `B_b X_ij(z)=X_ij(b_ij conj(z))` is even more directly controlled: two
  matching tests with `w=1` and `w=i`, followed by the finite phase projection
  `(G(A)+iG(iA))/2`, extract the rectangular anti-Schur slice
  `b_ij conj(A_ij)`. Random block averaging gives `||B_b||<=40||d^1B_b||`,
  and the general complex sector-preserving edge map satisfies the crude
  fixed-frame estimate
  `dist(S_A,Der_diag)<=124||d^1S_A||_inj`. See
  `agent-B/notes/complex-antilinear-peirce-residual-theorem.md`.
  The quaternionic sector-preserving target is controlled in
  `agent-B/notes/quaternionic-internal-peirce-residual-theorem.md`: for
  `S_A X_ij(z)=X_ij(A_ij z)`, `A_ij in End_R(H)`, control
  `dist(S_A,{u_i z-z u_j})` by the norm of the bilinear internal curvature
  `A_ij(z)w+zA_jk(w)-A_ik(zw)`. Finite matched tests in unit quaternions
  extract the mixed `L_{Im}R_{Im}` rectangular slices directly and extract
  the left/right row-difference slices modulo the expected diagonal gauge;
  random matching reconstruction then gives the fixed-frame estimate.
  A sidecar audit anticipated the dual route via matched-triangle filling; the
  averaging theorem supplies the primal proof for the pure skew case. See
  `agent-B/notes/subagent-matching-curvature-audit-v0.1.md`.
  Two sidecar audits found no order-norm counterexample; the strongest stress
  test is Schur-multiplier families with logarithmic primitive norm, but their
  coboundaries appear to grow logarithmically as well. See
  `agent-B/notes/subagent-matrix-representation-audit-v0.1.md` and
  `agent-B/notes/subagent-matrix-obstruction-audit-v0.1.md`.
  See
  `agent-B/notes/peirce-sector-norm-accumulation.md` and
  `agent-B/notes/diagonal-frame-matrix-module-splitting.md`,
  `agent-B/notes/frame-covariance-and-global-matrix-obstacle.md`,
  `agent-B/notes/cochain-norm-conversion-caveat.md`,
  `agent-B/notes/central-valued-matrix-primitive-estimate.md`,
  `agent-B/notes/multiplication-primitive-estimate.md`,
  `agent-B/notes/unit-normalized-adjoint-reduction.md`, and
  `agent-B/notes/trace-zero-rank-one-matrix-primitive-estimate.md`, and
  `agent-B/notes/nuclear-rank-one-route-caveat.md`, and
  `agent-B/notes/fixed-frame-peirce-matrix-reduction.md`,
  `agent-B/notes/sector-preserving-schur-residual.md`,
  `agent-B/notes/real-symmetric-matching-reconstruction-theorem.md`,
  `agent-B/notes/complex-skew-connection-residual.md`,
  `agent-B/notes/pointwise-schur-curvature-caveat.md`,
  `agent-B/notes/subagent-schur-residual-audit-v0.1.md`,
  `agent-B/notes/matching-slice-schur-detection.md`,
  `agent-B/notes/matching-curvature-reconstruction-target.md`,
  `agent-B/notes/pure-skew-matching-reconstruction-theorem.md`,
  `agent-B/notes/hermitian-scalar-sector-reconstruction-corollary.md`,
  `agent-B/notes/complex-antilinear-peirce-residual-theorem.md`,
  `agent-B/notes/quaternionic-internal-peirce-target.md`,
  `agent-B/notes/quaternionic-internal-peirce-residual-theorem.md`,
  `agent-B/notes/off-sector-leakage-globalization-theorem.md`,
  `agent-B/notes/matrix-factor-exact-adjoint-splitting-theorem.md`,
  `agent-B/notes/finite-dimensional-adjoint-jb-splitting-corollary.md`,
  `agent-B/notes/subagent-matching-curvature-audit-v0.1.md`,
  `agent-B/notes/subagent-matrix-representation-audit-v0.1.md`, and
  `agent-B/notes/subagent-matrix-obstruction-audit-v0.1.md`.

Current status taxonomy:

- Closed in the exact-adjoint benchmark, modulo the standard derivation
  kernel: spin factors, finite spin direct sums, bounded-rank simple factors
  and direct sums, all high-rank matrix factors `H_n(F)`, `F=R,C,H`,
  multiplication primitives, central-valued matrix primitives, trace-zero
  rank-one matrix primitives, exact commutative scalar modules in max sector
  norm, fixed diagonal-frame matrix restrictions, coherent off-sector leakage,
  and sector-preserving edge-map residuals. Combining the matrix theorem with
  the adjoint direct-sum reduction closes the finite-dimensional adjoint
  JB-algebra benchmark in order norm.
- No exact-adjoint simple-factor family is currently left open by the matrix
  benchmark. This is not yet Theorem 1.
- Still outside the exact-adjoint benchmark and required for Theorem 1:
  arbitrary relevant Jordan modules, approximate cocycles, approximate-module
  errors, dimension-free projection onto the cocycle/coboundary image, and a
  positivity-capable or concrete comparison output. See
  `agent-B/notes/layer1-after-adjoint-benchmark-obligations.md`.
  The commutative scalar, normalized spin adjoint, and fixed diagonal-frame
  matrix module next-arrow tests are now positive. The matrix/internal Peirce
  next-arrow problem is still not globally closed because full
  noncommutative matrix cochains, compatibility across frames, arbitrary
  relevant modules, and approximate-module robustness remain. The next
  high-rank matrix target is decomposed in
  `agent-B/notes/full-matrix-next-arrow-source-decomposition-target.md`:
  `D x D` is closed, while `D x E` cochain-level leakage and `E x E` Peirce
  curvature/matching are open.

For the positive-map factorization theorem, this algebraic version is not
enough by itself. A useful Layer 1 output must additionally provide at least
one of:

- positive near-inverse maps;
- a nearby concrete JC-subalgebra in the ambient `B(H)_sa`;
- a comparison theorem strong enough to pair with near-positive projection
  stability.

See `agent-B/notes/layer1-output-requirements.md`.

## Theorem 2: Algebraic Positive-Map Bridge

Let `H` be finite-dimensional and let `Phi:B(H)_sa -> B(H)_sa` be unital
positive with

```text
||Phi^2-Phi|| <= eta
```

in operator norm. For small `eta`, set

```text
P=theta(2Phi-I),        A=Im P,        a*b=P(a o b),
```

where `a o b=(ab+ba)/2`.

Then Agent B's theorem is:

```text
(A,*,1,A_+ inherited from B(H)_sa)
is an O(sqrt(eta))-JB order-unit algebra.
```

Status: proved internally at the `O(sqrt(eta))` scale. Detailed proof:
`agent-B/theory/theorem-B-algebraic-bridge.md`. Agent A reports a line-by-line
verification in `agent-a-findings` v0.5 §10. Agent B's report-review pass on
2026-06-02 found no local algebraic error in Section 6 of `report/`; it did
patch status/provenance and small-threshold wording around the theorem. The
spectral-idempotent estimate is proved directly by the Banach-algebra formula
`sgn(S)=S(S^2)^(-1/2)` for `S=2Phi-I`, after fixing a small universal
threshold `eta0`.

Proof ingredients:

1. Spectral calculus gives `P^2=P`, `P(1)=1`, `||P-Phi||=O(eta)`,
   `||P||<=1+O(eta)`, and `P` is `O(eta)`-positive.
2. Since `A=Im P` is a unital self-adjoint real subspace, the inherited cone
   `A cap B(H)_+` gives an exact Archimedean order-unit space and its
   order-unit norm is exactly the ambient operator norm.
3. Jordan-Schwarz for `Phi` gives first insertion:
   `||P(Px o b)-P(x o b)||<=C sqrt(eta)||x||||b||` for `b in A`.
4. Square holes `q_r=P(r^2)-r^2` are almost positive kernel elements. After a
   positivity shift, `||P(q_r^2)||<=C eta||r||^4`.
5. Polarization gives arbitrary product-hole bounds from the square-hole
   bounds; then Cauchy-Schwarz gives hole-hole and hole-range estimates, which
   close the Jordan identity at `O(sqrt(eta))`.

The proof now explicitly isolates the standard order estimates used in these
steps: Jordan-Schwarz for unital positive maps on self-adjoint elements,
Cauchy-Schwarz for positive functionals, positive-cone norm monotonicity, and
the state-supremum formula for self-adjoint norms. It also makes explicit the
self-adjoint order-perturbation rule
`||x-y||<=epsilon => x>=y-epsilon 1`, used in the square-hole lower bound. No
CP/cb input is used in the bridge proof.

This theorem does not require `P` to be positive. `P` can fail positivity even
classically.

## Theorem 3: Conditional Exact UP Factorization

Assume near-positive projection stability at the sharp square-root scale:
every `delta`-positive unital idempotent `P:B(H)_sa -> B(H)_sa` with
`||P||<=1+delta` is `O(sqrt(delta))`-close to a unital positive idempotent.

Then for `Phi` as in Theorem 2 there exist a finite-dimensional special JB/JC
algebra `J` and unital positive maps

```text
Delta:J -> B(H)_sa,
Upsilon:B(H)_sa -> J
```

such that

```text
||Delta Upsilon - Phi|| <= C sqrt(eta),
Upsilon Delta = id_J,
Upsilon(Delta(x) o Delta(y)) = x*y        (x,y in J).
```

This implication is now written as a theorem-level proof in
`agent-B/theory/theorem-C-conditional-factorization.md`. It uses the spectral
estimate for `P=theta(2Phi-I)`, the assumed projection-stability theorem to
replace `P` by a positive idempotent `E`, and exact Effros-Stormer on `E`.
The proof now explicitly justifies the real-to-complex step: a unital positive
idempotent `E:B(H)_sa->B(H)_sa` extends complex-linearly to a unital positive
projection on `B(H)`, so Effros-Stormer applies and restricts back to the real
self-adjoint range with product `E(x o y)`. It also checks positivity of the
factor maps against the chosen cones: inclusion is positive for
`J_+=J cap B(H)_+`, and `E(V_+) subset J_+`.
The proof now also verifies cone compatibility: the JB positive cone of the
Effros-Stormer product equals the inherited cone `J cap B(H)_+`. One inclusion
uses `x*x=E(x o x)` and positivity of `E`; the other uses the unital JB
criterion `z>=0 iff || ||z||1-z ||<=||z||` together with the inherited Banach
norm.

If instead Theorem 1 is proved with a positivity-capable/concrete output, an
analogous exact factorization should follow by comparing `P` to the canonical
positive expectation onto the nearby concrete JC algebra. That route is not yet
formalized.

Status: the implication from near-positive projection stability is proved
conditionally; the projection-stability theorem itself remains open. Exact
factorization is not proved from algebraic stability alone.

Reason: generic dimension-free `O(epsilon)` positivity rounding is false for
finite-dimensional JB targets. A spin-factor example gives maps that are
`epsilon`-positive but at distance at least `sqrt(epsilon)` from every positive
unital map. See `agent-B/notes/factorization-positivity-rounding.md`.

The near-positive projection-stability route is also open. Its commutative
version is equivalent, up to constants, to:

```text
Q row-stochastic, ||Q^2-Q||_{infty->infty} <= eps
  => dist(Q, stochastic idempotents) <= C sqrt(eps).
```

No proof or citation for this dimension-free Markov theorem has been found.
Linear projection stability is false already in `ell_infty^3`, so the
square-root exponent is sharp if true. See
`agent-B/notes/near-positive-projection-stability-program.md`.

Several nontrivial classical facts are now proved:

- rank-one signed perturbations `P=I-u v^T` are `O(sqrt(delta))`-close to
  stochastic idempotents; this class contains the sharp Hume family
  (`agent-B/notes/rank-one-classical-stability.md`);
- exact signed affine retractions whose row polytope is a simplex are
  `O(sqrt(delta))`-close to stochastic idempotents with a universal constant
  independent of the number of vertices
  (`agent-B/notes/simplex-classical-stability.md`). The line-segment theorem
  is the two-vertex case (`agent-B/notes/line-segment-classical-stability.md`).
- bounded binary-coordinate dependencies are impossible at small defect:
  if rows `r_a` have distinct binary code words witnessed by affine functions
  `s_1,...,s_m:K->[0,1]`, then
  `||sum_a c_a r_a||_1 >= (1-C m sqrt(delta)) sum_a |c_a|`. In particular,
  exact parallelogram row polytopes and fixed-complexity non-simplex
  product-of-simplexes vertex geometries cannot occur for small `delta`
  when their factor coordinates are bounded on all of `K`
  (`agent-B/notes/parallelogram-classical-stability.md`).

The remaining non-simplex classical problem is reduced, for the simplex-based
route, to constructing `O(sqrt(delta))` approximate simplex coordinates for
row polytopes; see `agent-B/notes/approximate-simplexity-reduction.md`. The
bounded-coordinate lemma suggests a second route through angle-free
bounded-coordinate/dependency-cancellation decompositions.
The coordinate reduction is now robust to small signed coordinate errors:
`agent-B/notes/robust-approximate-simplexity-reduction.md` shows that it is
enough for the affine coordinate vectors to have coefficient negative mass
`O(delta)` and reconstruction error `O(sqrt(delta))`; exact pointwise
nonnegativity of the coordinates is not required.
Wegener's sidecar report
`agent-B/notes/subagent-exposed-redundant-classical-v0.1.md` sharpens the
remaining target further: well-exposed separated vertices satisfy an intrinsic
`l1` circuit-cancellation bound. The formal proof of the cancellation bound is
`agent-B/notes/exposed-circuit-cancellation.md`; the exposedness-modulus
local target is `agent-B/notes/exposed-redundant-dichotomy-target.md`.
Hubble's later stress test shows that a pointwise exposed-or-redundant
deletion lemma is not sufficient by itself: redundancy can be circular and
sequential deletion can accumulate error. The current non-accumulating target
is the global exposed-hull lemma in
`agent-B/notes/simultaneous-skeleton-reduction.md`: if
`W_{rho,kappa}` is the set of vertices exposed at
`rho=O(sqrt(delta))` with gap `kappa>=c sqrt(delta)`, then every row should be
`O(sqrt(delta))`-close to `conv W_{rho,kappa}`.
The branch where all row-polytope vertices are separated and well exposed is
now a proved stability case:
`agent-B/notes/well-exposed-classical-stability.md` shows the vertices must be
affinely independent, hence the row polytope is a simplex and the simplex
stability theorem applies.
The merge-compatible extension
`agent-B/notes/cluster-representative-classical-stability.md` proves stability
when well-exposed representative rows have disjoint clusters and all other
rows are `O(sqrt(delta))`-close to their convex hull. This removes the need
for global affine simplex coordinates in that subcase.
This row-polytope theorem has been packaged as an exact commutative
positive-map factorization theorem:
`agent-B/theory/classical-cluster-factorization-theorem.md` proves that an
almost-idempotent row-stochastic map whose spectral idempotent satisfies the
cluster-representative geometry factors, up to `O(sqrt(eta))`, through a
commutative special JB algebra by unital positive maps. It now also records
the corollary that the global exposed-hull hypothesis implies the same exact
factorization conclusion.

The target `J` should be special JB/JC. It is not reversible in general.
Decomposable factor maps require reversible/universally reversible target
structure or separate hypotheses.

## Theorem 4: Dilation-Compatible `O(eta)` Bridge

There is a valid Kitaev-strength theorem under a stronger lifted hypothesis.

Suppose there are:

- a finite-dimensional C*-algebra `D`;
- a unital order-isometric Jordan embedding `j:M_sa -> D_sa`;
- a unital positive map `C:D_sa -> M_sa`;
- `Phi=Cj`;
- `F=jC` extends to a UCP map `D -> D`;
- `||F^2-F||_cb <= eta`.

Then for

```text
P=theta(2Phi-I),        A=Im P,        a*b=P(a o b),
```

`A` is an `O(eta)` epsilon-JB order-unit algebra.

Status: proved by reduction to Kitaev's UCP theorem. See
`agent-B/notes/decomposable-dilation-compatible-theorem.md`.

This is **not** automatic from an arbitrary CP+coCP decomposition. The naive
doubled route fails: `Phi=Cj` can be exactly idempotent while `jC` has order-one
idempotence defect. See `agent-B/notes/decomposable-doubling-obstruction.md`.
Sartre also found that bad decompositions of the exact depolarizing projection
can have off-diagonal universal-envelope defect despite `eta=0`; see
`agent-B/notes/subagent-decomposable-alpha1-stress.md`.

## Theorem 5: Decomposable `O(eta)` Conjecture

Conjectural strengthening:

If `Phi` is unital positive, almost idempotent, and admits a controlled
CP+coCP decomposition

```text
Phi = Phi_0 + Psi_0 o tau,
Phi_0,Psi_0 CP,
Phi_0(1)+Psi_0(1)=1,
```

then the bridge in Theorem 2 improves from `O(sqrt(eta))` to `O(eta)`.

Status: open. The standard decomposable norm is the wrong hypothesis:
transpose on `M_n` is unital positive decomposable but has standard
Haagerup/Wittstock decomposable norm `n`. The component bounds above are the
right boundedness input, but not enough by themselves to justify the naive
doubled proof. A proof must either:

- choose a compatible decomposition/lift satisfying a lifted almost-idempotence
  estimate; or
- prove a direct intrinsic CP/coCP two-hole cancellation for the Jordan defect.

See `agent-B/notes/decomposable-alpha1-route.md`.

## Exact Consistency

When `eta=0`, `P=Phi` is a unital positive projection. Effros-Stormer applies:
`P(B(H)_sa)` is a JC algebra for

```text
r*s=P(r o s).
```

The stack above reduces to this exact result.
