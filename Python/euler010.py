import eulerlib

def main():
    return str(sum(eulerlib.prime_numbers.primes_wheel_fact(2000000)))

if __name__ == "__main__":
    print(main())