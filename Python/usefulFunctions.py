from math import ceil, sqrt, factorial

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
        if newlst[i] == 10:
            newlst[i] = 'A'
        elif newlst[i] == 11:
            newlst[i] = 'B'
        elif newlst[i] == 12:
            newlst[i] = 'C'
        elif newlst[i] == 13:
            newlst[i] = 'D'
        elif newlst[i] == 14:
            newlst[i] = 'E'
        elif newlst[i] == 16:
            newlst[i] = 'F' 
        elif newlst[i] == 17:
            newlst[i] = 'G' 
        elif newlst[i] == 18:
            newlst[i] = 'H' 
        elif newlst[i] == 19:
            newlst[i] = 'I' 
        elif newlst[i] == 20:
            newlst[i] = 'J' 
        elif newlst[i] == 21:
            newlst[i] = 'K' 
        elif newlst[i] == 22:
            newlst[i] = 'L' 
        elif newlst[i] == 23:
            newlst[i] = 'M' 
        elif newlst[i] == 24:
            newlst[i] = 'N' 
        elif newlst[i] == 25:
            newlst[i] = 'O'
        elif newlst[i] == 26:
            newlst[i] = 'P' 
        elif newlst[i] == 27:
            newlst[i] = 'Q' 
        elif newlst[i] == 28:
            newlst[i] = 'R' 
        elif newlst[i] == 29:
            newlst[i] = 'S' 
        elif newlst[i] == 30:
            newlst[i] = 'T' 
        elif newlst[i] == 31:
            newlst[i] = 'U' 
        elif newlst[i] == 32:
            newlst[i] = 'V' 
        elif newlst[i] == 33:
            newlst[i] = 'W' 
        elif newlst[i] == 34:
            newlst[i] = 'X' 
        elif newlst[i] == 35:
            newlst[i] = 'Y' 
        elif newlst[i] == 36:
            newlst[i] = 'Z' 

    res = ''.join(str(d) for d in newlst)
    return res