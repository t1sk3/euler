package main

import (
	"fmt"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	LIMIT := 1001
	res := 1

	for i := 3; i <= LIMIT; i += 2 {
		res += 4*i*i - 6*(i-1)
	}
	return res
}
