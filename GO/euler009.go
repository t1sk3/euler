package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	for c := 1; c < 999; c++ {
		for b := 1; b < 1000-c; b++ {
			for a := 1; a < 1001-b-c; a++ {
				if a+b+c == 1000 && is_triplet(a, b, c) {
					return a * b * c
				}
			}
		}
	}
	return -1
}

func is_triplet(a int, b int, c int) bool {
	if math.Pow(float64(c), 2) == math.Pow(float64(b), 2)+math.Pow(float64(a), 2) {
		return true
	}
	return false
}
