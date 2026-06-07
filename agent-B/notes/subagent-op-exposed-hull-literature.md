# Subagent G - Literature Search For `op-exposed-hull`

Date: 2026-06-07.  Lane: Agent B exploration sandbox.  Status: literature
scout only, not canonical ground truth.

Read first: `agent-B/notes/op-exposed-hull-mission-control.md` and
`agent-B/notes/op-exposed-hull-literature-scout-2026-06-07.md`.

## Target Recalled

`op-exposed-hull` asks for a dimension-free global skeleton statement for an
exact signed affine retraction:

```text
P1 = 1,  P^2 = P,  neg(p_i) <= delta,  tau = sqrt(delta).
```

For `rho = C tau`, `kappa = c tau`, if `W_{rho,kappa}` is the set of row
vertices with exposedness modulus at least `kappa` at scale `rho`, prove

```text
dist_1(p_i, conv W_{rho,kappa}) <= C' tau
```

for every row.

## Search Method

Sources used: broad web search, Crossref metadata queries, limited Semantic
Scholar API search, arXiv pages, journal landing pages, repository PDFs, and
the existing local Agent B scout note.

Search phrases included:

```text
idempotent stochastic matrices
idempotent Markoff chains
near idempotent stochastic matrix perturbation
almost idempotent stochastic matrix
regularized power limit stochastic matrix
ergodic projector finite Markov chain
Hoffman constant linear inequalities reference polyhedron
approximate affine retraction simplex
exposed points convex sets strong exposed stability
convex hull vertex selection approximation polytope
```

## Verdict

No source found states the needed theorem, or an obvious equivalent:

```text
near-positive signed affine idempotent retractions are O(sqrt(delta))-close to
the hull of uniformly well-exposed row vertices, dimension-free.
```

The useful literature is indirect:

- exact idempotent stochastic matrices and their semigroup geometry are well
  covered;
- Markov-chain power-limit/eigenprojection tools produce exact stochastic
  idempotents under spectral/ergodic assumptions, but do not give the
  dimension-free signed-retraction rounding needed here;
- Hoffman/error-bound theory gives the right LP-dual language, but generic
  constants depend on conditioning and cannot be cited as a black box;
- exposed-point convexity theorems are qualitative/topological, not the
  simultaneous quantitative `sqrt(delta)` skeleton lemma.

All theorem relevance below is `[UNVERIFIED - needs local refs/]` until a
payload is acquired under `refs/` and byte-checked.

## Highest-Priority Sources

### 1. Blackwell - idempotent Markoff chains

- David Blackwell, "Idempotent Markoff chains", Annals of Mathematics (2) 43
  (1942), no. 3, 560-567.
- DOI: `10.2307/1968811`
- URL: `https://celebratio.org/Blackwell_DH/article/252/`
- Relevance: foundational exact `P^2=P` Markov-kernel source. Useful for
  terminology and the exact idempotent endpoint. Does not address perturbative
  signed near-positivity.
- Refs recommendation: acquire PDF from JSTOR/Celebratio and byte-pin. Also
  acquire Blackwell's 1941 thesis only if the classification proof is absent
  from the paper.

### 2. Schwarz - semigroup of stochastic matrices

- Stefan Schwarz, "On the Structure of the Semigroup of Stochastic Matrices",
  Magyar Tud. Akad. Mat. Kutato Int. Kozl. 9 (1964), 297-311.
- URL: `https://real.mtak.hu/189463/`
- PDF: `https://real.mtak.hu/189463/1/cut_MATKUTINT_1964_3_pp297_-_311.pdf`
- Relevance: exact semigroup/idempotent structure inside stochastic matrices.
  Relevant to the final stochastic idempotent shape after `op-exposed-hull`,
  not a quantitative rounding theorem.
- Refs recommendation: acquire the repository PDF. It is open and appears
  suitable for local byte verification.

### 3. Gonzalez-Hartfiel - stochastic idempotent matrix space

