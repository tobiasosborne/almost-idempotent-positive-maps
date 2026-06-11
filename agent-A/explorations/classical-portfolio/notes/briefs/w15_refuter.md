# w15_refuter: build the first H >> delta thin-chain instance (or kill the templates)

You are a codex (gpt-5.5) REFUTER with numerics. Two previous refuters failed to
build a counterexample to the path-product floor; a fresh autopsy of the delta=0
proof now identifies EXACTLY where positivity is load-bearing — use it to design
cancellation where the proof needs positivity.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w15_refuter.
PROGRESS PROTOCOL: append one short line per stage to
/tmp/codex-sigma-wall/w15_refuter/progress.md.

## READ FIRST
1. agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex — the full
   self-contained statement (definitions, Conjecture 2 = the path-product floor
   Pi_C >= tau - O(L*delta), the constraints ledger: the corner theorem caps,
   the proved branches a counterexample must dodge).
2. notes/swarm-answers/w14_autopsy.md (under agent-A/explorations/classical-portfolio/):
   the sign-rigidity table. The delta=0 proof FAILS for signed P exactly at
   (a) zero-sum closure ("0 = sum of nonnegatives => each term 0" — destroyed by
   cancellation), (b) the zero-pattern symmetry / block partition, (c) positive
   diagonal. A counterexample should make cancellation do the work these steps
   forbid: thin chains whose path products decay while sigma_tilde stays > tau.
3. notes/swarm-answers/w12_chain_refuter.md and w13_chain_refuter2.md — the
   quantified failure maps of your predecessors. DO NOT re-run their dead templates;
   start from where their constructions broke and use the autopsy to pick different
   degrees of freedom.
4. notes/swarm-answers/w12_comp_finisher.md — the proved finisher; your instance
   must evade its hypotheses (e.g. exploit its declared primitivity/periodicity gap,
   or keep every component thin).

## TARGET
An EXPLICIT matrix P (any moderate n) with: P^2 = P EXACTLY (or to machine
precision via an exactly-idempotent construction, e.g. P = V W with W V = I),
entries >= -delta, rows summing to 1, exhibiting a hidden top vertex with
sigma_tilde > tau whose band component C has Pi_C << tau - O(L*delta) — ideally an
instance with H >> delta (the empirical record, 67k+ instances, fits
delta >= ~H/2; break it). Periodic/cyclic carrier structure is an UNEXPLOITED
degree of freedom (the finisher's primitivity gap).

## METHOD
Write and RUN code (python3, numpy) in your workdir. Construct exactly-idempotent
signed P families (spectral projections of perturbed stochastic generators; V W
factorizations; block designs with cyclic thin chains), then VERIFY every claimed
property numerically and print the certificate: delta, H, sigma_tilde of the hidden
vertex, tau, Pi_C, L. Save the construction script + the certificate instance to
your workdir.

## DELIVERABLE (verdict-first)
VERDICT: COUNTEREXAMPLE (give the matrix or its exact construction + the printed
certificate numbers) / NOT-REFUTED (the failure map: each template you tried, the
quantified obstruction that killed it, in display math). Then calibrated
P(the floor is true) updated from your search, and the single most promising
remaining counterexample degree of freedom.
