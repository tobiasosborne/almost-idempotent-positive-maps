#!/usr/bin/env python3
"""
Red-green tests for scripts/check-provenance.py — prove the report<->registry sync gate actually
CATCHES drift (a renamed/removed label, a stale source hash, an undefined \\ref, a now-proved result
still framed "open") while PASSING the in-sync live repo.

"Runs without errors is never a passing test" — every check below asserts a verdict against a
known-correct value, and the load-bearing ones PERTURB a clean input to confirm it flips pass->fail
(port-and-verify). No external deps; run:
  python3 scripts/tests/test_check_provenance.py
"""
import importlib.util
import hashlib
import pathlib
import shutil
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
_spec = importlib.util.spec_from_file_location("check_provenance", ROOT / "scripts" / "check-provenance.py")
cp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cp)

passed = failed = 0


def check(name, cond):
    global passed, failed
    if cond:
        passed += 1
        print(f"PASS  {name}")
    else:
        failed += 1
        print(f"FAIL  {name}")


# -------------------------------------------------------------------------------------------------
# A) Pure helpers on synthetic inputs.
# -------------------------------------------------------------------------------------------------

# labels_of: explicit `report <label>` token, AND the first-hyphen->colon transform fallback.
check("labels_of reads an explicit `report <label>` token",
      cp.labels_of({"id": "lem-foo", "provenance": "bridge md:1; report lem:bar"}, {"lem:bar"}) == {"lem:bar"})
check("labels_of falls back to the id first-hyphen transform when the label exists",
      cp.labels_of({"id": "thm-baz", "provenance": ""}, {"thm:baz"}) == {"thm:baz"})
check("labels_of keeps uppercase slugs (lem-P-properties -> lem:P-properties)",
      cp.labels_of({"id": "lem-P-properties", "provenance": ""}, {"lem:P-properties"}) == {"lem:P-properties"})
check("labels_of returns nothing when neither token nor transform resolves",
      cp.labels_of({"id": "lem-qux", "provenance": ""}, set()) == set())

# forward labels: a registry token with no \label is an ERROR; a resolving one is clean.
check("forward: a `report <label>` with no \\label is flagged",
      len(cp.check_forward_labels([{"id": "a", "provenance": "report thm:gone"}], set())) == 1)
check("forward: a resolving `report <label>` is clean",
      cp.check_forward_labels([{"id": "a", "provenance": "report thm:ok"}], {"thm:ok"}) == [])

# claim labels: a per-claim row whose label is absent from the .tex is an ERROR.
check("claim labels: an absent per-claim label is flagged",
      len(cp.check_claim_labels([("thm:gone", "HOS")], set())) == 1)
check("claim labels: a resolving per-claim label is clean",
      cp.check_claim_labels([("thm:here", "HOS")], {"thm:here"}) == [])

# claim sources: unknown key flagged; mixed-case external citations are NOT mistaken for keys
# (this is the false-positive we fixed: Kadison1952 -> 'K', JvNW1934 -> 'J').
REG = {"HOS": ("p", "0" * 16), "VLW": ("p", "0" * 16)}
check("claim sources: a known key is clean", cp.check_claim_sources([("x", "HOS / VLW")], REG) == [])
check("claim sources: an UNKNOWN key is flagged",
      len(cp.check_claim_sources([("x", "B-GHOST")], REG)) == 1)
check("claim sources: external citation 'Kadison1952 / VLW' is NOT a false key error",
      cp.check_claim_sources([("x", "Kadison1952 / VLW")], REG) == [])
check("claim sources: external citation 'HOS / JvNW1934' is NOT a false key error",
      cp.check_claim_sources([("x", "HOS / JvNW1934")], REG) == [])
check("claim sources: marker words (ORIGINAL/elementary) are not keys",
      cp.check_claim_sources([("x", "ORIGINAL (consensus)"), ("y", "HOS / elementary")], REG) == [])

