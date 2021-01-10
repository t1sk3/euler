from tqdm import tqdm
import time
from math import factorial as fact

def calculateFac(num):
    return fact(num)

def calc(n, r):
    top = calculateFac(n)
    bottom1 = calculateFac(r)
    bottom21 = n - r
    bottom22 = calculateFac(bottom21)
    newnum = top/(bottom1 * bottom22)
    return newnum

def checkNum(num):
    if num > 1000000:
        return True
    return False

def main():
    start_time = time.time()
    counter = 0
    for n in tqdm(range(1,101)):
        for r in range(1,n+1):
            if checkNum(calc(n, r)):
                counter += 1
    print(counter)
    print(f"--- Found in {time.time() - start_time} seconds ---")
    
if __name__ == "__main__":
    main()