from math import *

def compute():
	LIMIT = 1500000

	triples = set()
	for s in range(3, ceil(sqrt(LIMIT)) + 1, 2):
		for t in range(s - 2, 0, -2):
			if gcd(s, t) == 1:
				a = s * t
				b = (s * s - t * t) // 2
				c = (s * s + t * t) // 2
				if a + b + c <= LIMIT:
					triples.add((a, b, c))
	
	ways = [0] * (LIMIT + 1)
	for triple in triples:
		sigma = sum(triple)
		for i in range(sigma, len(ways), sigma):
			ways[i] += 1
	
	ans = ways.count(1)
	return str(ans)


if __name__ == "__main__":
	print(compute())