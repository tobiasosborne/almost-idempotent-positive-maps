export const meta = {
  name: 'lcequiv-proof-kit',
  description: 'Scope lem-classical-equiv + groundability gate: node plan, externals byte-matched to present refs, G/A/R verdict (decides whether the af build can proceed without acquiring sources)',
  phases: [
    { title: 'Scope', detail: 'outline both directions; list foundational facts + constants' },
    { title: 'Ground', detail: 'one probe per foundational fact: byte-extract a verbatim string from PRESENT refs, or flag as un-acquired' },
    { title: 'Synthesize', detail: 'proof kit: node plan <=12/depth<=3, externals table, G/A/R verdict' },
  ],
}

// ---- shared context every agent needs ----
const CTX = `
PROJECT: a Jordan generalization of Kitaev's almost-idempotent-positive-maps theorem.
TARGET LEMMA (registry contract, VERBATIM — this is the af root, do not alter it):
"The signed-idempotent and stochastic-idempotent formulations of classical stability are equivalent up to universal constants: Q row-stochastic with ||Q^2-Q|| <= eta gives P=theta(2Q-1) signed affine retraction with ||P-Q|| <= C eta and neg mass delta <= C eta, and conversely row-normalising p_i^+ gives Q with ||P-Q|| <= 2 delta, ||Q^2-Q|| <= 6 delta+4 delta^2."

So there are TWO directions to prove, each with EXPLICIT universal constants:
  FORWARD  (stochastic -> signed): Q row-stochastic, ||Q^2-Q||<=eta  ==>  P=theta(2Q-1) is a signed affine
           retraction (P^2=P, P1=1) with ||P-Q|| <= C eta and negative mass delta <= C eta.
           (theta = the sign/step function; P = spectral projection via holomorphic functional calculus of 2Q-I.)
  CONVERSE (signed -> stochastic): P signed affine retraction with negative mass delta  ==>  row-normalising the
           positive parts p_i^+ yields row-stochastic Q with ||P-Q|| <= 2 delta and ||Q^2-Q|| <= 6 delta + 4 delta^2.

FILES TO READ (ground truth and prior art):
  - argument/lemmas/lem-classical-equiv.md          (the registry shard; contract + provenance)
  - definitions/def-stochastic.md                   (THE definition; references def-exposed, def-near-positive-projection)
  - agent-B/notes/subagent-classical-sqrt-stability-proof.md   (PRIOR-ART OUTLINE — has the converse derivation
        ||Q^2-Q||<=6delta+4delta^2 explicitly, and the forward "standard spectral separation estimate" hand-wave)
  - agent-B/notes/classical-affine-face-lemmas.md   (Lemma 3, prior art)
  - report prose: grep report/ for the label "lem:classical-equiv" (find the .tex file, read its statement/proof)

THE NORM throughout is the operator norm ell^infty_n -> ell^infty_n, i.e. ||A|| = max_i sum_j |A_ij| (max row ell^1).

HARD RULES (this repo's single guarded failure is a confident-plausible-WRONG claim):
  - GROUND TRUTH = a byte-VERBATIM string in a LOCAL refs/ source. NEVER paraphrase a fact from memory and call it
    grounded. If a fact is not byte-extractable from a PRESENT refs payload, say so honestly.
  - The theory notes (agent-B/notes/...) are OUTLINE / PRIOR ART ONLY — NOT ground truth. Any step a note hand-waves
    (e.g. "by the standard spectral separation estimate") is a HIGH-RISK foundational fact that MUST be grounded.
  - PRESENT refs payloads (content available to grep/Read right now):
      refs/kitaev-2405.02434/  (8 files; esp. approximate_algebras.tex ~ lines 638-642 has the operator-norm setup)
      refs/hos/  refs/idel-2013/  refs/effros-stormer-1979/  refs/vlw-2604.08380/
      refs/blecher-read-2019/  refs/baak-moslehian/
    Do NOT trust kaup-1984 or chu-russo (SUSPECT, and not present anyway). The present 7 are GENUINE.
`;

