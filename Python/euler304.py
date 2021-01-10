from math import ceil, sqrt
from tqdm import tqdm

def isPrime(num):
    c = 0
    q = int(ceil(sqrt(num)))                    
    for i in range(2, q+1):                     
        if num != 1 and i != num:               
            if num % i == 0:
                c = 1
            else:
                c = c
    if c == 0:
        return True
    else:
        return False

def findNextPrime(last):
    finding = True
    number = last
    while finding:
        number += 1
        if isPrime(number):
            return number

def a(n):
    if n == 1:
        return findNextPrime(10**14)
    else:
        return findNextPrime(a(n-1))

def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 

def b(n):
    return Fibonacci(a(n))

def main():
    lst = []
    for i in tqdm(range(1,100001)):
        lst.append(b(i))
    return sum(lst)

if __name__ == "__main__":
    print(main() % 1234567891011)