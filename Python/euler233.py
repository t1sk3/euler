import sympy
from math import *

def f(N):
    points = []

    r = sqrt((N/2)**2 * 2)
    print(r)

    for x in range(0, N+1):
        if x % 1000 == 0:
            print(x)
        for y in range(0, N+1):
            if r**2 - 1 < (x - N/2)**2 + (y - N/2)**2 < r**2 + 1:
                print(x,y)
                points.append([x, y])
    return len(points)

print(f(10000))