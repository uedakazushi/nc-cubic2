#!/usr/bin/env python3
"""Exact certificates for global regularity, classical geometry and Cayley compactification.
Requires SymPy. Universal h calculation uses QQ(h); its exceptional pivots
are handled by the proved h=1 case, cubic scaling, opposite algebra, and h=0.
These checks do not infer characteristic-zero identities from modular zeroes.
"""
import sympy as sp
from itertools import product,permutations
h=sp.symbols('h');K=sp.QQ.frac_field(h);hh=K.gens[0]
words=[(a,w) for a in range(3) for w in product(range(3),repeat=4-2*a)]
idx={w:i for i,w in enumerate(words)}
rels=[{(0,(0,1)):K.one,(0,(1,0)):-K.one,(0,(2,2)):-hh},
 {(0,(1,2)):K.one,(0,(2,1)):-K.one,(0,(0,0)):-hh,(1,()):-hh},
 {(0,(2,0)):K.one,(0,(0,2)):-K.one,(0,(1,1)):-hh}]
def add(out,row,factor=K.one):
 for k,v in row.items():
  z=out.get(k,K.zero)+factor*v
  if z:out[k]=z
  else:out.pop(k,None)
piv={};factors=set();relation_rows=0
for a in range(2):
 for size in [2-2*a]:
  for cut in range(size+1):
   for w in product(range(3),repeat=size):
    for rel in rels:
     relation_rows+=1
     row={idx[(a+b,w[:cut]+z+w[cut:])]:c for (b,z),c in rel.items()}
     while row:
      k=max(row)
      if k not in piv:
       c=row[k]
       factors.add(str(sp.factor(K.to_sympy(c))))
       piv[k]={j:v/c for j,v in row.items()};break
      add(row,piv[k],-row[k])
assert len(words)==91 and relation_rows==84 and len(piv)==69
W={(0,(i,i,i)):K(3) for i in range(3)}
for w in permutations(range(3)):W[0,w]=-hh**2
W[1,(0,)]=K(9)
for x in range(3):
 row={}
 for (a,w),c in W.items():
  add(row,{idx[(a,w+(x,))]:c});add(row,{idx[(a,(x,)+w)]:-c})
 for k in sorted(piv,reverse=True):
  if k in row:add(row,piv[k],-row[k])
 assert not row,(x,row)
print('PASS rank69/91, universal h centrality; pivots',sorted(factors))

# Remaining exceptional pivots h^6=1 follow from h=1 by root-of-unity
# scaling and passage to the opposite algebra; h=0 is commutative.
w=sp.symbols('omega')
Wsym={(a,z):K.to_sympy(c) for (a,z),c in W.items()}
for (a,z),c in Wsym.items():
    changed=c.subs(h,w*h)*w**z.count(1)
    assert sp.rem(sp.expand(changed-c),w*w+w+1,w)==0
assert {(a,tuple(reversed(z))):c for (a,z),c in Wsym.items()}==Wsym
for pivot in factors:
    # Numerators and denominators specialize away from 0 or h^6=1.
    for expression in sp.together(sp.sympify(pivot)).as_numer_denom():
        for factor,exponent in sp.factor_list(expression,h)[1]:
            assert sp.rem(h*(h**6-1),factor,h)==0
for relation,phase in zip(rels,(w,w,sp.Integer(1))):
 for (mpower,word),coefficient in relation.items():
  original=K.to_sympy(coefficient)
  changed=original.subs(h,w*h)*w**word.count(1)
  assert sp.rem(sp.expand(changed-phase*original),w*w+w+1,w)==0
print('PASS: exceptional h-values covered by exact cubic scaling and opposite symmetry')

