package main

import (
	"fmt"
	"math/big"
	"strings"
)

var (
	prec uint
)

func main() {
	fmt.Println(solve())
}

func solve() string {
	prec = 81
	tmp := new(big.Float).SetPrec(prec).SetFloat64(2.2)
	tmp2 := new(big.Float).SetPrec(prec).SetFloat64(2.2)
	a := new(big.Float).SetPrec(prec).SetFloat64(2.2)       // I plotted a few inputs for the function concat and
	b := concat(a)                                          // now know that the solution is a little bigger than 2.2
	adder := new(big.Float).SetPrec(prec).SetFloat64(0.01)  // In this graph it can be seen that the point where
	divider := new(big.Float).SetPrec(prec).SetFloat64(0.1) // the plotted points (y=concat(x)) cross the line given by                                         // y=x is our solution, as here both x an y are the same in
	for a.Text('f', 24) != b {                              // both functions
		tmp2, _ = new(big.Float).SetPrec(prec).SetString(b)
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
	bFloor, _ := new(big.Float).SetPrec(prec).SetString(b.Text('f', 0))
	one := new(big.Float).SetPrec(prec).SetFloat64(1.0)
	tmp := b.Text('f', 100)
	res = tmp[:strings.Index(tmp, ".")+1]
	for len(res) <= 26 {
		bFloor.SetPrec(prec).SetString(b.Text('f', 100)[:strings.Index(b.Text('f', 100), ".")])
		b.SetPrec(prec).Mul(bFloor, new(big.Float).SetPrec(prec).Add(new(big.Float).SetPrec(prec).Sub(&b, bFloor), one))
		tmp = b.Text('f', 100)
		res += tmp[:strings.Index(tmp, ".")]
	}
	return res[:26]
}
