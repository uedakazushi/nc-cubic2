#!/usr/bin/env python3
"""Exact integer certificate for generic smoothness of the rank-4 Poisson component.

Input: F0=sum(x_i^3), P0=e012+e345 on six variables.
Output: full rank 36 of the Jacobi derivative on mixed cubic coefficients.
Requires Python 3 and SymPy; no numeric sampling or Groebner black box.
"""
from itertools import combinations
import sympy as sp

x = sp.symbols("x0:6")
F0 = sum(z**3 for z in x)

def qmatrix(F):
    Q = sp.zeros(6)
    for block in (0, 3):
        a, b, c = block, block + 1, block + 2
        for i, j, k in ((a, b, c), (b, c, a), (c, a, b)):
            Q[i, j] = sp.diff(F, x[k])
            Q[j, i] = -Q[i, j]
    return Q

Q = qmatrix(F0)
triples = list(combinations(range(6), 3))
monomials = []
for a in range(4):
    for b in range(4 - a):
        for c in range(4 - a - b):
            for d in range(4 - a - b - c):
                for e in range(4 - a - b - c - d):
                    f = 3 - a - b - c - d - e
                    if 0 < a + b + c < 3:
                        monomials.append(x[0]**a*x[1]**b*x[2]**c
                                         *x[3]**d*x[4]**e*x[5]**f)
assert len(monomials) == 36

def jacobi_derivative(delta_F):
    D = qmatrix(delta_F)
    out = []
    for i, j, k in triples:
        out.append(sp.expand(sum(
            Q[i,l]*sp.diff(D[j,k],x[l]) + D[i,l]*sp.diff(Q[j,k],x[l])
          + Q[j,l]*sp.diff(D[k,i],x[l]) + D[j,l]*sp.diff(Q[k,i],x[l])
          + Q[k,l]*sp.diff(D[i,j],x[l]) + D[k,l]*sp.diff(Q[i,j],x[l])
            for l in range(6))))
    return out

columns = []
for mon in monomials:
    coefficients = []
    for pol in jacobi_derivative(mon):
        poly = sp.Poly(pol, *x)
        coefficients.extend(poly.coeff_monomial(v) for v in monomials)
    columns.append(sp.Matrix(coefficients))
M = sp.Matrix.hstack(*columns)
assert M.shape == (720, 36)
rows = (36,38,45,47,57,59,72,81,93,153,155,165,167,189,
        201,258,259,260,270,271,272,295,296,307,308,332,
        344,381,383,417,474,475,476,511,512,548)
assert len(rows) == 36
minor = M.extract(rows, list(range(36)))
det = minor.det()
assert det == -39346408075296537575424
assert M.rank() == 36
print("PASS: rank-4 Fermat Jacobi tangent: matrix", M.shape)
print("PASS: nonzero exact determinant =", det)
print("Consequence with normal-form theorem: rank-4 component generically smooth.")
