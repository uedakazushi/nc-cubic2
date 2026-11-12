#!/usr/bin/env python3
"""Exact rational identities in the elliptic product/trace comparison.

The interpretation as Serre traces is proved by the evaluation-sequence
Cech argument in the manuscript, not by finite numerical tests.
"""
import sympy as s


def zero(p):
    assert s.factor(p)==0, s.factor(p)


def main():
    h,x,y,z=s.symbols('h x y z')
    delta=3+h**3
    ell=x+y
    k=z-h*x
    qc=x*x-x*y+y*y+h*h*x*z
    rc=z*z+h*x*z
    pc=s.Matrix([[k,qc/3],[-ell,rc/3]])
    ss=-z/3-2*h*x/delta
    tt=(4*h*h*x-2*h*h*y)/(3*delta)
    rr=2*h*h/delta
    ac=s.Matrix([[ss,tt],[-rr,1]])
    zero(s.trace(pc*ac))
    aval=s.factor(ac.det().subs({x:1,y:-1,z:h}))
    zero(aval+9*h*(1+h**6/27)/delta**2)
    curve=x**3+y**3+z**3+h*h*x*y*z
    zero((curve-3*(ell*qc+k*rc)/3))
    # y'(t) from H(1,y,t)=0, then omega/dt=1/(y^2+h^2 t/3).
    t=s.symbols('t')
    yp=-(3*t*t+h*h*y)/(3*y*y+h*h*t)
    w=1/(y*y+h*h*t/3)
    zero(yp.subs({t:0,y:-1})-h*h/3)
    zero(yp.subs({t:-h,y:-1})+2*h*h/(3-h**3))
    res_o=s.factor(rr/(h*h/3))
    res_p=s.factor(rr*(3/(3-h**3))/(-2*h*h/(3-h**3)))
    zero(res_o-6/delta)
    zero(res_p+3/delta)
    trace=res_o+res_p
    zero(aval/((-h)*trace**2)-(1+h**6/27))
    matrix=s.Matrix([[-2,-1],[3,1]])
    assert (matrix-s.eye(2)).det()==3
    print('PASS: target evaluation cocycle, square scalar, two residues, scalar elimination, rigidity matrix')


if __name__=='__main__':main()
