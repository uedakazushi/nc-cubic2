#!/usr/bin/env python3
"""Reproduce the filtered degree-18 center checks over F_101.

This checks dim F_18=1330, rank 49 of 50 weighted center monomials
and the stated cubic central relation modulo 101. A modular zero
alone is NOT a characteristic-zero proof of the relation. See the
separate exact-Q degree-7 certificate verify_center_degree7.py.
Python 3 standard library, no floating point, no GitHub Actions.
Run: python3 computations/verify_center_weight18_mod101.py
The full filtered computation may be expensive.
"""
from itertools import product
from functools import lru_cache

P = 101
def addto(out, vec, scale=1):
    for key, val in vec.items():
        z = (out.get(key, 0) + val * scale) % P
        if z: out[key] = z
        else: out.pop(key, None)

def row_reduce(row, piv, insert=False):
    row = {k: v % P for k, v in row.items() if v % P}
    while row:
        k = max(row)
        if k not in piv:
            if insert:
                inv = pow(row[k], -1, P)
                piv[k] = {i: x * inv % P for i, x in row.items()}
            return row
        addto(row, piv[k], -row[k])
    return row

def canonical(row, piv):
    row = dict(row)
    for k in sorted(piv, reverse=True):
        if k in row: addto(row, piv[k], -row[k])
    return row

# B[n] is a word basis of F_n, L[n][x] multiplies from the left
# F_n -> F_(n+1), E[n] is the natural inclusion F_n -> F_(n+1).
B = [[()], [(), (0,), (1,), (2,)]]
L = [[[ {x+1: 1} ] for x in range(3)]]
E = [[{0: 1}]]

def linear_map(matrix, v):
    out = {}
    for j, c in v.items(): addto(out, matrix[j], c)
    return out

def word_value(w, n):
    if n == 0: return {0:1}
    if len(w) < n: return linear_map(E[n-1], word_value(w, n-1))
    return linear_map(L[n-1][w[0]], word_value(w[1:], n-1))

def candidate_word(w, n):
    if not w: return {0:1}
    x, tail = w[0], w[1:]
    return {1+x*len(B[n-1])+j: c
            for j, c in word_value(tail,n-1).items()}

REL = (
    ((0,1,1),(1,0,-1),(2,2,-1)),
    ((1,2,1),(2,1,-1),(0,0,-1)),
    ((2,0,1),(0,2,-1),(1,1,-1)),
)

