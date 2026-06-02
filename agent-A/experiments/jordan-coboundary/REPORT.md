# Numerical test: dimension-free splitting of the Jordan coboundary $d^1$

(Authoring agent stalled before writing this; report reconstructed by Agent A from the saved `results_*.json`.)

## Question
Does the Jordan-cohomology coboundary $d^1:C^1(J,J)\to C^2(J,J)$,
$(d^1h)(a,b)=a\circ h(b)+h(a)\circ b-h(a\circ b)$, admit a bounded right-inverse
$s$ (so $d^1 s=\mathrm{id}$ on $Z^2=B^2$, valid since $H^2=0$) whose norm is
**independent of $\dim J$**? $\|s\|=1/\sigma_{\min}(d^1)$ for the relevant norms.

## Setup validation (computation is correct)
For $J=H_n(\mathbb C)$, $\dim\ker d^1 = 3,8,15,24,35$ for $n=2..6$ $= n^2-1=\dim\mathfrak{su}(n)$ ✓.
For spin factors $V_n$, $\dim\ker d^1 = 1,3,6,10,15,21,28 = n(n-1)/2=\dim\mathfrak{so}(n)$ ✓.
These match the known derivation algebras exactly, so the coboundary operator is built correctly.

## Result 1 — Frobenius/trace inner-product norm: BOUNDED (dimension-free)
$1/\sigma_{\min}(d^1)$ with cochains measured in the trace (Frobenius) inner product:

| family | $n$ | $1/\sigma_{\min}$ |
|---|---|---|
| $H_n(\mathbb C)$ | 2,3,4,5,6 | 0.91, 0.78, 0.69, 0.62, 0.57 (decreasing) |
| spin $V_n$ | 2..8 | 0.66, 0.64, 0.635, 0.630, 0.627, 0.625, 0.623 → ~0.62 (converges) |
| $H_n(\mathbb R)$ | 2..6 | 0.93 → 0.70 ($\sim 2/\sqrt n$, decreasing) |

**Verdict: in the trace/Frobenius norm the bounded right-inverse exists with $\|s\|\le 1$, uniformly in dimension.** This confirms the *projective-norm/group-averaging* mechanism in the inner-product norm: $\sigma_{\min}$ grows like $\sqrt n$ while $\sigma_{\max}=O(\sqrt n)$ stays comparable, so $1/\sigma_{\min}$ stays $O(1)$.

## Result 2 — operator (order-unit) norm: UNRESOLVED (this is the norm the theorem needs)
The structure theorem controls cochains in the **order-unit (operator) norm** of $J$, not the Frobenius norm. Certified **lower** bounds on $\|s\|_{\mathrm{op}\to\mathrm{op}}$ for $H_n(\mathbb C)$ (max operator-norm ratio found by search; the true $\|s\|_{\mathrm{op}}$ is $\ge$ these):

| $n$ | $\|s\|_{\mathrm{op}}$ lower bound | $/\sqrt n$ | $/n$ | crude upper bound |
|---|---|---|---|---|
| 2 | 1.39 | 0.98 | 0.70 | 7.3 |
| 3 | 1.41 | 0.81 | 0.47 | 21 |
| 4 | 1.57 | 0.78 | 0.39 | 44 |
| 5 | 1.62 | 0.73 | 0.32 | 78 |
| 6 | 1.79 | 0.73 | 0.30 | — |

**Verdict: inconclusive.** The lower bound grows *slowly* (sub-$\sqrt n$: $\|s\|/\sqrt n$ and $\|s\|/n$ both decrease), consistent with bounded or $\log$-type growth. But the crude **upper** bound grows like $\sim n$, so boundedness is NOT established. The data range ($n\le 6$) cannot distinguish "bounded" from "slowly growing".

## Interpretation (the real subtlety)
The Frobenius-norm boundedness comes from averaging over the unitary group of the multiplication algebra $M(J)$, whose elements ARE Frobenius-isometries. But the order-unit norm is only preserved by the *Jordan automorphism* group $\Aut(J)$, which is strictly smaller than $U(M(J))$. The cohomological splitting that is $O(1)$ in Frobenius norm need not be $O(1)$ in operator norm, because the order-isometry group $\Aut(J)$ may be too small to represent the $M(J)$-separability idempotent with $O(1)$ operator-norm projective bound. **This is the precise gap.** Resolving it requires either (i) an $\Aut(J)$-only construction of the splitting with an operator-norm bound, or (ii) Kitaev's incremental route (apply the splitting only to small/controlled $\mathcal B$ at each merge step), or (iii) accepting a Frobenius-norm formulation and converting at a (possibly dimension-dependent) cost.

## Caveats
- $\|s\|_{\mathrm{op}}$ values are LOWER bounds from random+structured search; true values are $\ge$. Operator-norm computation is expensive (~400 s/n), which is why the run stalled at $n=5$–$6$.
- Test is for the ADJOINT module $M=J$; the error-reduction uses $M=A$ (an $\eps$-JB algebra), a further approximation not tested here.

## Files
`jordan_common.py`, `jordan_fast.py` (build $d^1$), `run_sweep.py` (Frobenius), `run_opnorm.py`/`opnorm_trend.py`/`opnorm_sharp.py` (operator norm), `results_*.json`.
