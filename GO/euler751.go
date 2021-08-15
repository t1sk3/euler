package main

import (
	"fmt"
	"math/big"
	"strings"
)

func main() {
	fmt.Println(solve())
}

func solve() string {
	tmp := new(big.Float).SetPrec(200).SetFloat64(2.2)
	tmp2 := new(big.Float).SetPrec(200).SetFloat64(2.2)
	a := new(big.Float).SetPrec(200).SetFloat64(2.2)
	b := concat(a)
	adder := new(big.Float).SetPrec(200).SetFloat64(0.01)
	divider := new(big.Float).SetPrec(200).SetFloat64(0.1)
	counter := 0

	for a.Text('f', 24) != b {
		counter++
		tmp2, _ = new(big.Float).SetPrec(200).SetString(b)
		if a.Cmp(tmp2) == 1 {
			a.Copy(tmp)
			adder.Mul(adder, divider)
		} else {
			tmp.Copy(a)
			a.Add(a, adder)
			b = concat(a)
		}
	}
	return a.Text('f', 24)
}

func concat(n *big.Float) string {
	var b big.Float
	b.Copy(n)
	res := ""
	bFloor, _ := new(big.Float).SetPrec(200).SetString(b.Text('f', 0))
	one := new(big.Float).SetPrec(200).SetFloat64(1.0)
	tmp := b.Text('f', 100)
	res = tmp[:strings.Index(tmp, ".")+1]
	for len(res) <= 26 {
		bFloor.SetPrec(200).SetString(b.Text('f', 100)[:strings.Index(b.Text('f', 100), ".")])
		b.SetPrec(200).Mul(bFloor, new(big.Float).SetPrec(200).Add(new(big.Float).SetPrec(200).Sub(&b, bFloor), one))
		tmp = b.Text('f', 100)
		res += tmp[:strings.Index(tmp, ".")]
	}
	return res[:26]
}
