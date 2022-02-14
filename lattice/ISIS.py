import field
import numpy as np


def solve(A, y, B):
    n = A.shape[0]
    m = A.shape[1]
    base = 2*B + 1
    for i in range(0, pow(base, m)):
        cur = []
        for j in range(0, m):
            cur.append(((i//pow(base, j))%base)-B)
        s = field.array(cur, A.q)
        s = s.reshape((m,1))
        if np.all((A@s - y) == 0):
            print(f"Found solution after {i} trials.")
            return s, True
    return [], False
