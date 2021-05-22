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
	LIMIT := 100

	num := big.NewInt(int64(LIMIT))
	ref := big.NewInt(num.Int64())
	ref2 := big.NewInt(ref.Int64())
	temp := new(big.Int)
	num_string := ""
	n := 0
	res := 0

	for i := 1; i < LIMIT; i++ {
		ref = big.NewInt(ref2.Int64())
		temp = big.NewInt(int64(i))
		num = num.Mul(num, ref.Sub(ref, temp))
	}
	num_string = num.String()
	for _, c := range num_string {
		n, _ = strconv.Atoi(string(c))
		res += n
	}
	return res
}
