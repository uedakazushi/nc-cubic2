#!/usr/bin/env python3
"""Check the current point-scheme paper; optionally run its four finite checks.

This is a source/reference and finite-algebra check, not a proof verifier.
Run from any directory; no network or GitHub Actions are used.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
ENTRY = "papers/mixed_cubic_point_schemes.tex"
CHECKS = (
    "verify_mixed_test_family.py",
    "verify_point_scheme_thickening.py",
    "verify_lambda_point_scheme.py",
    "verify_lambda_discriminant.py",
)


def strip_comments(text: str) -> str:
    return re.sub(r"(?<!\\)%[^\n]*", "", text)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--calculations", action="store_true")
    parser.add_argument("--build", action="store_true")
    args = parser.parse_args()
    sources: dict[str, str] = {}
    blobs: dict[str, str] = {}

    def visit(relative: str) -> None:
        path = (ROOT / relative).resolve()
        if not path.is_relative_to(ROOT):
            raise ValueError(f"Input outside repository: {relative}")
        key = path.relative_to(ROOT).as_posix()
        if key in sources:
            raise ValueError(f"Repeated TeX input: {key}")
        data = path.read_bytes()
        text = strip_comments(data.decode("utf-8"))
        sources[key] = text
        blobs[key] = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        for child in re.findall(r"\\input\{([^}]+)\}", text):
            visit(child if child.endswith(".tex") else child + ".tex")

    visit(ENTRY)
    text = "\n".join(sources.values())
    labels = re.findall(r"\\label\{([^}]+)\}", text)
    refs = re.findall(r"\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}", text)
    cites = [key.strip() for group in re.findall(r"\\cite(?:\[[^]]*\])*\{([^}]+)\}", text)
             for key in group.split(",")]
    bib = re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}", text)
    errors = {
        "duplicate_labels": sorted(k for k, n in Counter(labels).items() if n > 1),
        "duplicate_bibitems": sorted(k for k, n in Counter(bib).items() if n > 1),
        "undefined_references": sorted(set(refs) - set(labels)),
        "undefined_citations": sorted(set(cites) - set(bib)),
    }
    if any(errors.values()):
        raise ValueError(json.dumps(errors, ensure_ascii=False))
    if args.calculations:
        with tempfile.TemporaryDirectory(prefix="nc-cubic-point-check-") as tmp:
            for name in CHECKS:
                subprocess.run([sys.executable, str(ROOT / "computations" / name),
                                "--output", str(Path(tmp) / (Path(name).stem + ".json"))],
                               cwd=ROOT, check=True)
    if args.build:
        subprocess.run(["latexmk", "-g", "-r", ".latexmkrc", ENTRY], cwd=ROOT, check=True)
    report = {
        "status": "PASS", "entry": ENTRY, "tex_files": len(sources),
        "labels": len(labels), "references": len(refs), "citations": len(cites),
        "bibliography_entries": len(bib), "errors": errors, "source_blobs": blobs,
        "finite_calculations_run": args.calculations,
        "latexmk_run": args.build,
        "proof_verification": False,
    }
    out = ROOT / "build" / "mixed_point_schemes_check.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: {len(sources)} TeX files, {len(labels)} labels, {len(refs)} references")


if __name__ == "__main__":
    main()
