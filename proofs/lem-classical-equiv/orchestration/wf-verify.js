export const meta = {
  name: 'lcequiv-verify',
  description: 'Adversarial per-node verification of proofs/lem-classical-equiv: one FRESH verifier per node, SEQUENTIAL (af is not concurrency-safe), leaves->root. Each re-greps refs, checks deps/constants, then af accept (--confirm) or af challenge.',
  phases: [{ title: 'Verify', detail: 'fresh verifier per node, leaves->root, sequential' }],
};

const WS = 'proofs/lem-classical-equiv';

const COMMON = `
You are an INDEPENDENT ADVERSARIAL VERIFIER for ONE node of the af workspace ${WS} (af v0.1.3), in repo
/home/tobiasosborne/Projects/almost-idempotent-positive-maps. You did NOT build this proof. Your job is to ATTACK
the node and accept it ONLY if it genuinely closes with dimension-free rigor. Reviewer != author is sacred.

LEMMA (the af root, registry contract): "The signed-idempotent and stochastic-idempotent formulations of classical
stability are equivalent up to universal constants: Q row-stochastic with ||Q^2-Q|| <= eta gives P=theta(2Q-1)
signed affine retraction with ||P-Q|| <= C eta and neg mass delta <= C eta, and conversely row-normalising p_i^+
gives Q with ||P-Q|| <= 2 delta, ||Q^2-Q|| <= 6 delta+4 delta^2." Arena is M_n(R) with operator norm
||A||=max_i sum_j|A_ij| (max row ell^1). Built DIRECTLY from Kitaev's general Banach-algebra calculus at M_n(R)
(NOT importing lem-P-properties — different arena B(H)_sa).

PROCEDURE (do ALL of it, for YOUR node only):
1. Read the node and its dependencies: 'af show <node> -d ${WS}' (or 'af status -d ${WS}'). Read the FULL statement
   of YOUR node AND of each dependency node it cites (you may trust a dep's CONCLUSION only — re-derive nothing of
   the dep, but CONFIRM the dep's hypotheses are actually met by this node's setup).
2. Re-ground every refs external the node cites: open the cited file at the locus and CONFIRM the quoted bytes
   byte-match (FULL quote; asterisk/whitespace-only mismatch is OK). The cited Kitaev externals live at
   refs/kitaev-2405.02434/approximate_algebras.tex. List what you re-checked.
3. ATTACK the math: try to find a gap, an unjustified step, an n-DEPENDENT constant masquerading as universal, a
   hypothesis used out of scope, or a wrong algebraic identity. DEMAND that every constant is dimension-free in n
   (the matrix size). If you think you have a counterexample, REPRODUCE it (algebra or a tiny numeric) BEFORE
   acting — a verifier can produce a confident WRONG refutation (LEARNINGS R7); do not challenge on an unverified hunch.
4. DECIDE and ACT on af (capture exact command + output):
   - If it genuinely closes: 'af claim <node> --owner <VID> --role verifier -d ${WS}' then
     'af accept <node> --agent <VID> --confirm -d ${WS}' then 'af release <node> --owner <VID> -d ${WS}'.
     (accept WITHOUT a prior challenge requires --confirm.)
   - If there is a real gap: 'af claim <node> --owner <VID> --role verifier -d ${WS}' then
     'af challenge <node> --owner <VID> --target <statement|inference|context|dependencies|scope|gap>
       --reason "<concrete, specific>" -d ${WS}' then 'af release <node> --owner <VID> -d ${WS}'.
   - If 'af claim' fails citing a stale lock, run 'af reap -d ${WS}' once then re-claim.
   - af accept may refuse if a dependency is not yet validated; if so, still report your LOGICAL verdict and note
     "blocked on dep <X>".
Do NOT touch any other node, the registry shard, the report, or git. Do NOT run af accept --all.
`;

const VERDICT_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['node', 'verdict', 'refs_rechecked', 'deps_hypotheses_satisfied', 'dimension_free_confirmed', 'weak_spot_assessment', 'issues_found', 'af_command', 'af_result', 'reasoning'],
  properties: {
    node: { type: 'string' },
    verdict: { type: 'string', enum: ['accept', 'challenge', 'blocked'] },
    refs_rechecked: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['external', 'locus', 'byte_match'], properties: { external: { type: 'string' }, locus: { type: 'string' }, byte_match: { type: 'boolean' } } } },
    deps_hypotheses_satisfied: { type: 'boolean' },
    dimension_free_confirmed: { type: 'boolean', description: 'every constant in/under this node is dimension-free in n' },
    weak_spot_assessment: { type: 'string', description: 'your finding on this node-specific focus point' },
    issues_found: { type: 'array', items: { type: 'string' } },
    af_command: { type: 'string', description: 'the exact af accept/challenge command you ran' },
    af_result: { type: 'string', description: 'the af tool output / resulting node state' },
    reasoning: { type: 'string' },
  },
};

