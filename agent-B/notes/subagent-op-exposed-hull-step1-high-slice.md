# Subagent Step 1: High-Slice Extraction

Date: 2026-06-07.  Lane: Agent B sandbox.  Status: exploratory lemma note,
not a canonical proof shard.

## Task

Work on the first sublemma in the closed-bad-class/high-face block for
`op-exposed-hull`:

```text
long bad lifetime + affine separator phi
  -> high slice still O(tau)-closed under the repaired kernel q.
```

Required inputs read:

```text
docs/plans/2026-06-07-op-exposed-hull-attack-plan.md
agent-B/notes/subagent-op-exposed-hull-bad-kernel.md
agent-B/notes/subagent-op-exposed-hull-frameworks.md
agent-B/notes/subagent-op-exposed-hull-lp-dual.md
```

## Setup

Rows are signed probabilities `p_i`, with

```text
P1=1,        P^2=P,        neg(p_i)<=delta,        tau=sqrt(delta).
```

Write

```text
a_i=neg(p_i),        q_i=p_i^+/(1+a_i).
```

The bad-kernel note gives the positive-coordinate reconstruction

```text
||p_i - sum_j q_i(j)p_j||_1 <= eps,        eps <= 4 delta.      (PC)
```

Let `phi` be an affine functional with l1-dual Lipschitz constant at most
`L_phi` on the affine row span:

```text
|phi(x)-phi(y)| <= L_phi ||x-y||_1.
```

In the usual distance-dual normalization from the LP-dual note, `L_phi<=1`.
Set

```text
phi_i = phi(p_i),        M=max_j phi_j,        h_i=M-phi_i.
```

Use the global maximum over all rows, or at least over every possible
`q_i`-successor.  If `M` is only the maximum over a bad subset and some
successor lies above it, the nonnegative-height argument below is invalid.

For a level `gamma>0`, write

```text
H_gamma={j : h_j <= gamma}={j : phi_j >= M-gamma},
Low_gamma={j : h_j >= gamma}={j : phi_j <= M-gamma}.
```

If `B` is a bad set, also write `s_i=q_i(B^c)`.

## Rowwise Drift Bound

This part is proof-ready.

From `(PC)`,

```text
|phi_i - sum_j q_i(j) phi_j| <= L_phi eps.
```

Therefore

```text
sum_j q_i(j) h_j
  = M - sum_j q_i(j) phi_j
 <= M - phi_i + L_phi eps
  = h_i + L_phi eps.                         (1)
```

Since `h_j>=0` for all rows and `h_j>=gamma` on `Low_gamma`,

```text
q_i(Low_gamma) <= (h_i + L_phi eps)/gamma.   (2)
```

Equivalently, for every `alpha<gamma` and every `i in H_alpha`,

```text
q_i(H_gamma^c) <= (alpha + L_phi eps)/gamma. (3)
```

This is the desired inequality in the prompt:

```text
q_i({phi <= M-gamma})
  <= (height_defect_i + O(delta))/gamma.
```

With `L_phi<=1`, `eps<=4delta`, and `gamma=G tau`, this gives

```text
q_i(Low_gamma) <= (h_i/delta + 4)/G * tau
```

when `h_i=O(delta)`.  In particular, for a separator-maximal row `u`
with `h_u=0`,

```text
q_u({phi <= M-G tau}) <= (4/G) tau.          (4)
```

If `i in H_{A0 delta}`, then

```text
q_i(H_{G tau}^c) <= ((A0+4)/G) tau.          (5)
```

Thus the true rowwise conclusion is two-scale:

```text
top O(delta)-core -> G tau-high slice with O(tau) leakage.
```

A one-scale statement for all `i in H_{c tau}` would only give leakage
approximately `c/G`, which is constant rather than `O(tau)`.

## Adding Bad-Set Closure

If `B` is a bad set and `i in B`, then

```text
q_i((B cap H_gamma)^c)
 <= q_i(B^c) + q_i(H_gamma^c)
 <= s_i + (h_i + L_phi eps)/gamma.           (6)
```

So if `i in B cap H_{A0 delta}` and `s_i<=S tau`, then

```text
q_i((B cap H_{G tau})^c)
 <= (S + (A0+4)/G) tau.                      (7)
```

This is the clean rowwise high-slice extraction lemma.  It needs either a
rowwise exit hypothesis or a later pruning step; a distributional
quasi-closed measure alone does not control the exit of every top row.

## Distributional Version

Let `nu` be any probability measure supported on `B`.  Averaging (1) gives

```text
nu q(H_gamma^c)
 <= (nu h + L_phi eps)/gamma.                (8)
```

Also

```text
nu q((B cap H_gamma)^c)
 <= nu s + (nu h + L_phi eps)/gamma.         (9)
```

