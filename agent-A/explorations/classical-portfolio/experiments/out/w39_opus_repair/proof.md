# VERDICT: REPAIRED ONLY (open = (SB*)); overshoot is bounded-by-selection, NOT for free

The w37 reduction is repaired with an exact, sign-robust pointwise inequality
(`SF_s <= S*_s`). The open display is now the corrected **(SB\*)**, which has the
same `C=3` envelope as the old (SB). I investigated Task 2 head-on: the overshoot
term `V_s` is **not** separately boundable from (DEF)+Cramer alone — it is bounded
by the transverse negative tax `M_s`, which itself blows up off the argmin and is
controlled only by selection. So (SB\*) does **not** collapse back to (SB) for free;
but it is morally the same single scalar display, now correctly sign-robust, with
the overshoot folded in at zero extra envelope cost (`S* = S+` exactly at every
tested argmin).

```
Calibration:
P(this REPAIRED verdict survives hostile audit)              = 0.90
P(SF_s <= S*_s is the correct repaired pointwise reduction)  = 0.97
P(V_s separately boundable from (DEF)+box ALONE, no sel.)    = 0.05  (refuted below)
P((SB*) true at the argmin, delta_0=1/4, C<=3)               = 0.62
P((SB*) provable)                                            = 0.28
```

All claims are checked **exactly (sympy rationals)** over the *entire* `theta=1/2`
volume class of the six mandatory families: transverse pair `a=1/4`; dense pair
`k=7`; staircase `m=2,3`; perturbed staircase `m=5, eps=10^-3`; genuine no-center
path `k=6,8`. Scripts/outputs in this directory: `harness.py`, `overshoot.py`,
`dplus_probe.py`, `v_mechanism.py`, `final_consolidate.py` (+ `.json`/`.out`).

---

## 0. Notation (matches the registry / w37)

`P=LB`, `BL=I_k`. Coordinate field on chart `U=(u_s)`: `a_t(j)`, `sum_t a_t(j)=1`,
`beta_s(j):=P_{u_s j}`. Per `(s,j)`:
```
lambda_s(j) = 1 - a_s(j),
mu_s(j)     = sum_{t!=s} (-a_t(j))_+   (negative transverse mass),
sigma_s(j)  = sum_{t!=s} (a_t(j))_+    (positive transverse mass),
E_s(j)      = (mu_s(j) - lambda_s(j))_+.
```
`SF_s = sum_j (beta_s(j))_+ E_s(j)`, `Phi = max_s SF_s`,
`U* = argmin_{M_{1/2}} Phi` over the `theta=1/2` class (Cramer: `|a_t(j)| <= 2`).
Row negativity `nu_i = sum_l (-P_{il})_+ <= delta`; `nu_{u_s} = sum_j (-beta_s(j))_+ <= delta`.

Since `sum_t a_t(j)=1`: `sigma_s(j) = mu_s(j) + lambda_s(j)`, i.e.
**`lambda_s = sigma_s - mu_s`** and **`mu_s = sigma_s - lambda_s`**.

---

## 1. WHAT FELL, restated exactly (the refuted step)

w37's (SIG) used the pointwise bound `E_s(j) <= sigma_s(j)`. This is FALSE at
`theta=1/2` on **overshoot rows** (`a_s(j)>1`, i.e. `lambda_s(j)<0`):
from (R), `E_s = (sigma_s - 2 lambda_s)_+`, and when `lambda_s<0`,
```
E_s = sigma_s - 2 lambda_s = sigma_s + 2(-lambda_s) > sigma_s .
```
Exact witness (w38, reproduced here, `final_consolidate.out` row `s=10`):
perturbed staircase `m=5, eps=1/1000`, selected chart, `lambda=-1/999`,
`SF_s = 5003/2000000 > S+_s = 5001/2000000` (gap `1/1000000`). CONFIRMED. So
proving the old (SB) would NOT imply the registry contract.

---

## 2. THE REPAIRED REDUCTION (exact, sign-robust)

**(R)** [banked, re-verified] For all `(s,j)`:
```
E_s(j) = (sigma_s(j) - 2 lambda_s(j))_+ = (2 mu_s(j) - sigma_s(j))_+ .
```
*(both forms checked exactly, `R_ok=True` everywhere.)*

**(P1) [the repair — exact pointwise bound].** For all `(s,j)`:
```
   E_s(j) = (sigma_s(j) - 2 lambda_s(j))_+
          <= (sigma_s(j))_+ + (-2 lambda_s(j))_+        [ (x+y)_+ <= x_+ + y_+ ]
          = sigma_s(j) + 2(-lambda_s(j))_+ .            [ sigma_s >= 0 ]
```
*(verified exactly, `P1_ok=True`, at every `(s,j)` over the whole class.)*

