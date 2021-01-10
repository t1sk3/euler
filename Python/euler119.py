import eulerlib

#248155780267521
#print(eulerlib.numtheory.digital_sum(11))

def checkSum(num, ori):
    i = 1
    if num == 1:
        return False
    while True:
        if num**i == ori:
            return True
        elif num**i > ori:
            return False
        i += 1

def compute():
    i = 11
    lst = []
    while True:
        if checkSum(eulerlib.numtheory.digital_sum(i), i):
            lst.append(i)
        if len(lst) == 30:
            return lst[-1]
        i += 1

print(compute())
