#!/usr/bin/env python3
"""Exact central-singularity and Hessian checks for the four A1 points."""
import sympy as sp

g, u, v, w = sp.symbols("g u v w")
phi = (49*u**3 - (13*g**2 + 14)*u**2 + (g**2 + 1)**2*u
       + (11*u - g**2 - 1)*v*w + v**3 - w**3)
coords = (g, u, v, w)
H = sp.hessian(phi, coords)
for point, full, fibre in [
    ((0, sp.Rational(1, 7), 0, 0), -sp.Rational(64, 343), -sp.Rational(32, 7)),
    ((0, -1, -4, 4), sp.Integer(576), sp.Integer(288)),
]:
    at = dict(zip(coords, point))
    assert sp.expand(phi.subs(at)) == 0
    assert all(sp.expand(sp.diff(phi, x).subs(at)) == 0 for x in coords)
    assert sp.factor(H.subs(at).det()) == full
    assert sp.factor(H[1:4, 1:4].subs(at).det()) == fibre
print("PASS: four A1 central points up to cubic symmetry, exact Hessians")

Hparam = sp.symbols("H")
Fh = (49*u**3-(13*Hparam+14)*u**2+(Hparam+1)**2*u
      +(11*u-Hparam-1)*v*w+v**3-w**3)
expected = {
    sp.Integer(0): [-v**2 + 4*w, -56*u + v**3 + 8,
                    v*(u + 1), (u + 1)*(7*u - 1)],
    -sp.Integer(1): [w**2, -2*u + 11*v*w, u*w, v**2, u*v, u**2],
    -sp.Rational(28, 27): [w, v, u - sp.Rational(1, 189)],
}
for value, generators in expected.items():
    f = Fh.subs(Hparam, value)
    basis = sp.groebner([sp.diff(f, x) for x in (u, v, w)] + [f],
                        w, v, u, order="lex")
    assert len(basis.polys) == len(generators)
    assert all(sp.expand(poly.as_expr()-want) == 0
               for poly, want in zip(basis.polys, generators))
print("PASS: singular ideals at H=0,-1,-28/27 (exact Groebner bases)")
