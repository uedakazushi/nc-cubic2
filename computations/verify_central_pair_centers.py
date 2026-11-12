#!/usr/bin/env python3
"""Exact central-pair Rains certificate, reconstructed from its displayed formula.

Weighted free-word engine adapted from nc-cubic commit da722ca,
computations/verify_universal_hesse_mixed_center.py; mathematical input is
Etingof--Ginzburg section 9 and the corrected Rains data.

Original engine documentation:

Central A,B,C,D,E,H are algebraically independent, with weights 1,1,1,2,2,2.
h,t remain indeterminates. All row reduction is over Q(h,t); there are NO
random samples or finite-field specializations. Run with Python + SymPy.
The degree-four free-word quotient gives 339 columns and 162 relation multiples;
all three commutators reduce to zero in the 144-dimensional relation span.
The source variables h,t in this implementation denote t,q respectively.
The printed formulas in the manuscript use q,t; no numeric interpolation is used.
"""
from collections import defaultdict
from itertools import product
import sympy as sp
from sympy.polys.domains import QQ
from sympy.polys.fields import field

h, t = sp.symbols("h t")
K, _h, _t = field("h,t", QQ)
WEIGHTS = (1, 1, 1, 2, 2, 2)
ZERO = (0,) * 6


def central_monomials(weight):
    def rec(i, remaining, powers):
        if i == 6:
            if not remaining:
                yield tuple(powers)
            return
        for k in range(remaining // WEIGHTS[i] + 1):
            yield from rec(i + 1, remaining - k * WEIGHTS[i], powers + [k])
    return list(rec(0, weight, []))


def add(*polys):
    ans = defaultdict(lambda: 0)
    for p in polys:
        for term, value in p.items():
            ans[term] += value
    return {key: v for key, v in ans.items() if v != 0}


def scale(poly, number):
    return {key: v * number for key, v in poly.items() if v * number != 0}


def mul(p, q):
    ans = defaultdict(lambda: 0)
    for (a, w), v in p.items():
        for (b, z), t in q.items():
            ans[(tuple(i + j for i, j in zip(a, b)), w + z)] += v * t
    return {key: v for key, v in ans.items() if v != 0}


def word(w="", center=ZERO):
    return {(center, tuple(w)): sp.S.One}


def central(i):
    return word("", tuple(int(i == j) for j in range(6)))


def cub(p):
    return mul(mul(p, p), p)


x, y, z = (word(a) for a in "xyz")
A, B, C, D, E, H = (central(i) for i in range(6))


def sym2(a, b):
    return scale(add(mul(a, b), mul(b, a)), sp.Rational(1, 2))


def relations():
    # h denotes the source t; t denotes q, kept algebraically independent.
    return (add(mul(x,y),scale(mul(y,x),-t),scale(add(mul(z,z),mul(C,z),H),-h)),
            add(mul(y,z),scale(mul(z,y),-t),scale(add(mul(x,x),mul(A,x),D),-h)),
            add(mul(z,x),scale(mul(x,z),-t),scale(add(mul(y,y),mul(B,y),E),-h)))

def omega():
    q=t; v=h
    aa=q**3-v**3; Q=q*q+q+1
    kk=q**4+q**3+q*q-(2*q+1)*v**3; jj=Q+(q+2)*v**3
    H1=(q+1)*(q**3+q*q+q-v**3)
    H2=q**3+2*q*q+2*q+1+(q+1)*v**3
    H3=q**4+2*q**3+2*q*q+q-(q+1)*v**3
    return add(scale(add(cub(x),cub(z)),(q+1)*aa),scale(cub(y),(q+1)*(1+v**3)),
      scale(word('zyx'),q*(q+1)*((q-1)*Q/v-2*v*v)),
      scale(add(mul(A,mul(x,x)),mul(C,mul(z,z))),kk),scale(mul(B,mul(y,y)),jj),
      scale(mul(A,word('zy')),-(q+1)*v*v*q),scale(mul(B,word('zx')),-(q+1)*v*v),
      scale(mul(C,word('yx')),-(q+1)*v*v*q),
      mul(add(scale(D,H1),scale(mul(A,A),-q*v**3),scale(mul(B,C),-q*v*v)),x),
      mul(add(scale(E,H2),scale(mul(B,B),v**3),scale(mul(A,C),-q*v*v)),y),
      mul(add(scale(H,H3),scale(mul(C,C),-q*v**3),scale(mul(A,B),-q*v*v)),z))


def basis_degree_four():
    return [(c, w) for k in range(5) for c in central_monomials(k)
            for w in product("xyz", repeat=4-k)]


def relation_multiples():
    for k in range(3):
        for c in central_monomials(k):
            for left_size in range(3-k):
                for left in product("xyz", repeat=left_size):
                    for right in product("xyz", repeat=2-k-left_size):
                        for r in relations():
                            yield mul(mul(word("".join(left), c), r),
                                      word("".join(right)))


def verify():
    B = basis_degree_four()
    positions = {key: i for i, key in enumerate(B)}
    pivots = {}
    def reduce(poly, insert=False):
        row = {positions[key]: K.from_expr(sp.sympify(value))
               for key, value in poly.items() if value != 0}
        while row:
            first = min(row)
            if first not in pivots:
                if insert:
                    lead = row[first]
                    pivots[first] = {j: val / lead for j, val in row.items()}
                    return {}
                return row
            multiple = row[first]
            for j, val in pivots[first].items():
                new = row.get(j, K.zero) - multiple * val
                if new:
                    row[j] = new
                else:
                    row.pop(j, None)
        return {}

    R = list(relation_multiples())
    for r in R:
        reduce(r, insert=True)
    assert (len(B), len(R), len(pivots)) == (339, 162, 144)
    # At h=0, q=1 the relations are commutative. A separate rational-rank calculation at h=0 proves h-flatness in degree 4:
    # the rank over Q(h) and the rank at h=0 are both 144.
    special_pivots = {}
    for relation in R:
        row = {positions[key]: sp.Rational(sp.sympify(value).subs({h:0,t:1}))
               for key, value in relation.items()
               if sp.sympify(value).subs({h:0,t:1}) != 0}
        while row:
            lead = min(row)
            if lead not in special_pivots:
                coefficient = row[lead]
                special_pivots[lead] = {i: v / coefficient for i, v in row.items()}
                break
            factor = row[lead]
            for i, v in special_pivots[lead].items():
                new = row.get(i, sp.S.Zero) - factor * v
                if new:
                    row[i] = new
                else:
                    row.pop(i, None)
    assert len(special_pivots) == 144
    Om = omega()
    for generator in (x, y, z):
        comm = add(mul(Om, generator), scale(mul(generator, Om), -1))
        assert not reduce(comm), "universal centrality failed"
    print("PASS: Rains polynomial, 339 words / 162 relations / rank 144; commutative specialization rank 144")
    print("PASS: 3 exact Rains commutators over Q(q,t)[L1,L2,L3,M1,M2,M3]")




def verify_free_identities():
    """Independent free-algebra expansions: no quotient reducer or truncation."""
    X=sp.symbols('X Y Z',commutative=False)
    ee=sp.symbols('e1:4'); mm=sp.symbols('m1:4'); ll=sp.symbols('L1:4')
    def comm(a,b):return a*b-b*a
    def preferred(xx,es,ms):
        import itertools
        top=sum(a**3 for a in xx)/3-h*h*sum(xx[i]*xx[j]*xx[k] for i,j,k in itertools.permutations(range(3)))/9
        for i in range(3):
            j,k=(i+1)%3,(i+2)%3
            top+=es[i]*(xx[j]*xx[k]+xx[k]*xx[j])/2+ms[i]*xx[i]
            top+=h*h*es[i]**2*xx[i]/6+h**4*(es[i]*xx[i]**2-es[j]*es[k]*xx[i])/18
        return top
    def shifts(L,es,ms):
        ns=[ms[i]-L[i]**2/4-(es[(i+1)%3]*L[(i+2)%3]+es[(i+2)%3]*L[(i+1)%3])/2 for i in range(3)]
        cc=sum(L[i]**3/12+es[i]*L[(i+1)%3]*L[(i+2)%3]/4-ms[i]*L[i]/2 for i in range(3))
        return ns,cc
    for shift in range(3):
        xx=X[shift:]+X[:shift];es=ee[shift:]+ee[:shift];ms=mm[shift:]+mm[:shift]
        a,b,c=xx;e1,e2,e3=es;m1,m2,m3=ms
        r=comm(a,b)-h*(c*c+e1*b+e2*a+m3)
        s=comm(b,c)-h*(a*a+e2*c+e3*b+m1)
        t0=comm(c,a)-h*(b*b+e3*a+e1*c+m2)
        c0=-(r*b*b+b*r*b+b*b*r)/3+(t0*c*c+c*t0*c+c*c*t0)/3+m3*t0-m2*r
        c0+=-e3*(r*a+a*r)/2+e2*(t0*a+a*t0)/2+e1*(b*t0-r*c+comm(a,s)/2)
        c1=(comm(b*c+c*b,s)+e3*comm(t0,c)+e2*comm(r,b))/6
        c2=(r*comm(a,c)-s*a*a-t0*(a*b+b*a)-a*r*c+a*s*a+a*t0*b+2*b*t0*a-b*a*t0+c*a*r)/18
        c3=(comm(r,b*b)+comm(t0,c*c)+e1*comm(s,a))/18
        assert sp.expand(comm(preferred(xx,es,ms),a)-c0-h*c1-h*h*c2-h**3*c3)==0
    ns,cc=shifts(ll,ee,mm)
    shifted=tuple(X[i]+ll[i]/2 for i in range(3))
    classical=sum(X[i]**3/3+ll[i]*X[i]**2/2+ee[i]*(X[(i+1)%3]*X[(i+2)%3]+X[(i+2)%3]*X[(i+1)%3])/2+mm[i]*X[i] for i in range(3))
    assert sp.expand(preferred(shifted,ee,ns).subs(h,0)+cc-classical)==0
    # Rains diagonal normalization versus the symmetric preferred normalization.
    rain=0
    for (powers,w),coefficient in omega().items():
        coeff=sp.prod(v**n for v,n in zip(ll+mm,powers))
        mon=sp.prod(X['xyz'.index(letter)] for letter in w)
        rain+=coefficient.subs(t,1)*coeff*mon/6
    ns0,cc0=shifts(ll,(0,0,0),mm)
    pref=preferred(shifted,(0,0,0),ns0)+cc0
    delta=h*h*ll[0]*ll[1]*ll[2]/12+h**3*(ll[0]*mm[0]-ll[1]*mm[1]+ll[2]*mm[2])/6
    a,b,c=X
    r=comm(a,b)-h*(c*c+ll[2]*c+mm[2])
    s=comm(b,c)-h*(a*a+ll[0]*a+mm[0])
    t0=comm(c,a)-h*(b*b+ll[1]*b+mm[1])
    ET=3*c*r-2*t0*b-b*t0+2*s*a+a*s
    assert sp.expand(rain-pref-delta-h*h*ET/9-h*h*(ll[0]*s-ll[1]*t0+ll[2]*r)/6)==0
    print('PASS: all three free-algebra 41-term centrality certificates, translation and exact Rains scalar difference')




def verify_ordered_cubic_minor():
    from sympy.polys.matrices import DomainMatrix
    words=list(product('xyz',repeat=3));pos={w:i for i,w in enumerate(words)}
    unordered=[w for w in words if list(w)!=sorted(w)]
    rels=[{'xy':1,'yx':-t,'zz':-h},{'yz':1,'zy':-t,'xx':-h},{'zx':1,'xz':-t,'yy':-h}]
    rows=[]
    for side in (0,1):
        for letter in 'xyz':
            for rel in rels:
                rows.append({tuple(letter+w if side==0 else w+letter):K.from_expr(s) for w,s in rel.items()})
    sub=DomainMatrix([[r.get(w,K.zero) for w in unordered] for r in rows],(18,17),K.to_domain())
    row_indices=sub.transpose().rref()[1]
    assert len(row_indices)==17
    selected=sub.extract(list(row_indices),list(range(17)))
    determinant=selected.det()
    assert determinant == K.from_expr(-t**5*(t**3-h**3)**2)
    print('PASS: ordered cubic minor rows',list(row_indices),'det=-q^5(q^3-t^3)^2')


if __name__ == '__main__':
    verify()
    verify_free_identities()
    verify_ordered_cubic_minor()