const SCOPE_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['direction', 'outline', 'constants', 'foundational_facts', 'hypotheses'],
  properties: {
    direction: { type: 'string' },
    outline: { type: 'array', items: { type: 'string' }, description: 'ordered proof steps for this direction' },
    constants: {
      type: 'array',
      items: {
        type: 'object', additionalProperties: false, required: ['symbol', 'value', 'role'],
        properties: { symbol: { type: 'string' }, value: { type: 'string' }, role: { type: 'string' } },
      },
    },
    foundational_facts: {
      type: 'array',
      description: 'every external fact the proof rests on (not derived within the proof)',
      items: {
        type: 'object', additionalProperties: false,
        required: ['key', 'statement', 'why_needed', 'kind', 'candidate_source'],
        properties: {
          key: { type: 'string', description: 'canonical slug; prefer: op-norm-def, op-norm-submult, op-norm-triangle, func-calc-spectral-bound, spectral-mapping, neg-mass-bound, stochastic-props, small-eta-hyp' },
          statement: { type: 'string' },
          why_needed: { type: 'string' },
          kind: { type: 'string', description: "'external' = must be byte-quoted from refs; 'node' = derivable inside the proof from more basic facts; 'hypothesis' = a stated assumption of the lemma" },
          candidate_source: { type: 'string', description: 'best guess at which PRESENT refs payload (or none) states it' },
        },
      },
    },
    hypotheses: { type: 'array', items: { type: 'string' }, description: 'e.g. eta < 1/4, delta <= 1' },
  },
};

const GROUND_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['fact_key', 'statement', 'grounded', 'source_id', 'locus', 'verbatim_string', 'note'],
  properties: {
    fact_key: { type: 'string' },
    statement: { type: 'string' },
    grounded: { type: 'boolean', description: 'true ONLY if a byte-verbatim string in a PRESENT refs payload states this fact' },
    source_id: { type: 'string', description: 'refs payload dir name, e.g. kitaev-2405.02434 / hos; "" if none' },
    locus: { type: 'string', description: 'relative path:line(s), e.g. refs/kitaev-2405.02434/approximate_algebras.tex:640; "" if none' },
    verbatim_string: { type: 'string', description: 'the EXACT bytes copied from the file (no paraphrase, no normalization); "" if none found' },
    note: { type: 'string', description: "if not grounded: either a derivation path from MORE-BASIC present facts (=> build as a proof node), OR the precise un-acquired source that would be needed (=> R / STOP-and-acquire)" },
  },
};

const KIT_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['groundability_verdict', 'verdict_rationale', 'externals', 'derived_nodes', 'ungrounded_gaps', 'node_plan', 'node_count', 'max_depth', 'needs_factoring', 'recommendation'],
  properties: {
    groundability_verdict: { type: 'string', enum: ['G', 'A', 'R'], description: 'G=fully groundable in present refs; A=acceptable (gaps are derivable as nodes from present facts); R=refused (needs un-acquired sources => STOP)' },
    verdict_rationale: { type: 'string' },
    externals: {
      type: 'array', description: 'facts grounded byte-verbatim in present refs (these become af externals)',
      items: { type: 'object', additionalProperties: false, required: ['key', 'statement', 'source_id', 'locus', 'verbatim_string'],
        properties: { key: { type: 'string' }, statement: { type: 'string' }, source_id: { type: 'string' }, locus: { type: 'string' }, verbatim_string: { type: 'string' } } },
    },
    derived_nodes: {
      type: 'array', description: 'facts NOT quoted but proven inside the workspace as nodes (from more basic externals)',
      items: { type: 'object', additionalProperties: false, required: ['key', 'statement', 'derived_from'],
        properties: { key: { type: 'string' }, statement: { type: 'string' }, derived_from: { type: 'string' } } },
    },
    ungrounded_gaps: {
      type: 'array', description: 'R-triggers: facts neither quotable from present refs nor derivable from present facts',
      items: { type: 'object', additionalProperties: false, required: ['key', 'statement', 'needed_source', 'severity'],
        properties: { key: { type: 'string' }, statement: { type: 'string' }, needed_source: { type: 'string' }, severity: { type: 'string' } } },
    },
    node_plan: {
      type: 'array', description: 'the af proof tree: <=12 nodes, depth <=3 (brittleness limit)',
      items: { type: 'object', additionalProperties: false, required: ['node_id', 'statement', 'depends_on'],
        properties: { node_id: { type: 'string' }, statement: { type: 'string' }, depends_on: { type: 'array', items: { type: 'string' } } } },
    },
    node_count: { type: 'number' },
    max_depth: { type: 'number' },
    needs_factoring: { type: 'boolean', description: 'true if the tree would exceed 12 nodes / depth 3 and should be split into a sub-lemma' },
    recommendation: { type: 'string', description: 'concrete next action for the orchestrator' },
  },
};

