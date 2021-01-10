from tqdm import tqdm

def fact(num):
    fact = 1
    for i in range(1,num+1): 
        fact = fact * i
    return fact

def countUp(startnum):
    strnum = str(startnum)
    newnum = 0
    for digit in strnum:
        newnum += fact(int(digit))
    return newnum

def iterate():
    goodones = 0
    for i in tqdm(range(1,1000001)):
        usedlst = []
        iterating = True
        usedlst.append(i)
        nextnum = countUp(i)
        usedlst.append(nextnum)
        while iterating:
            nextnum = countUp(nextnum)
            if nextnum not in usedlst:
                usedlst.append(nextnum)
            else:
                if len(usedlst) == 60:
                    goodones += 1
                    iterating = False
                else:
                    iterating = False
    return goodones

def main():
    print(iterate())

if __name__ == "__main__":
    main()
    

# %%
