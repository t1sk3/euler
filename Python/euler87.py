import eulerlib

LIMIT = 7069
LIMIT2 = 367
LIMIT3 = 83

#LIMIT = 7

def compute():
    counter = 0
    p = 0
    lst = []
    for i in eulerlib.prime_numbers.primes_wheel_fact(LIMIT):
        p += 1
        for j in eulerlib.prime_numbers.primes_wheel_fact(LIMIT2):
            for k in eulerlib.prime_numbers.primes_wheel_fact(LIMIT3):
                if i**2 + j**3 + k**4 < 50000000 and i**2 + j**3 + k**4 not in lst:
                    #print(i**2 + j**3 + k**4,i,j,k)
                    lst.append(i**2 + j**3 + k**4)
                    counter += 1
                else:
                    break
            if i**2 + j**3 > 50000000:
                break
        if p % 10 == 0:
            print(p)
    return counter


print(compute())

'''lst = []
for prime in eulerlib.prime_numbers.prime_wheel_fact_gen():
    lst.append(prime)
    if prime**4>50000000:
        print(last)
        break
    last = prime'''