If `nu` is supported on `B cap H_alpha`, then `nu h<=alpha`, hence

```text
nu q((B cap H_gamma)^c)
 <= nu s + (alpha + L_phi eps)/gamma.        (10)
```

For `alpha=A0 delta`, `gamma=G tau`, `L_phi<=1`, and `eps<=4delta`,

```text
nu q((B cap H_{G tau})^c)
 <= nu s + ((A0+4)/G) tau.                   (11)
```

This is the distributional high-slice closure that follows directly from
the drift inequality.

## Relation To Long Lifetime

The bad-kernel resolvent alternative supplies a quasi-closed distribution
`mu` on `B` when the expected bad lifetime is large.  A typical output is

```text
mu s <= eta,        ||muT-mu||_1 <= eta,
```

with `eta=O(tau)`.

This gives distributional bad closure, but not rowwise closure.  If a high
slice has mass

```text
m_alpha = mu(B cap H_alpha)>0,
```

and `nu=mu|_{B cap H_alpha}/m_alpha`, then

```text
nu q((B cap H_gamma)^c)
 <= eta/m_alpha + (alpha + L_phi eps)/gamma. (12)
```

Thus a positive-mass `O(delta)` top slice is distributionally
`O(tau + eta/m_alpha)`-closed into a `gamma~tau` top slice.  If
`m_alpha` is bounded below, this is enough.  If `m_alpha` is tiny, the
long-lived distribution sits below the separator maximum, and Step 1 alone
does not extract a recurrent high component.

The standard pruning consequence is:

```text
If nu q(E^c)<=theta, then
E_good={i in E : q_i(E^c)<=sqrt(theta)}
satisfies nu(E_good)>=1-sqrt(theta).
```

Applied to `E=B cap H_alpha` and the estimate above, this turns
distributional closure into rowwise closure for most of the high-slice mass,
but not necessarily for the separator-maximal vertex.

## Candidate Contracts

Proof-ready small contract:

```text
lem-high-slice-drift-bound:
Assume (PC) with error eps and let phi be L_phi-Lipschitz in l1.  If
M=max_j phi(p_j), h_i=M-phi(p_i), and H_gamma={j:h_j<=gamma}, then for
every i and every gamma>0,
  q_i(H_gamma^c) <= (h_i+L_phi eps)/gamma.
```

Bad-set corollary:

```text
lem-high-slice-bad-closure:
Under the same hypotheses, if B is a bad set with exit s_i=q_i(B^c), then
for every i in B,
  q_i((B cap H_gamma)^c) <= s_i+(h_i+L_phi eps)/gamma.
In particular, rows in B cap H_{A0 delta} map outside B cap H_{G tau}
with mass at most s_i+((A0+4)/G)tau.
```

Distributional corollary:

```text
lem-high-slice-distributional-closure:
For any probability nu supported on B cap H_alpha,
  nu q((B cap H_gamma)^c)
    <= nu q(B^c)+(alpha+L_phi eps)/gamma.
```

These are small enough for later `af` packaging.

## What This Does Not Prove

Step 1 does not prove the closed-bad-class augmentation lemma by itself.
Three points remain outside this note:

```text
1. A long-lived distribution may give small average exit but not rowwise exit.
2. The separator-maximal row may have tiny mass under the quasi-stationary
   distribution, so the conditional bound (12) may lose eta/m_alpha.
3. The two-scale top-core statement must still be combined with Step 4
   shadow recurrence to produce a recurrent high bad component.
```

These are not defects in the drift inequality; they are the next no-cycle
problem.

## Constants

Safe normalization for the later chain:

```text
eps <= 4 delta,        L_phi <= 1,
gamma = G tau,         alpha = A0 delta.
```

Then

```text
top-row leakage <= (4/G) tau,
O(delta)-core leakage <= ((A0+4)/G) tau.
```

Choosing `G>=100(A0+4)` makes the height leakage at most `0.01 tau`; the
remaining leakage budget belongs to `q_i(B^c)` or to distributional pruning.

## Verdict

Step 1 is essentially solved in the correct two-scale form.  The proof is a
one-line drift/Markov inequality from positive-coordinate reconstruction.

The form that should be handed to Agent A later is not "the whole
`tau`-high slice is rowwise `O(tau)`-closed"; that statement is too strong
for this argument.  The proof-ready statement is:

```text
rows with separator height defect O(delta) map with only O(tau) mass below
a separator level gamma~tau, and the same holds distributionally for any
measure supported on that top core.
```

The next handoff is to Step 2/3: use this high plateau to test whether a
separator-maximal top row is well-exposed, and if not, generate a
rho-separated high shadow witness without losing the `O(tau)` closure budget.
