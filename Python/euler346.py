import itertools

LIMIT = 10**12

def compute():
    strongs = {1}
    for length in range(3, LIMIT.bit_length() + 1):
        for base in itertools.count(2):
            value = (base ** length - 1) // (base - 1)
            if value >= LIMIT:
                break
            strongs.add(value)
    ans = sum(strongs)
    return str(ans)

if __name__ == "__main__":
    print(compute())