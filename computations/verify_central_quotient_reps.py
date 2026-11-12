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


# Exact rank certificate for the axial 3-dimensional simples.
# Column order: E_{rc} in X, then Y, then Z, 3*r+c per block;
# row order: entries of [X,Y]-Z^2, [Y,Z]-X^2-I, [Z,X]-Y^2.
prime = 29
def value_at_t2(expr):
    val = sp.together(expr.subs(t, 2))
    return int(sp.numer(val)) * pow(int(sp.denom(val)), -1, prime) % prime

xx = sp.diag(*(value_at_t2(v) for v in lam))
yy, zz = sp.zeros(3), sp.zeros(3)
dvals = [value_at_t2(v) for v in diff]
for idx in range(3):
    yy[(idx+1)%3, idx] = dvals[(idx-1)%3]
    zz[(idx-1)%3, idx] = dvals[idx]

comm = lambda aa, bb: aa*bb-bb*aa
jac_cols = []
for k in range(27):
    aa, bb, cc = (sp.zeros(3) for _ in range(3))
    owner = k//9
    row, col = divmod(k%9, 3)
    (aa,bb,cc)[owner][row,col] = 1
    first = comm(aa,yy)+comm(xx,bb)-zz*cc-cc*zz
    second = comm(bb,zz)+comm(yy,cc)-xx*aa-aa*xx
    third = comm(cc,xx)+comm(zz,aa)-yy*bb-bb*yy
    jac_cols.append([int(z)%prime for mat in (first,second,third) for z in mat])

rows = [2,0,1,5,3,4,10,11,9,14,6,7,13,20,16,17,18,19,8]
cols = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,18,19,20]
minor = [[jac_cols[j][i] for j in cols] for i in rows]
determinant = 1
for k in range(len(rows)):
    pivot = next((i for i in range(k,len(rows)) if minor[i][k]), None)
    assert pivot is not None
    if pivot != k:
        minor[pivot], minor[k] = minor[k], minor[pivot]
        determinant = -determinant
    lead = minor[k][k]
    determinant = determinant * lead % prime
    inv = pow(lead, -1, prime)
    for i in range(k+1,len(rows)):
        factor = minor[i][k]*inv % prime
        minor[i] = [(u-factor*v)%prime for u,v in zip(minor[i], minor[k])]
assert determinant % prime == 15
assert sp.Poly(q, t, modulus=3).is_irreducible
print("PASS: axial rigidity certificate: 19x19 minor = 15 mod 29, q irreducible mod 3")
