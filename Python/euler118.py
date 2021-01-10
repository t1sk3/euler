import eulerlib
import itertools

def joinAll(lst):
    res = []
    for comb in lst:
        number = ''
        for char in list(comb):
            number += str(char)
        res.append(int(number))
    return res

lst = [1,2,3,4,5,6,7,8,9]
comb = []
for i in range(1,10):
    for num in joinAll(list(itertools.combinations(lst,i))):
        if eulerlib.is_prime(num):
            
            comb.append(num)
comb = list(reversed(comb))
print(comb)