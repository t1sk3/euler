from euler51 import isPrime
import time

def spiral():
    primediagonals = [3,5,7,13,17,31,37,34]
    diagonals = [1,3,5,7,9,13,17,21,25,31,37,43,49]
    adder = 8
    number = 49
    while True:
        for i in range(0,4):
            number += adder
            diagonals.append(number)
            if isPrime(number):
                primediagonals.append(number)
        adder += 2
        if len(primediagonals)/len(diagonals) < 0.1:
            return adder - 1

def main():
    start_time = time.time()
    print(spiral())
    print(f"Found in {time.time() - start_time} seconds")

if __name__ == "__main__":
    main()


