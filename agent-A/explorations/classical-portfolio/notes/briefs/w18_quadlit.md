# w18_quadlit: the quadratic-matrix-constraint literature — what already exists

You are a codex (gpt-5.5) RESEARCH-RECON worker in a 5-worker round whose shared
charge is: exploit the exact quadratic constraint P^2 = P to its fullest. Your
lens: IT IS NOT THE FIRST TIME someone has a quadratic constraint on a matrix —
map the existing mathematical technology and rank what transfers.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps (read-only).
You have NO network: you are mining your TRAINING KNOWLEDGE. Therefore EVERY
claim you make is an UNVERIFIED-LEAD by definition: state it precisely (theorem
statement, named source: author/title/year/where in the book or paper), so the
orchestrator can acquire + byte-pin it into refs/ before any binding use. The
repo's law: nothing binds until byte-matched locally. Precision of the lead IS
the deliverable.

## CONTEXT (read first)
1. agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex — the
   problem: exact signed stochastic idempotents (P^2 = P, P1 = 1, entries >=
   -delta rowwise), target = the linear law delta >= c*H (equivalently: every
   such P is O(delta)-close in the right sense to the nonneg stochastic
   idempotent normal form = Hognas-Mukherjea/Baake-Sumner classification —
   see §5 items; "B-S normal-form distance" is the audited W-free target).
2. The dossier wave-10 table + meta-finding + wave-15/16 sections
   (notes/wave5-sigma-wall-parallel.md): the recorded dead ends.

## SURVEY DOMAINS (cover at least these; add more — surprise us)
a. PERTURBATION OF IDEMPOTENTS/PROJECTIONS: Kato (Perturbation Theory, Ch. I-II)
   — analytic similarity transformations between nearby projections, the
   explicit U = (PQ + (1-P)(1-Q))(1 - (P-Q)^2)^{-1/2}; idempotents at distance
   < 1 are similar; Riesz/holomorphic functional calculus error bounds. WHICH
   exact statements + where.
b. THE GEOMETRY OF IDEMPOTENT SETS in Banach algebras: Aupetit, Esterle,
   Zemanek (connected components of idempotents, polynomial paths,
   ||p - q|| >= 1/||2p-1|| style gaps); the Grassmannian gap metric; graph
   subspaces / rotation of invariant subspaces (Davis-Kahan!) — quantitative
   subspace perturbation under non-self-adjoint perturbations.
c. NONNEGATIVE IDEMPOTENT MATRICES: Flor (1969?) classification; nonnegative
   matrix theory near idempotents; eventually nonnegative matrices; Perron
   theory for signed/quasi-positive matrices.
d. ALGEBRAIC RICCATI: the corner equation X = X A X-type quadratic systems,
   their perturbation/conditioning theory, Newton methods with global
   convergence on the idempotent/invariant-subspace formulation.
e. STABILITY OF SUBALGEBRAS/PROJECTIONS in operator algebras: "almost
   projections are near projections" (standard C*-fact: spectral gap of an
   almost-idempotent ⇒ a true idempotent nearby — Kitaev's Lemma-style); BUT
   our P is EXACTLY idempotent and the perturbation is in the POSITIVITY —
   find work on "almost-positive projections", "almost completely positive",
   matrices idempotent + entrywise-near-nonnegative; stability of stochastic
   semigroup structure (Markov perturbation theory, quasi-stationary
   distributions, nearly uncoupled chains / Simon-Ando aggregation,
   stochastic complementation - Meyer!).
f. SEMI-ALGEBRAIC/REAL-GEOMETRY tools for matrix varieties: determinantal
   varieties, Lojasiewicz inequalities for the distance to a variety
   (THE LINEAR LAW IS A LOJASIEWICZ-TYPE INEQUALITY with exponent 1 between
   two semi-algebraic sets! — the distance-to-{delta=0-locus} vs the
   function H; Lojasiewicz exponent theory: when is the exponent 1? error
   bounds in semi-algebraic optimization, Hoffman bounds for polynomial
   systems) — this may be the single sharpest framing: name the exact
   theorems (Lojasiewicz, Kurdyka, error-bound literature: Luo-Pang, Li,
   Mordukhovich) that could give delta >= c(n)*H FOR FREE at fixed n, and
   what controls the constant's n-dependence.
g. Anything else your training knows about "quadratic matrix equation +
   entrywise positivity": copositive programming, completely positive
   factorizations, sign-pattern matrix theory of idempotents.

## DELIVERABLE (verdict-first)
A RANKED TABLE (top 10): lead | exact statement (display math where possible) |
source (author, title, year, section/theorem number, confidence in the
reference's existence 0-1) | what it would do for the campaign (which open:
linear law / quotient floor / anti-splitting / sigma-H tradeoff) | what could
break the transfer. Then a paragraph per top-3 lead sketching the attack. Then
the acquisition shopping list (what to download/buy, in priority order).
Calibrated P(at least one lead is decisive). DO NOT soften reference
uncertainty — wrong-but-precise is recoverable, vague is useless.
