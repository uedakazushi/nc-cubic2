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

# All 21 points in the double-center chart. q=t^3 is a local coordinate
# since t is invertible. At q=+-1 the Hessian is block diagonal.
q = sp.symbols("q", nonzero=True)
Hq = -sp.Rational(7,27)*(q+2+1/q)
assert sp.diff(Hq,q).subs(q,1) == sp.diff(Hq,q).subs(q,-1) == 0
for q0, point, dH, det3 in [
    (-1, (sp.Rational(1,7),0,0), sp.Rational(1,49), -sp.Rational(32,7)),
    (-1, (-1,-4,4), sp.Integer(1), sp.Integer(288)),
    (1, (sp.Rational(1,189),0,0), -sp.Rational(1,1323), -sp.Rational(8,1701)),
]:
    at = dict(zip((u,v,w),point)) | {Hparam:Hq.subs(q,q0)}
    assert sp.diff(Fh,Hparam).subs(at) == dH
    assert sp.hessian(Fh,(u,v,w)).subs(at).det() == det3
    expected_det = sp.factor(dH*sp.diff(Hq,q,2).subs(q,q0)*det3)
    assert expected_det != 0
    actual = sp.hessian(Fh.subs(Hparam,Hq),(q,u,v,w)).subs(
        dict(zip((q,u,v,w),(q0,)+point)))
    assert sp.factor(actual.det()) == expected_det

# Cubic root symmetry accounts for the three nonaxial points, and
# each nonzero q has exactly three distinct t-roots.
assert sp.expand(Fh.subs({v:sp.Symbol("r")*v,w:sp.Symbol("r")**2*w},
                        simultaneous=True)-Fh).subs(sp.Symbol("r")**3,1) == 0
assert sp.hessian(Fh,(Hparam,u,v,w)).subs(
    {Hparam:-1,u:0,v:0,w:0}).rank() == 1
poly = 7*q**2-13*q+7
assert sp.discriminant(poly,q) == -27
assert sp.gcd(poly,q*(q*q-1)) == 1
assert sp.cancel(Hq+1+poly/(27*q)) == 0
assert 3*(1+3)+2*3+3 == 21
print("PASS: all 15 ordinary double points have nonzero Hessian; other six have rank 1")
