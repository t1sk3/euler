#1389019170

def checkValue(n):
    n = str(n)
    i = 0
    for j in range(1,10):
        if not int(n[i]) == j:
            p = n[i]
            return False
        i += 2
    if not int(n[-1]) == 0:
        return False
    return True

def compute():
    i = 1
    while True:
        i += 1
        if len(str(i**2)) == 19:
            if checkValue(i**2):
                return i

if __name__ == "__main__":
    print(compute())
    