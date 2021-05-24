package main

import (
	"fmt"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	bestNum := 0
	bestLen := 0
	leng := -1
	LIMIT := 1000

	for i := 1; i <= LIMIT; i++ {
		leng = get_cycle_length(i)
		if leng > bestLen {
			bestNum = i
			bestLen = leng
		}
	}
	return bestNum
}

func get_cycle_length(n int) int {
	seen := make(map[int]int)
	state := 1
	var ok bool
	for i := 1; ; i++ {
		_, ok = seen[state]
		if ok {
			return i - seen[state]
		} else {
			seen[state] = i
			state = state * 10 % n
		}
	}
}
