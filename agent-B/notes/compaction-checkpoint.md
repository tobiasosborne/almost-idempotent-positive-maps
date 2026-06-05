# Agent B Compaction Checkpoint

Last updated: 2026-06-05, Europe/Berlin.

## Resume Protocol: Read This First

This file is the durable state for Agent B. After any context compaction or
fresh resume, do the following before taking new mathematical action:

1. Read this file from the top, including the last numbered item.
2. Read root `agent-b-findings`; it is the current message to Agent A and the
   canonical public summary of Agent B's position.
3. Read root `agent-a-findings` for new Agent A claims; do not assume the
   conversation summary has the latest Agent A state.
4. If working on a theorem or proof file, read that exact file before editing
   it. The most important current files are:
   - `agent-B/notes/theorem-stack-v0.3.md`;
   - `agent-B/theory/theorem-B-algebraic-bridge.md`;
   - `agent-B/theory/theorem-C-conditional-factorization.md`;
   - `agent-B/theory/classical-cluster-factorization-theorem.md`;
   - `agent-B/notes/layer1-quantitative-obligations-v0.2.md`;
   - `agent-B/notes/known-jstar-stability-literature-check.md`;
   - `agent-B/notes/approximate-simplexity-reduction.md`;
   - `agent-B/notes/robust-approximate-simplexity-reduction.md`;
   - `agent-B/notes/subagent-exposed-redundant-classical-v0.1.md`;
   - `agent-B/notes/exposed-circuit-cancellation.md`;
   - `agent-B/notes/well-exposed-classical-stability.md`;
   - `agent-B/notes/cluster-representative-classical-stability.md`;
   - `agent-B/notes/exposed-redundant-dichotomy-target.md`;
   - `agent-B/notes/simultaneous-skeleton-reduction.md`;
   - `agent-B/notes/stochastic-stoquastic-special-cases.md`;
   - `agent-B/notes/audit-consensus-2026-06-04.md`;
   - `agent-B/notes/regular-polygon-retraction-obstruction.md`;
   - `agent-B/notes/symmetric-coordinate-negative-mass-criterion.md`;
   - `agent-B/notes/response-to-agent-a-v0.12-layer1-caveat.md`;
   - `agent-B/notes/spin-splitting-audit-2026-06-05.md`;
   - `agent-B/notes/adjoint-spin-splitting-theorem.md`;
   - `agent-B/notes/spin-normalized-cocycle-projection-reduction.md`;
   - `agent-B/notes/adjoint-direct-sum-reduction.md`;
   - `agent-B/notes/spin-direct-sum-adjoint-corollary.md`;
   - `agent-B/notes/bounded-rank-adjoint-reduction.md`;
   - `agent-B/notes/commutative-scalar-module-splitting.md`;
   - `agent-B/notes/commutative-coordinate-cocycle-projection.md`;
   - `agent-B/notes/commutative-scalar-cocycle-projection-theorem.md`;
   - `agent-B/notes/peirce-sector-norm-accumulation.md`;
   - `agent-B/notes/diagonal-frame-matrix-module-splitting.md`;
   - `agent-B/notes/diagonal-frame-matrix-next-arrow-walsh-target.md`;
   - `agent-B/notes/full-matrix-next-arrow-source-decomposition-target.md`;
   - `agent-B/notes/frame-covariance-and-global-matrix-obstacle.md`;
   - `agent-B/notes/cochain-norm-conversion-caveat.md`;
   - `agent-B/notes/central-valued-matrix-primitive-estimate.md`;
   - `agent-B/notes/multiplication-primitive-estimate.md`;
   - `agent-B/notes/unit-normalized-adjoint-reduction.md`;
   - `agent-B/notes/trace-zero-rank-one-matrix-primitive-estimate.md`;
   - `agent-B/notes/nuclear-rank-one-route-caveat.md`;
   - `agent-B/notes/fixed-frame-peirce-matrix-reduction.md`;
   - `agent-B/notes/sector-preserving-schur-residual.md`;
   - `agent-B/notes/real-symmetric-matching-reconstruction-theorem.md`;
   - `agent-B/notes/complex-skew-connection-residual.md`;
   - `agent-B/notes/pointwise-schur-curvature-caveat.md`;
   - `agent-B/notes/subagent-schur-residual-audit-v0.1.md`;
   - `agent-B/notes/matching-slice-schur-detection.md`;
   - `agent-B/notes/matching-curvature-reconstruction-target.md`;
   - `agent-B/notes/pure-skew-matching-reconstruction-theorem.md`;
   - `agent-B/notes/hermitian-scalar-sector-reconstruction-corollary.md`;
   - `agent-B/notes/complex-antilinear-peirce-residual-theorem.md`;
   - `agent-B/notes/quaternionic-internal-peirce-target.md`;
   - `agent-B/notes/quaternionic-internal-peirce-residual-theorem.md`;
   - `agent-B/notes/off-sector-leakage-globalization-theorem.md`;
   - `agent-B/notes/matrix-factor-exact-adjoint-splitting-theorem.md`;
   - `agent-B/notes/finite-dimensional-adjoint-jb-splitting-corollary.md`;
   - `agent-B/notes/layer1-after-adjoint-benchmark-obligations.md`;
   - `agent-B/notes/next-arrow-to-newton-error-reduction.md`;
   - `agent-B/notes/report-review-v0.2.md`;
   - `agent-B/notes/subagent-matching-curvature-audit-v0.1.md`;
   - `agent-B/notes/subagent-matrix-representation-audit-v0.1.md`;
   - `agent-B/notes/subagent-matrix-obstruction-audit-v0.1.md`.
5. Preserve the status labels:
   - arbitrary-UP algebraic bridge: proved internally at `O(sqrt(eta))`, with
     Agent A v0.5 line-by-line verification and Agent B report-review audit;
   - exact UP factorization: conditional on projection stability or a
     positivity-capable Layer 1 output;
   - abstract Layer 1 stability: open;
   - decomposable `O(eta)` theorem: conjectural except under the stronger
     dilation-compatible lifted-UCP hypothesis.

After each substantial conclusion, update this checkpoint and then update
`agent-b-findings`. Do not leave new mathematical state only in chat.

## Current Resume Snapshot

Last verified after Agent A's report update and Agent B report audit v0.2 on
2026-06-05.

- Agent B added `agent-B/notes/report-review-v0.2.md` after deploying five
  skeptical read-only report-audit subagents. The report builds, and coverage is
  broadly good, but required fixes remain: the faithful-invariant proof uses a
  false parallelogram-type operator-norm inequality; Section 8's exposedness
  target uses all of `K` instead of the outside row set and contains a false
  nesting claim for classical special cases; several small-defect hypotheses are
  omitted; Layer 1 still underreports the pre-cohomological
  idempotent/frame/Peirce/coordinatization gaps; cochain notation/norms need
  definitions; the high-rank matrix exact-adjoint status should reflect
  independent re-audit pending; and provenance hashes/status vocabulary need
  cleanup. See the note before relying on the report as final.

- Agent B patched `agent-B/notes/theorem-stack-v0.3.md` to make the status
  taxonomy explicit. The exact-adjoint benchmark below Theorem 1 is now closed
  for finite-dimensional adjoint JB-algebra factors and direct sums in order
  norm: spin factors, matrix factors, bounded-rank exceptional pieces, and
  direct sums are controlled modulo the derivation kernel. This still does not
  settle arbitrary modules, approximate cocycles, approximate-module errors,
  or positivity/concrete output.

- Agent B added `agent-B/notes/fixed-frame-peirce-matrix-reduction.md`.
  After unit-normalization and subtracting the derivation detected on a fixed
  diagonal frame, random diagonal signs give a pointwise estimate for
  off-sector leakage from a source Peirce edge `V_ij`: for `x in V_ij`,
  `||(I-P_ij)h(x)|| <= C||d^1h||||x||` with dimension-free `C`. The key
  operator is
  `R_ij A=E_epsilon (L_epsilon-l_ij(epsilon)I)^2A`, whose Peirce eigenvalues
  are `0,1/2,1,3/2`, invertible with universal constants off `V_ij`. This was
  later globalized in
  `agent-B/notes/off-sector-leakage-globalization-theorem.md` by applying the
  same diagonal-sign spectral gap to the full operator space
  `B(E,J)`: `R(T)=E_epsilon ad_epsilon^2(T)` has kernel exactly the
  sector-preserving maps and spectrum `1/2,1,3/2` on leakage maps.
- Agent B added `agent-B/notes/sector-preserving-schur-residual.md` and
  `agent-B/notes/real-symmetric-matching-reconstruction-theorem.md`. In the
  real fixed-frame sector-preserving subcase, if
  `h(s_ij)=m_ij s_ij`, then
  `d^1h(s_ij,s_jk)=(1/2)(m_ij+m_jk-m_ik)s_ik` for distinct `i,j,k`, and
  `d^1h(s_ij,s_ij)=2m_ij(e_i+e_j)`. Thus the real residual is a concrete
  bilinear Schur multiplier problem. The note includes the full coordinate
  formula:
  `(d^1M_m(x,y))_ik=(1/2)sum_j(m_ij+m_jk-m_ik)(x_ij y_jk+y_ij x_jk)` and
  `(d^1M_m(x,y))_ii=2sum_{j != i}m_ij x_ij y_ij`. It also records the
  middle-slice caveat: fixing a base vertex `p` only sees rank-one products
  `x_ip y_pk` in the ordinary bilinear norm, so it does not by itself extract
  a full Schur multiplier slice. The random matching reconstruction theorem
  now closes this real scalar residual: for
  `S=sup ||M_{kappa_pi}||`, `E=sup_{i != j}|m_ij|`, the all-matrix Schur
  extension satisfies `||M_m||<=24(S+E)`, and the square/matching lower bounds
  give `||M_m||<=60||d^1M_m||_inj`.
- Agent B added `agent-B/notes/complex-skew-connection-residual.md`. For
  `H_n(C)`, the skew sector-preserving residual has
  `K_beta X_ij(z)=X_ij(i beta_ij z)` with `beta_ji=-beta_ij`. Diagonal
  frame-stabilizer derivations are exactly the gauges
  `beta_ij=alpha_i-alpha_j`, and
  `d^1K_beta(X_ij(z),X_jk(w))=(i/2)(beta_ij+beta_jk-beta_ik)X_ik(zw)`. Thus
  the complex skew target is a complete-graph connection estimate in Schur
  multiplier norm, modulo additive gauges.
- Agent B added `agent-B/notes/pointwise-schur-curvature-caveat.md`. In the
  complex skew-connection sector, a block-embedded triangular sign symbol has
  uniformly bounded edge coefficients and bounded pointwise triangle
  curvatures, but its Hermitian Schur multiplier norm grows logarithmically
  with `n` by the classical triangular-projection theorem of
  Kwapien--Pelczynski. Thus the residual matrix proof must use the full
  bilinear operator norm of the Jordan defect, not only pointwise
  edge/curvature bounds.
- Sidecar agent Ramanujan produced
  `agent-B/notes/subagent-schur-residual-audit-v0.1.md`. It found no
  counterexample to the real residual estimate
  `||M_m|| <= C||D_m||_inj`, but it identifies an ordinary-vs-cb gap in the
  natural Haagerup route. Fixing a base vertex writes
  `m_ik=m_ip+m_pk-kappa(i,p,k)`, so a cb-bilinear Schur norm may control
  `gamma_2(m)`, but extracting a fixed middle slice from the ordinary bilinear
  injective norm is an amplification step not yet justified.
- Agent B added `agent-B/notes/matching-slice-schur-detection.md`. It proves
  a general matching-slice lower bound. For any Hermitian sector symbol `mu`
  and disjoint blocks `I,J,K`, testing `d^1S_mu` on an `I-J` block matrix and
  a matching `pi:J->K` controls the ordinary Schur multiplier with symbol
  `kappa_pi(i,j)=mu_ij+mu_{j,pi(j)}-mu_{i,pi(j)}`. In the block triangular
  skew-connection stress family in `H_{3n}(C)`, this gives `L-R` block
  `(1/2)i(sign o A)` for arbitrary `A in M_n(C)`. Thus the triangular sign
  family has logarithmic ordinary bilinear defect, not just logarithmic
  primitive Schur norm, and is not a counterexample. The remaining issue is
  whether all residual Schur norm can be recovered from matching curvature
  slices plus square-detected edge weights.
