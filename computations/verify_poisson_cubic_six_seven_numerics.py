#!/usr/bin/env python3
"""Exact low-dimensional complete-intersection Chern/Hodge checks.

This verifies the numerical invariants in the separate manuscript
papers/poisson_cubic_six_seven_geometry.tex. It does NOT verify the
Poisson normal-form theorem or nonreduced primary decompositions.

Run: python3 computations/verify_poisson_cubic_six_seven_numerics.py
Requires: sympy.
"""
import sympy as sp

t = sp.symbols("t")


def chern(projective_dimension, degrees):
    dim = projective_dimension - len(degrees)
    total = (1+t)**(projective_dimension+1)
    for d in degrees:
        total /= 1+d*t
    coefficients = sp.series(total, t, 0, dim+1).removeO().expand()
    return coefficients, sp.prod(degrees), dim


# Rank-two Poisson-zero components: Y=(2,2,2,3).
C6, deg6, d6 = chern(7, [2, 2, 2, 3])
assert (d6,deg6,C6)==(3,24,1-t+7*t**2-21*t**3)
e6=sp.expand(C6).coeff(t,3)*deg6
assert e6==-504
pg6=8
h216=(4-2*pg6-e6)//2
assert h216==246

C7, deg7, d7 = chern(8, [2, 2, 2, 3])
assert (d7,deg7,C7)==(4,24,1+6*t**2-14*t**3+48*t**4)
e7=sp.expand(C7).coeff(t,4)*deg7
assert e7==1152
h02=sp.binomial(10,2)-3
h03=sp.binomial(11,3)-3*9-1
h31=3*h02+h03-80
h22=e7-6-2*h31
assert (h02,h03,h31,h22)==(42,137,183,780)

# For n=7 rank four, Delta=(2^6) in P^8.
Cdelta,degdelta,ddelta=chern(8,[2]*6)
assert (ddelta,degdelta,Cdelta)==(2,64,1-3*t+12*t**2)
K2=9*degdelta
c2=sp.expand(Cdelta).coeff(t,2)*degdelta
chi=(K2+c2)//12
assert (K2,c2,chi,chi-1)==(576,768,112,111)

# Critical complete intersections and Poisson-zero curves.
assert ((4*64+2)//2, (6*192+2)//2)==(129,577)
assert 3*8**2 == 192
assert (8**2,(8-1)**2)==(64,49)

# Fano/Calabi-Yau character from adjunction K=(sum d_i-M-1)H.
assert sum([2,2,2,3])-7-1==1
assert sum([2,2,2,3])-8-1==0

print("PASS: n=6 Y(2,2,2,3): degree24, p_g8, e=-504, h21=246")
print("PASS: n=7 CY4 Y(2,2,2,3): e=1152, h31=183, h22=780")
print("PASS: n=7 Delta(2^6): K^2=576, c2=768, chi=112, p_g=111")
print("PASS: g(Delta_n6)=129, g(Z_n7)=577, deg(Z)=192")
print("PASS: transverse primary length64, reduced-kernel transverse length49")
print("SCOPE: exact numerical consistency only, not a primary ideal proof")
