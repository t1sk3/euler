from tqdm import tqdm

def giveNextNum(num):
    newnum = 0
    for digit in str(num):
        newnum += int(digit)**2
    return newnum

def iterateNum(num):
    while True:
        num = giveNextNum(num)
        if num == 1:
            return False
        elif num == 89:
            return True

def iterateNumbers():
    counter = 0
    for i in tqdm(range(1,10000000)):
        if iterateNum(i):
            counter += 1
    return counter

def main():
    print(iterateNumbers())

if __name__ == "__main__":
    main()