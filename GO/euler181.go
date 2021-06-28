package main

import (
	"fmt"
)

func main() {
	fmt.Println(solve())
}

func solve() int64 {
	bb := 60
	w := 40
	vals := [][]int64{}
	tmp := []int64{}
	for i := 0; i <= bb; i++ {
		tmp = []int64{}
		for j := 0; j <= w; j++ {
			tmp = append(tmp, 0)
		}
		vals = append(vals, tmp)
	}
	vals[0][0] = 1
	for a := 0; a <= bb; a++ {
		for b := 0; b <= w; b++ {
			if a+b != 0 {
				for c := bb; c >= a; c-- {
					for d := w; d >= b; d-- {
						for mult := 1; c-(a*mult) >= 0 && d-(b*mult) >= 0; mult++ {
							vals[c][d] += vals[c-a*mult][d-b*mult]
						}
					}
				}
			}
		}
	}
	return vals[bb][w]
}
