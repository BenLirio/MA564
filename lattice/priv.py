import field
from random import randint
import numpy as np

Q = 13
B = 1

def Gen(n):
    k = field.uniform((n,1), Q)
    return k

def Enc(k, x):
    a = field.uniform((1,n), Q)
    e = field.array(np.random.randint(-B, B+1, size=(1,1)), Q)
    return (a, a@k + e + x*(Q//2))

def Dec(k, c):
    c0, c1 = c
    if abs(Q//2 - (c1 - c0@k)) > Q//4:
        return 0
    else:
        return 1

if __name__ == '__main__':
    n = 32
    n_tries = 1024
    correct = 0
    for _ in range(0, n_tries):
        k = Gen(n)
        x = field.array([[randint(0, 1)]], Q)
        c = Enc(k, x)
        if Dec(k, c) == x:
            correct += 1
    print(f"{correct/n_tries} ({correct}/{n_tries})")

