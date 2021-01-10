#28433×27830457+1

def printLastTen():
    MOD = 10**10
    result = (28433 * pow(2, 7830457, MOD) + 1) % MOD
    return result

def main():
    print(printLastTen())

if __name__ == "__main__":
    main()