VERDICT: BARRIER CROSSED.

Best verified crossed instance found here:

```text
n = 7, k = 4
delta = 0.22840025035566297
tau = sqrt(delta) = 0.4779123877403294
sigma_tilde = 0.7768728655109876
sigma_tilde/tau = 1.625554987566249
delta/sigma_tilde^2 = 0.37843968308661874
W = [0, 1, 2, 3]
hidden top vertex v = 4
H = 0.0075670786660321536
H/tau = 0.01583361063690125
P_vv = 0.7665718403047566
nu_v = 0.006256602977531618
```

Saved certificate files:

```text
w16_best_matrix.json
w16_best_matrix.txt
w16_best_factorization.json
w16_best_certificate.json
w16_results.json
w16_frontier.json
w16_nlopt_search.py
w15_verifier_reuse.py
```

Disk reverify:

```text
R Lambda - I max residual = 2.220446049250313e-16
Lambda R - P max residual = 0.0
row-sum residual = 2.220446049250313e-16
idempotence residual = 2.220446049250313e-16
```

Hiddenness LP certificate for v=4:

```text
rho = 1.9116495509613176
kappa = 0.11947809693508235
t* = 0.01940511010320419
t*/kappa = 0.1624156276421764
far rows = [0, 1, 3]
HiGHS status = optimal
```

Active LP constraints:

```text
h(row 0) <= 1
h(row 2) >= 0
h(row 4) >= 0
t <= h(row 1)
t <= h(row 3)
```

The reproducible one-parameter warm-start scale family already crosses:

```text
scale = 3.7655323442775135
delta/sigma_tilde^2 = 0.4039611434494771
sigma_tilde/tau = 1.5733676035563189
```

Its active boundary is not the delta <= 0.25 budget.  The target remains hidden until
scale about 3.765532370010934, where row 1 hits the rho-distance threshold and leaves the
far set in the target exposedness LP; immediately after that v=4 enters W and the top
hidden vertex changes.  Just before the boundary, hiddenness margin itself is slack:
t*/kappa about 0.151 in the scale-family certificate.

Small per-shape frontier from this run:

```text
(n,k)=(7,4): crossed; best delta/sigma_tilde^2 = 0.37843968308661874
(n,k)=(12,4): PASS examples, but sigma_tilde/tau = 0.0041638519794276185
(n,k)=(6,3), (8,4), (10,4): no PASS hidden candidate in the small random sample
```

Calibration:

```text
P(hidden => sigma_tilde <= sqrt(delta) is true) = 0.01
```

That residual 0.01 is only tolerance/implementation caution; under the recorded verifier
conventions, the saved instance is a direct numerical refutation of the C0=1 barrier.

Most informative next numerical experiment:

Rationalize or interval-certify the saved factorization, then continue the active-set
system at the row-1 rho-threshold to maximize sigma_tilde/tau while preserving hiddenness.
