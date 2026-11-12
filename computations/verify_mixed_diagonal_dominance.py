#!/usr/bin/env python3
"""Exact orbit differential and leading formal minors for nine mixed coefficients."""
import sympy as s


def exponents(n,d):
    if n==1:yield (d,)
    else:
        for i in range(d+1):
            for tail in exponents(n-1,d-i):yield (i,)+tail


def main():
    x=s.symbols('x y z u v');u,v=x[3:]
    f=sum(t**3 for t in x[:3])/3+u**3+v**3+sum(x[:3])*(u*u+v*v)
    orbit=[x[j]*s.diff(f,x[i]) for i in range(5) for j in range(5)]
    directions=[m for z in x[:3] for m in (z*u*u,z*u*v,z*v*v)]+[s.prod(x[:3])]
    mon=list(exponents(5,3))
    cols=[]
    for p in orbit+directions:
        pp=s.Poly(p,*x)
        cols.append([pp.coeff_monomial(s.prod(t**a for t,a in zip(x,e))) for e in mon])
    det=s.Matrix(cols).T.det(method='domain-ge')
    assert det==-20736,det
    q,k,a,c=s.symbols('s kappa a c')
    mat=(q+1)*s.eye(3)-s.ones(3)
    assert s.factor(mat.det())==(q-2)*(q+1)**2
    leading=k**3*(2*k*k*a/3)**3*(2*k*k*c/3)**3*mat.det()**2
    assert s.factor(leading-s.Rational(64,729)*k**15*a**3*c**3*(q-2)**2*(q+1)**4)==0
    print('PASS: full 35x35 determinant -20736 and nine-parameter leading minor')


if __name__=='__main__':main()
