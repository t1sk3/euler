from math import *

def getRelativePrimeList(n):
    L = []
    for i in range(1,n):
        if gcd(i,n)==1:
            L.append(i)
    return L

def compute():
    lst = []
    for i in range(1, 9):
        if i % 1000 == 0:
            print(i)
        for j in getRelativePrimeList(i):
            lst.append(j/i)
    return len(lst)

if __name__ == "__main__":
    print(compute())