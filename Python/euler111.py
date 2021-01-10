import eulerlib

def S(n,d,lst1):
    x, lst = M(n,d,lst1)
    return sum(lst)

def M(n,d,lst1):
    lst = []
    max1 = 0
    res = []
    for prime in lst1:
        times = [int(k) for k in str(prime)].count(d)
        if max1 < times:
            max1 = times
            res = []
            res.append(prime)
        elif max1 == times:
            res.append(prime)
    return max1, res

def compute():
    results = []
    primes = []
    for prime in eulerlib.prime_numbers.prime_wheel_fact_gen():
        if len(str(prime)) == 10:
            primes.append(prime)
        elif len(str(prime)) > 10:
            break
    for d in range(10):
        results.append(S(10,d,primes))
    return sum(results)

if __name__ == "__main__":
    print(compute())
