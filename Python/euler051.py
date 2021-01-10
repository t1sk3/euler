from math import ceil, sqrt
import time

def isPrime(num):
    c = 0
    q = int(ceil(sqrt(num)))                    #Please be patient
    for i in range(2, q+1):                     #This script is in no way, shape or form efficient
        if num != 1 and i != num:               #It can take up to 80 seconds (on my pc) to find the solution
            if num % i == 0:
                return False
    return True

def findNextPrime(last):
    finding = True
    number = last
    while finding:
        number += 1
        if isPrime(number):
            return number

def changingNumbers(prime, quant):
    five = False
    six = False
    if quant == 5:
        five = True
    elif quant == 6:
        six = True
    else:
        return
    
    primelst = []
    choicelst = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    fivedigitchoices = [[1, 0, 0, 0, 1],
                        [0, 1, 0, 0, 1],
                        [0, 0, 1, 0, 1],
                        [0, 0, 0, 1, 1]]
    sixdigitchoices = [[1,1,0,0,0,1],
                        [1,0,1,0,0,1],
                        [1,0,0,1,0,1],
                        [1,0,0,0,1,1],
                        [0,1,1,0,0,1],
                        [0,1,0,1,0,1],
                        [0,0,1,1,0,1],
                        [0,1,0,0,1,1],
                        [0,0,1,0,1,1],
                        [0,0,0,1,1,1]]

    digitlst = []
    prime = str(prime)
    for digit in prime:
        digitlst.append(digit)
    
    counter = 1
    if five:
        for i in range(0,3):
            newlst = list(digitlst)
            primelst.clear()
            counter = 1
            for numnum in choicelst:
                for j in range(0,4):
                    if fivedigitchoices[i][j] == 0:
                        newlst[j] = numnum
                newprim = int(''.join(str(d) for d in newlst))
                if isPrime(newprim) and str(newprim) != prime and newlst[0] != '0' and newprim not in primelst:
                    counter += 1
                    primelst.append(newprim)
            if counter == 8:
                primelst.append(int(prime))
                if min(primelst) == int(prime):
                    return True, primelst
    elif six:
        for i in range(0,9):
            newlst = list(digitlst)
            primelst.clear()
            counter = 1
            for numnum in choicelst:
                for j in range(0,5):
                    if sixdigitchoices[i][j] == 0:
                        newlst[j] = numnum
                newprim = int(''.join(str(d) for d in newlst))
                if isPrime(newprim) and str(newprim) != prime and newlst[0] != '0' and newprim not in primelst:
                    counter += 1
                    primelst.append(newprim)
            if counter == 8:
                primelst.append(int(prime))
                if min(primelst) == int(prime):
                    return True, primelst
    return ValueError

def enterNext():
    entering = True
    isItGood = False
    nextOne = findNextPrime(56993)
    while entering:
        nextOne = findNextPrime(nextOne)
        if nextOne > 999999:
            print("not found")
            exit(0)

        leng = len(str(nextOne))

        try:
            isItGood, thelst = changingNumbers(nextOne, leng)
        except:
            isItGood = False

        if isItGood:
            entering = False
            
    if finalCheck(thelst):
        return thelst
    else:
        print("Final check returned False, the script will be aborted.")
        exit(0)

def findSmallest(lst1):
    smallest = min(lst1)
    return smallest

def finalCheck(lst):
    counter = 0
    for number in lst:
        print(number, isPrime(number))
        if isPrime(number):
            counter += 1
    if counter == 8:
        return True
    else:
        return False
    
def main():
    start_time = time.time()
    print(findSmallest(enterNext()))
    print(f"--- Found in {time.time() - start_time} seconds ---")

if __name__ == "__main__":
    main()