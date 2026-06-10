REPAIR: SUCCESS-a

The old `H-rho` step is false, but route (a) gives a valid replacement with a weaker loss.

**Repaired Lemma**
Let `D_v = sup_{x in K} ||x-v||_1 <= D := 2+4δ`, `C = conv W`, and `H = dist_1(v,C)`. If `v` is a hidden row vertex failing `(rho,kappa)`-exposedness, then either

```text
H <= Lambda_v := kappa D_v^2 / rho,
```

or there is another geometric row vertex `u != v`, not in `W`, such that

```text
dist_1(u,C) >= H - Lambda_v.
```

With `rho=4tau`, `kappa=tau/4`,

```text
Lambda_v <= (2+4δ)^2 / 16.
```

So for `δ <= 1`, `Lambda_v <= 9/4`; for small `δ`, the guaranteed loss tends to `1/4`. This is not the old `O(rho)` loss.

**Proof**
Let `F = {j : ||p_j-v||_1 >= rho}`. Since `v` fails exposedness, the established dual gives `mu` a probability on `F`, `alpha,beta >= 0`, and `B := sum beta_i < kappa`, with

```text
sum_j mu_j (p_j-v) = sum_i (beta_i-alpha_i)(p_i-v).
```

Set `A := sum alpha_i` and

```text
x = (sum_j mu_j p_j + sum_i alpha_i p_i) / (1+A).
```

Rearranging the dual identity gives

```text
x - v = (sum_i beta_i (p_i-v)) / (1+A),
```

hence

```text
||x-v||_1 <= B D_v/(1+A).
```

Therefore, by 1-Lipschitzness of `dist_1(.,C)`,

```text
dist_1(x,C) >= H - B D_v/(1+A).          (1)
```

Let `M = max{dist_1(u,C) : u is a geometric vertex, u != v}`. If `M >= H - B D_v^2/rho`, we are done.

Assume instead `M < H - L`, where `L > B D_v^2/rho`. Expand each row as

```text
p_i = theta_i v + (1-theta_i) z_i,    z_i in conv(vertices \ {v}).
```

Then convexity of distance gives

```text
dist_1(p_i,C) <= theta_i H + (1-theta_i) M
              <= H - (1-theta_i)L.
```

For every `mu`-row, `||p_j-v||_1 >= rho`, while `||z_j-v||_1 <= D_v`, so

```text
1-theta_j >= rho/D_v.
```

Thus

```text
sum_j mu_j dist_1(p_j,C) <= H - (rho/D_v)L,
sum_i alpha_i dist_1(p_i,C) <= A H.
```

Since `x` is the corresponding average, convexity gives

```text
dist_1(x,C) <= H - (rho/D_v)L/(1+A).     (2)
```

Combining (1) and (2),

```text
B D_v/(1+A) >= (rho/D_v)L/(1+A),
```

so `L <= B D_v^2/rho`, contradiction. Hence

```text
M >= H - B D_v^2/rho > H - kappa D_v^2/rho.
```

Choose a vertex `u != v` attaining `M`. If the lower bound is positive, `u` cannot lie in `W`, since every `W` vertex lies in `C` and has distance `0`.

**Downstream Change**
The vertex recursion survives only in this weakened form: a hidden vertex at height `H` produces another hidden vertex at height at least `H - kappa D_v^2/rho`, not `H-rho`. With the current parameters this loss is scale `~1/4`, not `O(tau)`, so the old same-shell recursion/cycle and no-staircase argument do not close the `O(tau)` theorem. The remaining obstruction is precisely a near-edge/self-shadow collar: far rows can be `rho` away from `v` while carrying only `rho/D_v` vertex mass away from `v`. That case now needs its own projection-cost/no-staircase lemma rather than being hidden inside the recursion step.
---
## ORCHESTRATOR ANNOTATION (post-review, 2026-06-10)
The repair is PROVED but QUANTITATIVELY VACUOUS at conjecture scale: the per-step loss
Λ_v = κD_v²/ρ → (2+4δ)²/16 ≈ 1/4 is a CONSTANT, while the regime of interest is H ~ Dτ → 0, so the
"H ≤ Λ_v" branch always fires. The bound becomes useful (loss ~ D²δ/16 ≪ H) exactly when the dual
mass is localized to an O(H)-neighbourhood of v — i.e. the recursion repair is CONDITIONAL on
dual-localization. Sixth independent reduction to the same crux. Do NOT cite the repaired recursion
as unconditionally restoring the D4 descent chain.
