package main

import (
	"eulerlib"
	"fmt"
	"math"
	"strconv"
)

// very inefficient but gets the right answer

func main() {
	fmt.Println(solve())
}

func solve() (res int64) {
	NUMSSTRING := []string{"0", "0", "1", "1", "2", "2", "3", "3", "4", "4", "5", "5", "6", "6", "7", "7", "8", "8", "9", "9"}
	var tmp float64
	var lst []int
	var p int
	var z int
	var allways float64
	var onez float64
	var twoz float64
	for _, i := range eulerlib.RemoveDuplicateSlices(eulerlib.Combinations(NUMSSTRING, 10)) {
		lst = convert_to_int(i)
		tmp = math.Abs(float64(90 - (2 * eulerlib.Sum(lst))))
		if int64(tmp)%11 == 0 {
			p = 10 - len(eulerlib.RemoveDuplicates(i))
			z = count_zero(i)

			allways = float64(eulerlib.Factorial(10)) / math.Pow(2, float64(p))
			onez = allways - (float64(eulerlib.Factorial(9)) / math.Pow(2, float64(p)))
			twoz = allways - (float64(eulerlib.Factorial(9)) / math.Pow(2, float64(p-1)))

			if z == 0 {
				res += int64(allways * allways)
			} else if z == 1 {
				res += int64(allways * onez)
			} else if z == 2 {
				res += int64(allways * twoz)
			}
		}
	}
	return
}

func count_zero(s []string) (res int) {
	for _, e := range s {
		if e == "0" {
			res++
		}
	}
	return
}

func convert_to_int(s []string) (res []int) {
	var tmp int
	for _, e := range s {
		tmp, _ = strconv.Atoi(e)
		res = append(res, tmp)
	}
	return
}
