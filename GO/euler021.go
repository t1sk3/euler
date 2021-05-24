package main

import (
	"fmt"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	divisorsum := []int{}
	for i := 0; i < 10000; i++ {
		divisorsum = append(divisorsum, 0)
	}
	for i := 1; i < len(divisorsum); i++ {
		for j := i * 2; j < len(divisorsum); j += i {
			divisorsum[j] += i
		}
	}

	res := 0
	j := -1
	for i := 0; i < len(divisorsum); i++ {
		j = divisorsum[i]
		if j != i && j < len(divisorsum) && divisorsum[j] == i {
			res += i
		}
	}
	return res
}