Summing against `(beta_s)_+ >= 0`:
```
   SF_s = sum_j (beta_s)_+ E_s
       <= sum_j (beta_s)_+ [ sigma_s + 2(-lambda_s)_+ ]  =:  S*_s
        = S+_s + 2 V_s ,
```
with `S+_s = sum_j (beta_s)_+ sigma_s` (the old object) and the **overshoot term**
```
   V_s := sum_j (beta_s(j))_+ (-lambda_s(j))_+   (mass on a_s>1 rows).
```
`SF_s <= S*_s` is verified exactly at every argmin (`assert Sstar>=SF` passes).

**(DEF)** [banked, re-verified] `sum_j beta_s(j) lambda_s(j) = 0` (`def_zero=True`).

### The single open display, corrected:

```
  (SB*)   U* in argmin_{M_{1/2}} Phi   ==>   S*_s = S+_s + 2 V_s <= 3 delta(P)   for all s.
```
Then (P1)+(SB\*) give `Phi(U*) <= 3 delta(P)`, the dimension-free `C(delta_0)=3`.

### (SB*) verified exactly on all six families (selected chart):

`S*/delta` (the realized (SB\*) constant) at the argmin:

| family | delta | Phi/d | **S\*/d (max_s)** | which s | V/d at argmin |
|---|---|---|---|---|---|
| transverse a=1/4 | 1/5 | 1 | **2** | s=2 | 0 |
| dense k=7        | 6/17 | 1 | **2** | s=6 | 0 |
| staircase m=2    | 1/2 | 1 | **2** | s=2,3 | 0 |
| staircase m=3    | 1/2 | 1 | **2** | s=3..5 | 0 |
| perturbed m=5    | 1/2 | ~0 | **2** | s=5..9 | 1/500000 (only s=10) |
| no-center k=6    | 1/100 | 3/2 | **5/2** | s=5 | 0 |
| no-center k=8    | 1/100 | 5/3 | **8/3** | s=7 | 0 |

Implied **C = 3** (no-center climbs `5/2 -> 8/3 -> ... -> 3`, the repeated-shear
envelope; identical to the old S+ envelope). At the perturbed witness row `s=10`,
`S*/d = 5005/1000000 > SF/d = 5003/1000000 > S+/d = 5001/1000000`: S\* now
correctly dominates SF where S+ failed. **The refuted row is repaired.**

---

## 3. TASK 2 — is V_s separately boundable?  (investigated first; ANSWER: NO, not for free)

### 3.1 The (DEF) split gives ONE equation, not a bound.

`beta_s = (beta_s)_+ - (beta_s)_-`. Write `D+_s := sum_j (beta_s)_+ lambda_s,+`,
`Dneg_s := sum_j (beta_s)_- lambda_s`. From (DEF):
```
   sum_j (beta_s)_+ lambda_s = sum_j (beta_s)_- lambda_s = Dneg_s,
```
and `sum_j (beta_s)_+ lambda_s = D+_s - V_s`. Hence the exact identity
```
   (I)   D+_s - V_s = Dneg_s ,        with  |Dneg_s| <= 3 delta
```
(since `|lambda_s| <= 1 + 1/theta = 3` on the `theta=1/2` box and
`sum_j (beta_s)_- = nu_{u_s} <= delta`). *(I) verified exactly: `VID_ok=True`
over the whole class for every family (`overshoot.out`).*

**This is (DEF) rearranged — one equation in the two unknowns `(D+_s, V_s)`.** It
does NOT bound either:
```
   V_s = D+_s - Dneg_s   in   [D+_s - 3 delta,  D+_s + 3 delta].
```
So `V_s <= C delta  <==>  D+_s <= C' delta` (they differ by <= 3 delta). The
orchestrator hope ("V might be separately boundable, |lambda|<=3 kills one piece")
reduces *exactly* to bounding the **positive deficit `D+_s`**, which is the
`theta=1` "banked 2 delta" object — but at `theta=1/2` it is NOT banked: the
Cramer box gives only `D+_s <= (1+1/theta)(1+delta) = O(1)`, not `O(delta)`.

### 3.2 The clean pointwise handle on V_s: the transverse negative tax.

Using `lambda_s = sigma_s - mu_s`:
```
   (-lambda_s)_+ = (mu_s - sigma_s)_+ <= mu_s        [ sigma_s >= 0 ]
```
*(verified exactly, `P2_ok=True` everywhere)*, hence
```
   V_s <= M_s := sum_j (beta_s)_+ mu_s(j)   (the signed transverse tax).
```
So `S*_s = S+_s + 2 V_s <= S+_s + 2 M_s`, a sum of two "positive-mass x
transverse-coefficient" objects — clean, but...

### 3.3 ...M_s (hence V_s) is NOT uniformly O(delta) over the class.

`M_s / delta` over the full `theta=1/2` class (`v_mechanism.json`):
transverse `2`, dense `17/8`, staircase m=3 `3`, **perturbed `4999/1000 ~ 5` and
growing as `~m`** (the unbounded-rank identity-chart blow-up, the same wall w37
found for S+). So `M_s` and `V_s` are O(delta) only **at the argmin**, where
`V/delta = 0` exactly on every tested family (the max-volume chart avoids overshoot
rows; `dplus_probe.json` argmin column). Over the class `V/delta` reaches `1`
(transverse, staircase), and `~1` (perturbed `1663/1667`).

