package main

import (
	"fmt"
	"math/big"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	res := 0
	ref := new(big.Int).SetInt64(1000000)
	tmp := new(big.Int).SetInt64(-1)
	for n := 1; n <= 100; n++ {
		for r := 1; r <= n; r++ {
			tmp = comb(n, r)
			if tmp.Cmp(ref) == 1 {
				res++
			}
		}
	}
	return res
}

func comb(n int, r int) *big.Int {
	n1 := new(big.Int).SetInt64(int64(n))
	r1 := new(big.Int).SetInt64(int64(r))
	n2 := factorialBigInt(n1)
	r2 := factorialBigInt(r1)
	rn := factorialBigInt(new(big.Int).SetInt64(int64(n - r)))
	return n2.Div(n2, r2.Mul(r2, rn))
}

func factorialBigInt(n *big.Int) *big.Int {
	if n.Text(10) == "1" || n.Text(10) == "0" {
		return new(big.Int).SetInt64(1)
	}
	res := new(big.Int).SetInt64(1)
	one := new(big.Int).SetInt64(1)
	for n.Text(10) != "1" {
		res.Mul(res, n)
		n.Sub(n, one)
	}
	return res
}
