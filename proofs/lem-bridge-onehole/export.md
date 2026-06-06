# Proof Export

## Node 1

**Statement:** For a range-product hole h=h_{r,s}=r∘s-P(r∘s) and t,u in A, the one-hole insertion contexts ||P((h∘t)∘u)|| <= C sqrt(eta)||r||||s||||t||||u|| (5.1) and ||P(h∘(t∘u))|| <= C sqrt(eta)||r||||s||||t||||u|| (5.2).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** SIGN + CRUDE BOUND. (a) Sign identity: by def-square-hole, h_{r,s}=r o s-P(r o s) and q_{r,s}=P(r o s)-r o s, so h_{r,s}=-q_{r,s} EXACTLY. Hence for any z in B(H)_sa, P(h_{r,s} o z)=-P(q_{r,s} o z), so ||P(h_{r,s} o z)|| = ||P(q_{r,s} o z)|| and any (HZ)/(HH) bound on the q-side transfers verbatim to the h-side. Also h_{r,s} in Ker P: P(h_{r,s})=P(r o s)-P(P(r o s))=P(r o s)-P(r o s)=0 using P^2=P (GT-Pprops). (b) Crude norm bound: ||h_{r,s}|| = ||r o s-P(r o s)|| <= ||r o s||+||P(r o s)|| (triangle inequality for the order-unit norm, GT-bh-cstar). By GT-jb-submult (V=B(H)_sa is a JB algebra via GT-bhsa-jc + GT-jc-is-jb) ||r o s|| <= ||r|| ||s||. By GT-Pprops ||P|| <= 1+C eta, so ||P(r o s)|| <= (1+C eta)||r|| ||s||. Hence ||h_{r,s}|| <= (2+C eta)||r|| ||s|| <= 3||r|| ||s|| (since eta<=eta_0<1/4 and the universal C gives C eta<=1), i.e. ||h_{r,s}|| <= C||r|| ||s|| with the universal constant absorbed.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** ESTIMATE (5.1): ||P((h o t) o u)|| <= C sqrt(eta)||r|| ||s|| ||t|| ||u||, where h=h_{r,s} and t,u in A. Put y:=h o t in B(H)_sa. By P^2=P (GT-Pprops), y=P(y)+(y-P(y)) with P(y) in Im P=A and (y-P(y)) in Ker P (since P(y-P(y))=P(y)-P^2(y)=P(y)-P(y)=0). By real-linearity of P (GT-Pprops): P(y o u)=P(P(y) o u)+P((y-P(y)) o u). RANGE part [proved in child 1.2.1]: ||P(P(y) o u)|| <= C sqrt(eta)||r|| ||s|| ||t|| ||u||. KERNEL part [proved in child 1.2.2]: ||P((y-P(y)) o u)|| <= C sqrt(eta)||r|| ||s|| ||t|| ||u||. Adding the two (triangle inequality, GT-bh-cstar) gives ||P((h o t) o u)|| = ||P(y o u)|| <= 2C sqrt(eta)||r|| ||s|| ||t|| ||u||, i.e. (5.1) with constant absorbed.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** RANGE part of (5.1): ||P(P(y) o u)|| <= C sqrt(eta)||r|| ||s|| ||t|| ||u||, where y=h o t, h=h_{r,s}, t,u in A. First, P(y) o u with P(y) in A=Im P and u in A. Bound: ||P(P(y) o u)|| <= ||P|| ||P(y) o u|| (definition of operator norm of P, GT-Pprops; valid since P(y) o u in B(H)_sa) <= ||P|| ||P(y)|| ||u|| (GT-jb-submult, V=B(H)_sa a JB algebra via GT-bhsa-jc + GT-jc-is-jb). By GT-Pprops ||P|| <= 1+C eta <= 2 (eta<=eta_0<1/4). It remains to bound ||P(y)||=||P(h o t)||. By the sign identity (node 1.1) h=-q_{r,s}, so P(h o t)=-P(q_{r,s} o t), giving ||P(y)||=||P(q_{r,s} o t)||. Apply GT-HZ with z=t in A subset B(H)_sa: ||P(q_{r,s} o t)|| <= C sqrt(eta)||r|| ||s|| ||t||. Hence ||P(P(y) o u)|| <= 2 * C sqrt(eta)||r|| ||s|| ||t|| * ||u|| = C' sqrt(eta)||r|| ||s|| ||t|| ||u||, constant absorbed.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** KERNEL part of (5.1): ||P((y-P(y)) o u)|| <= C sqrt(eta)||r|| ||s|| ||t|| ||u||, where y=h o t, h=h_{r,s}, t,u in A. Set n:=y-P(y). By P^2=P (GT-Pprops), P(n)=P(y)-P^2(y)=P(y)-P(y)=0, so n in Ker P. Apply GT-FI (First-Insertion, instantiated at the kernel element n with b=u in A): since P(n)=0 we have P(P(n) o u)=P(0 o u)=0, so ||P(n o u)|| = ||P(n o u)-P(P(n) o u)|| <= C sqrt(eta)||n|| ||u|| by GT-FI. Now bound ||n||=||y-P(y)|| <= ||y||+||P(y)|| (triangle, GT-bh-cstar). ||y||=||h o t|| <= ||h|| ||t|| (GT-jb-submult) <= C||r|| ||s|| ||t|| (crude bound, node 1.1). ||P(y)|| <= ||P|| ||y|| <= (1+C eta)||y|| <= 2 C||r|| ||s|| ||t|| (GT-Pprops). Hence ||n|| <= 3 C||r|| ||s|| ||t|| = C''||r|| ||s|| ||t||. Therefore ||P(n o u)|| <= C sqrt(eta) * C''||r|| ||s|| ||t|| * ||u|| = C' sqrt(eta)||r|| ||s|| ||t|| ||u||, constant absorbed.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** ESTIMATE (5.2): ||P(h o (t o u))|| <= C sqrt(eta)||r|| ||s|| ||t|| ||u||, where h=h_{r,s} and t,u in A. Decompose t o u=P(t o u)+h_{t,u} (def-square-hole: h_{t,u}:=t o u-P(t o u), so this is an exact identity). By real-linearity of the Jordan product in its second slot and of P (GT-Pprops): P(h o (t o u))=P(h o P(t o u))+P(h o h_{t,u}). FIRST piece [proved in child 1.3.1]: ||P(h o P(t o u))|| <= C sqrt(eta)||r|| ||s|| ||t|| ||u||. SECOND piece [proved in child 1.3.2]: ||P(h o h_{t,u})|| <= C eta||r|| ||s|| ||t|| ||u||, which is <= C sqrt(eta)||r|| ||s|| ||t|| ||u|| since eta=sqrt(eta)*sqrt(eta) <= sqrt(eta) for eta<=eta_0<1/4<1. Adding the two (triangle inequality, GT-bh-cstar) gives (5.2) with constant absorbed.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** FIRST piece of (5.2): ||P(h o P(t o u))|| <= C sqrt(eta)||r|| ||s|| ||t|| ||u||, where h=h_{r,s}, t,u in A. Note P(t o u) in Im P=A subset B(H)_sa, so it is an admissible insertion argument z:=P(t o u). By the sign identity (node 1.1) h=-q_{r,s}, so P(h o z)=-P(q_{r,s} o z), giving ||P(h o P(t o u))||=||P(q_{r,s} o P(t o u))||. Apply GT-HZ with z=P(t o u): ||P(q_{r,s} o P(t o u))|| <= C sqrt(eta)||r|| ||s|| ||P(t o u)||. Bound ||P(t o u)|| <= ||P|| ||t o u|| <= (1+C eta)||t|| ||u|| (GT-Pprops ||P||<=1+C eta; GT-jb-submult ||t o u||<=||t|| ||u||, V=B(H)_sa a JB algebra via GT-bhsa-jc + GT-jc-is-jb) <= 2||t|| ||u|| (eta<=eta_0<1/4). Hence ||P(h o P(t o u))|| <= 2C sqrt(eta)||r|| ||s|| ||t|| ||u|| = C' sqrt(eta)||r|| ||s|| ||t|| ||u||, constant absorbed.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** SECOND piece of (5.2): ||P(h o h_{t,u})|| <= C sqrt(eta)||r|| ||s|| ||t|| ||u||, where h=h_{r,s}, t,u in A. By the sign identity (node 1.1, def-square-hole) h=h_{r,s}=-q_{r,s} and likewise h_{t,u}=-q_{t,u}, so h o h_{t,u}=(-q_{r,s}) o (-q_{t,u})=q_{r,s} o q_{t,u}, hence P(h o h_{t,u})=P(q_{r,s} o q_{t,u}) and ||P(h o h_{t,u})||=||P(q_{r,s} o q_{t,u})||. Apply GT-HH (two-hole insertion): ||P(q_{r,s} o q_{t,u})|| <= C eta||r|| ||s|| ||t|| ||u||. Finally eta = sqrt(eta) * sqrt(eta) <= sqrt(eta) because sqrt(eta) <= sqrt(eta_0) < sqrt(1/4) = 1/2 < 1; so C eta||r|| ||s|| ||t|| ||u|| <= C sqrt(eta)||r|| ||s|| ||t|| ||u||. This O(eta) term is absorbed into the O(sqrt eta) target.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

