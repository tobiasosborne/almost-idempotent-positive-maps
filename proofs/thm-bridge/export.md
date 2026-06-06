# Proof Export

## Node 1

**Statement:** For unital positive Phi on B(H)_sa with ||Phi^2-Phi|| <= eta <= eta_0, the near-fixed algebra (A=Im P, •, 1, A∩B(H)_+) is an eps-JB algebra with eps <= C sqrt(eta), with universal dimension-free constants and no use of complete positivity.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** ORDER-UNIT STRUCTURE (exact). By GT-orderunit, the near-fixed algebra (A=Im P, 1, A_+=A cap B(H)_+) is a finite-dimensional real order-unit space, and its order-unit norm ||a||_ou=inf{t>0: -t1<=a<=t1} coincides EXACTLY with the operator norm on A. By near_fixed_algebra (def-near-fixed-algebra) A=Im P is well-defined: P=theta(2Phi-1) is the spectral idempotent (GT-Pprops gives P^2=P, P(1)=1, so 1 in A and A is a real subspace of B(H)_sa). Thus the def-eps-jb-algebra ambient requirement -- a finite-dim real order-unit space with order-unit norm -- holds EXACTLY (zero eta-defect in order/unit/norm).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** UNIT LAW AND COMMUTATIVITY (exact). By GT-easy, the projected product a•b=P(a o b) on A satisfies the unit law 1•a=a and commutativity a•b=b•a EXACTLY (no eta error). These are precisely the two exact identities required by def-eps-jb-algebra (commutativity a o b=b o a and unit law 1 o a=a hold exactly), with the product symbol o of the definition realised by • on A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** AXIOM JB1 (approximate submultiplicativity). By GT-easy, ||a•b|| <= (1+C_1 eta)||a|| ||b|| for all a,b in A, with C_1 a universal dimension-free constant. This delivers def-eps-jb-algebra (JB1) ||a o b|| <= (1+eps)||a|| ||b|| with the O(eta) defect C_1 eta (to be absorbed into eps=C sqrt(eta) at node 1.7).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** AXIOM JB2 (lower square-norm bound). By GT-easy, ||a•a|| >= (1-C_2 eta)||a||^2 for all a in A, with C_2 universal dimension-free. This delivers def-eps-jb-algebra (JB2) ||a o a|| >= (1-eps)||a||^2 with the O(eta) defect C_2 eta (absorbed at node 1.7).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** AXIOM JB3 (approximate positivity of squares). By GT-easy, a•a >= -C_3 eta ||a||^2 1 for all a in A, with C_3 universal dimension-free. This delivers def-eps-jb-algebra (JB3) a o a >= -eps ||a||^2 1 with the O(eta) defect C_3 eta (absorbed at node 1.7).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** AXIOM JB4 (approximate Jordan identity). By GT-jordan, ||((a•a)•b)•a - (a•a)•(b•a)|| <= C_4 sqrt(eta) ||a||^3 ||b|| for all a,b in A, with C_4 universal dimension-free. This delivers def-eps-jb-algebra (JB4) ||((a o a) o b) o a - (a o a) o (b o a)|| <= eps ||a||^3 ||b|| with the O(sqrt(eta)) defect C_4 sqrt(eta) (this is the dominant term setting eps; see node 1.7).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** ABSORPTION: fix eta_0 < 1/4 (e.g. eta_0=1/8), strictly below 1/4 — the BINDING constraint from GT-Pprops (lem-P-properties requires eta<=eta_0<1/4 for the binomial series R=(S^2)^{-1/2}=(1-4(Phi-Phi^2))^{-1/2} to converge, i.e. 4 eta_0<1). Since eta_0<1/4<1, for 0<=eta<=eta_0 one has eta<=1 => eta^2<=eta => eta<=sqrt(eta). Hence the O(eta) defects (JB1-JB3: C_1,C_2,C_3 eta) and the O(sqrt eta) defect (JB4: C_4 sqrt eta) combine into eps=C sqrt(eta), C=max(C_1,C_2,C_3,C_4) a FINITE universal constant; final exponent sqrt(eta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.8

**Statement:** Constants universal & dimension-free: with eta_0 < 1/4 FIXED (strict), the GT-Pprops constant C(eta_0)=sum_{n>=1}|a_n|(4 eta_0)^{n-1} (a_n the binomial coefficients of x^{-1/2}) is FINITE because 4 eta_0<1 (inside the radius of convergence rho=1); hence every C_i built from it is finite, universal, and dimension-free (no dependence on dim H or rank). At the EXCLUDED boundary eta_0=1/4 (4 eta_0=1) the series diverges — which is precisely why eta_0<1/4 must be strict. AND no complete positivity is used anywhere: the binomial P, Jordan-Schwarz, and the one-hole estimates each use only positivity+unitality (CP-free per their validated workspaces); the assembly never invokes an amplification id_n (x) Phi.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

