package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	triangle := 0

	for i := 1; ; i++ {
		triangle += i
		if count_divisors(triangle) > 500 {
			return triangle
		}
	}
	return -1
}

func count_divisors(n int) int {
	count := 0
	end := int(math.Sqrt(float64(n)))
	for i := 1; i < end; i++ {
		if n%i == 0 {
			count += 2
		}
	}
	if end*end == n {
		count++
	}
	return count
}
