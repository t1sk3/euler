package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	for i := 2; ; i++ {
		if hasFourPF(i+0) && hasFourPF(i+1) && hasFourPF(i+2) && hasFourPF(i+3) {
			return i
		}
	}
}

func hasFourPF(n int) bool {
	return countDistPF(n) == 4
}

func countDistPF(n int) int {
	res := 0
	end := int(math.Sqrt(float64(n)))
	for i := 2; i <= end; i++ {
		if n%i == 0 {
			for n%i == 0 {
				n /= i
			}
			res++
			end = int(math.Sqrt(float64(n)))
		}
	}
	if n > 1 {
		res++
	}
	return res
}
