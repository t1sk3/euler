package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	var num int
	var bestA int
	var bestB int
	bNum := 0
	LIMIT := 1000

	for a := -LIMIT; a <= LIMIT; a++ {
		for b := -LIMIT; b <= LIMIT; b++ {
			num = number_of_consec_primes_generated(a, b)
			if num > bNum {
				bNum = num
				bestA = a
				bestB = b
			}
		}
	}
	return bestA * bestB
}

func number_of_consec_primes_generated(a int, b int) int {
	var n int
	for i := 0; ; i++ {
		n = i*i + i*a + b
		if n < 0 || !is_prime(n) {
			return i
		}
	}
}

func is_prime(n int) bool {
	end := int(math.Sqrt(float64(n)))
	for i := 2; i <= end; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}
