#!/usr/bin/env python3
"""
Red-green tests for scripts/check-defs.py — prove the Definitions DB gate actually CATCHES
drift, bad hashes, missing fields, and id mismatch ("runs without errors is never a passing
test"). No external deps; run: python3 scripts/tests/test_check_defs.py
"""
import importlib.util
import pathlib
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
MANIFEST = ROOT / "refs" / "manifest" / "checksums.sha256"  # real manifest (read-only)
HOS_SHA = "28740e73d547dd46"  # real prefix of refs/hos/joa-m.md (source-id: hos)

# import the hyphenated gate module by path
_spec = importlib.util.spec_from_file_location("check_defs", ROOT / "scripts" / "check-defs.py")
cd = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cd)

GOOD_CITED = (
    "---\nid: def-alpha\nterm: Alpha\naliases: A\nkind: cited\nstatus: locked\n"
    f"source: hos\nlocus: joa-m.md:1\nsha256: {HOS_SHA}\nconsensus: -\n---\nbody\n"
)
GOOD_CONSENSUS = (
    "---\nid: def-beta\nterm: Beta\nkind: consensus\nstatus: locked\n"
    "source: internal\nsha256: -\nconsensus: A+B\n---\nbody\n"
)

passed = failed = 0
def check(name, cond):
    global passed, failed
    if cond:
        passed += 1; print(f"PASS  {name}")
    else:
        failed += 1; print(f"FAIL  {name}")

def run(files):
    with tempfile.TemporaryDirectory() as d:
        d = pathlib.Path(d)
        for fn, content in files.items():
            (d / fn).write_text(content, encoding="utf-8")
        return cd.check_defs(d, MANIFEST, generate_index=False)

def has(msgs, sub):
    return any(sub in m for m in msgs)

# 1. GREEN: two valid shards -> no errors
e, w, p = run({"def-alpha.md": GOOD_CITED, "def-beta.md": GOOD_CONSENSUS})
check("valid DB has no errors", e == [])
check("valid DB parsed 2 shards", len(p) == 2)

# 2. RED: drift — two shards claim the same alias 'A'
drift = GOOD_CONSENSUS.replace("term: Beta\n", "term: Beta\naliases: A\n")
e, w, p = run({"def-alpha.md": GOOD_CITED, "def-beta.md": drift})
check("drift collision is caught", has(e, "DRIFT"))

# 3. RED: missing required field 'kind'
nokind = GOOD_CONSENSUS.replace("kind: consensus\n", "")
e, w, p = run({"def-beta.md": nokind})
check("missing 'kind' is caught", has(e, "missing required field 'kind'"))

# 4. RED: cited sha256 not in the manifest
badsha = GOOD_CITED.replace(HOS_SHA, "deadbeefdeadbeef")
e, w, p = run({"def-alpha.md": badsha})
check("bad sha256 is caught", has(e, "not in refs manifest"))

# 5. RED: id does not match filename stem
e, w, p = run({"def-gamma.md": GOOD_CITED})  # frontmatter id is def-alpha
check("id/filename mismatch is caught", has(e, "!= filename stem"))

# 6. RED: cited source not a known refs source-id
badsrc = GOOD_CITED.replace("source: hos\n", "source: nope\n")
e, w, p = run({"def-alpha.md": badsrc})
check("unknown cited source is caught", has(e, "not a refs/ source-id"))

# 7. WARN (not error): consensus shard left as draft
draft = GOOD_CONSENSUS.replace("status: locked\n", "status: draft\n")
e, w, p = run({"def-beta.md": draft})
check("draft shard warns, not errors", e == [] and has(w, "status=draft"))

print(f"\n{passed} passed, {failed} failed")
raise SystemExit(1 if failed else 0)
