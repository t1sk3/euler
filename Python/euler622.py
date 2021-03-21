from sympy import divisors
import time

def main():
    LIMIT = 60

    alldivs = set(divisors(2**LIMIT - 1))

    for i in range(1, LIMIT):
        alldivs -= set(divisors(i))
    return str(sum(alldivs) + len(alldivs))

if __name__ == "__main__":
    now = time.time()
    print(main())
    print(time.time() - now)