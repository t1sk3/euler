import eulerlib

def isReversible(num):
    reverse = ''
    for char in str(num):
        reverse = char + reverse
    if sorted(str(num)) == sorted(str(int(reverse))):
        return True, int(reverse)
    return False, 0

def checkValue(num):
    odds = [1,3,5,7,9]
    for char in str(num):
        if int(char) not in odds:
            return False
    return True

def compute():
    counter = 0
    for i in range(1,10**9 + 1):
        if i % 100000 == 0:
            print(i)
        reversible, reverse = isReversible(i)
        if reversible:
            num = i + reverse
            if checkValue(num):
                counter += 1
    return counter

print(compute())


