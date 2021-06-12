package main

import (
	"eulerlib"
	"fmt"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	for i := 9; ; i += 2 {
		if !isConjecture(i) {
			return i
		}
	}
}

func isConjecture(n int) bool {
	if n%2 == 0 || eulerlib.IsPrime(n) {
		return true
	}

	for i := 1; i*i*2 <= n; i++ {
		if eulerlib.IsPrime(n - i*i*2) {
			return true
		}
	}
	return false
}
