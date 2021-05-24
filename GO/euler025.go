package main

import (
	"fmt"
	"math/big"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	last := new(big.Int).SetInt64(1)
	current := new(big.Int).SetInt64(2)
	LIMIT := 1000
	counter := 3
	temp := new(big.Int).SetInt64(0)

	for true {
		counter++
		temp.SetString(current.Text(16), 16)
		current.Add(current, last)
		last.SetString(temp.Text(16), 16)
		if len(current.Text(10)) == LIMIT {
			return counter
		}
	}
	return -1
}
