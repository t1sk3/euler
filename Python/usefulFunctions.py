from math import ceil, sqrt

def isPrime(num):
    q = int(ceil(sqrt(num)))
    for i in range(2, q+1):
        if num != 1 and i != num:
            if num % i == 0:
                return False
    return True

def findNextPrime(last):
    finding = True
    number = last
    while finding:
        number += 1
        if isPrime(number):
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