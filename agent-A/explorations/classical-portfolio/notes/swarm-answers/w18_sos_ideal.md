# w18_sos_ideal — smallest hidden geometry (4,3); SOS-mod-ideal hits the hiddenness-lifting wall (codex, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w18_sos_ideal/brief.md. Artifacts: experiments/out/w18_sos_ideal/.

Done. Deliverable is saved at [answer.md](/tmp/codex-sigma-wall/w18_sos_ideal/answer.md).

Verdict summary:
- `(n,k)=(3,2)`: **CERTIFICATE at degree 2**. Hidden branch is empty; `H=0`, so `delta-cH=tau^2` is the SOS square.
- Smallest hidden geometry found/verified: `(n,k)=(4,3)`. Saved exact rational rank-chart witness; it is hidden but low-height, so it does not threaten the linear law.
- `(n,k)=(4,3)` degree-2/4 SOS: **FORMULATION OBSTRUCTION**, not a no-certificate result. The obstruction is exactly the need to lift `W`, far sets, vertex status, and `dist(.,C_W)` through global KKT/binary/quotient variables.

Artifacts:
- [sos_ideal_probe.py](/tmp/codex-sigma-wall/w18_sos_ideal/sos_ideal_probe.py)
- [outputs/sos_ideal_probe.json](/tmp/codex-sigma-wall/w18_sos_ideal/outputs/sos_ideal_probe.json)
- [progress.md](/tmp/codex-sigma-wall/w18_sos_ideal/progress.md)

Verification: `python3 -m py_compile sos_ideal_probe.py` passed, and the probe script was run successfully.