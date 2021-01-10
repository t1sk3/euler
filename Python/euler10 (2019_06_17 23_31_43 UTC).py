from math import *
p=0
q=0
c = 0
i=0
lst = []
while p < 2000000:
    c=0
    p=p+1
    q=int(ceil(sqrt(p)))
    for i in range(2, q+1):
        if p != 1:
            if p%i==0:
                    c=1
            else:
                    c=c
    if c==0:
        lst.append(p)
        print(p)
print(sum(lst))