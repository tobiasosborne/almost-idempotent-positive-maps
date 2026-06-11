# w24_freshread — fresh-agent readability test of OVERVIEW.md: FAILS-then-fixed (codex, 2026-06-11)
# All structural fixes applied (kernel-vs-linear-law split, scale-dependent visibility, O(sqrt-delta) exponent, glossary).

VERDICT: FAILS as self-contained onboarding. It is a strong campaign map, but a fresh agent would likely walk away with the wrong formal conjecture: `H <= C*delta` with strict exposed vertices, while `kernel-conjecture.tex` states a small-`delta`, `sigma_tilde > sqrt(delta)` branch bound `height <= B*sqrt(delta)` using scale-dependent exposedness.

Calibrated `P(wrong first move)`: **0.55**.

**Phase 1 Answers**
a. Central conjecture, from `OVERVIEW.md` alone:
For every real `n x n` matrix `P` with `P^2 = P`, `P1 = 1`, and row negativity
`delta = max_i sum_j max(-P_ij, 0)`, define visible row points `W`, their convex hull `C_W`, and height
`H = max_i dist_1(p_i, C_W)`. The central linear law says there is a universal constant `C`, apparently expected/sharp near `2`, such that `H <= C*delta`. The small-`delta` regime below `delta* = (2 - sqrt(3))^2` is the important one.

b. Already proved / pending / open:
Proved: the `delta=0` Hognas-Mukherjea normal form; the implication chain “linear law -> HLC -> op-exposed-hull -> op-classical”; component finisher and aperiodicity; several robust pieces of the H-M autopsy; tangent-cone, fixed-mass visibility, and mass-removed boundary recoding lemmas. Caveat: the local linear law assembly is claimed but its hostile audit is in flight. Pending: check `w23_loj_audit.md`; bank audited work into registry/af; dimension-free local constants. Open: the full small-`delta` global gap, meaning show small-negative exact idempotents are near the H-M family / prove the W-free target.

c. First 3 things I would do:
1. Read `report/kernel-conjecture.tex`.
2. Check `notes/swarm-answers/w23_loj_audit.md`.
3. If the audit held, attack the global H-M-neighborhood/W-free gap; if it broke, start at the break point.

Five things I must not do:
1. Re-run LP support-cleanup/hiddenness arguments without new input.
2. Use raw atom-level path-product floors.
3. Try scalar chain-local certificates or naive SOS encodings as if unblocked.
4. Record proof claims without a hostile audit by another worker.
5. Use unverified literature leads or large-`delta` examples to overclaim small-`delta` statements.

d. Jargon leakage / clarity debt / missing pointers:
Unresolved terms: `Layer-1`, `op-classical`, `op-exposed-hull`, `HLC`, `Recipe A->B`, `registry/af`, `bd`, “hostile audit”, “pushed witness”, “normal cone”, “LP dual cone”, “KKT”, “SOS modulo the idempotent ideal”, “stratified distance bound”, “Łojasiewicz/error-bound”, “Douglas-Ando”, “contractive projections on l_infty^n”, “boundary normal form”, “TOTAL REMOVED MASS”, “cohomological Newton iteration”.

Sentences I had to read twice: the “visible” definition; “Linear law -> HLC”; “Proved and independently audited ... claimed assembly ... audit IN FLIGHT”; “The one standing gap ... GLOBAL question”; “squared chart-distance ... yields H <= C_loc*delta”.

Missing: exact formal visible definition; exact `HLC`; whether central target is all `delta` or only small `delta`; whether `C=2` is conjectured or empirical; exact neighborhood and constants in the local law; token size of the dossier; where the “dossier FINAL sections” begin.

e. Further reading estimate:
For precise statements: probably `10k-20k` tokens in `kernel-conjecture.tex`. For the full record: unclear from the overview; likely `50k+` for dossier final sections and `100k+` if the 70 worker verdict files are included. The layering is mostly clear: overview -> kernel -> dossier, but “dossier” is not named as a single file in the read-order sentence.

**Phase 2 Mislead List**
1. The overview’s “central target” is not the formal Kernel Conjecture. Formal kernel: there exist universal `delta_0, B` such that for `delta <= delta_0`, `W` is nonempty and every hidden vertex with `sigma_tilde_v > sqrt(delta)` has height `<= B*sqrt(delta)`.

2. The overview says `op-exposed-hull` is `O(delta)` close to the visible hull. Formal theorem gives `O(sqrt(delta))`.

3. The overview’s visible/hidden definition is too classical. Formal visibility is `(\rho,\kappa)`-exposedness with `rho=4sqrt(delta)` and `kappa=sqrt(delta)/4`, and nearby rows are exempt.

4. “Hidden means no functional certifies it” is misleading. Formally, hidden means failure of a scale-dependent margin condition, not failure of strict exposedness.

5. “Only the linear law is open” is too clean. The formal document presents the Kernel Conjecture as the missing input, with some arrows “proved modulo recorded audits.”

6. The overview says the current proof attack is the variety programme. The kernel document still presents the path-product/thin-chain form as the stronger working form, though with cloning corrections and caveats.

**Ranked Edits**
1. Quote: “Every exactly idempotent, row-sum-one matrix with negative budget δ satisfies H ≤ C·δ.”
Replacement: “The strongest desired linear law is `H <= C*delta`, but the formal Kernel Conjecture currently needed by the registry is weaker/different: for small `delta`, hidden vertices with `sigma_tilde > sqrt(delta)` must have height `<= B*sqrt(delta)`.”

2. Quote: “A row vertex is visible ... if some linear functional ... attains its strict maximum exactly at that row’s location.”
Replacement: “For the formal kernel, visibility means `(\rho,\kappa)`-exposedness with `rho=4sqrt(delta)` and `kappa=sqrt(delta)/4`: a row vertex admits an affine separator with margin at least `kappa` from rows at distance at least `rho`.”

3. Quote: “Linear law ⇒ HLC ... ⇒ op-exposed-hull ... every row is O(δ)-close...”
Replacement: “Kernel Conjecture ⇒ `H <= C sqrt(delta)` / HLC ⇒ `op-exposed-hull` with `O(sqrt(delta))` distance ⇒ `op-classical`.”

4. Quote: “Each link in that chain is proved; only the linear law is open.”
Replacement: “The downstream arrows are proved or proved modulo recorded audits; the missing formal input is the Kernel Conjecture, while the sharper `H <= C*delta` law remains a stronger target.”

5. Quote: “Equivalent W-free target.”
Replacement: “Related W-free target. This is the natural structure-theory formulation, but check `kernel-conjecture.tex` before treating it as formally equivalent to the current Kernel Conjecture.”