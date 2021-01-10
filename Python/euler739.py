import sympy

def makeSequence1(n):
    lst = [1,3,4]
    for i in range(1,n+1):
        lst.append(sympy.lucas(i))
    return lst

def makeSequence(n):
    lst = []
    for i in range(n):
        lst.append(1)
    return lst

def compute():
    sequence = makeSequence1(10**8)
    newSequence = makeSequence(len(sequence) - 1)
    print(sequence)
    while len(sequence) > 1:
        sequence = sequence[1:]
        j = 0
        while True:
            newSequence[j] = sum(sequence[:j+1])
            j += 1
            if j == len(newSequence):
                break
        sequence = newSequence
        newSequence = newSequence[1:]
    return sequence[0]

print(compute() % 1000000007)

#print(makeSequence1(8))
