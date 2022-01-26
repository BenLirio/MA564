import numpy as np
import time

q = 5

def push_row_to_bottom(A, x):
    return np.concatenate((A[:x], A[x+1:], A[x:x+1]))

matmul = lambda A, B: np.mod(np.matmul(A, B),q)
def inv(a, q):
    if a == 0:
        raise "divide by zero"
    for i in range(0, q):
        if (i*a)%q == 1:
            return i
    print(a, q)
    raise "Should not get here"


def rref(A):
    A = A.copy()
    rows = A.shape[0]
    for x in range(0, rows):
        rows_tried = 1
        while rows_tried <= (rows-x) and A[x,x] == 0:
            A = push_row_to_bottom(A, x)
            rows_tried += 1
        if A[x,x] == 0:
            continue
        A[x] = A[x] * inv(A[x,x], q)
        for y in range(0, rows):
            if x == y:
                continue
            A[y] = (A[y] - A[y,x]*A[x])%q
    return A
def generate_null(A):
    out = []
    Arref = rref(A)
    for col_idx in range(A.shape[0], A.shape[1]):
        col = np.zeros((A.shape[1]), dtype=int)
        for row_idx in range(0, A.shape[0]):
            col[row_idx] = -Arref[row_idx, col_idx]
        col[col_idx] = 1
        out.append(col)
    return np.mod(out, q).T
A = np.random.randint(1, q, size=(100,200), dtype=int)

A_null = generate_null(A)
print(A_null)