// ===================== PHASE 1: SCOPE (both directions, parallel) =====================
phase('Scope');
const directions = [
  {
    key: 'forward',
    desc: `FORWARD direction (stochastic -> signed): Q row-stochastic with ||Q^2-Q||<=eta  ==>  P=theta(2Q-1) is a
signed affine retraction (P^2=P exactly, P1=1) with ||P-Q|| <= C eta and negative mass delta <= C eta.
This is the RISKY direction: P=theta(2Q-1) is built by HOLOMORPHIC FUNCTIONAL CALCULUS (theta=sign/step fn) of
the matrix 2Q-I, and the bound ||P-Q||<=C eta comes from a SPECTRAL-SEPARATION / functional-calculus perturbation
estimate (the note calls it "the standard spectral separation estimate" for eta<1/4 — that is a hand-wave you must
expose). Pin down EXACTLY which spectral / functional-calculus fact is needed and at what generality.`,
  },
  {
    key: 'converse',
    desc: `CONVERSE direction (signed -> stochastic): P a signed affine retraction with negative mass delta
==> row-normalising the positive parts (q_i = mu_i^+/(1+a_i), a_i=neg(mu_i)<=delta) yields row-stochastic Q with
||P-Q|| <= 2 delta and ||Q^2-Q|| <= 6 delta + 4 delta^2. The note derives this explicitly via
Q^2-Q = (Q-P)Q + P(Q-P) - (Q-P) with ||P||<=1+2delta, ||Q||=1. List every operator-norm fact (max-row-ell^1
identity, submultiplicativity, triangle) this rests on.`,
  },
];

const scopes = (await parallel(directions.map((d) => () =>
  agent(
    `${CTX}\n\nYou are scoping ONE direction of the equivalence.\n${d.desc}\n\n` +
    `Read the files above. Produce an ordered proof OUTLINE for THIS direction, the EXPLICIT constants it produces, ` +
    `the lemma HYPOTHESES it uses, and — most important — an exhaustive list of FOUNDATIONAL FACTS (every fact the ` +
    `proof rests on that is NOT derived within it). For each foundational fact classify kind = external | node | ` +
    `hypothesis, and guess the candidate PRESENT refs source. Be ruthless about exposing hand-waves (especially the ` +
    `"spectral separation estimate"): name the precise theorem/inequality and its hypotheses. Do NOT treat the ` +
    `theory notes as ground truth.`,
    { schema: SCOPE_SCHEMA, label: `scope:${d.key}`, phase: 'Scope' }
  )
))).filter(Boolean);

if (scopes.length === 0) {
  log('FATAL: both scope agents failed; aborting.');
  return { error: 'scope failed' };
}

// dedupe foundational facts by key across both directions (barrier justified: need ALL facts before grounding)
const factByKey = new Map();
for (const s of scopes) {
  for (const f of (s.foundational_facts || [])) {
    const k = (f.key || f.statement || '').trim();
    if (!k) continue;
    if (!factByKey.has(k)) factByKey.set(k, { ...f, directions: [s.direction] });
    else factByKey.get(k).directions.push(s.direction);
  }
}
const facts = [...factByKey.values()];
log(`Scoped ${scopes.length} direction(s); ${facts.length} distinct foundational facts to ground.`);

