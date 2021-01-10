def chanceNone(n):
    if n == 1:
        return 1
    return (1/2*n) * (1)/((n-1)*2-1) * chanceNone(n-1)

#print(1 - chanceNone(3))
#print(calcRest(5))

#56/180