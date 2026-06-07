# Proof Export

## Node 1

**Statement:** The signed-idempotent and stochastic-idempotent formulations of classical stability are equivalent up to universal constants: Q row-stochastic with ||Q^2-Q|| <= eta gives P=theta(2Q-1) signed affine retraction with ||P-Q|| <= C eta and neg mass delta <= C eta, and conversely row-normalising p_i^+ gives Q with ||P-Q|| <= 2 delta, ||Q^2-Q|| <= 6 delta+4 delta^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** N1 (ARENA, shared by both directions). M_n(R) under the operator norm ||A|| := ||A||_{inf->inf} = sup_{||x||_inf<=1} ||Ax||_inf, induced by ||x||_inf=max_k|x_k| on R^n, is a unital Banach algebra (GT-operator-norm-banach: bounded linear operators on a Banach space form a unital Banach algebra, instantiated at calA=R^n). Concretely: ||I||=1; triangle ||A+B||<=||A||+||B|| and exact submultiplicativity ||AB||<=||A|| ||B|| follow from the sup-definition (no 1+eps slack); finite-dim => complete. CLOSED FORM (EXTRACTION-LEVEL FLAG -- NOT byte-stated in any present ref; derived inline, established lem-P-properties node 1.1.2 pattern): for ||x||_inf<=1, |(Ax)_i|<=sum_j|A_ij|, with equality at x_j=sign(A_ij), so ||A||=max_i sum_j|A_ij| (max row ell^1). In particular ||A||=max_i ||a_i||_1 where a_i is row i; for a probability/signed row a_i, ||a_i||_1 is its total variation. [GT-operator-norm-banach]

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** N2 (FORWARD spectral defect). Let Q be row-stochastic (GT-hyp / def-stochastic: Q>=0 entrywise, Q1=1) with ||Q^2-Q||<=eta, eta<=eta_0<1/4. By N1 (1.1), ||Q||=max_i ||q_i||_1 = max_i sum_j Q_ij = 1 (rows are probability vectors: Q>=0 and Q1=1 give row sums 1). Set S:=2Q-I. Then S1=2(Q1)-1=2*1-1=1, and ||S||<=2||Q||+||I||=2+1=3 (N1 triangle, ||I||=1). Also S^2-I=(2Q-I)^2-I=4Q^2-4Q+I-I=4(Q^2-Q), so ||S^2-I||=4||Q^2-Q||=4 eta <= 4 eta_0 < 1 (GT-small-eta-threshold: the eta<1/4 threshold; here ||S^2-I||=4eta<1 exactly matches Kitaev's ||X^2-I||<=4delta<1 under P->Q, delta->eta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** N3 (FORWARD inverse-sqrt + EXPLICIT C -- HONEST FLAG 1: the explicit constant is DERIVED here, not cited; Kitaev gives only big-O). Apply GT-funcalc-taylor-bound with B=M_n(R) (N1), f(x)=x^{-1/2}, x0=1, r=1, X=S^2. Since ||S^2-I||=4eta<1=r (N2), R:=(S^2)^{-1/2}=sum_{n>=0} a_n (S^2-I)^n converges, commutes with S^2 (and S), with a_n=C(-1/2,n). DERIVED scalar real-analysis (one line, no external): |a_n|=|C(-1/2,n)|=C(2n,n)/4^n>=0 (the signs alternate so |a_n|=(-1)^n C(-1/2,n)), and sum_{n>=0}|a_n| t^n=(1-t)^{-1/2} for 0<=t<1. Hence R1=a_0 1 + sum_{n>=1}a_n (S^2-I)^n 1 = 1 (a_0=f(1)=1; (S^2-I)1=S^2 1 - 1 = S(S1)-1 = S*1-1 = 1-1 = 0 by N2 S1=1, so all n>=1 terms vanish). By the GT-funcalc-taylor-bound sum-bound, ||R-I||=||f(S^2)-f(I)|| <= sum_{n>=1}|a_n| ||S^2-I||^n = ||S^2-I|| sum_{n>=1}|a_n| ||S^2-I||^{n-1} <= C_1(eta_0) ||S^2-I||, where C_1(eta_0):=sum_{n>=1}|a_n| (4 eta_0)^{n-1} <= (4eta_0)^{-1}((1-4eta_0)^{-1/2}-1) < infinity is EXPLICIT and finite (geometric-type tail, 4eta_0<1). Thus ||R-I|| <= C_1(eta_0) ||S^2-I|| = 4 C_1(eta_0) eta. [GT-funcalc-taylor-bound; N1; N2]

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** N4 (FORWARD calculus multiplicativity -- HONEST FLAG 2, TENSION for the verifier). CLAIM: R^2=(S^2)^{-1}, hence sgn(S):=S R satisfies sgn(S)^2=S^2 R^2=I exactly. DERIVED as a Cauchy-product node (conservative), NOT read off Kitaev's bytes: Kitaev:535 only DISMISSES the holomorphic calculus and does not state f(X)g(X)=(fg)(X). (TENSION the verifier must byte-check: the sibling repo's proofs/lem-P-properties external GT-funcalc (0f14e166) DOES assert 'the calculus is multiplicative f(X)g(X)=(fg)(X)' as cited @ :503-532,:642; we do NOT rely on that wording, we re-derive it.) DERIVATION: write Y:=S^2-I, ||Y||=4eta<1 (N2); R=sum_m a_m Y^m and R^2=(sum_m a_m Y^m)(sum_k a_k Y^k). Both series converge ABSOLUTELY in operator norm: sum_m |a_m| ||Y||^m <= (1-||Y||)^{-1/2}<infinity (N3) and submultiplicativity ||Y^{m+k}||<=||Y^m|| ||Y^k|| (N1), all powers of the single element Y commute, so the Cauchy product is justified and R^2 = sum_N (sum_{m+k=N} a_m a_k) Y^N = sum_N b_N Y^N where b_N are the coefficients of f(x)^2=((1+y)^{-1/2})^2=(1+y)^{-1}=sum_N (-1)^N y^N (y=x-1). Thus R^2=(S^2)^{-1}=sum_N (-1)^N Y^N=(I+Y)^{-1}, and (I+Y)=S^2, so S^2 R^2=I. Therefore sgn(S)^2=(SR)(SR)=S^2 R^2=I (S,R commute via the common functional calculus in S^2, N3). [GT-funcalc-taylor-bound; N1; N3]

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** N5 (FORWARD: P is an exact signed affine retraction). Define P:=theta(2Q-I)=(1/2)(I+sgn(S)) where S=2Q-I (N2), sgn(S)=S R (N4). This is exactly the GT-kitaev-spectral-propP construction with the renaming P_Kitaev->Q, delta->eta (||Q^2-Q||<=eta<1/4, GT-hyp): Prop_P gives ~P=theta(2Q-I) with ~P^2=~P EXACTLY. We re-derive idempotence directly to keep it self-contained: P^2=(1/4)(I+sgn(S))^2=(1/4)(I+2 sgn(S)+sgn(S)^2)=(1/4)(I+2 sgn(S)+I)=(1/4)(2I+2 sgn(S))=(1/2)(I+sgn(S))=P, using sgn(S)^2=I (N4). Unit-preservation: P1=(1/2)(1+sgn(S)1)=(1/2)(1+S(R1))=(1/2)(1+S*1)=(1/2)(1+S1)=(1/2)(1+1)=1, using R1=1 (N3) and S1=1 (N2). So P1=1 and P^2=P exactly; P's rows are signed measures (real entries) of total mass 1 (from P1=1), i.e. P is a signed affine retraction in the sense of def-stochastic. [GT-kitaev-spectral-propP; N2; N3; N4]

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** N6 (FORWARD closeness, EXPLICIT universal C). Compute P-Q: P=(1/2)(I+SR), and Q=(1/2)(I+S) since S=2Q-I => Q=(1/2)(I+S). So P-Q=(1/2)(I+SR)-(1/2)(I+S)=(1/2)(SR-S)=(1/2)S(R-I). By N1 submultiplicativity and N2 (||S||<=3), N3 (||R-I||<=4 C_1(eta_0) eta): ||P-Q||<=(1/2)||S|| ||R-I||<=(1/2)(3)(4 C_1(eta_0) eta)=6 C_1(eta_0) eta. Define the EXPLICIT universal constant C:=6 C_1(eta_0) (HONEST FLAG 1: C is DERIVED, C_1(eta_0)=sum_{n>=1}|C(-1/2,n)|(4eta_0)^{n-1}<infinity from N3, depending only on the fixed regime parameter eta_0<1/4, dimension-free in n). Hence ||P-Q||<=C eta. [N1; N2; N3; N5]

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** N7 (FORWARD negative mass; closes FORWARD). The negative mass of P is delta:=max_i sum_j max(-P_ij,0) (def-stochastic). Since Q>=0 entrywise (GT-hyp / def-stochastic), for each (i,j): max(-P_ij,0)=max(Q_ij-P_ij-Q_ij,0)<=max(Q_ij-P_ij,0)<=|Q_ij-P_ij|=|P_ij-Q_ij| (using Q_ij>=0 so -P_ij<=Q_ij-P_ij, and max(t,0)<=|t|). Summing over j: sum_j max(-P_ij,0) <= sum_j |P_ij-Q_ij| = ||p_i-q_i||_1 (row i of P-Q). By N1 (||P-Q||=max_i ||p_i-q_i||_1): delta=max_i sum_j max(-P_ij,0) <= max_i ||p_i-q_i||_1 = ||P-Q|| <= C eta (N6, same universal C). CONCLUSION (FORWARD): from row-stochastic Q with ||Q^2-Q||<=eta, P=theta(2Q-1) is a signed affine retraction (P1=1, P^2=P exactly, N5) with ||P-Q||<=C eta (N6) and negative mass delta<=C eta. [N1; N6; def-stochastic]

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.8