- Agent B added `agent-B/notes/matching-curvature-reconstruction-target.md`.
  It packages the sharp standalone analytic target for the complex skew
  sector: control `dist_gamma2(mu,Der_diag)` by the supremum of all matching-slice
  Schur norms, where `Der_diag` consists of symbols
  `i(alpha_a-alpha_b)`. The exact kernel is correct: if
  `mu_ab+mu_bc-mu_ac=0` for all distinct triples, then Hermiticity forces
  `mu_ab=i(s_b-s_a)`, hence a diagonal derivation gauge. The note now proves
  a local tripartite reconstruction: for pure skew `mu=i beta` and disjoint
  equal blocks `I,J,K`, the `I-J` block after the average gauge
  `alpha_i=avg_K beta_ik`, `alpha_j=avg_K beta_jk` equals the average over
  matching curvature slices `kappa_pi`, hence its Schur norm is controlled by
  their supremum.
- Agent B added `agent-B/notes/pure-skew-matching-reconstruction-theorem.md`.
  It proves the global gluing for pure skew symbols. For `N=|Omega|>=3`, let
  `m=floor(N/3)` and average the local tripartite gauges over ordered
  disjoint triples of `m`-subsets. This reconstructs
  `beta_ab-(r_a/N-r_b/N)`, `r_a=sum_c beta_ac`, as `lambda^{-1}E nu_ab` with
  `lambda^{-1}<=2` and `||M_{i nu}||<=6S`, where `S` is the matching-slice
  Schur supremum. Hence
  `dist_gamma2(i beta,Der_diag)<=12S<=24||d^1S_{i beta}||_inj`. The pure
  complex skew sector-preserving residual is therefore dimension-free
  controlled. Together with the real scalar reconstruction theorem, the
  one-dimensional Schur/connection residuals are no longer the main
  obstruction. The later complex anti-linear and quaternionic notes control
  the internal Peirce edge maps after formal leakage removal; the later
  leakage theorem globalizes off-sector leakage.
- Agent B added
  `agent-B/notes/hermitian-scalar-sector-reconstruction-corollary.md`. For a
  scalar Hermitian symbol `mu=u+i beta`, combining the real symmetric and pure
  skew matching reconstructions gives
  `dist(M_mu,Der_diag)<=36S+24E`, where `S` is the matching-slice Schur
  supremum and `E=sup |Re mu_ij|`. In a fixed-frame scalar residual for
  `H_n(C)`, matching slices and square terms give
  `dist(M_mu,Der_diag)<=84||d^1M_mu||_inj`.
- Agent B added
  `agent-B/notes/complex-antilinear-peirce-residual-theorem.md`. For the
  anti-linear edge field `B_b X_ij(z)=X_ij(b_ij conj(z))`, two matching tests
  with `w=1` and `w=i` extract the rectangular anti-Schur slice
  `b_ij conj(A_ij)`, and random block averaging gives
  `||B_b||<=40||d^1B_b||_inj`. For a general complex sector-preserving edge
  map `S_A X_ij(z)=X_ij(a_ij z+b_ij conj(z))`, finite phase projections
  separate scalar and anti-linear curvature, yielding the crude fixed-frame
  estimate `dist(S_A,Der_diag)<=124||d^1S_A||_inj` after formal off-sector
  leakage removal. Therefore the fixed-frame sector-preserving residual for
  `H_n(C)` is controlled modulo diagonal gauge.
- Agent B added `agent-B/notes/quaternionic-internal-peirce-target.md` and
  `agent-B/notes/quaternionic-internal-peirce-residual-theorem.md`. For
  `S_A X_ij(z)=X_ij(A_ij z)`, `A_ij in End_R(H)`, the triangle defect is
  `C_A(i,j,k)(z,w)=A_ij(z)w+zA_jk(w)-A_ik(zw)`, and diagonal gauges are
  `G_u,ij(z)=u_i z-z u_j`. The coefficient extraction is now proved. For the
  mixed `L_{Im}R_{Im}` part, with `U={1,i,j,k}` and matching block maps
  `T_w(z)=C_A(i,j,pi(j))(z,w)`, the average
  `G=(1/4)sum_{w in U}R_{conj(w)}T_w` satisfies `P_MG=P_MA_ij`, so mixed
  slices are directly controlled. For the left/right component
  `A_ij(z)=p_ij z-zp_ji`, the same finite tests extract row-difference slices
  `p_ij-p_ik`; random row-gauge reconstruction gives
  `dist(S_A,{G_u})<=C||d^1S_A||_inj` after formal leakage removal. Therefore
  the fixed-frame sector-preserving residual is controlled for
  `H_n(R)`, `H_n(C)`, and `H_n(H)`.
- Agent B added `agent-B/notes/off-sector-leakage-globalization-theorem.md`.
  For `H=h|_E:E->J`, after the diagonal gauge,
  `[L_a,H]x=f(a,x)-h(a)o x`. For diagonal signs, set
  `ad_epsilon(T)=L_epsilon T-TL_epsilon|_E` and
  `R(T)=E_epsilon ad_epsilon^2(T)`. On maps from source `V_ij` to a target
  Peirce sector, `R` has eigenvalue
  `E(lambda_W(epsilon)-l_ij(epsilon))^2`, equal to `0` only for
  `W=V_ij` and otherwise one of `1/2,1,3/2`. Since
  `R(H)=E ad_epsilon([L_epsilon,H])`, the fixed polynomial inverse on
  `{1/2,1,3/2}` gives `||(I-P_sec)h|_E||<=C||d^1h||_inj`.
- Agent B added
  `agent-B/notes/matrix-factor-exact-adjoint-splitting-theorem.md`. Combining
  unit normalization, diagonal gauge, global leakage control, and the
  sector-preserving edge-map theorems gives
  `dist(h,Der(H_n(F)))<=C||d^1h||_inj` for `F=R,C,H`, uniformly in `n`, for
  exact adjoint coboundaries. Together with the spin, bounded-rank, and
  direct-sum notes, this closes the exact-adjoint finite-dimensional JB
  benchmark in order norm. Layer 1 remains open for arbitrary modules,
  approximate cocycles/errors, and positivity/concrete output.
- Agent B added
  `agent-B/notes/finite-dimensional-adjoint-jb-splitting-corollary.md`, which
  records the assembled exact-adjoint result for every finite-dimensional JB
  algebra: `dist(h,Der(B))<=C||d^1h||_inj`, uniformly over dimension and
  number of simple summands. This is still only exact adjoint cohomology, not
  the Layer 1 error-reduction theorem.
- Agent B added
  `agent-B/notes/layer1-after-adjoint-benchmark-obligations.md`. The precise
  next cohomological gap is not inversion of `d^1` on exact coboundaries, but
  a dimension-free projection/closed-range estimate for approximate
  2-cocycles:
  `dist(theta,im d^1)<=C||d^2theta||`, plus robustness under approximate
  module actions and the derivation gauge. This is the current Layer 1
  frontier unless the proof is forced to use an incremental Peirce/frame
  version instead of a global estimate.
- Agent B added
  `agent-B/notes/commutative-coordinate-cocycle-projection.md` and
  `agent-B/notes/commutative-scalar-cocycle-projection-theorem.md`. For
  scalar irreducible modules over `R^m`, including coordinate modules and
  half-sum Peirce `1/2` modules, the support-unit projection satisfies the
  next-arrow estimate `dist(theta,im d^1)<=12||Jtheta||`, where `Jtheta` is
  the two-variable linearized Jordan identity defect. Thus commutative scalar
  sectors, including mixed Peirce `1/2` modules, are not the approximate
  2-cocycle obstruction.
- Agent B upgraded
  `agent-B/notes/spin-normalized-cocycle-projection-reduction.md` to a
  theorem. For normalized spin adjoint 2-cochains `theta(1,z)=0`, write
  `theta(x,y)=c(x,y)1+D(x,y)` on the vector part. The scalar part is an exact
  coboundary. The vector defect satisfies
  `J_D(a,b)=<a,b>D(a,a)-<b,D(a,a)>a`, hence
  `||J_D||=sup_{||a||=1}||P_{a^\perp}D(a,a)||`. A Hilbert-space lemma for
  nearly radial quadratic maps gives
  `inf_u||D-D_u||<=(2sqrt(2)+2)||J_D||`, where
  `D_u(x,y)=<u,x>y+<u,y>x`. Thus normalized spin next-arrow estimates are
  dimension-free.
- Agent B added
  `agent-B/notes/diagonal-frame-matrix-next-arrow-walsh-target.md`. The fixed
  diagonal-frame exact projection `Pi_n=d^1S_n` is dimension-free, and the
  next-arrow estimate is now also proved:
  `||theta-Pi_n theta||<=C||Jtheta||`. After the scalar support-unit
  normalization, each off-diagonal residual decomposes into `A`, `B`, `U`, and
  `W` modes. The diagonal coordinate sectors and all four off-diagonal modes
  admit matrix-valued Walsh/Rademacher reconstructions from `Jtheta` with
  universal constants: `A` and `B` by ordinary diagonal signs, `U` by sparse
  `{0,+-1}` signs, and `W` by the two-density identity
  `Q_W(y)=(64/3)T_{1/4}(y)-4T_{1/2}(y)`. Thus fixed diagonal-frame matrix
  modules are not a next-arrow obstruction.
- Agent B added `agent-B/notes/next-arrow-to-newton-error-reduction.md`. This
  closes the abstract perturbative bookkeeping conditional on exact-complex
  estimates: for a unit-normalized perturbation `x*y=x o y+theta(x,y)`,
  `Def_*=Jtheta+O(||theta||^2)`, and if exact constants `K_1` for inverting
  coboundaries and `K_2` for `dist(theta,im d^1)<=K_2||Jtheta||` are
  available, then a coordinate change `T=I-h` gives the Newton improvement
  `delta -> C(K_1,K_2)(epsilon+delta^2)`. This does not prove global Layer 1;
  it reduces the remaining work to proving the exact-complex estimates in the
  relevant modules and controlling approximate-module errors.
- Agent B added
  `agent-B/notes/full-matrix-next-arrow-source-decomposition-target.md`. This
  records the next high-rank matrix target after the diagonal-frame theorem:
  decompose a full adjoint 2-cochain by source type
  `theta_DD`, `theta_DE`, `theta_EE` relative to a fixed frame
  `J=D direct_sum E`. The `D x D` block is closed by the diagonal-frame Walsh
  theorem. The open fixed-frame blocks are `D x E` cochain-level leakage,
  expected to use the same diagonal-sign spectral gap as the exact-adjoint
  leakage theorem, and `E x E` Peirce curvature/matching, expected to use
  triangle/matching tests in operator norm.
- Sidecar agent Averroes produced
  `agent-B/notes/subagent-matching-curvature-audit-v0.1.md`. It found no
  counterexample to matching-curvature reconstruction. It reformulates the
  proof route dually: because Schur multiplier norm is `gamma_2`, quotienting
  by gauges reduces to divergence-free edge witnesses. The decisive remaining
  lemma is a dimension-free filling result expressing every divergence-free
  Schur-dual edge witness as a controlled sum/average of matched triangle
  layers.
- Sidecar agent Nietzsche produced
  `agent-B/notes/subagent-matrix-representation-audit-v0.1.md`. It found no
  order-norm counterexample to dimension-free exact-adjoint matrix splitting.
  It confirms that frame averaging and rank-one summation are proof-route
  failures, not lower bounds, and identifies the large non-scalar irreducible
  pieces (`S^4_0`, `V_(3,1)` for `H_n(R)` and analogous `U_s`, `U_a` for
  `H_n(C)`) as the next decisive representation-theoretic targets.
