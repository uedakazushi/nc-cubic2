#!/usr/bin/env python3
"""Exact checks from PDF VI, §16. These are not global-dimension proofs."""
import sympy as sp
x, y, z, beta, s, s0, alpha = sp.symbols("x y z beta s s0 alpha", nonzero=True)
G = (x**3+y**3+z**3)/3-sp.Rational(2, 3)*x*y*z+x

def rem(poly, var, divisor):
    return sp.rem(sp.Poly(sp.expand(poly), var),
                  sp.Poly(divisor, var)).as_expr()

# Abelianized relations: x^2=-1, y^2=z^2=0.
G0 = rem(rem(rem(G, x, x*x+1), y, y*y), z, z*z)
assert sp.expand(G0-sp.Rational(2, 3)*x*(1-y*z)) == 0
bvalue = -G0
image = 9*bvalue**2+4
image = rem(rem(rem(image, x, x*x+1), y, y*y), z, z*z)
assert sp.expand(image-8*y*z) == 0

# Double ramification: s0^2=alpha, beta0=2/s0^3.
b = s**(-3)+s**3/s0**6
assert sp.simplify(b-2/s0**3-(s**3-s0**3)**2/(s0**6*s**3)) == 0
assert sp.simplify((2/s0**3)**2*(s0**2)**3-4) == 0

# Compare the two bad affine fibers with the cubic discriminant.
lhs = (9*4/alpha**3+4)*(243*4/alpha**3+112)*alpha**6
rhs = 16*(alpha**3+9)*(28*alpha**3+243)
assert sp.expand(lhs-rhs) == 0
print("PASS: representation scheme, ramified center, discriminant factors")
