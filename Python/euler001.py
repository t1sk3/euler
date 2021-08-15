
def main():
    n = 3
    o = 5
    lst = []
    while n < 1000:
        lst.append(n)
        n = n + 3
    while o < 1000:
        lst.append(o)
        o = o + 5
    lst = list(dict.fromkeys(lst))
    a = sum(lst)
    return str(a)

if __name__ == "__main__":
    print(main())