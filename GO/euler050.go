package main

import (
	"eulerlib"
	"fmt"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	LIMIT := 1000000
	isPrime := eulerlib.ListPrimality(LIMIT)
	primes := eulerlib.ListPrimes(LIMIT)

	maxS := 0
	maxR := -1
	var sum int
	for i := 0; i < len(primes); i++ {
		sum = 0
		for j := i; j < len(primes); j++ {
			sum += primes[j]
			if sum > LIMIT {
				break
			} else if j-i > maxR && sum > maxS && isPrime[sum] {
				maxS = sum
				maxR = j - i
			}
		}
	}
	return maxS
}
