# op-exposed-hull Literature Scout

Date: 2026-06-07.  Agent B sandbox.  Web-scouted leads only; not local
ground truth.  Any source used canonically must be added to `refs/` and
byte-checked.

## Directly relevant leads

1. Gonzalez-Torres, "A geometric study of cores of idempotent stochastic
   matrices", Linear Algebra and its Applications 527 (2017), 87--127.
   DOI: `10.1016/j.laa.2017.03.032`.
   URL: `https://www.sciencedirect.com/science/article/pii/S0024379517302124`.
   Relevance: geometry of idempotents in the compact affine semigroup of
   stochastic matrices; "cores" and lattice structure may give language for the
   exact positive endpoint and nearby retraction geometry.
   Current assessment: useful background, unlikely to prove near-positive
   stability directly.

2. Schwarz, "On the structure of the semigroup of stochastic matrices",
   Magyar Tud. Akad. Mat. Kutato Int. Kozl. 9 (1964), 297--311.
   URL: `https://real.mtak.hu/189463/`.
   PDF: `https://real.mtak.hu/189463/1/cut_MATKUTINT_1964_3_pp297_-_311.pdf`.
   Relevance: classical semigroup decomposition of stochastic matrices and
   idempotents of every rank.
   Current assessment: likely good for exact stochastic idempotent structure,
   not approximate signed idempotents.

3. Blackwell, "Idempotent Markoff chains", Annals of Mathematics 43 (1942),
   560--567.  DOI: `10.2307/1968811`.
   URL: `https://celebratio.org/Blackwell_DH/article/252/`.
   Relevance: foundational classification of idempotent Markov kernels.
   Current assessment: may clarify the exact recurrent/transient decomposition
   but not the quantitative signed perturbation.

4. Agaev and Chebotarev, "The Projection Method for Reaching Consensus and the
   Regularized Power Limit of a Stochastic Matrix", Automation and Remote
   Control 72 (2011), 2458--2476; arXiv:1109.3948.
   Relevance: regularized idempotent/power-limit projection associated to a
   stochastic matrix.
   Current assessment: possible alternate exact idempotent candidate for an
   almost-idempotent stochastic matrix, but not obviously close in
   `l_infty -> l_infty` at dimension-free `sqrt eta`.

5. Hoffman error-bound literature for linear inequalities.
   Primary source: Hoffman, "On approximate solutions of systems of linear
   inequalities", Journal of Research of the National Bureau of Standards 49
   (1952), 263--265.
   URL: `https://nvlpubs.nist.gov/nistpubs/jres/049/4/v49.n04.a05.pdf`.
   Modern computable constants:
   Pena--Vera--Zuluaga, "An algorithm to compute the Hoffman constant of a
   system of linear constraints", arXiv:1804.08418.
   Reference-polyhedron variant:
   Pena--Vera--Zuluaga, "New characterizations of Hoffman constants for
   systems of linear constraints", arXiv:1905.02894.
   Relevance: the LP-dual route may need a dimension-free error bound for a
   polyhedral system whose constants are controlled by `P^2=P` and negative
   mass, not by arbitrary facet angles.
   Current assessment: generic Hoffman constants depend on matrix conditioning,
   so this is a framework, not a ready theorem.  Useful if the right-fixity
   identities create a normalized system with a universal Hoffman constant.

6. Complexity/stability caveat for generic error bounds.
   Search found recent complexity literature indicating that verifying or
   stabilizing arbitrary linear-inequality error bounds is computationally
   hard outside fixed dimension.  This reinforces that a successful proof must
   exploit the signed-retraction structure, not cite a black-box Hoffman
   bound.

## Search verdict so far

No found theorem directly states:

```text
almost-idempotent row-stochastic matrix is O(sqrt eta)-close to an idempotent
row-stochastic matrix, dimension-free
```

and no found convex-geometry theorem directly supplies the global exposed-hull
lemma.  The most promising imported tools are exact stochastic-idempotent
structure and LP/Hoffman duality; the missing quantitative estimate still seems
new.
