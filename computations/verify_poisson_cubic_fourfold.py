#!/usr/bin/env python3
"""Exact finite checks for the cubic-fourfold Poisson-pair project.

Not a proof of the global trivector normal-form theorem or scheme reducedness.
Requires Python 3 and SymPy.
"""
from math import comb
import sympy as sp

x = sp.symbols("x0:6")
f = sum(t**3 for t in x[:3])
g = sum(t**3 for t in x[3:])

def qmatrix(F):
    q = sp.zeros(6)
    for start in (0, 3):
        a, b, c = start, start + 1, start + 2
        for i, j, k in ((a, b, c), (b, c, a), (c, a, b)):
            q[i, j] = sp.diff(F, x[k])
            q[j, i] = -q[i, j]
    return q

def jacobi(q, i, j, k):
    return sp.expand(sum(q[i, l] * sp.diff(q[j, k], x[l])
                         + q[j, l] * sp.diff(q[k, i], x[l])
                         + q[k, l] * sp.diff(q[i, j], x[l])
                         for l in range(6)))

q0 = qmatrix(f + g)
assert all(jacobi(q0, i, j, k) == 0
           for i in range(6) for j in range(i + 1, 6)
           for k in range(j + 1, 6))
qm = qmatrix(f + g + x[0] * x[1] * x[3])
violations = {(i, j, k): jacobi(qm, i, j, k)
              for i in range(6) for j in range(i + 1, 6)
              for k in range(j + 1, 6)
              if jacobi(qm, i, j, k) != 0}
assert violations
point = {x[0]: 1, x[3]: -1, **{x[i]: 0 for i in (1, 2, 4, 5)}}
assert (f + g).subs(point) == 0
assert q0.subs(point).rank() == 4
N = 6
pgl = N**2 - 1
rank2 = (comb(N + 2, 3) - 1) + (3 * (N - 3) + 1)
rank4 = comb(N, 3) + (2 * comb(5, 3) - 1)
assert (rank2, rank4, pgl) == (65, 39, 35)
assert (rank2 - pgl, rank4 - pgl) == (30, 4)
assert comb(6, 3) // 2 == 10
print("PASS: 20 Jacobi triples for split Fermat example")
print("PASS: mixed perturbation violates Jacobi in", len(violations), "triples")
print("PASS: sample on F=0 has affine Poisson rank 4")
print("PASS: incidence dimensions 65, 39; quotient dimensions 30, 4")
print("PASS: unordered 3+3 partitions of six labels = 10")
