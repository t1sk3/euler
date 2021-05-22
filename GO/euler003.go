package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	LIMIT := 600851475143

	for i := int(math.Sqrt(float64(LIMIT))); i > 1; i-- {
		//fmt.Println(i)
		if LIMIT%i == 0 && is_prime(i) {
			return i
		}
	}
	return -1
}

func is_prime(p int) bool {
	for i := 2; i <= int(math.Sqrt(float64(p))); i++ {
		if p%i == 0 {
			return false
		}
	}
	return true
}
