VERDICT: LP-CERTIFICATE AT SMALL k; GENERAL-k GAP NOT CLOSED.

I wrote the long-form artifact to [proof.md](/tmp/codex-sigma-wall/w33_sf_geom/proof.md). SF is not proved, and I did not find a dimension-free counterexample. The main result is an exact geometry-included LP loop using the H-M converse parametrization `P = L B`, `B L = I`, with row negative masses imposed on the full matrix `P`, not on coefficient weights alone.

Key artifacts:
- [fixed_support_geom_lp.py](/tmp/codex-sigma-wall/w33_sf_geom/fixed_support_geom_lp.py): structural HiGHS LP.
- [targeted_geom_lp_summary.txt](/tmp/codex-sigma-wall/w33_sf_geom/targeted_geom_lp_summary.txt): sparse `k=3,4` support certificates.
- [dense_pair_C2_summary.txt](/tmp/codex-sigma-wall/w33_sf_geom/dense_pair_C2_summary.txt): dense transverse-pair stress results.
- [dense_pair_k7_verify.txt](/tmp/codex-sigma-wall/w33_sf_geom/dense_pair_k7_verify.txt): exact rational verification of the `k=7`, `a=1/4` active matrix with `delta=6/17`, target `3/4`, ratio `17/8`.
- [gurobi_status.txt](/tmp/codex-sigma-wall/w33_sf_geom/gurobi_status.txt): Gurobi is installed, but model creation is blocked by HostID license mismatch.

Final checks passed: scripts compile, `answer.md` is absent.