def build_to_17():
    for n in range(2, 18):
        d = len(B[n-1])
        piv = {}
        for j, word in enumerate(B[n-2]):
            for ri, triples in enumerate(REL):
                row = {}
                for x, y, coeff in triples:
                    for k, v in L[n-2][y][j].items():
                        pos = 1 + x*d + k
                        row[pos] = (row.get(pos, 0) + coeff*v) % P
                if ri == 1:
                    for pos, v in candidate_word(word, n).items():
                        row[pos] = (row.get(pos, 0)-v) % P
                row_reduce(row, piv, insert=True)
        bases = [k for k in range(1+3*d) if k not in piv]
        pos = {k: i for i,k in enumerate(bases)}
        B.append([() if k == 0 else
                  ((k-1)//d,)+B[n-1][(k-1)%d] for k in bases])
        def canon_index(row):
            return {pos[k]: v for k,v in canonical(row, piv).items()}
        L.append([[canon_index({1+x*d+j: 1}) for j in range(d)]
                  for x in range(3)])
        E.append([canon_index(candidate_word(word, n)) for word in B[n-1]])
        expected = (n+1)*(n+2)*(n+3)//6
        assert len(B[n]) == expected, (n, len(B[n]), expected)
        print("PBW", n, expected, flush=True)

def build_degree18():
    n = 18
    d = len(B[17])
    piv = {}
    for j, word in enumerate(B[16]):
        for ri, triples in enumerate(REL):
            row = {}
            for x,y,coeff in triples:
                for k,v in L[16][y][j].items():
                    pos = 1+x*d+k
                    row[pos] = (row.get(pos,0)+coeff*v)%P
            if ri == 1:
                for pos,v in candidate_word(word,n).items():
                    row[pos] = (row.get(pos,0)-v)%P
            row_reduce(row,piv,insert=True)
    bases = [k for k in range(1+3*d) if k not in piv]
    assert len(bases) == 1330
    return piv, {key:i for i,key in enumerate(bases)}

def polynomial(terms):
    return {tuple("XYZ".index(c) for c in w): v % P
            for w,v in terms.items() if v % P}

def pol_add(a,b,factor=1):
    out=dict(a)
    addto(out,b,factor)
    return out

def pol_mul(a,b):
    out={}
    for w,c in a.items():
        for z,d in b.items():
            key=w+z
            out[key]=(out.get(key,0)+c*d)%P
    return {k:v for k,v in out.items() if v}

def pol_scale(a,c):
    return {k:v*c%P for k,v in a.items() if v*c%P}

def central_generators():
    g=polynomial({"YYY":1,"ZYX":-1,"X":1})
    u=pol_mul(polynomial({"ZZZ":1}),pol_add(g,polynomial({"ZZZ":-1})))
    v=polynomial({
        "YZZYYY":1,"ZYZZYX":-1,"ZYZZZZ":-1,
        "ZZYYZX":2,"ZZYZZZ":1,"ZZZYZZ":-3,
        "YZZX":1,"ZYZX":1,"ZZYX":1,"ZZZZ":3
    })
    w=polynomial({
        "YZZZZY":1,"ZYZZZY":1,"ZZYYZZ":1,
        "ZZYZZY":2,"ZZZZYY":-1,"ZZZZZX":1,
        "ZYZZ":-1,"ZZYZ":-2,"ZZZY":-2,"ZZ":1
    })
    return g,u,v,w

def main():
    build_to_17()
    piv,positions=build_degree18()
    print("PASS: dim F18 = 1330 mod 101",flush=True)
    d=len(B[17])
    @lru_cache(maxsize=10000)
    def evaluate(word):
        if not word: row={0:1}
        else:
            row={1+word[0]*d+i:c
                 for i,c in word_value(word[1:],17).items()}
        return {positions[i]:c for i,c in canonical(row,piv).items()}

    gens=central_generators()
    unit={():1}
    powers=[]
    for gen,maximum in zip(gens,(6,3,3,3)):
        p=[unit]
        for j in range(maximum):p.append(pol_mul(p[-1],gen))
        powers.append(p)

    monomials=[(i,a,b,c) for i in range(7)
               for a in range(4) for b in range(4) for c in range(4)
               if 3*i+6*(a+b+c)<=18]
    assert len(monomials)==50
    columns=[]
    for k,expo in enumerate(monomials):
        q=unit
        for i,j in enumerate(expo):q=pol_mul(q,powers[i][j])
        vector={}
        for word,c in q.items():addto(vector,evaluate(word),c)
        columns.append(vector)
        print("center monomial",k+1,"/",50,flush=True)

    # Independent columns, sparse modular elimination.
    rank_piv={}
    for v in columns:
        row=dict(v)
        while row:
            k=max(row)
            if k not in rank_piv:
                inv=pow(row[k],-1,P)
                rank_piv[k]={i:c*inv%P for i,c in row.items()}
                break
            addto(row,rank_piv[k],-row[k])
    assert len(rank_piv)==49
    print("PASS: rank of 50 center monomials =49 mod 101",flush=True)

    # Phi=49U^3-(13g^2+14)U^2+(g^2+1)^2U
    #     +(11U-g^2-1)VW+V^3-W^3.
    g,u,v,w=gens
    q=pol_add(pol_scale(powers[1][3],49),
              pol_scale(pol_mul(powers[0][2],powers[1][2]),-13))
    q=pol_add(q,pol_scale(powers[1][2],-14))
    q=pol_add(q,pol_mul(powers[0][4],u))
    q=pol_add(q,pol_scale(pol_mul(powers[0][2],u),2))
    q=pol_add(q,u)
    vw=pol_mul(v,w)
    q=pol_add(q,pol_scale(pol_mul(u,vw),11))
    q=pol_add(q,pol_mul(powers[0][2],vw),-1)
    q=pol_add(q,vw,-1)
    q=pol_add(q,powers[2][3])
    q=pol_add(q,powers[3][3],-1)
    residue={}
    for word,c in q.items():addto(residue,evaluate(word),c)
    assert not residue, ("Phi nonzero modulo 101",len(residue))
    print("PASS: Phi=0 modulo 101",flush=True)
    print("NOTE: This does not prove Phi=0 over Q; exact-Q certificate still needed.")

if __name__=="__main__":
    main()