// leaves -> root order; per-node adversarial focus (from the prover's hand-off + the kit's honest flags)
const NODES = [
  { id: '1.1', vid: 'verifier-n1', focus: 'EXTRACTION-LEVEL FLAG: the max-row-ell^1 closed form ||A||=max_i sum_j|A_ij| is NOT byte-stated in any present ref. Verify the INLINE derivation from the generic sup-definition (|(Ax)_i|<=sum_j|A_ij| for ||x||_inf<=1, equality at x_j=sign(A_ij)) is correct, AND that the node HONESTLY flags it extraction-level (does not pretend it is cited). Confirm GT-operator-norm-banach (kitaev:638-642) really only states the generic "bounded operators form a Banach algebra", not the closed form. Confirm exact submultiplicativity (no 1+eps slack) and ||I||=1.' },
  { id: '1.2', vid: 'verifier-n2', focus: 'Elementary spectral defect. Verify S1=1, ||S||<=3, and the IDENTITY S^2-I=4(Q^2-Q) exactly, so ||S^2-I||=4eta<=4eta_0<1. Confirm GT-small-eta-threshold genuinely grounds the eta<1/4 threshold (kitaev:525,532,2176). Check the dep on 1.1 (norm facts) is used correctly.' },
  { id: '1.3', vid: 'verifier-n3', focus: 'HONEST FLAG 1 (explicit constant). The big one. Verify: |a_n|=|C(-1/2,n)|=C(2n,n)/4^n and the sign pattern (|a_n|=(-1)^n C(-1/2,n)); sum|a_n|t^n=(1-t)^{-1/2}; R1=1 (the (S^2-I)1=0 vanishing); the bound ||R-I||<=C_1(eta_0)||S^2-I|| with C_1(eta_0)=sum_{n>=1}|a_n|(4eta_0)^{n-1} FINITE and EXPLICIT (geometric-type tail, 4eta_0<1) and DIMENSION-FREE IN n. Re-grep GT-funcalc-taylor-bound FULL quote (kitaev:503-516): confirm the convergence statement and the sum-bound ||f(X)-f(x0 I)||<=sum|a_n|||X-x0 I||^n are actually in those bytes.' },
  { id: '1.4', vid: 'verifier-n4', focus: 'HONEST FLAG 2 (multiplicativity TENSION) — scrutinize HARDEST. The node DERIVES R^2=(S^2)^{-1} (hence sgn(S)^2=I) via a Cauchy product, NOT by citing Kitaev. (a) BYTE-CHECK the contested claim: does refs/kitaev:503-532 and/or :642 actually state "f(X)g(X)=(fg)(X)" (the wording the sibling lem-P-properties external GT-funcalc asserts)? Report what the bytes literally say. (b) Independently verify the Cauchy-product derivation: absolute convergence of R=sum a_m Y^m in op-norm (sum|a_m|||Y||^m<inf), submultiplicativity for ||Y^{m+k}||, commuting powers of Y=S^2-I, and that the product coefficients give f^2=(1+y)^{-1}=sum(-1)^N y^N so R^2=(I+Y)^{-1}=(S^2)^{-1}. Confirm S,R commute. This node is the linchpin of the forward direction.' },
  { id: '1.5', vid: 'verifier-n5', focus: 'Idempotence + unit. Verify P^2=P via (1/4)(I+sgn S)^2 expansion using sgn(S)^2=I (dep 1.4), and P1=1 via R1=1 (1.3) and S1=1 (1.2). Re-grep GT-kitaev-spectral-propP FULL quote (kitaev:514-533): confirm Prop_P (||P^2-P||<=delta<1/4 => theta(2P-I) exactly idempotent) is in those bytes and that instantiating it at Q (delta->eta) is legitimate. Confirm the self-contained re-derivation does not secretly need anything unproven.' },
  { id: '1.6', vid: 'verifier-n6', focus: 'HONEST FLAG 1 again (explicit C). Verify P-Q=(1/2)S(R-I) exactly, and ||P-Q||<=(1/2)||S||||R-I||<=(1/2)(3)(4C_1 eta)=6C_1(eta_0)eta, so C:=6C_1(eta_0). Confirm C is DIMENSION-FREE in n and depends only on eta_0<1/4. Deps 1.3 (||R-I|| bound) and 1.5 used correctly.' },
  { id: '1.7', vid: 'verifier-n7', focus: 'Negative mass closes FORWARD. Verify the entrywise bound max(-P_ij,0)<=|P_ij-Q_ij| using Q_ij>=0 (def-stochastic), summing to neg(p_i)<=||p_i-q_i||_1, hence delta<=||P-Q||<=C eta (dep 1.6, same universal C). Confirm Q>=0 is a genuine hypothesis (GT-hyp/def-stochastic), not smuggled.' },
  { id: '1.8', vid: 'verifier-n8', focus: 'CONVERSE construction + distances. Verify the disjoint-support split p_i=p_i^+ - p_i^-, the ell^1 additivity on disjoint supports, a_i=||p_i^-||_1=neg(p_i)<=delta, ||p_i^+||_1=1+a_i, q_i=p_i^+/(1+a_i) is a probability vector, ||p_i-q_i||_1=2a_i so ||P-Q||<=2delta, and the LOAD-BEARING point ||P||<=1+2delta REQUIRES the +/- split (P1=1 alone does NOT bound ||P||). Check def-stochastic is applied correctly.' },
  { id: '1.9', vid: 'verifier-n9', focus: 'CONVERSE exact ring identity. Verify Q^2-Q=(Q-P)Q+P(Q-P)-(Q-P)=PD+DP+D^2-D (D=Q-P) is an EXACT identity in M_n(R), valid ONLY because P^2=P holds EXACTLY (a genuine hypothesis). Expand both forms and confirm they agree. No approximation allowed here.' },
  { id: '1.10', vid: 'verifier-n10', focus: 'CONVERSE defect closes CONVERSE. Verify the norm bound ||Q^2-Q||<=||Q-P||||Q||+||P||||Q-P||+||Q-P|| (triangle+submult, dep 1.1), substitute ||Q-P||<=2delta, ||Q||=1, ||P||<=1+2delta (dep 1.8), and confirm the arithmetic 2delta*1+(1+2delta)*2delta+2delta = 6delta+4delta^2 EXACTLY.' },
  { id: '1', vid: 'verifier-root', focus: 'ROOT assembly. Verify the contract is EXACTLY proved: FORWARD conclusion (dep 1.7: P=theta(2Q-1) signed affine retraction, ||P-Q||<=C eta, delta<=C eta) + CONVERSE conclusion (dep 1.10: ||P-Q||<=2delta, ||Q^2-Q||<=6delta+4delta^2) together establish the equivalence "up to universal constants". Confirm BOTH hypotheses (forward: eta<=eta_0<1/4; converse: P^2=P exact) are the lemma\'s given data (via GT-hyp), NOT smuggled-in derived facts, and that no child node is left pending/challenged. Accept the root ONLY if all children are validated.' },
];

phase('Verify');
const verdicts = [];
for (const n of NODES) {
  const v = await agent(
    `${COMMON}\nYOUR NODE: ${n.id}.  YOUR verifier owner-id (VID): ${n.vid}.\n` +
    `NODE-SPECIFIC FOCUS (scrutinize this hardest): ${n.focus}\n` +
    `Run the full PROCEDURE above on node ${n.id} only, then return the verdict.`,
    { schema: VERDICT_SCHEMA, label: `verify:${n.id}`, phase: 'Verify' }
  );
  verdicts.push(v || { node: n.id, verdict: 'blocked', reasoning: 'verifier agent returned null' });
  log(`node ${n.id}: ${(v && v.verdict) || 'null'}${v && v.issues_found && v.issues_found.length ? ' — issues: ' + v.issues_found.join('; ') : ''}`);
}

const accepted = verdicts.filter((v) => v.verdict === 'accept').length;
const challenged = verdicts.filter((v) => v.verdict === 'challenge');
log(`VERIFY PASS DONE: ${accepted}/${NODES.length} accepted; ${challenged.length} challenged.`);
return { verdicts, accepted, challenged: challenged.map((c) => ({ node: c.node, issues: c.issues_found, reasoning: c.reasoning })) };
