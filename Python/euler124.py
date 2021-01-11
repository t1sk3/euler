

def main():
    lst = [0] + [1] * 100000
    for i in range(2,100000+1):
        if lst[i] == 1:
            for j in range(i, 100000+1, i):
                lst[j] *= i
    lst = data = sorted((rad, i) for (i, rad) in enumerate(lst))
    return str(lst[10000][1])

print(main())