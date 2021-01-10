import itertools, eulerlib

# It is easier to generate the squares first and later check wether or not the number is a palindrome
# 2906969179

def main():
    res = set()
    for i in range(1, 10001): # because 10000**2 is the upper limit, 10001**2 would be higher than 10**8
        num = i**2
        for j in itertools.count(i + 1):
            num += j**2
            if num >= 10**8:
                break
            if eulerlib.is_palindrome(num):
                res.add(num)
    return sum(res)

if __name__ == "__main__":
    print(main())
