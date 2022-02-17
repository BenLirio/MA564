from random import randint
import math

q = 809
bound = q/4

def dist():
    low = -101
    hi = math.ceil(2*bound + 1) + low
    return randint(low, hi)

class Secret():
    def __init__(self, n):
        self.s = n
    def approx(self):
        a = self.s + dist()
        return a
    def add(self,v):
        self.s += v
    def mult(self):
        self.s *= 2

secret = randint(0,q)
s = Secret(secret)

while True:
    cmd = input("> ").split(" ")
    if cmd[0] == "app":
        print(s.approx())
    if cmd[0] == "add":
        val = float(cmd[1])
        s.add(val)
        print(f"Added: {val}")
    if cmd[0] == "mult":
        s.mult()
        print("Mult by 2")
    if cmd[0] == "done":
        print(f"Actual: {secret}")
        break
