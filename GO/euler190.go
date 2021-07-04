package main

import (
	"fmt"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	res := 0
	for i := 2; i <= 15; i++ {
		res += int(find_max(i))
	}
	return res
}

func find_max(n int) float64 {
	v := make([]float64, n)
	res := float64(1)
	v[0] = 1
	for i := 0; i < n; i++ {
		v[i] = float64(1 * (i + 1))
	}

	v[0] = float64(n) / sum(v)

	for i := 0; i < n; i++ {
		v[i] = v[0] * float64(i+1)
	}

	for i := 0; i < n; i++ {
		for j := 0; j < i+1; j++ {
			res *= v[i]
		}
	}
	return res
}

func sum(v []float64) (res float64) {
	for _, e := range v {
		res += e
	}
	return
}
