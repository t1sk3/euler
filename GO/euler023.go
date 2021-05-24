package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	LIMIT := 28123
	res := 0
	isAbundant := []bool{}
	for i := 0; i < LIMIT; i++ {
		isAbundant = append(isAbundant, false)
	}

	for i := 1; i < len(isAbundant); i++ {
		isAbundant[i] = is_abundant(i)
	}

	for i := 1; i <= LIMIT; i++ {
		if !is_sum_of_2_abundants(i, isAbundant) {
			res += i
		}
	}
	return res
}

func is_sum_of_2_abundants(n int, a []bool) bool {
	for i := 0; i <= n; i++ {
		if a[i] && a[n-i] {
			return true
		}
	}
	return false
}

func is_abundant(n int) bool {
	sum := 1
	end := int(math.Sqrt(float64(n)))
	for i := 2; i <= end; i++ {
		if n%i == 0 {
			sum += i + n/i
		}
	}
	if end*end == n {
		sum -= end
	}
	return sum > n
}
