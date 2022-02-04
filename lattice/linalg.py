import field


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

def row_space(A):
    A = A.copy()

    # Base Case
    if A.shape[0] == 0 or A.shape[1] == 0:
        return 0

    # Inductive Case
    nrows = A.shape[0]

    # Swap rows s.t. A[0,0] != 0
    for i in range(0, nrows):
        if A[i,0] != 0:
            A[0], A[i] = A[i], A[0]
            break

    # Col is degenerate
    if A[0,0] == 0:
        return row_space(A[:,1:])

    # Normalize pivot row
    A[0] = A[0]/A[0,0]

    # Eliminate values in Col
    for i in range(1, nrows):
        A[i] = A[i] - (A[0]*A[i,0])

    # Recurse
    return 1 + row_space(A[1:,1:])

col_space = lambda A: row_space(A)
null_space = lambda A: A.space[0] - col_space(A)
left_null_space = lambda A: A.shape[1] - row_space(A)

if __name__ == '__main__':
    n = 2
    m = 4
    q = 13
    A = field.uniform((n,m), q)
    #A = field.array([[1,2,3],[2,4,6],[4,8,12],[1,2,3],[1,2,3]], q)
    A = field.array([
        [1, 2, 3],
        [2, 8, 5],
        [3,2,3],
        ], q)
    print(A)
