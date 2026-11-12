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

# Finite flat rank-six comparison and its precise etale locus.
g = sp.symbols("g")
gs = -sp.Rational(3,2)*(s**(-3)+s**3/alpha**3)
monic = s**6+sp.Rational(2,3)*alpha**3*g*s**3+alpha**3
assert sp.cancel(monic.subs(g,gs)) == 0
assert sp.cancel(sp.diff(gs,s)-sp.Rational(9,2)*(s**(-4)-s**2/alpha**3)) == 0
assert sp.cancel(gs**2-9/alpha**3
                 -sp.Rational(9,4)*(s**6-alpha**3)**2/(alpha**6*s**6)) == 0

# The genuine ambient derivation fixes uv and kills all other terms of W.
u, v, t, q = sp.symbols("u v t q", nonzero=True)
delta = lambda f: sp.expand(u*sp.diff(f,u)-v*sp.diff(f,v))
assert delta(alpha*u*v) == 0
assert delta(alpha*u*v*x+u**3+v**3) == 3*(u**3-v**3)
assert sp.expand(sp.prod([v-u,v**2+u*v+u**2])-(v**3-u**3)) == 0
# Eliminate s^2=alpha*t in g(s)^2, and specialize alpha^3=-243/28.
assert sp.cancel(gs**2-sp.Rational(9,4)/alpha**3*(q+2+1/q)
                 ).subs(q,s**6/alpha**3).cancel() == 0
assert sp.Rational(9,4)/(-sp.Rational(243,28)) == -sp.Rational(7,27)
print("PASS: rank-six monic comparison, ramification locus, ambient derivation")
