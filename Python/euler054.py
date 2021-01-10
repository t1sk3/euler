def checkRoyalFlush(cardsnum, cardssuit):
    flushes = ['T', 'J', 'Q', 'K', 'A']
    flush = 0
    suit = cardssuit[0]
    for card in cardsnum:
        if cardssuit[cardsnum.index(card)] != suit:
            return False
        if card in flushes:
            flush += 1
            flushes.remove(card[:1])
    if flush == 5:
        return True
    return False

def checkStraightFlush(cardsnum, cardssuit):
    suit = cardssuit[0]
    for card in cardsnum:
        if cardssuit[cardsnum.index(card)] != suit:
            return False
    if checkConsecutive(cardsnum):
        return True
    else:
        return False

def checkFourOfAKind(cardsnum):
    for card in cardsnum:
        if cardsnum.count(card) == 4:
            return True
    return False

def checkFullHouse(cardsnum):
    if checkThreeOfAKind(cardsnum) and checkPair(cardsnum):
        return True
    return False

def checkFlush(cardssuit):
    if cardssuit.count(cardssuit[0]) == 5:
        return True
    return False

def checkStraight(cardsnum):
    if checkConsecutive(cardsnum):
        return True
    return False

def checkThreeOfAKind(cardsnum):
    for card in cardsnum:
        if cardsnum.count(card) == 3:
            return True
    return False

def checkTwoPair(cardsnum):
    counter = 0
    usednums = []
    for card in cardsnum:
        if cardsnum.count(card) == 2 and card not in usednums:
            usednums.append(card)
            counter += 1
    if counter == 2:
        return True
    return False

def checkPair(cardsnum):
    for card in cardsnum:
        if cardsnum.count(card) == 2:
            return True
    return False

def highCard(cardsnum):
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    cardvalues = []
    for card in cardsnum:
        cardvalues.append(values.index(card) + 1)
    return cardsnum[cardvalues.index(max(cardvalues))]

def splitUp(hand):
    num = []
    suit = []
    for card in hand:
        suit.append(card[1:])
        num.append(card[:1])
    return num, suit

def checkConsecutive(cardsnum):
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    values2 = ['7', '8', '9', 'T', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6']
    cardvalue = []
    cardvalue2 = []
    for card in cardsnum:
        cardvalue.append(values.index(card) + 1)
        cardvalue2.append(values2.index(card) + 1)
    
    if sorted(cardvalue) == list(range(min(cardvalue), max(cardvalue)+1)) or sorted(cardvalue2) == list(range(min(cardvalue2), max(cardvalue2)+1)):
        return True
    return False

def compareCard(cardsnum1, cardsnum2):
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    comparing = True
    index1 = []
    index2 = []
    for card in cardsnum1:
        index1.append(values.index(card))
    for card in cardsnum2:
        index2.append(values.index(card))
    while comparing:
        if max(index1) > max(index2):
            return True
        elif max(index1) < max(index2):
            return False

def openUp():
    hands = open("C:\\Users\\matti\\Documents\\Python\\Projects\\euler\\poker.txt")
    handlines = hands.readlines()
    hands.close

    handsplayer1 = []
    handsplayer2 = []

    for line in handlines: 
        line = line.strip("\n")
        firstpart, secondpart = line[:15], line[15:]
        cards1 = firstpart.split(" ")
        cards2 = secondpart.split(" ")
        for card in cards1:
            if card == "":
                cards1.remove(card)
        for card in cards2:
            if card == "":
                cards2.remove(card)
        handsplayer1.append(cards1)
        handsplayer2.append(cards2)
    
    return handsplayer1, handsplayer2

def checkHand(handnum, handsuit):
    if checkRoyalFlush(handnum, handsuit):
        return 'Royal flush'
    elif checkStraightFlush(handnum, handsuit):
        return 'Straight Flush'
    elif checkFourOfAKind(handnum):
        return 'Four of a Kind'
    elif checkFullHouse(handnum):
        return 'Full House'
    elif checkFlush(handsuit):
        return 'Flush'
    elif checkStraight(handnum):
        return 'Straight'
    elif checkThreeOfAKind(handnum):
        return 'Three of a Kind'
    elif checkTwoPair(handnum):
        return 'Two Pair'
    elif checkPair(handnum):
        return 'One Pair'
    else:
        return highCard(handnum)

def checkDestinctWinner(hand1, hand2):
    specialhands = ['Royal flush', 'Straight Flush', 'Four of a Kind', 'Full House', 'Flush', 'Straight', 'Three of a Kind', 'Two Pair', 'One Pair']
    if hand1 in specialhands and hand2 not in specialhands:
        return '1'
    elif hand1 not in specialhands and hand2 in specialhands:
        return '2'
    elif hand1 in specialhands and hand2 in specialhands:
        if specialhands.index(hand1) < specialhands.index(hand2):
            return '1'
        elif specialhands.index(hand1) > specialhands.index(hand2):
            return '2'
    elif hand1 not in specialhands and hand2 not in specialhands:
        if compareCard(list(hand1), list(hand2)):
            return '1'
        else:
            return '2'
    return ValueError

def sameHand(handnum1, handsuit1, handnum2, handsuit2):
    cardvalues = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    for card in handnum1:
        if handnum1.count(card) == 2:
            card1 = card
    for card in handnum2:
        if handnum2.count(card) == 2:
            card2 = card
    if cardvalues.index(card1) > cardvalues.index(card2):
        return '1'
    elif cardvalues.index(card1) < cardvalues.index(card2):
        return '2'

def main():
    handsplayer1, handsplayer2 = openUp()

    counter = 0
    handnums1 = []
    handsuits1 = []
    handnums2 = []
    handsuits2 = []

    for hand in handsplayer1:
        handnum, handsuit = splitUp(hand)
        handnums1.append(handnum)
        handsuits1.append(handsuit)
    
    for hand in handsplayer2:
        handnum, handsuit = splitUp(hand)
        handnums2.append(handnum)
        handsuits2.append(handsuit)

    for i in range(0,1000):
        handnumi1, handsuiti1 = handnums1[i], handsuits1[i]
        handnumi2, handsuiti2 = handnums2[i], handsuits2[i]

        handname1 = checkHand(handnumi1, handsuiti1)
        handname2 = checkHand(handnumi2, handsuiti2)

        '''
        #this prints the different numbers/values of the hand,
        #then the different suits of the hand
        #and then it shows what kind of hand it is
        #then repeated for player 2
        print(handnumi1, handsuiti1)
        print(handname1)
        print(handnumi2, handsuiti2)
        print(handname2)
        print("---")
        '''

        if handname1 == handname2:
            winner = sameHand(handnumi1, handsuiti1, handnumi2, handsuiti2)
        else:
            winner = checkDestinctWinner(handname1, handname2)
        
        if winner == '1':
            counter += 1

    print(f"Player 1 wins {counter} times.")
    
if __name__ == "__main__":
    main()