# source hashes: present-file mismatch is an ERROR (port-and-verify); malformed sha errors;
# absent -> warn; absolute path -> warn.
with tempfile.TemporaryDirectory() as td:
    tdp = pathlib.Path(td)
    (tdp / "src.md").write_text("the real source bytes", encoding="utf-8")
    real = hashlib.sha256((tdp / "src.md").read_bytes()).hexdigest()[:16]
    e, w = cp.check_source_hashes({"K": ("src.md", real)}, root=tdp)
    check("source hash: a fresh in-repo hash is clean (port)", e == [])
    e, w = cp.check_source_hashes({"K": ("src.md", "0" * 16)}, root=tdp)   # PERTURB the recorded hash
    check("source hash: a stale recorded hash flips to ERROR (verify RED)", len(e) == 1)
    e, w = cp.check_source_hashes({"K": ("src.md", "abc")}, root=tdp)
    check("source hash: a malformed (non-16-hex) sha is an ERROR", len(e) == 1)
    e, w = cp.check_source_hashes({"K": ("missing.md", "a" * 16)}, root=tdp)
    check("source hash: an absent payload warns (not a false error)", e == [] and len(w) == 1)
    e, w = cp.check_source_hashes({"K": ("/abs/foreign.md", "a" * 16)}, root=tdp)
    check("source hash: an absolute /home-style path warns (not refs/-relative)", e == [] and len(w) == 1)
    # tracked-set determinism: a present-but-untracked file (gitignored payload) only WARNS even if its
    # hash is wrong, so a clean CI checkout and a developer's populated tree reach the SAME verdict.
    e, w = cp.check_source_hashes([("K", "src.md", "0" * 16)], root=tdp, tracked=set())
    check("source hash: a present-but-UNTRACKED wrong hash only WARNS (clone-determinism)", e == [] and len(w) == 1)
    e, w = cp.check_source_hashes([("K", "src.md", "0" * 16)], root=tdp, tracked={"src.md"})
    check("source hash: a TRACKED file with a wrong hash still ERRORS", len(e) == 1)

# status drift returns (errors, warnings): OVERCLAIM (open framed non-open) is an ERROR (the project's
# #1 guarded failure mode); UNDERCLAIM (proved framed only-open) is a WARNING; a result merely CITED as
# the condition of a 'proved, cond.' row (op:npps) must NOT fire.
SH = [{"id": "op-foo", "provenance": "", "status": "open", "af": "none"},
      {"id": "thm-bar", "provenance": "", "status": "proved", "af": "validated"},
      {"id": "op-npps", "provenance": "", "status": "open", "af": "none"}]
TL = {"op:foo", "thm:bar", "op:npps"}
e, w = cp.check_status_drift([("proved", ["op:foo"])], SH, TL)
check("status OVERCLAIM (open result framed 'proved') is an ERROR, not a warning",
      any("op-foo" in m for m in e) and w == [])
e, w = cp.check_status_drift([("open", ["op:foo"])], SH, TL)
check("status drift: an open result framed 'open' is clean", e == [] and w == [])
e, w = cp.check_status_drift([("open", ["thm:bar"])], SH, TL)
check("status UNDERCLAIM (proved result framed only 'open') is a WARNING, not an error",
      e == [] and any("thm-bar" in m for m in w))
e, w = cp.check_status_drift([(r"proved, cond.\ (\cref{op:npps})", ["op:npps"]),
                              ("open", ["op:npps"])], SH, TL)
check("status drift: op-npps cited as a 'proved, cond.' CONDITION + its own open row does NOT fire",
      e == [] and w == [])

# anchor: a registry result mapping to zero report labels is surfaced (dropped/unlinked statement).
check("anchor: a shard mapping to NO report label warns",
      len(cp.check_anchor([{"id": "lem-orphan", "provenance": ""}], set())) == 1)
check("anchor: an anchored shard is clean",
      cp.check_anchor([{"id": "thm-x", "provenance": "report thm:x"}], {"thm:x"}) == [])

# broadened claim-source separators: a ';'-joined ghost key is no longer silently accepted.
check("claim sources: a ';'-joined ghost key is caught (HOS;GHOST)",
      len(cp.check_claim_sources([("x", "HOS;GHOST")], REG)) == 1)

