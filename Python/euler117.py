def compute():
	# Dynamic programming
	LENGTH = 50
	ways = [1] + [0] * LENGTH
	for n in range(1, len(ways)):
		ways[n] += sum(ways[max(n - 4, 0) : n])
	return str(ways[-1])


if __name__ == "__main__":
	print(compute())