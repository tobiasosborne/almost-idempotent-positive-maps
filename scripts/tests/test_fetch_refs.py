#!/usr/bin/env python3
"""
Offline red-green tests for scripts/fetch-refs.py — prove the reconstruct/cache logic NEVER installs a
file whose bytes do not hash to the recorded sha256, restores a bespoke file from a content-addressed
cache, and that --populate-cache seeds the cache by hash. (The arXiv network fetch is exercised live,
like check-provenance's latexmk build, not unit-tested.)

  python3 scripts/tests/test_fetch_refs.py
"""
import hashlib
import importlib.util
import pathlib
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
_spec = importlib.util.spec_from_file_location("fetch_refs", ROOT / "scripts" / "fetch-refs.py")
fr = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fr)

passed = failed = 0


def check(name, cond):
    global passed, failed
    if cond:
        passed += 1
        print(f"PASS  {name}")
    else:
        failed += 1
        print(f"FAIL  {name}")


def sha(b):
    return hashlib.sha256(b).hexdigest()


# --- the real lock parses and is internally consistent ---
files = fr.load_lock()
check("load_lock reads all 53 refs files", len(files) == 53)
check("every lock entry has a 64-hex sha256", all(len(f["sha256"]) == 64 for f in files))
fetchable = [f for f in files if f.get("fetch")]
check("18 files are fetch-reproducible (kitaev + vlw + ES + baak-moslehian + blecher-read + baake-sumner)", len(fetchable) == 18)
check("every fetch spec is well-formed (arxiv kind has an id; url kind has a url)",
      all((f["fetch"]["kind"].startswith("arxiv") and f["fetch"].get("id"))
          or (f["fetch"]["kind"] == "url" and f["fetch"].get("url")) for f in fetchable))

# --- cache_lookup: a correct blob verifies; a WRONG-content blob is rejected; a miss is None ---
with tempfile.TemporaryDirectory() as td:
    cache = pathlib.Path(td)
    good = b"the real source bytes"
    h = sha(good)
    (cache / h).write_bytes(good)
    check("cache_lookup returns bytes for a hash-correct blob", fr.cache_lookup(h, cache_dir=cache) == good)
    # a blob whose NAME is the sha but whose CONTENT differs (corruption / tampering) is refused
    bad_h = sha(b"x")
    (cache / bad_h).write_bytes(b"not what the hash says")
    check("cache_lookup REFUSES a corrupted blob (name != content hash)", fr.cache_lookup(bad_h, cache_dir=cache) is None)
    check("cache_lookup misses cleanly", fr.cache_lookup(sha(b"absent"), cache_dir=cache) is None)

# --- reconstruct (offline, cache-only entries): present / restored / MISSING + verified install ---
with tempfile.TemporaryDirectory() as td:
    refs = pathlib.Path(td) / "refs"
    cache = pathlib.Path(td) / "cache"
    refs.mkdir()
    cache.mkdir()
    b_present = b"already here and valid"
    b_cached = b"only in the cache"
    b_missing = b"nowhere"
    L = [
        {"path": "p/present.txt", "sha256": sha(b_present), "fetch": None},
        {"path": "c/cached.txt", "sha256": sha(b_cached), "fetch": None},
        {"path": "m/missing.txt", "sha256": sha(b_missing), "fetch": None},
    ]
    (refs / "p").mkdir()
    (refs / "p" / "present.txt").write_bytes(b_present)        # already valid on disk
    (cache / sha(b_cached)).write_bytes(b_cached)              # available in the CAS
    rows = dict(fr.reconstruct(L, refs_dir=refs, cache_dir=cache, write=True, allow_fetch=False))
    check("reconstruct: an on-disk valid file is 'present'", rows["p/present.txt"] == "present")
    check("reconstruct: a cache-only file is 'restored'", rows["c/cached.txt"] == "restored")
    check("reconstruct: a no-source file is 'MISSING'", rows["m/missing.txt"] == "MISSING")
    restored = refs / "c" / "cached.txt"
    check("reconstruct INSTALLS the restored file, hash-verified",
          restored.is_file() and sha(restored.read_bytes()) == sha(b_cached))
    check("reconstruct does NOT create the missing file", not (refs / "m" / "missing.txt").exists())

    # port-and-verify: corrupt the cache blob -> restore must REFUSE (never install bad bytes)
    (restored).unlink()
    (cache / sha(b_cached)).write_bytes(b"TAMPERED")
    rows2 = dict(fr.reconstruct(L, refs_dir=refs, cache_dir=cache, write=True, allow_fetch=False))
    check("reconstruct REFUSES a tampered cache blob (goes MISSING, installs nothing)",
          rows2["c/cached.txt"] == "MISSING" and not restored.exists())

# --- populate_cache seeds a CAS by sha from present+valid files only ---
with tempfile.TemporaryDirectory() as td:
    refs = pathlib.Path(td) / "refs"
    cas = pathlib.Path(td) / "cas"
    refs.mkdir()
    b1 = b"file one"
    L = [{"path": "a.txt", "sha256": sha(b1), "fetch": None},
         {"path": "absent.txt", "sha256": sha(b"two"), "fetch": None}]
    (refs / "a.txt").write_bytes(b1)
    n, skipped = fr.populate_cache(L, cas, refs_dir=refs)
    check("populate_cache writes one blob for the present file", n == 1 and (cas / sha(b1)).is_file())
    check("populate_cache skips the absent file", skipped == 1)
    check("populated blob is content-addressed (named by its sha)", sha((cas / sha(b1)).read_bytes()) == sha(b1))

print(f"\n{passed} passed, {failed} failed")
raise SystemExit(1 if failed else 0)
