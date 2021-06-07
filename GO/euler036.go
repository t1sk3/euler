package main

import (
	"eulerlib"
	"fmt"
	"strconv"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	var res int

	for i := 1; i < 1000000; i++ {
		if eulerlib.IsPalindrome(strconv.Itoa(i)) && eulerlib.IsPalindrome(eulerlib.DecimalToBase(i, 2)) {
			res += i
		}
	}
	return res
}
