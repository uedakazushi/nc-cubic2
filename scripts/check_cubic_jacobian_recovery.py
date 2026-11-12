#!/usr/bin/env python3
"""Audit the finite Jacobian paper and optionally rerun rational computations.

No network access, GitHub Actions, or mathematical proof verification.
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
ENTRY = "papers/cubic_jacobian_recovery.tex"


def git_blob(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


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
        text = re.sub(r"(?<!\\)%[^\n]*", "", data.decode("utf-8"))
        sources[key] = text
        blobs[key] = git_blob(data)
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
    computation = None
    if args.calculations:
        with tempfile.TemporaryDirectory(prefix="cubic-jacobian-check-") as tmp:
            cert = Path(tmp) / "certificate.json"
            subprocess.run([sys.executable, str(ROOT / "computations" /
                "verify_explicit_jacobian_recovery.py"), "--output", str(cert)],
                cwd=ROOT, check=True)
            result = json.loads(cert.read_text())
            examples = result["examples"]
            if [e["integrability_matrix_rank"] for e in examples] != [20, 24, 25]:
                raise AssertionError("Unexpected exact ranks")
            if examples[-1]["full_rank_minor_determinant"] != "15872":
                raise AssertionError("Unexpected obstruction certificate")
            if not result["nonsymmetric_product_rejected_before_Sym2"]:
                raise AssertionError("Asymmetry rejection failed")
            computation = {"ranks": [20, 24, 25], "kernel_dimensions": [5, 1, 0],
                           "obstruction_minor": "15872", "nonsymmetric_input_rejected": True}
    if args.build:
        subprocess.run(["latexmk", "-g", "-r", ".latexmkrc", ENTRY], cwd=ROOT, check=True)
    report = {
        "status": "PASS", "entry": ENTRY, "tex_files": len(sources),
        "labels": len(labels), "references": len(refs), "citations": len(cites),
        "bibliography_entries": len(bib), "errors": errors, "source_blobs": blobs,
        "calculation": computation, "latexmk_run": args.build,
        "mathematical_proof_verification": False,
    }
    out = ROOT / "build" / "cubic_jacobian_recovery_check.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: {len(sources)} TeX files, {len(labels)} labels, {len(refs)} references")


if __name__ == "__main__":
    main()
