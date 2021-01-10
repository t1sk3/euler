from fractions import Fraction
from tqdm import tqdm
import sys

sys.setrecursionlimit(1100)

#this is using bruteforce
def frac(counter, limit):
    if counter == limit - 1:
        return 2
    counter += 1
    return 2 + Fraction(1, frac(counter, limit))

def checkFrac(frac):
    if len(str(frac.numerator)) > len(str(frac.denominator)):
        return True
    return False

def main():
    counter = 0
    lst = []
    for i in tqdm(range(1, 1001)):
        if checkFrac(Fraction(1 + Fraction(1, frac(0, i)), 1)):
            lst.append('x')
            counter += 1
        else:
            lst.append('o')
    return counter

#this is not using bruteforce but with understanding of the underlying pattern, does not work yet
def mainSecond():
    counter = 0
    limitingcounter = 0
    isitseven = True
    lst = []
    while True:
        counter += 1
        limitingcounter += 1
        if counter == 7 and isitseven:
            lst.append('x')
            isitseven = False
            counter = -1
        elif counter == 4 and isitseven == False:
            lst.append('x')
            isitseven = True
            counter = -1
        else:
            lst.append('o')
        if limitingcounter == 1000:
            return lst.count('x')

if __name__ == "__main__":
    print(f"The number of fractions with a numerator that has more digits than the denominator is {main()}")
    #print(f"Not using the bruteforce method, the result is {mainSecond()}")