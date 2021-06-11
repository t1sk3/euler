package main

import (
	"eulerlib"
	"fmt"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	res := -1
	for i := 2143; i < 10000000; i++ {
		if eulerlib.IsPrime(i) && eulerlib.IsPandigital(i) {
			res = i
		}
	}
	return res
}
