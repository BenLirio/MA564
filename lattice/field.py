import numpy as np

class IntArray(np.ndarray):
    def __new__(obj, shape, q):
        obj = super().__new__(obj, shape, dtype=int)
        obj.q = q
        return obj
    def __array_finalize__(self, obj):
        if obj is None: return
        self.q = getattr(obj, 'q', None)
    def __init__(self, q):
        self.q = q
        self[:] %= self.q
    def matmul(self, other):
        if self.q != other.q:
            raise Exception(f"Error: {self} and {other} have a different modulo.")
        return np.matmul(self, other).copy() % self.q
    def multiply(self, other):
        if self.q != other.q:
            raise Exception(f"Error: {self} and {other} have a different modulo.")
        return np.multiply(self, other).copy() % self.q
    def add(self, other):
        if self.q != other.q:
            raise Exception(f"Error: {self} and {other} have a different modulo.")
        return ((self + other).copy()) % self.q
    def sub(self, other):
        if self.q != other.q:
            raise Exception(f"Error: {self} and {other} have a different modulo.")
        return ((self - other).copy()) % self.q
    def inv(self):
        if len(self.shape) == 1 and self.shape[0] == 1:
            a = self.copy()
            a[0] = pow(int(a[0]), -1, self.q)
            return a
        elif len(self.shape) == 2 and self.shape[0] == self.shape[1]:
            A = self.copy()
            n = A.shape[0]
            G = eye(n, A.q)
            for x in range(0, n):
                inv = A[x, x:(x+1)].inv()
                G[x] = G[x].multiply(inv)
                A[x] = A[x].multiply(inv)
                for xp in range(0, n):
                    if x != xp:
                        scale = A[xp,x:(x+1)]
                        A[xp] = A[xp].sub(A[x].multiply(scale))
                        G[xp] = G[xp].sub(G[x].multiply(scale))
                        print(f"A:\n{A}")
                        print(f"G:\n{G}")
            return G
        else:
            raise Exception(f"Error: Shape {self.shape} is not invertable")



def array(data, q):
    A = np.array(data, dtype=int).view(IntArray)
    A.__init__(q)
    return A

def eye(n, q):
    A = np.eye(n, dtype=int).view(IntArray)
    A.__init__(q)
    return A

def uniform(size, q):
    A = np.random.randint(1, q, size=size).view(IntArray)
    A.__init__(q)
    return A

if __name__ == '__main__':
    n = 3
    q = 97
    A = uniform(size=(n, n), q=q)
    print(A.inv())
    print(A.inv().matmul(A))
