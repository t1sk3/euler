def summing(num):
    summy = 0
    for i in range(1, num + 1):
        summy += i**i
    return summy

def lastTen(num):
    num = str(num)
    downsizing = True
    while downsizing:
        if len(num) != 10:
            num = num[1:]
        else:
            downsizing = False
            print(len(num))
    return(num)
    
def main():
    print(lastTen(summing(1000)))

if __name__ ==  "__main__":
    main()