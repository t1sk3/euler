import eulerlib

from usefulFunctions import isPrime
from math import sqrt

def memoize(function):
    from functools import wraps

    memo = {}

    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper

def compute():
	PRIME_LIMIT = 100000  # Arbitrary initial cutoff
	primes = eulerlib.prime_numbers.primes(PRIME_LIMIT)
	
	
	# Tries to find any suitable set and return its sum, or None if none is found.
	# A set is suitable if it contains only primes, its size is targetsize,
	# its sum is less than or equal to sumlimit, and each pair concatenates to a prime.
	# 'prefix' is an array of ascending indices into the 'primes' array,
	# which describes the set found so far.
	# The function blindly assumes that each pair of primes in 'prefix' concatenates to a prime.
	# 
	# For example, find_set_sum([1, 3, 28], 5, 10000) means "find the sum of any set
	# where the set has size 5, consists of primes with the lowest elements being [3, 7, 109],
	# has sum 10000 or less, and has each pair concatenating to form a prime".
	def find_set_sum(prefix, targetsize, sumlimit):
		if len(prefix) == targetsize:
			return sum(primes[i] for i in prefix)
		else:
			istart = 0 if (len(prefix) == 0) else (prefix[-1] + 1)
			for i in range(istart, len(primes)):
				if primes[i] > sumlimit:
					break
				if all((is_concat_prime(i, j) and is_concat_prime(j, i)) for j in prefix):
					prefix.append(i)
					result = find_set_sum(prefix, targetsize, sumlimit - primes[i])
					prefix.pop()
					if result is not None:
						return result
			return None
	
	
	# Tests whether concat(primes[x], primes[y]) is a prime number, with memoization.
	@memoize
	def is_concat_prime(x, y):
		return isPrime(int(str(primes[x]) + str(primes[y])))
	
	
	# Tests whether the given integer is prime. The implementation performs trial division,
	# first using the list of primes named 'primes', then switching to simple incrementation.
	# This requires the last number in 'primes' (if any) to be an odd number.
	
	
	sumlimit = PRIME_LIMIT
	while True:
		setsum = find_set_sum([], 5, sumlimit - 1)
		if setsum is None:  # No smaller sum found
			return str(sumlimit)
		sumlimit = setsum


if __name__ == "__main__":
	print(compute())
