package main

import (
	"fmt"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	maxP := 0
	maxT := 0
	var t int

	for p := 1; p <= 1000; p++ {
		t = countSol(p)
		if t > maxT {
			maxT = t
			maxP = p
		}
	}
	return maxP
}

func countSol(p int) int {
	res := 0
	var c int
	for a := 1; a <= p; a++ {
		for b := a; b <= p; b++ {
			c = p - a - b
			if b <= c && a*a+b*b == c*c {
				res++
			}
		}
	}
	return res
}
