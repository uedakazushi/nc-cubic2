#!/usr/bin/env python3
"""Integer checks for Poisson-pair component dimensions; not a proof of the normal form."""
from math import comb

def dim(N, k):
    m = N - 3 * k
    assert N >= 5 and k >= 1 and m >= 0
    cubic = comb(m + 2, 3) + k * (10 + 6 * m + 3 * comb(m + 1, 2))
    orbit = k * (3 * N - 8)
    incidence = orbit + cubic - 1
    quotient = incidence - (N * N - 1)
    return incidence, quotient

for n in range(3, 21):
    N = n + 2
    vals = [dim(N, k) for k in range(1, N // 3 + 1)]
    assert len(vals) == N // 3
    for k in range(1, N // 3):
        difference = vals[k-1][0] - vals[k][0]
        assert difference == 3 * (3*k-1) * (N-3*k) + 8 > 0
    print(f"n={n}: components={len(vals)}, dimensions=" +
          ",".join(str(value[1]) for value in vals))
expected = {
    3:[17],4:[30,4],5:[48,16],6:[72,34],
    7:[103,59,6],8:[142,92,24],9:[190,134,51],
    10:[248,186,88,8]
}
for n, values in expected.items():
    assert [dim(n + 2,k)[1] for k in range(1,(n+2)//3+1)] == values
print("PASS: all formulas and recurrence checks")
