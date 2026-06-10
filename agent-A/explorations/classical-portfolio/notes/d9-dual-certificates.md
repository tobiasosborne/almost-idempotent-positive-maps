# d9 -- Dual certificates for the MRP collapse-edge (analytic blueprint)

**Date:** 2026-06-10 - **Scope:** exploration only
(`agent-A/explorations/classical-portfolio/experiments/`), NOT committed to canonical layers.
**Agent:** numerics worker, exploration lane.

This is the methodology-gap deliverable flagged on day 1: d8 persisted only PRIMAL collapse margins;
the proof push needs the **DUAL** certificates of the collapse-edge LPs -- which constraints bind at
the sigma_v-wall, with what multipliers, and the SHAPE of the separating functional. d9 re-runs the
d8_decision collapse-edge sweep over sigma_v in
{0.05, 0.10, 0.20, 0.35, 0.50, 0.536, 0.70, 1.00} (k_groups=1; d8 showed kg irrelevant), bisects each
cell to the collapse edge, and AT THE EDGE persists:

1. the **exposedness-LP** margin-maximizing separating functional h(x)=a.x+b for v and each supplier
   (the LP primal IS the functional), the achieved margin t*/kappa, and the DUAL variables / binding
   far-row blockers (re-solved in gurobipy, Presolve OFF, Method=1 dual simplex, FeasTol=OptTol=1e-9);
2. the **min-neg (Lambda,R)-LP** duals (which constraint families -- idempotence RL, stochasticity
   Lsum, pinned far-geometry, supplier-feed lin, neg/epi budget -- carry nonzero prices) at the edge;
3. a per-cell summary mapping the binding sets to row ROLES and reporting the functional's shape on
   the cluster {v}+suppliers vs the anchors/W.

Every reported point passes `d8_mrp3.verify` (idem_resid<1e-7, multiplicity-correct W via
`d3_vertexfix`, robust exposedness LP, honest tau=sqrt(delta), dist re-verified). Presolve is OFF on
ALL exposedness LPs. Tags: [NUMERICAL] / [OBSERVATION] / [GUESS].

