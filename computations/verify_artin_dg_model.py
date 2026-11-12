#!/usr/bin/env python3
"""Exact checks of the four-dimensional dg model, not categorical smoothness.

Requires Python 3 and SymPy. All arithmetic is in QQ[h] or QQ.
The general generation, Morita and non-smoothness arguments are in the paper.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sympy as sp


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, default=Path('build/artin_dg_model_check.json'))
    args = ap.parse_args()
    h = sp.Symbol('h')
    zero = sp.zeros(4, 1)
    basis = [sp.eye(4)[:, i] for i in range(4)]
    degree = [0, 0, 1, 1]  # e_minus, e_plus, s, t
    products = {(0, 0): 0, (1, 1): 1, (1, 2): 2,
                (2, 0): 2, (1, 3): 3, (3, 0): 3}

    def multiply(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
        result = zero.copy()
        for (i, j), k in products.items():
            result[k] += a[i] * b[j]
        return sp.simplify(result)

    differential = sp.zeros(4)
    differential[2, 0], differential[2, 1] = h, -h
    unit = basis[0] + basis[1]
    for a in basis:
        assert multiply(unit, a) == a == multiply(a, unit)
    assert differential * differential == sp.zeros(4)
    for i, a in enumerate(basis):
        for j, b in enumerate(basis):
            assert differential * multiply(a, b) == (
                multiply(differential * a, b) + (-1)**degree[i] * multiply(a, differential * b))
            for c in basis:
                assert multiply(multiply(a, b), c) == multiply(a, multiply(b, c))
    d01 = differential[2:4, 0:2]
    assert d01.rank() == 1 and d01.subs(h, 0).rank() == 0
    assert d01.nullspace() == [sp.Matrix([1, 1])]
    # Exterior generator maps to t; t^2=0 and 1 maps to the unit.
    assert multiply(basis[3], basis[3]) == zero
    assert differential * basis[3] == zero
    assert sp.Matrix.hstack(d01[:, 0], sp.Matrix([0, 1])).det() == h

    rows = []
    for N in (0, 1, 2, 3, 5, 8):
        m = N + 1
        H = sp.zeros(m)
        for i in range(m - 1):
            H[i + 1, i] = 1
        D = sp.Matrix.vstack(sp.Matrix.hstack(H, -H), sp.zeros(m, 2*m))
        rank = D.rank()
        assert rank == m - 1
        rows.append({'N': N, 'base_length': m, 'differential_rank': rank,
                     'H0_Q_dimension': 2*m-rank, 'H1_Q_dimension': 2*m-rank})
    report = {
        'status': 'PASS', 'coefficient_ring': 'QQ[h]',
        'associativity_basis_triples': 64, 'Leibniz_basis_pairs': 16,
        'unit_checks': 8, 'd_squared_zero': True,
        'generic_cohomology_dimensions': [1, 1],
        'special_cohomology_dimensions': [2, 2],
        'exterior_map_unit_product_and_cohomology': True,
        'Artin_truncations': rows,
        'not_verified': ['dg Morita equivalence', 'generation for all N',
                         'infinite semifree resolution', 'homological smoothness',
                         'Artin residual/MF comparison'],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
