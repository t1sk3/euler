import itertools
from tqdm import tqdm

def checkPerm(num, cubelst):
    numlst = list(str(num))
    permutations = list(itertools.permutations(numlst))
    counter = 0
    for permutation in permutations:
        if is_perfect_cube(int(''.join(permutation))):
            if int(''.join(permutation)) in cubelst:
                counter += 1
        if counter > 5:
            return False
    if counter == 5:
        return True
    return False

def checkCubeLst():
    cubelst = []
    for i in range(5000,6000):
        cubelst.append(i**3)
    for cube in tqdm(cubelst):
        if checkPerm(cube, cubelst):
            return cube

def is_perfect_cube(number) -> bool:
    number = abs(number)
    return round(number ** (1 / 3)) ** 3 == number

def main():
    print(checkCubeLst())

if __name__ == "__main__":
    main()