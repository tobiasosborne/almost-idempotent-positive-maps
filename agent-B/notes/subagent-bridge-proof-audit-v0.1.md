# Subagent Bridge Proof Audit v0.1

Audit target: `agent-B/theory/theorem-B-algebraic-bridge.md`

Context: `agent-B/notes/theorem-stack-v0.3.md`

## Verdict

I did not find a fatal gap in the local algebraic bridge proof of the
`O(sqrt(eta))` epsilon-JB order-unit algebra, assuming the initial
spectral-idempotent estimates for `P` are available in the stated norm:

```text
P^2=P,   P(1)=1,   ||P-Phi||=O(eta),   ||P||<=1+O(eta).
```

The Lemma 2 to Lemma 5 mechanism is mathematically coherent: state-seminorm
almost orthogonality gives first insertion, the square-hole positivity shift
gives an `O(eta)` null-square estimate, polarization gives hole-state bounds,
and the one-hole estimates are enough to close the Jordan identity at
`O(sqrt(eta))`.

The main issues are proof-polish and assumptions that should be made explicit
before treating the theorem as locked.

## Highest-Risk Issue

The bridge proof is conditional on the spectral-calculus estimate quoted at
`theorem-B-algebraic-bridge.md:59-64`. This is not just cosmetic: every later
step uses both `delta=||P-Phi||=O(eta)` and `||P||<=1+O(eta)`. The draft should
either cite a lemma that proves this for unital positive maps on the
self-adjoint order-unit norm, or include the proof. If the available Kitaev
estimate is only stated for UCP/cb settings, this is the one dependency that
could invalidate the current theorem statement.

Related statement issue: `theorem-stack-v0.3.md` defines epsilon-JB order-unit
algebras as finite-dimensional, but the theorem statement says only
`V=B(H)_sa`. Add `dim H<infty` or explicitly broaden the definition used in
this bridge theorem.

## Lemma Checks

### Lemma 2: State Seminorm Almost-Orthogonality

The argument is sound. The almost-contraction estimate follows from:

- `||Px-Phi x||<=delta||x||`,
- the square Lipschitz bound
  `||(Px)^2-(Phi x)^2||<=C delta ||x||^2`,
- Jordan-Schwarz for the unital positive map `Phi`,
- `||Phi^2-Phi||<=eta`.

The optimization step from

```text
2s |omega(u o n)| <= s^2(a+2K eta ||n||^2)+2K eta ||u||^2
```

does give

```text
|omega(u o n)| <= C sqrt(eta)||u||||n||
```

because `a=||n||_omega^2<=||n||^2`.

Recommended tightening:

- State explicitly that `rho o Phi` is a positive functional, so
  `||x||_omega^2=omega(x^2)` is a seminorm and the quadratic expansion is valid.
- In the first displayed proof line, spell out the square Lipschitz estimate
  and the absorption `delta=O(eta)`.
- In `(FI)`, record `||x-Px||<=C||x||` and that the final state supremum is
  over self-adjoint elements, hence equals operator norm.

### Lemma 3: Positivity Shift and `||P(q_r^2)||`

The positivity-shift argument appears valid. The key point is that the shifted
kernel element

```text
y=q_r+gamma 1,   gamma=C delta ||r||^2
```

is positive, while `Phi(y)` is positive and small:

```text
||Phi(y)|| <= ||Phi(q_r)||+gamma <= C delta ||r||^2.
```

Then `0<=y<=C||r||^2 1` gives `Phi(y^2)<=C||r||^2 Phi(y)`, and the estimate for
`Phi(q_r^2)` follows from `q_r^2<=(constant)(y^2+gamma^2 1)`. Replacing `Phi`
by `P` costs `delta||q_r^2||<=C delta||r||^4`.

Recommended tightening:

- Add the crude bound `||q_r||<=C||r||^2` before using
  `||Phi(q_r)||=||(Phi-P)(q_r)||`.
- Say explicitly that `gamma^2||1||=O(delta^2||r||^4)` is absorbed into
  `O(delta||r||^4)` after decreasing `eta0`.
- The proof of `(3.3)` uses the preceding bound on `Phi(q_r^2)`, not the
  displayed `(3.2)` alone. Make that dependency explicit.

No sign error found: `q_r=P(r^2)-r^2` is in `Ker P`, and the lower bound
`q_r>=-C eta||r||^2 1` is enough for the shift.

