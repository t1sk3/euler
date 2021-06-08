package main

import (
	"eulerlib"
	"fmt"
	"strconv"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	LIMIT := 1000000
	isPrime := eulerlib.ListPrimality(LIMIT - 1)
	res := 0

	for i := range isPrime {
		if isCircularPrime(i, isPrime) {
			res++
		}
	}
	return res
}

func isCircularPrime(n int, isPrime []bool) bool {
	s := strconv.Itoa(n)
	tmp := -1

	for i := range s {
		if i == len(s) {
			tmp, _ = strconv.Atoi(eulerlib.Substring(s, i))
		} else {
			tmp, _ = strconv.Atoi(s[i:] + eulerlib.Substring(s, i))
		}
		if !isPrime[tmp] {
			return false
		}
	}
	return true
}
