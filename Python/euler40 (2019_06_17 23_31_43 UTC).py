from operator import mul
sc = [9*(x+1) * pow(10, x) for x in xrange(50)]

def d(n, i=0):
	while n>sc[i]: n-= sc[i]; i+= 1
	L, d = divmod((n-1), i+1)
	return int(str(pow(10, i)+L)[d])

print(reduce(mul, (d(10**i) for i in range(7))))