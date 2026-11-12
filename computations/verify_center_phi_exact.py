#!/usr/bin/env python3
"""Characteristic-zero verification of the nonhomogeneous central equation.

Exact rational arithmetic; no modular inference. Incremental filtered
quotient construction; state stored outside Git (default /tmp/nc-cubic2-center-phi).
Without --run-all, each invocation builds at most one new degree.
Then run --verify. A PASS at degree 18 proves Phi=0 in R1 over Q.
Use --backend flint --run-all --verify for an accelerated full run
(requires python-flint). The default backend uses only the standard library.
"""
import argparse
import pickle
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
from functools import lru_cache
from time import monotonic

REL = (
    ((0, 1, 1), (1, 0, -1), (2, 2, -1)),
    ((1, 2, 1), (2, 1, -1), (0, 0, -1)),
    ((2, 0, 1), (0, 2, -1), (1, 1, -1)),
)

def add(out, row, factor=1):
    for k, v in row.items():
        z = out.get(k, 0) + factor*v
        if z: out[k] = z
        else: out.pop(k, None)

def eliminate(row, pivots, insert=False):
    row = {k: Q(v) for k, v in row.items() if v}
    while row:
        k = max(row)
        if k not in pivots:
            if insert:
                inv = 1/row[k]
                pivots[k] = {j: c*inv for j, c in row.items()}
            return row
        add(row, pivots[k], -row[k])
    return row

def normal(row, pivots):
    row = dict(row)
    for k in sorted(pivots, reverse=True):
        if k in row: add(row, pivots[k], -row[k])
    return row

def linmap(matrix, v):
    out = {}
    for j, c in v.items(): add(out, matrix[j], c)
    return out

