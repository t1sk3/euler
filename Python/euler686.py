#193060223

def p(L,n):
    i = 1
    counter = 0
    while True:
        i += 1
        string1 = str(2**i)
        if string1[0] == "1" and string1[1] == "2" and string1[2] == "3":
            counter += 1
            if counter == n:
                return i

print(p(123,678910))
