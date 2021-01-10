a = 0
lst = []
lst2 = []
while a < 100:
    a = a + 1
    lst.append(a)
for num in lst:
    b = num**2
    lst2.append(b)
e = sum(lst2)
c = sum(lst)
d = c**2
f = min(e,d)
g = max(e,d)
h = g - f
print(h)