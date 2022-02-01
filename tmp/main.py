import numpy as np

class C(np.ndarray):
    def __new__(cls, shape, q):
        obj = super().__new__(cls, shape)
        obj.q = q
        return obj


A = C(3, 7)
print(np.ndarray(3))

print(A.q)
print(A)
