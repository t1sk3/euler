from math import *
p=0
q=0
n=0
i=0
while n != 10001:
        c=0
        p=p+1
        q=int(ceil(sqrt(p)))
        for i in range(2, q+1):
                if p%i==0:
                        c=1
                else:
                        c=c
        if c==0:
               n = n + 1
print(p)