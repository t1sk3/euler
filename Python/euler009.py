from math import *

def main():
    a = 0
    b = 0
    c = 0
    while a < 1000:
        a = a + 1
        b = 0
        while b < 1000:
            b = b + 1
            c = sqrt(a**(2) + b**(2))
            if a + b + c == 1000:
                d = a*b*c
                break
    return str(int(d))

if __name__ == "__main__":
    print(main())