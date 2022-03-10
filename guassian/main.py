from math import pi, e

p = lambda s: lambda c: lambda x: pow(e,-pi*pow((x-c)/s, 2))

s = 3
n = 1
p = p(s)(0)

span = 10
N = 100

N = (N//2)*2
points = [ p((span*x)/N)/pow(s,n) for x in range(-N//2,N//2) ]
integral = span*sum(points)/N
print(integral)
