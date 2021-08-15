def memoize(f):
    results = {}
    def helper(n):
        if n not in results:
            results[n] = f(n)
        return results[n]
    return helper

def main():
    maxi = 0
    lenMaxi = 0
    for i in range(2, 1000001):
        if getLength(i) > lenMaxi:
            lenMaxi = getLength(i)
            maxi = i
    return str(maxi)

@memoize
def getLength(num):
    if num == 1:
        return 1
    if num % 2 == 0:
        nextNum = num // 2
    else:
        nextNum = num * 3 + 1
    
    return getLength(nextNum) + 1

if __name__ == "__main__":
    print(main())



