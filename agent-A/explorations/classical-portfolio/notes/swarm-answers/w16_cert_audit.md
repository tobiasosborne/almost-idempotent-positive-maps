# w16_cert_audit — CERTIFIED (exact rational); family persists to delta <= 0.1 (codex independent verifier, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w16_cert_audit/brief.md. Artifacts: experiments/out/w16_cert_audit/.

VERDICT: CERTIFIED (exact rational).  
Rational instance: [w16_best_rational_instance.json](/tmp/codex-sigma-wall/w16_cert_audit/w16_best_rational_instance.json). Verifier and full outputs: [independent_verifier.py](/tmp/codex-sigma-wall/w16_cert_audit/independent_verifier.py), [audit_results.json](/tmp/codex-sigma-wall/w16_cert_audit/audit_results.json), [audit_report.md](/tmp/codex-sigma-wall/w16_cert_audit/audit_report.md).

**Main Float Check**

| quantity | independent | claimed |
|---|---:|---:|
| `n,k` | `7,4` | `7,4` |
| `||P1-1||_inf` | `2.220e-16` | `2.220e-16` |
| `||P^2-P||_inf` | `2.220e-16` | `2.220e-16` |
| `||BL-I||_inf` | `2.220e-16` | `2.220e-16` |
| `delta` | `0.22840025035566297` | `0.22840025035566297` |
| `tau` | `0.4779123877403294` | `0.4779123877403294` |
| `W` | `[0,1,2,3]` | `[0,1,2,3]` |
| hidden top `v` | `4` | `4` |
| `H` | `0.007567078666031271` | `0.007567078666032154` |
| `H/tau` | `0.015833610636899403` | `0.01583361063690125` |
| `sigma_tilde_4` | `0.7768728655109876` | `0.7768728655109876` |
| `sigma_tilde/tau` | `1.625554987566249` | `1.625554987566249` |

All rows are geometrically distinct and all 7 are row vertices. Per-row exposedness margins: rows `0..3` are exposed with `t = 0.9962405162, 0.8115996744, 0.8156449337, 0.8702134918`; rows `4..6` are hidden with `t = 0.0194051101, 0.0179729018, 0.0183872609`. `outside_CW = [4,5,6]`, so sigma includes the self coefficient.

**Hiddenness LP, v=4**

`rho = 1.9116495509613176`, `kappa = 0.11947809693508235`. Far rows are `[0,1,3]` with distances `{0: 2.0435748183, 1: 1.9336320575, 3: 2.0432703924}`.

Primal optimum `t* = 0.01940511010320419`; dual optimum `0.01940511010320389`; dual stationarity residual `3.0e-16`. The LP with added constraint `t >= kappa` is infeasible. Active dual weights:

- `upper_h_le_1 row 0`: `0.01940511010320389`
- `lower_h_ge_0 row 2`: `4.161642162514185`
- `far_h_ge_t row 1`: `0.9724550638506694`
- `far_h_ge_t row 3`: `0.027544936149330616`

**Exact Rational Hardening**

I rationalized `X` and `Q` with continued-fraction denominators <= `10000`, enforced hidden-row sums exactly, and set `B=[I-QX,Q]`. Exact checks:

- `BL = I`: true
- `P^2 = P`: true
- `P1 = 1`: true
- exact `delta = 23123630110489/101241694344000 = 0.2284002678967354`
- exact `sigma_tilde_4 = 77691628979359472983156919443/100005592601676868585769246880 = 0.776872842389984`
- rational `sigma_tilde/tau = 1.625554876766013`
- rational `H/tau = 0.01583325024235046`
- max entry drift from float: `5.188e-7`

Perturbation scale is comfortably below decision margins: `sigma-tau = 0.2989604363`; min visible exposedness gap `t-kappa = 0.6921215541`; min hidden gap `kappa-t = 0.1000734248`; min outside distance to `C_W = 0.0063954188`; min pairwise distance-to-`rho` gap `0.0057265228`.

**Second Saved Instance**

`w16_scale_matrix.json` also verifies floating-only: `delta = 0.22934355220103006`, `tau = 0.47889826915643585`, `W = [0,1,2,3]`, hidden `[4,5,6]`, top `v=4`, `H/tau = 0.015247418318684937`, `sigma_tilde_4 = 0.7534830220899305`, `sigma/tau = 1.5733676035563189`. Its row-1 far distance is only about `4.6e-9` above `rho`, so this second saved scale point is threshold-fragile, unlike the main/rational certificate.

**Context**

`H/tau = 0.0158`, so this does not contradict the recorded “no `sigma_tilde > tau` and `H > 0.1 tau`” frontier and does not enter any floor antecedent with `B >= 0.01584`. The sigma-height-collapse lemma branch `sigma_tilde <= tau` does not apply. The corner value `2(2-sqrt(3)) = 0.5358983849` is far above this instance’s height ratio, and the canonical deficit check is consistent: `||Pg-g||_inf = 8.2e-17` float, `5.9e-17` rational.

Bonus continuation: independent `Q`-rescaling found the family still crosses below `delta <= 0.1`: at `alpha=0.40`, `delta=0.0913601001`, `sigma/tau=1.0280912445`; at `alpha=0.43`, `delta=0.0982121077`, `sigma/tau=1.0659476899`.

Calibrated `P(instance is genuine under the report definitions) = 0.999`. The residual is definition/LP-convention risk, not algebraic idempotence risk.