#!/usr/bin/env python3
"""Exact certificates for the PBW/CY section (requires SymPy).

Construct B_alpha^! over QQ[alpha]. Every elimination pivot is a nonzero
rational constant, so every reduction and basis survives all alpha-values.
Check orthogonality, dimensions, perfect Frobenius pairings with unit
determinants, and the identity Nakayama map on degree one. No numerical
specialization or inference from modular vanishing is used.
"""
import sympy as sp
from itertools import combinations
from sympy.polys.matrices import DomainMatrix
alpha=sp.symbols('alpha'); K=sp.QQ.frac_field(alpha); a=K.gens[0]
REL=[{(0,0):K.one,(1,2):K.one},{(1,1):K.one,(2,0):K.one},{(2,2):K.one,(0,1):K.one},{(3,3):K.one},{(4,4):K.one}]
for i,j in combinations(range(5),2):
 r={(i,j):K.one,(j,i):K.one}
 if (i,j)==(3,4):r[1,2]=a
 REL.append(r)
# Original ten quadratic relations: dual orthogonality is checked directly.
original = [
 {(0,1):K.one,(1,0):-K.one,(2,2):-K.one},
 {(1,2):K.one,(2,1):-K.one,(0,0):-K.one,(3,4):-a},
 {(2,0):K.one,(0,2):-K.one,(1,1):-K.one},
]
for i,j in combinations(range(5),2):
 if j>=3:
  original.append({(i,j):K.one,(j,i):-K.one})
assert len(original)==10 and len(REL)==15
assert all(sum(c*r.get(word,K.zero) for word,c in e.items())==0
           for e in REL for r in original)

def add(out,row,factor=K.one):
 for k,v in row.items():
  z=out.get(k,K.zero)+factor*v
  if z:out[k]=z
  else:out.pop(k,None)
def eliminate(row,piv):
 while row:
  k=max(row)
  if k not in piv:
   c=row[k]
   assert not c.numer.degree() and not c.denom.degree(),c
   piv[k]={j:v/c for j,v in row.items()}
   return
  add(row,piv[k],-row[k])
def normal(row,piv):
 row=dict(row)
 for k in sorted(piv,reverse=True):
  if k in row:add(row,piv[k],-row[k])
 return row
def lin(matrix,vector):
 out={}
 for j,c in vector.items():add(out,matrix[j],c)
 return out
B=[[()],[(i,) for i in range(5)]];L=[[[{i:K.one}] for i in range(5)]]
for n in range(2,7):
 d=len(B[n-1]);piv={}
 for j,_ in enumerate(B[n-2]):
  for rel in REL:
   row={}
   for (x,y),c in rel.items():
    for k,v in L[n-2][y][j].items():add(row,{x*d+k:v},c)
   eliminate(row,piv)
 keep=[i for i in range(5*d) if i not in piv];pos={i:j for j,i in enumerate(keep)}
 B.append([((i//d),)+B[n-1][i%d] for i in keep])
 def compact(row):return{pos[k]:v for k,v in normal(row,piv).items()}
 L.append([[compact({x*d+j:K.one}) for j in range(d)] for x in range(5)])
 assert len(keep)==[1,5,10,10,5,1,0][n]
 print(n,len(keep),'unit rational pivots',flush=True)
def word(w):
 if not w:return {0:K.one}
 return lin(L[len(w)-1][w[0]],word(w[1:]))
for n in range(6):
 rows=[[word(w+v).get(0,K.zero) for v in B[5-n]] for w in B[n]]
 mat=DomainMatrix(rows,(len(rows),len(rows[0])),K)
 det=mat.det();assert det and not det.numer.degree() and not det.denom.degree(),det
 assert det == K.convert([1,1,-1,-1,1,1][n])
 print('pairing',n,det,flush=True)
for i in range(5):
 for w in B[4]:assert word((i,)+w)==word(w+(i,))
print('PASS: Frobenius Nakayama on degree one is identity for every alpha',flush=True)

# Independent small checks of the constant-deformation bimodule complex.
from verify_center_phi_exact import Filtered

def add_q(out, row, scale=1):
    for key, value in row.items():
        value = out.get(key, 0)+scale*value
        if value:
            out[key] = value
        else:
            out.pop(key, None)

def ae_product(left, right):
    out = {}
    for (a,b),c in left.items():
        for (x,y),d in right.items():
            add_q(out, {(a+x,y+b):c*d})  # (a tensor b^op)(x tensor y^op)
    return out

relations = [
    {(1,2):1,(2,1):-1,(0,0):-1},
    {(2,0):1,(0,2):-1,(1,1):-1},
    {(0,1):1,(1,0):-1,(2,2):-1},
]
eta_difference = {}
hessian = [[{} for _ in range(3)] for _ in range(3)]
for j, relation in enumerate(relations):
    for word, coefficient in relation.items():
        add_q(eta_difference, {(j,)+word:coefficient})
        add_q(eta_difference, {word+(j,):-coefficient})
        for k, letter in enumerate(word):
            add_q(hessian[letter][j], {(word[:k],word[k+1:]):coefficient})
assert not eta_difference
operators = [{((i,),()):1,((),(i,)):-1} for i in range(3)]
for i in range(3):
    for j in range(3):
        assert hessian[i][j] == {(b,a):c for (a,b),c in hessian[j][i].items()}
algebra = Filtered()
assert algebra.extend() == (2,10)
def tensor_normal(polynomial):
    out = {}
    for (a,b),c in polynomial.items():
        for i,x in algebra.word(a,2).items():
            for j,y in algebra.word(b,2).items():
                add_q(out, {(i,j):c*x*y})
    return out
for j in range(3):
    composition = {}
    for i in range(3):
        add_q(composition, ae_product(hessian[i][j],operators[i]))
    assert not tensor_normal(composition)
for i in range(3):
    composition = {}
    for j in range(3):
        add_q(composition, ae_product(operators[j],hessian[i][j]))
    assert not tensor_normal(composition)
print("PASS: cubic syzygy, self-dual Hessian and both bimodule chain identities over Q")
