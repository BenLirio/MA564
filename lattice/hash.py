import field
import encoding
from math import log, ceil
import numpy as np

Q = 13 # prime
SCALE = 8

def Gen(n):
    m = SCALE*(ceil(log(n, 2))*n)
    s = field.uniform((n,m), Q)
    return s

def H(s, x): return s @ x


if __name__ == '__main__':
    n = 16
    s = Gen(n)
    m = SCALE*(ceil(log(n, 2))*n)
    x = field.array(np.ones((m,1), dtype=int), Q)
    print(H(s, x))
