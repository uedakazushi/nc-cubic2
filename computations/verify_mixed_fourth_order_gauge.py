#!/usr/bin/env python3
"""Rebuild fourth-order mixed curvature from PBW/Weyl products and finite BCH.

No high-order cochain data file is read. Coefficients use exact FLINT
multivariate rational polynomials with e1^2=e2^2=m1^2=0. The universal
second-order primitive is constructed and symmetrized before specialization.
"""
from itertools import product, permutations
from functools import lru_cache
from collections import defaultdict
from math import factorial
from flint import fmpq_mpoly_ctx, fmpq
import sympy as sp
import verify_mixed_second_order_gauge as second

CTX=fmpq_mpoly_ctx.get(('x','y','z','e1','e2','m1'),'lex')
X=CTX.gens();ZERO=CTX.constant(0);ONE=CTX.constant(1)
UNIT=[tuple(int(i==j) for j in range(3)) for i in range(3)]
Z=(0,0,0)


def filt(p,weight=None):
    return CTX.from_dict({a:c for a,c in p.to_dict().items()
                          if max(a[3:])<=1 and (weight is None or
                            sum(a[:5])+2*a[5]<=weight)})


def pmul(a,b,weight=None):return filt(a*b,weight)

def pdiff(p,idx):
    for i,n in enumerate(idx):
        for _ in range(n):p=p.derivative(i)
    return p


def sympy_poly(p):
    pp=sp.Poly(p,*second.x,*second.e,*second.m)
    out={}
    for a,c in pp.terms():
        if a[5] or a[7] or a[8]:continue
        ex=a[:3]+a[3:5]+(a[6],)
        if max(ex[3:])<=1:out[ex]=fmpq(int(sp.numer(c)),int(sp.denom(c)))
    return CTX.from_dict(out)


def sparse_add(a,b,scale=1):
    out=dict(a)
    for k,v in b.items():
        new=out.get(k,ZERO)+scale*v
        if new:out[k]=new
        else:out.pop(k,None)
    return out


def arity_filter(c,n):return {k:v for k,v in c.items() if len(k)==n}


def weight_filter(c,w):return {k:q for k,v in c.items() if (q:=filt(v,w))}


@lru_cache(None)
def splits(a,n):
    if n==1:return ((a,),)
    return tuple((b,)+tail for b in product(*(range(i+1) for i in a))
                 for tail in splits(tuple(i-j for i,j in zip(a,b)),n-1))


def fac(a):
    out=1
    for v in a:out*=factorial(v)
    return out


def compose(a,b,maxweight):
    out={}
    if not a or not b:return out
    for aa,co in a.items():
        for i in range(len(aa)):
            for bb,cc in b.items():
                q=len(bb)
                sign=1 if ((q-1)*i)%2==0 else -1
                for div in splits(aa[i],q+1):
                    dc=pdiff(cc,div[0])
                    if not dc:continue
                    val=pmul(co,dc,maxweight)
                    if not val:continue
                    mult=fmpq(fac(aa[i]),int(sp.prod(fac(d) for d in div)))*sign
                    key=aa[:i]+tuple(tuple(j+k for j,k in zip(bi,di))
                                     for bi,di in zip(bb,div[1:]))+aa[i+1:]
                    val=out.get(key,ZERO)+mult*val
                    if val:out[key]=val
                    else:out.pop(key,None)
    return out


def bracket(a,b,maxweight):
    if not a or not b:return {}
    # Mixed-arity even (MC) and odd (gauge) cochains have fixed parity.
    p,q=len(next(iter(a))),len(next(iter(b)))
    return sparse_add(compose(a,b,maxweight),compose(b,a,maxweight),-1 if ((p-1)*(q-1))%2==0 else 1)


# PBW polynomials: (h exponent, central mask, ordered/free word) -> rational.
def word_add(a,b,scale=fmpq(1)):
    out=dict(a)
    for k,v in b.items():
        val=out.get(k,fmpq(0))+scale*v
        if val:out[k]=val
        else:out.pop(k,None)
    return out


@lru_cache(None)
def nf(word,order=4):
    for i in range(len(word)-1):
        if word[i]>word[i+1]:break
    else:return {(0,0,word):fmpq(1)}
    pair=word[i:i+2]
    rules={('y','x'):[(-1,0,('z','z')),(-1,1,('y',)),(-1,2,('x',))],
           ('z','x'):[(1,0,('y','y')),(1,1,('z',))],
           ('z','y'):[(-1,0,('x','x')),(-1,2,('z',)),(-1,4,())]}
    out=dict(nf(word[:i]+(word[i+1],word[i])+word[i+2:],order))
    if order:
        for sign,mask,mid in rules[pair]:
            for (h,mm,ww),co in nf(word[:i]+mid+word[i+2:],order-1).items():
                if mm&mask:continue
                key=(h+1,mm|mask,ww)
                val=out.get(key,fmpq(0))+sign*co
                if val:out[key]=val
                else:out.pop(key,None)
    return out


