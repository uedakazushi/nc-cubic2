#!/usr/bin/env python3
"""Construct a finite curved Hochschild primitive rather than read old JSON.

All input differential symbols and all six central coefficients are kept.
The primitive is found by rational linear systems; bracket identities are
then checked using an independent ordinary-derivative insertion engine.
"""
import sympy as s
from itertools import product, permutations
from collections import defaultdict
from functools import lru_cache
from math import factorial

x=s.symbols('x y z'); e=s.symbols('e1:4'); m=s.symbols('m1:4')
z0=(0,0,0); units=[tuple(int(i==j) for j in range(3)) for i in range(3)]
F=sum(t**3 for t in x)/3+sum(e[i]*x[(i+1)%3]*x[(i+2)%3]+m[i]*x[i] for i in range(3))


def clean(p):return {k:s.expand(v) for k,v in p.items() if s.expand(v)!=0}
def add(a,b,c=1):
    d=defaultdict(lambda:s.S.Zero,a)
    for k,v in b.items():d[k]+=c*v
    return clean(d)
def plus(a,b):return tuple(i+j for i,j in zip(a,b))
def fact(a):return s.prod(factorial(i) for i in a)
@lru_cache(None)
def diff(p,a):
    for t,n in zip(x,a):p=s.diff(p,t,n)
    return p
@lru_cache(None)
def splits(a,n):
    if n==1:return ((a,),)
    out=[]
    for b in product(*(range(i+1) for i in a)):
        for tail in splits(tuple(i-j for i,j in zip(a,b)),n-1):out.append((b,)+tail)
    return tuple(out)


def insert(a,b,i):
    out=defaultdict(lambda:s.S.Zero)
    for aa,co in a.items():
        for bb,cc in b.items():
            for div in splits(aa[i],len(bb)+1):
                dc=diff(cc,div[0])
                if dc==0:continue
                new=aa[:i]+tuple(plus(j,k) for j,k in zip(bb,div[1:]))+aa[i+1:]
                mult=s.Rational(fact(aa[i]),s.prod(fact(d) for d in div))
                out[new]+=co*dc*mult
    return clean(out)


def circ(a,b):
    if not a or not b:return {}
    p,q=len(next(iter(a))),len(next(iter(b)))
    out={}
    for i in range(p):out=add(out,insert(a,b,i),s.Integer(-1)**((q-1)*i))
    return out


def bracket(a,b):
    p,q=len(next(iter(a))),len(next(iter(b)))
    return add(circ(a,b),circ(b,a),-s.Integer(-1)**((p-1)*(q-1)))


def partitions(a,n):
    return [v for v in splits(a,n) if all(sum(t)>0 for t in v)]


def hdiff(term):
    # Divided derivatives: transpose of the finite simplicial coboundary.
    out=defaultdict(lambda:s.S.Zero)
    n=len(term)
    for i,a in enumerate(term):
        for b,c in partitions(a,2):out[term[:i]+(b,c)+term[i+1:]]+=s.Integer(-1)**(n+i)
    return clean(out)


def construct(rhs):
    groups={}
    for key,co in rhs.items():
        total=tuple(sum(v[j] for v in key) for j in range(3))
        groups.setdefault(total,{})[key]=co* s.prod(fact(v) for v in key)
    w={}
    for total, rr in sorted(groups.items()):
        cols=sorted(partitions(total,3)); rows=sorted(partitions(total,4))
        mat=s.zeros(len(rows),len(cols));pos={r:i for i,r in enumerate(rows)}
        for j,col in enumerate(cols):
            for row,v in hdiff(col).items():mat[pos[row],j]=v
        piv=mat.rref()[1]
        # Deterministic left pivot solution with all other coordinates zero.
        try:
            sol,params=mat[:,list(piv)].gauss_jordan_solve(s.Matrix([rr.get(r,0) for r in rows]))
        except ValueError:
            print('FAILED BLOCK',total, 'rows',len(rows),'cols',len(cols), 'rhs',rr,flush=True)
            raise
        assert params.rows==0
        for j,co in zip(piv,sol):
            if co!=0:w[cols[j]]=s.expand(co/s.prod(fact(v) for v in cols[j]))
    return clean(w)


def main():
    mu={(z0,z0):s.S.One};curv={():F}
    pi=s.Matrix(3,3,lambda i,j:sum(s.LeviCivita(i,j,k)*s.diff(F,x[k]) for k in range(3)))
    c1={(units[i],units[j]):pi[i,j]/2 for i,j in product(range(3),repeat=2) if pi[i,j]!=0}
    v={tuple(units[i] for i in p):-s.LeviCivita(*p)/6 for p in permutations(range(3))}
    c2=defaultdict(lambda:s.S.Zero)
    for i,j,k,l in product(range(3),repeat=4):
        c2[(plus(units[i],units[k]),plus(units[j],units[l]))]+=pi[i,j]*pi[k,l]/8
        c=pi[i,j]*s.diff(pi[k,l],x[j])/12
        c2[(plus(units[i],units[k]),units[l])]+=c
        c2[(units[k],plus(units[i],units[l]))]-=c
    c2=clean(c2)
    assert not add(bracket(mu,c2),{k:co/2 for k,co in bracket(c1,c1).items()})
    assert not bracket(curv,c1)
    assert c2=={(b,a):co for (a,b),co in c2.items()}
    hh=s.hessian(F,x);adj=hh.adjugate()
    w1=defaultdict(lambda:s.S.Zero)
    for i,j in product(range(3),repeat=2):w1[(plus(units[i],units[j]),)]+=adj[i,j]/24
    w1=clean(w1)
    assert not bracket(mu,v)
    assert not add(bracket(curv,v),c1,-1)
    rhs={k:co/2 for k,co in bracket(v,c1).items()}
    assert not bracket(mu,rhs), bracket(mu,rhs)
    w3=construct(rhs)
    assert not add(bracket(mu,w3),rhs,-1)
    rem=add(add(c2,bracket(curv,w3),-1),bracket(mu,w1),-1)
    print('constructed primitive ordinary differential types:',len(w3),flush=True)
    print('primitive polynomial coefficient terms:',sum(len(s.Poly(co,*x,*e,*m).terms()) for co in w3.values()),flush=True)
    print('second identity residual types:',len(rem),flush=True)
    assert not rem, rem
    assert not add(bracket(curv,w1),{():-hh.det()/8},-1)
    print('PASS: all finite second-order curved gauge identities with all e_i,m_i independent')
    return mu,curv,c1,c2,v,w1,w3


if __name__=='__main__':main()
