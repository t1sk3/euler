package main

import (
	"fmt"
	"math/big"
)

func main() {
	fmt.Println(solve())
}

func solve() string {
	res := new(big.Int).SetInt64(1)
	tmp := new(big.Int).SetInt64(-1)
	tmp2 := new(big.Int).SetInt64(-1)
	for i := 2; i <= 1000; i++ {
		tmp2 = new(big.Int).SetInt64(int64(i))
		res.Add(res, tmp.Exp(tmp2, tmp2, nil))
	}
	return res.Text(10)[len(res.Text(10))-10:]
}
