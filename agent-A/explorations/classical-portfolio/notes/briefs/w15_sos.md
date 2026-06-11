# w15_sos: SOS/certificate search SPECIALIZED to the reduced thin-chain inequality

You are a codex (gpt-5.5) certificate-search worker. The campaign's last unwalked
computational route: a sum-of-squares / LP-dual certificate search for the REDUCED
thin-chain inequality at small n — explicitly DISTINCT from wave-10's full-problem
SOS (which collapsed into the exposedness-LP basin; do not repeat it).
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w15_sos.
PROGRESS PROTOCOL: append one short line per stage to
/tmp/codex-sigma-wall/w15_sos/progress.md.

## READ FIRST
1. agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex — full
   self-contained statement; Conjecture 2 (path-product floor) is the target.
2. notes/swarm-answers/w13_chain_excl.md (under
   agent-A/explorations/classical-portfolio/) — the previous prover's reduction:
   extract the REDUCED inequality on a single thin chain (the polynomial system in
   the chain's edge weights + the hidden vertex's budget) and its died-at point.
3. notes/swarm-answers/w12_chain_refuter.md, w13_chain_refuter2.md — feasible-region
   data from the refuters (their near-miss instances seed your numerics).
4. notes/swarm-answers/w14_autopsy.md — the new H-M frame; the exact-row-reproduction
   identity p_i = sum_j P_ij p_j (P^2 = P is EXACT; only signs are perturbed) is a
   valid polynomial constraint you may add to the system.

## TASK
1. FORMALIZE the reduced thin-chain inequality as a polynomial feasibility/
   optimization problem in few variables: chain length L (treat L = 2,3,4,5
   separately), edge weights, negative-mass budget delta, sigma_tilde, tau. State it
   exactly (display math) before computing.
2. SEARCH for a certificate at small L:
   - LP duality on the linearized system (scipy.optimize.linprog is available;
     numpy available; NO network — use only installed packages, hand-roll anything
     missing, e.g. a small interior-point SDP or rational LP via fractions).
   - SOS: parametrize low-degree multipliers, reduce to LP/least-squares on
     coefficients; try degree 2 then 4.
   - If a certificate appears numerically: ROUND to rational and VERIFY exactly
     (fractions module), then print the exact certificate.
3. If infeasible from the certificate side: extract what the dual/SOS failure says
   geometrically (which constraint is slack — a candidate counterexample direction;
   cross-check it against the refuters' failure maps).

## DELIVERABLE (verdict-first)
VERDICT per L in {2,3,4,5}: CERTIFICATE FOUND (the exact rational certificate +
the inequality it proves, display math) / NO CERTIFICATE AT THIS DEGREE (the dual
witness + its geometric reading) / FORMALIZATION BLOCKED (exactly what is ambiguous
in the reduction — quote the w13 locus). Then: does any found certificate extend to
general L by induction (sketch)? Calibrated P(certificate route closes the kernel).
Save all scripts + outputs in your workdir.
