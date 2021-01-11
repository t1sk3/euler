from math import sqrt


def count_divisors(n):
    d = {}
    count = 1

    while n % 2 == 0:
        n = n / 2
        try:
            d[2] += 1
        except KeyError:
            d[2] = 1

    for i in range(3, int(sqrt(n+1)), 2):
        while n % i == 0 and i != n:
            n = n / i
            try:
                d[i] += 1
            except KeyError:
                d[i] = 1

    d[n] = 1

    for _,v in d.items():
        count = count * (v + 1)

    return count

def tri_number(num):
  next = 1 + int(sqrt(1+(8 * num)))
  return num + (next/2)


def main():
    i = 1
    while count_divisors(i) < 500:
        i = tri_number(i)
    return str(int(i))

if __name__ == "__main__":
    print(main())