import eulerlib

LIMIT = 120000

def main():
    rads = [0] + [1] * (LIMIT - 1)
    for i in range(1, len(rads)):
        if rads[i] == 1:
            for j in range(i, len(rads), i):
                rads[j] *= i

    sortedrads = sorted((rad,n) for (n,rad) in enumerate(rads))
    sortedrads = sortedrads[1:]

    res = 0
    for i in range(2, LIMIT):
        for (rad, r) in sortedrads:
            rad *= rads[i]
            if rad >= i:
                break
            a = i - r
            if r < a and rad * rads[a] < i and eulerlib.numtheory.gcd(r,a) == 1:
                res += i
    return str(res)

if __name__ == "__main__":
    print(main())