import numpy as np

inv = lambda x, q: pow(int(x), -1, q)


class MatOverField():
    def __init__(self, data, q):
        self.q = q
        self.data = np.mod(np.array(data, dtype=int), q)
        self.shape = self.data.shape
    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, val):
        self.data[key] = val
        self.data[key] = np.mod(self.data[key], self.q)
    def copy(self):
        return MatOverField(self.data.copy(), self.q)
    def T(self):
        return MatOverField(self.data.T, self.q)
    def push_row_to_bottom(self, x):
        self.data = np.concatenate((self.data[:x], self.data[x+1:], self.data[x:x+1]))
    def __mul__(self, other):
        if self.q != other.q:
            raise f"Field size {self.q} does not match {other.q}"
        return np.mod(np.matmul(self.data, other.data), self.q)
    def __str__(self):
        return f"{self.data}"

def rref(A):
    A = A.copy()
    rows = A.shape[0]
    for x in range(0, rows):
        rows_tried = 1
        while rows_tried <= (rows-x) and A[x,x] == 0:
            A.push_row_to_bottom(x)
            rows_tried += 1
        if A[x,x] == 0:
            continue
        A[x] = A[x] * inv(A[x,x], A.q)
        for y in range(0, rows):
            if x == y:
                continue
            A[y] = (A[y] - A[y,x]*A[x])%A.q
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
    return MatOverField(out, A.q).T()
while True:
    q = 5
    A = MatOverField(np.random.randint(0,5, size=(100,200)), q)
    A_null = generate_null(A)
    print(A*A_null)
