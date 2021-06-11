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
	digits := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	perms := eulerlib.Permutations(digits)
	tmp := -1
	res := 0
	for _, e := range perms {
		tmp, _ = strconv.Atoi(eulerlib.JoinSlice(e))
		if isSpecial(tmp) {
			res += tmp
		}
	}
	return res
}

func isSpecial(n int) bool {
	num := strconv.Itoa(n)
	divs := []int{2, 3, 5, 7, 11, 13, 17}
	var tmp int
	for i := 1; i < 8; i++ {
		tmp, _ = strconv.Atoi(eulerlib.Substring(num[i:], 3))
		if tmp%divs[i-1] != 0 {
			return false
		}
	}
	return true
}
