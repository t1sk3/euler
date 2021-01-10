from math import *

def compare(root, square):
    length = len(str(square))
    

def f(N):
    i = 0
    squares = []
    s = []
    while i < N + 1:
        squares.append(i**2)
        i += 1
    for square in squares:
        total = 0
        root = sqrt(square)
        if compare(root, square):
            s.append(square)
    print(s)
    return sum(s)

if __name__ == "__main__":
    print(f(10000))