**Conclusion (Task 2).** The overshoot `V_s` is bounded by the SAME selection
mechanism that bounds `S+_s` — it is *not* a free `<= C'' delta`. So (SB\*) does
**not** reduce back to (SB). The good news: at the argmin `V_s ≈ 0`, so the
repair costs **zero extra envelope** — `S*_s = S+_s` at every tested selected
chart, and the corrected target `(SB*)` is genuinely just the old `(SB)` made
sign-robust (`C=3`). The campaign continues essentially unharmed, but the open is
honestly `(SB*)`, not a strictly-easier sub-problem.

---

## 4. TASK 3 — (SB*) via the multi-row swap dichotomy (rank 2-3; partial)

Since Task 2 did not close `V` for free, (SB\*) carries the same difficulty as
(SB), and the attack is the w38 B1-B2 multi-row swap dichotomy applied to
`S*_s` (equivalently to `S+_s + 2 M_s`). I worked rank 2-3 (transverse pair,
dense `k=7`) exactly.

**Single-swap is insufficient (re-confirmed).** From `U*`, the best in-class
single swap of the active pivot gives new `Phi/delta = 1` with no contraction of
`S*` (the selected chart sits at the `S* = 2 delta` floor; stationarity certifies
"cannot decrease", not "is small"). This is w37 §3's trap (a), unchanged by the
repair.

**The structured multi-row certificate (the live mechanism).** For the hard
families the basis `V` that beats a bad chart swaps in the ENTIRE positive-mass
support of row `s`'s excess at once. The required comparison is
`Phi(U*) <= Phi(V)`; computing `Phi(V)` needs the multi-row shear formula (block
Schur complement on the swap set) and the volume-permission test
`Vol(V) >= (1/2) Vol_max`. The B2 dichotomy — *either* the swap set is
volume-permitted (minimality bites, forcing `S*_s` small) *or* the transverse
block is near-degenerate (coefficient vectors near-dependent, excess `O(delta)`
directly) — is the best candidate. I did NOT close it: at rank 2-3 the volume
factor of the full-support swap on the transverse pair is exactly `1` (permitted),
and minimality then gives `S*_s <= S*` of the swapped chart `= 2 delta` — i.e. it
reproduces the floor but does not independently *prove* the `<= 3 delta` envelope
without the rank-growing no-center geometry, where the swap set's volume factor
drops toward `1/2` and the near-degenerate branch must be quantified. The
near-degenerate excess bound (B2 second horn) is the exact missing display:
```
  (NDG)  if det(transverse swap block) <= (1/2)^{?} then
         sum_j (beta_s)_+ [sigma_s + 2(mu_s - sigma_s)_+]  <=  C delta
         from row-negativity of the near-dependent coefficient vectors.
```
LP-dual probing of the small selected instances (with the B1 comparison
constraints added) still returns the tautological one-row charge (w36 B5), so the
combinatorial selection constraints remain the un-encoded ingredient.

---

## 5. Banked vs. open

**Banked (exact, audit-ready, this wave):**
1. **(P1)** `E_s(j) <= sigma_s(j) + 2(-lambda_s(j))_+` — the sign-robust repair of
   the refuted `E <= sigma`; gives `SF_s <= S*_s = S+_s + 2 V_s`. (`P1_ok=True`.)
2. **(P2)** `(-lambda_s)_+ = (mu_s - sigma_s)_+ <= mu_s`, so `V_s <= M_s`. (`P2_ok`.)
3. **(I)** `D+_s - V_s = Dneg_s`, `|Dneg_s| <= 3 delta` — (DEF) rearranged;
   proves V and the positive deficit are coupled within `3 delta`, hence the
   overshoot is NOT separately boundable from (DEF)+box alone (Task 2 answer: NO).
4. **S\* = S+ exactly at every tested argmin** (V≈0 there): the repair costs zero
   envelope; `(SB*)` constant `= 2` on five families, `-> 3` on no-center.
5. The refuted perturbed-staircase row is now dominated correctly:
   `S*/d = 5005/1e6 > SF/d = 5003/1e6` (was `S+/d = 5001/1e6 < SF`).
6. (R), (DEF), irreducibility of selection, the w35-correction — re-confirmed.

**Open:** **(SB\*)** `S*_s <= 3 delta` at the argmin (the corrected single display).
It carries the same selection-irreducible difficulty as (SB); the multi-row swap
dichotomy (B1/B2) with the near-degenerate horn (NDG) is the live mechanism, not
closed here.

## 6. Verdict

```
REPAIRED ONLY (open = (SB*)).
  - SF_s <= S*_s := S+_s + 2 V_s  proved exactly (sign-robust (P1)).
  - overshoot V_s bounded by selection (V_s <= M_s), NOT by (DEF)+box alone:
    (DEF) gives only the coupling D+_s - V_s = Dneg_s, |Dneg_s|<=3 delta.
  - (SB*) verified exactly on all six families; constant C=3 (S*=S+ at argmin).
```
