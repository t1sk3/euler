from math import *

def getDistance(x1, y1, x2, y2):
    distance = sqrt((x1-x2)**2 + (y1-y2)**2)
    return distance

def checkRight(a,b,c):
    if int(a**2) == int(b**2 + c**2) or int(b**2) == int(a**2 + c**2) or int(c**2) == int(a**2 + b**2):
        return True
    return False

def compute():
    counter = 0
    used = []
    for i in range(0,51):
        for j in range(0,51):
            if i == j == 0:
                continue
            for k in range(0,51):
                for l in range(0,51):
                    if k == l == 0 or i == k == 0 or j == l == 0:
                        continue
                    elif i == k and j == l:
                        continue
                    a = getDistance(i,j,k,l)
                    b = getDistance(i,j,0,0)
                    c = getDistance(k,l,0,0)
                    if checkRight(a,b,c) and [[i,j],[k,l]] not in used and [[k,l],[i,j]] not in used:
                        used.append([[i,j],[k,l]])
                        counter += 1
    return counter

if __name__ == "__main__":
    print(compute())
