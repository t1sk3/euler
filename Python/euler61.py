import itertools
import time

def triangle():
    trianglelst = []
    n = 0
    while True:
        n += 1
        num = int(n*(n+1)/2)
        if len(str(num)) == 4:
            trianglelst.append(num)
        elif len(str(num)) > 4:
            return trianglelst

def square():
    squarelst = []
    n = 0
    while True:
        n += 1
        num = int(n**2)
        if len(str(num)) == 4:
            squarelst.append(num)
        elif len(str(num)) > 4:
            return squarelst

def pentagonal():
    pentagonallst = []
    n = 0
    while True:
        n += 1
        num = int(n*((3*n)-1)/2)
        if len(str(num)) == 4:
            pentagonallst.append(num)
        elif len(str(num)) > 4:
            return pentagonallst

def hexagonal():
    hexagonallst = []
    n = 0
    while True:
        n += 1
        num = int(n*(2*n-1))
        if len(str(num)) == 4:
            hexagonallst.append(num)
        elif len(str(num)) > 4:
           return hexagonallst

def heptagonal():
    heptagonallst = []
    n = 0
    while True:
        n += 1
        num = int(n*(5*n-3)/2)
        if len(str(num)) == 4:
            heptagonallst.append(num)
        elif len(str(num)) > 4:
            return heptagonallst

def octogonal():
    octogonallst = []
    n = 0
    while True:
        n += 1
        num = int(n*(3*n-2))
        if len(str(num)) == 4:
            octogonallst.append(num)
        elif len(str(num)) > 4:
            return octogonallst

def findSetPerm(lst1, lst2, lst3, lst4, lst5, lst6):
    for numo in lst1:
        for numhex in lst2:
            if str(numo)[-2] == str(numhex)[0] and str(numo)[-1] == str(numhex)[1]:
                for nump in lst3:
                    if str(numhex)[-2] == str(nump)[0] and str(numhex)[-1] == str(nump)[1]:
                        for numt in lst4:
                            if str(nump)[-2] == str(numt)[0] and str(nump)[-1] == str(numt)[1]:
                                for nums in lst5:
                                    if str(numt)[-2] == str(nums)[0] and str(numt)[-1] == str(nums)[1]:
                                        for numhep in lst6:
                                            if str(nums)[-2] == str(numhep)[0] and str(nums)[-1] == str(numhep)[1]:
                                                if str(numhep)[-2] == str(numo)[0] and str(numhep)[-1] == str(numo)[1]:
                                                    return numt + nums + nump + numhex + numhep + numo
    raise ValueError

def findSet():
    permutations = list(itertools.permutations([0, 1, 2, 3, 4, 5]))
    for perm in permutations:
        iteration = []
        for digit in perm:
            if digit == 0:
                iteration.append(triangle())
            elif digit == 1:
                iteration.append(square())
            elif digit == 2:
                iteration.append(pentagonal())
            elif digit == 3:
                iteration.append(hexagonal())
            elif digit == 4:
                iteration.append(heptagonal())
            elif digit == 5:
                iteration.append(octogonal())
        try:
            result = findSetPerm(iteration[0], iteration[1], iteration[2], iteration[3], iteration[4], iteration[5])
            return result, perm
        except:
            continue
    return None

def main():
    start_time = time.time()
    print(f"The sum of the set along with the order in which the polygonal numbers are used are:\n{findSet()}")
    print(f"--- Found in {time.time() - start_time} seconds ---")

if __name__ == "__main__":
    main()