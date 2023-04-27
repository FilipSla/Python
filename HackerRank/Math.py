import math
import numpy

a = int(input())
b = int(input())


### Mod Divmod
def myFunction(a, b):
    # vrací tuple(x//y, x%y)
    c = divmod(a, b)
    return print(c[0], c[1], c, sep="\n")


myFunction(a, b)

### Power - Mod Power
a = int(input())
b = int(input())
m = int(input())


def modPower(a, b, m):
    return print(pow(a, b), pow(a, b, m), sep="\n")


modPower(a, b, m)

### Integers Come In All Sizes
a = int(input())
b = int(input())
c = int(input())
d = int(input())


def bigCalculation(a, b, c, d):
    return pow(a, b) + pow(c, d)


print(bigCalculation(a, b, c, d))


### Triangle Quest
ab = int(input())
bc = int(input())
def calculateAngle(ab, bc):
    ac = pow(pow(ab, 2) + pow(bc, 2), 0.5)
    return round(math.atan(ab/ac)*(180/math.pi))
result = print(calculateAngle(ab,bc))