package main

import (
	"fmt"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	LIMIT := 20
	i := 1
	check := 0
	for true {
		i++
		check = 0
		for j := 1; j < LIMIT+1; j++ {
			if i%j == 0 {
				check++
			} else {
				break
			}
		}
		if check == LIMIT {
			return i
		}
	}
	return -1
}
