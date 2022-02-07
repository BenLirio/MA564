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

def perp(A):
    pivots, A = rref(A.T)
    pivot_cols = set([ c for r,c in pivots ])
    null_cols = set(range(0,A.shape[1])) - pivot_cols

    P = field.array(np.zeros((len(null_cols), A.shape[1])), A.q)
    i = 0
    for c in null_cols:
        P[i,c] = 1
        for rp, cp in pivots:
            if A[rp,c] == 0: continue
            P[i,cp] = -A[rp,c]
        i += 1
    return P

def rref(A):
    A = A.copy()
    cr = 0
    cc = 0
    pivots = []
    swaps = []
    while True:
        if cr >= A.shape[0] or cc >= A.shape[1]:
            break
        for i in range(cr, A.shape[0]):
            if A[i,cc] != 0:
                A[cr,:], A[i,:] = A[i,:], A[cr,:]
                break
        if A[cr,cc] == 0:
            cc += 1
            continue
        pivots.append((cr,cc))
        A[cr] = A[cr]/A[cr,cc]
        for i in range(0, A.shape[0]):
            if cr == i: continue
            A[i] = A[i] - A[cr]*A[i,cc]
        cr += 1
        cc += 1
    return pivots, A


if __name__ == '__main__':
    n = 6
    m = 3
    q = 7
    while True:
        A = field.uniform((n, m), q)
        r = len(rref(A)[0])
        if r == min(n, m): continue
        print(A)
        print(f"A: ({n}, {m})")
        print(f"C(A): ({n}, {r})")
        print(f"C(At): ({m}, {r})")
        print(f"N(A): ({m}, {m-r})")
        print(f"N(At): ({n}, {n-r})")
        break
