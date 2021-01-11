def main():
    lst = []
    lst1 = []
    a = 0
    lst.append(a)
    b = 1
    lst.append(b)
    c = 1
    lst.append(c)
    while a < 4000000 and b < 4000000 and c < 4000000:
        a = b + c
        lst.append(a)
        b = c + a
        lst.append(b)
        c = a + b
        lst.append(c)
    for num in lst:
        if num%2==0:
            lst1.append(num)

    d = sum(lst1)
    return str(d)

if __name__ == "__main__":
    print(main())

