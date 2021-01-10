import itertools

#1587000

def checkValue(x):
    lst = [int(d) for d in str(x)]
    if list(reversed(sorted(lst))) == lst or list(sorted(lst)) == lst:
        return False
    return True

def compute():
    lst = []
    lstUsed = []
    for i in itertools.count(1):
        lstUsed.append(i)
        if checkValue(i):
            lst.append(i)
        if len(lst)/len(lstUsed) > 0.99:
            return i-1

print(compute())