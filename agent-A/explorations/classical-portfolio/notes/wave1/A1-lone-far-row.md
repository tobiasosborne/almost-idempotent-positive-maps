VERDICT: CONFIRMED-WITH-CORRECTIONS

Independent argument: let `L=conv(rows\{v})` and `d=dist_1(v,L)`. If `d>0`, then `v∉L`, hence `v` is an extreme point of `K=conv({v}∪L)`. By finite-dimensional `l1/l∞` separation, choose affine-linear `phi` with `||phi||_∞≤1` and `phi(v)≥sup_L phi+d`. Set `M=phi(v)`, `m=min_K phi`, and `h(x)=(M-phi(x))/(M-m)`. Then `h:K→[0,1]`, `h(v)=0`, and for every other row `p_i∈L`, `h(p_i)≥d/(M-m)`. Since `M-m≤diam_1(K)`, this gives `h(p_i)≥d/diam_1(K)≥rho/diam_1(K)` when `d≥rho`. Also any row with `||p_i-v||_1<rho` would put `d<rho`, so the required far-row condition is satisfied.

Reconciliation: this is the same argument as the recorded proof, including the corrected signed-row constant `diam_1(K)≤2+4δ`, hence `κ≥rho/(2+4δ)`.

Correction: the vertex conclusion needs `d>0`; as written, if `rho=0` the hypothesis `d≥rho` is vacuous. Example at `δ=0`: rows `(1,0,0)`, `(0,1,0)`, `(1/2,1/2,0)` form an exact stochastic idempotent with the third row non-vertex and `d=0=rho`. For the intended `rho>0` case, the claim is proved.