# strip_tex_comment + tex_labels: a commented-out \label must NOT count as a live label.
check("strip_tex_comment drops a %-comment", cp.strip_tex_comment(r"\label{thm:x} % \label{thm:y}").strip() == r"\label{thm:x}")
check("strip_tex_comment honours an escaped \\%", cp.strip_tex_comment(r"50\% done") == r"50\% done")
with tempfile.TemporaryDirectory() as td:
    tdp = pathlib.Path(td)
    (tdp / "s.tex").write_text("\\label{thm:live}\n% \\label{thm:commented-out}\n", encoding="utf-8")
    labs = cp.tex_labels(tdp)
    check("tex_labels includes a live \\label", "thm:live" in labs)
    check("tex_labels EXCLUDES a \\label inside a %-comment", "thm:commented-out" not in labs)

# status_table_rows: split on UNescaped & + strip comments (a real false-green the reviewer found).
with tempfile.TemporaryDirectory() as td:
    tdp = pathlib.Path(td)
    (tdp / "11-discussion.tex").write_text(
        "\\midrule\n"
        "Tarski \\& friends theorem & open & \\Cref{thm:x} \\\\\n"
        "Foo % a comment with & and \\ref{thm:ghost}\n & proved & \\Cref{thm:y} \\\\\n"
        "\\bottomrule\n\\label{tab:status}\n", encoding="utf-8")
    rows = cp.status_table_rows(tdp)
    r_x = [r for r in rows if "thm:x" in r[1]][0]
    check("status table: an escaped \\& in a cell does not shift the status column", r_x[0] == "open")
    framed = {l for _, labs in rows for l in labs}
    check("status table: a \\ref inside a %-comment is not harvested as a framed label", "thm:ghost" not in framed)

# source hashes: EVERY row is hashed even when a key repeats (the B-ROUND fix) — port-and-verify.
with tempfile.TemporaryDirectory() as td:
    tdp = pathlib.Path(td)
    (tdp / "a.md").write_text("alpha", encoding="utf-8")
    (tdp / "b.md").write_text("beta", encoding="utf-8")
    ha = hashlib.sha256((tdp / "a.md").read_bytes()).hexdigest()[:16]
    hb = hashlib.sha256((tdp / "b.md").read_bytes()).hexdigest()[:16]
    e, w = cp.check_source_hashes([("B-ROUND", "a.md", ha), ("B-ROUND", "b.md", hb)], root=tdp)
    check("source hash: a key reused for TWO files hashes both (clean)", e == [])
    e, w = cp.check_source_hashes([("B-ROUND", "a.md", "0" * 16), ("B-ROUND", "b.md", hb)], root=tdp)
    check("source hash: a stale hash on the FIRST dup-keyed row is now caught (was silently dropped)", len(e) == 1)

# parse_provenance: dup key surfaced + both rows kept; BOM-tolerant frontmatter.
with tempfile.TemporaryDirectory() as td:
    pp = pathlib.Path(td) / "PROV.md"
    pp.write_text("## Ground-truth source registry\n\n| Key | Path | SHA | x |\n|---|---|---|---|\n"
                  "| `B-ROUND` | `a.md` | `1111111111111111` | x |\n"
                  "| `B-ROUND` (spin) | `b.md` | `2222222222222222` | x |\n\n"
                  "## Per-claim ledger\n\n| Report label | Source | Loc | St | Note |\n|---|---|---|---|---|\n"
                  "| thm:x | B-ROUND | l | O | n |\n", encoding="utf-8")
    p = cp.parse_provenance(pp)
    check("parse: source_rows keeps BOTH dup-keyed rows", len(p["source_rows"]) == 2)
    check("parse: a duplicate source key is surfaced as a parse warning", any("twice" in x for x in p["parse_warnings"]))
    check("parse: a clean per-claim row is parsed", p["claim_rows"] == [("thm:x", "B-ROUND")])
