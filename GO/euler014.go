package main

import (
	"fmt"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	maxi := 0
	lenMaxi := 0
	temp := 0
	m := make(map[int]int)

	for i := 2; i < 1000001; i++ {
		temp = get_length(i, m)
		m[i] = temp
		if temp > lenMaxi {
			lenMaxi = temp
			maxi = i
		}
	}
	return maxi
}

func get_length(n int, m map[int]int) int {
	var nextNum int
	value, ok := m[n]
	if ok {
		return value
	}
	if n == 1 {
		return 1
	}
	if n%2 == 0 {
		nextNum = int(n / 2)
	} else {
		nextNum = n*3 + 1
	}
	return get_length(nextNum, m) + 1
}
