package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	LIMIT := 2000000
	res := 0

	for i := 2; i < LIMIT; i++ {
		if is_prime(i) {
			res += i
		}
	}
	return res
}

func is_prime(p int) bool {
	for i := 2; i <= int(math.Sqrt(float64(p))); i++ {
		if p%i == 0 {
			return false
		}
	}
	return true
}
