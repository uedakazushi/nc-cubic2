#!/usr/bin/env python3
"""Check the standalone first-order cubic paper and its finite tests.

Source closure and symbolic calculations are not categorical proof verification.
No network, GitHub Actions, or PDF tracking is used.
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

ROOT = Path(__file__).resolve().parents[1]
ENTRY = 'papers/cubic_first_order_deformations.tex'
CHECKS = ('verify_first_order_curved_kernel.py', 'verify_second_order_plucker.py')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--calculations', action='store_true')
    parser.add_argument('--build', action='store_true')
    args = parser.parse_args()
    sources: dict[str, str] = {}
    blobs: dict[str, str] = {}

    def visit(relative: str) -> None:
        path = (ROOT / relative).resolve()
        if not path.is_relative_to(ROOT):
            raise ValueError(f'Input outside repository: {relative}')
        key = path.relative_to(ROOT).as_posix()
        if key in sources:
            raise ValueError(f'Repeated TeX input: {key}')
        data = path.read_bytes()
        text = re.sub(r'(?<!\\)%[^\n]*', '', data.decode('utf-8'))
        sources[key] = text
        blobs[key] = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
        for child in re.findall(r'\\input\{([^}]+)\}', text):
            visit(child if child.endswith('.tex') else child + '.tex')

    visit(ENTRY)
    text = '\n'.join(sources.values())
    labels = re.findall(r'\\label\{([^}]+)\}', text)
    refs = re.findall(r'\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}', text)
    cites = [k.strip() for group in re.findall(r'\\cite(?:\[[^]]*\])*\{([^}]+)\}', text)
             for k in group.split(',')]
    bib = re.findall(r'\\bibitem(?:\[[^]]*\])?\{([^}]+)\}', text)
    errors = {
        'duplicate_labels': sorted(k for k, n in Counter(labels).items() if n > 1),
        'duplicate_bibitems': sorted(k for k, n in Counter(bib).items() if n > 1),
        'undefined_references': sorted(set(refs) - set(labels)),
        'undefined_citations': sorted(set(cites) - set(bib)),
    }
    if any(errors.values()):
        raise ValueError(json.dumps(errors, ensure_ascii=False))
    calculations = {}
    if args.calculations:
        for name in CHECKS:
            process = subprocess.run([sys.executable, str(ROOT / 'computations' / name)],
                                     cwd=ROOT, check=True, capture_output=True, text=True)
            calculations[name] = process.stdout.strip()
    if args.build:
        subprocess.run(['latexmk', '-g', '-r', '.latexmkrc', ENTRY], cwd=ROOT, check=True)
    report = {
        'status': 'PASS', 'entry': ENTRY, 'tex_files': len(sources),
        'labels': len(labels), 'references': len(refs), 'citations': len(cites),
        'bibliography_entries': len(bib), 'errors': errors, 'source_blobs': blobs,
        'calculations': calculations, 'latexmk_run': args.build,
        'proof_verification': False,
    }
    output = ROOT / 'build' / 'cubic_first_order_check.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
