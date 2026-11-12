#!/usr/bin/env python3
"""Rebuild the orbit matrix from its 25 equations, over Q, to degree seven.

Two independent recurrences give the classical degree-nine branch jet and
its -h^2 e_i^2 x_i/12 correction. No source PDF or saved matrix is read.
Requires python-flint; the categorical identification is a manuscript input.
"""
from flint import fmpq_mpoly_ctx, fmpq

R = fmpq_mpoly_ctx.get(('a1', 'a2', 'a3', 'c1', 'c2', 'c3'), 'lex')
a = [R.gen(i) for i in range(3)]
c = [R.gen(i+3) for i in range(3)]
zero, one = R.constant(0), R.constant(1)
weights = [fmpq(1, 3)]*3+[fmpq(1), fmpq(1)]


def trunc(p, n):
    return R.from_dict({m: v for m, v in p.to_dict().items() if sum(m) <= n})


def homogeneous(p, n):
    return R.from_dict({m: v for m, v in p.to_dict().items() if sum(m) == n})


def triple(x, y, z, degree):
    return trunc(trunc(x*y, degree)*z, degree)


def sf(mat, cols, degree):
    return sum((6*weights[r]*triple(*(mat[r][i] for i in cols), degree)
                for r in range(5)), zero)


def solve(quantum=False):
    mat = [[one if i == j else zero for j in range(5)] for i in range(5)]
    for degree in range(1, 8):
        changes = []
        tt = 3*sf(mat, (0, 1, 2), degree)
        pp = [sf(mat, tuple(j for j in range(3) if j != i)+(3,), degree)
              for i in range(3)]
        qq = [sf(mat, tuple(j for j in range(3) if j != i)+(4,), degree)
              for i in range(3)]
        for i in range(5):
            for j in range(5):
                if i == j:
                    lhs = sum((weights[r]*triple(mat[r][i], mat[r][i], mat[r][i], degree)
                               for r in range(5)), zero)
                    target = R.constant(weights[i])
                else:
                    lhs = sum((3*weights[r]*triple(mat[r][i], mat[r][i], mat[r][j], degree)
                               for r in range(5)), zero)
                    target = a[j] if i == 3 and j < 3 else (
                             c[j] if i == 4 and j < 3 else zero)
                    if quantum and i in (3, 4) and j < 3:
                        p = pp[j] if i == 3 else qq[j]
                        target -= triple(tt, p, p, degree)/12
                changes.append((i, j, -homogeneous(lhs-target, degree)/(3*weights[i])))
        for i, j, delta in changes:
            mat[i][j] += delta
        print(('quantum' if quantum else 'classical'), 'orbit equations solved:', degree, flush=True)
    return trunc(3*sf(mat, (0, 1, 2), 9), 9)


def main():
    pa, pc = a[0]*a[1]*a[2], c[0]*c[1]*c[2]
    ea = sum((a[i]**3*a[j]**3 for i in range(3) for j in range(i+1, 3)), zero)
    ec = sum((c[i]**3*c[j]**3 for i in range(3) for j in range(i+1, 3)), zero)
    jj = sum((a[i]**2*c[i]*a[j]*c[j]**2 for i in range(3) for j in range(3) if i != j), zero)
    rr = zero
    for i in range(3):
        j, k = [v for v in range(3) if v != i]
        rr += a[i]**2*c[i]**2*(a[j]*c[k]+a[k]*c[j])
    base = 2*(pa+pc)/3+2*rr/27
    classical = base+2*(pa*ea+pc*ec)/243+4*(pa+pc)*jj/243
    correction = -4*(pa+pc)*(ea+ec)/243
    assert solve(False) == classical
    assert solve(True) == classical+correction
    print('PASS: all six source variables, classical and corrected branch jets through degree nine')
    print('PASS: quantum ninth term contains', len(homogeneous(classical+correction, 9).to_dict()), 'monomials')


if __name__ == '__main__':
    main()
