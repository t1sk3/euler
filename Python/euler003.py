from math import *

def main():
    a = 600851475143
    i = 0
    lst = []
    lst2 = []
    for i in range(2,ceil(sqrt(a))):
        if a%i==0:
            lst.append(i)
    lst = list(dict.fromkeys(lst))
    for num in lst:
        q=0
        n=2
        u=0
        c=0
        q=int(ceil(sqrt(num)))
        for u in range(2, q+1):
            if num%u==0:
                    c=1
            else:
                    c=c
        if c==0:
            lst2.append(num)
    return str(lst2[-1])

if __name__ == "__main__":
    print(main())