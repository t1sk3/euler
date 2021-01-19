

def main():
    peter = [1,2,3,4]
    colin = [1,2,3,4,5,6]
    peterRes = []
    colinRes = []
    peterChance = []
    colinChance = []
    for i in peter:
        for j in peter:
            for k in peter:
                for l in peter:
                    for m in peter:
                        for n in peter:
                            for o in peter:
                                for p in peter:
                                    for q in peter:
                                        peterRes.append(i+j+k+l+m+n+o+p+q)
    
    for i in colin:
        for j in colin:
            for k in colin:
                for l in colin:
                    for m in colin:
                        for n in colin:
                            colinRes.append(i+j+k+l+m+n)
    
    for i in range(1,37):
        x = peterRes.count(i)
        y = colinRes.count(i)
        peterChance.append([i, x/len(peterRes)])
        colinChance.append([i, y/len(colinRes)])

    for i in peterChance:
        res = 0
        for j in colinChance:
            if i[0] > j[0]:
                res += i[1]*j[1]
        i.append(res)
    
    chance = 0
    for i in peterChance:
        chance += i[2]

    return str(round(chance, 7))


print(main())