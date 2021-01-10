from sympy import *

def compute():
    i = 3
    maximum = 0
    while i <= 1000000:
        if i % 10000 == 0:
            print(i)
        if i/totient(i) > maximum:
            maximum = i/totient(i)
            maxi = i
        i += 1
    return maxi

if __name__ == "__main__":
    print(compute())