**Statement:** N8 (CONVERSE construction + distances). Let P be a signed affine retraction (GT-hyp / def-stochastic: P1=1, P^2=P exactly, rows p_i signed measures of total mass 1) with negative mass delta=max_i sum_j max(-P_ij,0). Disjoint-support split of each row: p_ij=p_ij^+ - p_ij^- with p_ij^+=max(p_ij,0), p_ij^-=max(-p_ij,0); supports {j:p_ij>0} and {j:p_ij<0} are disjoint. ell^1 additivity on disjoint supports: ||a p_i^+ - b p_i^-||_1=a||p_i^+||_1+b||p_i^-||_1 for a,b>=0. Total mass: sum_j p_ij=(P1)_i=1 (P1=1). Set a_i:=||p_i^-||_1=sum_j max(-P_ij,0)=neg(p_i)<=delta. Then ||p_i^+||_1=sum_j p_ij + ||p_i^-||_1 = 1 + a_i (since sum_j p_ij^+ - sum_j p_ij^- = sum_j p_ij =1). Define q_i:=p_i^+/(1+a_i) (well-defined: 1+a_i>=1>0). Then q_i>=0 entrywise and ||q_i||_1=||p_i^+||_1/(1+a_i)=(1+a_i)/(1+a_i)=1, so Q (rows q_i) is row-stochastic (Q>=0, Q1=1, def-stochastic), and by N1 ||Q||=max_i ||q_i||_1=1. DISTANCES: p_i-q_i=p_i^+ - p_i^- - p_i^+/(1+a_i)=p_i^+ (1-1/(1+a_i)) - p_i^- = p_i^+ (a_i/(1+a_i)) - p_i^-, disjoint supports, so ||p_i-q_i||_1=(a_i/(1+a_i))||p_i^+||_1 + ||p_i^-||_1=(a_i/(1+a_i))(1+a_i)+a_i=a_i+a_i=2 a_i. Hence ||P-Q||=max_i ||p_i-q_i||_1=max_i 2 a_i<=2 delta (N1). Also ||p_i||_1=||p_i^+||_1+||p_i^-||_1=(1+a_i)+a_i=1+2 a_i, so ||P||=max_i ||p_i||_1=max_i(1+2 a_i)=1+2 delta (N1; note P1=1 ALONE does NOT bound ||P||, the +/- split does). [N1; GT-hyp; def-stochastic]

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.9

