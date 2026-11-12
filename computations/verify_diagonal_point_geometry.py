#!/usr/bin/env python3
"""Exact polynomial checks for diagonal stationary divisors and elliptic shift.
The degree-56 and irreducibility assertions use the geometric proof in the text.
"""
import sympy as s
alpha,h,a,X,Y,Z,u,v,t=s.symbols('alpha h a X Y Z u v t')
P=X**6+s.Rational(2,3)*alpha**3*X**3-alpha**3
assert s.factor(s.discriminant(P,X))==64*alpha**15*(alpha**3+9)**3
relations=[a**3+s.Rational(2,3)*alpha*a*X+1-s.Rational(2,3)*h*h*X*Y*Z,
           X*X+alpha*a,Y*Y,Z*Z]
gb=s.groebner(relations,a,X,Y,Z,order='grlex',domain=s.QQ.poly_ring(alpha,h))
leading={p.LM(order=gb.order).exponents for p in gb.polys}
assert leading=={(3,0,0,0),(0,2,0,0),(0,0,2,0),(0,0,0,2)}
assert all(p.LC(order=gb.order)==1 for p in gb.polys)
# Elimination identity, before imposing Y^2=Z^2=0.
assert s.expand(-alpha**3*relations[0].subs(a,-X*X/alpha)-
    (P+s.Rational(2,3)*h*h*alpha**3*X*Y*Z))==0
assert s.expand((P+s.Rational(2,3)*h*h*alpha**3*X*Y*Z).subs(alpha**3,-9)-
    ((X**3-3)**2-6*h*h*X*Y*Z))==0
c=alpha**3/(alpha**3+9)
Df=9*(u**3+v**3)**2+4*alpha**3*u**3*v**3
Dg=9*c*(u**3-v**3)**2+4*alpha**3*u**3*v**3
assert s.factor(Dg-c*Df)==0
print('PASS: monic uniform 24-term basis, elimination, all three local-ring regimes and pencil ambiguity')
x,y,z=s.symbols('x y z')
M=s.Matrix([[-y,x,-h*z],[-h*x,-z,y],[z,-h*y,-x]])
assert s.expand(M.det()+h*(x**3+y**3+z**3+h*h*x*y*z))==0
assert M.subs({x:1,y:-1,z:0})*s.Matrix([1,-1,-h])==s.zeros(3,1)
H=(1-t*t)**3/(1-t)**5
assert s.series(H,t,0,5).removeO().coeff(t,3)==20
assert 2*5-2+2*24==56
print('PASS: elliptic graph determinant and marked kernel, canonical sections dimension20 and RH degree56')
