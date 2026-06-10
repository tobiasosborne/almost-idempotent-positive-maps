VERDICT: DIED-AT the excision-to-sup step.

The fatal display is the Markov threshold tradeoff. Let the target finisher leakage be
\[
\eta_* = c(1-q)\tau .
\]
The best cut gives only a weighted average
\[
A:=\sum_{i\in T} w_i \lambda_i(T^c)\le C\tau ,
\]
not \(O(\tau^2)\). If
\[
BAD=\{i\in T:\lambda_i(T^c)>r\},
\]
then Markov gives \(w(BAD)\le A/r\). To make the kept rows usable for t10, need \(r\le \eta_*\). To keep \(v\) closed after excision, even in the best weighting \(w\sim P_v^+\), need \(P_v^+(BAD)\lesssim \eta_*\), hence \(A/r\lesssim \eta_*\), i.e.
\[
r\gtrsim A/\eta_* .
\]
Together:
\[
A/\eta_* \lesssim r \le \eta_*
\quad\Rightarrow\quad
A\lesssim \eta_*^2=O((1-q)^2\tau^2),
\]
but the available coarea bound is \(A=O(\tau)\). So the two requirements are incompatible at the target scale.

The check “\(v\) is never BAD” is not enough. It controls only \(P_v^+(T^c)\):
\[
P_v^+(T^c)\le \delta\Omega/t_*=O(\tau).
\]
After excision the new leakage is
\[
P_v^+((T\setminus BAD)^c)=P_v^+(T^c)+P_v^+(BAD),
\]
and \(P_v^+(BAD)\) can be order one: BAD rows may have \(g=O(\delta\Omega)\), so \(g_v=0\) does not charge much mass sent to them.

Iterating the excision does not fix this. At step \(m\),
\[
\lambda_i^{(m+1)}=\lambda_i(T^c)+\sum_{j\in R_m}|P_{ij}|,
\]
and the new term is leakage into low-\(g\) removed rows, outside the harmonic/coarea budget. This is exactly the missing support/minorization theorem.

The stochastic-complement branch also does not close from current inputs. X2 gives exact complement algebra, but the needed conditioning is absent; the effective defect/leakage contains inverse-gap factors like
\[
\delta_{\rm eff}\sim \delta/\gamma,\qquad \gamma=\|(I-P_{BB})^{-1}\|^{-1},
\]
and the existing X2 amplifier shows no universal control without a new conditioning lemma.

New sub-lemmas from this pass:

1. Excision threshold tradeoff: average \(O(\tau)\) cannot yield both sup \(O(\tau)\) and removed \(v\)-mass \(O(\tau)\).
2. Excised-block exposure gap: a single \(\rho\)-far BAD row with \(g<\kappa\Omega\) still blocks \(g/\Omega\) from exposing \(v\).
3. Iterated excision needs a new Carleson/minorization estimate, not present in the current dossier.
4. Stochastic complement reduces to the known X2 conditioning gap.

\(P(\text{linear law true})\approx 0.78\).  
\(P(\text{this death diagnosis survives audit})\approx 0.86\).