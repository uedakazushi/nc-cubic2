#!/usr/bin/env python3
"""Check the current integrated manuscript; finite calculations do not audit proofs."""
from pathlib import Path
from collections import Counter
import argparse
import concurrent.futures
import hashlib
import json
import re
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
ENTRY = 'papers/relative_reconstruction_models.tex'
OUTPUT_CHECKS = '''finite_recovery curved_diagonal regular_diagonal bar_comparison
artin_sectors diagonal_identity artin_rotation_obstructions central_symmetry
geometric_rotation one_sided_morita rotation_orbit explicit_model_comparison
kontsevich_second_jet mixed_test_family minimal_ainfty_arity complete_curved_transport
generic_cubic_descent three_object_window etale_inputs nonelliptic_inputs hochschild_sectors'''.split()
PLAIN_CHECKS = '''general_dimension_multiblock local_projective_model reconstruction
rotation_obstructions componentwise_reconstruction mixed_characters algebra poisson_second_jet'''.split()


def source_check():
    seen = {}
    def visit(path):
        path = path.resolve()
        assert path.is_relative_to(ROOT), path
        if path in seen:
            return
        text = re.sub(r'(?<!\\)%[^\n]*', '', path.read_text())
        seen[path] = text
        for name in re.findall(r'\\(?:input|include)\{([^}]+)\}', text):
            visit(ROOT / (name if name.endswith('.tex') else name + '.tex'))
    visit(ROOT / ENTRY)
    text = '\n'.join(seen.values())
    labels = re.findall(r'\\label\{([^}]+)\}', text)
    refs = re.findall(r'\\(?:ref|eqref|autoref|pageref)\{([^}]+)\}', text)
    keys = re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}', text)
    cites = [x.strip() for s in re.findall(r'\\cite(?:\[[^\]]*\])*\{([^}]+)\}', text) for x in s.split(',')]
    assert not [x for x, n in Counter(labels).items() if n > 1], 'duplicate labels'
    assert not [x for x, n in Counter(keys).items() if n > 1], 'duplicate bibliography keys'
    assert not set(refs) - set(labels), set(refs) - set(labels)
    assert not set(cites) - set(keys), set(cites) - set(keys)
    manifest = json.loads((ROOT / 'validation_reconstruction_manifest.json').read_text())
    for item in manifest['chapters'] + manifest['assets'] + manifest['notes']:
        assert (ROOT / item['destination']).is_file(), item
    return {'tex_inputs': len(seen), 'labels': len(labels), 'references': len(refs),
            'citations': len(cites), 'bibliography_entries': len(keys),
            'input_sha256': {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(seen)}}


def calculate(name):
    out = ROOT / 'build/relative_reconstruction_checks'
    out.mkdir(parents=True, exist_ok=True)
    target = out / (name + '.json')
    cmd = [sys.executable, 'computations/independent/verify_2jet.py' if name == 'poisson_second_jet' else 'computations/verify_' + name + '.py']
    if name in OUTPUT_CHECKS:
        cmd += ['--output', str(target)]
    start = time.monotonic()
    with (out / (name + '.log')).open('w') as log:
        process = subprocess.run(cmd, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, timeout=1800)
    assert process.returncode == 0, f'{name}: see {out / (name + ".log")}'
    result = {'name': name, 'exit_code': 0, 'seconds': round(time.monotonic() - start, 2)}
    certificate = {'artin_sectors': 'artin_sector_certificate', 'etale_inputs': 'etale_input_checks',
                   'nonelliptic_inputs': 'input_checks', 'hochschild_sectors': 'hochschild_sector_checks'}.get(name, name + '_certificate')
    expected = ROOT / 'computations' / (certificate + '.json')
    if target.exists() and expected.exists():
        actual, saved = json.loads(target.read_text()), json.loads(expected.read_text())
        if name == 'mixed_test_family':
            # The relocation changes only this documentary path.
            saved['proof_formulas_source'] = actual['proof_formulas_source']
        assert actual == saved, f'{name}: certificate changed'
        result['certificate_equal'] = True
    return result


def build_check():
    with (ROOT / 'build/relative_reconstruction_build.log').open('w') as log:
        subprocess.run(['latexmk', '-r', '.latexmkrc', ENTRY], cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, check=True)
    log = (ROOT / 'build/relative_reconstruction_models.log').read_text()
    failures = {key: bool(re.search(pattern, log)) for key, pattern in {
        'unresolved': r'There were undefined references|Reference .* undefined|Citation .* undefined',
        'duplicates': r'multiply defined', 'missing_glyphs': r'Missing character:',
        'overfull': r'Overfull \\[hv]box'}.items()}
    assert not any(failures.values()), failures
    match = re.search(r'Output written on .*?\((\d+) pages', log, re.S)
    return {'pages': int(match[1]) if match else None, 'failures': failures,
            'pdf_sha256': hashlib.sha256((ROOT / 'build/relative_reconstruction_models.pdf').read_bytes()).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--calculations', action='store_true')
    parser.add_argument('--build', action='store_true')
    args = parser.parse_args()
    record = {'source': source_check()}
    (ROOT / 'build').mkdir(exist_ok=True)
    if args.calculations:
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            record['calculations'] = list(pool.map(calculate, OUTPUT_CHECKS + PLAIN_CHECKS))
    if args.build:
        record['typesetting'] = build_check()
    record['limit'] = 'Source consistency, typesetting and finite checks; not an independent mathematical proof audit.'
    (ROOT / 'build/relative_reconstruction_current_check.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(record, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
