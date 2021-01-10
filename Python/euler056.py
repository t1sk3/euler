def calcNum():
    maxvalue = 0
    for i in range(1,100):
        for j in range(1,100):
            if digitSum(i**j) > maxvalue:
                maxvalue = digitSum(i**j)
    return maxvalue

def digitSum(num):
    num = str(num)
    numlst = []
    for digit in num:
        numlst.append(int(digit))
    return sum(numlst)

def main():
    print(calcNum())

if __name__ == "__main__":
    main()