def giveNum(i, prime):
    x = prime + 2*i**2
    return x

def listing():
    lst = []

    file = open("C:\\Users\\matti\\Documents\\Python\\Projects\\euler\\1000primes.txt", "r")
    lines = file.readlines()
    file.close()

    prime_list = []
    prime_listtemp = []
    for line in lines:
        if not len(line.strip()) == 0:
            columns = line.split(' ')
            if ' ' in columns:
                columns[i].replace(' ', '')
            if '\n' in columns:
                columns.remove('\n')
            columns = list(dict.fromkeys(columns))
        for i in range(0,len(columns)):
            prime_listtemp.append(columns[i])
    
    for i in range(0,len(prime_listtemp)):
        if prime_listtemp[i] != '':
            prime_list.append(int(prime_listtemp[i]))
    prime_list = sorted(prime_list)
    
    for i in range(0,100):
        for prime in prime_list:
            lst.append(giveNum(i, prime))
    lst = list(dict.fromkeys(lst))
    return lst

def main():
    oddNums = listing()
    oddNums = sorted(oddNums)
    for num in oddNums:
        if num %2 == 0:
            oddNums.remove(num)
    for i in range(4,2*len(oddNums)):
        if i % 2 == 1:
            if i not in oddNums:
                print("That stupidass number you were looking for should look something like this: ", i)
                break

if __name__ == "__main__":
    main()