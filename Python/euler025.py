a = 1
b = 1
lst = []
lst2 = []
lst.append(a)
lst.append(b)
while len(lst2) < 1000:
    a = a + b
    lst.append(a)
    b = b + a
    lst.append(b)
    lst2 = [int(d) for d in str(lst[-1])]
print(len(lst))