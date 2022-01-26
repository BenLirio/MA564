import numpy as np

n = 3
m = 10
A = np.random.randint(0, m, size=(n,m), dtype=int)

class Omega():
    def __init__(self, m):
        self.cur = 0
        self.bits = np.zeros((m), dtype=int)
    def __iter__(self):
        return self
    def __next__(self):
        return self.next()
    def next(self):
        self.cur += 1
        if self.cur < 1<<m:
            bits = list(np.binary_repr(self.cur, width=m))
            bits = np.array([ int(bit) for bit in bits ], dtype=int)
            self.bits = bits
            return bits
        else:
            raise StopIteration()

omega = Omega(m)
print(A)
for x in omega:
    res = np.mod(np.matmul(A, x), m)
    if np.sum(res) == 0:
        print(x)
