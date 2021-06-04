package main

import (
	"eulerlib"
	"fmt"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	numer := 1
	denom := 1
	n0 := -1
	n1 := -1
	d0 := -1
	d1 := -1

	for d := 10; d < 100; d++ {
		for n := 10; n < d; n++ {
			n0 = n % 10
			n1 = n / 10
			d0 = d % 10
			d1 = d / 10

			if n1 == d0 && n0*d == n*d1 || n0 == d1 && n1*d == n*d0 {
				numer *= n
				denom *= d
			}
		}
	}
	return denom / eulerlib.Gcd(numer, denom)
}