- Sidecar agent Poincare produced
  `agent-B/notes/subagent-matrix-obstruction-audit-v0.1.md`. It found no
  genuine obstruction. It emphasizes that the right lower-bound target is
  `dist(h,Der(J)) >> ||d^1h||`, since `||d^1h||/||h||` can be made small by
  adding a large derivation. The strongest stress test found was logarithmic
  Schur multipliers, but structured tests suggest their coboundaries grow
  logarithmically too.

- `agent-a-findings` is at Agent A v0.12. Agent A retracted the stale
  "dimension-free obstruction resolved in principle" claim in
  `agent-A/theory/01-error-reduction.md`, discharged Agent B's faithful-section
  report requests, and proposed a spin-factor-first Layer 1 attack.
- Agent B responded in
  `agent-B/notes/response-to-agent-a-v0.12-layer1-caveat.md`. Main
  correction: Agent A's direct-sum reduction is automatic for adjoint or
  block-respecting modules, but not for arbitrary Jordan modules. The
  one-dimensional off-diagonal Peirce module for `R \oplus R` inside `H_2(R)`
  has `(a,b)` acting by `(a+b)/2`, so central idempotents act by `1/2` and
  `d^1` has mixed components. For `R^m`, scalar unital Jordan modules are
  coordinate evaluations or half-sums of two coordinates, so these pairwise
  Peirce-`1/2` modules are intrinsic. Any summand-count reduction for the ER
  lemma must explicitly rule out or uniformly control such mixed components.
- Agent B agrees with Agent A's element-level symmetry/idempotent equivalence
  `c=(1+s)/2 => c*c-c=(s*s-1)/4`, and has no objection to a spin-first
  operator-norm splitting attack as a diagnostic, provided the module class is
  stated and R2 incrementalism remains the full-theorem route.
- Agent B audited Agent A's spin note in
  `agent-B/notes/spin-splitting-audit-2026-06-05.md`. The spin element-norm
  reduction is correct:
  `||S||_ou <= 2 sqrt(2)||S||_{Fop->Fop}` for spin cochains. But the remaining
  Euclidean-injective `Fop->Fop` right-inverse estimate is not implied by HS
  pseudoinverse bounds, bounded rank, Schur's lemma, or small multiplicity. The
  spin target should be restated as an explicit `O(n)`-equivariant adjoint
  right inverse with injective cochain norm bounded independently of `n`.
  Agent A's "rank-balance" condition for `H_n` is also directionally wrong as
  written: `||h(a)||_2 <= K||h(a)||_ou` is low-rank control and does not remove
  an upper `sqrt(n)` loss in `||h(a)||_ou`.
- Agent B then proved that adjoint spin target in
  `agent-B/notes/adjoint-spin-splitting-theorem.md`. For
  `V=R1+H`, the exact adjoint coboundary image has an `O(H)`-equivariant
  Euclidean-injective right inverse with
  `||S_H f||_Fop <= 2||f||_Fop`; hence an order-unit adjoint spin splitting
  constant `<=4 sqrt(2)`. This is theorem-level progress for the spin benchmark,
  but not the full Layer-1 ER lemma because arbitrary modules,
  approximate-cocycle/module errors, direct sums, and high-rank matrix factors
  remain open.
- Agent B added `agent-B/notes/adjoint-direct-sum-reduction.md`, which proves
  summand-count independence for the adjoint/block-respecting case. If
  `B=direct_sum_r B_r` and the factors have exact adjoint splitting constants
  `K_r`, then the direct sum has constant at most `max_r K_r+1`. The key
  off-block formula is `(Sf)_r(x)=(S_r f^r)(x_r)+P_r f(e_r,x_{\ne r})`, which
  avoids summing over the number of ideals. This is the accepted precise form
  of Agent A's direct-sum reduction; arbitrary modules still require separate
  mixed Peirce control.
- Agent B added `agent-B/notes/spin-direct-sum-adjoint-corollary.md`. Combining
  the adjoint spin splitting (`<=4 sqrt(2)` in order norm) with the adjoint
  direct-sum reduction gives an exact adjoint right inverse for arbitrary
  finite direct sums of spin factors with constant `<=4 sqrt(2)+1`,
  independent of spin dimensions and summand count. This closes the exact
  adjoint spin-sum family, but not arbitrary modules or approximate errors.
- Agent B added `agent-B/notes/bounded-rank-adjoint-reduction.md`. For every
  fixed rank cutoff `R0`, finite direct sums of arbitrary spin factors, matrix
  factors `H_n(F)` with `n<=R0`, and Albert factors have exact adjoint splitting
  constant depending only on `R0`, not on spin dimensions or summand count.
  This uses finite-dimensional closed-range constants for the finitely many
  bounded-rank non-spin simple factors and the adjoint direct-sum reduction.
  At that stage the only asymptotic exact-adjoint simple-factor benchmark
  still open was `sup_n K_adj(H_n(F))<infinity` for `F=R,C,H`; this is now
  closed by the matrix-factor theorem recorded above.
- Agent B added
  `agent-B/notes/trace-zero-rank-one-matrix-primitive-estimate.md`. For
  `J=H_n(F)`, `F=R,C,H`, every normalized rank-one primitive
  `h(x)=phi(x)c` with `phi(1)=0` satisfies
  `(1/2)||h|| <= ||d^1h|| <= 3||h||`, uniformly in `n`. The proof uses the
  sign symmetry `u=sign(rho)` for the trace-dual density of `phi`: if
  `||u o c||>=1/4`, then `(d^1h)(u,u)=2u o c` is large; otherwise
  `(d^1h)(u,c)=phi(c)(u o c)+c^2-phi(u o c)c` is within `1/2` of `c^2`. Thus
  the residual high-rank matrix obstruction must involve coherent sums or
  higher-rank endomorphism geometry, not a single normalized rank-one
  primitive.
- Agent B added `agent-B/notes/nuclear-rank-one-route-caveat.md`. It records
  the limitation of the rank-one estimate: decomposing a general primitive
  into rank-one maps gives only a nuclear/projective norm bound. The identity
  on the traceless space `J_0` has operator norm `1` but nuclear norm at least
  `dim J_0` by duality `nu(Id_E)=sup_{||A||<=1}|tr A|`. Thus a termwise
  rank-one summation cannot give the dimension-free high-rank matrix splitting
  without additional exact-coboundary cancellation.
- Agent B also proved in
  `agent-B/notes/commutative-scalar-module-splitting.md` that one-dimensional
  unital modules over `R^m` have norm-one exact coboundary splittings in the
  max/injective norm. For coordinate modules and half-sum Peirce-`1/2` modules,
  `S_l f(x)=f(x,s)` with `s=e_k` or `s=e_p+e_q` gives
  `d^1 S_l f=f` and `||S_l f||<=||f||`. The same support-unit formula works for
  vector-valued multiplicities in an `l_infty` direct sum of scalar sectors.
  The note now also proves that every exact finite-dimensional `R^m` module
  algebraically decomposes into evaluation sectors and pair half-sum sectors:
  the idempotent actions satisfy
  `T_i(T_i-1)(2T_i-1)=0`, commute, and obey `2T_iT_jT_i=T_iT_j`.
  Thus the exact commutative module problem is controlled up to the
  complementability constant of the sector projections. The same formula gives
  a projection `Pi=d^1S` onto `im(d^1)` with norm `<=3` in max sector norm and
  `<=3K_dec` for arbitrary norms. Remaining issues: poor sector projection
  constants, noncommutative Peirce modules, and approximate-module bookkeeping.
- Agent B recorded the key high-rank norm caveat in
  `agent-B/notes/peirce-sector-norm-accumulation.md`. In `H_n(R)` with diagonal
  frame, each off-diagonal line `R(E_ij+E_ji)` is a harmless half-sum scalar
  sector of norm `1`, but the coherent sum over all pairs is `11^T-I` with
  operator norm `n-1`. Thus scalar sector control in max norm does not solve
  the matrix order-unit problem by naive inclusion.
- Agent B then proved in
  `agent-B/notes/diagonal-frame-matrix-module-splitting.md` that the exact
  coboundary problem for a fixed diagonal frame is nevertheless
  dimension-free: for `H_n(F)`, `F=R,C,H`, restricted to diagonal `R^n`, a
  Rademacher/Schur-multiplier formula gives `||S_n f||<=11||f||`. The same
  formula on all 2-cochains gives a projection `Pi_n=d^1 S_n` onto `im(d^1)`
  with `||Pi_n||<=33`. This removes the fixed-frame off-diagonal Peirce module
  as the high-rank obstruction. The remaining matrix-family issue is the full
  noncommutative cochain complex and approximate-module/cocycle errors.
  The note has been re-audited with the explicit Rademacher expectation
  calculation showing it recovers the canonical primitive modulo the
  antisymmetric kernel.
- Agent B added
  `agent-B/notes/frame-covariance-and-global-matrix-obstacle.md`. The
  fixed-frame splitting is fully frame-covariant: conjugating by any isometric
  Jordan automorphism gives the same constants `11` for the right inverse and
  `33` for the projection on every Jordan frame. The note also identifies a
  concrete failed globalization route. Averaged diagonal pinching
  `A(z)=int_G alpha E_0 alpha^{-1}(z)d alpha` acts on the traceless part by
  `lambda=(n-1)/(dim_R H_n(F)-1)`, namely `2/(n+2)`, `1/(n+1)`, and
  `1/(2n+1)` for `F=R,C,H`. Thus reconstructing global traceless data from
  random frames costs `1/lambda`, a rank-sized factor. This rules out the
  naive frame-averaging proof, not a more subtle full cochain homotopy.
- Agent B added `agent-B/notes/cochain-norm-conversion-caveat.md`. In
  `H_n(R)`, the 1-cochain `h_n(x)=x_11 1` has `||h_n||_op=1` but
  `||h_n||_F=sqrt(n)`. Its exact coboundary satisfies `||d^1h_n||_op<=3`, yet
  every primitive of `d^1h_n` has Frobenius-injective norm at least `sqrt(n)`
  because primitives differ by derivations and derivations have zero diagonal
  on `e_11`. This is not an order-norm obstruction; it is a no-go for any proof
  that asks for Frobenius-bounded primitives against order-bounded 2-cochains.
  The matrix-family proof must be directly order-norm or genuinely
  incremental.
- Agent B added `agent-B/notes/central-valued-matrix-primitive-estimate.md`.
  This turns the previous warning into a positive controlled component. For
  `J=H_n(F)`, `F=R,C,H`, and any real functional `phi`, the central primitive
  `h_phi(x)=phi(x)1` satisfies
  `||h_phi|| <= ||d^1h_phi|| <= 3||h_phi||` in order cochain norm. The lower
  bound uses a trace-dual density `rho` and the spectral sign symmetry
  `u=sign(rho)`, for which `phi(u)=||phi||_*` and
  `(d^1h_phi)(u,u)=2phi(u)u-phi(1)1`. Thus high-rank central primitive values
  are uniformly controlled; the remaining matrix problem lies in the
  noncentral/noncommutative components.
- Agent B added `agent-B/notes/multiplication-primitive-estimate.md`. For any
  unital JB algebra `B` and adjoint primitive `h=L_c`, `h(x)=c o x`, the exact
  estimate `||L_c|| <= ||d^1L_c|| <= 3||L_c||` holds in order cochain norm.
  The lower bound is just `(d^1L_c)(1,1)=c` and `||L_c||=||c||`. Thus the
  noncentral multiplication part is also not a source of dimension growth.
- Agent B added `agent-B/notes/unit-normalized-adjoint-reduction.md`. For an
  exact adjoint coboundary `f=d^1h`, `c=f(1,1)=h(1)`. Subtracting
  `d^1L_c` leaves `f_0=f-d^1L_c=d^1(h-L_c)` with normalized primitive
  `(h-L_c)(1)=0` and `f_0(1,x)=0`. The constants are
  `||L_c||<=||f||` and `||f_0||<=4||f||`; a normalized splitting with constant
  `K` gives a full splitting with constant `1+4K`. Thus the residual exact
  adjoint matrix target should be stated for unit-vanishing 2-coboundaries.
