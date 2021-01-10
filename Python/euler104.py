import eulerlib

def compute():
    counter = -1
    for num in eulerlib.fibonacci.fibo_gen():
        counter += 1
        if sorted(str(num)[len(str(num))-9:]) == sorted(str(num)[:9]) == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return counter
        if counter % 1000 == 0:
            print(counter)

print(compute())