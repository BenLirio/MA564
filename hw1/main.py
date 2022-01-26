import numpy as np
import sympy

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

class SIS():
    def __init__(self, n, m, q, seed=None):
        self.seed = seed
        if self.seed:
            np.random.seed(self.seed)
        self.n = n
        self.m = m
        self.q = q
        self.A = np.random.randint(0, high=self.q, size=(n,m), dtype=int)
    def find_binary_solution(self):
        # O(2^n)
        X = VectorGenerator(self.m, 2)
        for x in X:
            res = np.mod(np.matmul(self.A, x), self.q)
            if np.sum(res) == 0:
                return x
        return []
    def find_solution(self):
        return sympy.Matrix(self.A).nullspace()

N = 100
while N:
    break
    sis = SIS(3, 5, 11)
    solution = sis.find_binary_solution()
    if not any(solution):
        continue
    print(sis.A)
    print(solution)
    break

sis = SIS(3, 5, 11)
res =sis.find_solution()

