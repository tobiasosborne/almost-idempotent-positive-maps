VERDICT: PARTIAL. I prove the `sigma_tilde <= tau` side of existential DMF with explicit constants, but the full attack dies at the exact place where a shallow optimal witness is pushed through `P`: negativity makes the pushed witness leave the optimal dual face.

Proof / post-mortem:

Let `C = conv W`, `s = sigma_tilde_v`, and `nu_v <= delta`. Split the positive part of row `v` into mass `m = 1 + nu_v - s` on rows in `C` and mass `s` outside `C`. If `m > 0`, take the normalized inside-`C` barycenter `c in C`. Since every row has `||p_i||_1 <= 1 + 2delta`,

```text
H = dist_1(p_v, C)
  <= ||p_v - c||_1
  <= (s + nu_v + |s - nu_v|)(1 + 2delta)
  = 2 max(s, nu_v)(1 + 2delta).
```

So if `sigma_tilde_v <= tau` and `delta <= 1/4`, then `H <= 3 tau`. Taking `C_D = 3`, the DMF threshold is `H - C_D delta/tau = H - 3tau <= 0`; since `g >= 0`, every optimal witness has deep mass `1`. Thus existential DMF holds on the whole `sigma_tilde <= tau` branch with `m* = 1`, `C_D = 3`.

For `sigma_tilde > tau`, I tried the support-minimal optimal-witness cleanup. The fatal calculation is this. Push the `mu`-rows of an optimal witness through `P`. Let

```text
M_F = sum_j mu_j sum_{k in F_v} P^+_{jk},
N   = sum_j mu_j neg(p_j).
```

The pushed, renormalized witness has objective

```text
B_pushed = (B + N) / M_F.
```

To remain optimal one would need

```text
B_pushed <= B
iff
M_F >= 1 + N/B.        (*)
```

But always `M_F <= 1 + N`, while `B = t* < kappa < 1`. Hence `(*)` is impossible as soon as `N > 0`. This is exactly why the Baake-Sumner descent works at `delta = 0` but not perturbatively by LP cleanup alone.

New sub-lemmas:

1. `sigma_tilde` height cap:  
   `H <= 2(1+2delta) max(sigma_tilde_v, neg(p_v))`. Proved above.

2. `sigma_tilde <= tau` DMF branch:  
   for `delta <= 1/4`, existential DMF holds with `m* = 1`, `C_D = 3`. Proved by the height cap.

3. Pushed-witness cost lemma:  
   pushing shallow witness rows through `P` changes the dual objective to `(B+N)/M_F`; optimality would require `M_F >= 1+N/B`, impossible for any negative leakage `N>0`. Proved above; this is a dead-end certificate.

Calibration: `P(existential DMF true) = 0.72`. `P(this partial argument survives audit) = 0.84` overall; the `sigma_tilde` cap itself is about `0.93`, the pushed-witness death calculation about `0.88`.

Sharpest structural insight: `sigma_tilde`, not `sigma_v`, is the real branch variable. If `sigma_tilde` is `O(tau)`, DMF is already vacuous because the hidden vertex is only `O(tau)` from `conv W`. If `sigma_tilde > tau`, the obstruction is not ordinary LP support cleanup: any negative mass, however small, makes row-substitution non-optimal by the factor `N/B ~ N/tau`. The remaining problem is genuinely quantitative Baake-Sumner stability for a signed shallow hidden web, not another exposedness-dual algebra trick.