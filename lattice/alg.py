import util
import secrets
import field
import numpy as np

SCALE = 1
Q = 5
B = 1

class LWEGenerator:
    def __init__(self, n):
        self.num_queries = 0
        self.m = SCALE*util.get_m(n,Q)
        self.n = n
        self._s = field.uniform((self.n, 1), Q)

    def __iter__(self):
        return self

    def __next__(self):
        if self.num_queries >= self.m: raise StopIteration()
        a = field.uniform((self.n, 1), Q)
        e = secrets.randbelow(2*B + 1) - B
        b = a.T @ self._s + e
        self.num_queries += 1
        return a, b

# Arora-Ge
# New Algorithms for Learning in Presence of Errors

class Solver:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def guess(self, s):
        acc = field.array([[1]], Q)
        for x in range(-B,B+1):
            acc = acc * (self.b - self.a.T@s + x)
        return acc[0,0] == 0



if __name__ == '__main__':
    n = 3
    lwe_gen = LWEGenerator(n)
    for (a,b) in lwe_gen:
        solver = Solver(a,b)