### Lemma 4: Polarization, HH, and HZ

The polarization identity is correct:

```text
lambda q_{r,s}=q_{lambda r,s}
              =1/4(q_{lambda r+s}-q_{lambda r-s}).
```

Optimizing in `lambda` gives the claimed
`||q_{r,s}||_omega<=C sqrt(eta)||r||||s||`.

The HH and HZ conversions are also sound, provided the replacement costs are
written out:

- HH replacement:
  `||(P-Phi)(q_{r,s} o q_{u,v})|| <= C eta ||r||||s||||u||||v||`.
- HZ replacement:
  `||(P-Phi)(q_{r,s} o z)|| <= C eta ||r||||s||||z||`, absorbed into the
  `O(sqrt(eta))` target for `eta<=eta0<=1`.

Recommended tightening:

- State the Cauchy-Schwarz inequality used for the positive functional
  `rho o Phi` in Jordan form:
  `|omega(x o y)|^2<=omega(x^2)omega(y^2)`.
- State the crude norm bound
  `||q_{r,s}||<=C||r||||s||`, used in the replacement estimates.

### Lemma 5: One-Hole Contexts

Both one-hole estimates are valid.

For `(5.1)`, the decomposition `y=h o t=P(y)+(y-P(y))` works because:

- `||P(y)||<=C sqrt(eta)||r||||s||||t||` by HZ;
- `||P(P(y) o u)||` is then small by the product norm bound;
- FI applied to `x=y`, `b=u` controls
  `P((y-P(y)) o u)=P(y o u)-P(P(y) o u)`.

For `(5.2)`, the split `t o u=P(t o u)+h_{t,u}` works because the first term is
HZ and the second is HH. The HH contribution is actually `O(eta)`, so note
explicitly that it is absorbed into `O(sqrt(eta))`.

Recommended tightening:

- In `(5.1)`, record `||y||<=C||r||||s||||t||`, since FI uses the crude norm of
  `y`, not the small norm of `P(y)`.
- In `(5.2)`, replace "controlled by `(HH)`" with "controlled by `(HH)`, hence
  `O(eta)` and absorbed for small `eta`."

### Final Jordan-Identity Expansion

The expansion is consistent. The signs of the holes match the definitions:

```text
h_{r,s}=r o s-P(r o s),   q_{r,s}=-h_{r,s}.
```

The left side reduces to

```text
P(((a^2 o b) o a)) + O(sqrt(eta)||a||^3||b||),
```

using FI for `P(l o a)` and Lemma 5 for the `h_{a,a}` term.

The right side reduces to

```text
P(a^2 o (b o a)) + O(sqrt(eta)||a||^3||b||),
```

using Lemma 5, FI for `P(p o h_{b,a})`, and HH for the two-hole terms.

The final cancellation by the ambient special Jordan identity

```text
(a^2 o b) o a = a^2 o (b o a)
```

is legitimate.

Recommended tightening:

- At `theorem-B-algebraic-bridge.md:419-424`, explicitly say FI is applied with
  `x=h_{b,a}` and `b=p`, so `P(h_{b,a})=0` makes the left FI term vanish.
- At `theorem-B-algebraic-bridge.md:427-433`, record that the HH terms are
  `O(eta)` and are absorbed into `O(sqrt(eta))`.

## Additional Proof-Polish Items

- Since `Phi` is stated only on `B(H)_sa`, either invoke the real Jordan
  version of Jordan-Schwarz or mention the standard complexification. The local
  references already contain the needed Jordan-Schwarz result for unital
  positive maps.
- Define the cutoff function/projection notation `theta(2Phi-I)` or cite the
  exact spectral projection convention.
- Replace some `O(...)` statements inside the proof with named constants at the
  end, or add one sentence saying all implicit constants are universal and
  `eta0` is decreased whenever an `O(eta)` term is absorbed into
  `O(sqrt(eta))`.

## Bottom Line

Conditional on the quoted spectral-projection estimates, the proof of the
`O(sqrt(eta))` algebraic bridge is sound. I would not mark Lemmas 2-5 or the
final Jordan-identity expansion as containing a fatal mathematical gap. The
draft needs tighter bookkeeping and a clear statement of its external
spectral-calculus and finite-dimensionality assumptions.
