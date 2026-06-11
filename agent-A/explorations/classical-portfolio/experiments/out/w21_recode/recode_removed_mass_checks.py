#!/usr/bin/env python3
"""Removed-mass recoding checks for w21_recode.

The script intentionally mirrors the w20 audit stress family, but it evaluates
the repaired quantities: total removed recurrent mass, total removed transient
coefficient mass per row, survivor-coordinate relative shift, and the recoded
H-M residual.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np


TOL = 1e-10


@dataclass
class HM:
    blocks: list[list[int]]
    transients: list[int]
    pis: list[np.ndarray]
    alphas: dict[int, np.ndarray]
    name: str = ""

    @property
    def n(self) -> int:
        return sum(len(b) for b in self.blocks) + len(self.transients)

    @property
    def k(self) -> int:
        return len(self.blocks)


@dataclass
class Recode:
    old: HM
    new: HM
    drop_sets: list[list[int]]
    face_drop: dict[int, list[int]]
    q: list[float]
    r: dict[int, float]

    @property
    def q_total(self) -> float:
        return float(sum(self.q))

    @property
    def r_max(self) -> float:
        return max((float(v) for v in self.r.values()), default=0.0)

    @property
    def removed_mass_budget(self) -> float:
        return self.q_total + self.r_max


def embedded_pi(n: int, block: list[int], pi: np.ndarray) -> np.ndarray:
    out = np.zeros(n)
    out[block] = pi
    return out


def build_p0(st: HM) -> np.ndarray:
    n = st.n
    P = np.zeros((n, n))
    pi_full = [embedded_pi(n, b, pi) for b, pi in zip(st.blocks, st.pis)]
    for s, block in enumerate(st.blocks):
        for i in block:
            P[i] = pi_full[s]
    for i in st.transients:
        P[i] = sum(st.alphas[i][s] * pi_full[s] for s in range(st.k))
    return P


def row_l1_eps(P: np.ndarray, Q: np.ndarray) -> float:
    return max(float(np.abs(P[i] - Q[i]).sum()) for i in range(P.shape[0]))


def min_recurrent_mass(st: HM) -> float:
    vals = [float(x) for pi in st.pis for x in pi if x > 0.0]
    return min(vals) if vals else math.inf


def delta(P: np.ndarray) -> float:
    return max(float(np.maximum(-row, 0.0).sum()) for row in P)


def hm_residual(P: np.ndarray) -> dict[str, float]:
    n = P.shape[0]
    return {
        "idempotence": float(np.max(np.abs(P @ P - P))),
        "row_sum": float(np.max(np.abs(P @ np.ones(n) - 1.0))),
        "negative_part": delta(P),
    }


def recode_hm(st: HM, drop_sets: list[Iterable[int]], face_drop: dict[int, Iterable[int]]) -> Recode:
    drop = [sorted(set(ds)) for ds in drop_sets]
    old_to_block: dict[int, int] = {}
    for s, block in enumerate(st.blocks):
        for j in block:
            old_to_block[j] = s

    q: list[float] = []
    new_blocks: list[list[int]] = []
    new_pis: list[np.ndarray] = []
    dropped_rows: list[int] = []
    for s, (block, pi) in enumerate(zip(st.blocks, st.pis)):
        D = set(drop[s])
        if not D.issubset(block):
            raise ValueError(f"drop set {s} is not contained in its block")
        K = [j for j in block if j not in D]
        if not K:
            raise ValueError(f"block {s} would have no survivor")
        qs = float(sum(pi[block.index(j)] for j in D))
        if qs >= 1.0:
            raise ValueError(f"block {s} removed mass is not below one")
        kept = np.array([pi[block.index(j)] for j in K], dtype=float) / (1.0 - qs)
        q.append(qs)
        new_blocks.append(K)
        new_pis.append(kept)
        dropped_rows.extend(sorted(D))

    face = {i: sorted(set(v)) for i, v in face_drop.items()}
    r: dict[int, float] = {}
    new_alphas: dict[int, np.ndarray] = {}
    new_transients = sorted(set(st.transients).union(dropped_rows))
    for i in new_transients:
        if i in old_to_block and i not in st.transients:
            a = np.zeros(st.k)
            a[old_to_block[i]] = 1.0
            new_alphas[i] = a
            continue
        old = np.array(st.alphas[i], dtype=float)
        E = set(face.get(i, []))
        ri = float(sum(old[s] for s in E))
        r[i] = ri
        if ri >= 1.0:
            raise ValueError(f"transient row {i} would lose all coefficient mass")
        a = old.copy()
        for s in E:
            a[s] = 0.0
        a /= 1.0 - ri
        new_alphas[i] = a

    return Recode(st, HM(new_blocks, new_transients, new_pis, new_alphas, st.name + "_recoded"), drop, face, q, r)


def recurrent_compress_row(x: np.ndarray, rec: Recode) -> np.ndarray:
    y = np.array(x, dtype=float, copy=True)
    for s, block in enumerate(rec.old.blocks):
        D = rec.drop_sets[s]
        if not D:
            continue
        K = rec.new.blocks[s]
        mass = float(np.sum(y[D]))
        y[D] = 0.0
        y[K] += mass * rec.new.pis[s]
    return y


def recurrent_compress(P: np.ndarray, rec: Recode) -> np.ndarray:
    return np.vstack([recurrent_compress_row(row, rec) for row in P])


def survivor_relative_shift(rec: Recode) -> float:
    worst = 0.0
    for s, K in enumerate(rec.new.blocks):
        old_block = rec.old.blocks[s]
        old_pi = rec.old.pis[s]
        for new_pos, j in enumerate(K):
            old_mass = float(old_pi[old_block.index(j)])
            new_mass = float(rec.new.pis[s][new_pos])
            worst = max(worst, abs(new_mass - old_mass) / new_mass)
    return worst


def face_l1_shift(rec: Recode, i: int) -> float:
    if i not in rec.old.transients:
        return 0.0
    old = rec.old.alphas[i]
    new = rec.new.alphas[i]
    return float(np.abs(old - new).sum())


def audit_stress_cases() -> list[dict]:
    rows = []
    for nsmall, theta in [(4, 1e-5), (8, 1e-5), (20, 1e-5), (20, 1e-4)]:
        small = theta * 0.99
        kept_tiny = theta * 1.01
        big = 1.0 - nsmall * small - kept_tiny
        pi = np.array([small] * nsmall + [kept_tiny, big])
        block = list(range(nsmall + 2))
        transient = nsmall + 3
        st = HM(
            blocks=[block, [nsmall + 2]],
            transients=[transient],
            pis=[pi, np.array([1.0])],
            alphas={transient: np.array([theta * 0.5, 1.0 - theta * 0.5])},
            name=f"w20_stress_{nsmall}_{theta:g}",
        )
        rec = recode_hm(st, [block[:nsmall], []], {transient: [0]})
        P0 = build_p0(st)
        P1 = build_p0(rec.new)
        eps = row_l1_eps(P0, P1)
        q_total = rec.q_total
        q_alpha = rec.r_max
        old_ratio = eps / (min_recurrent_mass(rec.new) / 8.0)
        rows.append(
            {
                "case": st.name,
                "nsmall": nsmall,
                "theta": theta,
                "q_total": q_total,
                "q_alpha_max": q_alpha,
                "eps_recode": eps,
                "bound_2_removed": 2.0 * rec.removed_mass_budget,
                "eps_over_2_removed": eps / (2.0 * rec.removed_mass_budget),
                "old_eps_over_mu_after_div8": old_ratio,
                "mu_after": min_recurrent_mass(rec.new),
                "survivor_relative_shift": survivor_relative_shift(rec),
                "survivor_shift_bound_qmax": max(rec.q),
                "face_l1_shift": face_l1_shift(rec, transient),
                "face_l1_bound": 2.0 * q_alpha,
                "hm_residual": hm_residual(P1),
                "passes_removed_mass": eps <= 2.0 * rec.removed_mass_budget + 1e-12,
                "passes_survivor_shift": survivor_relative_shift(rec) <= max(rec.q) + 1e-12,
                "passes_face_shift": face_l1_shift(rec, transient) <= 2.0 * q_alpha + 1e-12,
            }
        )
    return rows


def make_mixed_case(rng: np.random.Generator, idx: int) -> tuple[HM, list[list[int]], dict[int, list[int]]]:
    k = 4
    block_sizes = [5, 4, 3, 4]
    blocks: list[list[int]] = []
    cursor = 0
    pis: list[np.ndarray] = []
    drop_sets: list[list[int]] = []
    for s, size in enumerate(block_sizes):
        block = list(range(cursor, cursor + size))
        cursor += size
        ndrop = 1 + (idx + s) % max(1, size - 2)
        raw_drop = np.array([10.0 ** (-(6 + ((idx + s + a) % 4))) for a in range(ndrop)])
        raw_drop *= 1.0 + 0.2 * rng.random(ndrop)
        survivor_raw = rng.random(size - ndrop) + 0.2
        survivor_raw /= survivor_raw.sum()
        survivor_raw *= 1.0 - float(raw_drop.sum())
        pi = np.concatenate([raw_drop, survivor_raw])
        pis.append(pi)
        blocks.append(block)
        drop_sets.append(block[:ndrop])

    transients = list(range(cursor, cursor + 5))
    alphas: dict[int, np.ndarray] = {}
    face_drop: dict[int, list[int]] = {}
    for offset, i in enumerate(transients):
        small_slots = sorted({(offset + idx) % k, (offset + 2 * idx + 1) % k})
        a = rng.random(k) + 0.1
        for s in small_slots:
            a[s] = 10.0 ** (-(5 + ((idx + offset + s) % 4)))
        a /= a.sum()
        alphas[i] = a
        face_drop[i] = [s for s in small_slots if a[s] < 5e-4]
    return HM(blocks, transients, pis, alphas, f"mixed_{idx}"), drop_sets, face_drop


def mixed_degenerations() -> dict:
    rng = np.random.default_rng(20260611)
    cases = []
    nonexpansive_failures = 0
    delta_failures = 0
    for idx in range(12):
        st, drop_sets, face_drop = make_mixed_case(rng, idx)
        rec = recode_hm(st, drop_sets, face_drop)
        P0 = build_p0(st)
        P1 = build_p0(rec.new)
        eps = row_l1_eps(P0, P1)
        bound = 2.0 * rec.removed_mass_budget
        residual = hm_residual(P1)

        for _ in range(50):
            x = rng.normal(size=st.n)
            z = rng.normal(size=st.n)
            rx = recurrent_compress_row(x, rec)
            rz = recurrent_compress_row(z, rec)
            if np.abs(rx - rz).sum() > np.abs(x - z).sum() + 1e-9:
                nonexpansive_failures += 1
            row = rng.normal(size=st.n)
            if delta(recurrent_compress(row.reshape(1, -1), rec)) > delta(row.reshape(1, -1)) + 1e-9:
                delta_failures += 1

        cases.append(
            {
                "case": st.name,
                "q": rec.q,
                "q_total": rec.q_total,
                "r_max": rec.r_max,
                "eps_recode": eps,
                "bound_2_removed": bound,
                "eps_over_bound": eps / bound if bound > 0 else 0.0,
                "mu_after": min_recurrent_mass(rec.new),
                "survivor_relative_shift": survivor_relative_shift(rec),
                "survivor_shift_bound_qmax": max(rec.q),
                "max_face_l1_shift": max((face_l1_shift(rec, i) for i in st.transients), default=0.0),
                "max_face_l1_bound": 2.0 * rec.r_max,
                "hm_residual": residual,
                "passes": (
                    eps <= bound + 1e-10
                    and survivor_relative_shift(rec) <= max(rec.q) + 1e-10
                    and max((face_l1_shift(rec, i) for i in st.transients), default=0.0) <= 2.0 * rec.r_max + 1e-10
                    and max(residual.values()) <= 1e-9
                ),
            }
        )
    return {
        "cases": cases,
        "nonexpansive_failures": nonexpansive_failures,
        "delta_nonincrease_failures": delta_failures,
    }


def second_order_boundary_summary() -> dict:
    candidates = [
        Path("/tmp/codex-sigma-wall/w21_second/second_order_full_records.json"),
        Path("/tmp/codex-sigma-wall/w21_second/second_order_fixed_window_results.json"),
    ]
    source = next((p for p in candidates if p.exists()), None)
    if source is None:
        return {"available": False}
    data = json.loads(source.read_text(encoding="utf-8"))
    records = data.get("records", [])
    local_ratios = []
    transition_ratios = []
    sharp_transition = []
    for rec in records:
        cutoff = 0.1 * float(rec.get("min_positive_entry", 0.0))
        for sample in rec.get("samples", []):
            ratio = sample.get("H_over_delta")
            if not isinstance(ratio, (int, float)) or not math.isfinite(float(ratio)):
                continue
            item = (float(ratio), rec, sample, cutoff)
            if float(sample["t"]) < cutoff:
                local_ratios.append(item)
            else:
                transition_ratios.append(item)
                if float(ratio) >= 1.9:
                    sharp_transition.append(item)
    local_ratios.sort(key=lambda x: x[0], reverse=True)
    transition_ratios.sort(key=lambda x: x[0], reverse=True)
    sharp_transition.sort(key=lambda x: x[0], reverse=True)
    top = []
    for ratio, rec, sample, cutoff in sharp_transition[:8]:
        top.append(
            {
                "ratio": ratio,
                "stratum": rec["stratum"],
                "source": rec["source"],
                "t": sample["t"],
                "min_positive_entry": rec["min_positive_entry"],
                "cutoff_0p1_min_entry": cutoff,
                "boundary_window_factor": float(sample["t"]) / float(rec["min_positive_entry"]),
                "visible": sample["visible"],
                "vertices": sample["vertices"],
            }
        )
    return {
        "available": True,
        "source": str(source),
        "records": len(records),
        "with_local_samples": len(local_ratios),
        "with_transition_samples": len(transition_ratios),
        "max_local_ratio": local_ratios[0][0] if local_ratios else None,
        "max_transition_ratio": transition_ratios[0][0] if transition_ratios else None,
        "sharp_transition_count_ratio_ge_1p9": len(sharp_transition),
        "top_sharp_transition": top,
    }


def write_summary(out: dict) -> str:
    lines: list[str] = []
    lines.append("w21 removed-mass recoding checks")
    lines.append("")
    lines.append("w20 audit stress family under repaired quantities")
    for row in out["audit_stress"]:
        lines.append(
            "{case}: q={q_total:.12g} q_alpha={q_alpha_max:.12g} "
            "eps={eps_recode:.12g} 2Q={bound_2_removed:.12g} eps/(2Q)={eps_over_2_removed:.6g} "
            "old eps/(mu_after/8)={old_eps_over_mu_after_div8:.6g} "
            "survivor_shift={survivor_relative_shift:.12g} qmax={survivor_shift_bound_qmax:.12g} "
            "face_l1={face_l1_shift:.12g} face_bound={face_l1_bound:.12g} "
            "passes={passes_removed_mass}/{passes_survivor_shift}/{passes_face_shift}".format(**row)
        )
    lines.append("")
    mixed = out["mixed_degenerations"]
    lines.append("mixed-rate recurrent and transient-face degenerations")
    lines.append(f"cases: {len(mixed['cases'])}")
    lines.append(f"nonexpansive_failures: {mixed['nonexpansive_failures']}")
    lines.append(f"delta_nonincrease_failures: {mixed['delta_nonincrease_failures']}")
    worst = max(mixed["cases"], key=lambda r: r["eps_over_bound"])
    lines.append(
        "worst eps/(2Q): {eps_over_bound:.6g} case={case} q_total={q_total:.12g} "
        "r_max={r_max:.12g} mu_after={mu_after:.12g} passes={passes}".format(**worst)
    )
    lines.append("")
    l3 = out["second_order_boundary"]
    lines.append("w21_second boundary-event filter")
    if not l3.get("available"):
        lines.append("available: false")
    else:
        lines.append(f"source: {l3['source']}")
        lines.append(f"records: {l3['records']}")
        lines.append(f"with_local_samples: {l3['with_local_samples']}")
        lines.append(f"max_local_ratio: {l3['max_local_ratio']}")
        lines.append(f"with_transition_samples: {l3['with_transition_samples']}")
        lines.append(f"max_transition_ratio: {l3['max_transition_ratio']}")
        lines.append(f"sharp_transition_count_ratio_ge_1p9: {l3['sharp_transition_count_ratio_ge_1p9']}")
        for row in l3["top_sharp_transition"]:
            lines.append(
                "sharp ratio={ratio:.12g} stratum={stratum} source={source} "
                "t={t:.3g} min_entry={min_positive_entry:.3g} "
                "t/min_entry={boundary_window_factor:.6g} visible={visible} vertices={vertices}".format(**row)
            )
    return "\n".join(lines) + "\n"


def main() -> None:
    out = {
        "audit_stress": audit_stress_cases(),
        "mixed_degenerations": mixed_degenerations(),
        "second_order_boundary": second_order_boundary_summary(),
    }
    Path("recode_removed_mass_results.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    text = write_summary(out)
    Path("recode_removed_mass_summary.txt").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
