n = 0
lst = []
lst2 = [0]
for n in range (837000,838000):
    #n = 837799
    lst.clear()
    lst.append(n)
    print(n)
    while n != 1:
        if n%2==0:
            n = n / 2
            lst.append(n)
        else:
            n = 3 * n + 1
            lst.append(n)
    if len(lst) > len(lst2):
        lst2.clear()
        lst2 = lst
print(lst2[0])
print(len(lst2))
print(lst2)