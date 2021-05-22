package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	LIMIT := 100
	sqos := 0
	sosq := 0

	for i := 1; i <= LIMIT; i++ {
		sosq += int(math.Pow(float64(i), 2))
		sqos += i
	}
	sqos = int(math.Pow(float64(sqos), 2))
	return int(math.Abs(float64(sqos - sosq)))
}
