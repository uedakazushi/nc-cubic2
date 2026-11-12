#!/usr/bin/env python3
"""Exact PGL2 stabilizer and rational infinitesimal orbit for central pairs."""
import itertools
import sympy as s
points=[(0,1),(1,0),(1,1),(2,1),(4,1),(9,1)]
base=points[:3]
stabilizers=[]
for image in itertools.permutations(points,3):
    rows=[]
    for (u,v),(a,b) in zip(base,image):
        rows.append([b*u,b*v,-a*u,-a*v])
    ns=s.Matrix(rows).nullspace()
    assert len(ns)==1
    mat=s.Matrix(2,2,ns[0]);assert mat.det()
    def same(p,q):return p[0]*q[1]==p[1]*q[0]
    if all(any(same(mat*s.Matrix(p),q) for q in points) for p in points):
        stabilizers.append(mat)
assert len(stabilizers)==1 and stabilizers[0][0,1]==stabilizers[0][1,0]==0
assert stabilizers[0][0,0]==stabilizers[0][1,1]
print('PASS: all 120 rational projective maps checked; six-point stabilizer is trivial')
x,y,z,u,v=s.symbols('x y z u v');xx=(x,y,z,u,v)
q=(u*v,(u-v)*(u-2*v),(u-4*v)*(u-9*v))
P=s.zeros(5)
for i,j,k in ((0,1,2),(1,2,0),(2,0,1)):
    P[j,k]=xx[i]**2+q[i];P[k,j]=-P[j,k]
mons=[xx[i]*xx[j] for i in range(5) for j in range(i,5)]
columns=[]
for a,b in itertools.product(range(5),repeat=2):
    vec=[]
    for i,j in itertools.combinations(range(5),2):
        value=xx[b]*s.diff(P[i,j],xx[a])
        if i==a:value-=P[b,j]
        if j==a:value-=P[i,b]
        p=s.Poly(value,*xx)
        vec.extend(p.coeff_monomial(m) for m in mons)
    columns.append(vec)
mat=s.Matrix.hstack(*(s.Matrix(c) for c in columns));assert mat.shape==(150,25)
assert mat.rank()==24
ns=mat.nullspace();assert len(ns)==1
assert ns[0]==s.Matrix([int(i==j) for i in range(5) for j in range(5)])
sub=mat[:,1:];row_indices=list(sub.T.rref()[1]);assert len(row_indices)==24
det=sub[row_indices,:].det();assert det
print('PASS: orbit differential is 150x25, rank24; scalar kernel only')
print('24x24 minor rows:',row_indices,'columns: 1..24; determinant:',det)
