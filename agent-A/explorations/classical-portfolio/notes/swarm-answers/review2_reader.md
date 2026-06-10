I read only `report/main.tex` and `report/sections/*.tex` in order, as requested.

1. [main.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/main.tex:130): Claims “The report is self-contained,” but later imports `lem-classical-equiv`, `thm-cluster`, Baake--Sumner anchors, source assemblies, and numerical artifacts. Fix: weaken the claim or include full statements/proofs/contracts sufficient to use them.

2. [01-linear-markov-setting.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/sections/01-linear-markov-setting.tex:112): Imported equivalence contract uses undefined `\theta(2Q-1)` and “row-normalising \(p_i^+\).” Fix: define the transform, the ambient all-ones matrix/vector, and the normalization map.

3. [04-reduction-chain.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/sections/04-reduction-chain.tex:57): “HLC assembly implies `op-exposed-hull`” relies on a new “source assembly” stronger than HLC. Fix: state this as a separate imported proposition or prove why HLC alone gives the assembly.

4. [05-corner-theorem.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/sections/05-corner-theorem.tex:15): “Corner family” is not actually defined; it is “the verified d8--d12 budget-line family” with “binding financier” and “apex poke.” Fix: give the family parametrization or move this out of theorem-like status.

5. [08-residual-dmf.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/sections/08-residual-dmf.tex:82): Notation contradiction: says the geometric branch variable is “not the older index-based \(\sigoff\),” but \(\sigoff\) was formal off-own-site mass, distinct from the index-not-in-\(W\) proxy. Fix: name all three quantities consistently.

6. [02-geometry-exposedness.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/sections/02-geometry-exposedness.tex:130): Small-\(\sigtilde\) barycenter proof normalizes the \(C_W\)-part without stating that its mass is positive. Fix: add the missing case split or prove positivity.

7. [08-residual-dmf.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/sections/08-residual-dmf.tex:104): Same barycenter normalization gap repeated. Fix: centralize this lemma once with full hypotheses.

8. [00-abstract-roadmap.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/sections/00-abstract-roadmap.tex:27): Roadmap front-loads HLC, DMF, “optimal failed-exposedness witness,” “depth window,” “hidden webs,” and Baake--Sumner before definitions. Fix: add a short pre-roadmap glossary or defer jargon until Section 02/08.

9. [03-main-results-status.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/sections/03-main-results-status.tex:42): “two-family verified assembly” is used as if meaningful to a newcomer. Fix: define it or remove the internal audit label from the mathematical chain.

10. [06-day1-belt.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/sections/06-day1-belt.tex:68): “identity realization,” “archetype simplex,” and “transfer to a general frame” are unexplained. Fix: define the realization model and what transfer would mean.

11. [06-day1-belt.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/sections/06-day1-belt.tex:94): “exact nonconstant shell” and “biorthogonality” appear without setup. Fix: either define shell coordinates or cut this item from a self-contained belt.

12. [07-wave-lemmas-dual-witness.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/sections/07-wave-lemmas-dual-witness.tex:147): “Branch A,” “top-band blockers,” and “aggregate pinning” are used before real definitions. Fix: add a local glossary before the reductions.

13. [08-residual-dmf.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/sections/08-residual-dmf.tex:125): “Partial web exclusions” states three mechanisms in slogans only. Fix: give precise hypotheses/conclusions or label as informal evidence.

14. [09-numerics-record.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/sections/09-numerics-record.tex:40): Nickname glossary arrives after `MRP`, `financier`, `budget line`, and `flat floor` were used for several sections. Fix: move this glossary to Section 00 or 03.

15. [09-numerics-record.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/sections/09-numerics-record.tex:83): `M_{\mathrm{far}}` and `T_{\mathrm{far}}` are reported without definitions. Fix: define both numerical observables before the table.

16. [10-refutations-dead-routes.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/sections/10-refutations-dead-routes.tex:28): “Literal psi-gap” refutation cites source-note counterexamples but does not show one. Fix: include the exact rational counterexample or remove “self-contained.”

17. [10-refutations-dead-routes.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/sections/10-refutations-dead-routes.tex:125): Dead-route table lists many unexplained routes: KKT dichotomy, high zero face, raw circuit bounds, log-staircase. Fix: add one-sentence definitions or omit unused history.

18. [11-methodology.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/sections/11-methodology.tex:31): Methodology says notes are provenance and imports are ledger-allowed, which conflicts with four-corners readability. Fix: separate provenance claims from in-report mathematical claims.

19. [99-glossary-notation.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/sections/99-glossary-notation.tex:50): “First shard” labels do not match actual section numbering, e.g. `10-residual-dmf-obstruction`. Fix: replace with actual section/file references.

20. [99-glossary-notation.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/sections/99-glossary-notation.tex:95): Glossary status for “all-shallow witness” is `OPEN` despite exact-rational examples elsewhere. Fix: distinguish existence from height-\(\tau\) exclusion.

21. [99-glossary-notation.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/sections/99-glossary-notation.tex:162): Named-results table introduces labels not defined in the prose: `CEL`, `FTI-2`, ladder analysis, reciprocal-carrier lemma. Fix: either define them or delete them from the final glossary.

22. [05-corner-theorem.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/sections/05-corner-theorem.tex:91): Uses unqualified `\sigma` cells in numerical discussion despite the notation policy. Fix: state whether this is \(\sigoff\), \(\sigtilde\), or a historical sweep parameter.

Overall verdict: the report is not self-contained for the stated target reader. The main high-level chain can be roughly followed after Sections 02, 04, and 08, but only if the reader tolerates many black boxes, campaign labels, late definitions, and provenance claims. The core mathematical objects are mostly defined; the dependency story is not clean enough. My estimate: `P(basic-LA + Markov reader can actually follow the main chain) = 0.35`; `P(they can verify the chain without project lore) = 0.10`.