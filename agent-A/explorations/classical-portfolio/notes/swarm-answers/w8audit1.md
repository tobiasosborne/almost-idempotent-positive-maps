**Verdict Table**
| lemma | verdict | one-line reason |
|---|---|---|
| §1.1 dual + localization | SOUND-WITH-FIX | Dual matches `d1_infra`, but α-localization needs `t*>0`; `t*=0` remains separate. |
| §2.1 W2 exchange | SOUND | Exact affine pairing with `g`, using `g_v=0` and `0≤g≤R`. |
| §2.3 RF return-flow | SOUND-WITH-FIX | Core diagonal split works, but state `P_vv≥0` and repair the constant proof. |
| §2.4 ND′ near-delta depth | SOUND-WITH-FIX | Main proof survives; advertised `t0≥1.7τ for δ≤0.05` is false. |
| §2.5 SF supply-forcing | SOUND-WITH-FIX | Supply bound is sound; localized A-shadow branch again needs `t*>0`. |
| §2.6 FC/CPL | SOUND-WITH-FIX | FC sound; CPL needs the `P_vv≤0` wording fix already noticed in self-review. |
| §2.7 NG′ no-gain | BROKEN | Not a formal proved lemma; key “consistency” claim is asserted via templates/numerics. |
| §2c.1 RW row-witness | SOUND | Constructed witness is dual-feasible; mass balance checks exactly. |
| §2c.2 WL W-locality | SOUND-WITH-FIX | Statement true, but proof cannot rely on RW as stated for `P_ww≥1`; use exposer proof. |

**Details**
§1.1: The dual at [wave8-fable-closer.md:82](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave8-fable-closer.md:82) matches `exposed_margin`’s max-margin LP in [d1_infra.py:118](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/experiments/d1_infra.py:118). `WLOG α_v=0` is safe by replacing `γ` with `γ-α_v`. Fix: every use of “α lives in the ρ-ball” must carry `t*>0`; at `t*=0`, far α is allowed.

§2.3: The line
```text
P_vv = 1 - σ_v + ν_v
```
is only correct when `P_vv≥0`; otherwise `ν_v` includes the self negative entry. The `3.1δ` bound is plausibly true, but [wave8-fable-closer.md:176](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave8-fable-closer.md:176)’s derivative justification is too loose as written.

§2.4: The exact threshold is
```text
t0/τ = 7/4 - 2τ - δ/2.
```
At `δ=0.05`, this is about `1.278τ`, not `≥1.7τ`. The face extraction itself is fine under the robust duplicate convention in [d3_vertexfix.py:27](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/experiments/d3_vertexfix.py:27).

§2.6: Fix CPL at [wave8-fable-closer.md:265](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave8-fable-closer.md:265):
```text
if P_vv > 0: p_j(S)=P_jv+p_j(A_v);
if P_vv <= 0: p_j(S)=p_j(A_v), so the bound only improves.
```

§2.7: Broken as a proved lemma. The formal-looking assertion
```text
{diagonal identity, F-GB at f, g_f<ε} is consistent with the rest of the belt at any H
```
at [wave8-fable-closer.md:287](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave8-fable-closer.md:287) is not proved from the hypotheses; it appeals to previous templates and numerical probes. Downgrade NG′ to analysis/dead-end guidance, preserving only the algebraic identities.

§2c.2: WL should be proved directly. If `h` exposes `w`, then
```text
0 = h(p_w) = Σ_k P_wk h(p_k),
κ Σ_far P^+_wk ≤ Σ_{P_wk<0} |P_wk| h(p_k) ≤ ν_w.
```
This avoids RW’s stated `P_ww∈[0,1)` restriction.

**Overall**
P(§2+§2c survives af-formalization as written): **0.45**. With the listed fixes and NG′ downgraded out of “proved lemma” status: **0.78**.

Single weakest link: **NG′ as a proved lemma**. Among the real positive lemmas, the weakest reusable dependency is the `t*=0` α-localization gap, because it infects the A-dichotomy/shadow branch.