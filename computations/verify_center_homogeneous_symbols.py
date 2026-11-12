#!/usr/bin/env python3
"""Exact-Q degree-six leading symbols in gr R1 = S1.

Checks that gr(g²),gr(U),gr(V),gr(W) are independent in (S1)_6.
S1 has homogeneous relations XY-YX-Z², YZ-ZY-X², ZX-XZ-Y².
Use with verify_center_degree7.py and the known Sklyanin
center-generation theorem to prove gr Z(R1)=Z(S1).
"""
from itertools import product
from verify_center_degree7 import (
    Q, WORDS, INDEX, mul, wordpoly, add, reduce_row, canonical
)

def main():
    relation = (
        {(0, 1): 1, (1, 0): -1, (2, 2): -1},
        {(1, 2): 1, (2, 1): -1, (0, 0): -1},
        {(2, 0): 1, (0, 2): -1, (1, 1): -1},
    )
    piv = {}
    for m in range(5):
        for j in range(m+1):
            for prefix in product(range(3), repeat=j):
                for suffix in product(range(3), repeat=m-j):
                    for rel in relation:
                        row = {}
                        for w, c in rel.items():
                            i=INDEX[prefix+w+suffix]
                            row[i]=row.get(i,0)+c
                        reduce_row(row, piv, insert=True)
    f6 = [i for i,w in enumerate(WORDS) if len(w)<=6 and i not in piv]
    assert len(f6)==84
    g = wordpoly({"YYY":1, "ZYX":-1, "X":1})
    u = mul(wordpoly({"ZZZ":1}),add(g,wordpoly({"ZZZ":-1})))
    v = wordpoly({
        "YZZYYY":1, "ZYZZYX":-1, "ZYZZZZ":-1,
        "ZZYYZX":2, "ZZYZZZ":1, "ZZZYZZ":-3,
        "YZZX":1, "ZYZX":1, "ZZYX":1, "ZZZZ":3
    })
    w = wordpoly({
        "YZZZZY":1, "ZYZZZY":1, "ZZYYZZ":1,
        "ZZYZZY":2, "ZZZZYY":-1, "ZZZZZX":1,
        "ZYZZ":-1, "ZZYZ":-2, "ZZZY":-2, "ZZ":1
    })
    pivot={}
    for p in (mul(g,g),u,v,w):
        lead={i:c for i,c in p.items() if len(WORDS[i])==6}
        row=canonical(lead,piv)
        assert reduce_row(row,pivot,insert=True)
    assert len(pivot)==4
    print("PASS Q: (S1)_6 has four independent leading symbols gr(g²),gr(U),gr(V),gr(W)")

if __name__=="__main__":
    main()
