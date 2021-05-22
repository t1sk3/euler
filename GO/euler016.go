package main

import (
	"fmt"
	"math/big"
	"strconv"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	num := new(big.Int).SetInt64(2)
	two := new(big.Int).SetInt64(2)
	num_string := ""
	res := 0
	temp := -1

	for i := 0; i < 999; i++ {
		num.Mul(num, two)
	}

	num_string = num.Text(10)
	for _, c := range num_string {
		temp, _ = strconv.Atoi(string(c))
		res += temp
	}
	return res
}
