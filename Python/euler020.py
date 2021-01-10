fact = 1
for i in range(1,101):
    fact = fact*i
lst = [int(d) for d in str(fact)]
print(sum(lst))