- A sidecar counterexample-search agent for dense polygon-like classical row
  polytopes completed on 2026-06-04. The resulting sharpened note is
  `agent-B/notes/regular-polygon-retraction-obstruction.md`: dense regular
  polygons of fixed diameter cannot be realized by exact signed affine
  retractions with row negative mass tending to zero.
- Agent A v0.11 agreed with Agent B that faithful invariant state alone does not
  transfer to ambient-product closure at a dimension-free rate; the valid
  estimate is conditioned by the least density of the invariant state.
- `agent-B/notes/audit-consensus-2026-06-04.md` records the current audited
  consensus: Layer 1 is open precisely because a dimension-free
  order-unit-norm Jordan cochain homotopy is missing; theorem C is sound as a
  conditional implication; and the sharp classical exact-factorization gap is
  the global exposed-hull lemma.
- `agent-B/notes/theorem-stack-v0.3.md` has been patched with the current
  Layer-1 partial splitting status: adjoint spin exact splitting proved,
  exact commutative modules algebraically decomposed and max-sector controlled,
  and high-rank matrix Peirce-sector norm accumulation isolated.
- Agent A v0.5 verified `agent-B/theory/theorem-B-algebraic-bridge.md` line by
  line and considers the Layer-2 bridge closed at exponent `1/2`; this remains
  unchanged after later sidequests.
- `agent-B/notes/theorem-stack-v0.3.md` has been promoted accordingly: the
  arbitrary-UP algebraic bridge is now proved internally at `O(sqrt(eta))`, not
  merely a proof candidate.
- Agent B led the adversarial report review requested by the user. Subagent
  outputs are:
  `agent-B/notes/subagent-report-math-audit-v0.1.md`,
  `agent-B/notes/subagent-report-provenance-audit-v0.1.md`, and
  `agent-B/notes/subagent-report-exposition-build-audit-v0.1.md`.
  Integrated review notes are in
  `agent-B/notes/report-review-v0.1.md`.
- The report in `report/` was patched and rebuilt successfully. `report/main.pdf`
  is current. Build residuals are minor typesetting only: one 3.7pt overfull
  line in the spectral-idempotent proof and one harmless underfull table line.
- Report provenance status: HOS/IDEL/KIT/VLW/ES page-level rows used in the
  report are registered and line-checked where marked `V`; Whitehead and
  Aut(J)-compactness remain explicitly flagged as extraction/PDF-level pending
  primary byte-check.
- Newest report-provenance audit on 2026-06-04 found no needed downgrade for
  Section 6 bridge labels. It did flag three faithful-invariant ledger fixes to
  request from Agent A: `prop:faithful-exact` should cite VLW/inline proof
  rather than pure-original status; `ex:no-faithful` should not cite the stale
  A-FIT "only invariant state" sentence; and `thm:faithful-approx` should
  distinguish B-FIT's exact-invariant subcase from A-FIT/report's
  approximate-invariance extension.
- Newest theorem-C state: exact UP factorization from near-positive
  projection stability is proof-level conditional, including
  real-to-complex Effros-Stormer, positivity of `Delta` and `Upsilon`, and
  equality of the Effros-Stormer JB cone with `J cap B(H)_+`.
- Newest Layer 1 literature state: Baak--Moslehian J*-homomorphism stability
  and Chu--Russo/Penico cohomology do not provide the needed
  dimension-free epsilon-JB product stability theorem; see
  `agent-B/notes/known-jstar-stability-literature-check.md`.
- Newest Layer 1 proof-audit state: the exact missing lemma is an explicit
  dimension-free operator-norm/order-unit-norm right inverse or homotopy
  `S:C^2_J(B,M)->C^1_J(B,M)` with universal norm bound, including approximate
  cocycle and approximate-module control. Haar averaging over `Aut(B)` alone
  does not supply this inverse.
- Newest classical-route state: approximate simplex coordinates may be signed
  if their coefficient negative mass is `O(delta)`; Wegener's sidecar found no
  counterexample and originally reformulated the remaining non-simplex gap as
  an exposed-or-redundant vertex dichotomy at scale `sqrt(delta)`. That local
  deletion formulation is now superseded by the global exposed-hull target in
  `agent-B/notes/simultaneous-skeleton-reduction.md`. The proved
  exposed-circuit cancellation lemma is in
  `agent-B/notes/exposed-circuit-cancellation.md`; the fully well-exposed
  separated vertex case is proved in
  `agent-B/notes/well-exposed-classical-stability.md`; the
  merge-compatible cluster-representative case is proved in
  `agent-B/notes/cluster-representative-classical-stability.md`; the formal
  exposedness modulus and LP-dual target are in
  `agent-B/notes/exposed-redundant-dichotomy-target.md`.
- Newest exact classical factorization state:
  `agent-B/theory/classical-cluster-factorization-theorem.md` packages the
  cluster-representative row-polytope theorem as an exact commutative
  positive/JB factorization theorem for almost-idempotent row-stochastic maps
  whose spectral idempotents satisfy the cluster geometry. It now also has a
  corollary replacing cluster geometry by the global exposed-hull hypothesis.
- Newest classical-gap sharpening:
  `agent-B/notes/simultaneous-skeleton-reduction.md` explains why a
  pointwise exposed-or-redundant deletion lemma is not enough without a
  non-accumulating certificate. The clean target is now the global
  exposed-hull lemma: for `W_{rho,kappa}` the set of vertices exposed at
  scale `rho=O(sqrt(delta))` with gap `kappa>=c sqrt(delta)`, every row should
  be `O(sqrt(delta))`-close to `conv W_{rho,kappa}`. A maximal separated
  subset of `W` then gives the cluster-representative skeleton.
- Newest special-case framing:
  `agent-B/notes/stochastic-stoquastic-special-cases.md` records the canonical
  row-stochastic Markov conjecture, the equivalent signed-idempotent form, the
  doubly stochastic/block-average special case, and the symmetric stoquastic
  formulation `H=I-Q`.
- Newest counterexample-search result:
  `agent-B/notes/regular-polygon-retraction-obstruction.md` rules out the most
  obvious dense regular polygon obstruction. Dihedral symmetrization reduces any
  affine coordinate lift to radial orbits, and the negative part of
  `a+2c cos(theta)` has supporting lower bound
  `sqrt(3)/pi |c|-a/3`; the barycentric constraints force vertex negative mass
  at least `sqrt(3)/pi-1/3-o(1)`. The global exposed-hull lemma remains open,
  but a counterexample must be more subtle than fixed-diameter regular polygons.
- Newest proof-tool extraction:
  `agent-B/notes/symmetric-coordinate-negative-mass-criterion.md` abstracts the
  regular-polygon argument. Exact signed idempotents are signed affine
  coordinate systems for their row polytopes; averaging over a finite symmetry
  group cannot increase maximum row negative mass. Therefore any symmetric
  proposed counterexample must pass the equivariant coordinate negative-mass
  lower-bound test before it can be a genuine small-defect signed retraction.
- The next mathematical priorities are:
  1. attack one of the two open engines:
     dimension-free Layer 1 positive/concrete stability, or
     dimension-free near-positive projection stability, now focused on the
     global exposed-hull lemma;
  2. keep decomposable `O(eta)` labelled conjectural except under the
     dilation-compatible lifted-UCP hypothesis.

## Role And Write Discipline

- User objective: generalise Kitaev arXiv:2405.02434 from almost-idempotent UCP maps / approximate C*-algebras to positive maps / Jordan algebras, using arXiv:2604.08380 as the positive-map setting.
- I am Agent B. My private work goes under `agent-B/`.
- Coordination with Agent A is via root files:
  - read `agent-a-findings`;
  - write only `agent-b-findings`.
- The north star is consensus on formulation, theorem statements, and proof.

## Local Sources

- Kitaev source and PDF:
  - `agent-B/references/kitaev-2405.02434/approximate_algebras.tex`
  - `agent-B/references/kitaev-2405.02434/kitaev-2405.02434v2.pdf`
- Positive maps / sufficiency source and PDF:
  - `agent-B/references/positive-maps-2604.08380/paper.tex`
  - `agent-B/references/positive-maps-2604.08380/positive-maps-2604.08380v2.pdf`
- Effros-Stormer positive projections:
  - `agent-B/references/effros-stormer-1979/positive-projections-jordan-structure.pdf`
  - `agent-B/references/effros-stormer-1979/positive-projections-jordan-structure.txt`

## Extracted Facts

Kitaev arXiv:2405.02434:
- A UCP map `Phi` is `eta`-idempotent when `||Phi^2-Phi||_cb <= eta`.
- Functional calculus gives an exact idempotent linear map
  `tilde Phi = theta(2 Phi - 1)` with `||tilde Phi-Phi||_cb = O(eta)`.
- `tilde Phi` is unital and *-preserving but need not be positive or CP.
- On `A = Im tilde Phi`, Kitaev defines `X star Y = tilde Phi(XY)`.
- For UCP `Phi`, this is an extended `O(eta)`-C*-algebra.
- Any finite-dimensional extended `eps`-C*-algebra is `O(eps)`-isomorphic to a genuine finite-dimensional C*-algebra.
- For finite-dimensional `H`, this yields a C*-algebra `B` and UCP maps `Delta:B -> B(H)`, `Upsilon:B(H)->B` such that `Delta Upsilon` approximates `Phi` in cb norm and `Upsilon(Delta(X)Delta(Y))` approximates `XY` uniformly on matrix levels.

Complete positivity is essential in Kitaev at:
- Kadison/Schwarz and matrix-level norm control.
- Choi/Stinespring proof of approximate associativity.
- Passing all estimates to `M_n tensor A`.
- Rounding approximate maps into UCP maps.

Positive-map paper arXiv:2604.08380:
- UP maps satisfy Jordan-Schwarz:
  `{T a*, T a} <= T {a*, a}`.
- Equality defines the positive-map multiplicative domain, a J*-algebra, and `T` restricts to a J*-homomorphism there.
- If `T` is UP with faithful invariant state, `Fix(T)` is a J*-algebra.
- Cesaro means of a UP map give an idempotent UP projection onto its fixed space.
- A faithful idempotent UP map is a conditional expectation onto a concrete J*-algebra.
- Every finite-dimensional concrete J*-algebra has a unique trace-preserving conditional expectation: trace-orthogonal projection, positive by self-duality of the cone.
- Minimal PTP-sufficient operator systems are J*-algebras and admit unique state-preserving UP conditional expectations.
- Finite-dimensional abstract J*-algebras decompose into factors: complex matrices, symmetric real type, symplectic/quaternionic type, and spin factors.
- Universally reversible iff no spin-factor summand `V_n` for `n >= 4`.

Effros-Stormer:
- For a unital positive projection on a C*-algebra, the range need not be a concrete Jordan subalgebra under inherited product.
- The range carries a Jordan product of Choi-Effros type, expected as `P(x o y)` on self-adjoint parts / complexification.
- This is probably the right exact object for a raw positive projection without faithful-concrete-range assumptions.

## Historical Mathematical Fork

The items in this section record earlier reasoning and may be superseded by the
Current Resume Snapshot above.

Naive theorem to avoid:
- "If `Phi` is almost-idempotent UP then `Im theta(2Phi-1)` with inherited Jordan product is an approximate J*-algebra close to a concrete J*-algebra."

Reason:
- `tilde Phi = theta(2Phi-1)` may not be positive.
- Even if exactly positive and idempotent, the range of a positive projection is generally a Jordan algebra for the projected/Effros-Stormer product, not necessarily closed under the inherited ambient Jordan product unless extra faithfulness/concrete conditional expectation conditions apply.
- Positive maps do not tensor with `M_n`, so cb/complete-order parts of Kitaev do not transfer verbatim.

Promising exact model:
- Start with finite-dimensional order-unit/JB/J*-type data rather than an associative product:
  - self-adjoint order-unit space `A_sa = Im tilde Phi` inside `B(H)_sa`;
  - product `x bullet y = tilde Phi(x o y)` where `x o y = (xy+yx)/2`;
  - complexification for J*-language.
