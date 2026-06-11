# w32_excess: the signed-face excess — the deepest residual, now finite-dimensional

You are a codex (gpt-5.5) PROVER. Five reduction waves have chased the
classical campaign's global route into one single-row, finite-dimensional
coefficient inequality. Prove it by exploiting its finiteness, or exhibit the
conspiring configuration.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w32_excess.
PROGRESS PROTOCOL: short line per stage to progress.md.
ARTIFACT RULE: long-form proof to proof.md, NEVER answer.md.

## THE TARGET (the signed-face excess)
P exactly idempotent, P1 = 1, row negative mass <= delta <= delta_0;
u_1..u_m the max-volume actual-row basis (rows p_j = sum_t a_t(j) p_{u_t},
|a_t(j)| <= 1, sum_t a_t(j) = 1 — the audited L2 chart). Prove for each s:
  sum_j (P_{u_s j})_+ * E_s(j) <= C_sf * delta,
  E_s(j) := ( sum_{t != s} (-a_t(j))_+ - (1 - a_s(j)) )_+ .
Note E_s(j) > 0 iff the foreign coefficients of j are NET-NEGATIVE
(each negative a_t contributes 2|a_t| to the excess net of the deficit);
E_s vanishes on convex coefficient vectors. At delta = 0, E_s = 0 identically
(H-M coefficients are convex).

## READ (the reduction chain + every exact identity available)
1. notes/swarm-answers/w31_tax.md + experiments/out/w31_tax/proof.md (under
   agent-A/explorations/classical-portfolio/) — the split that isolated the
   excess (the deficit part <= 2*delta is PROVED there) + its numerics
   (tax_audit.py: WHERE the excess lives — transverse pairs; lp_rank_stress).
2. notes/swarm-answers/w30_telescope.md + w30_maxvol.md — the coefficient
   identity a*P^+ = P_{u.} + a*P^- + b*P^+ - b*P^- and the Cramer facts.
3. EXACT identities at your disposal (all derived in the chain; re-verify):
   (i) componentwise coefficient idempotence: sum_j P_{u_s j} a_t(j) =
   delta_{ts} EXACTLY; (ii) sum_t a_t(j) = 1 exactly; (iii) |a_t(j)| <= 1
   (max-volume); (iv) row negative masses nu_j <= delta; (v) in-class
   concentration (w27: class rows are eta-close to representatives);
   (vi) cross-cluster leakage <= 2delta/(1-eta) (w27); (vii) the coefficient
   vectors a(j) THEMSELVES form an exactly idempotent system: derive the
   k x k (or m x m) algebra satisfied by the matrix A = (a_t(j)) restricted
   to representative rows and use it — the problem may close entirely at the
   coefficient-matrix level, where it is an inequality about an exactly
   idempotent m x m-ish system with near-positivity inherited how? (work out
   exactly what A inherits: A's rows at representatives are e_s; P restricted
   to coefficient space is conjugate to a smaller idempotent — make this
   precise; the excess may then be an instance of the SAME problem at rank m
   with bounded coefficients — if literally self-similar, SAY SO: a
   self-similarity/induction on rank could close it OR reveal the
   irreducibility).
4. LP/EXTREMAL ATTACK (the finiteness leverage — do this seriously): for
   fixed small m (2, 3, 4): treat (P_{u_s j})_+ weights and coefficient
   vectors a(j) as LP variables subject to the EXACT constraints (i)-(iv)
   (drop the geometry — relaxation); maximize the excess. If the LP max is
   O(delta) with a dimension-free constant: extract the dual certificate,
   rationalize, and convert to a proof (the constraints are all linear given
   the supports — handle the (.)_+ by case-splitting on sign patterns;
   enumerate sign patterns for small m). If the LP max is LARGER than
   O(delta): the relaxation is too loose — identify which dropped constraint
   (geometry/idempotence-of-the-full-system) cuts the violating
   configuration, add its linearization, repeat. This loop either yields a
   certificate + proof, or a candidate conspiring configuration to attempt
   realizing as an actual idempotent (the campaign's instance machinery:
   experiments/out/w16_nlopt, w17_antecedent generators).
5. NUMERICS conventions: experiments/out/w31_tax/tax_audit.py.

## DELIVERABLE (verdict-first; long form to proof.md)
VERDICT: EXCESS PROVED (display math, explicit C_sf, honest dependence; the
chain's conditional corollaries restated in one paragraph) / LP-CERTIFICATE
AT SMALL m (+ the induction/general-m gap stated precisely) / DIED-AT (the
exact configuration the LP loop could not cut + whether it is realizable) /
COUNTEREXAMPLE (verified). Calibrated P(survives audit). Save code + outputs.
