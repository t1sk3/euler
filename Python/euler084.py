import random
from math import *

def makeList():
    lst = []
    for i in range(40):
        lst.append(0)
    return lst

def checkCh(card):
    global coordinate
    if card > 0:
        if card == 50:
            while True:
                if coordinate in [5, 15, 25, 35]:
                    break
                elif coordinate > 39:
                    coordinate -= 40
                coordinate += 1
        elif card == 51:
            while True:
                if coordinate in [12, 28]:
                    break
                elif coordinate > 39:
                    coordinate -= 40
                coordinate += 1
        else:
            coordinate = card
    elif card < 0:
        coordinate += card

def checkCc(card):
    global coordinate
    coordinate = card

def compute():
    global double, res, ch, cc, coordinate, dice, chcells, cccells, g2j
    for i in range(9999999):

        dice1 = random.choice(dice)
        dice2 = random.choice(dice)
        throw = dice1 + dice2
        if dice1 == dice2:
            double += 1
        if double == 3:
            double = 0
            coordinate = 10
        else:
            coordinate += throw
            if coordinate > 39:
                coordinate -= 40
            if coordinate in chcells:
                cardch = ch[0]
                ch.remove(cardch)
                ch.append(cardch)
                checkCh(cardch)
            elif coordinate in cccells:
                cardcc = cc[0]
                ch.remove(cardcc)
                ch.append(cardcc)
                checkCc(cardcc)
            elif coordinate == g2j:
                coordinate = 10
        res[coordinate] += 1
    return res

dice = [1,2,3,4,5,6]
coordinate = 0

ch = [0, 10, 11, 24, 39, 5, 50, 50, 51, -3]
cc = [00, 10]

random.shuffle(ch)
random.shuffle(cc)

chcells = [7, 22, 36]
cccells = [2, 17, 33]
g2j = 30

double = 0

res = makeList()

results = compute()
resultsbackup = results

sum1 = sum(results)

max1 = max(results)
index1 = resultsbackup.index(max1)
results.remove(max1)

max2 = max(results)
index2 = resultsbackup.index(max2)
results.remove(max2)

max3 = max(results)
index3 = resultsbackup.index(max3)
results.remove(max3)

print(f"{index1}: {max1/sum1}")
print(f"{index2}: {max2/sum1}")
print(f"{index3}: {max3/sum1}")