import eulerlib, fractions

def compute():
	TARGET = fractions.Fraction(15499, 94744)
	totient = 1
	denominator = 1
	p = 2
	while True:
		totient *= p - 1
		denominator *= p
		while True:
			p += 1
			if eulerlib.is_prime(p):
				break
		if fractions.Fraction(totient, denominator) < TARGET:
			for i in range(1, p):
				numer = i * totient
				denom = i * denominator
				if fractions.Fraction(numer, denom - 1) < TARGET:
					return str(denom)

if __name__ == "__main__":
	print(compute())