class Filtered:
    def __init__(self):
        self.B = [[()], [(), (0,), (1,), (2,)]]
        self.L = [[[{x+1: Q(1)}] for x in range(3)]]
        self.E = [[{0: Q(1)}]]
        self.last_pivots = None

    def word(self, w, n):
        if n == 0:
            assert not w
            return {0: Q(1)}
        if len(w) < n:
            return linmap(self.E[n-1], self.word(w, n-1))
        return linmap(self.L[n-1][w[0]], self.word(w[1:], n-1))

    def candidate(self, w, n):
        if not w: return {0: Q(1)}
        d = len(self.B[n-1])
        return {1+w[0]*d+i: c for i, c in self.word(w[1:], n-1).items()}

    def extend(self):
        n = len(self.B)
        d = len(self.B[n-1])
        pivots = {}
        for basis_idx, word in enumerate(self.B[n-2]):
            for ridx, terms in enumerate(REL):
                row = {}
                for x, y, c in terms:
                    for k, v in self.L[n-2][y][basis_idx].items():
                        coordinate = 1+x*d+k
                        row[coordinate] = row.get(coordinate, 0) + c*v
                if ridx == 1: add(row, self.candidate(word, n), -1)
                eliminate(row, pivots, True)
        kept = [j for j in range(1+3*d) if j not in pivots]
        pos = {j:i for i,j in enumerate(kept)}
        self.B.append([() if j == 0 else
                       ((j-1)//d,)+self.B[n-1][(j-1)%d] for j in kept])
        def compact(row):
            return {pos[k]:v for k,v in normal(row, pivots).items()}
        self.L.append([[compact({1+x*d+j: Q(1)}) for j in range(d)]
                       for x in range(3)])
        self.E.append([compact(self.candidate(w, n)) for w in self.B[n-1]])
        self.last_pivots = pivots
        expected = (n+1)*(n+2)*(n+3)//6
        assert len(self.B[n]) == expected, (n, len(self.B[n]), expected)
        return n, expected

def poly(spec):
    return {tuple("XYZ".index(c) for c in word): Q(v)
            for word, v in spec.items() if v}

def plus(a, b, scale=1):
    out = dict(a)
    add(out, b, scale)
    return out

def times(a, b):
    out = {}
    for w, x in a.items():
        for z, y in b.items():
            word = w+z
            out[word] = out.get(word, 0) + x*y
    return {k:v for k,v in out.items() if v}

def scalar(a, c):
    return {k:v*c for k,v in a.items() if v*c}

def phi():
    one = {(): Q(1)}
    g = poly({"YYY":1,"ZYX":-1,"X":1})
    u = times(poly({"ZZZ":1}),plus(g,poly({"ZZZ":-1})))
    v = poly({
        "YZZYYY":1,"ZYZZYX":-1,"ZYZZZZ":-1,
        "ZZYYZX":2,"ZZYZZZ":1,"ZZZYZZ":-3,
        "YZZX":1,"ZYZX":1,"ZZYX":1,"ZZZZ":3,
    })
    w = poly({
        "YZZZZY":1,"ZYZZZY":1,"ZZYYZZ":1,
        "ZZYZZY":2,"ZZZZYY":-1,"ZZZZZX":1,
        "ZYZZ":-1,"ZZYZ":-2,"ZZZY":-2,"ZZ":1,
    })
    g2=times(g,g); u2=times(u,u); vw=times(v,w)
    result=plus(scalar(times(u2,u),49),scalar(times(g2,u2),-13))
    result=plus(result,scalar(u2,-14))
    result=plus(result,times(times(g2,g2),u))
    result=plus(result,scalar(times(g2,u),2))
    result=plus(result,u)
    result=plus(result,scalar(times(u,vw),11))
    result=plus(result,times(g2,vw),-1)
    result=plus(result,vw,-1)
    result=plus(result,times(times(v,v),v))
    result=plus(result,times(times(w,w),w),-1)
    assert max(map(len, result)) <= 18
    return result

def evaluate_polynomial(algebra, polynomial, degree):
    """Noncommutative Horner evaluation, grouping words by first letter.

    p = c + X*p_X + Y*p_Y + Z*p_Z. Recursing on p_x at
    degree-1 shares the expensive final multiplication across all words
    with the same first letter. Only exact linear maps are used.
    """
    assert all(len(word) <= degree for word in polynomial)
    @lru_cache(maxsize=20000)
    def evaluate(terms, n):
        out = {}
        groups = [{}, {}, {}]
        for word, coefficient in terms:
            if not word:
                add(out, {0: coefficient})
            else:
                groups[word[0]][word[1:]] = coefficient
        for x, group in enumerate(groups):
            if group:
                vector = evaluate(tuple(sorted(group.items())), n-1)
                add(out, linmap(algebra.L[n-1][x], vector))
        return out
    return evaluate(tuple(sorted(polynomial.items())), degree)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--state-dir", default="/tmp/nc-cubic2-center-phi")
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--backend", choices=("fraction", "flint"), default="fraction")
    parser.add_argument("--run-all", action="store_true", help="build all remaining degrees in this invocation")
    parser.add_argument("--smoke", action="store_true", help="check exact dimensions and Horner evaluation through degree 8")
    args = parser.parse_args()
    global Q
    if args.backend == "flint":
        from flint import fmpq
        Q = fmpq
    if args.smoke:
        algebra=Filtered()
        for n_expected in range(2,9):
            n, dim=algebra.extend()
            assert n == n_expected
            assert dim == (n+1)*(n+2)*(n+3)//6
        print("PASS: exact-Q filtered quotient dimensions in degrees 2 through 8")
        for degree in range(9):
            polynomial = {
                word: Q(sum((j+1)*(x+1) for j, x in enumerate(word)) % 11 - 5, 7)
                for d in range(degree+1) for word in product(range(3), repeat=d)
            }
            direct = {}
            for word, coefficient in polynomial.items():
                add(direct, algebra.word(word, degree), coefficient)
            assert evaluate_polynomial(algebra, polynomial, degree) == direct
        print("PASS: exact Horner and word-by-word evaluation agree through degree 8")
        return
    state_dir=Path(args.state_dir)
    state_dir.mkdir(parents=True,exist_ok=True)
    path=state_dir/("rational-filtered-state.pkl" if args.backend == "fraction"
                    else "flint-rational-filtered-state.pkl")
    if path.exists():
        with path.open("rb") as f: algebra=pickle.load(f)
        assert isinstance(algebra, Filtered)
    else: algebra=Filtered()
    while len(algebra.B)-1 < 18:
        started = monotonic()
        n, dim=algebra.extend()
        temporary_path = path.with_suffix(".tmp")
        with temporary_path.open("wb") as f:
            pickle.dump(algebra,f,pickle.HIGHEST_PROTOCOL)
        temporary_path.replace(path)
        print(f"EXACT Q quotient: degree={n}, dimension={dim}; "
              f"{monotonic()-started:.2f}s", flush=True)
        if not args.run_all:
            return
    if not args.verify:
        print("Ready. Run with --verify to check Phi exactly over Q.")
        return
    polynomial = phi()
    print(f"Reducing {len(polynomial)} free words by exact Horner evaluation", flush=True)
    residue = evaluate_polynomial(algebra, polynomial, 18)
    if residue:
        print("FAIL: Phi nonzero in the exact quotient:",len(residue),"terms")
        raise SystemExit(1)
    print("PASS: Phi=0 in R1 over Q, exact rational arithmetic")

if __name__=="__main__":
    main()
