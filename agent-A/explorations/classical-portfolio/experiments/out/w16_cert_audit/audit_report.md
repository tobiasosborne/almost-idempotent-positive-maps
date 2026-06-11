# w16 independent certification audit

VERDICT: CERTIFIED (exact rational)

## Floating best instance

| quantity | independent | claimed | diff |
|---|---:|---:|---:|
| delta | 0.22840025035566297 | 0.22840025035566297 | 0 |
| tau | 0.4779123877403294 | 0.4779123877403294 | 0 |
| sigma_tilde | 0.77687286551098755 | 0.77687286551098755 | 0 |
| sigma_tilde_over_tau | 1.6255549875662489 | 1.6255549875662489 | 0 |
| H | 0.0075670786660312706 | 0.0075670786660321536 | -8.8297424927219481e-16 |
| H_over_tau | 0.015833610636899403 | 0.015833610636901248 | -1.8457457784393227e-15 |
| W | [0, 1, 2, 3] | [0, 1, 2, 3] | |

row_sum_resid = 2.220e-16, idempotence_resid = 2.220e-16
duplicate row groups = [[0], [1], [2], [3], [4], [5], [6]]
row vertices = ['0', '1', '2', '3', '4', '5', '6']
hidden vertices = [4, 5, 6]; outside_CW = [4, 5, 6]

## Hiddenness LP for v=4
rho = 1.9116495509613176, kappa = 0.11947809693508235
far rows = [0, 1, 3]; far distances = {'0': 2.043574818280074, '1': 1.933632057531571, '3': 2.0432703923894624}
primal t* = 0.019405110103204191; kappa - t* = 0.10007298683187815
dual objective = 0.01940511010320389; stationarity_inf = 3.010e-16
t >= kappa feasibility status = 2 (The problem is infeasible. (HiGHS Status 8: model_status is Infeasible; primal_status is Infeasible))
active dual weights:
- upper_h_le_1 row 0: 0.01940511010320389
- lower_h_ge_0 row 2: 4.1616421625141848
- far_h_ge_t row 1: 0.97245506385066938
- far_h_ge_t row 3: 0.027544936149330616

## Exact rational hardening

rational instance = /tmp/codex-sigma-wall/w16_cert_audit/w16_best_rational_instance.json
denominator limit = 10000
BL=I exactly: True; P^2=P exactly: True; P1=1 exactly: True
max |P_float-P_rat|_inf = 5.188e-07
delta_rat = 0.2284002678967354; tau_rat = 0.47791240609209484; sigma_rat = 0.776872842389984; sigma/tau = 1.6255548767660131; H/tau = 0.015833250242350459
exact delta fraction = 23123630110489/101241694344000
exact sigma fraction = 77691628979359472983156919443/100005592601676868585769246880

## Perturbation scale

- delta_lipschitz_bound_for_entry_eps: 3.6315293460778553e-06
- tau_first_order_bound_for_entry_eps: 3.7993671013617199e-06
- fixed_outside_support_sigma_bound: 1.5563697197476523e-06
- height_conv_bound: 2.2975204284928982e-06
- sigma_minus_tau: 0.29896043629788915
- min_visible_t_minus_kappa: 0.69212155414135745
- min_hidden_kappa_minus_t: 0.1000734248062345
- min_outside_distance_to_CW: 0.0063954188354189995
- min_abs_l1_distance_minus_rho: 0.0057265228293432724

## Second saved scale instance

delta = 0.22934355220103006, tau = 0.47889826915643585, sigma_tilde_v4 = 0.75348302208993045, sigma/tau = 1.5733676035563189, H/tau = 0.015247418318684937, W = [0, 1, 2, 3], hidden = [4, 5, 6]
row_sum_resid = 2.220e-16, idempotence_resid = 2.220e-16

## Context

H/tau best = 0.015833610636899403; below 0.1*tau record threshold: True
sigma-height-collapse branch applies: False
corner H/tau = 0.53589838486224561; best H/tau below corner: True
linear-law delta >= H/2: True

continuation probe:

| alpha | delta | sigma/tau | H/tau | W | v4 crosses |
|---:|---:|---:|---:|---|---|
| 0.25 | 0.0571001 | 0.812777 | 0.0316045 | [0, 1, 2, 3] | False |
| 0.35 | 0.0799401 | 0.961691 | 0.0267175 | [0, 1, 2, 3] | False |
| 0.40 | 0.0913601 | 1.02809 | 0.0249952 | [0, 1, 2, 3] | True |
| 0.43 | 0.0982121 | 1.06595 | 0.0241094 | [0, 1, 2, 3] | True |
| 0.45 | 0.10278 | 1.09046 | 0.0235688 | [0, 1, 2, 3] | True |
| 0.50 | 0.1142 | 1.14944 | 0.0223622 | [0, 1, 2, 3] | True |
| 0.60 | 0.13704 | 1.25915 | 0.0204192 | [0, 1, 2, 3] | True |
| 0.75 | 0.1713 | 1.40777 | 0.0182707 | [0, 1, 2, 3] | True |
| 0.90 | 0.20556 | 1.54214 | 0.0166855 | [0, 1, 2, 3] | True |
| 1.00 | 0.2284 | 1.62555 | 0.0158336 | [0, 1, 2, 3] | True |
