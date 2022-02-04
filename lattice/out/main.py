import field
import numpy as np

n = 2
m = 5
q = 7
B = 1

print("Ben Lirio")

A = field.uniform((n,m), q)
print(f"\nLet 'A' be a uniform ({n}, {m}) matrix in Z_{q}")
print(A)

s = field.uniform((n,1), q)
print(f"\nLet 's' be a uniform ({n}) vector in Z_{q}")
print(s)


e = field.array(np.random.randint(-B, B+1, size=(1,m)), q)
print(f"\nLet 'e' be a ({m}) vector s.t. |e| <= {B}")
print(e)

b0 = s.T @ A + e
print(f"\nLet 'B_0' be computed as s.T * A + e")
print(b0)

b1 = field.uniform((1,m), q)
print(f"\nLet 'B_1' be a uniform ({m}) vector in Z_{q}")
print(b1)


print("\nInstance 0: (A, B_0)")
print("Instance 1: (A, B_1)")