with tempfile.TemporaryDirectory() as td:
    f = pathlib.Path(td) / "lem-x.md"
    f.write_text("﻿---\nid: lem-x\nprovenance: report lem:x\n---\nbody\n", encoding="utf-8")
    fm = cp._frontmatter(f)
    check("_frontmatter tolerates a leading UTF-8 BOM", fm is not None and fm.get("id") == "lem-x")

# build-log scan: an undefined reference (a dangling \Cref to a renamed label) is an ERROR.
check("build log: 'undefined references' -> ERROR", len(cp.scan_build_log("There were undefined references.")[0]) == 1)
check("build log: a named undefined Reference is reported with the label",
      "thm:gone" in (cp.scan_build_log("LaTeX Warning: Reference `thm:gone' on page 3 undefined on input line 9.")[0][0]))
check("build log: a clean log is clean", cp.scan_build_log("Output written on main.pdf (12 pages).") == ([], []))
check("build log: undefined citations are a WARNING, not an error",
      cp.scan_build_log("There were undefined citations.") == ([], cp.scan_build_log("There were undefined citations.")[1]) and
      len(cp.scan_build_log("There were undefined citations.")[1]) == 1)


# -------------------------------------------------------------------------------------------------
# B) Integration on the REAL repo — the live invariant is ZERO semantic drift errors.
# -------------------------------------------------------------------------------------------------

shards, texlabels, prov, groups, errors, warnings = cp.run_semantic()
check("live repo invariant: ZERO report/registry drift errors (goes RED on real drift)", errors == [])
check("parses the full registry (>=59 results)", len(shards) >= 59)
check("parses the PROVENANCE per-claim ledger (>=70 rows)", len(prov["claim_rows"]) >= 70)
check("parses the source registry (>=30 sources)", len(prov["source_registry"]) >= 30)
gnames = {g[0] for g in groups}
check("runs all semantic checks", {"forward labels", "claim labels", "claim sources",
                                   "hash freshness", "status drift"} <= gnames)


# -------------------------------------------------------------------------------------------------
# C) Port-and-verify on LIVE data: clean now, PERTURB one value -> RED, confirming coupling to reality.
# -------------------------------------------------------------------------------------------------

real_shards = cp.parse_registry()
check("port: live forward-label check is green", cp.check_forward_labels(real_shards, texlabels) == [])
# perturb a real shard's report token to a bogus label -> must go RED
victim = next(s for s in real_shards if cp.REPORT_TOK.search(s.get("provenance", "")))
perturbed = dict(victim)
perturbed["provenance"] = victim.get("provenance", "") + " report thm:this-label-does-not-exist-zzz"
check("port: perturbing a shard to name a non-existent report label flips forward-check RED",
      len(cp.check_forward_labels([perturbed], texlabels)) == 1)

real_claims = prov["claim_rows"]
check("port: live claim-label check is green", cp.check_claim_labels(real_claims, texlabels) == [])
bad_claim = (real_claims[0][0] + "-zzz-removed", real_claims[0][1])
check("port: a per-claim row pointing at a removed label flips claim-check RED",
      len(cp.check_claim_labels([bad_claim], texlabels)) == 1)


# -------------------------------------------------------------------------------------------------
# D) Build integration (guarded): the real report compiles clean AND run_build does NOT mutate the
#    tracked report/main.pdf (it must build into the scratch dir). Skips cleanly if latexmk is absent.
# -------------------------------------------------------------------------------------------------

if shutil.which("latexmk"):
    pdf = ROOT / "report" / "main.pdf"
    before = hashlib.sha256(pdf.read_bytes()).hexdigest() if pdf.is_file() else None
    be, bw = cp.run_build()
    after = hashlib.sha256(pdf.read_bytes()).hexdigest() if pdf.is_file() else None
    check("run_build: the real report compiles with NO undefined references", be == [])
    check("run_build: the tracked report/main.pdf is NOT mutated by the gate build", before == after)
else:
    check("run_build: latexmk absent -> clean warn-skip (no error)", cp.run_build()[0] == [])

print(f"\n{passed} passed, {failed} failed")
raise SystemExit(1 if failed else 0)
