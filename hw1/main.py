import numpy as np

inv = lambda x, q: pow(int(x), -1, q)

class VectorGenerator():
    def __init__(self, n, q):
        self.n = n
        self.q = q
    def __iter__(self):
        self.vec = np.zeros((self.n), dtype=int)
        return self
    def __next__(self):
        valid = False
        for i in range(0, self.n):
            self.vec[i] = (self.vec[i] + 1)%self.q
            if self.vec[i] != 0:
                valid = True
                break
        if not valid:
            raise StopIteration
        return self.vec

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
            res = self * MatOverField(x, self.q)
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
        return MatOverField(out, Arref.q).T()

rand_mat = lambda n, m, q: MatOverField(np.random.randint(0, q, size=(n, m)), q)

print("HW1")
print("Name: Ben Lirio")

while True:
    q = 11
    n = 3
    m = 5
    A = rand_mat(n, m, q)
    binary_solutions = A.find_binary_solutions()
    if len(binary_solutions) > 0:
        print("\n\n========== Problem 1 ==========")
        print("Matrix:")
        print(A)
        print("\nSolution(s):")
        print(binary_solutions)
        break

while True:
    q = 11
    n = 2
    m = 4
    A = rand_mat(n, m, q)
    binary_solutions = A.find_binary_solutions()
    if len(binary_solutions) == 0:
        print("\n\n========== Problem 2 ==========")
        print("Matrix:")
        print(A)
        print("\nBrute force 4^2 trials failed")
        break

while True:
    q = 97
    n = 5
    m = 10
    A = rand_mat(n, m, q)
    try:
        A_null = A.generate_null()
        print("\n\n========== Problem 3 ==========")
        print(f"Matrix {n} x {m} over Z_{q}:")
        print(A)
        print(f"\nThese are all the solutions:")
        print(A_null)
        print("Run time: O(m*n^2)")
        print("Explaination: Each column of the solution matrix is in the null space of A")
        print("This works because for all y in Z, there exists an x such that 'y = |x| < q/2 (mod q)'.")
        print("Therefore there is no restriction on the vector 'x' (mod q)")
        break
    except:
        pass