**Statement:** N9 (CONVERSE algebraic identity, exact ring computation). With Q from N8 and P the signed affine retraction (P^2=P EXACTLY, GT-hyp/def-stochastic), set D:=Q-P. Then Q=P+D, and in the associative unital ring M_n(R) (N1 arena): Q^2=(P+D)^2=P^2+PD+DP+D^2=P+PD+DP+D^2 (using P^2=P). Subtract Q=P+D: Q^2-Q=(P+PD+DP+D^2)-(P+D)=PD+DP+D^2-D. Equivalently Q^2-Q=(Q-P)Q+P(Q-P)-(Q-P): expand (Q-P)Q+P(Q-P)=DQ+PD=D(P+D)+PD=DP+D^2+PD, minus (Q-P)=minus D, giving DP+D^2+PD-D=PD+DP+D^2-D, identical. This is an EXACT identity (no approximation), pure distributivity+associativity in M_n(R), valid because P^2=P holds exactly. [N1; N8; P^2=P from GT-hyp/def-stochastic]

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.10

**Statement:** N10 (CONVERSE defect bound; closes CONVERSE). Take ||.|| (=||.||_{inf->inf}, N1) on the exact identity N9: Q^2-Q=PD+DP+D^2-D with D=Q-P. Triangle + submultiplicativity (N1): ||Q^2-Q||<=||P|| ||D||+||D|| ||P||... more precisely ||Q^2-Q||=||(Q-P)Q+P(Q-P)-(Q-P)||<=||Q-P|| ||Q|| + ||P|| ||Q-P|| + ||Q-P||. Substitute from N8: ||Q-P||=||P-Q||<=2 delta, ||Q||=1, ||P||<=1+2 delta. Hence ||Q^2-Q|| <= (2 delta)(1) + (1+2 delta)(2 delta) + 2 delta = 2 delta + 2 delta + 4 delta^2 + 2 delta = 6 delta + 4 delta^2. CONCLUSION (CONVERSE): row-normalising p_i^+ yields a row-stochastic Q (N8) with ||P-Q||<=2 delta (N8) and ||Q^2-Q||<=6 delta+4 delta^2. [N1; N8; N9]

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

