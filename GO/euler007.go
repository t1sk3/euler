package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	LIMIT := 10001
	lst := []int{}
	i := 1

	for len(lst) < LIMIT {
		i++
		if is_prime(i) {
			lst = append(lst, i)
		}
	}
	return lst[len(lst)-1]
}

func is_prime(p int) bool {
	for i := 2; i <= int(math.Sqrt(float64(p))); i++ {
		if p%i == 0 {
			return false
		}
	}
	return true
}