- Raul Ernesto Gonzalez and D. J. Hartfiel, "On the structure of the stochastic
  idempotent matrix space", Linear Algebra and its Applications 145 (1991),
  141-158.
- DOI: `10.1016/0024-3795(91)90292-5`
- URL: `https://www.sciencedirect.com/science/article/pii/0024379591902925`
- Relevance: describes the space of stochastic idempotents as pieces
  homeomorphic to polytopes. This is likely the best exact finite-dimensional
  geometry source for the endpoint, especially if the proof needs a local
  chart around a stochastic idempotent stratum.
- Refs recommendation: acquire open-archive PDF if accessible through
  ScienceDirect, otherwise request via library.

### 4. Gonzalez-Torres - cores of idempotent stochastic matrices

- Raul E. Gonzalez-Torres, "A geometric study of cores of idempotent stochastic
  matrices", Linear Algebra and its Applications 527 (2017), 87-127.
- DOI: `10.1016/j.laa.2017.03.032`
- URL: `https://www.sciencedirect.com/science/article/pii/S0024379517302124`
- Relevance: studies cores of idempotents in the compact affine semigroup of
  stochastic matrices, including lattice/core geometry. Good language for
  exact positive idempotents and their surrounding semigroup, but not a
  signed-perturbation result.
- Refs recommendation: acquire the open-archive PDF.

### 5. Gonzalez-Torres - maximal monoids

- Raul E. Gonzalez-Torres, "A geometric description of the maximal monoids of
  some matrix semigroups", Linear Algebra and its Applications 445 (2015),
  275-290.
- DOI: `10.1016/j.laa.2014.10.035`
- URL: `https://www.sciencedirect.com/science/article/pii/S0024379514007149`
- Relevance: exact affine-semigroup structure; includes maximal monoids around
  idempotents and affine isomorphisms to lower-dimensional stochastic matrix
  semigroups. Potentially useful if a skeleton proof is rephrased as moving
  into a core/maximal monoid.
- Refs recommendation: acquire after Gonzalez-Hartfiel and the 2017 core
  paper.

## Markov Projection And Perturbation Tools

### 6. Agaev-Chebotarev - regularized power limit

- R. P. Agaev and P. Yu. Chebotarev, "The projection method for reaching
  consensus and the regularized power limit of a stochastic matrix",
  Automation and Remote Control 72 (2011), no. 12, 2458-2476.
- DOI: `10.1134/S0005117911120034`
- arXiv: `https://arxiv.org/abs/1109.3948`
- Relevance: provides a regularized power-limit/eigenprojection construction
  for stochastic matrices. It may be a useful numerical candidate for exact
  stochastic idempotents from an almost-idempotent stochastic matrix. It does
  not give a dimension-free `sqrt(delta)` perturbation bound for signed
  retractions.
- Refs recommendation: acquire arXiv source/PDF and journal metadata.

### 7. Berkhout-Heidergott - finite-chain ergodic projector

- Joost Berkhout and Bernd F. Heidergott, "The Jump Start Power Method: A New
  Approach for Computing the Ergodic Projector of a Finite Markov Chain",
  Journal of Scientific Computing 78 (2019), 1691-1723.
- DOI: `10.1007/s10915-018-0828-1`
- URL: `https://link.springer.com/article/10.1007/s10915-018-0828-1`
- Relevance: numerical and analytic methods for finite Markov-chain ergodic
  projectors. Useful for experiments and sanity checks against power-limit
  candidates, not a proof of `op-exposed-hull`.
- Refs recommendation: acquire open-access PDF if available from Springer.

### 8. Seneta - ergodicity coefficients and perturbation

- E. Seneta, "Coefficients of ergodicity: structure and applications",
  Advances in Applied Probability 11 (1979).
- DOIs found by Crossref: `10.2307/1426800` and `10.2307/1426955`
  (likely parts/issues; verify before canonical use).
- E. Seneta, "Sensitivity of finite Markov chains under perturbation",
  Statistics & Probability Letters 17 (1993), 163-168.
