'''from math import *

def getRelativePrimeList(n):
    L = []
    for i in range(1,n):
        if gcd(i,n)==1:
            L.append(i)
    return L

def compute():
    lst = []
    for i in range(1, 1000001):
        if i % 1000 == 0:
            print(i)
        for j in getRelativePrimeList(i):
            lst.append(j/i)
    return lst[lst.index(3/7)-1]

if __name__ == "__main__":
    print(compute())'''

def compute():
	LIMIT = 1000000
	maxnumer = 0
	maxdenom = 1
	for d in range(1, LIMIT + 1):
		n = d * 3 // 7
		if d % 7 == 0:
			n -= 1
		if n * maxdenom > d * maxnumer:  # n/d > maxdenom/maxnumer
			maxnumer = n
			maxdenom = d
	return str(maxnumer)


if __name__ == "__main__":
	print(compute())