def wp_mul(a,b):
    out={}
    for (ha,ma,wa),ca in a.items():
        for (hb,mb,wb),cb in b.items():
            if ha+hb>4 or ma&mb:continue
            for (hc,mc,wc),cc in nf(wa+wb,4-ha-hb).items():
                if (ma|mb)&mc:continue
                key=(ha+hb+hc,ma|mb|mc,wc)
                co=out.get(key,fmpq(0))+ca*cb*cc
                if co:out[key]=co
                else:out.pop(key,None)
    return out


def monword(a):return tuple(t for t,n in zip('xyz',a) for _ in range(n))
@lru_cache(None)
def sym_word(a):
    w=monword(a)
    pp=list(permutations(w))
    out={}
    for v in pp:out=word_add(out,nf(v),fmpq(1,len(pp)))
    return out


def change_t(a):
    out={}
    for (hh,mask,w),co in a.items():
        expo=tuple(w.count(t) for t in 'xyz')
        for (hi,mi,wi),ci in sym_word(expo).items():
            if hh+hi>4 or mask&mi:continue
            key=(hh+hi,mask|mi,wi)
            out[key]=out.get(key,fmpq(0))+co*ci
    return {k:v for k,v in out.items() if v}


def inverse_t(a):
    out=dict(a);term=dict(a)
    for n in range(1,5):
        term=word_add(change_t(term),term,-1)
        out=word_add(out,term,(-1)**n)
    return out


def coeff(poly,h):
    out={}
    for (hh,mask,w),c in poly.items():
        if hh!=h:continue
        aa=tuple(w.count(t) for t in 'xyz')+tuple(int(bool(mask&(1<<i))) for i in range(3))
        out[aa]=out.get(aa,fmpq(0))+c
    return CTX.from_dict(out)


def source_jets():
    jets={i:{} for i in range(1,5)}
    # Triangular symbol extraction; positive input orders only.
    for degree in range(2,5):
        for aa in product(range(degree+1),repeat=3):
            if not 0<sum(aa)<degree:continue
            for bb in product(range(degree+1),repeat=3):
                if sum(bb)!=degree-sum(aa):continue
                ww=inverse_t(wp_mul(sym_word(aa),sym_word(bb)))
                for h in range(1,5):
                    if h==4 and degree>3:continue
                    residual=coeff(ww,h)
                    for (ia,ib),co in jets[h].items():
                        if all(i<=j for i,j in zip(ia,aa)) and all(i<=j for i,j in zip(ib,bb)):
                            mult=1;mon=ONE
                            for k in range(3):
                                mult*=factorial(aa[k])//factorial(aa[k]-ia[k])
                                mult*=factorial(bb[k])//factorial(bb[k]-ib[k])
                                mon*=X[k]**(aa[k]+bb[k]-ia[k]-ib[k])
                            residual-=pmul(co,mon)*mult
                    residual/=fac(aa)*fac(bb)
                    if residual:jets[h][(aa,bb)]=residual
    print('Weyl source types:',{i:len(v) for i,v in jets.items()},flush=True)
    return jets


def second_data():
    mu,curv,c1,c2,v,w1,w3=second.main()
    avg={}
    for perm in permutations(range(3)):
        mapping={second.x[i]:second.x[perm[i]] for i in range(3)}
        mapping.update({second.e[i]:second.e[perm[i]] for i in range(3)})
        mapping.update({second.m[i]:second.m[perm[i]] for i in range(3)})
        for key,co in w3.items():
            new=tuple(tuple(a[perm.index(i)] for i in range(3)) for a in key)
            val=sympy_poly(co.xreplace(mapping))/6
            avg=sparse_add(avg,{new:val})
    convert=lambda d:{k:q for k,v in d.items() if (q:=sympy_poly(v))}
    return convert(mu),convert(curv),convert(c1),convert(c2),convert(v),sparse_add(convert(w1),avg)


def chain_key(vertices,total):
    if len(set(vertices))!=len(vertices):return None
    if not vertices:return (total,)
    return (vertices[0],)+tuple(tuple(b-a for a,b in zip(left,right))
                              for left,right in zip(vertices,vertices[1:]))+(
                                  tuple(a-b for a,b in zip(total,vertices[-1])),)


