package main

import (
	"fmt"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	LIMIT := 1000
	res := 0
	for i := 1; i < LIMIT; i++ {
		if i%3 == 0 || i%5 == 0 {
			res += i
		}
	}
	return res
}
