import numpy as np

class Int():
    def __init__(self):
        pass

class Mat():
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
        return Mat(self.data.copy(), self.q)
    
    def T(self):
        return Mat(self.data.T, self.q)

    def push_row_to_bottom(self, x):
        self.data = np.concatenate((self.data[:x], self.data[x+1:], self.data[x:x+1]))
    def __mul__(self, other):
        if self.q != other.q:
            raise f"Field size {self.q} does not match {other.q}"
        return np.mod(np.matmul(self.data, other.data), self.q)

    def __str__(self):
        return f"{self.data}"
    def rref(self):
        A = self.copy()
        num_rows = A.shape[0]
        col_idx = 0
        row_idx = 0
        while row_idx < num_rows and col_idx < num_rows:
            pivot_value = A[row_idx, col_idx]
            num_pivots_tried = 1
            max_tries = num_rows - row_idx
            while pivot_value == 0 and num_pivots_tried <= max_tries:
                A.push_row_to_bottom(row_idx)
                num_pivots_tried += 1
                pivot_value = A[row_idx, col_idx]
            if pivot_value != 0:
                A[row_idx] = A[row_idx] * inv(A[row_idx,col_idx], A.q)
                for row_idx_prime in range(0, num_rows):
                    if row_idx_prime != row_idx:
                        A[row_idx_prime] = (A[row_idx_prime] - A[row_idx_prime, col_idx]*A[row_idx]) % A.q
                row_idx += 1
            else:
                raise "Not enough pivot rows (Swapping Columns not implemented)"
            col_idx += 1
        return A

    def find_binary_solutions(self):
        # O(2^n)
        X = VectorGenerator(self.shape[1], 2)
        for x in X:
            res = self * Mat(x, self.q)
            if np.sum(res) == 0:
                return x
        return []

    def generate_null(self):
        out = []
        Arref = self.rref()
        num_rows = Arref.shape[0]
        num_cols = Arref.shape[1]
        for col_idx in range(num_rows, num_cols):
            col = np.zeros((num_cols), dtype=int)
            for row_idx in range(0, num_rows):
                col[row_idx] = -Arref[row_idx, col_idx]
            col[col_idx] = 1
            out.append(col)
        return Mat(out, Arref.q).T()
