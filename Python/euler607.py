from scipy.optimize import fsolve
import math

def main():
    global D, d, dd, v_lst
    D = 5 * math.sqrt(2)
    d = 1
    dd = D - d * 5
    v_lst = [0.9, 0.8, 0.7, 0.6, 0.5]
    x = fsolve(f, 1.0)
    return round(solve(x), 10)

def f(x):
    global D, d, dd, v_lst
    res = 0
    for v in v_lst:
        res += 1 / math.sqrt((1 + 1. / x / x) / v / v - 1)
    return res * d + dd * x - D

def solve(x):
    st0 = 1 / math.sqrt(1/x/x+1)
    ct0 = math.sqrt(1 - st0**2)
    res = dd / ct0
    for v in v_lst:
        sti = st0 * v
        cti = math.sqrt(1 - sti**2)
        res += d / cti / v
    return res

if __name__ == "__main__":
    print(main())
