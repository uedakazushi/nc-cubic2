#!/usr/bin/env python3
"""Exact Ext^1 ranks for all eight 3-dimensional simples at g=0.

Requires SymPy. Reuses and verifies the representations in the companion
script. All ranks are over QQ[t]/q or QQ[w]/(w^2+w+1), not floating point
or finite fields. The sign involution exchanges the two simples at each
point; cubic root symmetry permutes the three nonaxial central points.
Different central characters have zero Ext by the central action.
"""
import sympy as sp
from sympy.polys.matrices import DomainMatrix
import verify_central_quotient_reps as reps


def verify_pair(matrices, variable, polynomial, name):
    theta = sp.CRootOf(polynomial, 0)  # exact algebraic root, no approximation
    field = sp.QQ.algebraic_field(theta)

    def over_field(rows):
        data = [[field.new([sp.QQ.convert(c) for c in sp.Poly(
            reps.mod(entry, variable, polynomial), variable,
            domain=sp.QQ).all_coeffs()]) for entry in row] for row in rows]
        return DomainMatrix(data, (len(data), len(data[0])), field)

    for sign, expected in [(1, (19, 19, 8, 0)), (-1, (16, 16, 9, 2))]:
        x, y, z = matrices
        tx, ty, tz = [sign*a for a in matrices]
        columns, central_columns = [], []
        # An upper triangular extension has off-diagonal blocks a,b,c.
        for k in range(27):
            a, b, c = [sp.zeros(3) for _ in range(3)]
            owner = k//9
            row, col = divmod(k % 9, 3)
            (a, b, c)[owner][row, col] = 1
            relations = [
                x*b+a*ty-y*a-b*tx-z*c-c*tz,
                y*c+b*tz-z*b-c*ty-x*a-a*tx,
                z*a+c*tx-x*c-a*tz-y*b-b*ty,
            ]
            columns.append([entry for mat in relations for entry in mat])
            central_columns.append(list(
                y**2*b+y*b*ty+b*ty**2-z*y*a-z*b*tx-c*ty*tx+a))
        rows = list(map(list, zip(*columns)))
        jacobian = over_field(rows)
        central_jacobian = over_field(
            rows+list(map(list, zip(*central_columns))))
        inner_columns = []
        for k in range(9):
            h = sp.zeros(3)
            h[k//3, k % 3] = 1
            inner_columns.append([entry for mat in
                (x*h-h*tx, y*h-h*ty, z*h-h*tz) for entry in mat])
        inner = over_field(list(map(list, zip(*inner_columns))))
        assert jacobian.matmul(inner).is_zero_matrix
        assert central_jacobian.matmul(inner).is_zero_matrix
        rank, central_rank, inner_rank = (
            jacobian.rank(), central_jacobian.rank(), inner.rank())
        ext = 27-rank-inner_rank
        assert (rank, central_rank, inner_rank, ext) == expected
        assert 27-central_rank-inner_rank == ext
        print(f"PASS exact {name}, sign={sign}: ranks "
              f"J={rank}, (J,dg)={central_rank}, inner={inner_rank}; Ext1={ext}",
              flush=True)


def main():
    verify_pair((reps.X, reps.Y, reps.Z), reps.t, reps.q, "axial")
    verify_pair((reps.X0, reps.Y0, reps.Z0), reps.w,
                reps.w**2+reps.w+1, "nonaxial")
    print("PASS: Ext1 table at all four central points, in R1 and R1/(g)")


if __name__ == "__main__":
    main()
