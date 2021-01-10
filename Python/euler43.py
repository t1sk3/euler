#This script takes a minute to finish

from itertools import permutations

def ZerotoNine():
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    permutationLst = [''.join(p) for p in permutations(numbers)]
    subNum = []

    for number in permutationLst:
        specNum = split(number)
        i = 0
        strlist = []
        while i<7:
            i += 1
            strlist.append(int(''.join(specNum[0+i:3+i])))
        if strlist[0]%2 == 0 and strlist[1]%3 == 0 and strlist[2]%5 == 0 and strlist[3]%7 == 0 and strlist[4]%11 == 0 and strlist[5]%13 == 0 and strlist[6]%17 == 0:
            subNum.append(int(number))
    return sum(subNum)

def split(word):
    return [char for char in word]

def main():
    print("Final answer:", ZerotoNine())

if __name__ == "__main__":
    main()