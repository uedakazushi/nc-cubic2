#!/usr/bin/env python3
"""Check source closure and optional exact dg-model arithmetic/build.

No network or GitHub Actions. This is not a mathematical proof verifier.
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
ENTRY = 'papers/cubic_artin_windows.tex'


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--calculations', action='store_true')
    ap.add_argument('--build', action='store_true')
    ap.add_argument('--entry', choices=[ENTRY, 'papers/proper_dg_smoothness_and_artin_limits.tex'], default=ENTRY)
    args = ap.parse_args()
    sources: dict[str, str] = {}
    blobs: dict[str, str] = {}

    def visit(relative: str) -> None:
        path = (ROOT / relative).resolve()
        if not path.is_relative_to(ROOT):
            raise ValueError(f'Input outside repository: {relative}')
        key = path.relative_to(ROOT).as_posix()
        if key in sources:
            raise ValueError(f'Repeated input: {key}')
        data = path.read_bytes()
        sources[key] = re.sub(r'(?<!\\)%[^\n]*', '', data.decode('utf-8'))
        blobs[key] = hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        for name in re.findall(r'\\input\{([^}]+)\}', sources[key]):
            visit(name if name.endswith('.tex') else name+'.tex')

    visit(args.entry)
    text = '\n'.join(sources.values())
    labels = re.findall(r'\\label\{([^}]+)\}', text)
    refs = re.findall(r'\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}', text)
    cites = [k.strip() for group in re.findall(r'\\cite(?:\[[^]]*\])*\{([^}]+)\}', text)
             for k in group.split(',')]
    bib = re.findall(r'\\bibitem(?:\[[^]]*\])?\{([^}]+)\}', text)
    errors = {
        'duplicate_labels': [k for k, n in Counter(labels).items() if n > 1],
        'duplicate_bibitems': [k for k, n in Counter(bib).items() if n > 1],
        'undefined_references': sorted(set(refs)-set(labels)),
        'undefined_citations': sorted(set(cites)-set(bib)),
    }
    if any(errors.values()):
        raise ValueError(json.dumps(errors, ensure_ascii=False))
    if args.calculations:
        subprocess.run([sys.executable, str(ROOT/'computations/verify_artin_dg_model.py'),
                        '--output', str(ROOT/'build/artin_dg_model_check.json')], cwd=ROOT, check=True)
    if args.build:
        subprocess.run(['latexmk', '-g', '-r', '.latexmkrc', args.entry], cwd=ROOT, check=True)
    report = {
        'status': 'PASS', 'entry': args.entry, 'tex_files': len(sources),
        'labels': len(labels), 'references': len(refs), 'citations': len(cites),
        'bibliography_entries': len(bib), 'errors': errors, 'source_blobs': blobs,
        'calculations_run': args.calculations, 'latexmk_run': args.build,
        'mathematical_proof_verification': False,
    }
    out = ROOT/'build'/(Path(args.entry).stem+'_check.json')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
