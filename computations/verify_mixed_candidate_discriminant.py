#!/usr/bin/env python3
"""Exact norm proof of the five-variable Hesse candidate discriminant."""
import sympy as s


def main():
    c, k, a, h, t = s.symbols('c kappa alpha h t')
    def mul_rs(t):
        return s.Matrix([[0,0,0,0], [0,t*t,0,0], [0,0,t*t,0], [1,0,0,t*t]])
    normmat = s.eye(16)+c*s.kronecker_product(mul_rs(c),s.eye(4))+k*a*s.kronecker_product(s.eye(4),mul_rs(a/3))
    d = 1+c**3
    norm = normmat.det(method='domain-ge')
    expected = d**3*(1+k*a**3/9)**3*(d+k*a**3/9)**9
    assert s.expand(norm-expected) == 0
    resultant = 3**8*k**32*d**3*(k*a**3+9)**3*(k*a**3+9*d)**9
    assert s.expand((3*k)**32*norm-resultant) == 0
    dh = 1+h**6/27
    assert s.factor(resultant.subs({c:h**2/3,k:dh})-
                    3**8*dh**44*(dh*a**3+9)**3*(a**3+9)**9) == 0
    yz = [s.zeros(2),s.Matrix([[-2*c,c],[c,-2*c]])]
    # Only yz products are needed: 0 or c^2; uv=alpha^2/9.
    assert s.det(s.Matrix([[0,c],[c,0]]))*(k*k*(36*a*a/9-a*a)) == -3*c*c*k*k*a*a
    assert s.det(s.Matrix([[-2*c,c],[c,-2*c]]))*(k*k*(36*a*a/9-a*a)) == 9*c*c*k*k*a*a
    print('PASS: symbolic 16x16 norm, resultant constant and powers, candidate specialization, node Hessians')


if __name__=='__main__':
    main()
