

def main():
    global FACTORS, factSols
    FACTORS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    factSols = []

    for fact in FACTORS:
        sols = set()
        for j in range(1, fact):
            if pow(j, 3, fact) == 1:
                sols.add(j)
        factSols.append(sols)
    
    res = buildAndSumSols(0, 0, 1)

    return str(res - 1)

def buildAndSumSols(factInd, x, m):
    if factInd == len(FACTORS):
        return x
    res = 0
    fact = FACTORS[factInd]
    for sol in factSols[factInd]:
        newx = chineseRemainderTheorem(x, m, sol, fact)
        tmp = buildAndSumSols(factInd+1, newx, m * fact)
        res += tmp
    return res

def chineseRemainderTheorem(a, p, b, q):
    return (a + (b - a) * pow(p, -1, q) * p) % (p * q)

if __name__ == "__main__":
    print(main())