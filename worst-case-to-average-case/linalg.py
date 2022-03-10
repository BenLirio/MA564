import field
import numpy as np

is_square = lambda A: not (len(A.shape) != 2 or A.shape[0] != A.shape[1])

def inv(A):
    if not is_square(A):
        raise "Can only invert square matricies"
    A = A.copy()
    n = A.shape[0]
    Ap = field.eye(n, A.q)
    for i in range(0, n):
        pivot = A[i,i]
        A[i] = A[i]/pivot
        Ap[i] = Ap[i]/pivot
        for j in range(0, n):
            if j == i: continue
            scale = A[j,i]
            A[j] = A[j] - A[i]*scale
            Ap[j] = Ap[j] - Ap[i]*scale
    return Ap

def rref(A):
    A = A.copy()
    cr = 0
    cc = 0
    pivots = set()
    swaps = set()
    while True:
        if cr >= A.shape[0] or cc >= A.shape[1]:
            break
        for i in range(cr, A.shape[0]):
            if A[i,cc] != 0:
                t1 = A[cr].copy()
                A[cr] = A[i]
                A[i] = t1
                break
        if A[cr,cc] == 0:
            cc += 1
            continue
        pivots.add((cr,cc))
        A[cr] = A[cr]/A[cr,cc]
        for i in range(0, A.shape[0]):
            if cr == i: continue
            A[i] = A[i] - A[cr]*A[i,cc]
        cr += 1
        cc += 1
    return pivots, A

def null_space(A):
    pivots, A = rref(A)
    rank = len(pivots)
    n,m = A.shape[0],A.shape[1]
    dim = (m, m-rank)
    A_null = field.array(np.zeros(dim), A.q)
    pivot_rows = set([a for a,_ in pivots])
    pivot_cols = set([b for _,b in pivots])
    col_of_row = {a:b for a,b in pivots}

    A_null_col_idx = 0
    for A_col_idx in range(0,m):
        if A_col_idx in pivot_cols: continue
        for A_row_idx in range(0,n):
            if A_row_idx in pivot_rows:
                A_null[col_of_row[A_row_idx], A_null_col_idx] = -A[A_row_idx,A_col_idx]
        A_null[A_col_idx,A_null_col_idx] = 1
        A_null_col_idx += 1
    return A_null

def perp(A): return null_space(A.T).T


if __name__ == '__main__':
    n = 10
    m = 5
    q = 97
    A = field.array([[1,1,1,1],[1,1,1,1],[2,3,4,5]], q)
    A = field.uniform((n, m), q)
    print(A)
    print(perp(A))
    print(perp(A)@A)
