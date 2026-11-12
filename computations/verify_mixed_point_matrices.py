#!/usr/bin/env python3
"""Exact free-word quotient checks over Q(h), with m independent of h.

This rebuilds the point-ideal MF, mixed defects, evaluation cocycle, and
product homotopy. It does not infer categorical equivalences from matrices.
"""
from itertools import product, permutations
from collections import defaultdict
from sympy.polys.domains import QQ
from sympy.polys.fields import field

K, h = field('h', QQ)


def add(*ps):
    d = defaultdict(lambda: K.zero)
    for p in ps:
        for k, v in p.items(): d[k] += v
    return {k:v for k,v in d.items() if v}


def sc(p, c):
    return {k:v*c for k,v in p.items() if v*c}


def mul(p, q):
    d = defaultdict(lambda: K.zero)
    for (a,w),v in p.items():
        for (b,z),t in q.items(): d[(a+b,w+z)] += v*t
    return {k:v for k,v in d.items() if v}


def word(w): return {(0,w):K.one}
zero = {}
one = word('')
x,y,z = (word(t) for t in 'xyz')
m = {(1,''):K.one}


def matrix(rows): return rows

def mm(a,b):
    return [[add(*(mul(a[i][k],b[k][j]) for k in range(len(b))))
             for j in range(len(b[0]))] for i in range(len(a))]


def ma(a,b): return [[add(a[i][j],b[i][j]) for j in range(2)] for i in range(2)]

def ms(a,c): return [[sc(p,c) for p in row] for row in a]


def diag(p): return [[p,zero],[zero,p]]


def quotient(mixed=True):
    basis = [(a, ''.join(w)) for d in range(5) for a in range(d//2+1)
             for w in product('xyz',repeat=d-2*a)]
    pos = {k:i for i,k in enumerate(basis)}
    rel = [add(word('xy'),sc(word('yx'),-1),sc(word('zz'),-h)),
           add(word('yz'),sc(word('zy'),-1),sc(word('xx'),-h),sc(m,-h) if mixed else zero),
           add(word('zx'),sc(word('xz'),-1),sc(word('yy'),-h))]
    piv = {}
    def reduce(p, insert=False):
        row = {pos[k]:v for k,v in p.items() if v}
        while row:
            i = min(row)
            if i not in piv:
                if insert:
                    lead=row[i];piv[i]={j:v/lead for j,v in row.items()}
                    return {}
                return row
            fac=row[i]
            for j,v in piv[i].items():
                new=row.get(j,K.zero)-fac*v
                if new: row[j]=new
                else: row.pop(j,None)
        return row
    for d in range(3):
        for a in range(d//2+1):
            for nleft in range(d-2*a+1):
                for left in product('xyz',repeat=nleft):
                    for right in product('xyz',repeat=d-2*a-nleft):
                        for r in rel:
                            p=mul(mul({(a,''.join(left)):K.one},r),word(''.join(right)))
                            reduce(p,True)
    return reduce


def main():
    reduce=quotient()
    ell=add(x,y)
    q=add(word('xx'),sc(word('xy'),-1),word('yy'))
    aa=add(z,sc(add(y,sc(x,-1)),h))
    bb=add(sc(ell,-1),sc(z,-h*h))
    q1=add(q,sc(word('zz'),h),sc(word('xz'),-h*h))
    q2=add(word('zz'),sc(word('xz'),h),sc(word('yz'),-2*h),sc(q,h*h))
    r1=add(word('zz'),sc(word('xz'),-h),sc(word('yy'),-h*h))
    r2=add(sc(q,-1),sc(word('zz'),-h))
    p=[[aa,sc(q1,K.one/3)],[bb,sc(q2,K.one/3)]]
    qq=[[sc(r1,K.one/3),sc(r2,K.one/3)],[ell,z]]
    omega=add(sc(add(word('xxx'),word('yyy'),word('zzz')),K.one/3),
              sc(add(*(word(''.join(t)) for t in permutations('xyz'))),-h*h/9))
    center=add(omega,mul(m,x))
    j=sc(add(sc(word('xx'),h*h),sc(word('xz'),2*h),sc(word('yx'),-2*h*h),
             sc(word('yy'),4*h*h),sc(word('yz'),-2*h),sc(word('zy'),-2*h),
             sc(word('zz'),-2*h**3)),K.one/9)
    r0=[[x,sc(add(x,sc(y,-2)),h/3)],
        [sc(add(sc(x,h*h),sc(z,2*h)),K.one/3),add(x,sc(z,2*h*h/3))]]
    rr1=[[add(x,sc(z,2*h*h/3)),sc(j,-1)],[sc(one,-h),x]]
    def check(mat,label):
        for row in mat:
            for pol in row:
                assert not reduce(pol), (label,pol,reduce(pol))
        print('PASS:',label)
    check(ma(ma(mm(p,qq),ms(diag(center),-1)),[[mul(m,t) for t in row] for row in r0]),'PQ mixed defect')
    check(ma(ma(mm(qq,p),ms(diag(center),-1)),[[mul(m,t) for t in row] for row in rr1]),'QP mixed defect')
    check(ma(mm(r0,p),ms(mm(p,rr1),-1)),'mixed intertwiner R0 P = P R1')
    check(ma(mm(rr1,qq),ms(mm(qq,r0),-1)),'mixed intertwiner R1 Q = Q R0')
    # Evaluation cocycle and its square homotopy live on the m=0 fibre.
    reduce=quotient(mixed=False)
    aaev=[[sc(add(sc(y,h),sc(z,-1)),K.one/3),zero],[zero,one]]
    bbev=[[one,sc(x,h*h/3)],[sc(one,h*h),sc(add(sc(x,-h),sc(y,2*h),sc(z,h**3-1)),K.one/3)]]
    check(ma(mm(p,aaev),mm(bbev,qq)),'evaluation cocycle, first block')
    check(ma(mm(qq,bbev),mm(aaev,p)),'evaluation cocycle, second block')
    astar=[[sc(one,-K.one/3),sc(one,-2*h/3)],[zero,zero]]
    bstar=[[zero,sc(one,2*h/3)],[zero,sc(one,(h**3-1)/3)]]
    check(ma(ma(mm(p,astar),mm(bstar,qq)),ms(ma(mm(bbev,aaev),ms(r0,h)),-1)),
          'evaluation square = -h R modulo boundary, first block')
    check(ma(ma(mm(qq,bstar),mm(astar,p)),ms(ma(mm(aaev,bbev),ms(rr1,h)),-1)),
          'evaluation square = -h R modulo boundary, second block')
    print('LIMIT: no matrix identity by itself determines the periodicity scalar or Serre trace')


if __name__=='__main__': main()
