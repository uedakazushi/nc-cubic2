#!/usr/bin/env python3
"""Exact symbolic validation of the 3x3 representations from paper VI §§17–18.

This checks relations and G1=0, not center V,W or the Ext rank certificates.
"""
import sympy as sp

t = sp.symbols("t")
q = 7*t**6 + 21*t**4 + 14*t**2 + 1
lam = [(42*t**5 + 119*t**3 + 75*t)/13,
       (7*t**5 + 35*t**3 + 45*t)/13, t]
diff = [lam[(i + 1) % 3] - lam[i] for i in range(3)]
X = sp.diag(*lam)
Y, Z = sp.zeros(3), sp.zeros(3)
for i in range(3):
    Y[(i+1) % 3, i] = diff[(i-1) % 3]
    Z[(i-1) % 3, i] = diff[i]
I = sp.eye(3)

def mod(expr, var, poly):
    return sp.rem(sp.Poly(sp.together(expr), var),
                  sp.Poly(poly, var)).as_expr().cancel()

def check_relations(x, y, z, var, poly, name):
    omega = ((x**3 + y**3 + z**3)/3
             - (x*y*z + x*z*y + y*x*z + y*z*x + z*x*y + z*y*x)/9)
    matrices = [x*y-y*x-z**2, y*z-z*y-x**2-I, z*x-x*z-y**2,
                omega+x]
    for j, mat in enumerate(matrices):
        for a in mat:
            assert mod(a, var, poly) == 0, (name, j, a)
    print("PASS:", name, "all relations and G1=0")

assert sp.gcd(q, sp.diff(q, t)) == 1
assert sp.gcd(q, sp.together(diff[0]*diff[1]*diff[2]).as_numer_denom()[0]) == 1
check_relations(X, Y, Z, t, q, "axial representations")
s = sum(lam)
assert mod(s**2+7, t, q) == 0
assert mod(diff[0]*diff[1]*diff[2]+s/7, t, q) == 0
print("PASS: axial distinct eigenvalues, trace and six roots of T^6+1/7")

w = sp.symbols("w")
X0 = sp.Matrix([[-1, 1, 1-w],
                [-1, (2*w+1)/3, 1],
                [-(w+2)/3, sp.Rational(1, 3), -(2*w+1)/3]])
Y0 = sp.diag(-1, w, w**2)
Z0 = sp.Matrix([[-1, -(2*w+1)/3, w+1],
                [-w-1, (w-1)/3, w+1],
                [(w-1)/3, -w/3, -(w+2)/3]])
check_relations(X0, Y0, Z0, w, w**2+w+1, "nonaxial representations")
assert mod(sp.trace(X0)+1, w, w**2+w+1) == 0
assert mod(sp.trace(Z0)+2, w, w**2+w+1) == 0
print("PASS: nonaxial traces and cubic-root reductions")
