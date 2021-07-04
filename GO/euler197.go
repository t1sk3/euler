package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(solve())
}

func solve() float64 {
	ITER := int64(1000000000000)
	x := float64(-1)
	y := float64(-1)
	i := int64(0)
	var rem int64
	var res float64

	for ; i < ITER; i++ {
		if i > 0 && x == y {
			break
		}
		x = f(x)
		y = f(f(y))
		//fmt.Println(x, y)
	}
	rem = (ITER - i) % i
	//fmt.Println(rem, x)
	for ; rem > 0; rem-- {
		x = f(x)
	}
	res = x + f(x)
	res = math.Floor(res*1000000000) / 1000000000
	return res
}

func f(x float64) float64 {
	return math.Floor(math.Pow(2, 30.403243784-(x*x))) / 1000000000
}
