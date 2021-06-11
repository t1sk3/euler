package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	res := -1
	var penI int
	var penJ int
	var dif int
	for i := 2; ; i++ {
		penI = penNum(i)
		if res != -1 && penI-penNum(i-1) >= res {
			break
		}
		for j := i - 1; j >= 1; j-- {
			penJ = penNum(j)
			dif = penI - penJ
			if res != -1 && dif >= res {
				break
			} else if isPenNum(penI+penJ) && isPenNum(dif) {
				res = dif
			}
		}
	}
	return res
}

func penNum(n int) int {
	return n * (n*3 - 1) / 2
}

func isPenNum(n int) bool {
	if n <= 0 {
		return false
	}
	tmp := n*24 + 1
	sqrt := int(math.Sqrt(float64(tmp)))
	return sqrt*sqrt == tmp && sqrt%6 == 5
}