- Prove this is an approximate finite-dimensional JB/J*-algebra under hypotheses replacing UCP/cb.
- Then prove a Jordan stability theorem: finite-dimensional approximate JB/J*-algebras with the right order/norm axioms are `O(eps)`-isomorphic to genuine finite-dimensional J*-algebras.
- Finally obtain positive maps `Delta:J -> B(H)` and `Upsilon:B(H)->J` approximating `Phi` in operator norm / order-unit norm, not cb norm, unless restricting to decomposable/universally reversible cases.

Likely theorem levels:
1. Norm-level positive theorem: UP, `||Phi^2-Phi|| <= eta`, finite-dimensional, plus a uniform approximate Jordan-Schwarz/KMS contraction hypothesis if needed. Conclusion: factorization through a finite-dimensional J*-algebra by UP maps in operator norm.
2. Stronger decomposable/reversible theorem: if maps admit an explicitly controlled CP+coCP decomposition and the target J*-algebra is universally reversible, recover matrix-level/decomposable analogs.
3. Exact consistency theorem: when `eta=0` and there is a faithful invariant state or `Phi` is a faithful conditional expectation, the result reduces to the J*-conditional expectation facts of arXiv:2604.08380.

## Historical Next Steps

1. Effros-Stormer text has been OCR'd. Exact theorem: a unital positive projection on a unital JC-algebra has range a JC-algebra for `P(x o y)`.
2. Decide the precise definition of "epsilon-J*-algebra" or "epsilon-JB-algebra"; do not invent constants before checking known JB stability literature.
3. Test whether the approximate product `tilde Phi(x o y)` satisfies approximate Jordan identity using only positivity/Jordan-Schwarz and almost-idempotence. This is the central technical risk.
4. Current rigorous partial result: approximate Effros-Stormer Lemma 1.1 with `O(sqrt(eta))` defect; see `agent-B/notes/approximate-effros-stormer.md` and `agent-B/notes/layer2-bridge-sqrt.md`.
5. New candidate result: approximate null-ideal estimates for range-product
   holes close the Jordan identity at `O(sqrt(eta))`; see
   `agent-B/notes/layer2-null-ideal-sqrt.md`. This was later verified by
   Agent A v0.5 via `agent-B/theory/theorem-B-algebraic-bridge.md` and is now
   promoted in the Current Resume Snapshot above.
6. Keep `agent-b-findings` updated after each substantial conclusion, with explicit questions for Agent A.
7. Agent A v0.2 has been read. Agent B agrees with two-layer/order-unit architecture but objects to "reversible" and automatic "decomposable" in the arbitrary positive-map theorem. See `agent-B/notes/response-to-agent-a-v0.2.md`.
8. Agent B has a square-root first insertion estimate and now a candidate null-ideal completion of the full approximate Jordan identity. An earlier first-insertion-only overclaim was corrected. See `agent-B/notes/layer2-bridge-sqrt.md` and `agent-B/notes/layer2-null-ideal-sqrt.md`.
9. Historical theorem stack drafted at `agent-B/notes/theorem-formulation-v0.1.md`;
   current clean theorem stack is `agent-B/notes/theorem-stack-v0.3.md`.
10. Alternative bridge route drafted at `agent-B/notes/alternative-bridge-near-positive-projection.md`: prove near-positive unital projections are close to positive idempotents, then apply exact Effros-Stormer.
11. Alternative near-contractive route drafted at `agent-B/notes/alternative-bridge-near-contractive-projection.md`: exact contractive projection theory is relevant but does not directly supply the needed quantitative binary Jordan product theorem.
12. Agent A v0.4 read. Agent B agrees `alpha=1` is not automatic and decomposable is promising. Agent B subsequently found a candidate null-ideal proof of the full `alpha=1/2` bridge. See `agent-B/notes/response-to-agent-a-v0.4.md` and `agent-B/notes/layer2-null-ideal-sqrt.md`.
13. Compaction rule: after each substantial result, update this checkpoint and
    `agent-b-findings` before continuing. A resumed Agent B should first read
    this file, then `agent-b-findings`, then the newest `agent-a-findings`.
14. Current theorem draft records Agent B's candidate full bridge at
    `alpha=1/2`, pending peer review. The decomposable `alpha=1` bridge is
    conjectural until the controlled CP/coCP two-hole calculation is written.
15. Euclid sidecar result: the standard Haagerup/Wittstock decomposable norm is
    not `1` for every unital positive decomposable map; transpose on `M_n` has
    standard decomposable norm `n`. State decomposable hypotheses using an
    explicit CP+coCP decomposition with bounded CP pieces. For unital maps, any
    such decomposition has `Phi_0(1)+Psi_0(1)=1`, hence each CP piece has cb
    norm at most `1`. See `agent-B/notes/subagent-decomposable-norm.md`.
16. Factorization warning: the algebraic bridge does not by itself produce
    exact UP factor maps. Generic `O(epsilon)` positivity-rounding is false:
    McClintock produced a spin-factor counterexample with lower bound
    `sqrt(epsilon)`. See `agent-B/notes/factorization-positivity-rounding.md`
    and `agent-B/notes/subagent-positivity-rounding.md`.
17. Clean current theorem stack written at
    `agent-B/notes/theorem-stack-v0.3.md`. Prefer this over
    `theorem-stack-v0.2.md` and `theorem-formulation-v0.1.md` for the latest
    formulation.
18. Parfit's null-ideal probe found no counterexample. A clean classical `R^3`
    stochastic family has `||P(h_{r,s}^2)||/eta -> 32/27`, supporting
    linear null-square smallness and showing `O(eta^2)` is false in that
    normalization. See `agent-B/experiments/null-ideal-probe/REPORT.md`.
19. Concise response/update for Agent A written at
    `agent-B/notes/response-to-agent-a-v0.5.md`.
20. Formalized algebraic bridge theorem draft written at
    `agent-B/theory/theorem-B-algebraic-bridge.md`. This is the main proof
    object for Agent A to review.
21. Pasteur sidecar: the spin-factor positivity-rounding obstruction does not
    obviously upgrade to a near-positive idempotent/projection counterexample.
    Idempotency/retraction saturates spin faces; natural constructions have
    defect `Theta(sqrt(epsilon))`, matching distance to a positive projection.
    Near-positive projection stability remains plausible. See
    `agent-B/notes/subagent-near-positive-projection-stability.md`.
22. Layer 1 output requirements written at
    `agent-B/notes/layer1-output-requirements.md`: norm/Jordan algebraic
    stability alone is insufficient; need positive comparison maps, concrete
    JC output with expectation comparison, or near-positive projection
    stability.
23. Near-positive projection stability program written at
    `agent-B/notes/near-positive-projection-stability-program.md`, including a
    classical `l_infty^n` subproblem. This is an open route to exact UP factor
    maps.
24. Decomposable `O(eta)` route recorded at
    `agent-B/notes/decomposable-alpha1-route.md`. Status: plausible but open;
    needs a doubled/universal-envelope two-hole proof because CP/coCP summands
    are not individually unital/almost-idempotent.
25. Hume sidecar disproved linear near-positive projection stability
    classically. Explicit `3 x 3` unital idempotents have defect `delta=s^2`
    and distance `2sqrt(delta)+O(delta)` from stochastic idempotents. Projection
    stability, if true, is sharp at exponent `1/2`. See
    `agent-B/notes/subagent-classical-projection-stability.md`.
26. Concise addendum for Agent A written at
    `agent-B/notes/response-to-agent-a-v0.6.md`.
27. Gibbs and Heisenberg sidecars reduced the classical near-positive
    projection-stability theorem to dimension-free `sqrt` stability of
    almost-idempotent stochastic matrices:
    `Q` stochastic and `||Q^2-Q||<=eps` should be `C sqrt(eps)`-close to a
    stochastic idempotent. Rowwise repair gives
    `||P-Q||<=2delta` and `||Q^2-Q||<=6delta+4delta^2`; the converse uses
    spectral functional calculus. No proof or citation was found. See
    `agent-B/notes/subagent-classical-sqrt-stability-proof.md`,
    `agent-B/notes/near-positive-projection-stability-program.md`, and
    `agent-B/notes/response-to-agent-a-v0.7.md`.
28. `agent-B/theory/theorem-B-algebraic-bridge.md` was tightened after a local
    proof audit: Lemma 2 now spells out the polynomial optimization proving
    almost-orthogonality of `Im P` and `Ker P`; Lemmas 4 and 5 now spell out
    the state-supremum and one-hole context estimates. No theorem statement or
    exponent changed.
29. Agent A's local Layer 1 drafts were reviewed. `agent-A/theory/00-overview.md`
    is stale relative to v0.4/current consensus (`reversible`,
    `decomposable`, and `O(eta)` are overclaimed for arbitrary UP maps).
    `agent-A/theory/01-error-reduction.md` correctly identifies the
    dimension-free bounded Jordan cohomology splitting as the main gap; `H^2=0`
    alone is qualitative. Review recorded at
    `agent-B/notes/layer1-agent-a-review-v0.1.md`.
30. The naive decomposable doubled/lifted route was stress-tested and found
    insufficient. If `Phi=Cj` factors through the doubled/opposite algebra,
    `F=jC` need not be almost idempotent: `F^2-F=j((Phi-I)C)`, not controlled by
    `||Phi^2-Phi||`. A commutative stochastic example in the exact doubled
    form has `Cj` exactly idempotent but `||jCjC-jC||=1`. See
    `agent-B/notes/decomposable-doubling-obstruction.md`. The decomposable
    `O(eta)` theorem remains conjectural unless a direct CP/coCP two-hole
    identity or stronger dilation-compatible hypothesis is proved.
31. A positive conditional result was recorded at
    `agent-B/notes/decomposable-dilation-compatible-theorem.md`: if there is a
    dilation-compatible model with a unital order-isometric Jordan embedding
    `j`, `Phi=Cj`, and a genuinely UCP lifted map `F=jC` satisfying
    `||F^2-F||_cb<=eta`, then Kitaev's UCP theorem for `F` restricts to an
    `O(eta)` JB bridge for `Phi`. This lifted-UCP hypothesis is extra and not
    automatic from a CP+coCP decomposition.
32. Sartre sidecar reinforced the decomposable warning: an exact depolarizing
    projection on `M_2` can be written with a bad CP+coCP decomposition whose
    natural universal extension has off-diagonal defect `||Phi F-F||>=eps/2`
    despite `eta=0`. See
    `agent-B/notes/subagent-decomposable-alpha1-stress.md`. Therefore any
    decomposable `O(eta)` proof must choose compatible decompositions or prove
    direct cancellation.
33. Corrected theorem stack v0.3 written at
    `agent-B/notes/theorem-stack-v0.3.md`. It separates: open abstract Layer 1,
    candidate arbitrary-UP `O(sqrt(eta))` bridge, conditional exact UP
    factorization, proved dilation-compatible `O(eta)` bridge, and conjectural
    decomposable `O(eta)` bridge.
34. Classical Markov/projection stability was reformulated as affine retraction
    stability of the simplex. The missing lemma is:
    `dist(P, stochastic idempotent affine retractions) <= C sqrt(sup_{x in
    Delta_n} dist(Px,Delta_n))` for exact affine retractions `P`. See
    `agent-B/notes/markov-affine-retraction-formulation.md`.
35. Proved the classical square-root stability theorem for rank-one signed
    idempotents `P=I-u v^T`, including Hume's sharp family. The proof normalizes
    the positive/negative masses of `v`, shows at most one positive and one
    negative active row can exceed `sqrt(delta)`, and rounds to a transient or
    two-state recurrent stochastic idempotent. See
    `agent-B/notes/rank-one-classical-stability.md`.
36. Tightened the final Jordan-identity bookkeeping in
    `agent-B/theory/theorem-B-algebraic-bridge.md`. No theorem statement or
    exponent changed; the proof now explicitly routes the left-side kernel hole
    through `(FI)` and the right-side expansion through `(5.2)`, `(FI)`, and
    `(HH)`.
37. Added `agent-B/notes/classical-affine-face-lemmas.md`. For an
    almost-idempotent stochastic matrix, any exposed row-polytope face is
    almost closed: an `alpha`-exposed row leaks at most `(alpha+eps)/gamma` mass
    outside the `gamma`-exposed slice. Choosing `gamma=sqrt(eps)` gives the
    sharp face-leakage scale. This is partial structure for Markov
    square-root stability, not a full proof; the missing piece is
    dimension-free recursive rounding of almost-closed exposed faces.
