VERDICT: GAP

PROVED: (i) is correct. If `m=neg(lambda)`, write `lambda=lambda^+ - lambda^-`, with masses `1+m` and `m`. Then `q=(1+m)^{-1}Σ lambda_a^+ f_a` and `r=m^{-1}Σ lambda_a^- f_a` lie in `conv{f_a}⊂conv W`, and `p=(1+m)q-mr`, so `dist₁(p,conv W)≤||p-q||₁≤m diam₁({f_a})≤(2+4δ)m`.

PROVED: the first part of (ii) is also correct. From `p_i=p_iP=Σ_j P_ij p_j`, normalize the positive and negative coefficient parts to get `p_i=(1+ε_i)q_i-ε_i r_i`, `q_i,r_i∈K`, hence `||p_i-q_i||₁≤diam₁(K)ε_i≤(2+4δ)ε_i`.

GAP: the recorded proof then says `dist(q_i,C)≥H-O(δ)`, so the positive part “must put almost all mass” on rows of height at least `H/2`. This does not follow for an arbitrary row with `h_i=H`: a large amount of positive mass below `H/2` can be compensated by mass on rows with height much larger than `H`.

Corrected statement: if `H` is a global maximum of `h_j=dist₁(p_j,C)` over rows, then the leakage bound follows. With normalized positive weights `α_j=P_ij^+/(1+ε_i)`, convexity gives  
`dist(q_i,C)≤Σ α_j h_j≤H-μ H/2`, where `μ=Σ_{h_j≤H/2}α_j`. Combining with `dist(q_i,C)≥H-(2+4δ)ε_i` yields `μ≤2(2+4δ)ε_i/H≤2(2+4δ)δ/H`. Unnormalized positive mass gains a factor `1+ε_i`.