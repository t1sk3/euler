def iterate():
    counter = 0
    usednum = []
    for i in range(1,10):
        for j in range(1,30):
            if checkLength(j, i**j) and [i, i**j] not in usednum:
                usednum.append([i, i**j])
                counter += 1
    return counter

def checkLength(num, power):
    if len(str(power)) == num:
        return True
    return False

def main():
    print(iterate())

if __name__ == "__main__":
    main()