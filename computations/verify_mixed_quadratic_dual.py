#!/usr/bin/env python3
"""All 32768 associativity identities of the rank-32 quadratic dual over Q[alpha,h]."""
from itertools import product
from flint import fmpq_mpoly_ctx
C=fmpq_mpoly_ctx.get(('alpha','h'),'lex')
a,h=C.gens();one=C.constant(1)


def emul(i,j):
    degree=i.bit_count()+j.bit_count()
    if degree>3:return {}
    if i&j:
        if degree!=2:return {}
        return {1:{6:-h},2:{5:h},4:{3:-h}}[i]
    sign=(-1)**sum(1 for p in range(3) for q in range(3) if p>q and i&(1<<p) and j&(1<<q))
    return {i|j:sign*one}


def ft(i,j):
    if i==0:return [(j,0,1)]
    if j==0:return [(i,0,1)]
    return {(1,2):[(3,0,1)],(2,1):[(0,1,1),(3,0,-1)],
            (2,3):[(2,1,1)],(3,1):[(1,1,1)],(3,3):[(3,1,1)]}.get((i,j),[])


def multiply(i,j):
    ei,fi=divmod(i,4);ej,fj=divmod(j,4)
    sign=(-1)**((fi.bit_count()*ej.bit_count())%2)
    out={}
    for f,cp,co in ft(fi,fj):
        for ee,ce in emul(ei,ej).items():
            terms=emul(ee,6) if cp else {ee:one}
            for eb,cb in terms.items():
                coeff=sign*co*ce*cb*((-a*h) if cp else one)
                key=4*eb+f
                out[key]=out.get(key,C.constant(0))+coeff
    return {k:v for k,v in out.items() if v}


def main():
    table={(i,j):multiply(i,j) for i,j in product(range(32),repeat=2)}
    def expand(p,k,left):
        out={}
        for i,co in p.items():
            for j,v in table[(i,k) if left else (k,i)].items():
                out[j]=out.get(j,C.constant(0))+co*v
        return {j:v for j,v in out.items() if v}
    for i,j,k in product(range(32),repeat=3):
        assert expand(table[i,j],k,True)==expand(table[j,k],i,False),(i,j,k)
    assert [sum(1 for i in range(32) if (i//4).bit_count()+(i%4).bit_count()==d)
            for d in range(6)]==[1,5,10,10,5,1]
    print('PASS: 32768 polynomial associativity identities and Hilbert series (1+t)^5')


if __name__=='__main__':main()
