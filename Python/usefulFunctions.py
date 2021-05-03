from math import ceil, sqrt, factorial
import string

def is_prime(num):
    q = int(ceil(sqrt(num)))
    for i in range(2, q+1):
        if num != 1 and i != num:
            if num % i == 0:
                return False
    return True

def binomial(n, k):
    assert 0 <= k <= n
    return factorial(n) // (factorial(k) * factorial(n - k))

def findNextPrime(last):
    finding = True
    number = last
    while finding:
        number += 1
        if is_prime(number):
            return number

def divisor(n):
    large_divisors = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

def divisorGen(n):
    return list(divisor(n))

def list_primes():
    n = 0
    while True:
        n += 1
        if is_prime(n):
            yield n

def to_base(num, base):
    if base == 10:
        return num
    
    num = int(num)
    basebase = 1
    iteration = 0
    newlst = []
    while basebase <= num:
        basebase = basebase*base
        iteration += 1
    iteration += -1
    multiplier = base**iteration
    for i in range (0, iteration + 1):
        if int(num) >= multiplier:
            nieuw = (num - (num%multiplier))/multiplier
            newlst.append(nieuw)
            num = num - multiplier*nieuw

        else:
            newlst.append('0')
        if multiplier != 1:
            multiplier = multiplier/base
        elif multiplier == 1:
            multiplier = 0

    for i in range(0, len(newlst)):
        newlst[i] = int(newlst[i])

    for i in range(0, len(newlst)):
        for j in range(10, 36):
            if newlst[i] == j:
                newlst[i] = string.ascii_lowercase[i-9]

    res = ''.join(str(d) for d in newlst)
    return res