import eulerlib

#922058210

def compute():
    res = []
    lst = eulerlib.fibonacci.first_n_fibo(90)
    lst.remove(lst[0])

    for num in lst:
        res.append(S(num))
    
    return sum(res)

def S(k):
    lst = []
    for i in range(1,k+1):
        lst.append(s(i))
    return sum(lst)

def s(n):
    i = 0
    while True:
        i += 1
        if getSum(i) == n:
            return i

def getSum(x):
    lst = []
    x = str(x)
    for num in x:
        lst.append(int(num))
    return sum(lst)

if __name__ == "__main__":
    print(compute())
