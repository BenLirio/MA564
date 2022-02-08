from random import randint
import numpy as np
import field
import util
Q = 593
B = 1

def Gen(n):
    m = util.get_m(n, Q)
    A = field.uniform((m,n), Q)
    sk = field.uniform((n,1), Q)
    e = field.array(np.random.randint(-B, B+1, size=(m,1)),Q)
    pk = (A, A@sk + e)
    return pk,sk

def Enc(pk, x):
    A, v = pk
    m = A.shape[0]
    r = field.array(np.random.randint(0, 2, size=(m,1)),Q)
    return (r.T @ A, r.T @ v + x*(Q//2))

def Dec(sk, c):
    c0, c1 = c
    if abs(Q//2 - abs(c1 - c0@sk)) < Q//4:
        return field.array([[1]], Q)
    else:
        return field.array([[0]], Q)

if __name__ == '__main__':
    n = 32
    print(util.get_m(n,Q)*B, Q//4)
    n_tries = 1000
    correct = 0
    for _ in range(0, n_tries):
        pk, sk = Gen(n)
        x = field.array([[randint(0,1)]], Q)
        c = Enc(pk, x)
        if Dec(sk, c)[0][0] == x[0][0]:
            correct += 1
    print(f"{correct/n_tries} ({correct}/{n_tries})")
