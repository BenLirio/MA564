import field
import linalg
import numpy as np
# N is dim
# Q is modulo
# B is basis [ N x N ]
N = 3
Q = 103
B = field.uniform((N,N),Q)


# P(B) is fundemental region

# [ N x N ] [ N ]       [0,1)c1 + [0,1)c2 + ... + [0,1)cn
X = B @ np.random.random((N))
# x <- Guass in [ N ]
# v := x mod P(B)
V = X
# a := B-inv v
A = linalg.inv(B) @ V
print(A)
# 
# M is large enough
# A := B_inv V in [ N x M ]
# 
# x := SIS_oracle on A
# x in [ M ]
# 
#   B_inv       V       x   is in Z
# [ N x N ] [ N x M ] [ M ]
# 
#  Multiply both sides by B
# 
#     V       x   in B
# [ N x M ] [ M ]
# 
# X <=> V mod P(B)
# 
# Therefore V in B
# 
#     X       x
# [ N x M ] [ M ]
# 
# 
# How short is |Xx| ?
