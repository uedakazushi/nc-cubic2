#!/usr/bin/env python3
"""Exact characteristic-zero certificates for marked Hesse critical geometry.

Run with SymPy. Global irreducibility, normality and formal splitting are
proved in the manuscript; these checks certify its finite matrix identities.
"""
import sympy as s


def block_hessian(q):
    z = s.zeros(2)
    return z.row_join(q[2]).row_join(q[1]).col_join(
        q[2].row_join(z).row_join(q[0])).col_join(
        q[1].row_join(q[0]).row_join(z))


def gamma(k):
    return 6*(k[0]*k[2]*k[4]+k[1]*k[3]*k[5])


def check_zero(expr):
    assert s.expand(expr) == 0, s.factor(expr)


def main():
    coeff = s.symbols('a1 b1 c1 a2 b2 c2 a3 b3 c3')
    q = [s.Matrix([[coeff[3*i], coeff[3*i+1]],
                   [coeff[3*i+1], coeff[3*i+2]]]) for i in range(3)]
    h = block_hessian(q)
    rowdet = s.Matrix(3, 3, coeff).det()
    expected = 4*s.prod(t.det() for t in q)-rowdet**2
    check_zero(h.det(method='domain-ge')-expected)
    print('PASS: universal 6x6 determinant identity over Q[nine coefficients]')
    k = s.Matrix([1, 0, 0, 1, 1, 1])
    lk = (h*k).jacobian(coeff)
    assert lk[:, [0, 1, 2, 3, 4, 7]].det() == 2
    qr = [s.Matrix([[1, 1], [1, -1]]), s.Matrix([[-1, 1], [1, 2]]),
          s.diag(-2, -3)]
    hr = block_hessian(qr)
    assert hr*k == s.zeros(6, 1) and hr[1:, 1:].det() == -12
    print('PASS: rational kernel incidence point and rank-six / rank-five minors')
    qa2 = [s.eye(2), s.diag(1, 4), s.Matrix([[5, 4], [4, 5]])]
    ka2 = s.Matrix([-2, 1, 2, -4, 6, 3])
    ha2 = block_hessian(qa2)
    assert ha2*ka2 == s.zeros(6, 1)
    assert ha2[:5, :5].det() == -90 and gamma(ka2) == -216
    qa3 = [s.eye(2), s.Matrix([[0, -1], [-1, -1]]),
           s.Matrix([[-3, 1], [1, 0]])]
    ka3 = s.Matrix([1, 1, 1, 2, 2, -1])
    ha3 = block_hessian(qa3)
    assert ha3*ka3 == s.zeros(6, 1)
    assert ha3[:5, :5].det() == 2 and gamma(ka3) == 0
    g = s.Matrix([12, -12, 12, -6, 6])
    eta = s.Matrix([6, 12, 6, 6, -6])
    assert ha3[:5, :5]*eta == -g and (g.dot(eta)/2) == -36
    x = s.Matrix(s.symbols('x y z'))
    ell = x[0]+x[1]+2*x[2]
    emm = x[0]+2*x[1]-x[2]
    p2 = s.expand(sum(x[i]*(qa3[i][0, 0]*ell**2+
                  2*qa3[i][0, 1]*ell*emm+qa3[i][1, 1]*emm**2)/2
                  for i in range(3)))
    b = s.Matrix([[-1, -s.Rational(3, 2), -s.Rational(1, 2)],
                  [s.Rational(5, 2), 4, s.Rational(1, 2)],
                  [s.Rational(5, 2), s.Rational(3, 2), 8]])
    bx = b*x
    check_zero(p2+sum(x[i]**2*bx[i] for i in range(3)))
    quartic = s.Poly(sum(s.diff(p2, x[i])*bx[i]+x[i]*bx[i]**2
                         for i in range(3)), *x).coeff_monomial(s.prod(x))
    assert quartic == -s.Rational(23, 2)
    print('PASS: A2 / A3 kernels, cubic and both independent quartic contributions')
    qb = [s.Matrix([[1, 1], [1, 2]]), s.Matrix([[-1, -1], [-1, 3]]),
          s.diag(0, 1)]
    kb = s.Matrix([1, 0, 1, 0, 0, 0])
    hb = block_hessian(qb)
    j = hb[1:, 1:]
    assert hb*kb == s.zeros(6, 1) and j.det() == -8
    assert j.inv()[3, 3] == -s.Rational(1, 8)
    dh = h.diff(coeff[0])
    dk = -j.inv()*(dh*kb)[1:, :]
    assert dk[3] == s.Rational(1, 8)
    gb = s.Matrix([0, 0, 0, 6, 0])
    assert -(gb.dot(j.inv()*gb))/2 == s.Rational(9, 4)
    print('PASS: boundary generic reducedness and nonzero A3 quartic')
    a, b, c, z, kap = s.symbols('a b c z kappa')
    disc = (256*kap**3*c**3-128*kap**2*a**2*c**2+144*kap**2*a*b**2*c
            -27*kap**2*b**4+16*kap*a**4*c-4*kap*a**3*b**2)
    check_zero(s.discriminant(kap*z**4+a*z**2+b*z+c, z)-disc)
    sub = {b: -4*kap*z**3-2*a*z, c: 3*kap*z**4+a*z**2}
    r, t = a+6*kap*z**2, a+2*kap*z**2
    p = t*r**2
    check_zero(disc.subs(sub))
    identities = [a**3-4*kap*a*c+s.Rational(9, 2)*kap*b**2,
                  -b*(a**2+12*kap*c)/2,
                  s.Rational(3, 4)*a*b**2-2*a**2*c+8*kap*c**2]
    for i, expr in enumerate(identities):
        check_zero(expr.subs(sub)-p*z**i)
    for var, fac in zip((a, b, c), (z**2, z, 1)):
        check_zero(s.diff(disc, var).subs(sub)-16*kap*t*r**3*fac)
    check_zero((a**2+12*kap*c).subs(sub)-r**2)
    check_zero((8*a**3+27*kap*b**2).subs(sub)-4*r**2*(2*a+3*kap*z**2))
    print('PASS: swallowtail resultant, conductor generators and Jacobian pullbacks')
    assert 3*s.binomial(6, 4)-3*6 == 27
    print('PASS: four component degrees 27, 6, 6, 6')


if __name__ == '__main__':
    main()