// ===================== PHASE 2: GROUND (one probe per fact, parallel read-only) =====================
phase('Ground');
const grounded = (await parallel(facts.map((f) => () =>
  agent(
    `${CTX}\n\nYou are a GROUNDING PROBE for ONE foundational fact. Your job: determine whether this fact is stated ` +
    `byte-VERBATIM in a PRESENT refs payload, and if so copy the EXACT bytes.\n\n` +
    `FACT key="${f.key}": ${f.statement}\n` +
    `WHY THE PROOF NEEDS IT: ${f.why_needed}\n` +
    `SCOPE's classification: kind=${f.kind}, candidate_source=${f.candidate_source}\n\n` +
    `Procedure: grep -rn the PRESENT refs payloads (refs/kitaev-2405.02434, refs/hos, refs/idel-2013, ` +
    `refs/effros-stormer-1979, refs/vlw-2604.08380, refs/blecher-read-2019, refs/baak-moslehian) for terms related ` +
    `to this fact; when you find a candidate, Read the exact line(s) and COPY THE BYTES VERBATIM into verbatim_string ` +
    `(no paraphrase, no re-typing from memory). Set grounded=true ONLY if the bytes genuinely state the fact.\n` +
    `If NOT found verbatim: set grounded=false and in 'note' give EITHER (a) a concrete derivation path from ` +
    `more-basic facts that ARE present (=> this becomes a proof NODE, acceptable), OR (b) the precise un-acquired ` +
    `source that would be needed (=> a STOP/acquire trigger). Be honest — a confident wrong "grounded" is the worst outcome.`,
    { schema: GROUND_SCHEMA, label: `ground:${f.key}`, phase: 'Ground' }
  )
))).filter(Boolean);

log(`Grounding done: ${grounded.filter((g) => g.grounded).length}/${grounded.length} facts byte-grounded in present refs.`);

// ===================== PHASE 3: SYNTHESIZE (proof kit + G/A/R verdict) =====================
phase('Synthesize');
const kit = await agent(
  `${CTX}\n\nYou are the SYNTHESIZER. Below are the per-direction scopes and the per-fact grounding results. ` +
  `Build the final PROOF KIT for the af workspace and render an honest groundability verdict.\n\n` +
  `SCOPES:\n${JSON.stringify(scopes, null, 2)}\n\n` +
  `GROUNDING RESULTS:\n${JSON.stringify(grounded, null, 2)}\n\n` +
  `Produce KIT_SCHEMA:\n` +
  `- externals: the facts grounded byte-verbatim in present refs (copy source_id/locus/verbatim_string through ` +
  `UNCHANGED — do not edit the bytes). For the single highest-risk external (the functional-calculus / spectral ` +
  `separation bound), if it is claimed grounded, RE-CONFIRM by your own reasoning that the quoted bytes truly state ` +
  `the needed inequality at the needed generality; if they don't, move it to ungrounded_gaps.\n` +
  `- derived_nodes: facts you will PROVE inside the workspace (not quoted) from the externals.\n` +
  `- ungrounded_gaps: anything neither quotable nor derivable from present facts (these force verdict R).\n` +
  `- node_plan: the af proof tree, <=12 nodes and depth <=3 (brittleness limit). Cover BOTH directions. If it cannot ` +
  `fit in 12 nodes/depth 3, set needs_factoring=true and propose the sub-lemma split.\n` +
  `- groundability_verdict: G (fully groundable now), A (gaps all derivable as nodes from present facts — build can ` +
  `proceed), or R (a load-bearing fact needs an un-acquired source — STOP and tell the orchestrator exactly what to acquire).\n` +
  `- recommendation: the concrete next action.\n` +
  `Be conservative: when the spectral-separation bound is only a hand-wave with no present byte-source AND no clean ` +
  `derivation from present facts, the honest verdict is R, not optimism.`,
  { schema: KIT_SCHEMA, label: 'synthesize:proof-kit', phase: 'Synthesize' }
);

return { scopes, grounded, kit };