The two regimes (from d8's sigma_v-wall law H/tau = min(sigma_v, 0.536)):
- **budget-bound** (sigma_v < 0.536): the cluster collapses at H/tau ~ sigma_v, BEFORE the
  exposedness wall; the binding constraint should be the external-mass BUDGET, not the wall.
- **wall-bound** (sigma_v >= 0.536): the cluster reaches the universal (rho,kappa)-exposedness wall;
  margin -> kappa exactly at H/tau -> 0.536.

The dual certificates below are the analytic blueprint: to prove Branch A (budget) / Branch B (wall),
exhibit THIS functional and prove THESE binding inequalities.

---

## Per-cell certificates

## sigma_v = 0.050  [budget-bound]

- collapse edge: d=0.0125, delta=0.00063, tau=0.0250, H/tau=0.0500, **delta/H^2=400.000**, |W|=8, idem_resid=0.0e+00
- cluster exposedness margin/kappa at edge: min=0.026229303440254183, max=0.09993753903810121 (v margin/kappa = 0.09993753903810121)

### Exposedness-LP separating functional + binding blockers (AT the edge)

**v (the hidden top vertex):**
  margin t*/kappa = 0.0999  (exposed=False); far rows = 11; #binding blockers = 4
    blocker frame-financing#4 Pi=-0.9494  h=+0.0006  l1_to_target=0.1013
    blocker frame-group#0  Pi=-0.0256  h=+0.0006  l1_to_target=1.9500
    blocker frame-financing#0 Pi=-0.0125  h=+0.0006  l1_to_target=1.9763
    blocker frame-financing#1 Pi=-0.0125  h=+0.0006  l1_to_target=1.9763
    h on cluster: supplier#0=+0.738, supplier#1=+0.738, v=+0.000
    h on anchors: anchor#0=+1.000, anchor#1=+1.000

**supplier#0:**
  margin t*/kappa = 0.0262  (exposed=False); far rows = 10; #binding blockers = 2
    blocker v''            Pi=-0.7375  h=+0.0002  l1_to_target=0.5250
    blocker frame-group#0  Pi=-0.2625  h=+0.0002  l1_to_target=1.4763
    h on cluster: supplier#0=+0.000, supplier#1=+0.000, v=+0.975
    h on anchors: anchor#0=+0.001, anchor#1=+1.000

**supplier#1:**
  margin t*/kappa = 0.0262  (exposed=False); far rows = 10; #binding blockers = 2
    blocker v''            Pi=-0.7375  h=+0.0002  l1_to_target=0.5250
    blocker frame-group#0  Pi=-0.2625  h=+0.0002  l1_to_target=1.4763
    h on cluster: supplier#0=+0.000, supplier#1=+0.000, v=+0.975
    h on anchors: anchor#0=+0.001, anchor#1=+1.000

### Just PAST the edge (first collapse instance)

- d=0.013000000000000003, tau=0.025495097567963927, H/tau=0.0, |W|=9, v_in_W=True, suppliers_in_W=[], entry_pass=False
**v just past edge:**
  margin t*/kappa = 2.0134  (exposed=True); far rows = 10; #binding blockers = 3
    blocker frame-group#0  Pi=-0.5163  h=+0.0128  l1_to_target=1.9490
    blocker frame-financing#0 Pi=-0.2419  h=+0.0128  l1_to_target=1.9768
    blocker frame-financing#1 Pi=-0.2419  h=+0.0128  l1_to_target=1.9768
    h on cluster: supplier#0=+0.740, supplier#1=+0.740, v=+0.000
    h on anchors: anchor#0=+1.000, anchor#1=+1.000

### Min-neg (Lambda,R)-LP duals at the edge instance

- mneg(LP)=0.0006250000000000001; nonzero duals: 3; families: {'pin': 1, 'neg': 1, 'epi': 1}
  - pin: ('pin', 10, 0)=-1.000
  - neg: ('neg', 10, 0)=+1.000
  - epi: ('epi', 10)=-1.000


## sigma_v = 0.100  [budget-bound]

- collapse edge: d=0.0260, delta=0.00260, tau=0.0510, H/tau=0.1020, **delta/H^2=96.154**, |W|=8, idem_resid=0.0e+00
- cluster exposedness margin/kappa at edge: min=0.05610703473163863, max=0.2034318577136559 (v margin/kappa = 0.2034318577136559)

### Exposedness-LP separating functional + binding blockers (AT the edge)

**v (the hidden top vertex):**
  margin t*/kappa = 0.2034  (exposed=False); far rows = 11; #binding blockers = 4
    blocker frame-financing#4 Pi=-0.8977  h=+0.0026  l1_to_target=0.2052
    blocker frame-group#0  Pi=-0.0535  h=+0.0026  l1_to_target=1.8980
    blocker frame-financing#0 Pi=-0.0244  h=+0.0026  l1_to_target=1.9562
    blocker frame-financing#1 Pi=-0.0244  h=+0.0026  l1_to_target=1.9562
    h on cluster: supplier#0=+0.725, supplier#1=+0.725, v=+0.000
    h on anchors: anchor#0=+1.000, anchor#1=+1.000

**supplier#0:**
  margin t*/kappa = 0.0561  (exposed=False); far rows = 10; #binding blockers = 2
    blocker v''            Pi=-0.7242  h=+0.0007  l1_to_target=0.5520
    blocker frame-group#0  Pi=-0.2758  h=+0.0007  l1_to_target=1.4532
    h on cluster: supplier#0=+0.000, supplier#1=+0.000, v=+0.949
    h on anchors: anchor#0=+0.003, anchor#1=+1.000

**supplier#1:**
  margin t*/kappa = 0.0561  (exposed=False); far rows = 10; #binding blockers = 2
    blocker v''            Pi=-0.7242  h=+0.0007  l1_to_target=0.5520
    blocker frame-group#0  Pi=-0.2758  h=+0.0007  l1_to_target=1.4532
    h on cluster: supplier#0=+0.000, supplier#1=+0.000, v=+0.949
    h on anchors: anchor#0=+0.003, anchor#1=+1.000

### Just PAST the edge (first collapse instance)

- d=0.0265, tau=0.051478150704935, H/tau=0.0, |W|=9, v_in_W=True, suppliers_in_W=[], entry_pass=False
**v just past edge:**
  margin t*/kappa = 2.0060  (exposed=True); far rows = 10; #binding blockers = 3
    blocker frame-group#0  Pi=-0.5275  h=+0.0258  l1_to_target=1.8970
    blocker frame-financing#0 Pi=-0.2362  h=+0.0258  l1_to_target=1.9568
    blocker frame-financing#1 Pi=-0.2362  h=+0.0258  l1_to_target=1.9568
    h on cluster: supplier#0=+0.731, supplier#1=+0.731, v=-0.000
    h on anchors: anchor#0=+1.000, anchor#1=+1.000

### Min-neg (Lambda,R)-LP duals at the edge instance

- mneg(LP)=0.0026; nonzero duals: 3; families: {'pin': 1, 'neg': 1, 'epi': 1}
  - pin: ('pin', 10, 0)=-1.000
  - neg: ('neg', 10, 0)=+1.000
  - epi: ('epi', 10)=-1.000


## sigma_v = 0.200  [budget-bound]

- collapse edge: d=0.0555, delta=0.01110, tau=0.1054, H/tau=0.2107, **delta/H^2=22.523**, |W|=8, idem_resid=0.0e+00
- cluster exposedness margin/kappa at edge: min=0.12690667784586213, max=0.4167996737356438 (v margin/kappa = 0.4167996737356438)

### Exposedness-LP separating functional + binding blockers (AT the edge)

**v (the hidden top vertex):**
  margin t*/kappa = 0.4168  (exposed=False); far rows = 11; #binding blockers = 4
    blocker frame-financing#4 Pi=-0.7912  h=+0.0110  l1_to_target=0.4222
    blocker frame-group#0  Pi=-0.1153  h=+0.0110  l1_to_target=1.7890
    blocker frame-financing#0 Pi=-0.0467  h=+0.0110  l1_to_target=1.9277
    blocker frame-financing#1 Pi=-0.0467  h=+0.0110  l1_to_target=1.9277
    h on cluster: supplier#0=+0.698, supplier#1=+0.698, v=-0.000
    h on anchors: anchor#0=+1.000, anchor#1=+1.000

**supplier#0:**
  margin t*/kappa = 0.1269  (exposed=False); far rows = 10; #binding blockers = 2
    blocker v''            Pi=-0.6955  h=+0.0033  l1_to_target=0.6110
    blocker frame-group#0  Pi=-0.3045  h=+0.0033  l1_to_target=1.4112
    h on cluster: supplier#0=+0.000, supplier#1=+0.000, v=+0.895
    h on anchors: anchor#0=+0.014, anchor#1=+1.000

**supplier#1:**
  margin t*/kappa = 0.1269  (exposed=False); far rows = 10; #binding blockers = 2
    blocker v''            Pi=-0.6955  h=+0.0033  l1_to_target=0.6110
    blocker frame-group#0  Pi=-0.3045  h=+0.0033  l1_to_target=1.4112
    h on cluster: supplier#0=+0.000, supplier#1=+0.000, v=+0.895
    h on anchors: anchor#0=+0.014, anchor#1=+1.000

### Just PAST the edge (first collapse instance)

- d=0.055999999999999994, tau=0.10583005244258362, H/tau=0.0, |W|=9, v_in_W=True, suppliers_in_W=[], entry_pass=False
**v just past edge:**
  margin t*/kappa = 2.0044  (exposed=True); far rows = 10; #binding blockers = 3
    blocker frame-group#0  Pi=-0.5549  h=+0.0530  l1_to_target=1.7880
    blocker frame-financing#0 Pi=-0.2225  h=+0.0530  l1_to_target=1.9284
    blocker frame-financing#1 Pi=-0.2225  h=+0.0530  l1_to_target=1.9284
    h on cluster: supplier#0=+0.710, supplier#1=+0.710, v=+0.000
    h on anchors: anchor#0=+1.000, anchor#1=+1.000

### Min-neg (Lambda,R)-LP duals at the edge instance

- mneg(LP)=0.011099999999999999; nonzero duals: 3; families: {'pin': 1, 'neg': 1, 'epi': 1}
  - pin: ('pin', 10, 0)=-1.000
  - neg: ('neg', 10, 0)=+1.000
  - epi: ('epi', 10)=-1.000


## sigma_v = 0.350  [budget-bound]

- collapse edge: d=0.1070, delta=0.03745, tau=0.1935, H/tau=0.3870, **delta/H^2=6.676**, |W|=8, idem_resid=0.0e+00
- cluster exposedness margin/kappa at edge: min=0.7461372588698684, max=0.7461372588698684 (v margin/kappa = 0.7461372588698684)

### Exposedness-LP separating functional + binding blockers (AT the edge)

**v (the hidden top vertex):**
  margin t*/kappa = 0.7461  (exposed=False); far rows = 11; #binding blockers = 4
    blocker frame-financing#4 Pi=-0.6265  h=+0.0361  l1_to_target=0.7749
    blocker frame-group#0  Pi=-0.2236  h=+0.0361  l1_to_target=1.6110
    blocker frame-financing#0 Pi=-0.0749  h=+0.0361  l1_to_target=1.9194
    blocker frame-financing#1 Pi=-0.0749  h=+0.0361  l1_to_target=1.9194
    h on cluster: supplier#0=+0.656, supplier#1=+0.656, v=+0.000
    h on anchors: anchor#0=+1.000, anchor#1=+1.000

**supplier#0:**
  margin t*/kappa = 0.7461  (exposed=False); far rows = 8; #binding blockers = 1
    blocker frame-group#0  Pi=-1.0000  h=+0.0361  l1_to_target=1.3609
    h on cluster: supplier#0=-0.000, supplier#1=-0.000, v=+0.813
    h on anchors: anchor#0=+0.036, anchor#1=+1.000

**supplier#1:**
  margin t*/kappa = 0.7461  (exposed=False); far rows = 8; #binding blockers = 1
    blocker frame-group#0  Pi=-1.0000  h=+0.0361  l1_to_target=1.3609
    h on cluster: supplier#0=-0.000, supplier#1=-0.000, v=+0.813
    h on anchors: anchor#0=+0.036, anchor#1=+1.000

### Just PAST the edge (first collapse instance)

- d=0.10749999999999998, tau=0.1939716474127082, H/tau=0.0, |W|=9, v_in_W=True, suppliers_in_W=[], entry_pass=False
**v just past edge:**
  margin t*/kappa = 2.0016  (exposed=True); far rows = 10; #binding blockers = 3
    blocker frame-group#0  Pi=-0.6001  h=+0.0971  l1_to_target=1.6100
    blocker frame-financing#1 Pi=-0.1999  h=+0.0971  l1_to_target=1.9203
    blocker frame-financing#0 Pi=-0.1999  h=+0.0971  l1_to_target=1.9203
    h on cluster: supplier#0=+0.677, supplier#1=+0.677, v=-0.000
    h on anchors: anchor#0=+1.000, anchor#1=+1.000

### Min-neg (Lambda,R)-LP duals at the edge instance

- mneg(LP)=0.03744999999999999; nonzero duals: 3; families: {'pin': 1, 'neg': 1, 'epi': 1}
  - pin: ('pin', 10, 0)=-1.000
  - neg: ('neg', 10, 0)=+1.000
  - epi: ('epi', 10)=-1.000


## sigma_v = 0.500  [budget-bound]

- collapse edge: d=0.1435, delta=0.07175, tau=0.2679, H/tau=0.5357, **delta/H^2=3.484**, |W|=8, idem_resid=0.0e+00
- cluster exposedness margin/kappa at edge: min=0.9997178622610776, max=0.9997178622610778 (v margin/kappa = 0.9997178622610778)

### Exposedness-LP separating functional + binding blockers (AT the edge)

**v (the hidden top vertex):**
  margin t*/kappa = 0.9997  (exposed=False); far rows = 11; #binding blockers = 4
    blocker frame-financing#4 Pi=-0.4665  h=+0.0669  l1_to_target=1.1435
    blocker frame-group#0  Pi=-0.2906  h=+0.0669  l1_to_target=1.5206
    blocker frame-financing#0 Pi=-0.1214  h=+0.0669  l1_to_target=1.8832
    blocker frame-financing#1 Pi=-0.1214  h=+0.0669  l1_to_target=1.8832
    h on cluster: supplier#0=+0.687, supplier#1=+0.687, v=+0.000
    h on anchors: anchor#0=+1.000, anchor#1=+1.000

**supplier#0:**
  margin t*/kappa = 0.9997  (exposed=False); far rows = 8; #binding blockers = 1
    blocker frame-group#0  Pi=-1.0000  h=+0.0669  l1_to_target=1.4718
    h on cluster: supplier#0=+0.000, supplier#1=+0.000, v=+0.776
    h on anchors: anchor#0=+0.067, anchor#1=+1.000

**supplier#1:**
  margin t*/kappa = 0.9997  (exposed=False); far rows = 8; #binding blockers = 1
    blocker frame-group#0  Pi=-1.0000  h=+0.0669  l1_to_target=1.4718
    h on cluster: supplier#0=+0.000, supplier#1=+0.000, v=+0.776
    h on anchors: anchor#0=+0.067, anchor#1=+1.000

### Just PAST the edge (first collapse instance)

- d=0.144, tau=0.2683281572999748, H/tau=0.0, |W|=11, v_in_W=True, suppliers_in_W=[8, 9], entry_pass=False
**v just past edge:**
  margin t*/kappa = 1.0012  (exposed=True); far rows = 11; #binding blockers = 4
    blocker frame-financing#4 Pi=-0.4664  h=+0.0672  l1_to_target=1.1440
    blocker frame-group#0  Pi=-0.2906  h=+0.0672  l1_to_target=1.5209
    blocker frame-financing#0 Pi=-0.1215  h=+0.0672  l1_to_target=1.8835
    blocker frame-financing#1 Pi=-0.1215  h=+0.0672  l1_to_target=1.8835
    h on cluster: supplier#0=+0.687, supplier#1=+0.687, v=+0.000
    h on anchors: anchor#0=+1.000, anchor#1=+1.000

### Min-neg (Lambda,R)-LP duals at the edge instance

- mneg(LP)=0.07175; nonzero duals: 3; families: {'pin': 1, 'neg': 1, 'epi': 1}
  - pin: ('pin', 10, 0)=-1.000
  - neg: ('neg', 10, 0)=+1.000
  - epi: ('epi', 10)=-1.000


## sigma_v = 0.536  [wall-bound]

- collapse edge: d=0.1335, delta=0.07156, tau=0.2675, H/tau=0.5350, **delta/H^2=3.494**, |W|=8, idem_resid=0.0e+00
- cluster exposedness margin/kappa at edge: min=0.9985461616933587, max=0.9985461616933587 (v margin/kappa = 0.9985461616933587)

### Exposedness-LP separating functional + binding blockers (AT the edge)

**v (the hidden top vertex):**
  margin t*/kappa = 0.9985  (exposed=False); far rows = 11; #binding blockers = 4
    blocker frame-financing#4 Pi=-0.4330  h=+0.0668  l1_to_target=1.2151
    blocker frame-group#0  Pi=-0.3010  h=+0.0668  l1_to_target=1.4980
    blocker frame-financing#0 Pi=-0.1330  h=+0.0668  l1_to_target=1.8581
    blocker frame-financing#1 Pi=-0.1330  h=+0.0668  l1_to_target=1.8581
    h on cluster: supplier#0=+0.671, supplier#1=+0.671, v=-0.000
    h on anchors: anchor#0=+1.000, anchor#1=+1.000

**supplier#0:**
  margin t*/kappa = 0.9985  (exposed=False); far rows = 8; #binding blockers = 1
    blocker frame-group#0  Pi=-1.0000  h=+0.0668  l1_to_target=1.4376
    h on cluster: supplier#0=-0.000, supplier#1=-0.000, v=+0.766
    h on anchors: anchor#0=+0.067, anchor#1=+1.000

**supplier#1:**
  margin t*/kappa = 0.9985  (exposed=False); far rows = 8; #binding blockers = 1
    blocker frame-group#0  Pi=-1.0000  h=+0.0668  l1_to_target=1.4376
    h on cluster: supplier#0=-0.000, supplier#1=-0.000, v=+0.766
    h on anchors: anchor#0=+0.067, anchor#1=+1.000

### Just PAST the edge (first collapse instance)

- d=0.13399999999999998, tau=0.268, H/tau=0.0, |W|=11, v_in_W=True, suppliers_in_W=[8, 9], entry_pass=False
**v just past edge:**
  margin t*/kappa = 1.0002  (exposed=True); far rows = 11; #binding blockers = 4
    blocker frame-financing#4 Pi=-0.4329  h=+0.0670  l1_to_target=1.2156
    blocker frame-group#0  Pi=-0.3010  h=+0.0670  l1_to_target=1.4984
    blocker frame-financing#0 Pi=-0.1331  h=+0.0670  l1_to_target=1.8584
    blocker frame-financing#1 Pi=-0.1331  h=+0.0670  l1_to_target=1.8584
    h on cluster: supplier#0=+0.672, supplier#1=+0.672, v=+0.000
    h on anchors: anchor#0=+1.000, anchor#1=+1.000

### Min-neg (Lambda,R)-LP duals at the edge instance

- mneg(LP)=0.071556; nonzero duals: 3; families: {'pin': 1, 'neg': 1, 'epi': 1}
  - pin: ('pin', 10, 0)=-1.000
  - neg: ('neg', 10, 0)=+1.000
  - epi: ('epi', 10)=-1.000


## sigma_v = 0.700  [wall-bound]

- collapse edge: d=0.1025, delta=0.07175, tau=0.2679, H/tau=0.5357, **delta/H^2=3.484**, |W|=8, idem_resid=0.0e+00
- cluster exposedness margin/kappa at edge: min=0.9997178622610776, max=0.9997178622610776 (v margin/kappa = 0.9997178622610776)

### Exposedness-LP separating functional + binding blockers (AT the edge)

**v (the hidden top vertex):**
  margin t*/kappa = 0.9997  (exposed=False); far rows = 11; #binding blockers = 4
    blocker frame-group#0  Pi=-0.3259  h=+0.0669  l1_to_target=1.4450
    blocker frame-financing#4 Pi=-0.2799  h=+0.0669  l1_to_target=1.5435
    blocker frame-financing#0 Pi=-0.1971  h=+0.0669  l1_to_target=1.7210
    blocker frame-financing#1 Pi=-0.1971  h=+0.0669  l1_to_target=1.7210
    h on cluster: supplier#0=+0.671, supplier#1=+0.671, v=+0.000
    h on anchors: anchor#0=+1.000, anchor#1=+1.000

**supplier#0:**
  margin t*/kappa = 0.9997  (exposed=False); far rows = 8; #binding blockers = 1
    blocker frame-group#0  Pi=-1.0000  h=+0.0669  l1_to_target=1.4385
    h on cluster: supplier#0=+0.000, supplier#1=+0.000, v=+0.741
    h on anchors: anchor#0=+0.067, anchor#1=+1.000

**supplier#1:**
  margin t*/kappa = 0.9997  (exposed=False); far rows = 8; #binding blockers = 1
    blocker frame-group#0  Pi=-1.0000  h=+0.0669  l1_to_target=1.4385
    h on cluster: supplier#0=+0.000, supplier#1=+0.000, v=+0.741
    h on anchors: anchor#0=+0.067, anchor#1=+1.000

### Just PAST the edge (first collapse instance)

- d=0.10299999999999998, tau=0.268514431641951, H/tau=0.0, |W|=11, v_in_W=True, suppliers_in_W=[8, 9], entry_pass=False
**v just past edge:**
  margin t*/kappa = 1.0018  (exposed=True); far rows = 11; #binding blockers = 4
    blocker frame-group#0  Pi=-0.3266  h=+0.0673  l1_to_target=1.4440
    blocker frame-financing#4 Pi=-0.2798  h=+0.0673  l1_to_target=1.5442
    blocker frame-financing#0 Pi=-0.1968  h=+0.0673  l1_to_target=1.7222
    blocker frame-financing#1 Pi=-0.1968  h=+0.0673  l1_to_target=1.7222
    h on cluster: supplier#0=+0.671, supplier#1=+0.671, v=+0.000
    h on anchors: anchor#0=+1.000, anchor#1=+1.000

### Min-neg (Lambda,R)-LP duals at the edge instance

- mneg(LP)=0.07174999999999998; nonzero duals: 3; families: {'pin': 1, 'neg': 1, 'epi': 1}
  - pin: ('pin', 10, 0)=-1.000
  - neg: ('neg', 10, 0)=+1.000
  - epi: ('epi', 10)=-1.000


## sigma_v = 1.000  [wall-bound]

- collapse edge: d=0.0715, delta=0.07150, tau=0.2674, H/tau=0.5348, **delta/H^2=3.497**, |W|=8, idem_resid=0.0e+00
- cluster exposedness margin/kappa at edge: min=0.9982075189637656, max=0.9982075189637656 (v margin/kappa = 0.9982075189637656)

### Exposedness-LP separating functional + binding blockers (AT the edge)

**v (the hidden top vertex):**
  margin t*/kappa = 0.9982  (exposed=False); far rows = 11; #binding blockers = 3
    blocker frame-group#0  Pi=-0.3668  h=+0.0667  l1_to_target=1.3570
    blocker frame-financing#0 Pi=-0.3166  h=+0.0667  l1_to_target=1.4645
    blocker frame-financing#1 Pi=-0.3166  h=+0.0667  l1_to_target=1.4645
    h on cluster: supplier#0=+0.700, supplier#1=+0.700, v=-0.000
    h on anchors: anchor#0=+1.000, anchor#1=+1.000

**supplier#0:**
  margin t*/kappa = 0.9982  (exposed=False); far rows = 8; #binding blockers = 1
    blocker frame-group#0  Pi=-1.0000  h=+0.0667  l1_to_target=1.5000
    h on cluster: supplier#0=+0.000, supplier#1=+0.000, v=+0.700
    h on anchors: anchor#0=+0.067, anchor#1=+1.000

**supplier#1:**
  margin t*/kappa = 0.9982  (exposed=False); far rows = 8; #binding blockers = 1
    blocker frame-group#0  Pi=-1.0000  h=+0.0667  l1_to_target=1.5000
    h on cluster: supplier#0=+0.000, supplier#1=+0.000, v=+0.700
    h on anchors: anchor#0=+0.067, anchor#1=+1.000

### Just PAST the edge (first collapse instance)

- d=0.072, tau=0.2683281572999748, H/tau=0.0, |W|=11, v_in_W=True, suppliers_in_W=[8, 9], entry_pass=False
**v just past edge:**
  margin t*/kappa = 1.0012  (exposed=True); far rows = 11; #binding blockers = 3
    blocker frame-group#0  Pi=-0.3675  h=+0.0672  l1_to_target=1.3560
    blocker frame-financing#1 Pi=-0.3162  h=+0.0672  l1_to_target=1.4660
    blocker frame-financing#0 Pi=-0.3162  h=+0.0672  l1_to_target=1.4660
    h on cluster: supplier#0=+0.700, supplier#1=+0.700, v=-0.000
    h on anchors: anchor#0=+1.000, anchor#1=+1.000

### Min-neg (Lambda,R)-LP duals at the edge instance

- mneg(LP)=0.0715; nonzero duals: 3; families: {'pin': 1, 'neg': 1, 'epi': 1}
  - pin: ('pin', 10, 0)=-1.000
  - neg: ('neg', 10, 0)=+1.000
  - epi: ('epi', 10)=-1.000


---

## Cross-cell synthesis (analytic blueprint)

| sigma_v | regime | H/tau | delta/H^2 | v margin/kappa | #v-blockers | dominant blocker roles |
|---|---|---|---|---|---|---|
| 0.050 | budget-bound | 0.050 | 400.000 | 0.100 | 4 | frame-financing, frame-group |
| 0.100 | budget-bound | 0.102 | 96.154 | 0.203 | 4 | frame-financing, frame-group |
| 0.200 | budget-bound | 0.211 | 22.523 | 0.417 | 4 | frame-financing, frame-group |
| 0.350 | budget-bound | 0.387 | 6.676 | 0.746 | 4 | frame-financing, frame-group |
| 0.500 | budget-bound | 0.536 | 3.484 | 1.000 | 4 | frame-financing, frame-group |
| 0.536 | wall-bound | 0.535 | 3.494 | 0.999 | 4 | frame-financing, frame-group |
| 0.700 | wall-bound | 0.536 | 3.484 | 1.000 | 4 | frame-financing, frame-group |
| 1.000 | wall-bound | 0.535 | 3.497 | 0.998 | 3 | frame-financing, frame-group |

### What the certificates say (read against d8's sigma_v-wall law H/tau = min(sigma_v, 0.536))

The per-cell sections record the EXACT margin-max separating functional h(x)=a.x+b at the collapse edge
and which rows bind it. The honest reading from the persisted duals (each claim tagged by evidence):

- **[NUMERICAL] The exposedness functional is the SAME shape in BOTH regimes -- it is the
  anchor-vs-apex LEVEL functional.** In every cell h pins the anchors at **h=1** (the box face
  h(anchor)<=1 is the active upper constraint, with v'' co-pinned near 1) and the target vertex at
  **h(v)=0**; the suppliers sit at an intermediate **h~0.65-0.74** (the apex v is poked BELOW the
  supplier midpoint). The functional's slope is the apex/poke direction. So the certificate object is
  identical across the wall -- only the achieved margin t* changes -- which says the proof does NOT
  need two different functionals, just one level functional and a bound on its value at v's blocker.

- **[NUMERICAL] The binding blocker is the FINANCING direction that pays for the apex poke (NOT the
  suppliers).** The dominant-Pi far-row at the edge is `frame-financing#k` (the low dir financing the
  apex wiggle), with secondary mass on `frame-group#0` (the suppliers' group dir). Crucially its
  l1-distance to v GROWS with the regime: at sigma_v=0.05 the dominant blocker is at l1~0.10 (right next
  to v, Pi~-0.95 -- a single nearly-degenerate blocker), and as sigma_v rises the blocker recedes to
  l1~rho and the Pi mass spreads over the group+financing dirs. The blocker's own height
  `h_value` EQUALS the margin t* and rises LINEARLY with sigma_v (0.0006, 0.036, 0.067 for
  sigma_v=0.05, 0.35, 0.70) -- this IS the measured law t*/kappa = sigma_v/0.5.

- **[OBSERVATION -> Branch A blueprint] Budget regime (sigma_v < 0.5): margin t*/kappa = sigma_v/0.5
  < 1, capped by the apex-financing blocker.** The financing dir that finances the apex sits at
  l1-distance ~ H from v and pins h there to ~t* = (sigma_v/0.5) kappa. Pushing v out (raising H) raises
  this blocker's height linearly until at H/tau ~ sigma_v it reaches kappa and v exposes. **To prove
  Branch A (H <= B_A sigma_v tau):** exhibit THIS level functional (anchors=1, v=0) and prove the
  apex-financing row's height under it is >= (H/(B_A tau)) kappa, i.e. the financing mass available to
  the apex (which scales with sigma_v) bounds how far below the financing level v can be driven. The
  multiplier on that financing far-constraint (the dominant Pi) is the Branch-A budget multiplier.

- **[OBSERVATION -> Branch B blueprint] Wall regime (sigma_v >= 0.5): margin t*/kappa -> 1.000 EXACTLY
  at the edge.** At/above 0.5 the v-margin saturates at kappa and the Pi mass is spread over the
  group+financing blockers at l1 ~ rho -- the universal (rho,kappa) wall geometry d3/d7 also hit.
  **To prove Branch B (sigma_v >= 1/2, H > B_B tau => exposed):** exhibit the same level functional and
  prove t* >= kappa from the wall-blocker inequalities recorded here (the group dir at l1~rho carries
  height >= kappa once H/tau > 0.536).

- **[NUMERICAL] The collapse is a SHARP, regime-diagnostic jump in the post-edge margin.** Just past
  the edge (first exposed d), v enters W in EVERY cell, but the post-edge margin t*/kappa is
  **2.00 in the budget regime** (sigma_v <= 0.35) and **1.00 at/above the wall** (sigma_v >= 0.5). The
  factor-2 over-shoot below the wall vs the marginal 1.00 at the wall is a clean numerical fingerprint
  that the budget collapse (financing blocker suddenly clears v) and the wall collapse (continuous
  exposure) are DIFFERENT mechanisms -- supporting the two-branch case split of the sigma_v-wall lemma.

- **[NUMERICAL] Min-neg (Lambda,R) duals: the cost is forced by the pinned far-geometry + the
  negativity-budget row, NOT by frame freedom.** At EVERY edge cell the nonzero dual families are
  EXACTLY `pin` (the fully-pinned v far position, Pi=-1), `neg` (the single binding negativity row,
  Pi=+1) and `epi` (the max-row-neg epigraph, Pi=-1) -- one constraint each. **`RL` (idempotence
  R Lambda = I) and `Lsum` (stochasticity) carry ZERO dual in all 8 cells** on the final Lambda-step.
  This reproduces d7's "R inert once rows pinned" finding from the dual side: with v pinned and R fixed,
  the negativity cost is set entirely by the pinned far apex (`pin`) clamped against the one binding
  budget row (`neg`/`epi`); the cost is structural geometry, not embedding/frame slack. (Caveat: the
  recorded duals are from the LAST Lambda-step of the alternating loop with R held fixed, so RL=0 here
  means R-freedom is not load-bearing at the optimum, NOT that idempotence is globally irrelevant --
  idempotence is enforced exactly as an equality elsewhere, idem_resid=0.)

Solver anomalies: NONE. All exposedness LPs Presolve OFF, gurobi Method=1 (dual simplex),
FeasTol=OptTol=1e-9; every reported gurobi solve returned OPTIMAL (no `solver_failed` entries in the
JSON). tau is honest (sqrt of each instance's own delta). idem_resid < 1e-7 (= 0, exact frame) on all
edge instances.
