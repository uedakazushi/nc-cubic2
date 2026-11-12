#!/usr/bin/env python3
"""Check TeX references, optional sector arithmetic, and optional LuaLaTeX build.

This is a source/reproduction checker, not a mathematical proof verifier.
No network, GitHub Actions, source deletion, commit, or push is performed.
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
ENTRY = 'papers/relative_cubic_realization.tex'
EXPECTED_CERTIFICATE = '8e7a35337e43b45fc26b04c11414554732213ea4'


def git_blob(data: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()


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
            raise ValueError(f'Input outside the repository: {relative}')
        key = path.relative_to(ROOT).as_posix()
        if key in sources:
            raise ValueError(f'Duplicate or circular TeX input: {key}')
        data = path.read_bytes()
        text = re.sub(r'(?<!\\)%[^\n]*', '', data.decode('utf-8'))
        sources[key] = text
        blobs[key] = git_blob(data)
        for child in re.findall(r'\\input\{([^}]+)\}', text):
            visit(child if child.endswith('.tex') else child + '.tex')

    visit(ENTRY)
    text = '\n'.join(sources.values())
    labels = re.findall(r'\\label\{([^}]+)\}', text)
    refs = re.findall(r'\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}', text)
    cites = [key.strip() for group in re.findall(r'\\cite(?:\[[^]]*\])*\{([^}]+)\}', text)
             for key in group.split(',')]
    bib = re.findall(r'\\bibitem(?:\[[^]]*\])?\{([^}]+)\}', text)
    errors = {
        'duplicate_labels': sorted(k for k, n in Counter(labels).items() if n > 1),
        'duplicate_bibitems': sorted(k for k, n in Counter(bib).items() if n > 1),
        'undefined_references': sorted(set(refs) - set(labels)),
        'undefined_citations': sorted(set(cites) - set(bib)),
    }
    if any(errors.values()):
        raise ValueError(json.dumps(errors, ensure_ascii=False))

    calc = {'executed': False}
    if args.calculations:
        with tempfile.TemporaryDirectory(prefix='relative-cubic-check-') as directory:
            certificate = Path(directory) / 'sectors.json'
            process = subprocess.run(
                [sys.executable, str(ROOT / 'computations/verify_hochschild_sectors.py'),
                 '--output', str(certificate)], cwd=ROOT, check=True,
                capture_output=True, text=True)
            data = certificate.read_bytes()
            actual = git_blob(data)
            if actual != EXPECTED_CERTIFICATE:
                raise ValueError(f'Sector certificate differs: {actual}')
            calc = {'executed': True, 'certificate_blob': actual,
                    'exact_source_certificate_reproduced': True,
                    'range_N': [5, 60], 'stdout': process.stdout.strip(),
                    'scope': 'Integer bookkeeping of the quoted BFK formula, not a proof of it.'}

    build: dict = {'executed': False}
    if args.build:
        process = subprocess.run(['latexmk', '-g', '-r', '.latexmkrc', ENTRY],
                                 cwd=ROOT, capture_output=True, text=True)
        build_dir = ROOT / 'build'
        build_dir.mkdir(parents=True, exist_ok=True)
        (build_dir / 'relative_cubic_build_output.txt').write_text(
            process.stdout + '\n' + process.stderr, encoding='utf-8')
        if process.returncode:
            raise RuntimeError('latexmk failed; see build/relative_cubic_build_output.txt')
        log = (build_dir / 'relative_cubic_realization.log').read_text(encoding='utf-8')
        checks = {
            'undefined_references_or_citations': len(re.findall(r'(?:Reference|Citation).*undefined|There were undefined references', log)),
            'multiply_defined_labels': len(re.findall(r'multiply defined|multiply-defined', log)),
            'missing_characters': log.count('Missing character:'),
            'overfull_boxes': log.count('Overfull \\'),
        }
        if any(checks.values()):
            raise ValueError(json.dumps(checks, ensure_ascii=False))
        matches = re.findall(r'Output written on .*?\((\d+) pages?', log, flags=re.S)
        pdf = build_dir / 'relative_cubic_realization.pdf'
        build = {'executed': True, 'engine': 'LuaLaTeX',
                 'pages': int(matches[-1]) if matches else None,
                 'log_checks': checks,
                 'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
                 'visual_review_by_this_script': False}
    report = {'status': 'PASS', 'entry': ENTRY, 'tex_files': len(sources),
              'labels': len(labels), 'references': len(refs), 'citations': len(cites),
              'bibliography_entries': len(bib), 'errors': errors, 'source_blobs': blobs,
              'calculations': calc, 'build': build, 'proof_verification': False}
    out = ROOT / 'build/relative_cubic_realization_check.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
