import field
import numpy as np
import linalg
import util

SCALE = 1
Q = 5
B = 1

class FieldArrayGenerator(field.FieldArray):
    def __iter__(self):
        return self
    def __next__(self):
        last = lambda x: x == 1
        _next = lambda x: {0:(-1%self.q),(-1%self.q):1}[x]
        first = 0
        n = self.shape[0]
        incremented = False
        for i in range(0,n):
            a = self[i,0]
            if last(a):
                self[i,0] = first
                continue
            self[i] = _next(a)
            incremented = True
            break
        if not incremented:
            raise StopIteration()
        return self

#class Omega():
#    def __init__(self, m):
#        self.cur = 0
#        self.bits = np.zeros((m), dtype=int)
#    def __iter__(self):
#        return self
#    def __next__(self):
#        return self.next()
#    def next(self):
#        self.cur += 1
#        if self.cur < 1<<m:
#            bits = list(np.binary_repr(self.cur, width=m))
#            bits = np.array([ int(bit) for bit in bits ], dtype=int)
#            self.bits = bits
#            return bits
#        else:
#            raise StopIteration()

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
    e = field.array(np.zeros((lwe.m,1)), Q)
    e = e.view(FieldArrayGenerator)

    b = A_perp@lwe.y
    possible_es = []
    for _ in e:
        if (A_perp@e == b).all():
            possible_es.append(e.copy())

    print(len(possible_es))
    lwe.y - e
