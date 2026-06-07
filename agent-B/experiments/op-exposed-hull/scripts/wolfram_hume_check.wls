(* Exact symbolic smoke check for Hume's 3x3 signed affine retraction. *)

s = Symbol["s"];
v = {1, -1 + s, -s};
u = {1 - s + s^2, -s, 0};
p = IdentityMatrix[3] - Outer[Times, u, v];
ones = ConstantArray[1, 3];

Print["P=" <> ToString[MatrixForm[p], InputForm]];
Print["P.ones=" <> ToString[FullSimplify[p.ones], InputForm]];
Print["P.P-P=" <> ToString[FullSimplify[p.p - p], InputForm]];
Print["row2-negative-entry=" <> ToString[FullSimplify[p[[2, 3]]], InputForm]];
Print["max-negative-mass-for-0<s<1/2=s^2"];
