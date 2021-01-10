a = 100
c = 0
lst = []
while a < 1000:
    b = 100
    while b < 1000:
        n = b * a
        temp = n
        rev  =0
        while n > 0:
            dig = n % 10
            rev = rev * 10 + dig
            n = n // 10
        if temp == rev:
            lst.append(temp)
        b = b + 1
    a = a + 1
print(max(lst))
