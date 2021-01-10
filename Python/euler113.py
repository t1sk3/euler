import itertools

#51161058134250

def checkValue(x):
    lst = [int(d) for d in str(x)]
    if list(reversed(sorted(lst))) == lst or list(sorted(lst)) == lst:
        return False
    return True

def compute():
    counter = 0
    for i in range(1,10**100 + 1):
        if not checkValue(i):
            counter += 1
    return counter

print(compute())