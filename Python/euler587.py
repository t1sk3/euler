from math import pi, sqrt
import scipy.integrate as integrate
import scipy.special as special
from numpy import arcsin, arccos, arctan
import numpy as np
import matplotlib.pyplot as plt
import itertools, math

def lsection():
    return ((2 * 2) - (pi * 1))/8

def findN(lsection):
    b = 2
    h = 2
    g = giveValueList()
    while True:
        b += 2
        rico = h/b
        intersect = giveIntersect(rico, g)
        Istr = integrate.quad(lambda x: rico * x, 0, intersect)[0]
        Icirc = integrate.quad(lambda x: -sqrt(1-(x-1)**2) + 1, intersect, 1)[0]
        Itot = Istr + Icirc - 0.0001073
        if Itot/lsection < 0.001:
            return int(b/2)

def giveValueList():
    lst = [1]
    working = True
    i = 0
    while working:
        i += 0.0001
        lst.append(-sqrt(1-(i-1)**2) + 1)
        if i >= 0.9997:
            working = False
    reworking = True
    while reworking:
        if len(lst) > 10000:
            lst.remove(lst[499])
        elif len(lst) < 10000:
            lst.append(0)
        elif len(lst) == 10000:
            reworking = False
    return lst

def giveIntersect(rico, g):
    f = np.arange(0, rico, rico/10000)
    reworking = True
    while reworking:
        if len(f) > 10000:
            f = np.delete(f, 0)
        elif len(f) < 10000:
            f = np.append(f, 0)
        elif len(f) == 10000:
            reworking = False
    idx = np.argwhere(np.diff(np.sign(f - g))).flatten()
    return idx[0]/10000

def main():
    print(findN(lsection()))

###
def compute():
	# The indefinite integral of (1 - sqrt(2x - x^2)) dx.
	def integral(x):
		t = x - 1.0
		return t - (math.sqrt(x * (2.0 - x)) * t + math.asin(t)) / 2.0
	
	lsectionarea = 1.0 - math.pi / 4.0
	for i in itertools.count(1):
		slope = 1.0 / i
		a = slope**2 + 1.0
		b = -2.0 * (slope + 1.0)
		c = 1.0
		x = (2.0 * c) / (-b + math.sqrt(b * b - 4 * a * c))
		concavetrianglearea = (x**2 * slope / 2) + (integral(1.0) - integral(x))
		if concavetrianglearea / lsectionarea < 0.001:
			return str(i)
###

if __name__ == "__main__":
	print(findN(lsection()))

