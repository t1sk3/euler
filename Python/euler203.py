from usefulFunctions import binomial
from sympy import primerange

def main():
    LIMIT = 51
    n = 0
    lst = []
    for i in range(LIMIT):
        k = 0
        while k < n+1:
            lst.append(binomial(n,k))
            k += 1
        n += 1
    lst = list(dict.fromkeys(lst))

    res = []

    for num in lst:
        if is_squarefree(num):
            res.append(num)
    return str(sum(res))


def is_squarefree(num):
    primes = primerange(0, num)
    for prime in primes:
        if prime > num**0.5:
            return True
        if num%(prime**2) == 0:
            return False
    return True

if __name__ == "__main__":
    print(main())