38. Boyle sidecar audited `agent-B/theory/theorem-B-algebraic-bridge.md`;
    see `agent-B/notes/subagent-bridge-proof-audit-v0.1.md`. It found no fatal
    local gap conditional on the initial spectral estimate. I then patched the
    proof to derive that estimate directly from `S=2Phi-I` and
    `sgn(S)=S(S^2)^(-1/2)`, giving `P^2=P`, `P(1)=1`, `||P-Phi||=O(eta)`, and
    `||P||<=1+O(eta)` without any CP/cb input.
39. Added `agent-B/notes/layer1-quantitative-obligations-v0.2.md`. It sharpens
    the Layer 1 gap: a Jordan analogue of Kitaev's error reduction needs an
    explicit cochain homotopy/right inverse with universal order-unit norm
    bounds. Haar averaging over `Aut(B)` is norm-one as a projection, but is
    not by itself a right inverse to the Jordan coboundary; the non-invariant
    components, direct sums, matrix rank, and spin-factor dimension are the
    places constants can leak.
40. Lagrange sidecar independently audited the Layer 1 averaging route; see
    `agent-B/notes/subagent-layer1-averaging-audit-v0.1.md`. It agrees the
    route is plausible but not a theorem. Specific stress points are spin
    factors `V_m`, matrix factors with unbounded rank, direct sums with mixed
    central/cross terms, and the approximate-module issue. Qualitative
    `H^2=0` plus compact `Aut(J)` Haar averaging does not provide the needed
    dimension-free bounded right inverse/projection in the order-unit cochain
    norm.
41. Wrote `agent-B/notes/response-to-agent-a-v0.8.md`, the newest concise
    synthesis for Agent A. It asks Agent A to update stale
    `reversible/decomposable/O(eta)` arbitrary-UP claims, peer-review the
    bridge proof, and focus Layer 1 work on the bounded homotopy `ER-norm`
    estimate.
42. Further tightened `agent-B/theory/theorem-B-algebraic-bridge.md` after
    Boyle's audit: Lemma 2 now spells out the square-Lipschitz step, Lemma 3
    records crude hole norms and the `gamma^2` absorption, Lemma 4 records
    crude polarized-hole norms and replacement costs, Lemma 5 records the
    crude one-hole context norm and HH absorption. No theorem statement or
    exponent changed.
43. Added `agent-B/theory/theorem-C-conditional-factorization.md`. This proves
    the theorem-level implication from near-positive projection stability to
    exact UP factorization: if every `delta`-positive unital idempotent
    `P:B(H)_sa->B(H)_sa` with `||P||<=1+delta` is `O(sqrt(delta))`-close to a
    positive unital idempotent `E`, then any almost-idempotent UP `Phi` factors
    through `J=E(B(H)_sa)` by UP maps `Delta=inclusion`, `Upsilon=E`, with
    `||Delta Upsilon-Phi||<=C sqrt(eta)`, `Upsilon Delta=id_J`, and exact
    pulled-back Effros-Stormer product identity
    `Upsilon(Delta x o Delta y)=x*y`. The open ingredient is now exactly the
    projection-stability theorem.
44. Proved a second classical projection-stability special case:
    `agent-B/notes/line-segment-classical-stability.md`. If an exact signed
    affine retraction has row polytope of affine dimension at most `1` and row
    negative masses at most `delta`, then it is `O(sqrt(delta))`-close to a
    stochastic idempotent. Endpoint idempotency in the affine coordinate
    `alpha` forces positive mass of one endpoint into
    `{alpha<=sqrt(delta)}` and positive mass of the other into
    `{alpha>=1-sqrt(delta)}`, yielding disjoint recurrent supports after
    normalization. This covers the first two-recurrent-component geometry and
    complements the rank-one-perturbation theorem.
45. Strengthened item 44 to arbitrary simplex row polytopes:
    `agent-B/notes/simplex-classical-stability.md`. If the row polytope of an
    exact signed affine retraction is a simplex and row negative masses are at
    most `delta`, then the retraction is `O(sqrt(delta))`-close to a stochastic
    idempotent with a universal constant independent of the number of simplex
    vertices. In barycentric coordinates, vertex idempotency gives
    `sum_j r^a_j lambda_b(j)=delta_ab`, so the positive mass of vertex `r^a`
    concentrates on `{lambda_a>=1-sqrt(delta)}`; normalizing these disjoint
    near-vertex restrictions yields recurrent distributions. The remaining
    classical projection-stability problem is now arbitrary non-simplex row
    polytopes, where no global affine barycentric coordinates exist.
46. Added `agent-B/notes/approximate-simplexity-reduction.md`. If selected rows
    `r^a` and affine functions `lambda_a` give `gamma`-approximate simplex
    coordinates for all rows, with `0<=lambda_a<=1`, `sum lambda_a=1`,
    `lambda_a(r^a)=1`, and
    `||p_i-sum_a lambda_a(p_i)r^a||_1<=gamma`, then the same concentration
    proof gives a stochastic idempotent within `C(sqrt(delta)+gamma)`.
    Therefore the non-simplex classical route is now reduced to proving
    `O(sqrt(delta))` approximate simplexity for row polytopes, or finding a
    counterexample to that lemma.
47. Fermat sidecar probed non-simplex row polytopes; see
    `agent-B/notes/subagent-non-simplex-classical-probe-v0.1.md`. It found no
    counterexample. It pinpointed the obstruction: one-face exposed leakage is
    dimension-free, but intersecting several facet slacks can lose facet count
    or inverse angle/altitude; and macroscopic affine dependencies such as
    parallelogram relations cannot be rounded by assigning every vertex a
    disjoint recurrent class. The missing lemma is now best phrased as an
    angle-free approximate-simplexity/cancellation theorem: macroscopic
    non-simplex affine dependencies must either cost more than `O(delta)`
    negative mass or be mergeable at `O(sqrt(delta))` scale.
48. Hardened the workflow for regular context compaction. The resume protocol
    is now at the top of this file rather than buried in the historical item
    list. Future resumed Agent B instances should treat this checkpoint,
    `agent-b-findings`, and then `agent-a-findings` as the source of truth
    before continuing, and should update durable files before moving on after
    any substantial mathematical result.
49. Added and corrected `agent-B/notes/parallelogram-classical-stability.md`
    after Popper's sidecar observation. The correct result is a
    coordinate-rectangle cancellation lemma, not a substantive new stability
    case: if four rows are separated by bounded affine coordinates
    `s,t:K->[0,1]`, then each corner row concentrates on its own disjoint
    corner slice and
    `||r_{00}+r_{11}-r_{10}-r_{01}||_1 >= 4-C sqrt(delta)`. Hence a genuine
    parallelogram row polytope, whose vertices satisfy
    `r_{00}+r_{11}=r_{10}+r_{01}`, is impossible for sufficiently small
    `delta`. The remaining non-simplex obstruction is therefore hidden in
    ill-conditioned or many-factor affine dependencies, not in bounded
    parallelogram cancellation.
50. Strengthened the previous item inside
    `agent-B/notes/parallelogram-classical-stability.md` to a bounded
    binary-coordinate cancellation lemma. If rows `r_a` have distinct binary
    code words witnessed by affine functions `s_1,...,s_m:K->[0,1]`, then
    each `r_a` is `O(m sqrt(delta))`-close to a probability measure supported
    on its own disjoint code cell. Consequently
    `||sum_a c_a r_a||_1 >= (1-C m sqrt(delta)) sum_a |c_a|` for all
    coefficients `c_a`. Thus any exact affine dependence with bounded
    coordinate witnesses is impossible when `m sqrt(delta)` is small. This
    sharpens the remaining non-simplex obstruction: the full proof needs an
    angle-free way to find bounded-coordinate witnesses or to merge
    ill-conditioned/many-factor dependencies without losing dimension-free
    constants.
51. Wrote `agent-B/notes/response-to-agent-a-v0.9.md`, a concise synthesis for
    Agent A. It keeps the main theorem stack unchanged and highlights the new
    bounded-coordinate cancellation lemma as the latest progress on the
    classical projection-stability route.
52. Added a corollary to
    `agent-B/notes/parallelogram-classical-stability.md`: fixed-complexity
    non-simplex product-of-simplexes vertex geometries are impossible at small
    defect when their factor coordinates are affine maps `K->[0,1]`.
    Pulling back the product simplex coordinates gives bounded binary
    coordinate witnesses with `m=sum_l N_l`; any two nontrivial factors give a
    rectangle affine relation, contradicting the cancellation lemma when
    `m sqrt(delta)` is small.
53. Patched `agent-B/theory/theorem-B-algebraic-bridge.md` with Lemma 0,
    verifying the exact order-unit structure on `A=Im P`. Since `P(1)=1`,
    `A` is a real subspace containing `1`; with cone `A cap B(H)_+`, it is an
    Archimedean order-unit space and its order-unit norm equals the ambient
    operator norm. This closes a definition-level gap in the algebraic bridge
    proof without changing the `O(sqrt(eta))` exponent or theorem status.
54. Wrote `agent-B/notes/response-to-agent-a-v0.10.md`, asking Agent A to
    review the bridge proof with the new Lemma 0 included. The requested
    review order is: spectral idempotent estimate, exact inherited
    order-unit structure, square-hole positivity shift, polarization/state
    supremum, and final Jordan identity bookkeeping.
55. Further patched `agent-B/theory/theorem-B-algebraic-bridge.md` with a
    "Standard Order Estimates" block before Lemma 1. It explicitly lists the
    only order tools used in the proof: Jordan-Schwarz for unital positive
    maps on self-adjoint elements, Cauchy-Schwarz for positive functionals,
    positive-cone norm monotonicity, and the state-supremum formula for
    self-adjoint operator norm. This is proof hardening only; theorem status
    and exponent are unchanged.
56. Added the self-adjoint order-perturbation rule to the same theorem-B
    standard-estimates block:
    `||x-y||<=epsilon => x>=y-epsilon 1` and `x<=y+epsilon 1`.
    Lemma 3 now explicitly uses this to justify
    `Phi(r)^2 >= r^2-C delta||r||^2 1` and the order cost of replacing
    `Phi(r^2)` by `P(r^2)`. This closes another implicit order-bookkeeping
    point in the square-hole positivity shift.
57. Expanded Lemma 4 in
    `agent-B/theory/theorem-B-algebraic-bridge.md`. The polarization identity
    is now written as polarization of the symmetric bilinear map
    `(r,s)->P(r o s)-r o s`, with the square-hole notation clarified, and the
    zero cases plus optimizing choice `lambda=||s||/||r||` are explicit.
    This hardens the passage from square-hole estimates to arbitrary
    product-hole estimates.
58. Patched `agent-B/theory/theorem-C-conditional-factorization.md` to justify
    the real-to-complex Effros-Stormer step. A unital positive idempotent
    `E:B(H)_sa->B(H)_sa` extends complex-linearly to a unital positive
    projection `E_C` on `B(H)`; positivity is checked on positive self-adjoint
    inputs. Effros-Stormer applies to `E_C`, and restriction to the
    self-adjoint range gives the real special JB product `x*y=E(x o y)` with
    inherited cone `J cap B(H)_+`. This hardens theorem-C without changing its
    conditional status.
59. Wrote `agent-B/notes/response-to-agent-a-v0.11.md`, a concise note for
    Agent A on the theorem-C real-to-complex/Effros-Stormer hardening. It
    reiterates that theorem-C proves only the implication from projection
    stability to exact UP factorization; projection stability itself remains
    open.
60. Further patched theorem-C to verify positivity of the exact factor maps
    against the chosen cones. For `Delta`, positivity is inclusion of
    `J_+=J cap B(H)_+` into `B(H)_+`. For `Upsilon=E`, positivity follows
    because `E(B(H)_+) subset B(H)_+` and idempotency gives `E(a) in J`, hence
    `E(a) in J_+`.
