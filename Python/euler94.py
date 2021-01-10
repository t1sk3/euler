import itertools, math, eulerlib

def compute():
	LIMIT = 10**9
	ans = 0
	for s in itertools.count(1, 2):
		if s * s > (LIMIT + 1) // 3:
			break
		for t in range(s - 2, 0, -2):
			if math.gcd(s, t) == 1:
				a = s * t
				b = (s * s - t * t) // 2
				c = (s * s + t * t) // 2
				if a * 2 == c - 1:
					p = c * 3 - 1
					if p <= LIMIT:
						ans += p
				if a * 2 == c + 1:
					p = c * 3 + 1
					if p <= LIMIT:
						ans += p
				if b * 2 == c - 1:
					p = c * 3 - 1
					if p <= LIMIT:
						ans += p
				if b * 2 == c + 1:
					p = c * 3 + 1
					if p <= LIMIT:
						ans += p
	return str(ans)

def main():
    print(compute())

if __name__ == "__main__":
    main()