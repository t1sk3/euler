package main

import (
	"eulerlib"
	"fmt"
	"sort"
	"strconv"
)

func main() {
	fmt.Println(solve())
}

func solve() string {
	LIMIT := 10000
	isPrime := eulerlib.ListPrimality(LIMIT - 1)
	var a int
	var b int
	for base := 1000; base < LIMIT; base++ {
		if isPrime[base] {
			for s := 1; s < LIMIT; s++ {
				a = base + s
				b = a + s
				if a < LIMIT && isPrime[a] && hasSameDigs(a, base) && b < LIMIT && isPrime[b] && hasSameDigs(b, base) && (base != 1487 || a != 4817) {
					return strconv.Itoa(base) + strconv.Itoa(a) + strconv.Itoa(b)
				}
			}
		}
	}
	return "-1"
}

func hasSameDigs(x int, y int) bool {
	return sortString(strconv.Itoa(x)) == sortString(strconv.Itoa(y))
}

func sortString(s string) string {
	res := []string{}
	for _, c := range s {
		res = append(res, string(c))
	}
	sort.Strings(res)
	return eulerlib.JoinSliceString(res)
}
