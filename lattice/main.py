import field
import numpy as np

class SIS:
    def __init__(self, n, m, q, B, hom=False):
        self.n = n
        self.m = m
        self.q = q
        self.B = B
        self.hom = hom
        self.A = field.uniform(size=(self.n, self.m), q=self.q)
        if self.hom:
            self.b = field.array(np.zeros((self.n,1)), q=self.q)
        else:
            self.b = field.uniform(size=(self.n, 1), q=self.q)

class LWE:
    def __init__(self, n, m, q, B):
        self.n = n
        self.m = m
        self.q = q
        self.s = field.uniform(size=(self.n,1), q=self.q)
        self.A = field.uniform(size=(self.n, self.m), q=self.q)
        e = np.random.randint(-B, B+1, size=(self.m, 1))
        self.e = field.array(e, q=self.q)
        self.y = self.A.T.mul(self.s).add(self.e)
    def reduce_to_SIS(self):
        pass
    def solve(self):
        self.recude_to_SIS()

n = 5
m = 10
q = 13
B = q//4
lwe = LWE(n, m, q, B)
print(lwe.A)
