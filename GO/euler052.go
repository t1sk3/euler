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

func solve() int {
	start := 125874
	var ref string
	var found bool
	for i := start + 1; ; i++ {
		ref = eulerlib.JoinSliceString(toStringSliceSorted(i))
		found = true
		for j := 2; j < 7; j++ {
			if eulerlib.JoinSliceString(toStringSliceSorted(i*j)) != ref {
				found = false
			}
		}
		if found {
			return i
		}
	}
}

func toStringSliceSorted(n int) []string {
	nstr := strconv.Itoa(n)
	res := []string{}
	for _, c := range nstr {
		res = append(res, string(c))
	}
	sort.Strings(res)
	return res
}
