def isLychrel(num):
    for i in range(0,50):
        num += returnPalindrome(num)
        if isPalindrome(num):
            return False
    return True

def returnPalindrome(num):
    return int(str(num)[::-1])

def isPalindrome(num):
    if num == int(str(num)[::-1]):
        return True
    return False

def main():
    counter = 0
    for i in range(10000):
        if isLychrel(i):
            counter += 1
    print(counter)

if __name__ == "__main__":
    main()