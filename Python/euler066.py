from math import *

def compute():
    d = 2
    lstd = []
    lstx = []
    while d <= 1000:
        if not checkSquare(d):
            print(d)
            lstd.append(d)
            lstx.append(findX(d))
        d += 1
    return lstd[lstx.index(max(lstx))]

def checkSquare(x):
    if sqrt(x).is_integer():
        return True
    else:
        return False

def findX(d):
    i = 1
    while True:
        j = 1
        while j < i:
            if i**2 - d*(j**2) == 1:
                return i
            else:
                j += 1
        i += 1

print(compute())
#print(checkSquare(3))