61. Strengthened theorem-C's cone treatment. After briefly separating the
    inherited cone from the Effros-Stormer JB cone, I patched theorem-C to
    prove they coincide. If `x=y*y=E(y o y)` in the Effros-Stormer product,
    positivity of `E` gives ambient positivity. Conversely, if
    `z in J cap B(H)_+`, then `0<=z<=||z||1` ambiently and the inherited
    Banach norm plus the unital JB criterion
    `z>=0 iff || ||z||1-z ||<=||z||` imply JB-positivity. Thus theorem-C
    genuinely supplies UP maps through the special JB cone.
62. Added the "Current Resume Snapshot" near the top of this checkpoint to
    make regular context compaction safer. A resumed Agent B should not have
    to reconstruct the current state from the historical item list before
    knowing whether there are active sidecars, stale Agent A claims, syntax
    fixes still pending, or the next viable mathematical priorities.
63. Added `agent-B/notes/robust-approximate-simplexity-reduction.md`. The
    simplex-coordinate reduction for classical projection stability now
    tolerates signed affine coordinate vectors, provided their coefficient
    negative mass is `O(delta)` and the row reconstruction error is
    `O(sqrt(delta))`; exact pointwise nonnegativity of coordinates is not
    required.
64. Wegener sidecar completed and was closed. Its report is recorded at
    `agent-B/notes/subagent-exposed-redundant-classical-v0.1.md`. It found no
    counterexample, flagged tensor Hume as a false-alarm candidate unless one
    proves lower bounds against all transient-class roundings, and isolated a
    complete exposed-circuit cancellation lemma. The remaining classical gap
    is now best stated as an exposed-or-redundant vertex dichotomy at
    `sqrt(delta)` scale.
65. Wrote `agent-B/notes/response-to-agent-a-v0.12.md`, the newest concise
    synthesis for Agent A, focused on the robust signed-coordinate reduction
    and exposed-or-redundant classical projection-stability target.
66. Added `agent-B/notes/exposed-redundant-dichotomy-target.md`. It defines
    the exposedness modulus
    `e_v(rho)=sup_h min_{||x-v||_1>=rho} h(x)` over affine
    `h:K->[0,1]` with `h(v)=0`, states the desired dichotomy
    `e_v(C sqrt(delta))>=c sqrt(delta)` or `v` is
    `O(sqrt(delta))`-redundant, and records the LP-dual obstruction. This is
    now the precise classical geometric core after the robust simplexity
    reduction.
67. Added `agent-B/notes/exposed-circuit-cancellation.md`, extracting the
    complete theorem-level part of Wegener's sidecar report. It proves that
    well-exposed rows concentrate on their row clusters and that pairwise
    separated well-exposed rows satisfy
    `||sum c_a v_a||_1 >= (1-C(delta/kappa+delta)) sum |c_a|`, hence at
    `kappa >= c sqrt(delta)` they cannot form nontrivial affine circuits at
    small defect. The remaining open step is exactly
    `not well exposed => O(sqrt(delta))-redundant/mergeable`.
68. Added `agent-B/notes/well-exposed-classical-stability.md`. If all vertices
    of the classical row polytope are pairwise separated and well exposed at
    scale `rho`, with exposedness gap `kappa` satisfying
    `C(delta/kappa+delta)<1`, then exposed-circuit cancellation forces the
    vertices to be affinely independent, so the row polytope is a simplex.
    The simplex classical theorem then gives a stochastic idempotent within
    `O(sqrt(delta))`. In particular this closes the branch
    `kappa >= c sqrt(delta)` for small `delta`.
69. Wrote `agent-B/notes/response-to-agent-a-v0.13.md`, the newest concise
    synthesis for Agent A, focused on the well-exposed classical stability
    special case and the now-narrower remaining non-simplex gap.
70. Added `agent-B/notes/known-jstar-stability-literature-check.md` and linked
    it from `agent-B/notes/layer1-quantitative-obligations-v0.2.md` and the
    theorem stack. Baak--Moslehian proves Hyers--Ulam--Rassias stability of
    maps between exact J*-algebras under global scaling-control hypotheses;
    it does not perturb an epsilon-JB product to an exact JB algebra.
    Chu--Russo/Penico supplies qualitative `H^2=0`, but not a
    dimension-free order-unit-norm cochain homotopy. Thus Agent A's Layer 1
    `ER-norm` gap remains real.
71. Wrote `agent-B/notes/response-to-agent-a-v0.14.md`, now the newest
    concise synthesis for Agent A. It reports the Layer 1 literature boundary
    and again asks Agent A to update the stale
    `agent-A/theory/00-overview.md` arbitrary-UP theorem claims
    (`reversible`, `decomposable`, `O(eta)`).
72. Added `agent-B/notes/cluster-representative-classical-stability.md`. If
    well-exposed representative rows have disjoint `rho`-clusters and every
    non-cluster row is `gamma`-close to a convex combination of the
    representatives, then setting cluster rows equal to the corresponding
    recurrent probabilities `pi_a` and outside rows to the same convex
    combinations of `pi_a` gives a stochastic idempotent within
    `C(rho+gamma+delta/kappa+delta)`. Thus at
    `rho,gamma=O(sqrt(delta))`, `kappa>=c sqrt(delta)`, stability follows
    without global affine simplex coordinates or accumulation over merged
    vertices.
73. Wrote `agent-B/notes/response-to-agent-a-v0.15.md`, now the newest concise
    synthesis for Agent A, focused on the cluster-representative classical
    stability reduction.
74. Added `agent-B/theory/classical-cluster-factorization-theorem.md`. For a
    row-stochastic `Q` with `||Q^2-Q||<=eta`, the spectral idempotent
    `P=theta(2Q-I)` satisfies `P^2=P`, `P1=1`, `||P-Q||=O(eta)`, and row
    negative mass `O(eta)`. If the rows of `P` satisfy the
    cluster-representative geometry at `rho,gamma=O(sqrt(eta))` and
    `kappa>=c sqrt(eta)`, the cluster theorem gives a stochastic idempotent
    `E` with `||E-Q||=O(sqrt(eta))`. Then
    `J=E(ell_infty^n)`, `Delta=inclusion`, and `Upsilon=E` give exact
    positive factor maps through the commutative special JB product
    `x*y=E(x.y)`.
75. Wrote `agent-B/notes/response-to-agent-a-v0.16.md`, now the newest concise
    synthesis for Agent A, focused on the exact commutative factorization
    theorem under cluster-representative spectral geometry.
76. Added `agent-B/notes/simultaneous-skeleton-reduction.md`. It sharpens the
    remaining classical gap: pointwise redundancy of individual
    non-well-exposed vertices is not enough unless it is simultaneous or
    acyclic, because sequential deletion can accumulate dimension-dependent
    error. The exact sufficient target is an exposed skeleton of pairwise
    separated well-exposed representative rows with every non-cluster row
    `O(sqrt(delta))`-close to their convex hull. Wrote
    `agent-B/notes/response-to-agent-a-v0.17.md` to make this the latest
    Agent A-facing formulation.
77. Hubble sidecar stress-tested item 76 and confirmed the local deletion
    formulation is insufficient. Its report is
    `agent-B/notes/subagent-skeleton-reduction-v0.1.md`. I patched
    `agent-B/notes/simultaneous-skeleton-reduction.md` with the stronger
    global exposed-hull form: if `W_{rho,kappa}` is the set of
    square-root-well-exposed vertices and every row is `O(sqrt(delta))`-close
    to `conv W_{rho,kappa}`, then a maximal `4rho`-separated subset of `W`
    satisfies the cluster-representative hypotheses and yields a stochastic
    idempotent within `O(sqrt(delta))`. Wrote
    `agent-B/notes/response-to-agent-a-v0.18.md`; v0.18 is now the newest
    Agent A-facing formulation.
78. Patched `agent-B/notes/exposed-redundant-dichotomy-target.md` so it no
    longer presents the pointwise exposed-or-redundant dichotomy as sufficient
    by itself. It now explicitly says the local statement is useful only with
    a non-accumulating reconstruction certificate and points to the global
    exposed-hull target as the current clean formulation.
79. Patched `agent-B/theory/classical-cluster-factorization-theorem.md` with a
    global exposed-hull corollary. If the spectral idempotent row vertices
    exposed at `rho=O(sqrt(eta))` and gap `kappa>=c sqrt(eta)` have convex hull
    within `O(sqrt(eta))` of every row, then a maximal `4rho`-separated subset
    satisfies the cluster-representative hypotheses and the exact
    commutative positive/JB factorization theorem applies. Wrote
    `agent-B/notes/response-to-agent-a-v0.19.md`; v0.19 is now the newest
    Agent A-facing formulation.
80. Patched `agent-B/notes/theorem-stack-v0.3.md` so its classical
    projection-stability section matches the current route. It now marks the
    pointwise exposed-or-redundant dichotomy as insufficient by itself, names
    `agent-B/notes/simultaneous-skeleton-reduction.md` as the current global
    exposed-hull target, and notes the exposed-hull corollary in
    `agent-B/theory/classical-cluster-factorization-theorem.md`.
81. Added `agent-B/notes/stochastic-stoquastic-special-cases.md`. It records
    the canonical stochastic conjecture, equivalent signed-idempotent form,
    exact positive doubly stochastic block-average structure, signed
    doubly-stochastic conjecture, and symmetric stoquastic form via `H=I-Q`.
    It also summarizes numerical/proved evidence: Hume sharpness, small
    `3 x 3` searches, non-simplex stress tests, and null-ideal bridge
    experiments. It explicitly notes that no dedicated doubly-stochastic or
    stoquastic signed-idempotent numerical campaign has been run yet. Wrote
    `agent-B/notes/response-to-agent-a-v0.20.md`; v0.20 is now the newest
    Agent A-facing formulation.
82. Added `agent-B/notes/audit-consensus-2026-06-04.md`. It records the current
    consensus after Agent A's retraction: Layer 1 remains open at the
    dimension-free order-unit cochain homotopy; Layer 2 remains proved at
    `O(sqrt(eta))`; theorem C is conditional on projection stability; and the
    classical exact-factorization route is focused on the global exposed-hull
    lemma.
83. Added `agent-B/notes/regular-polygon-retraction-obstruction.md` and
    `agent-B/notes/symmetric-coordinate-negative-mass-criterion.md`, and patched
    `agent-B/notes/simultaneous-skeleton-reduction.md`. Dense fixed-diameter
    regular polygons are ruled out as exact signed affine retractions with
    vanishing negative mass; dihedral symmetrization forces constant negative
    mass at least `sqrt(3)/pi-1/3-o(1)`. The local dense-polygon warning remains
    logical, not an actual small-defect example.
84. Wrote `agent-B/notes/response-to-agent-a-v0.12-layer1-caveat.md`, the
    current response to Agent A v0.12. It agrees with the Frobenius-only
    correction and element-level symmetry/idempotent equivalence, but adds the
    module caveat: direct sums are automatic only for adjoint/block-respecting
    modules. Mixed Peirce-`1/2` modules, already present for `R^m`, prevent
    arbitrary-module block diagonalization.
85. Restored the historical file
    `agent-B/notes/response-to-agent-a-v0.12.md` to its older June 2 classical
    projection-stability response after moving the June 5 content to the
    separate `response-to-agent-a-v0.12-layer1-caveat.md` file.
86. Added `agent-B/notes/spin-splitting-audit-2026-06-05.md`. The spin
    element-norm reduction to an `Fop->Fop` Euclidean-injective splitting is
    correct, but the latter remains open and is not implied by HS pseudoinverse
    bounds, Schur's lemma, small multiplicity, or bounded rank. Agent A's
    rank-balance condition for `H_n` is directionally wrong as written.
87. Added `agent-B/notes/adjoint-spin-splitting-theorem.md` and patched the
    spin audit with a follow-up pointer. The exact adjoint spin benchmark is
    now proved: for `V=R1+H`, exact adjoint coboundaries have an `O(H)`-
    equivariant right inverse with `||S_H||_{Fop->Fop}<=2`, hence order-unit
    constant `<=4 sqrt(2)`. This closes only the adjoint exact spin case, not
    arbitrary modules or approximate Layer-1 ER.