- DOI: `10.1016/0167-7152(93)90011-7`
- Relevance: gives standard perturbation machinery for stationary
  distributions and finite chains via coefficients of ergodicity and group
  inverses. This is relevant to resolvent estimates in the maximal-skeleton
  route, but existing results are typically spectral-gap or irreducibility
  conditioned, not the dimension-free bad-kernel alternative needed here.
- Refs recommendation: acquire Seneta 1979 and 1993 if the proof develops a
  bad-kernel resolvent certificate.

### 9. Hartfiel-Meyer - near-decomposable stochastic matrices

- D. J. Hartfiel and C. D. Meyer, "On the structure of stochastic matrices
  with a subdominant eigenvalue near 1", Linear Algebra and its Applications
  272 (1998), 193-203.
- DOI: `10.1016/S0024-3795(97)00333-9`
- URL: `https://citeseerx.ist.psu.edu/document?doi=6b332d3e46d4b21751f646374060897426dad6b4`
- Relevance: near-uncoupling from spectral information. This is a warning more
  than a tool: spectral near-1 behavior can suggest cluster structure, but
  constants are not obviously dimension-free and the hypothesis differs from
  exact signed idempotence plus small negative mass.
- Refs recommendation: lower priority; acquire if using a spectral cluster
  argument.

## LP, Hoffman, And Error Bounds

### 10. Hoffman - approximate linear inequalities

- A. J. Hoffman, "On approximate solutions of systems of linear inequalities",
  Journal of Research of the National Bureau of Standards 49 (1952), 263-265.
- DOI: `10.6028/jres.049.027`
- PDF: `https://upload.wikimedia.org/wikipedia/commons/0/07/On_approximate_solutions_of_systems_of_linear_inequalities_%28IA_jresv49n4p263%29.pdf`
- Relevance: source of Hoffman bounds: near satisfaction of a consistent
  finite linear inequality system implies distance to the solution set bounded
  by violation times a system constant. This exactly matches the LP-dual style
  of subagent A, but generic Hoffman constants are system-conditioned and do
  not provide the universal bound.
- Refs recommendation: acquire and byte-pin. This is a clean, short primary
  source.

### 11. Pena-Vera-Zuluaga - computable Hoffman constants

- Javier Pena, Juan Vera, Luis Zuluaga, "An algorithm to compute the Hoffman
  constant of a system of linear constraints", arXiv:1804.08418.
- arXiv: `https://arxiv.org/abs/1804.08418`
- Javier Pena, Juan Vera, Luis Zuluaga, "New characterizations of Hoffman
  constants for systems of linear constraints", arXiv:1905.02894.
- arXiv: `https://arxiv.org/abs/1905.02894`
- Relevance: useful if we build the joint feasibility LP certificate A5 and
  want to compute/interpret constants. The reference-polyhedron version is
  especially relevant because the row-positive constraints live in a simplex
  or box-like reference set. Still no universal constant without special
  structure.
- Refs recommendation: acquire arXiv PDFs if the LP-certificate workstream
  continues.

### 12. Robinson - stability of linear inequalities

- Stephen M. Robinson, "Bounds for error in the solution set of a perturbed
  linear program", Linear Algebra and its Applications 6 (1973), 69-81.
- DOI: `10.1016/0024-3795(73)90007-4`
- Stephen M. Robinson, "Stability theory for systems of inequalities. Part I:
  Linear systems", SIAM Journal on Numerical Analysis 12 (1975), 754-769.
- DOI: `10.1137/0712056`
- Relevance: broader perturbation/error-bound setting for LP systems. Likely
  secondary to Hoffman/Pena-Vera-Zuluaga unless the proof needs set-valued
  solution-map stability.
- Refs recommendation: lower priority.

## Exposed Points And Convex Skeletons

### 13. Straszewicz - exposed points dense in extreme points

- Stefan Straszewicz, "Uber exponierte Punkte abgeschlossener Punktmengen",
  Fundamenta Mathematicae 24 (1935), 139-143.
