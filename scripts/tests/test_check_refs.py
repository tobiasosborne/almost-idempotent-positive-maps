#!/usr/bin/env python3
"""
Red-green tests for scripts/check-refs.py — prove the provenance gate actually CATCHES a fabricated
"VERBATIM" quote (a paraphrase of a true fact mis-attributed to a refs/ locus) while PASSING a real
verbatim quote, and correctly SKIPS import-externals and no-quote externals.

"Runs without errors is never a passing test" — these assert the verdicts against known-correct values,
including the two real known fabrications in the repo (square-hole + bridge-polar GT-bhsa-jc) and a
synthetic fixture that we PERTURB to confirm pass->fail (port-and-verify). No external deps; run:
  python3 scripts/tests/test_check_refs.py
"""
import importlib.util
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent

# import the hyphenated gate module by path
_spec = importlib.util.spec_from_file_location("check_refs", ROOT / "scripts" / "check-refs.py")
cr = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cr)

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
# A) Unit tests on the pure helpers (no filesystem) — normalization + the matcher.
# -------------------------------------------------------------------------------------------------

REAL = ('Let H be a complex Hilbert space and B(H) the algebra of all bounded linear operators on H. '
        'By a JC algebra we shall mean any norm-closed Jordan subalgebra of $B(H)_{\\rm sa}$.')
FABRICATION = ('If A is a $C^*$ algebra then $A_{sa}$ with the Jordan product '
               '$a \\circ b = \\frac{1}{2}(ab+ba)$ is a JB algebra.')

tn_real = cr.normalize("intro words. " + REAL + " more text after.")

ok, chunk = cr.longest_run_match(cr.normalize(REAL), tn_real)
check("real verbatim quote matches its source text", ok and len(chunk) >= cr.MIN_RUN)

ok, _ = cr.longest_run_match(cr.normalize(FABRICATION), tn_real)
check("fabricated quote does NOT match a source that lacks those words", not ok)

# markdown noise (emphasis * and dollar-escaping \$) must NOT break a real match
ok, _ = cr.longest_run_match(
    cr.normalize("T is called positive, if for all $A \\ge 0$, $T(A) \\ge 0$."),
    cr.normalize("*T* is called *positive*, if for all  $A \\ge 0$ ,  $T(A) \\ge 0$ . Then"))
check("markdown emphasis/whitespace noise tolerated (formatting, not words)", ok)

# A WHOLESALE fabrication (a paraphrase of a true fact — the real-world fabrication mode, and what the
# two known repo cases are) leaves NO distinctive >=40-char run intact and is CAUGHT.
ok, _ = cr.longest_run_match(
    cr.normalize("If A is a $C^*$ algebra then $A_{sa}$ with the Jordan product is a JB algebra."),
    cr.normalize("*T* is called *positive*, if for all  $A \\ge 0$ ,  $T(A) \\ge 0$ . Then"))
check("a wholesale paraphrase (no distinctive run survives) is caught", not ok)

# A word swap inside a SHORT quote (whose only distinctive content IS that run) is caught: with the
# swap there is no >=40-char run that survives, and a short quote must match in WHOLE.
short_src = "$T(A) \\le 0$ for all positive A, a definition."   # source says \\ge, quote claims \\le
ok, _ = cr.longest_run_match(
    cr.normalize(short_src),
    cr.normalize("Recall $T(A) \\ge 0$ for all positive A, a definition. Next..."))
check("a word swap in a short quote (no surviving long run) is caught", not ok)

# extraction prefers the VERBATIM-tagged quote
q = cr.extract_quote('HOS, refs/x.md:1, VERBATIM: "the real claim". NOTE: "a longer aside not the quote"')
check("extract_quote prefers the VERBATIM run", q == "the real claim")


# -------------------------------------------------------------------------------------------------
# B) Integration on the REAL repo workspaces — the live invariant is ZERO fabricated quotes
#    (fail_count == 0); the now-corrected (R5) GT-bhsa-jc externals PASS, an import-external is
#    skip_import, a no-quote external is skip_noquote. The matcher's red->green (its ability to FLAG a
#    fabrication) is the stable synthetic fixture/perturbation in section C — not coupled to live state.
# -------------------------------------------------------------------------------------------------

rows, fail_count, skip_count = cr.check_refs()
by = {(r["workspace"], r["external"]): r["verdict"] for r in rows}


def verdict(ws, name):
    return by.get((ws, name))


check("square-hole GT-bhsa-jc PASSES (R5 fabrication corrected)",
      verdict("lem-square-hole-almost-positive", "GT-bhsa-jc") == "pass")
check("bridge-polar GT-bhsa-jc PASSES (R5 fabrication corrected)",
      verdict("lem-bridge-polar", "GT-bhsa-jc") == "pass")
check("orderunit GT-bhsa-jc PASSES (real verbatim quote)",
      verdict("lem-bridge-orderunit", "GT-bhsa-jc") == "pass")
check("an import-external is skip_import (GT-Pprops -> proofs/lem-P-properties)",
      verdict("lem-bridge-easy", "GT-Pprops") == "skip_import")
check("a no-quote external is skip_noquote (GT-order-unit-norm has a locus but no quote)",
      verdict("lem-P-properties", "GT-order-unit-norm") == "skip_noquote")
check("live repo invariant: ZERO fabricated/mismatched external quotes (goes RED if anyone re-fabricates)",
      fail_count == 0)
check("check_refs returns rows for every external in every workspace", len(rows) >= 60)


# -------------------------------------------------------------------------------------------------
# C) Port-and-verify on a synthetic external: a clean quote PASSES, then PERTURB one word -> FAIL.
#    (We drive classify_and_check directly with a freeform source referencing a real refs/ file.)
# -------------------------------------------------------------------------------------------------

# A SHORT, fully-distinctive quote at a real locus: it must match in whole (no >=40-char sub-run to
# fall back on), so a single word swap flips pass->fail. ("Jordan subalgebra of $B(H)_{\\rm sa}$" is
# verbatim at 3.1.2.)
GOOD_SRC = ('HOS, refs/hos/joa-m.md:2300 (3.1.2), VERBATIM: '
            '"norm-closed Jordan subalgebra of $B(H)_{\\rm sa}$"')
res = cr.classify_and_check("GT-test", GOOD_SRC, {})
check("synthetic good short quote -> pass (port)", res["verdict"] == "pass")

# perturb an INTERIOR word: "Jordan" -> "Banach" — a word-level fabrication at the SAME real locus.
# This splits the quote so neither surviving real run ("norm-closed", "subalgebra of $B(H)_{\\rm sa}$")
# reaches MIN_RUN, so it flips pass -> fail.
BAD_SRC = GOOD_SRC.replace("Jordan", "Banach")
res = cr.classify_and_check("GT-test", BAD_SRC, {})
check("perturbed short quote -> fail (verify it goes RED)", res["verdict"] == "fail")
check("a perturbed fail records the claimed snippet", bool(res["claimed_quote_snippet"]))

# an absent refs file -> skip_noquote with a warning (cannot verify), not a false fail
res = cr.classify_and_check("GT-x", 'refs/does/not/exist.md:1, VERBATIM: "anything at all here"', {})
check("absent refs file -> skip_noquote (cannot verify, not a false fail)",
      res["verdict"] == "skip_noquote" and "ABSENT" in res["note"])

print(f"\n{passed} passed, {failed} failed")
raise SystemExit(1 if failed else 0)
