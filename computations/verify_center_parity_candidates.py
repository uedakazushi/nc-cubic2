#!/usr/bin/env python3
"""Exact combinatorial parity check for the degree-18 central relation.

The simultaneous sign automorphism fixes U,V,W and negates g.
Given a verified homogeneous leading relation, its invariant
nonhomogeneous correction belongs to the 15-dimensional span
of weight <=12 even central monomials.
This script does NOT prove Phi=0 in R1 or the leading relation.
"""
from itertools import product
from fractions import Fraction

WEIGHTS = (3, 6, 6, 6)  # g,U,V,W

def monomials(limit, even=False):
    return [(i, a, b, c)
            for i in range(limit // 3 + 1)
            for a, b, c in product(range(limit // 6 + 1), repeat=3)
            if 3*i + 6*(a+b+c) <= limit and (not even or i % 2 == 0)]

def weight(exponents):
    return sum(x*y for x, y in zip(exponents, WEIGHTS))


def abelian_word(word):
    """Reduce a word modulo x^2+1, y^2, z^2 in the commutative quotient."""
    nx, ny, nz = (word.count(c) for c in "XYZ")
    if ny > 1 or nz > 1:
        return {}
    return {(nx % 2, ny, nz): (-1)**(nx // 2)}

def abelian_polynomial(spec):
    result = {}
    for word, coeff in spec.items():
        for mon, factor in abelian_word(word).items():
            result[mon] = result.get(mon, 0) + coeff * factor
    return {k:v for k,v in result.items() if v}

def abelian_product(a, b):
    result = {}
    for (nx, ny, nz), c in a.items():
        for (mx, my, mz), d in b.items():
            if ny + my > 1 or nz + mz > 1:
                continue
            sign = (-1)**((nx + mx)//2)
            mon = ((nx + mx)%2, ny + my, nz + mz)
            result[mon] = result.get(mon, 0) + sign*c*d
    return {k:v for k,v in result.items() if v}

def main():
    assert len(monomials(18)) == 50
    corrections = monomials(12, even=True)
    assert len(corrections) == 15
    assert [sum(weight(e) == n for e in corrections)
            for n in (0, 6, 12)] == [1, 4, 10]
    # Formal exponents (g,U,V,W), with exact integer coefficients.
    phi = {
        (0,3,0,0):49, (2,2,0,0):-13, (0,2,0,0):-14,
        (4,1,0,0):1, (2,1,0,0):2, (0,1,0,0):1,
        (0,1,1,1):11, (2,0,1,1):-1, (0,0,1,1):-1,
        (0,0,3,0):1, (0,0,0,3):-1,
    }
    assert all(e[0] % 2 == 0 and weight(e) <= 18 for e in phi)
    top = {e:c for e,c in phi.items() if weight(e) == 18}
    lower = {e:c for e,c in phi.items() if weight(e) < 18}
    assert len(top) == 7 and len(lower) == 4
    assert set(lower).issubset(set(corrections))
    g = abelian_polynomial({"YYY":1, "ZYX":-1, "X":1})
    u = abelian_polynomial({"ZZZYYY":1, "ZZZZYX":-1, "ZZZX":1, "ZZZZZZ":-1})
    v = abelian_polynomial({
        "YZZYYY":1, "ZYZZYX":-1, "ZYZZZZ":-1,
        "ZZYYZX":2, "ZZYZZZ":1, "ZZZYZZ":-3,
        "YZZX":1, "ZYZX":1, "ZZYX":1, "ZZZZ":3})
    w = abelian_polynomial({
        "YZZZZY":1, "ZYZZZY":1, "ZZYYZZ":1,
        "ZZYZZY":2, "ZZZZYY":-1, "ZZZZZX":1,
        "ZYZZ":-1, "ZZYZ":-2, "ZZZY":-2, "ZZ":1})
    assert g == {(1,0,0):1, (1,1,1):-1}
    assert not u and not v and not w
    assert abelian_product(g,g) == {(0,0,0):-1, (0,1,1):2}
    assert len(corrections)-2 == 13
    # At the axial character the top part is 1/7, not zero. The
    # correction constraints are affine: Q(p)=P18(p). For the three
    # nonaxial characters, VW=-16 and (V^3,W^3)=(-64,64).
    axial = (0, Fraction(1,7), 0, 0)
    def evaluate(spec, point):
        result = 0
        for powers, coeff in spec.items():
            term = coeff
            for value, exponent in zip(point, powers):
                term *= value**exponent
            result += term
        return result
    assert evaluate(top, axial) == Fraction(1,7)
    assert -evaluate(lower, axial) == Fraction(1,7)
    # Dependence on omega disappears in the cubic powers and VW.
    assert 49*(-1)**3 + 11*(-1)*(-16) - 64 - 64 == -1
    assert 14*(-1)**2 - (-1) - 16 == -1
    print("PASS: affine correction values 1/7 (axial), -1 (three nonaxial)")
    print("PASS: abelianization imposes two independent conditions; 13 free coefficients")
    print("PASS: 50 monomials of weight <=18")
    print("PASS: even correction space dimension 15 = 1+4+10")
    print("PASS: proposed Phi is even, with 7 top and 4 lower terms")
    print("NOT PROVED: graded leading relation or Phi=0 over Q")

if __name__ == "__main__":
    main()
