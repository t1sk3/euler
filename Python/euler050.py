from math import *
from tqdm import tqdm

def findPrimesBelow(num):
    p=0
    q=0
    c = 0
    i=0
    lst = []
    for p in tqdm(range(1, num + 1)):
        c=0
        q=int(ceil(sqrt(p)))
        for i in range(2, q+1):
            if p != 1:
                if p%i==0 and i != 1 and i != p:
                        c=1
                else:
                        c=c
        if c==0:
            lst.append(p)
    return lst

def findingConsecutiveSum(inp):
    result = 0
    resultprime = 0
    for i in tqdm(range(0, len(inp))):
        num = 0
        counter = 0
        for j in range(0, 100):
            counter += 1
            num += inp[i + j]
            if num in inp and counter > result:
                result = counter
                resultprime = num
    return num
                
def main():
    print(findingConsecutiveSum(findPrimesBelow(1000000)))

if __name__ == "__main__":
    main()