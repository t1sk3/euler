import eulerlib

def rad(n):
    res = 1
    divisors = eulerlib.numtheory.Divisors(100000).prime_factors(n)
    for item in divisors:
        res *= item[0]
    return res

def compute():
    lst = []
    for i in range(1,100000+1):
        lst.append([i,rad(i)])
    lst = sorted(lst, key = lambda x: int(x[1]))
    return lst[10000-1][0]

print(compute())