import field
import numpy as np
import ISIS
import linalg
import time


trials = 6
for i in range(0,trials):
    n = 5+2*i
    m = 3+i
    q = 97
    B = 1
    print(f"\n==================== Round {i} ====================")
    print(f"n={n}, m={m}, q={q}, B={B}")

    start = time.time()
    print("\nStep 1: Generate a LWE instance")
    lwe_A = field.uniform((n, m), q)
    lwe_s = field.uniform((m,1), q)
    print(f"Secret: {lwe_s.reshape((m))}")
    lwe_e = field.array(np.random.randint(-B, B+1, size=(n,1)),q)
    lwe_y = lwe_A@lwe_s + lwe_e

    print("\nStep 2: Transform into ISIS and solve using ISIS solver")
    isis_A = linalg.perp(lwe_A)
    isis_y = isis_A@lwe_y
    # Solve ISIS using brute force
    isis_s, found = ISIS.solve(isis_A, isis_y, B)
    if not found:
        print("Error: There should be at least 1 solution")
        continue


    print("\nStep 3: Extract LWE solution from ISIS solution")
    print(f"ISIS solution (LWE error): {isis_s.reshape((-1))}")
    lwe_y_prime = (lwe_y - isis_s)[0:m]         # y' has dim(m,1)
    lwe_A_prime = lwe_A[0:m]                    # A' has dim(m,m)

    # taking rref of A||y gives the solution to Ax = y
    tmp = np.concatenate([lwe_A_prime, lwe_y_prime], axis=1).view(field.FieldArray)
    tmp.q = q
    pivots, tmp_rref = linalg.rref(tmp)
    if len(pivots) != m:
        print("Error: Not enough pivots.")
        continue
    # The solution column of the rref matrix
    lwe_solution = tmp_rref[:,m].reshape((m,1))
    if np.all(lwe_solution == lwe_s):
        end = time.time()
        print(f"LWE solution: {lwe_solution.reshape((m))}")
        print("Time: {:.2f} seconds".format(end-start))
    else:
        print("Error: solution does not match secret.")
