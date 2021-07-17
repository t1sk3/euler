package main

import (
	"eulerlib"
	"fmt"
	"math/big"
)

func main() {
	fmt.Println(solve())
}

func solve() (res int) {
	tmp := new(big.Int).SetInt64(-1)
	tmp2 := new(big.Int).SetInt64(-1)
	tmpsum := -1
	for a := 1; a < 100; a++ {
		for b := 1; b < 100; b++ {
			tmp.SetInt64(int64(a))
			tmp2.SetInt64(int64(b))
			tmp.Exp(tmp, tmp2, nil)
			tmpsum = eulerlib.DigitSum(tmp.Text(10))
			if tmpsum > res {
				res = tmpsum
			}
		}
	}
	return
}
