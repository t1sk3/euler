package main

import (
	"fmt"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	TOTAL := 200
	COINS := []int{1, 2, 5, 10, 20, 50, 100, 200}
	ways := []int{1}

	for i := 0; i < TOTAL; i++ {
		ways = append(ways, 0)
	}

	for _, e := range COINS {
		for i := 0; i < len(ways)-e; i++ {
			ways[i+e] += ways[i]
		}
	}
	return ways[len(ways)-1]
}
