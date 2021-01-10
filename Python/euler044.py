from tqdm import tqdm

def sequence():
    lst = []
    for i in range(1,3000):
        lst.append(i*(3*i-1)/2)
    return lst

def check(number1, number2, lst):
    number3 = number1 + number2
    number4 = number1 - number2
    if number3 in lst and number4 in lst:
        return True
    return False

def iterate():
    c = 99999999999999999
    lst = sequence()
    for i in tqdm(range(1,3000)):
        num1 = i*(3*i-1)/2
        for j in range(1,3000):
            num2 = j*(3*j-1)/2
            if check(num1,num2,lst) and num1 - num2 <= c and num1 - num2 >= 0 and num1 != num2:
                c = num1 - num2
    return c

def main():
    print(iterate())

if __name__ == "__main__":
    main()