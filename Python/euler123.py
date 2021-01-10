import eulerlib

def main():
    lst = eulerlib.prime_numbers.primes_wheel_fact(10**6)
    for n in range(5, len(lst), 2):
        rem = n * lst[n-1] * 2
        if rem > 10**10:
            return n

if __name__ == "__main__":
    print(main())