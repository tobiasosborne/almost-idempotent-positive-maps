VERDICT: CERTIFIED EXACT for MAIN and ROBUST.

The rationalized block instances use B=[I;X], L=[I-QX,Q], with X rows forced to
sum exactly to 1. Thus L B = I, P = B L is exactly idempotent, and P 1 = 1
exactly. Exact rational certificates in verification_report.json certify W={0,1,2,3,4},
hidden vertices {5,6,7}, nonvertices {8,9}, and the antecedent for v=5.

MAIN rationalized: delta=0.2329335240003862, H/tau=0.10019261003238415
by exact height witness, sigma gate by P_55=0.7274084488643412 > tau,
hiddenness dual objective/kappa=0.999877369296419.

ROBUST rationalized: delta=0.23459249106770674, H/tau=0.1000025471673097
by exact height witness, sigma gate by P_55=0.7325554135477605 > tau,
hiddenness dual objective/kappa=0.9977747374212589.

Float recomputation matches the claimant's reported delta, W, H/tau, sigma/tau,
and hiddenness margins for both archived matrices. The main quotient component is
[1,2,3,5,6,7], L=2, Pi/tau=0.00024879427009641934; robust gives
Pi/tau=0.00025236363737045933.

Sensitivity: MAIN kappa-t*=1.4796373616676739e-5, with a local active-witness
entrywise flip upper bound about 6.55e-6. ROBUST kappa-t*=2.69449996533222e-4,
with flip upper bound about 8.49e-5. The exact rational drifts are 1.25e-11
and 1.95e-11 respectively, below these scales.

Context: delta*=(2-sqrt(3))^2=0.07179676972449088, so these deltas are above
the corner scale and do not touch the small-delta regime. Both obey H<=2 delta.
Nine saved candidate/certificate pairs were rechecked in pareto_sample_check.json
with no observed reporting bias.
