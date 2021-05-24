package main

import (
	"fmt"
	"sort"
	"strconv"
)

func main() {
	fmt.Println(solve())
}

func solve() string {
	nums := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	res := []string{}

	for _, e := range permutations(nums) {
		res = append(res, join_slice(e))
	}
	sort.Strings(res)
	return res[999999]
}

func join_slice(s []int) string {
	res := ""
	for _, e := range s {
		res += strconv.Itoa(e)
	}
	return res
}

func permutations(arr []int) [][]int {
	var helper func([]int, int)
	res := [][]int{}

	helper = func(arr []int, n int) {
		if n == 1 {
			tmp := make([]int, len(arr))
			copy(tmp, arr)
			res = append(res, tmp)
		} else {
			for i := 0; i < n; i++ {
				helper(arr, n-1)
				if n%2 == 1 {
					tmp := arr[i]
					arr[i] = arr[n-1]
					arr[n-1] = tmp
				} else {
					tmp := arr[0]
					arr[0] = arr[n-1]
					arr[n-1] = tmp
				}
			}
		}
	}
	helper(arr, len(arr))
	return res
}
