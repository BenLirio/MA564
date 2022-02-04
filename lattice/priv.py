import field
import numpy as np

Q = 13
B = 1

def Gen(n):
    k = field.uniform((n,1), Q)
    return k

def Enc(k, m):
    a = field.uniform((1,n), Q)
    e = field.array(np.random.randint(-B, B+1, size=(1,1)), Q)
    return (a, a@k + e + m*(Q//4))

def Dec(k, c):
    c0, c1 = c
    if abs(Q//2 - (c1 - c0@k)) > Q//4:
        return 0
    else:
        return 1

if __name__ == '__main__':
    n = 16
    k = Gen(n)
    m = 0
    c = Enc(k, m)
    if Dec(k, c) != m:
        print("Incorrect")
    else:
        print("Correct")

