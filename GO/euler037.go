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
	primes := eulerlib.ListPrimality(999999)
	res := 0

	for i, c := range primes {
		if c && len(strconv.Itoa(i)) > 1 {
			if checkPrime(i) {
				res += i
			}
		}
	}
	return res
}

func checkPrime(p int) bool {
	s := strconv.Itoa(p)
	var tmp1 int
	var tmp2 int
	for i := 1; i < len(s); i++ {
		tmp1, _ = strconv.Atoi(s[i:])
		tmp2, _ = strconv.Atoi(s[:len(s)-i])
		if !eulerlib.IsPrime(tmp1) || !eulerlib.IsPrime(tmp2) {
			return false
		}
	}
	return true
}
