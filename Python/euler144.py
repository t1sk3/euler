# 4x^2 + y^2 = 100
# -(4x/sqrt(100 - 4x^2))

from math import *
import sympy

def returnSlope(x, y):
    #f = 4*x**2 + y**2 = 100
    dy = -4*x/y
    return dy

def solveEquations(f1):

    x, y = sympy.symbols("x y", real=True)

    eq1 = sympy.Eq(4*x**2 + y**2, 100)
    eq2 = f1
    return sympy.solve([eq1, eq2])

def makeEquation(x1, y1, m):
    x, y = sympy.symbols("x y", real=True)

    #m = ((y2 - y1)/(x2 - x1))
    q = y1 - m * x1 

    eq = sympy.Eq(m * x - y, -q)
    return eq

def tangentSlope(dy):
    return 1/dy * -1

def makeAngle(dy):
    theta = atan(dy)
    return degrees(theta)

def makeRico(theta):
    dy = tan(radians(theta))
    return dy

def returnMirror(m, mirror):
    mAngle = makeAngle(m)
    mirrorAngle = makeAngle(mirror)
    diff = mirrorAngle - mAngle
    resAngle = mirrorAngle -180 + diff
    if resAngle > 90:
        resAngle -= 180
    elif resAngle < -90:
        resAngle += 180
    return makeRico(resAngle)

def getNewCo(sol, x, y):
    what = True
    for solution in sol:
        for co in solution:
            #if not x - 0.1 < solution[co] < x + 0.1 and not y - 0.1 < solution[co] < y + 0.1:
            if what:
                x1 = solution[co]
                what = False
            else:
                y1 = solution[co]
    return x1, y1


def compute():
    x1, y1 = 0, 10.1
    x2, y2 = 1.4, -9.6
    m = ((y2 - y1)/(x2 - x1))
    counter = 1
    while True:
        counter += 1
        mirror = returnSlope(x2, y2)
        m = returnMirror(m, mirror)
        sol = solveEquations(makeEquation(x2, y2, m))
        x1, y1 = x2, y2
        x2, y2 = getNewCo(sol, x2, y2)
        if -0.1 < x2 < 0.1 and 9.9 < y2 < 10.1:
            return counter

print(compute())