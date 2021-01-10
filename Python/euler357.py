import eulerlib

def checkValue(x):
    lst = eulerlib.Divisors().divisors(x)
    for d in lst:
        if not eulerlib.prime_numbers.is_prime(d + 30/d):
            return False
        return True

def compute():
    lst = []
    for n in range(1,100000001):
        if checkValue(n):
            lst.append(n)
    return sum(lst)

if __name__ == "__main__":
    print(compute())