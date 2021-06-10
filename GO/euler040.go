package main

import (
	"fmt"
	"math"
	"strconv"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	var tmp string
	res := 1

	for i := 1; i < 1000000; i++ {
		tmp += string(strconv.Itoa(i))
	}

	fmt.Println("hello")

	var tmp3 int

	for i := 0; i <= 6; i++ {
		tmp3, _ = strconv.Atoi(removeZero(string(tmp[int(math.Pow(10, float64(i)))-1])))
		res *= tmp3
	}
	return res
}

func removeZero(s string) string {
	res := ""

	for _, c := range s {
		if string(c) != string("0") {
			res += string(c)
		}
	}
	return res
}
