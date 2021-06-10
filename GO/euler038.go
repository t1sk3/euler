package main

import (
	"eulerlib"
	"fmt"
	"math"
	"strconv"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	res := -1
	tmp := ""
	tmp2 := -1

	for n := 2; n <= 9; n++ {
		for i := 1; i < int(math.Pow(10, float64(9/n))); i++ {
			tmp = ""
			for j := 1; j <= n; j++ {
				tmp += strconv.Itoa(i * j)
			}
			tmp2, _ = strconv.Atoi(tmp)
			if eulerlib.IsPandigital(tmp2) {
				res = eulerlib.MaximumBetweenInts(tmp2, res)
			}
		}
	}
	return res
}
