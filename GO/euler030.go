package main

import (
	"fmt"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	LIMIT := 1000000 // If a number has 7 or more digits, the sum of the fith power of the digits will always be less
	res := 0

	for i := 2; i < LIMIT; i++ {
		if i == fifth_power_sum(i) {
			res += i
		}
	}
	return res
}

func fifth_power_sum(n int) int {
	res := 0
	var temp int

	for n != 0 {
		temp = n % 10
		res += temp * temp * temp * temp * temp
		n /= 10
	}
	return res
}
