

def main():
    # creating dices
    peter = [1,2,3,4]
    colin = [1,2,3,4,5,6]
    peterRes = []
    colinRes = []
    peterChance = []
    colinChance = []

    # creating all peters possible combinations
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
    
    # creating all colins possible combinations
    for i in colin:
        for j in colin:
            for k in colin:
                for l in colin:
                    for m in colin:
                        for n in colin:
                            colinRes.append(i+j+k+l+m+n)
    
    # counting how many times a combination occurs
    for i in range(1,37):
        x = peterRes.count(i)
        y = colinRes.count(i)
        peterChance.append([i, x/len(peterRes)])
        colinChance.append([i, y/len(colinRes)])

    for i in peterChance:                   # When a throw of Peter is higher than Colins,
        res = 0                             # the chance of this throw winning will be equal to
        for j in colinChance:               # the chance of this throw * the sum of the chances of the throws it wins of Colin
            if i[0] > j[0]:
                res += i[1]*j[1]
        i.append(res)
    
    # adds up all calculated chances
    chance = 0
    for i in peterChance:
        chance += i[2]

    return str(round(chance, 7))


print(main())