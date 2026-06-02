"""
Analyze the extremal singular cochain (right singular vector for sigma_min)
of d^1 on H_n(C), to understand WHY sigma_min ~ sqrt(n/2).

Also verify that the nonzero singular values come in a clean spectrum
(multiplicities), which would explain the exact asymptotic.
"""
import numpy as np
import jordan_common as jc
from jordan_fast import build_d1_fast


def main():
    for n in [2, 3, 4, 5]:
        B = jc.basis_Hn_C(n)
        N, ip, jordan, Bb = jc.make_matrix_algebra(B)
        D, info = build_d1_fast(N, ip, jordan, Bb)
        U, sv, VT = np.linalg.svd(D, full_matrices=False)
        smax = sv[0]; tol = max(D.shape)*np.finfo(float).eps*smax
        nz = sv[sv > tol]
        # round to find multiplicities
        rounded = np.round(nz, 4)
        uniq, counts = np.unique(rounded, return_counts=True)
        print(f"H_{n}(C): N={N}, #nonzero sv={len(nz)}, smin={nz.min():.5f}")
        print("   distinct nonzero singular values (value x multiplicity):")
        # show smallest few and largest few distinct
        order = np.argsort(uniq)
        uu = uniq[order]; cc = counts[order]
        show = list(zip(uu, cc))
        # print smallest 6 and largest 3
        head = show[:6]; tail = show[-3:]
        print("     smallest:", ", ".join(f"{v:.4f}x{c}" for v, c in head))
        print("     largest :", ", ".join(f"{v:.4f}x{c}" for v, c in tail))
        # the extremal right singular vector = minimal cochain direction
        hmin = VT[len(sv) - 1 - (len(sv) - len(nz))]  # last nonzero
        # better: index of min nonzero
        idxmin = np.where(sv > tol)[0][-1]
        hmin = VT[idxmin].reshape(N, N)
        # is it close to a derivation-like / scalar-like structure?
        # check: how much of hmin is the "identity-insertion" h(x)= c*x ?
        idmap = np.eye(N).reshape(-1)
        idmap = idmap / np.linalg.norm(idmap)
        overlap_id = abs(np.dot(VT[idxmin], idmap))
        print(f"   |<extremal cochain, identity-map>| = {overlap_id:.4f}")
        print()


if __name__ == "__main__":
    main()
