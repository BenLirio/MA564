import numpy as np

class FieldArray(np.ndarray):
    def __new__(obj, shape, q):
        print(super())
        obj = super().__new__(obj, shape, dtype=int)
        obj.q = q
        return obj
    def __array_finalize__(self, obj):
        if obj is None: return
        self.q = getattr(obj, 'q', None)
    def __init__(self, q):
        self.q = q
        self[:] %= self.q
    def check_modulo(self, other):
        if hasattr(other, 'q'):
            if self.q != other.q:
                raise Exception(f"Error: {self} and {other} have a different modulo.")
    def __matmul__(self, other):
        self.check_modulo(other)
        return super().__matmul__(other) % self.q

    def __mul__(self, other):
        self.check_modulo(other)
        return super().__mul__(other) % self.q
    def __imul__(self, other):
        self.check_modulo(other)
        return super().__imul__(other) % self.q
    def __neg__(self):
        return super().__neg__() % self.q

    def __setitem__(self, key, value):
        super().__setitem__(key,value % self.q)


    def __add__(self, other):
        self.check_modulo(other)
        return super().__add__(other) % self.q
    def __iadd__(self, other):
        self.check_modulo(other)
        return super().__iadd__(other) % self.q

    def __truediv__(self, other):
        self.check_modulo(other)
        if not hasattr(other, 'q'):
            return self.__mul__(pow(int(other), -1, self.q))
        else:
            return self.__mul__(~other)

    def __floordiv__(self, other):
        return self.__truediv__(other)

    def __sub__(self, other):
        self.check_modulo(other)
        return super().__sub__(other) % self.q
    def __isub__(self, other):
        self.check_modulo(other)
        return super().__isub__(other) % self.q

    def __invert__(self):
        f = np.vectorize(lambda x: pow(int(x), -1, self.q))
        return f(self)

def array(data, q):
    A = np.array(data, dtype=int).view(FieldArray)
    A.__init__(q)
    return A

def eye(n, q):
    A = np.eye(n, dtype=int).view(FieldArray)
    A.__init__(q)
    return A

def uniform(size, q):
    A = np.random.randint(1, q, size=size).view(FieldArray)
    A.__init__(q)
    return A


if __name__ == '__main__':
    n = 2
    p = 7
    a = uniform((n,1), p)
    s = uniform((n,1), p)
    e = np.random.randint(0,2,size=(1,1)).view(FieldArray)
    e.__init__(p)
    print("a:", a.T)
    print("s:", s.T)
    print("e:", e)
    print("b:", a.T @ s + e)
