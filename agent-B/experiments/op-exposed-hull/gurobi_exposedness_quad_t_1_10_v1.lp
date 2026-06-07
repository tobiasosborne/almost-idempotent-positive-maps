Maximize
 obj: tvar
Subject To
 h0_ub: 0.01 a0 - 0.01 a1 + 0.98999999999999999 a2 + 0.01 a3 + 1 beta <= 1
 h0_lb: - 0.01 a0 + 0.01 a1 - 0.98999999999999999 a2 - 0.01 a3 - 1 beta <= 0
 h1_ub: 1 a1 + 1 beta <= 1
 h1_lb: - 1 a1 - 1 beta <= 0
 h2_ub: 0.01 a0 + 0.00010101010101010101 a1 + 0.98999999999999999 a2 - 0.00010101010101010101 a3 + 1 beta <= 1
 h2_lb: - 0.01 a0 - 0.00010101010101010101 a1 - 0.98999999999999999 a2 + 0.00010101010101010101 a3 - 1 beta <= 0
 h3_ub: 1 a3 + 1 beta <= 1
 h3_lb: - 1 a3 - 1 beta <= 0
 outside0: - 0.01 a0 + 0.01 a1 - 0.98999999999999999 a2 - 0.01 a3 - 1 beta + 1 tvar <= 0
 outside2: - 0.01 a0 - 0.00010101010101010101 a1 - 0.98999999999999999 a2 + 0.00010101010101010101 a3 - 1 beta + 1 tvar <= 0
 outside3: - 1 a3 - 1 beta + 1 tvar <= 0
 vertex_zero: 1 a1 + 1 beta = 0
Bounds
 a0 free
 a1 free
 a2 free
 a3 free
 beta free
 0 <= tvar <= 1
End
