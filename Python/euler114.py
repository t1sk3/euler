def compute():
	# Dynamic programming
	LENGTH = 50
	ways = [0] * (LENGTH + 1)
	for n in range(len(ways)):
		if n < 3:
			ways[n] = 1
		else:
			ways[n] = ways[n - 1] + sum(ways[ : n - 3]) + 1
	return str(ways[-1])


if __name__ == "__main__":
	print(compute())