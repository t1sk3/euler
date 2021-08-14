package main

import (
	"eulerlib"
	"fmt"
	"math"
)

var (
	LIMIT  int64
	primes []int
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	LIMIT = int64(math.Pow(10, 9))
	primes = eulerlib.ListPrimes(100)

	return solve2(0, 1)
}

func solve2(pInd int, pr int64) int {
	var res int
	if pInd == len(primes) {
		if pr <= LIMIT {
			return 1
		} else {
			return 0
		}
	} else {
		for pr <= LIMIT {
			res += solve2(pInd+1, pr)
			pr *= int64(primes[pInd])
		}
		return res
	}
}
