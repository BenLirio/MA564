import field
import numpy as np
import linalg
import util

SCALE = 1
Q = 5
B = 1

class LWE:
    def __init__(self, n):
        self.m = SCALE*util.get_m(n,Q)
        self.n = n
        self.A = field.uniform((self.m,self.n), Q)
        self.s = field.uniform((self.n, 1), Q)
        self.e = field.array(np.random.randint(-B, B+1, size=(self.m,1)),Q)
        self.y = self.A@self.s + self.e

if __name__ == '__main__':
    n = 2
    lwe = LWE(n)
    A_perp = linalg.perp(lwe.A)

    b = A_perp@lwe.y
    print(A_perp)
    print(b)