- DOI: `10.4064/fm-24-1-139-143`
- EUDML: `https://eudml.org/doc/212740`
- Relevance: qualitative finite-dimensional theorem: exposed points are dense
  in extreme points. This is conceptually adjacent but far too weak for
  `op-exposed-hull`, which needs a scale-aware simultaneous hull made from
  well-exposed vertices.
- Refs recommendation: acquire if the report cites the qualitative baseline.

### 14. Choquet-Corson-Klee - exposed points of convex sets

- Gustave Choquet, Harry Corson, Victor Klee, "Exposed points of convex sets",
  Pacific Journal of Mathematics 17 (1966), 33-43.
- DOI: `10.2140/pjm.1966.17.33`
- PDF: `https://msp.org/pjm/1966/17-1/pjm-v17-n1-p03-p.pdf`
- Relevance: precise descriptive/topological information on exposed points.
  Confirms that exposed-point structure is subtle even in finite dimension.
  Does not give the quantitative reconstruction lemma.
- Refs recommendation: acquire PDF; useful for the "generic convex geometry is
  insufficient" caveat.

### 15. De Wilde - finite-dimensional exposed point properties

- Marc De Wilde, "Some properties of the exposed points of finite-dimensional
  convex sets", Journal of Mathematical Analysis and Applications 99 (1984),
  257-264.
- DOI: `10.1016/0022-247X(84)90247-6`
- URL: `https://www.sciencedirect.com/science/article/pii/0022247X84902476`
- Relevance: finite-dimensional exposed/strongly exposed cone properties.
  Possibly useful for local modulus language, but not a global hull theorem.
- Refs recommendation: low-to-medium priority.

### 16. Cihak - exposed elements of doubly stochastic rectangular matrices

- Pavel Cihak, "On an exposed element of a set of doubly stochastic rectangular
  matrices", Commentationes Mathematicae Universitatis Carolinae 11 (1970),
  99-113.
- URL: `https://dml.cz/handle/10338.dmlcz/105268`
- Relevance: directly about exposed elements in a stochastic-matrix polytope.
  The matrix set differs from row-polytope `K=conv{p_i}`, but this may be a
  useful reference problem for exposedness under stochastic constraints.
- Refs recommendation: acquire only if the proof starts using exposed faces of
  stochastic matrix polytopes.

## Affine Retractions And Choquet Simplexes

### 17. Alfsen - compact convex sets and affine face retractions

- Erik M. Alfsen, "Compact Convex Sets and Boundary Integrals", Springer,
  1971; Ergebnisse der Mathematik und ihrer Grenzgebiete, vol. 57.
- DOI: `10.1007/978-3-642-65009-3`
- Open Library: `https://openlibrary.org/books/OL5316253M/Compact_convex_sets_and_boundary_integrals`
- Relevance: source for compact convex-set/Choquet-simplex face theory and
  affine retraction language. Existing web snippets say closed faces of
  compact metrizable simplexes admit continuous affine retractions. This is
  topological and exact; it does not produce a finite-dimensional quantitative
  `sqrt(delta)` approximation.
- Refs recommendation: acquire only if report text uses "affine retraction"
  background. Do not cite web snippets canonically.

### 18. Approximate retract literature

- Search found "approximative relative retract" and topological ANR-style
  sources, but no source matching finite-dimensional quantitative affine
  retract stability of a simplex under signed idempotent perturbation.
- Relevance: negative lead. The terminology overlaps, but the results appear
  topological/selection-theoretic, not LP/polytope quantitative.
- Refs recommendation: no acquisition unless a later proof actually invokes
  Choquet/selection machinery.

## Explicit Negative Findings

The following attempted routes did not produce a close theorem:

1. **Near-idempotent stochastic matrix stability.** Search hits mostly concern
   spectral idempotents, Markov power limits, or quantum-channel almost
   idempotence. No dimension-free classical theorem of the needed
   `O(sqrt(eta))` form was found.

2. **Generic Markov perturbation theory.** Useful for irreducible/gapped chains
   and stationary distributions, but `op-exposed-hull` must allow multiple
   classes and zero spectral gaps. The bad-kernel resolvent estimate would
   have to be proved from `P^2=P` and `neg<=delta`.