def cobar_primitive(rp,arity):
    groups={}
    for key,co in rp.items():
        total=tuple(sum(a[j] for a in key) for j in range(3))
        groups.setdefault(total,{})[key]=co*int(sp.prod(fac(a) for a in key))
    primitive={}
    for total,rd in groups.items():
        pivot=next(i for i,a in enumerate(total) if a>=2)
        ei=UNIT[pivot]
        for term in splits(total,arity-1):
            if not all(sum(a)>0 for a in term):continue
            vertices=[];partial=Z
            for block in term[:-1]:
                partial=tuple(a+b for a,b in zip(partial,block));vertices.append(partial)
            cv=[tuple(max(a,b) for a,b in zip(t,ei)) for t in vertices]
            # H=K c_* - P; eta_arity=(-1)^(arity-1) H^*.
            kk=chain_key([ei]+cv,total)
            val=rd.get(kk,ZERO) if kk is not None else ZERO
            for j in range(len(vertices)):
                kk=chain_key(vertices[:j+1]+cv[j:],total)
                if kk is not None:val-=((-1)**j)*rd.get(kk,ZERO)
            if val:primitive[term]=-val/int(sp.prod(fac(a) for a in term))
    return primitive


def unary_primitive(rr):
    groups={}
    for key,co in rr.items():
        total=tuple(a+b for a,b in zip(*key))
        val=co*fac(key[0])*fac(key[1])
        if total in groups:assert groups[total]==val, ('not symmetric coboundary',total)
        groups[total]=val
    return {(a,):-co/fac(a) for a,co in groups.items() if co}


def main():
    mu,curv,c1,c2,v,w=second_data()
    jets=source_jets()
    assert jets[1]==c1
    assert {k:val for k,val in jets[2].items() if sum(map(sum,k))<=4}==c2
    print('PASS: PBW/Weyl low symbols agree with full second-order product',flush=True)
    w2=-2*X[0]*X[1]*X[2]/3 # e1^2=e2^2=0
    w4=(X[3]*X[0]**2+X[4]*X[1]**2-X[3]*X[4]*X[2])/18
    s1=jets[1];s2=sparse_add(jets[2],{():w2});s3=jets[3];s4=sparse_add(jets[4],{():w4})
    q2={():X[0]*X[1]*X[2]/3}
    sq=sparse_add(s2,q2)
    # Apply the coefficient-weight projection only after each full nested term.
    r4=weight_filter(s4,3)
    for term,factor in [(bracket(v,s3,3),fmpq(1)),
                        (bracket(v,bracket(v,sq,4),3),fmpq(1,4)),
                        (bracket(w,sq,3),fmpq(1,2)),
                        (bracket(v,bracket(w,s1,4),3),fmpq(1,2))]:
        r4=sparse_add(r4,term,factor)
        print('fourth BCH accumulated types:',len(r4),flush=True)
    print('BCH constructed:',len(r4),flush=True)
    closed=bracket(sparse_add(mu,curv),r4,3)
    assert not closed, ('fourth closedness',len(closed))
    print('PASS: full projected fourth cochain is closed',flush=True)
    for arity in (6,4):
        rp=arity_filter(r4,arity)
        primitive=cobar_primitive(rp,arity)
        assert not sparse_add(bracket(mu,primitive,3),rp,-1)
        r4=sparse_add(r4,bracket(sparse_add(mu,curv),primitive,3),-1)
        print('PASS: descending contraction',arity,'primitive types',len(primitive),
              'remaining types',len(r4),flush=True)
    rr=arity_filter(r4,2)
    yz=rr.get((UNIT[1],UNIT[2]),ZERO)-rr.get((UNIT[2],UNIT[1]),ZERO)
    scalar=yz.to_dict().get((2,0,0,0,0,0),fmpq(0))
    r4=sparse_add(r4,bracket(sparse_add(mu,curv),v,3),-scalar)
    unary=unary_primitive(arity_filter(r4,2))
    assert not sparse_add(bracket(mu,unary,3),arity_filter(r4,2),-1)
    r4=sparse_add(r4,bracket(sparse_add(mu,curv),unary,3),-1)
    assert all(len(k)==0 for k in r4),r4.keys()
    q4=r4.get((),ZERO)
    expected=-fmpq(5,144)*(X[3]*X[0]**2+X[4]*X[1]**2)+X[3]*X[4]*X[2]/24+X[3]*X[5]/48
    print('fourth curvature:',q4,flush=True)
    assert q4==expected, (q4,expected)
    fder=[pdiff(curv[()],UNIT[i]) for i in range(3)]
    jac=-fmpq(5,144)*(pmul(X[3],fder[0])+pmul(X[4],fder[1]))
    assert q4==jac+X[3]*X[4]*X[2]/9+X[3]*X[5]/18
    print('PASS: fourth quantum coefficients V_e[h^4]=1/9 and T_e[h^4]=1/18',flush=True)


if __name__=='__main__':main()
