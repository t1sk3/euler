package main

import (
	"fmt"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	i := 286
	j := 166
	k := 144
	var triangle int
	var pentagon int
	var hexagon int
	var min int
	for true {
		triangle = i * (i + 1) / 2
		pentagon = j * (j*3 - 1) / 2
		hexagon = k * (k*2 - 1)
		min = minInt(minInt(triangle, pentagon), hexagon)
		if min == triangle && min == pentagon && min == hexagon {
			return min
		}
		if min == triangle {
			i++
		}
		if min == pentagon {
			j++
		}
		if min == hexagon {
			k++
		}
	}
	return -1
}

func minInt(a int, b int) int {
	if b > a {
		return a
	} else {
		return b
	}
}
