from decimal import *
from math import *

# 40886

getcontext().prec = 100

def compute():
    res = 0
    roots = []
    used = []
    sums = []
    for i in range(1, 101):
        if not sqrt(i).is_integer():
            used.append(i)
            num1 = getNums(i)
            sum1 = getSum(num1)
            roots.append(num1)
            sums.append(sum1)
            res += sum1
    
    for i in range(len(used)):
        print(f"{used[i]}: {roots[i]}, {len(roots[i])}, {sums[i]}")

    return res

def getNums(num):
    res = str(Decimal(num).sqrt()).split('.')[1]
    #res = res[0] + res[1]
    return res

def getSum(num):
    res = 0
    for n in num:
        res += int(n)
    return res

if __name__ == "__main__":
    print(compute())