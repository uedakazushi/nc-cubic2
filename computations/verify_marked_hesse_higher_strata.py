#!/usr/bin/env python3
"""Symbolic Q(q) and Q(rho) certificates for the A4 and D4 strata."""
import sympy as s
from verify_marked_hesse_geometry import block_hessian, gamma


def zero(expr):
    assert s.cancel(expr) == 0, s.factor(expr)


def normal_matrix(poly, x):
    p = s.Poly(poly, *x)
    return s.Matrix(3, 3, lambda i, j: -p.coeff_monomial(x[i]**2*x[j]))


def hesse_four(qs, n, x):
    ell = sum(n[2*i]*x[i] for i in range(3))
    emm = sum(n[2*i+1]*x[i] for i in range(3))
    p2 = s.expand(sum(x[i]*(qs[i][0, 0]*ell**2+2*qs[i][0, 1]*ell*emm+
                            qs[i][1, 1]*emm**2)/2 for i in range(3)))
    ax = normal_matrix(p2, x)*x
    c4 = s.Poly(sum(s.diff(p2, x[i])*ax[i]+x[i]*ax[i]**2
                     for i in range(3)), *x).coeff_monomial(s.prod(x))
    return p2, ax, s.factor(c4)


def main():
    q = s.symbols('q')
    qs = [s.Matrix([[(17-3*q)/20, -3*(q+1)/10], [-3*(q+1)/10, (2-3*q)/5]]),
          s.Matrix([[(q+1)/4, (q-1)/2], [(q-1)/2, q]]),
          s.Matrix([[-3, 1], [1, 0]])]
    h = block_hessian(qs)
    k = s.Matrix([1, 1, 1, 2, 2, -1])
    assert h*k == s.zeros(6, 1) and gamma(k) == 0
    dq = (3*q-1)*(4*q-1)
    zero(h[:5, :5].det(method='domain-ge')-dq/10)
    n = s.Matrix(s.symbols('n0:6'))
    gam = gamma(n)
    g = s.Matrix([s.diff(gam, ni).subs(dict(zip(n, k))) for ni in n[:5]])
    eta = -h[:5, :5].inv()*g
    b4 = -45*(3*q-5)**2/(4*dq)
    b5 = -135*(3*q-5)**2*(165*q**2-54*q-59)/(8*dq**2)
    zero(g.dot(eta)/2-b4)
    cg = s.hessian(gam, n)[:5, :5].subs(dict(zip(n, k)))
    zero(eta.dot(cg*eta)/2-b5)
    x = s.Matrix(s.symbols('x y z'))
    p2, ax, c4 = hesse_four(qs, k, x)
    zero(c4-(6*q-17)/2)
    ell = sum(k[2*i]*x[i] for i in range(3))
    emm = sum(k[2*i+1]*x[i] for i in range(3))
    p3 = s.expand(ell**3+emm**3)
    bx = normal_matrix(p3, x)*x
    c5 = s.Poly(sum(s.diff(p2, x[i])*bx[i]+s.diff(p3, x[i])*ax[i]+
                     2*x[i]*ax[i]*bx[i] for i in range(3)), *x).coeff_monomial(s.prod(x))
    zero(c5-3*(39*q+175)/4)
    # Differentiate the actual normalization expression, including its matrix.
    # A dual-number direction avoids expanding a generic six-variable quartic.
    dl = sum(eta[2*i]*x[i] for i in range(3) if 2*i < 5)
    dm = sum(eta[2*i+1]*x[i] for i in range(3) if 2*i+1 < 5)
    dp = s.Poly(sum(x[i]*(qs[i][0, 0]*ell*dl+
                   qs[i][0, 1]*(dl*emm+ell*dm)+qs[i][1, 1]*emm*dm)
                   for i in range(3)), *x)
    dp = s.Poly.from_dict({mon: s.cancel(co) for mon, co in dp.terms()}, *x).as_expr()
    da = normal_matrix(dp, x)*x
    dc4 = s.Poly(sum(s.diff(dp, x[i])*ax[i]+s.diff(p2, x[i])*da[i]+
                       2*x[i]*ax[i]*da[i] for i in range(3)), *x).coeff_monomial(s.prod(x))
    zero(dc4-3*(261*q**3-2073*q**2+605*q+459)/(2*dq))
    g5 = 3*(990*q**3-2319*q**2+24*q+1093)/(4*dq)
    zero(dc4+c5-g5)
    zero(b4*(g5-135*(3*q-1)/(2*(4*q-1)))-c4*b5)
    v, t = s.symbols('v t')
    arc = (4*dq*(b4+t**2*c4)).subs(q, s.Rational(5, 3)+t*v)
    # Here rho^3=t^2, hence the divided quartic equation is polynomial.
    zero(s.cancel(arc/t**2)-(-405*v**2-s.Rational(952, 3)-190*t*v+
                             228*t**2*v**2+144*t**3*v**3))
    print('PASS: A4 kernel, minor, both Hesse contributions, stationary terms, arc equation')
    dqs = [s.eye(2), s.diag(1, -1), s.Matrix([[0, 1], [1, 0]])]
    hd = block_hessian(dqs)
    a, b = s.symbols('s t')
    kd = s.Matrix([a, b, -a, b, -b, -a])
    assert hd*kd == s.zeros(6, 1) and hd[:4, :4].det() == 1
    zero(gamma(kd)-6*a*b*(a-b))
    # Binary cubic discriminant includes the root at infinity.
    cub = s.Poly(gamma(kd), a, b)
    ca, cb, cc, cd = [cub.coeff_monomial(m) for m in (a**3, a**2*b, a*b**2, b**3)]
    assert cb**2*cc**2-4*ca*cc**3-4*cb**3*cd-27*ca**2*cd**2+18*ca*cb*cc*cd == 1296
    alpha = s.symbols('alpha')
    f = 6*a*b*(a-b)+alpha*a*b
    rh = s.hessian(f, (a, b))
    rr = (alpha+12*(a-b))**2+144*a*b
    zero(rh.det()+rr)
    sx, sy, sz = a+alpha/12, b-alpha/12, b-a-alpha/12
    assert s.Matrix([sx, sy, sz]).jacobian([a, b, alpha]).det() != 0
    print('PASS: D4 kernel, nondegenerate complement, binary discriminant and quadratic cone')


if __name__ == '__main__':
    main()
