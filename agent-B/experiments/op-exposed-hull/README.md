# op-exposed-hull experiments

Sandbox for Agent B numerical exploration of the classical global exposed-hull
problem.

Rules:

- keep scripts reproducible and record command lines;
- write machine-readable outputs (`json`, `csv`) next to scripts;
- record solver versions when using LP/MILP/CAS tools;
- numerical results are evidence only, never proof;
- do not write outside `agent-B/experiments/op-exposed-hull/` unless explicitly
  updating an Agent B note.

Initial experiment targets:

1. compute exposedness moduli for finite row polytopes by LP;
2. optimize signed affine retractions with bounded negative mass;
3. search for rows far from `conv W_{rho,kappa}`;
4. test Hume products, rank-one families, regular-polygon constraints, and
   random low-rank idempotents.
