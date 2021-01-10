from sympy import *
from itertools import permutations

def compute():
    mini = 9999999999999
    for i in range(1, 10**7 + 1):
        if i % 10000 == 0:
            print(i)
        toti = totient(i)
        if sorted(str(i)) == sorted(str(toti)):
            mini = i/toti
            minimum = i
            #print(i, toti)
    return minimum

if __name__ == "__main__":
    print(compute())