3. **Generic Hoffman bounds.** They give the right language for Farkas/LP
   certificates but constants are controlled by matrix conditioning. A
   successful proof needs a special normalized system whose Hoffman constant is
   universal, or an explicit hand-built dual contradiction.

4. **Straszewicz/strongly exposed point theory.** Qualitative density of
   exposed points does not imply a simultaneous `rho,kappa` well-exposed hull.
   It also ignores the row-fixity identity.

5. **Convex-hull approximation and coresets.** Most results are either
   dimension-dependent, randomized, or optimize a fixed objective family. They
   do not use signed retraction identities and do not control all rows in
   `l_1` at `sqrt(delta)`.

## Best Proof-Relevant Takeaways

1. The theorem is likely new; do not expect to close it by citation.

2. The exact endpoint literature should be used only after the skeleton theorem
   produces a stochastic idempotent candidate. It will help identify/classify
   the endpoint, not prove closeness.

3. The strongest imported tool for the active proof is Hoffman/Farkas duality,
   but it must be fused with the special identity

```text
p_i = p_i P = sum_j p_i(j) p_j
```

   and the repaired positive-coordinate kernel

```text
q_i = p_i^+ / (1 + neg(p_i)).
```

4. The most promising literature-backed experiment is to compute Hoffman
   constants or infeasibility certificates for the joint LP A5 in small cases,
   then identify any multiplier pattern that uses right-fixity.

5. The maximal-skeleton route should search for a Markov-chain theorem only at
   the level of substochastic bad-kernel resolvents. Existing ergodicity
   coefficient literature can provide comparison language, but the actual
   `O(1/tau)` exit/resolvent bound appears to be a new lemma.

## Refs Acquisition Plan

Priority 0, acquire immediately if canonicalizing any part of the classical
route:

- Blackwell 1942, `10.2307/1968811`
- Schwarz 1964 repository PDF
- Hoffman 1952, `10.6028/jres.049.027`
- Choquet-Corson-Klee 1966, `10.2140/pjm.1966.17.33`
- Straszewicz 1935, `10.4064/fm-24-1-139-143`

Priority 1, acquire for endpoint geometry and exact stochastic idempotents:

- Gonzalez-Hartfiel 1991, `10.1016/0024-3795(91)90292-5`
- Gonzalez-Torres 2015, `10.1016/j.laa.2014.10.035`
- Gonzalez-Torres 2017, `10.1016/j.laa.2017.03.032`

Priority 2, acquire if numerical/LP/resolvent workstream produces a proof:

- Agaev-Chebotarev 2011, `10.1134/S0005117911120034`, arXiv:1109.3948
- Berkhout-Heidergott 2019, `10.1007/s10915-018-0828-1`
- Seneta 1979/1993, `10.2307/1426800`, `10.2307/1426955`,
  `10.1016/0167-7152(93)90011-7`
- Pena-Vera-Zuluaga arXiv:1804.08418 and arXiv:1905.02894
- Robinson 1973/1975, `10.1016/0024-3795(73)90007-4`, `10.1137/0712056`

Priority 3, only if terminology needs it:

- Alfsen 1971, `10.1007/978-3-642-65009-3`
- De Wilde 1984, `10.1016/0022-247X(84)90247-6`
- Cihak 1970 DML-CZ PDF

## Next Handoff

Recommended next subagent task:

```text
Build the joint LP infeasibility model A5 from
subagent-op-exposed-hull-lp-dual.md.  For fixed small n and symbolic or
rational delta, include failed exposedness duals for all separator-high rows,
P^2=P, row sums 1, and neg<=delta.  Use Gurobi CLI / scipy / Wolfram to mine
dual multipliers.  Compare any certificate with Hoffman canonical constants
and the positive-coordinate bad-kernel resolvent certificate.
```

If that model gives feasible counterexamples, export exact rational data under
`agent-B/experiments/op-exposed-hull/`.  If infeasible, the dual certificate is
the next best candidate for a formalisable proof skeleton.
