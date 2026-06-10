VERDICT: STATEMENT-AMBIGUOUS.

The notes do not fully pin down the ψ-gap lemma. `S-full` is recoverable as `x(S) >= 1-kappa` from [fable-hlc-attack.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/fable-hlc-attack.md:478), and ψ is only recorded as `x(S)+lambda phi` in [fable-hlc-attack.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/fable-hlc-attack.md:479). The audit adds “usual `lambda=1/2`,” but `Z`, the exact admissibility conditions on `phi`, and whether the row may lie in `W` are not formally specified; see [FA3-audit.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave4/FA3-audit.md:11) and [audit-summary.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave4/audit-summary.md:9).

**Formal Statement Attacked**
Using the most literal reconstruction:

`psi(x)=x(S)+(1/2)phi(x)`, `S-full` means `x(S) >= 1-kappa`, `psi-gap(q)=psi(v*)-psi(q)` where `v*` maximizes ψ, and `Z=max_i psi(p_i)-min_i psi(p_i)`. The lemma says: if `||q-v*||_1 >= rho` and `q(S)<1-kappa`, then `psi(v*)-psi(q) >= kappa Z`.

**Bare-Lemma Counterexample**
Let

```text
P =
[ 1      0      0       0      0  0 ]
[ 0      1      0       0      0  0 ]
[ 0      0      1       0      0  0 ]
[ 0      0      0       1      0  0 ]
[ 1/2    1/2    1/16   -1/16  0  0 ]
[ 29/32  0      5/32   -1/16  0  0 ]
```

Rows sum to 1. Since the first four rows are coordinate rows and the last two rows are the same affine combinations of those coordinate rows, `P^2=P` exactly. The maximum row negative mass is `delta=1/16`, hence `tau=1/4`, `rho=1`, `kappa=1/16`.

Take `S={1,2}`, `phi(x)=-2x_4`, and `psi=x_1+x_2-x_4`. Let `v*=p_5`, `q=p_6`.

`psi(p_5)=17/16`, `psi(p_6)=31/32`, `min psi=-1`, so `Z=33/16`.

`q(S)=29/32 < 15/16 = 1-kappa`, and

```text
||p_5-p_6||_1 = 13/32 + 16/32 + 3/32 = 1 = rho.
```

But

```text
psi-gap = 17/16 - 31/32 = 3/32 = 24/256
kappa Z = (1/16)(33/16) = 33/256
```

so `psi-gap < kappa Z`.

**Why This Is Not A Full F-ψ Refutation**
The same witness is killed by the canonical `W` interpretation: `q=p_6` is itself well-exposed. An explicit exposing function is

```text
h(x)=-(2/5)x_1+(3/5)x_2+(3/5)x_4+2/5,
```

with `h(q)=0` and far-row values at least `2/5 >> kappa`. Thus `q` enters `W`; then `phi=-2x_4` is not the actual top separator relative to `conv W`. So this refutes the standalone recorded inequality, but not a stronger version requiring `phi` to be the canonical separator after computing `W`.

**Calibration**
`P(bare recorded lemma true) = 0`: false under the literal reconstruction above.

`P(intended canonical F-ψ lemma true) ≈ 0.55`: I did not find a full-context counterexample. Minimal extra hypothesis: require `phi` to be the actual normalized top separator for the computed `C=conv W`, and require the high zero-face rows of that separator to be `S-full`; otherwise the S-deficit/`lambda phi` trade remains exactly the open loophole.