# Binary cubic discriminant, with the homogeneous degree-two resultant.
a,b,c,d,u,v,t=sp.symbols('a b c d u v t')
f=a*u**3+b*u*u*v+c*u*v*v+d*v**3
Delta=b*b*c*c-4*a*c**3-4*b**3*d-27*a*a*d*d+18*a*b*c*d
result=sp.resultant(sp.diff(f,u).subs(v,1),sp.diff(f,v).subs(v,1),u)
assert sp.expand(result+3*Delta)==0
assert sp.factor((1-t**2)**3/(1+t**3)).as_numer_denom()[1]==t*t-t+1
assert sp.factor((1-t)**4/(1-t**3)).as_numer_denom()[1]==t*t+t+1

# Classical pencil and its two resultant normalizations.
alpha,slope=sp.symbols('alpha slope')
pencil=4*alpha**3*slope**3+9*(1+slope**3)**2
x=sp.symbols("x")
p=x**3/3+alpha*slope*x+1+slope**3
assert sp.expand(sp.resultant(p,sp.diff(p,x),x)-pencil/9)==0
assert sp.factor(sp.discriminant(pencil,slope))==2**12*3**14*alpha**9*(alpha**3+9)**3
assert sp.rem(pencil-4*(alpha**3+9),slope**3-1,slope)==0
basis=[sp.Integer(1),u,v,u*v]
gb=sp.groebner([3*u*u+alpha*v,3*v*v+alpha*u],u,v,order="grlex",domain=sp.QQ.frac_field(alpha))
columns=[]
for monomial in basis:
 normal=sp.Poly(gb.reduce((1+alpha*u*v)*monomial)[1],u,v)
 columns.append([normal.coeff_monomial(term) for term in basis])
mult=sp.Matrix.hstack(*(sp.Matrix(column) for column in columns))
assert sp.factor(mult.det())==(alpha**3+9)**3/729
assert sp.factor((3**8*mult.det())**4)==3**8*(alpha**3+9)**12

# Cayley surface and the selected anticanonical elliptic boundary.
U,V,Wc,T=sp.symbols('U V W T')
a0,a1,a2,a3=aa=sp.symbols('a0 a1 a2 a3')
change=sp.Matrix([[-9,-1,-1,-1],[0,-4,-4*w,-4*w*w],
                  [0,4,4*w*w,4*w],[-63,1,1,1]])
rem=lambda x:sp.rem(sp.expand(x),w*w+w+1,w)
assert rem(change.det()+3456*(2*w+1))==0
P=49*U**3-14*U*U*T+U*T*T+(11*U-T)*V*Wc+V**3-Wc**3
sub=dict(zip((U,V,Wc,T),change*sp.Matrix(aa)))
sigma=sum(aa[i]*aa[j]*aa[k] for i in range(4) for j in range(i+1,4) for k in range(j+1,4))
assert rem(P.subs(sub,simultaneous=True)+1728*sigma)==0
assert sub[T]==-63*a0+a1+a2+a3
boundary=P.subs(T,0)
assert list(sp.groebner([sp.diff(boundary,x).subs(U,1) for x in (U,V,Wc)],V,Wc))==[1]
print('PASS: binary discriminant, Hilbert poles, classical pencil/resultants, Cayley transform and smooth boundary')

# The specified translation point on E1 has exact order six.
x,y,z=sp.symbols('x y z')
elliptic=x**3+y**3+z**3+x*y*z
O={x:1,y:-1,z:0};p={x:1,y:-1,z:-1};twop={x:1,y:0,z:-1}
assert all(elliptic.subs(point)==0 for point in (O,p,twop))
assert sp.hessian(elliptic,(x,y,z)).det().subs(O)==0
assert sp.hessian(elliptic,(x,y,z)).det().subs(twop)==0
assert sp.hessian(elliptic,(x,y,z)).det().subs(p)!=0
assert sp.expand(elliptic.subs(x,-(y+z)/2)-sp.Rational(7,8)*(y+z)*(y-z)**2)==0
assert sp.Matrix([[1,-1,0],[0,1,-1],[1,0,-1]]).det()==0
q=sp.symbols('q')
assert sp.expand(sp.discriminant(3*q*q+2*alpha**3*q-3*alpha**3,q)-4*alpha**3*(alpha**3+9))==0
print('PASS: exact order-six tangent/flex computation and six stationary length-four points')
