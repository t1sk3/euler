from tqdm import tqdm
from collections import OrderedDict 

def checkTimes(num, tim):
    timnum = num * tim
    strnum = str(num)
    strtimnum = str(timnum)
    strtimnum = removeDupWithOrder(strtimnum)
    strnum = removeDupWithOrder(strnum)
    if len(strnum) != 6 or len(strtimnum) != 6:
        return False
    for letter in strtimnum:
        if letter in strnum:
            strnum = strnum[:strnum.index(letter)] + strnum[strnum.index(letter)+1:]
    if len(strnum) == 0:
        return True
    return False

def removeDupWithOrder(str): 
    return "".join(OrderedDict.fromkeys(str)) 

def main():
    for j in tqdm(range(100000, 1000000)):
        counter = 0
        for i in range(1,7):
            if checkTimes(j,i):
                counter += 1
        if counter == 6:
            lol = int(j)
            print(lol)
            exit(0)

if __name__ == "__main__":
    main()