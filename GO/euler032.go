package main

import (
	"eulerlib"
	"fmt"
	"math"
	"sort"
	"strconv"
)

// I had a lot of difficulty porting this specific problem over
// The solution is very ugly but it works. Maybe I'll tidy it up later

func main() {
	fmt.Println(solve())
}

func solve() int64 {
	res := int64(0)
	for i := int64(1); i < 10000; i++ {
		if has_pandigital_product(i) {
			res += i
		}
	}
	return res
}

func has_pandigital_product(n int64) bool {
	var temp int64
	var temp2 string
	var temp3 int
	for i := int64(1); i < int64(math.Sqrt(float64(n)))+1; i++ {
		if n%i == 0 {
			temp2 = strconv.FormatInt(n, 10) + strconv.FormatInt(i, 10) + strconv.FormatInt((n-n%i)/i, 10)
			temp3, _ = strconv.Atoi(temp2)
			temp = int64(temp3)
			if sort_string(eulerlib.JoinSlice(eulerlib.MakeIntSlice(temp))) == "123456789" {
				return true
			}
		}
	}
	return false
}

func sort_string(s string) string {
	temp := []int{}
	temp2 := -1
	for _, e := range s {
		temp2, _ = strconv.Atoi(string(e))
		temp = append(temp, temp2)
	}
	sort.Ints(temp)
	return eulerlib.JoinSlice(temp)
}
