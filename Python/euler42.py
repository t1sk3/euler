def triangleLst():
    triangle = []
    for i in range(0,26*20):
        triangle.append(0.5*i*(i+1))
    return triangle

def checkWord():
    wordLst = []
    letterLst = []
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    counter = 0

    file = open("p042_words.txt")
    lines = file.readlines()
    file.close()
    
    for line in lines:
        if not len(line.strip()) == 0:
            columns = line.split('","')
        for i in range(0,len(columns)):
            wordLst.append(columns[i])

    for i in range(0,len(wordLst)):
        letterLst.clear()
        value = 0
        for char in wordLst[i]:
            letterLst.append(char)

        for letter in letterLst:
            if letter == '"':
                letterLst.remove('"')

        for letter in letterLst:
            value += (alphabet.index(letter)+1)
            
        if value in triangleLst():
            counter += 1
    return counter

def main():
    print(checkWord())

if __name__ == "__main__":
    main()