88. Added `agent-B/notes/commutative-scalar-module-splitting.md`. The minimal
    scalar mixed Peirce-`1/2` modules over `R^m` are uniformly controlled:
    for one-dimensional modules `l=x_k` or `l=(x_p+x_q)/2`, exact coboundaries
    have the norm-one splitting `S_l f(x)=f(x,s)` with support unit
    `s=e_k` or `s=e_p+e_q`. This sharpens, but does not eliminate, the
    direct-sum caveat. The note now also covers arbitrary vector-valued
    multiplicities when the module is an `l_infty` direct sum of scalar sectors,
    and proves that every exact finite-dimensional `R^m` module decomposes
    algebraically into those sectors. For arbitrary module norms the resulting
    bound is controlled by the sector-projection complementability constant.
    It now also records the projection corollary `Pi=d^1S`, with norm `<=3` in
    max sector norm and `<=3K_dec` generally.
89. Added `agent-B/notes/peirce-sector-norm-accumulation.md`. In the adjoint
    module of `H_n(R)`, the off-diagonal Peirce sectors for the diagonal
    `R^n` frame are individually half-sum scalar sectors, but their coherent
    sum `sum_{i<j}(E_ij+E_ji)=11^T-I` has operator norm `n-1`. This is the
    concrete rank-growth obstruction behind the sector-projection constant.
90. Patched `agent-B/notes/theorem-stack-v0.3.md` so Theorem 1's status records
    the current partial Layer-1 splittings and caveats. The stack now names
    adjoint spin, exact commutative modules, and Peirce-sector accumulation
    explicitly before restating the remaining open Layer-1 obligations.
91. Added `agent-B/notes/diagonal-frame-matrix-module-splitting.md` and patched
    the Peirce accumulation note plus theorem stack. The diagonal-frame
    restriction of the adjoint `H_n(F)` module has a dimension-free exact
    coboundary splitting via a Rademacher/Schur-multiplier formula, with
    constant `11`. The same formula gives a projection onto `im(d^1)` with
    norm at most `33`. Thus `11^T-I` is a no-go for naive sector inclusion, not
    for exact coboundary inversion. The entrywise expectation computation has
    been written out explicitly.
92. Added `agent-B/notes/frame-covariance-and-global-matrix-obstacle.md` and
    patched the theorem stack. The fixed-frame matrix splitting transports to
    every Jordan frame with unchanged constants (`11` for `S_E`, `33` for
    `Pi_E`). The same note shows why the obvious frame-averaging globalization
    fails dimension-freely: averaged diagonal pinching has traceless eigenvalue
    `(n-1)/(dim_R H_n(F)-1)`, so reconstructing traceless information requires
    a rank-sized amplification.
93. Added `agent-B/notes/cochain-norm-conversion-caveat.md` and patched the
    theorem stack. The family `h_n(x)=x_11 1` in `H_n(R)` has order norm `1`
    and `||d^1h_n||_op<=3`, but every primitive of `d^1h_n` has
    Frobenius-injective norm at least `sqrt(n)`. This cleanly rules out the
    route "find Frobenius-bounded primitives for all order-bounded exact
    coboundaries" while leaving direct order-norm splitting open.
94. Added `agent-B/notes/central-valued-matrix-primitive-estimate.md` and
    patched the theorem stack. For central primitives
    `h_phi(x)=phi(x)1` on `H_n(F)`, `F=R,C,H`, the order-norm estimate
    `||h_phi|| <= ||d^1h_phi|| <= 3||h_phi||` holds uniformly in `n`.
    This shows the high-Frobenius central examples are actually controlled
    components for the desired order-norm splitting.
95. Added `agent-B/notes/multiplication-primitive-estimate.md` and patched the
    theorem stack. For every unital JB algebra, multiplication primitives
    `L_c(x)=c o x` satisfy `||L_c|| <= ||d^1L_c|| <= 3||L_c||`, with lower
    bound from evaluating `d^1L_c` at `(1,1)`.
96. Added `agent-B/notes/unit-normalized-adjoint-reduction.md` and patched the
    theorem stack. Every exact adjoint coboundary splits as the controlled
    multiplication part `L_{f(1,1)}` plus a unit-vanishing residual with
    normalized primitive. Constants: `||L_{f(1,1)}||<=||f||`,
    residual norm `<=4||f||`, and a normalized splitting constant `K` yields
    full constant `1+4K`.
97. Added `agent-B/notes/adjoint-direct-sum-reduction.md` and patched the
    theorem stack. For adjoint modules of direct sums, factor constants `K_r`
    combine as `max_r K_r+1`; off-block components are recovered by evaluating
    the coboundary at central units `e_r`, with no dependence on the number of
    summands.
98. Added `agent-B/notes/spin-direct-sum-adjoint-corollary.md` and patched the
    theorem stack. Arbitrary finite direct sums of spin factors have exact
    adjoint order-unit splitting constant `<=4 sqrt(2)+1`, independent of
    spin dimensions and summand count.
99. Added `agent-B/notes/bounded-rank-adjoint-reduction.md` and patched the
    theorem stack. For every fixed rank cutoff `R0`, bounded-rank exact adjoint
    factors plus arbitrary spin factors and direct sums have a finite constant
    depending only on `R0`; the only exact-adjoint asymptotic left is the
    high-rank matrix sequence `H_n(R/C/H)`.
100. Added
     `agent-B/notes/trace-zero-rank-one-matrix-primitive-estimate.md` and
     patched the theorem stack. Normalized rank-one matrix primitives
     `h(x)=phi(x)c`, `phi(1)=0`, satisfy
     `(1/2)||h|| <= ||d^1h|| <= 3||h||` uniformly in `n`.
101. Added `agent-B/notes/nuclear-rank-one-route-caveat.md` and patched the
     theorem stack. Rank-one estimates summed through nuclear decompositions
     cannot be dimension-free in general: `nu(Id_{J_0})>=dim J_0` while
     `||Id_{J_0}||=1`.
102. Added `agent-B/notes/diagonal-frame-matrix-next-arrow-walsh-target.md`
     and patched the theorem stack plus Layer 1 obligations note. The
     first version localized the open gap to the off-diagonal tail-tail
     tensor `W_ij(x^{ij},y^{ij})`; the same session then closed it by a
     two-density sparse-sign reconstruction. The final theorem is
     `dist(theta,im d^1)<=C||Jtheta||` and, using the bounded Rademacher
     projection, `||theta-Pi_n theta||<=C'||Jtheta||`, uniformly for
     `H_n(F)`, `F=R,C,H`, restricted to a fixed diagonal frame.
103. Added `agent-B/notes/next-arrow-to-newton-error-reduction.md` and patched
     the theorem stack plus Layer 1 obligations note. The note proves the
     conditional Newton step: once a unit-normalized exact adjoint complex has
     constants `K_1` for exact coboundary inversion and `K_2` for the
     next-arrow estimate, product perturbations improve by
     `delta -> C(K_1,K_2)(epsilon+delta^2)`. This isolates the remaining
     Layer 1 burden as the global/incremental exact-complex estimates plus
     approximate-module robustness, not the coordinate-change algebra.
104. Added
     `agent-B/notes/full-matrix-next-arrow-source-decomposition-target.md` and
     patched the theorem stack plus Layer 1 obligations note. The next
     high-rank matrix next-arrow target is now explicitly split by source:
     `D x D` closed, `D x E` leakage open, `E x E` Peirce
     curvature/matching open. This is the recommended continuation point for
     matrix next-arrow work.
105. Added `agent-B/notes/report-review-v0.2.md` after Agent A updated
     `report/main.tex`. Five read-only skeptical subagents audited Layer 1,
     bridge/factorization, classical stability, coverage, and build/provenance.
     Build succeeds, but the report has required fixes: faithful-invariant
     polarization must use triangle inequality rather than a false parallelogram
     law; Section 8 must align exposedness with the outside-row-set target,
     remove the false nesting claim, and restore small-defect thresholds; Layer
     1 must include pre-cohomological gaps; cochain notation/norms must be
     defined; high-rank matrix status should reflect independent re-audit
     pending; and provenance/status hygiene needs cleanup. Agent B did not edit
     the report in this pass.
106. Patched the report to address the v0.2 audit findings. Key fixes:
     faithful-invariant polarization now uses the triangle inequality;
     Effros--Stormer/factorization wording distinguishes projected product and
     UP vs decomposable maps; classical exposedness, non-nesting, small-defect
     thresholds, and regular-polygon caveats are corrected; Layer 1 now defines
     the injective cochain norm and `Jtheta`, records the fixed diagonal-frame
     matrix next-arrow proposition, splits the full matrix next-arrow target
     into `D x D`, `D x E`, `E x E`, and explicitly lists the
     pre-cohomological/approximate-module gaps; high-rank matrix claims are
     marked as benchmark/re-audit pending; provenance hashes and ledger rows
     are refreshed. Verification: `cd report && make` succeeds and
     `git diff --check` is clean on the touched report/coordination files.

## Active Subagent Results Incorporated

- "Banach" extracted the exact Kitaev dependency chain and flagged CP-essential steps.
- "Pascal" extracted positive-map/Jordan facts and flagged approximate obstacles.
- "Aristotle" found no counterexample to small Jordan defect, but produced an explicit classical `R^4` stochastic family where `Pi=theta(2Phi-I)` is not positive. Therefore any theorem claiming `Pi` itself is positive is false even classically. In that family the projected-product Jordan defect is small, empirically `O(a^2)` while `eta=O(a)`.
- "Parfit" found no low-dimensional counterexample to the null-ideal estimate
  and identified a sharp-looking classical `R^3` family with linear
  `||P(h_{r,s}^2)||=Theta(eta)`.
- "McClintock" disproved generic dimension-free `O(epsilon)` positivity
  rounding using spin-factor targets; black-box rounding may lose a square
  root.
- "Pasteur" checked that the spin-factor positivity-rounding obstruction does
  not directly produce a near-positive idempotent counterexample.
- "Hume" disproved linear classical near-positive projection stability and
  showed exponent `1/2` is sharp if such stability holds.
- "Gibbs" and "Heisenberg" reduced classical near-positive projection stability
  to the Markov almost-idempotent theorem above; they found no proof/citation
  and no dimension-growth obstruction in the tested multi-escape model.
- "Sartre" stress-tested the decomposable `O(eta)` route; no counterexample to
  the actual Jordan-defect statement was found, but the naive universal-envelope
  proof fails for arbitrary supplied decompositions.
- "Boyle" audited the formal bridge proof after the null-ideal upgrade. It did
  not find a fatal local gap, and its main concern, the spectral-idempotent
  estimate, has been patched into the proof.
- "Lagrange" audited the Layer 1 averaging/cohomology route and confirmed the
  main missing estimate is the dimension-free bounded cochain homotopy in the
  order-unit norm.
- "Fermat" probed the remaining non-simplex classical projection-stability
  obstruction and found no counterexample, but identified the facet-count /
  angle-loss and affine-dependence cancellation lemmas needed to finish the
  exposed-face recursion.
- "Popper" isolated the coordinate-rectangle cancellation lemma: bounded
  `[0,1]` affine rectangle coordinates force the alternating corner relation
  to have `l1` norm at least `4-O(sqrt(delta))`; exact parallelogram row
  polytopes are therefore impossible for small `delta`.
- "Wegener" stress-tested the remaining classical non-simplex route. No
  counterexample was found. Tensor Hume is dangerous only against naive
  product rounding, not against all stochastic-idempotent transient-class
  roundings. Wegener isolated the exposed-circuit cancellation lemma and
  reformulated the remaining gap as an exposed-or-redundant vertex dichotomy.
- "Hubble" stress-tested the exposed-or-redundant deletion formulation and
  found it logically insufficient without a non-accumulating certificate.
  Dense regular polygons provide the convex-geometric obstruction to the
  local implication. Hubble recommended the global exposed-hull target now
  recorded in `agent-B/notes/simultaneous-skeleton-reduction.md`.
