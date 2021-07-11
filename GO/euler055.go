package main

import (
	"eulerlib"
	"fmt"
	"math/big"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	res := 0
	for i := 0; i < 10000; i++ {
		if isLychrel(i) {
			res++
		}
	}
	return res
}

func isLychrel(n int) bool {
	tmp := new(big.Int).SetInt64(int64(n))
	tmp2 := new(big.Int).SetInt64(-1)
	for i := 0; i < 49; i++ {
		tmp2, _ = new(big.Int).SetString(eulerlib.ReverseString(tmp.Text(10)), 10)
		tmp = tmp.Add(tmp, tmp2)
		if eulerlib.IsPalindrome(tmp.Text(10)) {
			return false
		}
	}
	return true
}
