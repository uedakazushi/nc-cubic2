#!/usr/bin/env python3
"""Exact Q degree <=7 central kernel, with rank bound over F_101.
Only Python 3 standard library. Run from the repository root.
A rank 78 mod 101 gives a characteristic-zero lower bound; six
independent rational central elements give the opposite upper bound.
"""
from fractions import Fraction as Q
from itertools import product

PRIME = 101
WORDS = [()] + [v for n in range(1, 8) for v in product(range(3), repeat=n)]
INDEX = {w: i for i, w in enumerate(WORDS)}
RELATIONS = (
    {(0, 1): 1, (1, 0): -1, (2, 2): -1},
    {(1, 2): 1, (2, 1): -1, (0, 0): -1, (): -1},
    {(2, 0): 1, (0, 2): -1, (1, 1): -1},
)

def add(a, b, factor=1):
    out = dict(a)
    for k, v in b.items():
        x = out.get(k, 0) + factor*v
        if x: out[k] = x
        else: out.pop(k, None)
    return out

def mul(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            k = INDEX[WORDS[i] + WORDS[j]]
            out[k] = out.get(k, 0) + x*y
    return {k: v for k, v in out.items() if v}

def wordpoly(spec):
    return {INDEX[tuple("XYZ".index(c) for c in w)]: Q(v)
            for w, v in spec.items() if v}

def reduce_row(row, pivots, insert=False):
    row = {k: Q(v) for k, v in row.items() if v}
    while row:
        k = max(row)
        if k not in pivots:
            if insert:
                v = row[k]
                pivots[k] = {i: x/v for i, x in row.items()}
            return row
        row = add(row, pivots[k], -row[k])
    return row

def canonical(row, pivots):
    row = dict(row)
    for k in sorted(pivots, reverse=True):
        if k in row:
            row = add(row, pivots[k], -row[k])
    return row

def main():
    pivots = {}
    # Every word a*r*b with |a|+|b| <= 5 is included.
    assert len(WORDS) == 3280
    relation_count = 0
    for m in range(6):
        for j in range(m+1):
            for prefix in product(range(3), repeat=j):
                for suffix in product(range(3), repeat=m-j):
                    for relation in RELATIONS:
                        row = {}
                        for w, coeff in relation.items():
                            i = INDEX[prefix + w + suffix]
                            row[i] = row.get(i, 0) + coeff
                        reduce_row(row, pivots, insert=True)
                        relation_count += 1
    assert relation_count == 6015
    quotient_basis = [i for i in range(len(WORDS)) if i not in pivots]
    assert len(quotient_basis) == 120
    filtered6 = [i for i in quotient_basis if len(WORDS[i]) <= 6]
    assert len(filtered6) == 84

    x, y, z = (wordpoly({name: 1}) for name in "XYZ")
    g = wordpoly({"YYY": 1, "ZYX": -1, "X": 1})
    u = mul(wordpoly({"ZZZ": 1}), add(g, wordpoly({"ZZZ": -1})))
    v = wordpoly({
        "YZZYYY": 1, "ZYZZYX": -1, "ZYZZZZ": -1,
        "ZZYYZX": 2, "ZZYZZZ": 1, "ZZZYZZ": -3,
        "YZZX": 1, "ZYZX": 1, "ZZYX": 1, "ZZZZ": 3,
    })
    w = wordpoly({
        "YZZZZY": 1, "ZYZZZY": 1, "ZZYYZZ": 1,
        "ZZYZZY": 2, "ZZZZYY": -1, "ZZZZZX": 1,
        "ZYZZ": -1, "ZZYZ": -2, "ZZZY": -2, "ZZ": 1,
    })

    for name, p in (("g", g), ("U", u), ("V", v), ("W", w)):
        for generator in (x, y, z):
            assert not canonical(
                add(mul(p, generator), mul(generator, p), -1), pivots
            ), "noncentral over Q: " + name

    six = [wordpoly({"":1}), g, mul(g, g), u, v, w]
    indep = {}
    for p in six:
        assert reduce_row(canonical(p, pivots), indep, insert=True)
    assert len(indep) == 6

    index7 = {i: j for j, i in enumerate(quotient_basis)}
    columns = []
    for i in filtered6:
        vector = {}
        for block, generator in enumerate((x, y, z)):
            p = {i: Q(1)}
            comm = canonical(add(mul(p, generator), mul(generator, p), -1),
                             pivots)
            for k, coeff in comm.items():
                residue = (coeff.numerator * pow(coeff.denominator, -1, PRIME)) % PRIME
                if residue: vector[block * 120 + index7[k]] = residue
        columns.append(vector)

    piv_mod = {}
    for column in columns:
        row = column.copy()
        while row:
            k = min(row)
            if k not in piv_mod:
                inv = pow(row[k], -1, PRIME)
                piv_mod[k] = {i: c * inv % PRIME for i, c in row.items()}
                break
            factor = row[k]
            for i, c in piv_mod[k].items():
                z0 = (row.get(i, 0) - factor * c) % PRIME
                if z0: row[i] = z0
                else: row.pop(i, None)
    assert len(piv_mod) == 78
    print("PASS Q: dim F7=120, dim F6=84, central 1,g,g²,U,V,W independent")
    print("PASS mod 101: commutator rank 78; hence exactly 6-dimensional center over Q")

if __name__ == "__main__":
    main()
