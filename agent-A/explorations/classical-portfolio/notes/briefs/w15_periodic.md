# w15_periodic: close the w12 component finisher's primitivity gap

You are a codex (gpt-5.5) PROVER on a bounded patch task. The proved per-component
finisher (wave 12) collapses FAT (primitive, aperiodic) positive components; it
declared a gap for PERIODIC components. Refuter #2's dichotomy suggests the gap is
benign. Prove it (or exhibit the periodic obstruction).
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w15_periodic.
PROGRESS PROTOCOL: append one short line per stage to
/tmp/codex-sigma-wall/w15_periodic/progress.md.

## READ FIRST
1. agent-A/explorations/classical-portfolio/notes/swarm-answers/w12_comp_finisher.md
   — the proved finisher: statement, hypotheses (find where primitivity/aperiodicity
   enters: the Birkhoff-Hilbert projective contraction needs a positive power), the
   declared gap.
2. notes/swarm-answers/w12_chain_refuter.md (same dir) — refuter #2's dichotomy
   (periodic components either … or …; locate it and use it).
3. notes/swarm-answers/t10 material if referenced by w12 (the Birkhoff projective
   idempotent-collapse lemma — bounded projective diameter + eps-idempotence =>
   row collapse, NO spectral gap needed).
4. report/kernel-conjecture.tex (same exploration dir) — definitions + how the
   finisher feeds Conjecture 2, so your patch composes with the chain.

## TASK
Extend the finisher to period-d components. Standard route to try first: a
period-d positive component has a cyclic block structure; P^d restricted to each
cyclic class is primitive — but here P^2 = P EXACTLY (idempotence is free), so
P^d = P for all d >= 1: check whether exact idempotence makes nontrivial
periodicity IMPOSSIBLE for the carrier of an idempotent (a cyclic class structure
with period d >= 2 forces P = P^d to mix classes — derive the contradiction, or
exhibit why the signed carrier evades it). If periodicity is excluded: the gap is
vacuous — prove THAT cleanly. If not excluded: run the d-power argument with the
projective-diameter bookkeeping and derive the modulus (explicit constants,
dimension-free; account for signed error accumulation over d steps, d <= component
size — is the constant still dimension-free?).
You may run small numerical checks (python3/numpy) in your workdir.

## DELIVERABLE (verdict-first)
VERDICT: GAP CLOSED (the proof, display math, explicit constants — state the
patched finisher in full) / GAP REAL (the periodic obstruction instance or the
precise inequality that fails, display math). Then calibrated
P(patch survives hostile audit).
