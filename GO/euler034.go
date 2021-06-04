package main

import (
	"eulerlib"
	"fmt"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	res := 0
	for i := 3; i < 10000000; i++ {
		if i == eulerlib.FactorialDigitSum(i) {
			res += i
		}
	}
	return res
}
